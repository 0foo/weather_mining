import statistics, csv, os, glob
from pprint import pprint 


'''
dly file format
ID            1-11   Character
YEAR         12-15   Integer
MONTH        16-17   Integer
ELEMENT      18-21   Character


VALUE1       22-26   Integer
MFLAG1       27-27   Character
QFLAG1       28-28   Character
SFLAG1       29-29   Character


VALUE2       30-34   Integer
MFLAG2       35-35   Character
QFLAG2       36-36   Character
SFLAG2       37-37   Character
  .           .          .
  .           .          .
  .           .          .
VALUE31    262-266   Integer
MFLAG31    267-267   Character
QFLAG31    268-268   Character
SFLAG31    269-269   Character

'''

def parse_values(element, input_str):
    out_values = []
    while input_str:
        value=input_str[0:5].strip()
        quality=input_str[6:7]  
        input_str = input_str[8:]
        if quality.strip(): 
            continue
        if not value.strip():
            continue
        if int(value) == int(-9999): 
            continue
        # convert to more human readable as it's recorded in data in tenths
        if element in ["TMAX", "TMIN", "PRCP"]:
            value = int(value) / 10
        # convert temps to farenheight 
        if element in ["TMAX", "TMIN"]:
            value = (value * 1.8) + 32
        out_values.append(int(value))
    return out_values

def parse_line(input_str):
    out={}
    out["id"] = input_str[0:11]
    out["year"] = input_str[11:15]
    out["month"] = input_str[15:17]
    out["element"] = input_str[17:21]
    out["values"] = parse_values(out["element"], input_str[21:])
    out["key"] = out["id"] + out["month"] + out["element"]
    return out



def parse_dly_file(input_file, output_file):
    with open(input_file) as the_file:
        x = 0
        gather = {}
        gather_count = {}
        for line in the_file:
            data = parse_line(line)
            if data["element"] not in ["PRCP", "TMAX", "TMIN", "SNOW", "SNWD"]:
                continue
            if int(data["year"]) < 1980:
                continue
            if data["key"] not in gather:
                gather[data["key"]] = data["values"]
                gather_count[data["key"]] = len(data["values"])
            else:
                gather[data["key"]] += data["values"]
                gather_count[data["key"]] += len(data["values"])

        out = []
        for key,values in gather.items():
            if len(values) < 10:
                continue
            out_row = [
                key, # general unique key
                key[0:11],  # station id
                key[11:13], # month
                key[-4:], # element being measure
                round(statistics.mean(values), 2), # average of all values
                round(statistics.stdev(values), 2), # standard deviation of all values
                max(values), # max value of all values
                min(values), # min value of all values
                len(values) # total number of values used
            ]
            out.append(out_row)
        
        with open(output_file, "a") as out_file:
            write = csv.writer(out_file, quoting=csv.QUOTE_ALL)
            write.writerows(out)


def parse_dly_dir(input_dir, output_file):
    # were appending each iteration so to avoid duplication delete the file and start from scratch, living that idempotent life
    if os.path.isfile(output_file):
        os.remove(output_file)
    source_dir = input_dir + "/*.dly"
    files = glob.glob(source_dir)
    for the_file in files:
        parse_dly_file(the_file, output_file)


# for testing
# input_file = "source_data/ghcnd_hcn/USC00190535.dly"
# output_file = "output_data/final_data.csv"
# if os.path.isfile(output_file):
#     os.remove(output_file)
# parse_dly_file(input_file, output_file)

parse_dly_dir("./source_data/ghcnd_hcn", "./output_data/final_data.csv")


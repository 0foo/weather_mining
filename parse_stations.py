import csv, os

'''
USC00455224  47.1356 -122.2561  173.7 WA MCMILLIN RSVR                      HCN 



------------------------------
Variable   Columns   Type
------------------------------
ID            1-11   Character
LATITUDE     13-20   Real
LONGITUDE    22-30   Real
ELEVATION    32-37   Real
STATE        39-40   Character
NAME         42-71   Character
GSN FLAG     73-75   Character
HCN/CRN FLAG 77-79   Character
WMO ID       81-85   Character
------------------------------


'''

input_file = "./source_data/ghcnd-stations.txt"
output_file = "./output_data/ghcnd-us-stations.csv"

if os.path.isfile(output_file):
    os.remove(output_file)

with open(input_file, "r") as file:
    out = []
    for line in file:
        if line[0:2] not in ["US"]:
            continue
        data = line[0:41].split()
        data.append(line[41:72].strip())
        out.append(data)
    # print(out)

    with open(output_file, "a") as out_file:
            write = csv.writer(out_file, quoting=csv.QUOTE_ALL)
            write.writerows(out)

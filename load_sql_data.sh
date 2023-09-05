# create spell table from schema
sqlite3 ./output_data/weather.db < ./create_weather_tables.sql


# populate monthly table
sqlite3 ./output_data/weather.db <<EOF
.mode csv
.import ./output_data/final_data.csv monthly
EOF





# # output info
# echo "Rows in spells database:"
# sqlite3 DandD.db "SELECT COUNT(*) FROM spells"


# # create csv file 
# sqlite3 DandD.db <<EOF
# .mode csv
# .headers on
# .output ../format/spells.csv
# SELECT * FROM spells
# EOF

# # create html file
# rm ../format/spells.html
# python3 ./csv_to_html.py
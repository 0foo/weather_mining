# create weather tables from schema
sqlite3 ./output_data/weather.db < ./create_weather_tables.sql


# populate monthly table
sqlite3 ./output_data/weather.db <<EOF
.mode csv
.import ./output_data/final_data.csv monthly
EOF


# populate stations table
sqlite3 ./output_data/weather.db <<EOF
.mode csv
.import ./output_data/ghcnd-us-stations.csv stations
EOF

sqlite3 ./output_data/weather.db <<EOF
    DROP TABLE station_min_max;
    CREATE TABLE station_min_max AS select m_tmin.station, m_tmin.month, m_tmin.average as min, m_tmax.average as max  from monthly as m_tmin left join (select * from monthly where element="TMAX") as m_tmax on m_tmin.stationmonth=m_tmax.stationmonth  where m_tmin.element="TMIN";
EOF

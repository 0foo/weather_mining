## Weather mining


* This is working with ghncd daily data from NOAA
* This script parses the daily data down to monthy averages with standard devs and min/max
* Output options in csv format and sqlite format
* This is only US data for now 250ish megs compressed vs ~3ish gigs compressed
    * theoretically would work with the big global dataset

* Select the stations with the most months with low and high between 30 degrees and 75 degrees.

```
sqlite> select station,state,name,lat,long,count from stations join (select station, count(*) as count from station_min_max where min > 30 and max < 75 group by station) as cs on cs.station=stations.stationid where count > 6 order by count;


station|state|name|lat|long|number_of_month_count
....more
USC00352406|OR|DRAIN|43.6592|-123.325|8
USC00353445|OR|GRANTS PASS|42.4239|-123.3219|8
USC00357169|OR|RIDDLE|42.9508|-123.3572|8
USC00357331|OR|ROSEBURG|43.2142|-123.3256|8
USC00454764|WA|LONGMIRE RAINIER NPS|46.7492|-121.812|8
USW00013724|NJ|ATLANTIC CITY MARINA|39.3778|-74.4236|8
USW00093729|NC|CAPE HATTERAS - BILLY MITCHELL|35.2325|-75.6222|8
USC00047902|CA|SANTA BARBARA|34.4167|-119.6844|9
USC00351862|OR|CORVALLIS STATE UNIV|44.6342|-123.19|9
USC00351897|OR|COTTAGE GROVE 2E|43.7917|-123.0275|9
USC00352997|OR|FOREST GROVE|45.5247|-123.1025|9
USC00355384|OR|MC MINNVILLE|45.2214|-123.1622|9
USC00351433|OR|CASCADIA|44.3914|-122.4811|10
USC00353770|OR|HEADWORKS PORTLAND WTR B|45.4486|-122.1547|10
USC00358466|OR|THREE LYNX|45.1219|-122.07|10
USC00450945|WA|BUCKLEY 1 NE|47.1694|-122.0036|10
USC00451276|WA|CENTRALIA|46.72|-122.9528|10
USC00451484|WA|CLEARBROOK|48.9672|-122.3292|10
USC00451939|WA|CUSHMAN POWERHOUSE #2|47.3706|-123.16|10
USC00454769|WA|LONGVIEW|46.1372|-122.9781|10
USC00455224|WA|MCMILLIN RSVR|47.1356|-122.2561|10
USC00458773|WA|VANCOUVER 4 NNE|45.6775|-122.6514|10
USC00047916|CA|SANTA CRUZ|36.9878|-121.9994|11
USC00452675|WA|EVERETT|47.9753|-122.195|11
USC00457507|WA|SEDRO-WOOLLEY|48.4958|-122.2355|11
USC00457773|WA|SNOQUALMIE FALLS|47.5414|-121.8361|11
USC00040693|CA|BERKELEY|37.8744|-122.2606|12
USC00043161|CA|FT BRAGG 5 N|39.51|-123.7564|12
USC00046175|CA|NEWPORT BEACH HARBOR|33.6031|-117.8836|12
USC00351055|OR|BROOKINGS|42.0464|-124.2878|12
USC00358494|OR|TILLAMOOK|45.4539|-123.8519|12
USC00450008|WA|ABERDEEN|46.9658|-123.8292|12
USC00450587|WA|BELLINGHAM 3 SSW|48.7178|-122.5114|12
USC00450729|WA|BLAINE|48.9947|-122.7619|12
USC00451233|WA|CEDAR LAKE|47.4144|-121.7561|12
USC00452914|WA|FORKS 1 E|47.9558|-124.3539|12
USC00454748|WA|LONG BEACH EXP STN|46.3675|-124.0378|12
USC00456096|WA|OLGA 2 SE|48.6117|-122.8064|12
USC00456624|WA|PORT ANGELES|48.1139|-123.4317|12
USC00456678|WA|PORT TOWNSEND|48.1161|-122.7586|12
USC00456914|WA|RAYMOND 2 S|46.6533|-123.73|12
USW00024213|CA|EUREKA WFO WOODLEY IS|40.8097|-124.1603|12
USW00024281|WA|SEATTLE URBAN SITE|47.65|-122.3|12
USW00024284|OR|N BEND SW OREGON RGNL AP|43.4133|-124.2436|12
USW00024285|OR|NEWPORT|44.6431|-124.0556|12
USW00094224|OR|ASTORIA AP (PORT OF)|46.1569|-123.8833|12
```
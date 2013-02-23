"""
Write out crime data to javascript file.
Data from Town of Cary website: http://data.carync.gov/
Currently filtering all except 2013 crimes.
"""

import json

with open ("crime_data.js", "w") as out_file:
	with open("CRIME_ALL.csv") as in_file:
		in_file.readline()  # skip first line, which contains field names
		out_file.write("var crimes = [");
		for line in in_file:
			date, street, offense, lat, lng = line.strip().split(',')
			month, day, year = (int(part) for part in date.split('/'))
			crime = {
				"month": month,
				"day": day,
				"year": year,
				"street": street,
				"offense": offense,
				"lat": lat,
				"lng": lng
			}
			crime_json = json.dumps(crime)
			if year == 2013:
				out_file.write(crime_json + ",\n")
		out_file.write("];")
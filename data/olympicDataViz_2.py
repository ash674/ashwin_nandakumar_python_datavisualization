
import numpy as np
import csv
import matplotlib.pyplot as plt

year = [1924,1928,1932,1936,1948,1952,1956,1960,1964,1968,1972,1976,1980,1984,1988,1992,1994,1998,2002,2006,2010,2014]
year1 = []
year2 = []
year3 = []
year4 = []
year5 = []
year6 = []
year7 = []
year8 = []
year9 = []
year10 = []
year11 = []
year12 = []
year13 = []
year14 = []
year15 = []
year16 = []
year17 = []
year18 = []
year19 = []
year20 = []
year21 = []
year22 = []


categories = []

with open('data/OlympicsWinter - Sheet1.csv', encoding='ISO-8859-1') as csvfile:
	reader = csv.reader(csvfile)
	line_count = 0 

	for row in reader:
		if line_count is 0:
			print("this is the first row in spreadsheet")
			categories.append(row)
			line_count += 1
			
		else: 
			if row[5] == "Men":
				if row[0] == "1924":
					year1.append(row[0])
			
				elif row[0] == "1928":
					year2.append(row[0])
			
				elif row[0] == "1932":
					year3.append(row[0])					
			
				elif row[0] == "1936":
					year4.append(row[0])
			
				elif row[0] == "1948":
					year5.append(row[0])
			
				elif row[0] == "1952":
					year6.append(row[0])
			
				elif row[0] == "1956":
					year7.append(row[0])
				
				elif row[0] == "1960":
					year8.append(row[0])
			
				elif row[0] == "1964":
					year9.append(row[0])
			
				elif row[0] == "1968":
					year10.append(row[0])
			
				elif row[0] == "1972":
					year11.append(row[0])
				
				elif row[0] == "1976":
					year12.append(row[0])								

			
				elif row[0] == "1980":
					year13.append(row[0])

			
				elif row[0] == "1984":
					year14.append(row[0])		


				elif row[0] == "1988":
					year15.append(row[0])


				elif row[0] == "1992":
					year16.append(row[0])


				elif row[0] == "1994":
					year17.append(row[0])


				elif row[0] == "1998":
					year18.append(row[0])

				elif row[0] == "2002":
					year19.append(row[0])
				
				elif row[0] == "2006":
					year20.append(row[0])

				elif row[0] == "2010":
					year21.append(row[0])

				elif row[0] == "2014":
					year22.append(row[0])



			print(line_count)
			line_count += 1	



quantity = [len(year1), len(year2),len(year3),len(year4),len(year5),len(year6),len(year7),len(year8),len(year9),len(year10),len(year11),len(year12),len(year13),len(year14), len(year15),len(year16),len(year17),len(year18),len(year19),len(year20),len(year21), len(year22)]

plot = plt.bar(year, quantity)

for value in plot:
	height = value.get_height()
	plt.text(value.get_x() + value.get_width()/2.,1.002*height,'%d' % int(height), ha='center', va='bottom')



plt.title("Number of medals won by men each year (1924--2014)")
plt.ylabel("Number of medals")
plt.show()
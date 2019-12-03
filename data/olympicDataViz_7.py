import csv
import matplotlib.pyplot as plt


mentotal = []
men = []
womentotal = []
women = []
total = []
categories = []

with open('data/Olympics-Winter.csv') as csvfile:
		reader = csv.reader(csvfile)
		line_count = 0 

		for row in reader:
			if line_count is 0:
				print("this is the first row in spreadsheet")
				categories.append(row)
				line_count += 1
			
			else:
				if row[4] == "CAN":	
					if row[5] == "Men":
						mentotal.append(row[0])

					else:
						womentotal.append(row[0])	

				print(line_count)
				line_count = 1	



labels = ["Men", "Women"]
total = [len(mentotal), len(womentotal)]
color = ['Blue', 'green']
explode = (0.02, 0.02)

plt.pie(total, explode=explode, colors=color, autopct='%.1f%%', shadow=True, startangle=140)

plt.axis('equal')

plt.legend(labels, loc=1)
plt.title("Comparison Between the number of medals won by Men and Women")
plt.show()
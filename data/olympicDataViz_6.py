import csv
import matplotlib.pyplot as plt

golds = []
silvers = []
bronzes = []

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
					if row[7] == "Gold":
						print("won a gold medal")
						golds.append(row[7])	

					elif row[7] == "Silver":
						print("won a silver medal")	
						silvers.append(row[7])

					else:
						print("won a bronze medal")
						bronzes.append(row[7])

				print(line_count)
				line_count = 1	

print(len(golds))
print(len(silvers))
print(len(bronzes))

labels = ["Gold", "Silver", "Bronze"]
sizes = [len(golds), len(silvers), len(bronzes)]
color = ['gold', 'silver', 'darkgoldenrod']
explode = (0.02, 0.02, 0.02)

plt.pie(sizes, explode=explode, colors=color, autopct='%.1f%%', shadow=True, startangle=140)

plt.axis('equal')

plt.legend(labels, loc=1)
plt.title("Percentage Of Gold, Silver, Bronze medals won by Canada (1924-2014)")
plt.show()
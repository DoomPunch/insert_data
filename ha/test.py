import csv
import numpy as np

aa = list(np.random.normal(22.10442873, 12.27877745, 1000))


file = open('good.csv', 'w', newline='', encoding='utf-8')
csv_writer = csv.writer(file)
for i in aa:
    print(float(i))
    csv_writer.writerow([i])
file.close()

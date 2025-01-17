import csv 
vegetables = [
 {"name": "eggplant", "color": "purple"},
 {"name": "tomato", "color": "red"},
 {"name": "corn", "color": "yellow"},
 {"name": "okra", "color": "green"},
 {"name": "arugula", "color": "green"},
 {"name": "broccoli", "color": "green"},
]
with open('vegetables.csv', 'w') as f:
 writer = csv.writer(f)
 writer.writerow(['name', 'color' 'length'])
 for vegetable in vegetables:
     name = vegetable['name']
     color = vegetable['color']
     length = len(vegetable['name'])
     writer.writerow([name, color, length])


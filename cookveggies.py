import csv
import json
import os

# Ensure the output directory exists
os.makedirs('output', exist_ok=True)

# Read the CSV file into a variable called vegetables
vegetables = []
with open('output/vegetables.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        vegetables.append({"name": row["name"], "color": row["color"], "length": len(row["name"])})

# Print the variable vegetables
print(vegetables)

# Write vegetables as a JSON file
with open('output/vegetables.json', 'w') as jsonfile:
    json.dump(vegetables, jsonfile, indent=2)
with open('name.txt', 'r') as f:
    my_name = f.read().strip()
with open('output/hello.txt', 'w') as f:
    f.write(f'Hello, {my_name}!')
import csv
import csv

with open('testwrite.csv', 'r') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

print(rows)

with open('testwrite.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['col1', 'col2'])
    writer.writerow(['val1', 'val2'])
    writer.writerow(['val1', 'val2'])
    writer.writerow(['val1', 'val2'])


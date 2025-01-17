with open('name.txt', 'r') as f:
    my_name = f.read().strip()
with open('output/hello.txt', 'w') as f:
    f.write(f'Hello, {my_name}!')


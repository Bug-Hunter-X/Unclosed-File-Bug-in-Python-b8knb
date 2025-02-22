def function_with_closed_file(filename):
    try:
        with open(filename, 'r') as file:
            # ... some code that processes the file ...
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
def function_with_unclosed_file(filename):
    file = open(filename, 'r')
    # ... some code that processes the file ... 
    # Forgot to close the file!
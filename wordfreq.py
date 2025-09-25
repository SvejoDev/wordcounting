def tokenize(lines):
    words = []
    for line in lines:
        start = 0
        while start < len(line): 
            while line[start].isspace():
                start = start +1
            while line[start].isdigit():
                if line[start]
            elif line[start].isalpha():
                print (f"{line[start]} is a letter")
            else:
                print (f"{line[start]} is a letter")
            start = start +1
    return words
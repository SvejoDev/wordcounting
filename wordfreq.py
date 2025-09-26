def tokenize(lines):
    words = []
    for line in lines:
        start = 0
        while start < len(line):
            while start < len(line) and line[start].isspace():
                start += 1
            if start >= len(line):
                break
            if line[start].isdigit():
                end = start
                while end < len(line) and line[end].isdigit():
                    end += 1
                words.append(line[start:end])
                start = end
            elif line[start].isalpha():
                end = start
                while end < len(line) and line[end].isalpha():
                    end += 1
                words.append(line[start:end].lower())
                start = end
            else:
                words.append(line[start])
                start += 1
    return words

def countWords(words, stopWords):
    frequencies = {}
    for word in words:
        if word not in stopWords:
            if word not in frequencies:
                frequencies[word] = 1
            else:
                frequencies[word] += 1
    return frequencies

def printTopMost(frequencies,n):
    sort = dict(sorted(frequencies.items(), key = lambda item: item[1], reverse = True))
    for word, count in sort.items():
        print(word.ljust(20),str(count).rjust(5))




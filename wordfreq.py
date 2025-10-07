def tokenize(lines): 
    # Tokenize is a function that takes in a list from sys.argv
    # After taking in the list it goes through every line and seperates each symbol, word and number
    words = []
    for line in lines:
        start = 0
        while start < len(line):
            while start < len(line) and line[start].isspace():
                # If its a space we jump to the next symbol
                start += 1
            if start >= len(line):
                break
            if line[start].isdigit():
                # If its a digit it goes through it
                end = start
                while end < len(line) and line[end].isdigit():
                    end += 1
                words.append(line[start:end])
                start = end
            elif line[start].isalpha():
                # If its a letter it goes through it
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
    # countWords is the function that counts how often words occur
    frequencies = {}
    for word in words:
        if word not in stopWords:
            if word not in frequencies:
                # if the word doesnt exist, we add to a dictionairy
                frequencies[word] = 1
            else:
                # if the word already exist, we add 1 to the dictionary
                frequencies[word] += 1
    return frequencies

def printTopMost(frequencies,n):
    # printTopMost is the function that prints and sorts each word and freq in a dictioanry
    sort_freq = dict(sorted(frequencies.items(), key = lambda item : item[1], reverse = True))
    # we use key = lambda to sort it and reverse = True to reverse the dictionary
    for word, freq in list(sort_freq.items())[:n]:
        print(word.ljust(20) + str(freq).rjust(5))
        # prints the dictionary
    
            
        
        




freq = {'word' : 9, 'words' : 2, 'wrong' : 4, "filipola" : 30}

sorterad = dict(sorted(freq.items(), key = lambda item: item[1], reverse = True))

for word, count in sorterad.items():
    print(word.ljust(20),str(count).rjust(5))
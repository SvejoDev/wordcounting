words = ["apple", "banana", "apple", "orange", "banana", "apple", "12","12","/"]

# Initialize an empty dictionary
word_count = {}

stop_words = ["banana"]

for word in words:
    if word not in stop_words:
    # Increment the count for each word
        if word  in word_count:
            word_count[word] += 1
        else:   
            word_count[word] = 1

# Output the resulting dictionary
print(word_count)
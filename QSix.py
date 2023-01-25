# How many unique words have been used in the sentence? Use the split methods and set
# to get the unique words

# example string
exmpStr = "I am a teacher and I love to inspire and teach people"

# splitting the string
split = exmpStr.split(" ")

# list to hold the unique words
u_words = []

# for loop to loop through string and append words that appear once into the list
for word in split:
    if word not in u_words:
        u_words.append(word)
    else:
        continue

print(u_words)
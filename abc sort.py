my_str = "hello this is an example of cased Letter"
words = [word.lower() for word in my_str.split()]
words.sort()

print("Sorted words are:")
for word in words:
    print(word)

def solve(text):
    
    
# Split the text into words
    words = text.split()

# Create a dictionary to store the frequency of each word
    word_freq = {}

# Iterate over each word in the text
    for word in words:
    # Update the frequency count for the current word
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1

# Find the word with the maximum frequency
    max_word = None
    max_freq = 0
    for word, freq in word_freq.items():
        if freq > max_freq:
            max_word = word
            max_freq = freq

# Output
    print(max_word, max_freq)



"""Count words in file."""


def word_count(file):
    file_name = open(file)
    word_dict = {}
    for line in file_name:
        line = line.strip()
        for word in line.split(' '): 
            if word not in word_dict:
                word_dict[word] = word_dict.get(word, 0) + 1 
            else:
                word_dict[word] += 1
        
    for word, count in word_dict.items():
       print(word, count)

word_count('twain.txt')


# -------------------------

"""Count words in file."""

input_file = open("test.txt")

word_counts = {}

for line in input_file:
    # Remove trailing whitespace at the end of each line
    line = line.rstrip()

    # Split the line by spaces to get a list of words
    words = line.split()

    for word in words:
        # Set the word count to whatever it was + 1; if it wasn't found at all,
        # we'll use `.get(word, 0)` to return 0 if the word wasn't already in
        # the dictionary
        word_counts[word] = word_counts.get(word, 0) + 1

for word, count in word_counts.items():
    print(word, count)
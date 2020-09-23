import random

# Read in all the words in one go
with open("applications/markov/input.txt") as f:
    words = f.read()

# TODO: analyze which words can follow other words
# Your code here
split_words = words.split()
words_dict = {}
start_words = []
stop_words = []
result = ''

for i in range(len(split_words) - 1):
    current = split_words[i]
    if current in words_dict:
        words_dict[current].append(f'{split_words[i + 1]}')
    else:
        words_dict[current] = [split_words[i + 1]]

for word in split_words:
    if word[0] == word[0].upper():
        start_words.append(word)
    if word[0] == '"' and word[1] == word[1].upper():
        start_words.append(word)

for word in split_words:
    if word[len(word) - 1] == '.' or word[len(word) - 1] == '?' or word[len(word) - 1] == '!':
        stop_words.append(word)
    if word[len(word) - 1] == '"' and word[len(word) - 2] == '.' or word[len(word) - 2] == '?' or word[len(word) - 2] == '!':
        stop_words.append(word) 

add_word = random.choice(start_words)
result += (f'{add_word} ')

while add_word not in stop_words:
    if add_word[len(add_word) - 1] == '.' or add_word[len(add_word) - 1] == '?' or add_word[len(add_word) - 1] == '!':
        result += (f'{add_word} ')
        print(result)
        break
    if add_word[len(add_word) - 1] == '"' and add_word[len(add_word) - 1] == '.' or add_word[len(add_word) - 1] == '?' or add_word[len(add_word) - 1] == '!':
        result += (f'{add_word} ')
        print(result)
        break
    add_word = random.choice(words_dict[add_word])
    result += (f'{add_word} ')
        
print(result)

# TODO: construct 5 random sentences
# Your code here


'''
U
Input -> text file
Output -> words from text file in weird order

Tasks:
    Split text into words
    *capitalization doesn't matter
    Save words to a data structure as keys, with values being what can follow the word
    *leave duplicate values

    Choose random word to start with
        Must start with capital letter, or " and a capital letter
    Print word to console
    If word is a stop word, stop
        Stop word ends with .?! or " followed by same punctuation
    If word is not stop word
        Choose a word that can follow preceding word (according to values)
        Repeat process
'''
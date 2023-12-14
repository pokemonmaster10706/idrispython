sentence = input('enter a sentence: \n\n')
word = input('enter a word: ')
sentence = sentence.split()

if word in sentence:
    count = 0
    for i in sentence:
        if i == word:
            count += 1
    print(f'the word {word} appears in the sentence {count} times.')
else:
    print(f'the word {word} does not appear in the string')
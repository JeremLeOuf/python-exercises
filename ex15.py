sentence = input('Input the sentence to be reversed: ')

def reverse(sentence):
    splitted = sentence.split()
    return ' '.join(splitted[::-1])

print(reverse(sentence))


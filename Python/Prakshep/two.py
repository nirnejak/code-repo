import nltk
lst = []
# Receive the first sentence from first script
sentence = "At eight o' clock on morning I am feeling very pleased"
tokens = nltk.word_tokenize(sentence)
tokens
tagged = nltk.pos_tag(tokens)
lst = tagged[0:len(sentence)]

print(lst)
# Store the lst in database

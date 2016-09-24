__author__ = 'arvid'

# This is the Codecadamy code for a function that censors words of your chosing

import string
def censor(text, word):

    text = string.split(text)

    m = 0
    for a in text:
        if(a == word):
            text[m] = "*" * len(word)
        m += 1

    text = " ".join(text)
    print (text)

censor("this is a test sentence for censor! test is what its about, test.", "test")

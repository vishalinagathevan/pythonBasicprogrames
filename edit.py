import re

def getWords(s,t):
    pattern = r'''(?ix)           # ignore case, verbose mode
                  \b{letter}      # start with letter
                  \w*             # zero or more additional word characters
                  [^{letter}\W]\b # ends with a word character that isn't letter
                  |               #    OR
                  \b[^{letter}\W] # does not start with a non-word character or letter
                  \w*             # zero or more additional word characters
                  {letter}\b      # ends with letter
                  '''.format(letter=t)
    return re.findall(pattern,s)

s = "The TART program runs on Tuesdays and Thursdays, but it does not start until next week."
print(getWords(s,'t%'))
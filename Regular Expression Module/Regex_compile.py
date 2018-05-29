import re

# Pre-compile the patterns
regexes = [ re.compile(p) for p in [ 'the',
                                     'this',
                                     'that',
                                     'easy'
                                     ]
            ]
text = 'welcome to the python world this is easy programmimg language'

for regex in regexes:
    print ('Looking for "%s" in "%s" ->' % (regex.pattern, text),)

    if regex.search(text):
        print ('found a match!')
    else:
        print ('no match')
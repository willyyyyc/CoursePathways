import re

#plan:
#break line into list of characters
#goal: a list of course title objects to fill an adjacency list. some entries in list will themselves be lists, representing optional ('or' prerequisites)

#change to re for each token
faculty = re.compile('^[A-Z]{4}$')
code = re.compile('^[0-9]{4}')
or_re = re.compile('or')
and_re = re.compile('and')
#need to separated the braces from the tokens
left_brace = re.compile('\(')
right_brace = re.compile('\)')

#heading = re.compile('Course Descriptions')
#csci = re.compile('^CSCI\\s\\d{4}\\s[a-zA-Z]+')
with open('test.txt', 'r') as f:
    for line in f:
        l = line.rsplit()
        bracesplit = re.compile('(\\()|(\\))').split
        l = [part for word in l for part in bracesplit(word) if part]
        print('->', l)
        if 'None' in l:
            print(l)
        else:
            for word in l:
                m = faculty.match(word)
                n = code.match(word)
                o = or_re.match(word)
                a = and_re.match(word)
                l = left_brace.match(word)
                r = right_brace.match(word)
                if m or n or o or a or l or r:
                    print(word)

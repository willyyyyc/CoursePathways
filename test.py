import re

#plan:
#break line into list of characters
#goal: a list of course title objects to fill an adjacency list. some entries in list will themselves be lists, representing optional ('or' prerequisites)

def remove_item(list, item):
    return [i for i in list if i != item]

none = re.compile('None')
faculty = re.compile('^[A-Z]{4}$')
code = re.compile('^[0-9]{4}')
or_re = re.compile('or')
and_re = re.compile('and')
left_brace = re.compile('\(')
right_brace = re.compile('\)')

with open('test.txt', 'r') as f:
    for line in f:
        l = line.rsplit()
        bracesplit = re.compile('(\\()|(\\))').split
        l = [part for word in l for part in bracesplit(word) if part]
        print('->', l)

        #x = [word for word in l if word != ('PREREQUISITES:')]
        l = remove_item(l, 'PREREQUISITES:')
        l = remove_item(l, ',')

        broken_code_0 = re.compile('^[0-9]{3}$')
        broken_code_1 = re.compile('^[0-9]')
        #iter_l = iter(l)
        #l = [i + next(iter_l, '') for i in iter_l if broken_code.match(i)]

        # Assumes one occurence
        i = 0
        while i < len(l) - 1:
            if broken_code_0.match(l[i]) and broken_code_1.match(l[i + 1]):
                l[i] = l[i] + l[i + 1]
                l.pop(i + 1)
                break
            i += 1


        patterns = [none, faculty, code, or_re, and_re, left_brace, right_brace]
        matches = [word for word in l if any(pattern.match(word) for pattern in patterns)]
        for match in matches:
            #make course title item
            l.remove(match)

        print('->', l)

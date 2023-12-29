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

broken_line = ['PREREQUISITES:', 'CSCI', '1300', 'or', 'MATH', '1000', 'or', 'MATH', '1280', ')', 'and', '(', 'CSCI', '1105', 'or', 'CSCI', '1110', 'or', 'CSCI', '1503', 'or', 'CSCI', '2202', ')']

with open('test.txt', 'r') as f:
    for line in f:
        l = line.rsplit()
        bracesplit = re.compile('(\\()|(\\))').split
        l = [part for word in l for part in bracesplit(word) if part]
        #print('->', l)
        print(l)
        if l == broken_line:
            l.insert(1, "(")
        #x = [word for word in l if word != ('PREREQUISITES:')]
        l = remove_item(l, 'PREREQUISITES:')
        l = remove_item(l, ',')


        broken_code_0 = re.compile('^\\d{3}$')
        broken_code_1 = re.compile('^\\d')
        broken_code_2 = re.compile('^CSCI\\d{4}')
        broken_code_3 = re.compile('^\\d$')
        #iter_l = iter(l)
        #l = [i + next(iter_l, '') for i in iter_l if broken_code.match(i)]
        print(l)

        # Assumes one occurence
        i = 0
        while i < len(l) - 1:
            if broken_code_0.match(l[i]) and broken_code_1.match(l[i + 1]):
                l[i] = l[i] + l[i + 1]
                l.pop(i + 1)
                break
            i += 1

        i = 0
        while i < len(l) - 1:
            if l[i] == 'CSC':
                l[i] = l[i] + l[i + 1]
                l.pop(i + 1)
                break
            i += 1

        i = 0
        while i < len(l) - 1:
            if l[i] == 'CSCi':
                l[i] = 'CSCI'
                break
            i += 1

        i = 0
        while i < len(l) - 1:
            if broken_code_2.match(l[i]):
                l.insert(i + 1, l[i].replace('CSCI', ""))
                l[i] = 'CSCI'
                break
            i += 1

        i = 0
        while i < len(l) - 1:
            if l[i] == 'MA':
                l[i] = l[i] + l[i + 1]
                l.pop(i + 1)
                break
            i += 1

        i = 0
        while i < len(l) - 1:
            if broken_code_3.match(l[i]):
                l.pop(i + 1)
                break
            i += 1

        patterns = [none, faculty, code, or_re, and_re, left_brace, right_brace]
        matches = [word for word in l if any(pattern.match(word) for pattern in patterns)]
        for match in matches:
            l.remove(match)

        print(matches)
        print('->', l)

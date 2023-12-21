offset = 0
start_page = -1
end_page = -1
start_found = False
sublist = ['Faculty', 'Computer', 'Science']

with open('files/table_of_contents.txt', 'r') as f:
    for line in f:
        li = list(line.split())
        if start_found:
            if 'Faculty' in li:
                for word in li:
                    try:
                        end_page = int(word)
                    except ValueError:
                        continue
                break
        else:
            if set(sublist).intersection(set(li)) == set(sublist):
                for word in li:
                    try:
                        start_page = int(word)
                    except ValueError:
                        continue
                start_found = True

print(start_page)
print(end_page)

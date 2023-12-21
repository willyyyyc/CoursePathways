file = open('test.txt', 'r')

DEFAULT = -1
first_line = file.readline()
print(first_line)
characters = list(first_line.split())
print(characters)

page_num = DEFAULT
for word in characters:
    try:
        page_num = int(word)
    except ValueError:
        continue


print(page_num)


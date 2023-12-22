import re
from Course import Course

courses = []
codes = []

heading = re.compile('Course Descriptions')
csci = re.compile('^CSCI\\s\\d{4}\\s[a-zA-Z]+')
prereq = re.compile('^PREREQUISITES:')
start_of_courses = False
with open('test.txt', 'r') as f:
    for line in f:
        m = heading.match(line)
        if m:
            start_of_courses = True
        if start_of_courses:
            n = csci.match(line)
            x = prereq.match(line)
            if n:
                title = list(line.split())
                s = ' '
                name = s.join(title[2:])
                code = title[1]
                courses.append(Course(code, name))
            elif x:
                courses[len(courses)-1].set_prerequisites(line.rstrip())

for course in courses:
    print(course.course_code, course.course_name, course.course_prerequisites)
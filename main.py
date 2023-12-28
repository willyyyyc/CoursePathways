import re
from FileGenerator import FileGenerator
from Course import Course
from CourseTitle import CourseTitle
from Graph import Graph


def get_page_range():
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

    return start_page, end_page


file_generator = FileGenerator()
page_range = get_page_range()
file_generator.file_from_page_range(page_range[0], page_range[1])


courses = []
codes = []

heading = re.compile('Course Descriptions')
csci = re.compile('^CSCI\\s\\d{4}\\s[a-zA-Z]+')
prereq = re.compile('^PREREQUISITES:')
start_of_courses = False
with open('files/faculty_cs.txt', 'r') as f:
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
                code = s.join(title[:2])
                new_title = CourseTitle(code, name)
                new_course = Course(new_title)
                courses.append(new_course)
            elif x:
                str_prereq = line.rstrip()
                # note: figure out how to split into course_title objects
                courses[len(courses)-1].set_prerequisites(str_prereq)

graph = Graph()
for course in courses:
    graph.add_edge(course.get_info(), course.get_prerequisites())
    print(course.get_prerequisites())

#print(graph.get_size())
#graph.print_graph()

#note: when getting prerequisites, need to make sure that it checks for the case where text flows to next line

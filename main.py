import re
import os
from FileGenerator import FileGenerator
from Course import Course
from CourseTitle import CourseTitle
from Graph import Graph
from TokenStreamBuilder import TokenStreamBuilder


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
check_uppercase = re.compile('^[a-z]')
start_of_courses = False
has_prereq = False
with open('files/faculty_cs.txt', 'r') as f:
    for line in f:
        m = heading.match(line)
        if m:
            start_of_courses = True
        if start_of_courses:
            n = csci.match(line)
            x = prereq.match(line)

            if has_prereq and check_uppercase.match(line):
                wrapped_line = line.rstrip()
                new_prereq = str_prereq + ' ' + wrapped_line
                courses[len(courses)-1].set_prerequisites(new_prereq)
            has_prereq = False
            if n:
                title = list(line.split())
                s = ' '
                name = s.join(title[2:])
                code = s.join(title[:2])
                new_title = CourseTitle(code, name)
                new_course = Course(new_title)
                courses.append(new_course)
            elif x:
                has_prereq = True
                str_prereq = line.rstrip()
                courses[len(courses)-1].set_prerequisites(str_prereq)

prereq_exists = os.path.isfile('files/raw_prerequisites.txt')
graph = Graph()
for course in courses:
    graph.add_edge(course.get_info(), course.get_prerequisites())
    if not prereq_exists:
        with open('files/raw_prerequisites.txt', 'a') as prereqs:
            try:
                prereqs.write(course.get_prerequisites() + '\n')
            except TypeError:
                prereqs.write('None\n')

builder = TokenStreamBuilder('files/raw_prerequisites.txt')
builder.build_token_stream()

#print(graph.get_size())
#graph.print_graph()

#note: when getting prerequisites, need to make sure that it checks for the case where text flows to next line
# extra field in course called special requirements? or additional? and have it be everything leftover after creating prereq list

#new steps:
#build the graph AFTER the token stream is complete.
#the course prerequisite field will be updated with final list repr. of prerequisites
#finally, graph is created

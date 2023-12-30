import re
import os
from FileGenerator import FileGenerator
from Course import Course
from CourseTitle import CourseTitle
from TokenStreamBuilder import TokenStreamBuilder
from CourseNetwork import CourseNetwork
from pyvis.network import Network


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

for course in courses:
    if not prereq_exists:
        with open('files/raw_prerequisites.txt', 'a') as prereqs:
            try:
                prereqs.write(course.get_prerequisites() + '\n')
            except TypeError:
                prereqs.write('None\n')

builder = TokenStreamBuilder('files/raw_prerequisites.txt')
all_token_streams = builder.build_token_stream()

# update course prerequisites to token streams
for course, token_stream in zip(courses, all_token_streams):
    course.set_prerequisites(token_stream)
    #print(course.get_info(), '\n', course.get_prerequisites(), '\n')

course_network = CourseNetwork()
graph = course_network.build_graph(courses)

#graph.print_graph()
course_network.display_network()

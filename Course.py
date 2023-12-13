#course class
class Course:
    def __init__(self, course_code, course_name, course_description):
        self.course_code = course_code
        self.name = course_name
        self.description = course_description
        self.prerequisites =
class Course:
    def __init__(self, course_code, course_name, course_prerequisites=None):
        self.course_code = course_code
        self.course_name = course_name
        self.course_prerequisites = course_prerequisites

    def set_prerequisites(self, course_prerequisites):
        self.course_prerequisites = course_prerequisites

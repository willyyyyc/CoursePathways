class Course:
    def __init__(self, course_code, course_name, course_prerequisites=None):
        if course_prerequisites is None:
            course_prerequisites = ['No prerequisites']
        self.course_code = course_code
        self.course_name = course_name
        self.course_prerequisites = course_prerequisites

    def set_prerequisites(self, course_prerequisites):
        self.course_prerequisites = course_prerequisites

    def get_info(self):
        return self.course_code + " " + self.course_name

    def get_prerequisites(self):
        return self.course_prerequisites

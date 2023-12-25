class Course:
    def __init__(self, course_title, course_prerequisites=None):
        self.course_title = course_title
        self.course_prerequisites = course_prerequisites

    def set_prerequisites(self, course_prerequisites):
        self.course_prerequisites = course_prerequisites

    def get_info(self):
        return self.course_title

    def get_prerequisites(self):
        return self.course_prerequisites

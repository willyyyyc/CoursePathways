class CourseTitle:
    def __init__(self, course_code, course_name):
        self.course_code = course_code
        self.course_name = course_name

    def __str__(self):
        return f"{self.course_code} {self.course_name}"

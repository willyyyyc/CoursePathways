class CourseTitle:
    """Outlines CourseTitle object.

    Attributes:
        course_code (str): The course code of the course, 'CSCI xxxx'
        course_name (str): The course name

    Methods:
        __str__(self): Returns the course code and course name
        __repr__(self): Returns the course code and course name
    """
    def __init__(self, course_code, course_name):
        """Inits CourseTitle object.

        Args:
            course_code (str): course code
            course_name (str): course name

        Returns:
              CourseTitle object
        """
        self.course_code = course_code
        self.course_name = course_name

    def __str__(self):
        """Returns course code and course.

        Used for an 'informal' string representation of the object.

        Returns:
            String representation of CourseTitle object
        """
        return f"{self.course_code} {self.course_name}"

    def __repr__(self):
        """Returns course code and course.

        Used when printing lists containing the object.

        Returns:
            String representation of CourseTitle object
        """
        return f"{self.course_code} {self.course_name}"

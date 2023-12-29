from CourseTitle import CourseTitle
class Course:
    """This class describes a course object

    Attributes:
        course_title (CourseTitle): title of course containing code and name
        course_prerequisites (CoursePrerequisites): a list of CourseTitle objects

    Methods:
        set_prerequisites(self, course_title, course_prerequisites):
            sets course_prerequisites to course_prerequisites

        get_info(self):
            returns course title

        get_prerequisites(self):
            returns course prerequisites
    """
    def __init__(self, course_title, course_prerequisites=None):
        """Constructor method.

        Args:
            course_title (CourseTitle): instance of CourseTitle, containing course code and name
            course_prerequisites (None): list of CourseTitle objects set to None
        """
        self.course_title = course_title
        self.course_prerequisites = course_prerequisites

    def set_prerequisites(self, course_prerequisites):
        """Sets course_prerequisites to list of CourseTitle objects.

        Args: course_prerequisites (CoursePrerequisites): list of CourseTitles

        Returns: void
        """
        self.course_prerequisites = course_prerequisites

    def get_info(self):
        """Return course title.

        Returns: course title
        """
        return self.course_title

    def get_prerequisites(self):
        """Return prerequisites.

        Returns: prerequisites
        """
        return self.course_prerequisites

from typing import Union
from CourseTitle import CourseTitle


class Token:
    """Token object.

    The TokenStreamBuilder object creates a Token object for valid strings in the input file.

    Attributes:
        value(Union[str, CourseTitle]): The value for the Token
    """
    def __init__(self, value: Union[str, CourseTitle]):
        self.value = value

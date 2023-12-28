import requests
from pypdf import PdfReader
import os


class FileGenerator:
    """This class is responsible for the generation and handling the pdf containing academic calendar.

    Attributes:
        response (Response): HTTP response from Dalhousie page containing academic calendar
        reader (PdfReader): Pdf reader that allows to parse the pdf and access specific pages

    Methods:
        print_page(self, page_num):
            Prints a specific page in the pdf

        create_table_of_contents(self):
            Creates new txt file containing table of contents of academic calendar from page range

        file_from_page_range(self, page_start, page_end):
            Creates new txt file containing content within a given page range of the pdf
    """
    def __init__(self):
        """Constructor for FileGenerator"""
        self.response = (requests.get
                         ('https://cdn.dal.ca/content/dam/dalhousie/pdf/academics/academiccalendar'
                          '/UG_2223_FullCalendar.pdf'))
        pdf_exists = os.path.isfile('files/dal_ug_full_academic_calendar.pdf')
        if not pdf_exists:
            with open('/files/dal_ug_full_academic_calendar.pdf', 'wb') as f:
                f.write(self.response.content)
        self.reader = PdfReader('files/dal_ug_full_academic_calendar.pdf')
        table_of_contents_exists = os.path.isfile('files/table_of_contents.txt')
        if not table_of_contents_exists:
            self.create_table_of_contents()

    def print_page(self, page_num):
        """Prints a specific page in pdf.

        Args:
            page_num (int): Page number

        Returns:
            void
        """
        print(self.reader.pages[page_num].extract_text())

    def create_table_of_contents(self):
        """Creates new txt file containing table of contents.

        Returns:
            txt file containing table of contents
        """
        with open('files/table_of_contents.txt', 'w') as f:
            page_count = 1
            while page_count < 6:
                text = self.reader.pages[page_count].extract_text()
                f.write(text)
                page_count += 1

    def file_from_page_range(self, page_start, page_end):
        """Creates txt file representing a page range of the pdf

        Args:
            page_start (int): integer representing the start of the page range
            page_end (int): integer representing the end of the page range

        Returns:
            txt file representing a page range of the pdf
        """
        faculty_file_exists = os.path.isfile('files/faculty_cs.txt')
        if not faculty_file_exists:
            with open('files/faculty_cs.txt', 'w') as f:
                page_count = page_start
                while page_count < page_end:
                    text = self.reader.pages[page_count].extract_text()
                    f.write(text)
                    page_count += 1

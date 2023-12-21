import requests
from pypdf import PdfReader

class FileGenerator:
    def __init__(self):
        self.response = requests.get('https://cdn.dal.ca/content/dam/dalhousie/pdf/academics/academiccalendar/UG_2223_FullCalendar.pdf')

    def generate_pdf(self):
        with open('files/dal_ug_full_academic_calendar.pdf', "wb") as f:
            f.write(self.response.content)
        print('pdf file created...')

        reader = PdfReader('files/dal_ug_full_academic_calendar.pdf')
        print('pdf reader created...')

        calendar_file = open('files/dal_ug_calendar.txt', 'w')

        print('Writing to txt file...')
        for page in reader.pages:
            text = page.extract_text()
            calendar_file.write(text)

        print('Successfully generated pdf file and txt file.')

    def print_page(self, page_num):
        reader = PdfReader('files/dal_ug_full_academic_calendar.pdf')
        print(reader.pages[page_num].extract_text())
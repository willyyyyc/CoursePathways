import requests
from pypdf import PdfReader

response = requests.get('https://cdn.dal.ca/content/dam/dalhousie/pdf/academics/academiccalendar/UG_2223_FullCalendar.pdf')
with open('dal_ug_full_academic_calendar.pdf', "wb") as f:
    f.write(response.content)

reader = PdfReader('dal_ug_full_academic_calendar.pdf')
print('PDF length (number of pages): ',len(reader.pages))
print('Test: Print text on page 0')
page = reader.pages[0]
text = page.extract_text()
print(text)
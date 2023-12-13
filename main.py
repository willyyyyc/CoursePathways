import requests
from pypdf import PdfReader

response = requests.get('https://cdn.dal.ca/content/dam/dalhousie/pdf/academics/academiccalendar/UG_2223_FullCalendar.pdf')
with open('dal_ug_full_academic_calendar.pdf', "wb") as f:
    f.write(response.content)

reader = PdfReader('dal_ug_full_academic_calendar.pdf')

calendar_file = open('dal_ug_calendar.txt', 'w')

for page in reader.pages:
    text = page.extract_text()
    calendar_file.write(text)
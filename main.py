from FileGenerator import FileGenerator

file_generator = FileGenerator()

try:
    file = open('files/dal_ug_calendar.txt', 'r')
except IOError:
    file_generator.generate_pdf()
    print('Required file did not exist so it was generated.')


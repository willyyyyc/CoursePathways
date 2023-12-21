import os
class CheckFile:
    def __init__(self):
        self.pdf_present = True
        try:
            open('files/dal_ug_full_academic_calendar.pdf', 'r')
        except FileNotFoundError:
            self.pdf_present = False
        self.txt_present = True
        try:
            open('files/dal_ug_calendar.txt', 'r')
        except FileNotFoundError:
            self.txt_present = False

    def check_files(self):
        return (self.pdf_present, self.txt_present)

    def remove_files(self):
        try:
            os.remove('files/dal_ug_full_academic_calendar.pdf')
            os.remove('files/dal_ug_calendar.txt')
        except OSError as e:
            print(f'Error while removing {e.filename}')
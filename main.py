from FileGenerator import FileGenerator
from CheckFile import CheckFile

file_generator = FileGenerator()
file_checker = CheckFile()
check = file_checker.check_files()
if not check[0]:
    print('Required file did not exist so it was generated.')
    file_generator.generate_pdf()


file_generator.print_page(3)
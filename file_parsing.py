import pandas as pd, re
#Inspired by blogpost https://www.vipinajayakumar.com/parsing-text-with-python/
#and accompanying stackoverflow thread https://stackoverflow.com/questions/47982949/how-to-parse-complex-text-files-using-python/47984221#47984221
rx_cell = re.compile(r'''
    ^
    CELL\s*(?P<cell_name>.+)
    (?P<cell_content>[\s\S]+?)
    (?=^CELL|\Z)
''', re.MULTILINE | re.VERBOSE)

rx_spots = re.compile(r'''
    ^
    SPOTS\s*(?P<spots>.+)
    (?P<spots_content>[\s\S]+?)
    (?=^CELL|\Z)
''', re.MULTILINE | re.VERBOSE)


result = ((cell.group('cell_content'), spots.group('spots_content'), student_number, name, score)
    for school in rx_school.finditer(string)
    for grade in rx_grade.finditer(school.group('school_content'))
    for student_score in rx_student_score.finditer(grade.group('students'))
    for student in zip(student_score.group('student_names')[:-1].split("\n"), student_score.group('student_scores')[:-1].split("\n"))
    for student_number in [student[0].split(", ")[0]]
    for name in [student[0].split(", ")[1]]
    for score in [student[1].split(", ")[1]]
)

df = pd.DataFrame(result, columns = ['School', 'Grade', 'Student number', 'Name', 'Score'])
print(df)

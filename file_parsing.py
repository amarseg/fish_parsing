import pandas as pd, re

rx_school = re.compile(r'''
    ^
    School\s*=\s*(?P<school_name>.+)
    (?P<school_content>[\s\S]+?)
    (?=^School|\Z)
''', re.MULTILINE | re.VERBOSE)

rx_grade = re.compile(r'''
    ^
    Grade\s*=\s*(?P<grade>.+)
    (?P<students>[\s\S]+?)
    (?=^Grade|\Z)
''', re.MULTILINE | re.VERBOSE)

rx_student_score = re.compile(r'''
    ^
    Student\ number,\ Name[\n\r]
    (?P<student_names>(?:^\d+.+[\n\r])+)
    \s*
    ^
    Student\ number,\ Score[\n\r]
    (?P<student_scores>(?:^\d+.+[\n\r])+)
''', re.MULTILINE | re.VERBOSE)


result = ((school.group('school_name'), grade.group('grade'), student_number, name, score)
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

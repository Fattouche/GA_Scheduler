from collections import defaultdict

ROOM_INFO_DICT_1 = {
    1: {"capacity": 5},
    2: {"capacity": 8},
    3: {"capacity": 10}
}

STUDENT_COURSES_DICT_1 = {
    1: [1],
    2: [1],
    3: [1],
    4: [1],
    5: [1, 2],
    6: [1, 2],
    7: [1, 2],
    8: [2],
    9: [3],
    10: [3, 1],
    11: [3, 2]
}

COURSE_STUDENTS_DICT_1 = defaultdict(set)
for key, value in STUDENT_COURSES_DICT_1.items():
    for course in value:
        COURSE_STUDENTS_DICT_1[course].add(key)

CHROMOSOME_1 = {
    1: [2, [4, 6], 'MW'],
    2: [1, [7, 9], 'TR'],
    3: [3, [10, 12], 'WF']
}

CHROMOSOME_2 = {
    1: [1, [4, 6], 'MW'],
    2: [2, [4, 6], 'TR'],
    3: [3, [4, 6], 'WF']
}

CHROMOSOME_3 = {
    1: [1, [6, 8], 'MW'],
    2: [2, [5, 6], 'MTR'],
    3: [3, [9, 11], 'WF']
}

CHROMOSOME_4 = {
    1: [1, [1, 3], 'MW'],
    2: [2, [5, 6], 'MTR'],
    3: [3, [9, 11], 'WF']
}

CHROMOSOME_5 = {
    1: [2, [4, 6], 'MW'],
    2: [1, [4, 6], 'MW'],
    3: [3, [4, 6], 'MW']
}

CHROMOSOME_6 = {
    1: [3, [4, 6], 'MW'],
    2: [2, [4, 6], 'MW'],
    3: [1, [4, 6], 'MW']
}


CHROMOSOME_7 = {
    1: [1, [1, 3], 'MW'],
    2: [1, [4, 6], 'MW'],
    3: [1, [1, 3], 'TR']
}

CHROMOSOME_8 = {
    1: [1, [1, 3], 'MW'],
    2: [1, [3, 6], 'MW'],
    3: [1, [1, 3], 'TR']
}


population = [CHROMOSOME_1, CHROMOSOME_2, CHROMOSOME_3, CHROMOSOME_4,
              CHROMOSOME_5, CHROMOSOME_6, CHROMOSOME_7, CHROMOSOME_8]

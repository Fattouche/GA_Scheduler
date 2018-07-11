import random
import math
import sys
import os

CLASS_TYPES = [1, 1.5, 3]
WEEKDAYS = ['M', 'T', 'W', 'R', 'F']
MAX_TIMESLOT = 27


def get_chromosome(course_students_dict, room_ids):
    chrom = {}
    for class_id in course_students_dict:
        chrom[class_id] = generate(room_ids)

    return chrom


def generate(room_ids):
    room_ids = list(room_ids)
    room = random.choice(room_ids)
    duration = random.choice(CLASS_TYPES)

    num_days = 4 - math.ceil(duration)  # kinda random but chooses 1 2 or 3
    days_list = random.sample(WEEKDAYS, num_days)
    days_list.sort(key=lambda x: WEEKDAYS.index(x))
    days = "".join(days_list)

    start_time = random.randint(0, MAX_TIMESLOT)
    end_time = start_time + int(duration/0.5)
    timeslot = [start_time, end_time]

    return [room, timeslot, days]

import random
import math
import sys, os
import xml_parser as parser

CLASS_TYPES = [1, 1.5, 3]
WEEKDAYS = ['M', 'T', 'W', 'R', 'F']
MAX_TIMESLOT = 27
class_information_list = parser.get_classmap()
room_information_list = parser.get_rooms()
room_ids = list(room_information_list.keys())


def get_chromosome():
    # room_ids = list(room_information_list.keys())    
    chrom = {}
    for class_id in class_information_list:
      chrom[class_id] = generate()

    return chrom

def generate():
      room = random.choice(room_ids)
      duration = random.choice(CLASS_TYPES)

      num_days = 4 - math.ceil(duration)  #kinda random but chooses 1 2 or 3
      days_list = random.sample(WEEKDAYS, num_days)
      days_list.sort(key=lambda x: WEEKDAYS.index(x))      
      days = "".join(days_list)

      start_time = random.randint(0,MAX_TIMESLOT)
      end_time = start_time + duration
      timeslot = [start_time, end_time]

      return [room, timeslot, days]

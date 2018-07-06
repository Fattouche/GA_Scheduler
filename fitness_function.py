PREFERRED_START = 4
PREFERRED_END = 16
ROOM = 0
TIMESLOT = 1
DAYS = 2

def calc_num_student_course_conflicts(chromosome, student_courses_dict):
  pass

def calc_num_course_time_loc_conflicts(chromosome):
  pass

def calc_num_overfilled_rooms(chromosome, room_information_dict):
  pass

def calc_num_unfavoured_time_slots_used(chromosome):
  num_unfavoureds_slots = 0
  
  for class_id in chromosome:
    start_timeslot = chromosome[class_id][TIMESLOT][0]
    end_timeslot = chromosome[class_id][TIMESLOT][1]

    if start_timeslot < PREFERRED_START or end_timeslot > PREFERRED_END:
      num_unfavoureds_slots +=1

  return num_unfavoureds_slots

def calc_num_empty_seats_in_course_rooms(chromosome, room_information_dict, course_information_dict):
  num_empty_seats = 0

  for class_id in chromosome:
    capacity = room_information_dict[class_id]["capacity"]
    enrolled = len(course_information_dict[class_id])
    num_empty_seats += (capacity - enrolled)

  return num_empty_seats

def calc_fitness(chromosome):
  pass


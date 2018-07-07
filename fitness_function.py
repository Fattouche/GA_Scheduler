COURSE_INFO_ROOM_ID_INDEX = 0
COURSE_INFO_TIMESLOT_INDEX = 1
COURSE_INFO_DAYS_INDEX = 2
PREFERRED_START = 4
PREFERRED_END = 16

def calc_num_student_course_conflicts(chromosome, student_courses_dict):
  num_student_course_conflicts = 0
  
  for student in student_courses_dict:
    student_courses = student_courses_dict[student]

    # Get time slots of each course from the chromosome
    course_timeslots = [
      chromosome[course][COURSE_INFO_TIMESLOT_INDEX] for course in student_courses
    ] 

    # Sort the courses by start time
    # This is O(1) since number of courses a student can have is O(1)
    course_timeslots.sort(
      Key=lambda timeslot: timeslot[0]
    )

    for i in range(1, len(course_timeslots)):
      prev_timeslot = course_timeslots[i-1]
      curr_timeslot = course_timeslots[i]

      prev_end_time = prev_timeslot[1]
      curr_start_time = curr_timeslot[0]

      if (curr_start_time <= prev_end_time):
        num_student_course_conflicts += 1

  return num_student_course_conflicts


def calc_num_course_time_loc_conflicts(chromosome):
  pass


def calc_total_room_overflow(chromosome, room_information_dict, 
                              course_students_dict):
  total_room_overflow = 0

  for course in chromosome:
    course_info_list = chromosome[course]
    room_id = course_info_list[COURSE_INFO_ROOM_ID_INDEX]

    room_capacity = room_information_dict[room_id]
    num_students_in_course = course_students_dict[course]

    if (num_students_in_course > room_capacity):
      total_room_overflow += (num_students_in_course - room_capacity)

  return total_room_overflow


def calc_num_unfavoured_timeslots_used(chromosome):
  num_unfavoureds_slots = 0
  
  for class_id in chromosome:
    start_timeslot = chromosome[class_id][COURSE_INFO_TIMESLOT_INDEX][0]
    end_timeslot = chromosome[class_id][COURSE_INFO_TIMESLOT_INDEX][1]

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


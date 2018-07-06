ALLELE_ROOM_ID_INDEX = 0
ALLELE_TIME_SLOT_INDEX = 1
ALLELE_DAYS_INDEX = 2


def calc_num_student_course_conflicts(chromosome, student_courses_dict):
  num_student_course_conflicts = 0
  
  for student in student_courses_dict:
    student_courses = student_courses_dict[student]

    # Get time slots of each course from the chromosome
    course_time_slots = [
      chromosome[course][ALLELE_TIME_SLOT_INDEX] for course in student_courses
    ] 

    # Sort the courses by start time
    # This is O(1) since number of courses a student can have is O(1)
    course_time_slots.sort(
      Key=lambda time_slot: time_slot[0]
    )

    for i in range(1, len(course_time_slots)):
      prev_time_slot = course_time_slots[i-1]
      curr_time_slot = course_time_slots[i]

      prev_end_time = prev_time_slot[1]
      curr_start_time = curr_time_slot[0]

      if (curr_start_time <= prev_end_time):
        num_student_course_conflicts += 1


def calc_num_course_time_loc_conflicts(chromosome):
  pass


def calc_num_overfilled_rooms(chromosome, room_information_dict):
  pass


def calc_num_unfavoured_time_slots_used(chromosome):
  pass


def calc_num_empty_seats_in_course_rooms(chromosome):
  pass


def calc_fitness(chromosome):
  pass
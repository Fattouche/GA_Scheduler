import argparse
import random
import xml.etree.ElementTree as ET
from xml.dom import minidom

parser = argparse.ArgumentParser(description='Generates test data.')
parser.add_argument('output_file', type=str, help='XML file to write test to.')
parser.add_argument('num_rooms', type=int, help='Number of rooms to generate.')
parser.add_argument('num_courses', type=int, help='Number of courses to generate.')
parser.add_argument('num_students', type=int, help='Number of students to generate.')
parser.add_argument('--min_room_capacity', type=int, default=5, help='Minimum room capacity.')
parser.add_argument('--max_room_capacity', type=int, default=40, help='Maximum room capacity.')

args = parser.parse_args()

if __name__ == '__main__':
  root = ET.Element('timetable')

  rooms = ET.SubElement(root, 'rooms')
  courses = ET.SubElement(root, 'courses')
  students = ET.SubElement(root, 'students')

  for i in range(1, args.num_rooms + 1):
    room = ET.SubElement(rooms, 'room')
    room.set('id', str(i))

    if i == 1:
      # Want to guarantee that at least one room will have the maximum capacity,
      # since this makes it easier to ensure that a valid solution is possible
      room.set('capacity', str(args.max_room_capacity))
    else:
      room.set('capacity', str(random.randint(args.min_room_capacity, args.max_room_capacity)))

    location = (random.randint(1, 1000), random.randint(1, 1000))
    room.set('location', ','.join((str(location[0]), str(location[1]))))
  
  for i in range(1, args.num_courses + 1):
    course = ET.SubElement(courses, 'course')
    course.set('id', str(i))

  remaining_registration_space = [args.max_room_capacity] * (args.num_courses+1)
  available_courses = [i for i in range(1, args.num_courses + 1)]

  for i in range(1, args.num_students + 1):
    student = ET.SubElement(students, 'student')
    student.set('id', str(i))

    max_num_courses = min(args.num_courses, 6)

    # Choose a random set of course IDs for the student to enroll in
    student_courses = random.sample(
      available_courses,
      random.randint(1, max_num_courses)
    )

    # Update remaining registration space
    # This guarantees that no course will have more students than the
    # capacity of the largest available room (if a course is full, its weight
    # will be zero)
    for registered_course in student_courses:
      remaining_registration_space[registered_course] -= 1

      if remaining_registration_space[registered_course] == 0:
        available_courses.remove(registered_course)

    for course_id in student_courses:
      course = ET.SubElement(student, 'class')
      course.set('id', str(course_id))


  xmlstr = minidom.parseString(ET.tostring(root)).toprettyxml(indent=" ")
  with open(args.output_file, 'w') as f:
    f.write(xmlstr)

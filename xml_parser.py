import os,sys
import xml.etree.ElementTree as ET

path = os.path.dirname(os.path.abspath(__file__))
tree = ET.parse(path + '/data/input.xml')
data = tree.getroot()

# Students and classes
students = {}
classes = {}
for raw_student in data[3]:
    student_id = int(raw_student.attrib["id"])
    students[student_id] = []
    for raw_class in raw_student:
        class_id = int(raw_class.attrib["id"])
        students[student_id].append(class_id)
        if(class_id not in classes):
            classes[class_id] = []
        classes[class_id].append(student_id)
class_map = {}

class_num = 1
for class_id in classes:
    class_map[class_num] = class_id
    class_num+=1

# Rooms
rooms = {}
for room in data[0]:
    location_x = int(room.attrib["location"].split(",")[0])
    location_y = int(room.attrib["location"].split(",")[1])
    rooms[int(room.attrib["id"])] = {
        "capacity": int(room.attrib["capacity"]), "location_x": location_x, "location_y": location_y}

def get_classes():
    return class_map
def get_students():
    return students
def get_rooms():
    return rooms
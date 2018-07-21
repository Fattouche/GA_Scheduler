import os
import sys
import xml.etree.ElementTree as ET


class Parser:
    def __init__(self, input_file):
        tree = ET.parse(input_file)
        self.data = tree.getroot()


    def parse_input(self):
        # Students and classes
        students = {}
        classes = {}

        # Findall finds only elements that are direct children of the current element
        student_root = self.data.findall("students")[0]
        for raw_student in student_root.iter("student"):
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
            class_num += 1

        # Rooms
        rooms = {}

        room_root = self.data.findall("rooms")[0]
        for room in room_root.iter("room"):
            location_x = int(room.attrib["location"].split(",")[0])
            location_y = int(room.attrib["location"].split(",")[1])
            rooms[int(room.attrib["id"])] = {
                "capacity": int(room.attrib["capacity"]), "location_x": location_x, "location_y": location_y
            }

        return (rooms, classes, students, class_map)

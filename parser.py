import xml.etree.ElementTree as ET
tree = ET.parse('data/input.xml')
data = tree.getroot()

# Rooms
rooms = {}
for room in data[0]:
    rooms[room.attrib["id"]] = {
        "capacity": room.attrib["capacity"], "location": room.attrib["location"]}

# classes
classes = []
for class_id in data[1]:
    classes.append(class_id.attrib["id"])

# Students
students = {}
for student in data[3]:
    students[student.attrib["id"]] = []
    for class_id in student:
        students[student.attrib["id"]].append(class_id.attrib["id"])

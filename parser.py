import xml.etree.ElementTree as ET
tree = ET.parse('data/input.xml')
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

# Rooms
rooms = {}
for room in data[0]:
    location_x = int(room.attrib["location"].split(",")[0])
    location_y = int(room.attrib["location"].split(",")[1])
    rooms[int(room.attrib["id"])] = {
        "capacity": int(room.attrib["capacity"]), "location_x": location_x, "location_y": location_y}

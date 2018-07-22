from collections import defaultdict

COURSE_INFO_ROOM_ID_INDEX = 0
COURSE_INFO_TIMESLOT_INDEX = 1
COURSE_INFO_DAYS_INDEX = 2
PREFERRED_START = 4
PREFERRED_END = 16

class FitnessCalculator:
    def __init__(self, room_information_dict, course_students_dict, student_courses_dict,
                fitness_threshold):
        self.room_information_dict = room_information_dict
        self.course_students_dict = course_students_dict
        self.student_courses_dict = student_courses_dict
        self.fitness_threshold = fitness_threshold


    def calc_num_student_course_conflicts(self, chromosome):
        num_student_course_conflicts = 0

        for student in self.student_courses_dict:
            student_courses = self.student_courses_dict[student]

            # Get time slots of each course from the chromosome
            course_timeslots = [
                (chromosome[course][COURSE_INFO_TIMESLOT_INDEX],
                chromosome[course][COURSE_INFO_DAYS_INDEX])
                for course in student_courses
            ]

            # Sort the courses by start time
            # This is O(1) since number of courses a student can have is O(1)
            course_timeslots.sort(
                key=lambda timeslot: timeslot[0][0]
            )

            for i in range(1, len(course_timeslots)):
                prev_timeslot = course_timeslots[i-1][0]
                curr_timeslot = course_timeslots[i][0]

                prev_end_time = prev_timeslot[1]
                curr_start_time = curr_timeslot[0]

                if (curr_start_time <= prev_end_time):
                    prev_days = course_timeslots[i-1][1]
                    curr_days = course_timeslots[i][1]

                    # Returns true if both strings contain a common char
                    if (not set(prev_days).isdisjoint(curr_days)):
                        num_student_course_conflicts += 1

        return num_student_course_conflicts
            

    def calc_single_course_room_time_conflicts(self, chromosome, course_id, 
        courses_per_time_and_day):

        num_course_room_time_conflicts = 0

        course_info_list = chromosome[course_id]
        room_id = course_info_list[COURSE_INFO_ROOM_ID_INDEX]

        for time in range(course_info_list[COURSE_INFO_TIMESLOT_INDEX][0],
                        course_info_list[COURSE_INFO_TIMESLOT_INDEX][1] + 1):
            for day in course_info_list[COURSE_INFO_DAYS_INDEX]:
                if room_id in courses_per_time_and_day[(time, day)]:
                    num_course_room_time_conflicts += 1
                else:
                    courses_per_time_and_day[(time, day)].add(room_id)

        return num_course_room_time_conflicts


    def calc_single_room_overflow(self, chromosome, course_id):
        room_overflow = 0

        course_info_list = chromosome[course_id]
        room_id = course_info_list[COURSE_INFO_ROOM_ID_INDEX]

        room_capacity = self.room_information_dict[room_id]['capacity']
        num_students_in_course = len(self.course_students_dict[course_id])

        if (num_students_in_course > room_capacity):
            room_overflow += (num_students_in_course - room_capacity)

        return room_overflow


    def calc_single_course_unfavoured_timeslots(self, chromosome, course_id):
        num_unfavoureds_slots = 0

        for time in range(chromosome[course_id][COURSE_INFO_TIMESLOT_INDEX][0],
                            chromosome[course_id][COURSE_INFO_TIMESLOT_INDEX][1] + 1):

            if time < PREFERRED_START or time > PREFERRED_END:
                num_unfavoureds_slots += 1

        return num_unfavoureds_slots


    def calc_num_empty_seats_single_course(self, chromosome, course_id):
        num_empty_seats = 0

        capacity = self.room_information_dict[chromosome[course_id][0]]["capacity"]
        enrolled = len(self.course_students_dict[course_id])

        if capacity > enrolled and enrolled != 0:
            num_empty_seats += (capacity - enrolled)

        return num_empty_seats


    def iterate_over_chromosome(self, chromosome):
        num_course_room_time_conflicts = 0
        total_room_overflow = 0
        num_unfavoureds_slots = 0
        num_empty_seats = 0

        # Index this dict by (time, day) - for calculating number of course
        # room time conflicts
        courses_per_time_and_day = defaultdict(set)

        for course_id in chromosome:
            num_course_room_time_conflicts += self.calc_single_course_room_time_conflicts(
                chromosome, course_id, courses_per_time_and_day)
                
            total_room_overflow += self.calc_single_room_overflow(chromosome, course_id)
            
            num_unfavoureds_slots += self.calc_single_course_unfavoured_timeslots(chromosome, course_id)
            
            num_empty_seats += self.calc_num_empty_seats_single_course(chromosome, course_id)

        return (num_course_room_time_conflicts, total_room_overflow,
                num_unfavoureds_slots, num_empty_seats)



    def calc_fitness_and_validity(self, chromosome):
        num_course_room_time_conflicts, total_room_overflow, \
        num_unfavoureds_slots, num_empty_seats = \
            self.iterate_over_chromosome(chromosome)

        num_student_course_conflicts = self.calc_num_student_course_conflicts(chromosome)

        fitness = \
            1.0 * num_student_course_conflicts \
            + 1.0 * num_course_room_time_conflicts \
            + 1.0 * total_room_overflow \
            + 0.1 * num_unfavoureds_slots \
            + 0.05 * num_empty_seats

        validity = True if (num_student_course_conflicts == 0 and \
                            num_course_room_time_conflicts == 0 and \
                            total_room_overflow == 0) else False

        return (fitness, validity)


    def get_fit_chromosomes(self, population):
        fit_chromosomes = []
        min_fitness = float('inf')

        for chromosome in population:
            chromosome_fitness_and_validity = self.calc_fitness_and_validity(chromosome)
            fitness = chromosome_fitness_and_validity[0]
            validity = chromosome_fitness_and_validity[1]
            
            if fitness <= self.fitness_threshold:
                fit_chromosomes.append((chromosome, fitness, validity))
           
            min_fitness = min(min_fitness, fitness)

        print('Min fitness: {}'.format(min_fitness))

        return fit_chromosomes

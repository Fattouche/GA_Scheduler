# AI_ClassScheduler
This course scheduler takes a data set from purdue university and generates an optimal course schedule based off hard and soft constraints as specified by the fitness function.

The schedule consists of:

Classes and their corresponding rooms/timeslots.


## Requirements
Python3

## Usage
`python3 genetic_algorithm.py input.xml fitness_value [--round_limit MAX_SELECTION_ROUNDS]` 

Example: `python3 genetic_algorithm.py data/generated_datasets/test_5.xml 40 --round_limit 500`

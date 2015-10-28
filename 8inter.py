#intersection of two dictionaries

math = {'stud1': 'B', 'stud2': 'A', 'stud3': 'F' }
cs = {'stud1': 'A', 'stud6': 'A', 'stud5': 'B' }

intersection = {}

intersection = filter(math.has_key, cs.keys())

print intersection
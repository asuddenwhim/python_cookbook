#obtain a value using key entered by user

data = {'1': 'crazy', '2': 'little', '3': 'girl'}

key = str(input('Enter key: '))

print data.get(key, 'not found')
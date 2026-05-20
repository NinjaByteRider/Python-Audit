# write to file
with open('notes.txt', 'w') as f:
    f.write('Audit log start\n')
    f.write('User admin logged in\n')

#read file
with open('notes.txt', 'r') as f:
    content = f.read()
    print(content)
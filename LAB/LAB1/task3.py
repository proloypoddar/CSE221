file = open("F:\CSE221\LAB\LAB1\input3.txt", "r")
N = int(file.readline())
ids = list(map(int, file.readline().split()))
marks = list(map(int, file.readline().split()))
file.close()

# Create a list of tuples where each tuple contains the ID and mark
students = []
for i in range(N):
    student = (ids[i], marks[i])
    students.append(student)

# Bubble Sort Algorithm
for i in range(N-1):
    for j in range(N-i-1):
        if students[j][1] < students[j+1][1] or (students[j][1] == students[j+1][1] and students[j][0] > students[j+1][0]):
            students[j], students[j+1] = students[j+1], students[j]

w = open("F:\CSE221\LAB\LAB1\output3.txt", "w")

# Write sorted student IDs and marks to the output file
for student in students:
    w.write(f"ID: {student[0]} Mark: {student[1]}\n")

w.close()

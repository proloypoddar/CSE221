def maximum_num_task(tasks):
    tasks.sort(key=lambda x: x[1])
    completed = 0
    choose_task = []

    end_time = -1  
    for i in tasks:
        start, end = i
        if start >= end_time:
            completed += 1
            choose_task.append(i)
            end_time = end

    return completed, choose_task

input_file = "F:\CSE221\LAB\LAB7\input_task1.txt" 
output_file = "F:\CSE221\LAB\LAB7\output_task1.txt"  

with open(input_file, "r") as f:
    N = int(f.readline())
    tasks = []
    for _ in range(N):
        start, end = map(int, f.readline().split())
        tasks.append((start, end))

max_completed, choose_task = maximum_num_task(tasks)

with open(output_file, "w") as f:
    f.write(str(max_completed) + "\n")
    for i in choose_task:
        f.write(f"{i[0]} {i[1]}\n")

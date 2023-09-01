def activity(tasks, m):
    tasks.sort(key=lambda x: x[1])
    completed = 0
    end_times = [-1] * m  
    for i in tasks:
        start, end = i
        assigned = False
        for i in range(m):
            if start >= end_times[i]:
                completed += 1
                end_times[i] = end
                assigned = True
                break
        if not assigned:
            continue  

    return completed
input_file = "F:\CSE221\LAB\LAB7\input_task2.txt" 
output_file = "F:\CSE221\LAB\LAB7\output_task2.txt" 

with open(input_file, "r") as f:
    N, M = map(int, f.readline().split())
    activities = []
    for _ in range(N):
        start, end = map(int, f.readline().split())
        activities.append((start, end))

max_completed = activity(activities, M)

with open(output_file, "w") as f:
    f.write(str(max_completed) + "\n")
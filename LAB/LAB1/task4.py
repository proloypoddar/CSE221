file = open("F:\CSE221\LAB\LAB1\input4.txt", "r")
N = int(file.readline())
trains = []
for _ in range(N):
    train_info = file.readline().strip().split(" will departure for ")
    train_name = train_info[0]
    departure_time = train_info[1].split(" at ")[1]
    trains.append((train_name, departure_time))
file.close()
for i in range(N-1):
    for j in range(N-i-1):
        if trains[j][0] > trains[j+1][0] or (trains[j][0] == trains[j+1][0] and trains[j][1] < trains[j+1][1]):
            trains[j], trains[j+1] = trains[j+1], trains[j]
w = open("F:\CSE221\LAB\LAB1\output4.txt", "w")
for train in trains:
    w.write(f"{train[0]} will departure for {train[1]}\n")

w.close()

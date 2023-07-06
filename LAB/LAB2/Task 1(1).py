def find_pair_sum(input_file, output_file):
    with open(input_file, 'r') as f:
        N, S = map(int, f.readline().split())
        arr = list(map(int, f.readline().split()))

    pair_found = False
    for i in range(N):
        for j in range(i + 1, N):
            if arr[i] + arr[j] == S:
                with open(output_file, 'w') as f:
                    f.write(f"{i + 1} {j + 1}\n")
                pair_found = True
                break
        if pair_found:
            break

    if not pair_found:
        with open(output_file, 'w') as f:
            f.write("IMPOSSIBLE\n")
input_file = "F:/CSE221/LAB/LAB2/input_task1_1.txt"
output_file = "F:/CSE221/LAB/LAB2/output_task1_1.txt"
find_pair_sum(input_file, output_file)

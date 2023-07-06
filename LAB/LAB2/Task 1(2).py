def find_pair_sum(input_file, output_file):
    with open(input_file, 'r') as f:
        N, S = map(int, f.readline().split())
        arr = list(map(int, f.readline().split()))

    value_index = {} 

    for i in range(N):
        complement = S - arr[i]
        if complement in value_index:
            with open(output_file, 'w') as f:
                f.write(f"{value_index[complement] + 1} {i + 1}\n") 
            return

        value_index[arr[i]] = i  

    with open(output_file, 'w') as f:
        f.write("IMPOSSIBLE\n")  

input_file = "F:/CSE221/LAB/LAB2/input_task1_2.txt"
output_file = "F:/CSE221/LAB/LAB2/output_task1_2.txt"
find_pair_sum(input_file, output_file)

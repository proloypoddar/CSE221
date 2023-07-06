def merge_lists(alice_list, bob_list):
    merged_list = []
    i = 0
    j = 0

    while i < len(alice_list) and j < len(bob_list):
        if alice_list[i] <= bob_list[j]:
            merged_list.append(alice_list[i])
            i += 1
        else:
            merged_list.append(bob_list[j])
            j += 1
    while i < len(alice_list):
        merged_list.append(alice_list[i])
        i += 1    
    while j < len(bob_list):
        merged_list.append(bob_list[j])
        j += 1
    return merged_list

file = open("F:\CSE221\LAB\LAB2\input_task2_2.txt", "r")
alice_length = int(file.readline())
alice_list = list(map(int, file.readline().split()))
bob_length = int(file.readline())
bob_list = list(map(int, file.readline().split()))
file.close()

merged_list = merge_lists(alice_list, bob_list)

output_file = open("F:\CSE221\LAB\LAB2\output_task2_2.txt", "w")
output_file.write(" ".join(map(str, merged_list)))
output_file.close()

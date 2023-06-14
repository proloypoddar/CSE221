# def merge_lists(alice_list, bob_list):
#     n = len(alice_list) + len(bob_list)
#     merged_list = [0] * n
#     i = 0
#     j = 0
#     k = 0
#     while i < len(alice_list) and j < len(bob_list):
#         if alice_list[i] <= bob_list[j]:
#             merged_list[k] = alice_list[i]
#             i += 1
#         else:
#             merged_list[k] = bob_list[j]
#             j += 1
#         k += 1

#     while i < len(alice_list):
#         merged_list[k] = alice_list[i]
#         i += 1
#         k += 1

#     while j < len(bob_list):
#         merged_list[k] = bob_list[j]
#         j += 1
#         k += 1

#     return merged_list
# alice_list = [1, 3, 5, 7, 9]
# bob_list = [2, 4, 6, 8, 10]

# sorted_list = merge_lists(alice_list, bob_list)
# print(sorted_list)
# ###########################################33
a = [1, 3, 5, 7]
b = [2, 2, 4, 8]

merged_list = []
i = 0
j = 0

while i < len(a) and j < len(b):
    if a[i] <= b[j]:
        merged_list.append(a[i])
        i += 1
    else:
        merged_list.append(b[j])
        j += 1
merged_list.extend(a[i:])
merged_list.extend(b[j:])

print(merged_list)

arr = [1,2,3,4,5,5,5,6,6,7]
freq_dict = {}

for num in arr:
    if num in freq_dict:
        freq_dict[num] += 1
    else:
        freq_dict[num] = 1

print(freq_dict)
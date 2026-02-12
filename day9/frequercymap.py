n = [1,3,2,4,5,5,1,6]
m = [10,2,4,5,9,111,1,0]

# max value 10 maan ke size 11 banaya (0 to 10)
hash_map = [0] * 11  

# frequency store karna
for i in n:
    hash_map[i] += 1

print("Frequency array:", hash_map)

# queries check karna
for x in m:
    if x < 0 or x > 10:
        print(0)
    else:
        print(hash_map[x])
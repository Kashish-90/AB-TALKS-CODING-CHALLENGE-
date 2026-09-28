posts = ["A", "B", "C", "A"]
k = 3

hash_map = {}

found = False

for i in range(len(posts)):
    if posts[i] in hash_map:
        if i - hash_map[posts[i]] <= k:
            found = True
            break

    hash_map[posts[i]] = i

if found:
    print("Duplicate found within K distance")
else:
    print("No duplicate found")

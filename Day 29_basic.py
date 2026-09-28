from collections import Counter

def top_k_hashtags(hashtags, k):
    freq = Counter(hashtags)

    sorted_hashtags = sorted(
        freq.items(),
        key=lambda x: x[1],
        reverse=True
    )

    return sorted_hashtags[:k]


hashtags = [
    "#AI", "#Python", "#AI", "#Coding",
    "#Python", "#AI", "#Data",
    "#Coding", "#Python", "#ML"
]

k = 3

result = top_k_hashtags(hashtags, k)

print("Top", k, "Trending Hashtags:")
for tag, count in result:
    print(tag, "->", count)

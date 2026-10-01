def sort_colors(colors):

    low = 0
    mid = 0
    high = len(colors) - 1

    while mid <= high:

        if colors[mid] == 0:
            colors[low], colors[mid] = colors[mid], colors[low]
            low += 1
            mid += 1

        elif colors[mid] == 1:
            mid += 1

        else:
            colors[mid], colors[high] = colors[high], colors[mid]
            high -= 1

    return colors


colors = [2, 0, 2, 1, 1, 0]

print("Sorted Colors:", sort_colors(colors))

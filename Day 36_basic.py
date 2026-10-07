# Container With Most Water
# Two Pointer Optimization

def max_water(height):
    left = 0
    right = len(height) - 1
    max_area = 0

    while left < right:
        width = right - left
        area = min(height[left], height[right]) * width

        if area > max_area:
            max_area = area

        # Move the smaller wall
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_area


# Example Input
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]

print("Heights:", height)
print("Maximum Water Stored:", max_water(height))

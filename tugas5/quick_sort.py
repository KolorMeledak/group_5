def quick_sort(nums, depth=0):
    indent = "  " * depth
    if len(nums) <= 1:
        return nums

    pivot = nums[-1]
    left = []
    right = []

    print(f"{indent}Quick Sort: {nums} → pivot: {pivot}")
    for x in nums[:-1]:
        if x <= pivot:
            print(f"{indent}  {x} <= {pivot} → kiri")
            left.append(x)
        else:
            print(f"{indent}  {x} > {pivot} → kanan")
            right.append(x)

    sorted_left = quick_sort(left, depth + 1)
    sorted_right = quick_sort(right, depth + 1)

    result = sorted_left + [pivot] + sorted_right
    print(f"{indent}Gabung: {sorted_left} + [{pivot}] + {sorted_right} = {result}")
    return result

data = [34, 7, 23, 32, 5, 62]
sorted_shell = quick_sort(data)
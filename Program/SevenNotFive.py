def seven(low,high):
    nums = []
    for i in range(low,high):
        if i % 7 == 0 and i % 5 != 0:
            nums.append(i)



    return nums

print(seven(20,32))

def words(nums):
    list = []
    word = ""
    final = ""
    for i in range(len(nums)):
        if nums[i] != " ":
            word = word + nums[i]
        else:
            list.append(word)
            word = ""
    list.append(word)

    s = set(list)
    s = sorted(s)
    return " ".join(s)



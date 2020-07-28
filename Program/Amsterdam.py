def ams(word):
   
    count = 0
    for i in range(len(word)-2):
        if word[i] == "a" and word[i +1] == "m" and word[i + 2] == " ":
            count +=1
            print(i)
        elif word[i] == "A" and word[i +1] == "m" and word[i + 2] == " ":
            count +=1
            

    return count


word = "I have been in Amsterdam"
print(ams(word))
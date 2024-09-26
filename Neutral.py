def neutralise(s1, s2):
    result = ""
    for i in range(len(s1)):
        # Wenn s1[i] == + und s2[i] == + dann result += "+"
        if s1[i] == s2[i]:
            result += s1[i]
        else:
            result += "0"
    return result
        

print(neutralise("--+++-+-","+++++---"))

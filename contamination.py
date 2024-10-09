def contamination(text,char):

    n = len(text)

    if n > 1:
        return char * n
    else:
        return ""




print(contamination("","z"))

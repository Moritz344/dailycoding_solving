def vaporcode(text):
    text = text.upper().replace(" ","")
    return " ".join(text)
    


print(vaporcode("Sample text"))

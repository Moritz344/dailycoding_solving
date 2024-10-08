def queue(data):
    data.append(5)
    data.append(15)
    data.append(25)
    data.append(35)

    data.pop(0)
    data.pop(0)


data = []
queue(data)
print(data)


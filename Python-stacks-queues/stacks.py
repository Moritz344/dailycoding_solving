def stack(data):
    # Last in First Out

    data.append(5)
    data.append(10)
    data.append(15)
    data.append(25)

    print(data[len(data) - 1])

    data.pop() # pop 15
    data.pop() # pop 25




data = []
stack(data)
print(data)

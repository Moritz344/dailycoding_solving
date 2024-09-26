def change_me(money):
    nominals = ['£5', '£2', '£1', '50p', '20p']

    if money not in nominals:
        return money

    if money == "20p":
        return "10p 10p"
    if money == "50p":
        return "20p 20p 10p"

    if money == "£1":
        return "20p " * 5
    if money == "£5":
        return "20p " * 25

    




print(change_me("£5"))

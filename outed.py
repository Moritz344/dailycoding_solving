def outed(meet,boss):
    people = len(meet)
    total_score = 0
    
    for i in meet:
        for member,rating in meet.items():
            if member == boss:
                total_score += rating * 2
            else:
                total_score += rating

        average_hapiness = total_score / people

        if average_hapiness <= 5:
            return "Get out Now!"
        else:
            return "Nice Work Champ!"






print(outed({'tim':0, 'jim':2, 'randy':9, 'sandy':7, 'andy':0, 'katie':5, 'laura':1, 'saajid':2, 'alex':3, 'john':2, 'mr':0}, 'laura'))
print(outed({'tim':1, 'jim':3, 'randy':9, 'sandy':6, 'andy':7, 'katie':6, 'laura':9, 'saajid':9, 'alex':9, 'john':9, 'mr':8}, 'katie'))
print(outed({'tim':2, 'jim':4, 'randy':0, 'sandy':5, 'andy':8, 'katie':6, 'laura':2, 'saajid':2, 'alex':3, 'john':2, 'mr':8}, 'john'))



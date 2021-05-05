
# tuples = (1, 2, 3)
# credit_card1 = (5022291058035724, 'Mojtaba Zandi Ghashghaei', '163', '03/11')
# credit_card2 = (6037701195253813, 'Gholamhosein Zandi Ghashghaei', '4045', '02/05')
# credit_cards = [credit_card1, credit_card2]
# print(credit_cards[0])

person = ('Kiarash Zandi', 23, 'coding')
person2 = ('Siavash Zandi', 30, 'making film')
people = [person, person2]
# name, age, favToDo = person
for name, age, favToDo in people:
    print(name)
    print(age)
    print(favToDo)
    print()
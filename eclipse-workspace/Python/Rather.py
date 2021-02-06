# Asks a would you rather Questions
Answer1 = (input('Would you rather live one life that lasts 1,000 years or live 10 lives that last 100 years each? '))
Status = True
#Makes sure no one puts a bad answer
while Status:
    if Answer1 == '1000 years':
        print('You would rather live one life that lasts', Answer1.lower())
        Status = False
    elif Answer1 == '1,000 years':
        print('You would rather live one life that lasts', Answer1.lower())
        Status = False
    elif Answer1 == '10 lives':
        print('You would rather live %s that lasts 100 years each' % Answer1.lower())
        Status = False
    else:
        Status = True
        print('Please put in a real answer')
        Answer1 = (input('Would you rather live one life that lasts 1,000  years or live 10 lives that last 100 years each? '))


Answer2 = (input('Would you rather have a dragon or be a dragon? '))
Status = True

while Status:
    if Answer2 == 'Be a dragon':
        print('You would rather', Answer2.lower())
        Status = False
    elif Answer2 == 'be a dragon':
        print('You would rather', Answer2.lower())
        Status = False
    elif Answer2 == 'have a dragon':
        print('You would rather', Answer2.lower())
        Status = False
    elif Answer2 == 'Have a dragon':
        print('You would rather', Answer2.lower())
        Status = False
    else:
        Status = True
        print('Please put in a real answer')
        Answer2 = (input('Would you rather have a dragon or be a dragon? '))


Answer3 = (input('Would you rather sound like Mickey Mouse or like Donald Duck for the rest of your life? '))
Status = True

while Status:
    if Answer3 == 'Mickey Mouse':
        print('You would rather sound like', Answer3)
        Status = False
    elif Answer3 == 'Donald Duck':
        print('You would rather sound like', Answer3)
        Status= False
    else:
        Status = True
        print('Please put in a real answer')
        Answer3 = (input('Would you rather sound like Mickey Mouse or like Donald Duck for the rest of your life? '))


Answer4 = (input('Would you rather live in the Star Wars Galaxy or live at Hogwarts? '))
Status = True

while Status:
    if Answer4 == 'Star Wars Galaxy':
        print('You would rather live in the ', Answer4)
        Status = False
    elif Answer4 == 'Hogwarts':
        print('You would rather live at', Answer4)
        Status= False
    else:
        Status = True
        print('Please put in a real answer')
        Answer4 = (input('Would you rather live in the Star Wars Galaxy or live at Hogwarts? '))


Answer5 = (input('Would you rather have the aliens that make first contact with humans be robots or living? '))
Status = True

while Status:
    if Answer5 == 'Robots':
        print('You would rather have aliens make first contact with humans be ', Answer5.lower())
        Status = False
    elif Answer5 == 'robots':
        print('You would rather have aliens make first contact with humans be', Answer5.lower())
        Status= False
    elif Answer5 == 'living':
        print('You would rather have aliens make first contact with humans be', Answer5.lower())
        Status= False
    elif Answer5 == 'Living':
        print('You would rather have aliens make first contact with humans be', Answer5.lower())
        Status= False
    else:
        Status = True
        print('Please put in a real answer')
        Answer5 = (input('Would you rather have the aliens that make first contact with humans be robots or living? '))




Answer6 = (input('Would you rather have all traffic lights you approach be green or never have to stand in line again? '))
Status = True

while Status:
    if Answer6 == 'All trafic lights to be green':
        print('You would rather have', Answer6.lower())
        Status = False
    elif Answer6 == 'all trafic lights to be green':
        print('You would rather have', Answer6.lower())
        Status = False
    elif Answer6 == 'never stand in line again':
        print('You would rather have to ', Answer6.lower())
        Status = False
    elif Answer6 == 'Never stand in line again':
        print('You would rather have to ', Answer6.lower())
        Status= False
    else:
        Status = True
        print('Please put in a real answer')
        Answer6 = (input('Would you rather have all traffic lights you approach be green or never have to stand in line again? '))


Answer7 = (input('Would you rather be able to control animals (but not humans) with your mind or control electronics with your mind? '))
Status = True

while Status:
    if Answer7 == 'Animals':
        print('You would rather control %s with your mind' % Answer7.lower())
        Status = False
    elif Answer7 == 'animals':
        print('You would rather control %s with your mind' % Answer7.lower())
        Status = False
    elif Answer7 == 'Electronics':
        print('You would rather control %s with your mind' % Answer7.lower())
        Status= False
    elif Answer7 == 'electronics':
        print('You would rather control %s with your mind' % Answer7.lower())
        Status= False
    else:
        Status = True
        print('Please put in a real answer')
        Answer7 = (input('Would you rather have all traffic lights you approach be green or never have to stand in line again? '))




List = (Answer1, Answer2, Answer3, Answer4, Answer5, Answer6, Answer7)
Ask = (input('Would you like a list of your answer? '))


if Ask == 'yes':
    print(List)
elif Ask == 'Yes':
    print(List)

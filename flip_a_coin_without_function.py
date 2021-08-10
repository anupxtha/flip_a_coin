import random
play=True
while play==True:
    choices = ('head', 'tail')
    user_choice='reset'
    while user_choice not in choices:
        user_choice = input('Head or Tail?\n').lower()
    random_number = random.randrange(1,3)
    if random_number == 1:
        Outcome = 'head'
    else:
        Outcome = 'tail'
    if user_choice == Outcome:
        print(f'Congrats it was {Outcome}, you are the winner!')
    elif user_choice != Outcome:
        print(f'Sorry, it was {Outcome}. Try Again.')
    yesorno = ('y', 'n')
    user_mood='reset'
    while user_mood not in yesorno:
        user_mood = input('Wanna Try Again? (type y for yes and n for no)\n')
        if user_mood == 'n':
            play=False
        elif user_mood == 'y':
            break

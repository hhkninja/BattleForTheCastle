play_more=True
while play_more:
    print('boom! boom! boom! you wake up covered in sweat but the booming wont stop you look out of the window in your room the castle is under attack! what will you do?') #if you want something to just print - use print('text here') with the ' !
#when you write your question you have to start it with int(input('question') you need to store the answer in a variable
    selection = int(input('1.run from the castle in fear and hope to get out, 2 put on armor draw your sord and fight.'))
    if selection == 1: #need 2 = bc you are checking if it = something see above you are setting it to that
        print('as you run you see enemey storm into the castle then you see all exits have been blocked and without your sword it is hopeless, an enemy grabs you and slaps cuffs on your hands')
    if selection == 2:
        print('you draw your sword moments later three enemmy walk in as you are in the closet they do not see you')
        select =int(input('3 run out and fight them, 4 stay hidden.'))
        if select ==3:
            print('your first slash brings down one of them but the other two fight hard and soon one is able to stab you')
        if select== 4:
            print('they do not see you in the closet and as they leave the room you think about what you could do...')
            dinoforce = int(input('5 head into the secret passegess ,but there may be enemmys in them, 6 stay in the closet but you may be spoted'))
            if dinoforce == 5:
                print('you crawl out no one is in there with you, so you make it out of the castle to fight another day, THE END')
            if dinoforce== 6:
                print('you stay hidden for another hour then you see an eye in the crack between the doors')
                bob = int(input('7 stab the eye, 8 stay hidden'))
                if bob == 7:
                    print('your thrust kills the man and you run you dodge enemy soon you get to the wall you jump down and run, to fight another day, THE END')
                if bob == 8:
                    print ('before you can react a sword blae slams through the door you fall knowing your armys hope falls with you')
    uinput = input ('type y if you want to play agian or q if you want to quit ')
    play_more =uinput.lower() == 'y'
    if uinput =='q':
        break

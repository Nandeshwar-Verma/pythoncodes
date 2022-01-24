#from IPython.display import clear_output     #works only in Jupiter and then clear_output()
from os import system,name
def clear(): 
    """ this is to clear the screen after every use"""
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear')

def cls():
    print('\n'*50)
    
#print_ttt(list9)


def print_ttt(list9):
    """ this is the final print of list of input"""
    print('\n',list9[0],list9[1],list9[2],'\n',list9[3],list9[4],list9[5],'\n',list9[6],list9[7],list9[8])

def play_again():
    """ this is to ask the players whether they want to play again"""
    play_again=input("wanna play again Y or N :")
    if play_again =='Y':
        main()
    else:
        print("GOOD BYE!")
        exit()
        
def validate(list9,player):
    """ this is to check if the tic tac toe condition is met or not row wise - column wise-diagonal"""
    #print("chance_count:",chance_count)
    if chance_count==9:
        if list9[0]==list9[1]==list9[2] or list9[3]==list9[4]==list9[5] or list9[6]==list9[7]==list9[8]:    #rows
                print("WINNNER WINNER WINNER WINNER WINNNER")
                print("winner is here. {} is winner".format(player))
                print("$"*50)
                play_again()
                
        elif list9[0]==list9[3]==list9[6] or list9[1]==list9[4]==list9[7] or list9[2]==list9[5]==list9[8]:  #columns
                print("WINNNER WINNER WINNER WINNER WINNNER")
                print("winner is here. {} is winner".format(player))
                print("$"*50)
                play_again()
                
        elif list9[0]==list9[4]==list9[8] or list9[2]==list9[4]==list9[6]:                                   #diagonal
                print("WINNNER WINNER WINNER WINNER WINNNER")
                print("winner is here.  {} is winner".format(player))
                print("$"*50)
                play_again()
                
        else:
                print("IT's a TIE!!! Both were fantastic ")
                play_again()
    else:
        if list9[0]==list9[1]==list9[2] or list9[3]==list9[4]==list9[5] or list9[6]==list9[7]==list9[8]:    #rows
                print("WINNNER WINNER WINNER WINNER WINNNER")
                print("winner is here. {} is winner".format(player))
                print("$"*50)
                play_again()
                
        elif list9[0]==list9[3]==list9[6] or list9[1]==list9[4]==list9[7] or list9[2]==list9[5]==list9[8]:  #columns
                print("WINNNER WINNER WINNER WINNER WINNNER")
                print("winner is here. {} is winner".format(player))
                print("$"*50)
                play_again()
                
        elif list9[0]==list9[4]==list9[8] or list9[2]==list9[4]==list9[6]:                                   #diagonal
                print("WINNNER WINNER WINNER WINNER WINNNER")
                print("winner is here.  {} is winner".format(player))
                print("$"*50)
                play_again()
                
        else:
                next

       

def current_player(user_dict,player_turn):
    """ this is for getting and printing the current player name who will won """
    key1=list()
    for item in user_dict.items():
        if item[1]==player_turn:
            key1.append(item[0])
    return key1[0]
    
def input_user_role():
    input1=['X','O']
    global retry
    global Player1
    global Player2
    global iur
    iur=input("what do you want to be as player 1 .Choose 'X' or 'O' :")
    if iur not in input1:
        print("wrong entry. choose either 'X' or 'O'. Try again ")
        retry=input("do you want to try again :Y or N ")
        if retry=='Y':
            input_user_role()
        else:
            print("Good Bye. Have a good Day! ")
        
    if iur=='X' or iur=='O':
        print('Player 1 is {}'.format(iur))
        input1.remove(iur)
        print('Player 2 is {}'.format(input1[0]))
        print("LETS PLAY TIC TAC TOE")
        Player1=iur
        Player2=input1[0]
        user_dict['Player1']=Player1
        user_dict['Player2']=Player2
        #print(user_dict)
def user_call():
    """ this is for getting who gets first and then odd chances will be for player one
        and even chances willl be for player 2"""
    global chance_count
    global player_turn
    chance_count=1
    while chance_count <=9:
        if chance_count %2!=0:
            print("player 1 chance . Player1 is {}".format(Player1))
            #chance_count+=1
            player_turn=Player1
            #print("player_turn=:",player_turn)
            user_grid()     #user grid call
        else:
            print("player 2 chance.Player2 is {}".format(Player2))
            #chance_count+=1
            player_turn=Player2
            #print("player_turn=:",player_turn)
            user_grid()     #user grid call
        chance_count+=1
        
def retry1():
        retry1=input("wanna try again Y or N :")
        count_retry=0
        if retry1.upper()=='Y':
               user_grid()
           
    
def user_grid():
    global input_num
    input_num1=(input("enter available number from grid shown :"))
    try:
        input_num=int(input_num1)
        user_data()
    except ValueError:
        print("invalid entry. Try again")
        user_grid()

def user_data():
    global current_player_val
    if input_num not in range(1,10) or input_num not in check_entry:
        print("available slots",check_entry)
        print("invalid etry")
        print("enter a valid entry not from the grid")
        retry1()
    else:
        check_entry.remove(input_num)
        list9[(input_num)-1]=player_turn
        #clear_output()                           #this is for clearing output . need more work but works in Jupyter notebook
        cls()                                    #this is for regualr IDEs
        print_ttt(list9)
        current_player_val=current_player(user_dict,player_turn) 
        validate(list9,current_player_val)

def main():
    """defining global variable and executing main"""
    global list9
    global check_entry
    global user_dict
    list9 =[1,2,3,4,5,6,7,8,9]
    check_entry =[1,2,3,4,5,6,7,8,9]
    user_dict={'Player1':'Default','Player2':'Default'}
    print("LETS PLAY TIC TAC TOE ")
    print("Below is first TIC TAC TOE format use numbers to input and have fun")
    print_ttt(list9)
    print("getting input variable")
    input_user_role()
    if iur=='X' or iur=='O':
        user_call()

main()

    

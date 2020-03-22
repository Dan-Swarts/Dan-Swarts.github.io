# CSCI 1133, Lab Section 002, HW 3, Problem A
# Daniel Swarts, swart179

#The following program simulates a game of "Rock, Paper, Scissors, Lizzard, Spock" between two people.

def play_game(play1,play2):

    #the following is every permutation
    #'R'=rock,  'P'=paper,  'SC'=scissors,  'SP'=spock,  'L'=lizard
    
    if play1 == 'R' and play2 == 'SC':
        w = 1
    elif play1 == 'R' and play2 == 'L':
        w = 1
    elif play1 == 'P' and play2 == 'R':
        w = 1
    elif play1 == 'P' and play2 == 'SP':
        w = 1
    elif play1 == 'SC' and play2 == 'P':
        w = 1
    elif play1 == 'SC' and play2 == 'L':
        w = 1
    elif play1 == 'SP' and play2 == 'R':
        w = 1
    elif play1 == 'SP' and play2 == 'SC':
        w = 1
    elif play1 == 'L' and play2 == 'P':
        w = 1
    elif play1 == 'L' and play2 == 'SP':
        w = 1
    elif play2 == 'R' and play1 == 'SC':
        w = 2
    elif play2 == 'R' and play1 == 'L':
        w = 2
    elif play2 == 'P' and play1 == 'R':
        w = 2
    elif play2 == 'P' and play1 == 'SP':
        w = 2
    elif play2 == 'SC' and play1 == 'P':
        w = 2
    elif play2 == 'SC' and play1 == 'L':
        w = 2
    elif play2 == 'SP' and play1 == 'R':
        w = 2
    elif play2 == 'SP' and play1 == 'SC':
        w = 2
    elif play2 == 'L' and play1 == 'P':
        w = 2
    elif play2 == 'L' and play1 == 'SP':
        w = 2
    else:
        w = 'T'
    return w







def play_round(list1,list2):
        
    score_1 = 0                                                         
    score_2 = 0                                                          
    round_number = 1                                                  
    
    while score_1 < 2 and score_2 < 2 and round_number <= 3:           #while loop ends the program when someone wins or they tie
                                                                         
                                                                         
        if play_game(list1[round_number],list2[round_number]) == 1:          
            score_1 += 1
            
        elif play_game(list1[round_number],list2[round_number]) == 2:    
            score_2 += 1
            
        round_number += 1

        

    if score_1 > score_2:   
        return 1
    elif score_2 > score_1:
        return 2
    else:
        return 'T'





def main():


    player_1 = [1]
    player_2 = [2]

    round_number = 1
    
    Keep_track1 = 0                             #keep track variables are needed to end the program early if a player wins twice in a row
    Keep_track2 = 0

    while Keep_track1 < 2 and Keep_track2 < 2 and round_number <= 3:

        print("Game {}!\n".format(round_number))
    
        player_1.append(str(input("Rock, Paper, Scissors, SHOOT!!! (Player one, please enter your move): ")))

        player_2.append(str(input("(Player 2, what was your move?)")))

        game_winner = play_game(player_1[round_number],player_2[round_number])

        if game_winner == 1:          
            Keep_track1 += 1
            
        elif game_winner == 2:    
            Keep_track2 += 1

        round_number += 1

        if game_winner == 1 or game_winner == 2:
            print("\nPlayer {} wins that round.\n".format(game_winner))

        else:
            print("That round was a tie! The plot thickens.\n")



    if play_round(player_1,player_2) == 1:
        print("\nPlayer 1 wins!\nhttps://www.youtube.com/watch?v=LA4z7XB1whg")
        
    elif play_round(player_1,player_2) == 2:
        print("\nPlayer 2 wins!\nhttps://www.youtube.com/watch?v=LA4z7XB1whg")
    else:
        print("Its...a draw!?")


if __name__ == "__main__":
    main()
    

    

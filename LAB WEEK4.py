
########################################################################
##
## CS 101 Lab
## Program # WEEK 4 LAB
## Name HASHIM ABDULLA
## Email HIAGKH@UMSYSTEM.edu
##
## PROBLEM : Describe the problem
##
## ALGORITHM :
##1. program asks user number of chips to start with
#2. program asks user how many chips to wager
#3.program randomly generates 3 numbers and checks if any match. if 3 match, a payout of 10x the wager is added to the bank, if 2 match, a payout of 3x
#the wager is added to the bank, if none match, the negative value of wager is subtracted from the bank.
#4. program continues until user loses all chips, then displays in how many spins the user lost all of his/her starting chips, and also displays max amount
#of chips the user had.
#5. program asks user if he/she would like to play again
##
## ERROR HANDLING:
##      Any Special Error handling to be noted.  Wager not less than 0. etc
## chips to start with can only be 1-100
#chips to wager must be above 0 and not greater than how much chips the user has
#to  play again , user must input:yes no n or y (case insensitive)
## OTHER COMMENTS:
##      Any special comments
##
########################################################################
# import modules needed
import random
def play_again():
    play=input("do you want to play again?")
    playy=play.upper()
    while playy !="NO" and playy!="N" and playy!="YES" and playy!="Y":
        print("You must enter Y/YES/N/NO to continue. Please try again")
        playy=input("do you want to play again?")
        playy=playy.upper()
    if playy=="YES" or playy=="Y":
        return True
    elif playy=="NO" or playy=="N":
        return False




def get_wager(bank: int) -> int:
    chips=int(input("How many chips do you want to wager?"))
    while chips<=0 or chips>bank:
        print("must be greater than 0 and less than or equal to the bank")
        chips=int(input("How many chips do you want to wager?"))
    return chips


def get_slot_results() -> tuple:
    one=random.randint(1,10)
    two=random.randint(1,10)
    three=random.randint(1,10)
    return one, two, three



def get_matches(reela, reelb, reelc) -> int:
    if reela==reelb==reelc:
        return 3
    elif reela==reelb or reela==reelc or reelb==reelc:
        return 2
    else:
        return 0


def get_bank() -> int:
    global start
    start = int(input("How many chips do you want to start with?"))
    while start <= 0 or start >= 101:
        print(" must be greater than 0 and less than 101")
        start = int(input("How many chips do you want to start with?"))

    return start


def get_payout(wager, matches):
    if matches == 3:
        return wager * 10
    elif matches == 2:
        return wager * 3
    elif matches == 0:
        return wager * -1


if __name__ == "__main__":
    playing = True
    while playing:
        bank = get_bank()
        first_bank=bank
        spin=0
        chipslist=[]
        chipslist.append(first_bank)
        while bank>0:  # Replace with condition for if they still have money.
            wager = get_wager(bank)
            reel1, reel2, reel3 = get_slot_results()
            matches = get_matches(reel1, reel2, reel3)
            payout = get_payout(wager, matches)
            bank = bank + payout
            print("Your spin", reel1, reel2, reel3)
            print("You matched", matches, "reels")
            print("You won/lost", payout)
            print("Current bank", bank)
            print()
            spin=spin+1
            chipslist.append(bank)

        print("You lost all", first_bank, "in", spin, "spins")
        print("The most chips you had was", max(chipslist))
        playing = play_again()

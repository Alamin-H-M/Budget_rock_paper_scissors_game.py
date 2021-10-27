import random
def main():
    computer = random.randint(1, 3)

    player = int(input("Rock(1), Paper(2) or Scissors(3)?: "))

    if computer == 1 and player == 1:
        print("Computer: Rock and You: Rock  DRAW! 🤐")
    elif computer == 1 and player == 2:
        print("Computer: Rock and You: Paper     YOU WIN! 😀")
    elif computer == 1 and player == 3:
        print("Computer: Rock and You: Scissor   YOU LOSE! 😂")
    
    elif computer == 2 and player == 1:
        print("Computer: Paper and You: Rock     YOU WIN! 😀")
    elif computer == 2 and player == 2:
        print("Computer: Paper and You: Paper    DRAW! 🤐")
    elif computer == 2 and player == 3:
        print("Computer: Paper and You: Scissor  YOU LOSE! 😂")
    
    elif computer == 3 and player == 1:
        print("Computer: Scissor and You: Rock   YOU WIN! 😀")
    elif computer == 3 and player == 2:
        print("Computer: Scissor and You: Paper  YOU LOSE! 😂")
    elif computer == 3 and player == 3:
        print("Computer: Scissor and You: Scissor    DRAW! 🤐")
    else:
        print("INVALID INPUT!😑")        
while True:
    main()
    ask = input("\n\nDo you want to continue this game? (Y)es or (N)o : ")
    if ask.lower() == "y":
        continue
    elif ask.lower() == "n":
        break
    else:
        print("INVALID INPUT!😑")
        break 

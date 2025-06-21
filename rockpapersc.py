import random
l=["rock",'paper',"scissor"]
computer=random.choice(l)

choice=0
while choice<5:
    
    gamer=input("enter your choice in the game:")

    if computer==gamer:
        print(f"your choice{gamer}is win, well done ")
        print("computer choice",computer)
    else:
        print(f"computer choice {computer}  you are loose try again.")

        
    break



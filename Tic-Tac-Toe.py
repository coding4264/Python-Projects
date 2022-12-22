import random
part1 = "_|"
part2 = "_|"
part3 = " |"
part4 = "_"
part5 = "_"
part6 = ""
part7 = "|_"
part8 = "|_"
part9 = "| "
class Player:
    print(part1,part4,part7,"\n")
    print(part2,part5,part8,"\n")
    print(part3,part6,part9)
    global space
    space = int(input("What space are you gonna take?"))
    def turn():
        if space == 1:
            part1 = ("_0|")
        elif space == 2:
            part2 = ("_0|")
        elif space == 3:
            part3 = ("0|")
        elif space == 4:
            part4 = ("0_")
        elif space == 5:
            part5 = ("0_")
        elif space == 6:
            part6 = ("0")
        elif space == 7:
            part7 = ("|0_")
        elif space == 8:
            part8 = ("|0_")
        else:
            part9 = ("|0")
    turn()
class AI:
    global aispace
    aispace = random.randrange(1,9)
    def aiturn():
        if space == 1:
            part1 = ("_x|")
        elif aispace == 2:
            part2 = ("_x|")
        elif aispace == 3:
            part3 = ("x|")
        elif aispace == 4:
            part4 = ("x_")
        elif aispace == 5:
            part5 = ("x_")
        elif aispace == 6:
            part6 = ("x")
        elif aispace == 7:
            part7 = ("|x_")
        elif aispace == 8:
            part8 = ("|x_")
        else:
            part9 = ("|x")
    aiturn()
print(part1,part4,part7,"\n")
print(part2,part5,part8,"\n")
print(part3,part6,part9)
calories = int(input("How much calories would you like to burn?\n"))
time = int(input("How long is this diet?(in days)\n"))
method = input("What Method would you like to use?\n")
#⬆ Type your method in only one word.
#It has to be either bycicle, excersise or the gym
def diet():
    long = calories / 9.9
    int(long)

    if method == "bike":
        print("With your method, you`re gonna have to bike for ", long, " Minutes")

    elif method == "excersise":
        print("With your method, you`re gonna have to excersise for ", calories / time , " minutes")

    elif method == "gym":
        print("With your method, you`re gonna have to burn ", calories / time , " calories everyday.")

diet()
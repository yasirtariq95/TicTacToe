def inputs(numberList, boxCount):
    choice = input("Enter your block choice: ")
    print()
    print("NOTE: ONLY ENTER 'X' OR 'O'")
    entry = input("Enter either noght or cross: ")
    print()
    game_functionality(choice, entry, numberList, boxCount)

def display(numberList, boxCount, entry):
    print("    | " + " " + " |")
    print(" " + numberList[0] + "  | " + numberList[1] + " |  " + numberList[2])
    print("    | " + " " + " |")
    print("---------------")
    print("    | " + " " + " |")
    print(" " + numberList[3] + "  | " + numberList[4] + " |  " + numberList[5])
    print("    | " + " " + " |")
    print("---------------")
    print("    | " + " " + " |")
    print(" " + numberList[6] + "  | " + numberList[7] + " |  " + numberList[8])
    print("    | " + " " + " |")
    print()

    showResult(numberList, entry)

    if boxCount < 8:
        boxCount += 1
        inputs(numberList, boxCount)

    else:
        print("Draw!")

def game_functionality(choice, entry, numberList, boxCount):
    choices = ["r11", "r12", "r13", "r21", "r22", "r23", "r31", "r32", "r33"]
    entries = ["X", "O"]
    if choice not in choices:
        print("Please enter the right entry block from the above list")
        print()
        inputs(numberList, boxCount)
    elif entry not in entries:
        print("Please either enter 'X' OR 'O'")
        print()
        inputs(numberList, boxCount)
    else:
        if choice == "r11":
            numberList[0] = entry
            display(numberList, boxCount, entry)
        if choice == "r12":
            numberList[1] = entry
            display(numberList, boxCount, entry)
        if choice == "r13":
            numberList[2] = entry
            display(numberList, boxCount, entry)
        if choice == "r21":
            numberList[3] = entry
            display(numberList, boxCount, entry)
        if choice == "r22":
            numberList[4] = entry
            display(numberList, boxCount, entry)
        if choice == "r23":
            numberList[5] = entry
            display(numberList, boxCount, entry)
        if choice == "r31":
            numberList[6] = entry
            display(numberList, boxCount, entry)
        if choice == "r32":
            numberList[7] = entry
            display(numberList, boxCount, entry)
        if choice == "r33":
            numberList[8] = entry
            display(numberList, boxCount, entry)

def showResult(numberList, entry):

    if (numberList[0] == numberList[1] == numberList[2] == entry or
            numberList[3] == numberList[4] == numberList [5] == entry or
            numberList[6] == numberList[7] == numberList [8] == entry or
            numberList[0] == numberList[3] == numberList [6] == entry or
            numberList[1] == numberList[7] == numberList [4] == entry or
            numberList[2] == numberList[5] == numberList [8] == entry or
            numberList[0] == numberList[4] == numberList [8] == entry or
            numberList[2] == numberList[4] == numberList [6] == entry):
        print("Congratulations! You have won the game!")
        exit()

    # else:
    #     print("Draw!")

if __name__ == '__main__':
    print("Please choose from the following list, where you want to add your entry")
    print("[r11, r12, r13, r21, r22, r23, r31, r32, r33]")
    print()
    print("############################# For Example #############################")
    print("If you want to add your entry in the second row second block then choose r22. It will add your entry in the table and the table will look"
          " like the following")
    print()
    print("    | " + " " + " |")
    print("    | " + " " + " |")
    print("    | " + " " + " |")
    print("---------------")
    print("    | " + " " + " |")
    print("    | " + "X" + " |")
    print("    | " + " " + " |")
    print("---------------")
    print("    | " + " " + " |")
    print("    | " + " " + " |")
    print("    | " + " " + " |")
    print()
    numberList = list(str(" ") * 9)
    boxCount = 0
    inputs(numberList, boxCount)
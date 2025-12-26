# Setup
BOLD = '\033[1m'
RED = '\033[31m'
GREEN = '\033[32m'
END = '\033[0m'

GBOLD = BOLD + GREEN
RBOLD = BOLD + RED

while True:
    UserInput = input(f"Keep the halt value at {GBOLD}512{END}? (press Enter or n)(or Exit):")
    if UserInput.lower() == "n":
        HaltValue = int(input("Enter Halt Value: "))
    elif UserInput == "":
        HaltValue = 512
    elif UserInput.lower() == "exit":
        print(f"============={RBOLD}Exiting Program.{END}============")
        break  
    else:
        print(RED + BOLD + "Error in Halt Value Input" + END)
        exit()

    ServoValue = int(input(f"Enter {BOLD}Servo Value{END}: "))


    if ServoValue > HaltValue:
        move = ServoValue - HaltValue
        ServoMoveA = HaltValue - move
        ServoMoveB = HaltValue + move
        print(f"\n==========HALT VALUE: {BOLD}{HaltValue}{END} ==========\nServoMoveA: {GBOLD}{ServoMoveA}{END}(Servo Move: -{move})\nServoMoveB: {RBOLD}{ServoMoveB}{END}(Servo Move: +{move})\n")
    elif ServoValue < HaltValue:    
        move = HaltValue - ServoValue
        ServoMoveA = HaltValue - move
        ServoMoveB = HaltValue + move
        print(f"\n==========HALT VALUE: {BOLD}{HaltValue}{END} ==========\nServoMoveA: {RBOLD}{ServoMoveA}{END}(Servo Move: +{move})\nServoMoveB: {GBOLD}{ServoMoveB}{END}(Servo Move: -{move})\n")
    elif ServoValue == HaltValue:
        ServoMoveA = HaltValue
        ServoMoveB = HaltValue
        print(f"\n==========HALT VALUE: {BOLD}{HaltValue}{END} ==========\nServoMoveA: {GBOLD}{ServoMoveA}{END}(No Move)\nServoMoveB: {GBOLD}{ServoMoveB}{END}(No Move)\n")
    else:
        print(RED + BOLD + "Error in Servo Degree Calculation" + END)



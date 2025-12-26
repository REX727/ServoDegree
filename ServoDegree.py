# Setup
BOLD = '\033[1m'
RED = '\033[31m'
GREEN = '\033[32m'
END = '\033[0m'


ServoD = int(input("Enter servo degree: "))


while True:
    if ServoD > 512:
        ServoDC = ServoD - 512
        ServoDCon = 512 - ServoDC
        print(f"Servo Degree after converted: {BOLD}{GREEN}{ServoDCon}{END}")
    elif ServoD < 512:
        ServoDC = 512 - ServoD
        ServoDCon = 512 + ServoDC
        print(f"Servo Degree after converted: {BOLD}{GREEN}{ServoDCon}{END}")
    elif ServoD == 512:
        ServoDCon = 512
        print(f"Servo Degree after converted: {BOLD}{GREEN}{ServoDCon}{END}")
    else:
        print("Invalid input for servo degree.")
    ServoD = int(input("Enter servo degree: "))

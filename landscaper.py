landscaper = {"tool": 0, "money": 0}

tools = [
    {"item": "teeth", "money earned": 1, "cost": 0},
    {"item": "rusty scissors", "money earned": 5, "cost": 5},
    {"item": "old-timey push lawnmower", "money earned": 50, "cost": 25},
    {"item": "battery-powered lawnmower", "money earned": 100, "cost": 250},
    {"item": "starving students", "money earned": 250, "cost": 500}
]

def cut_lawn():
    tool = tools[landscaper["tool"]]
    next_tool = tools[landscaper["tool"] + 1]
    print(f"You successfully cut a lawn with your {tool['item']} and earned ${tool['money earned']} you now have {landscaper['money']}!")

    landscaper["money"] += tool["money earned"]
    
    if(landscaper["money"] >= next_tool["cost"]):
        print(f"You now have enough money to upgrade to {next_tool['item']}, it will cost ${next_tool['cost']}")

def upgrade():
    if (landscaper["tool"] >= len(tools) - 1):
        print("No more upgrades available")
        return 0
    next_tool = tools[landscaper["tool"] + 1]
    if (next_tool == None):
        print("No more tools to upgrade")
        return 0
    if (landscaper["money"] < next_tool["cost"]):
        print("Get your money up not your funny up... you dont have enough money to upgrade")
        return 0
   
    print("You have successfully upgraded your tool")
    landscaper["money"] -= next_tool["cost"]
    landscaper["tool"] += 1

def quit_game():
    print("You have quit the game")
    return 0
    
def win_condition():
    if(landscaper["tool"] == len(tools) - 1 and landscaper["money"] >= 1000):
        print("You have won the game!")
        return True
    return False

while (True):

    result = input("Do you want to [c]ut lawn, [u]pgrade, or [q]uit?")

    if result == "c":
        cut_lawn()
    
    if result == "u":
        upgrade()
    
    if result == "q":
        quit_game()
        break

    if(win_condition()):
        break

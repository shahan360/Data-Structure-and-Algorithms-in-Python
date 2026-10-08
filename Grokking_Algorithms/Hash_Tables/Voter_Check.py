voted = {}
def check_voter(name):
    if voted.get(name):
        print("Kick them out!")
    else:
        voted[name] = True
        print("Let them vote!")

# Test the function
check_voter("Tom")
check_voter("Jerry")
check_voter("Tom")
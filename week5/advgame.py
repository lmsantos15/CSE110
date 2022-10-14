# 05 Prove: Milestone - Adventure Game

print()
# Text-based Adventure Game

intro = input("You are walking through a dark forest and find two items: a MATCH and a FLASHLIGHT. Which one do you want to pick up? ")

print()
# Action 1 Match
if intro.lower() == "match":
    actions = input("You pick up the match and strike it, and for an instant, the forest around you is illuminated. You see a large grizzly bear, and then the match burns out. Do you want to RUN, HIDE behind a tree, or FIGHT? ")
    print()
    # Run
    if actions.lower() == "run":
        print("Run! Do not stop until you get to safety. \n")
    # Hide
    elif actions.lower() == "hide":
        print("Make yourself as small as you can. As soon as you decide on a hiding spot, crouch, stoop, or sit down and draw your arms and legs in. \n")
    # Fight       
    elif actions.lower() == "fight":
        print("Grab something that will make you look big. While backing away look for a branch that you can use to defend your self. \n")       
    else:
        print("Try to call the Police and ask for help. \n")

    # Action 2 Flashlight        
elif intro.lower() == "flashlight":
    print()
    actions1 = input("You pick up the flashlight and turn it on. You see the pathway lit up in front of you, but you thought you also heard something off to the side. Do you want to FOLLOW the path, LOOK in the trees for the thing that made the noise, or TURN AROUND and go home? ")
    print()
    # Follow
    if actions1.lower() == "follow":
        print("Walk carefully and be mindful of your surroundings. \n")
    # Look
    elif actions1.lower() == "look":
        print("Follow the noise and make sure not to provoke it. \n")
    # Turn Around
    elif actions1.lower() == "turn around":
        print("Turn around and go home. \n")

    else:
        print("Send your geo location to your friends or family members. \n")
   
    # Last option
else:
    print("Stay still and don't make any noise—you're trying to convince the bear that you aren't a threat to it or its cubs. \n")






# This is the code for the Hormone Adventure Game.       
import tkinter
import tkinter.messagebox
# Game Set-up
characters = ["GHRH", "CRH", "TRH", "Parathyroid Hormone", "Inactive Vitamin D"]
answer = 0
angry = 0


def adrenal_pathway(response, answer, angry):
    '''The following function is for the Adrenal Hormone Pathway. Thee overall steps are:
    1. Hypothalamus releases CRH
    2. Binding to APG releases ACTH
    3. Binding to Adrenal Cortex releases Cortisol'''
    
    # STEP ONE: Hypothalamus releases CRH.
    print("\nYou awaken in the Hypothalamus carrying Cortisol Releasing Hormone (CRH). Motivated by circadian rhythm and stress,"\
    " you know\nthat you must move forward. The path before you leads to the Anterior Pituitary Gland (APG) door."\
    "\nWould you like to inspect the door?")
    c1 = input( "yes or no: ")
    while answer != 1:
        if c1 == 'yes':
            print("\nThe door to the Anterior Pituitary Gland has a hole labled CRH. You insert the CRH and the door opens.")
            answer = 1
        else:
            if angry != 2:
                print("\nYou stand there doing nothing. You should look at the door, there might be something interesting."\
                "\nWould you like to inspect the door?")
                answer = 0
                c1 = input("yes or no: ")
                angry += 1
            else:
                print("\nPlease say yes. It looks very interesting. Would you like to inspect the door?")
                c1 = input("yes or no: ")  

    # Reset variables:
    answer = 0
    angry = 0
    altar = 'no'

    # STEP TWO: Binding to APG releases ACTH.
    print("\nYou recover the CRH and walk through the APG door and you see a small room. In the center of the room,\nthere is a small altar"\
    "and another door on the far end of the room. What would you like to inspect?")
    c1 = input("Choose altar or door: ")
    while answer != 2:
        if c1 == "altar" and altar == 'no':
            print("\nYou inspect the altar and see a slot just big enough for CRH. Would you like to insert the CRH?")
            c2 = input("yes or no: ")
            while altar != 'yes':
                if c2 == "yes":
                    print("\nThe CRH perfectly slides into the slot and ejects an ACTH molecule, just like a Gacha pod."\
                    "\nNow you can inspect the door.")
                    answer += 1
                    altar = 'yes'
                    c1 = "door"
                else:
                    if angry != 2:
                        print("\nYou stand there doing nothing. You should look at the altar, there might be something interesting."\
                        "\nWould you like to inspect the altar?")
                        c2 = input("yes or no: ")
                        angry += 1
                    else:
                        print("\nPlease say yes. It looks very interesting. Would you like to inspect the altar?")
                        c2 = input("yes or no: ")
                        altar = 'no'
        
        # Reset variables:
        angry = 0  

        if c1 == "door":
            if altar == 'no':
                print("\nYou have no power here. Go to the altar instead!")
                c1 = "altar"
            if altar == 'yes':
                print("The door is labeled ACTH. Would you like to place the ACTH in the key slot?")
                c2 = input("yes or no: ")
                answer += 1
                if c2 == "yes":
                    print("\nThe ACTH opens the door, and you are led to the Adrenal Cortex.")
                else:
                    while c2 != 'yes':
                        if angry != 2:
                            print("\nYou stand there doing nothing. You should look at the door, there might be something interesting."\
                            "\nWould you like to inspect the door?")
                            c2 = input("yes or no: ")
                            angry += 1
                        else:
                            print("\nPlease say yes. It looks so mystical and inviting. Would you please just inspect the door?")
                            c2 = input("yes or no: ")
        else:
            c1 = input("What? ")
    
    # Reset variables:
    answer = 0
    angry = 0
    tim = 'no'

    # Step 3: Binding to Adrenal Cortex releases Cortisol.
    print("\nYou recover the ACTH and walk to the Adrenal Cortex. Inside the Adrenal Cortex lurks a mysterious skeleton."\
    "\nBehind the skeleton lies another door...\nYou can sneak around or approach the skeleton, what will you do?")
    c1 = input("sneak or approach: ")
    while answer != 2:
        if c1 == "approach" and tim == 'no':
            print("\nYou slink towards the cobwebbed skeleton and realize its hand is outstretched."\
            " Do you give the skeleton your ACTH?")
            c2 = input("yes or no: ")
            while tim != 'yes':
                if c2 == "yes":
                    print("\nYou hand over ACTH, which slowly disappears as the skeleton rattles and hands you Cortisol.")
                    answer += 1
                    tim = 'yes'
                    c1 = "sneak"
                else:
                    if angry != 2:
                        print("\nYou stand there doing nothing while the skeleton stares blankly at you."\
                        "\nWould you like to approach the skeleton?")
                        c2 = input("yes or no: ")
                        angry += 1
                    else:
                        print("\nThe skeleton hasn't seen people in ages, he's very lonely. Please approach him."\
                        " Would you like to approach it?")
                        c2 = input("yes or no: ")
                        tim = 'no'
        
        # Reset variables:
        angry = 0  

        if c1 == "sneak":
            if tim == 'no':
                print("\nThe door is locked, maybe the skeleton has the key.")
                c1 = "approach"
            if tim == 'yes':
                closing = "You hear the doors behind you close in succession upon obtaining Cortisol."\
                "\nNo more adventurers will be able to follow the path you tred, because you have obtained Cortisol and no more is needed."\
                "\nThus, all previous steps are closed off. This is known as a negative feedback loop."\
                "\n..."\
                "\nCarrying Cortisol, you now exit through the door and travel throughout the body."\
                "\nCortisol proves to be powerful and have a variety of effects."\
                "\nThe Immune systyem becomes suppressed, gluconeogenesis occurs in the liver,"\
                "\nprotein catabolism occurs in the muscle, and lipolysis occurs in the adipose tissue."\
                "\nThe End!"
                answer += 1
        else:
            c1 = input("What? ")
    return closing


# Prompt user to choose an adventure
print("Welcome to the Hormone Adventure Game. This is the list of possible starting Hormones:")
print(characters)
response = input("Please choose a Hormone: ")
if response == "CRH":
    closing = adrenal_pathway(response, answer, angry)
    print(closing)
else:
    print('\nSike. You can only start with CRH. It is the only one.')
    closing = adrenal_pathway(response,answer,angry)
    print(closing)
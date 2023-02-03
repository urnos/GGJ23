# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define p = Character("Plant")
define v = Character("Villainess")

transform right:
    xalign 0.75
    yalign 1.0


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    p "The garden is warm and quiet, with the faint noise of fountains bubbling on the other end of the house."

    p "The silence is comforting when you think about it."

    p "But it can drive a plant mad."

    p "If you've lived in this house for as long as I have, you would understand how lonely it can be."
     
    p "Especially when you're surrounded by hundreds of your own kind."
     
    p "Nobody listens to me."
     
    p "I've tried calling out for days but no luck finding someone."
    
    p "Even the humans that tend to us."
    
    p "I can't get their attention at all."
    
    p "If only I could just have one conversation."
    
    p "Someone to talk to."

    "Click."

    p "Who's that?"

    show eileen happy at right

    p "Is that the duchess?"

    # This ends the game.

    return

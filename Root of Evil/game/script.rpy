# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define p = Character("Plant", color="#7CFC00")
define v = Character("Villainess", color="#880808")

define q1 = False
define q2 = False

define react1_good = False

transform right:
    xalign 0.75
    yalign 1.0


# Introduction scene, Main plot point 1

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

    "{i}Click.{/i}"

    p "Who's that?"

    show eileen happy at right

    p "Is that the duchess?"

    p "What's she doing here?"

    p "I've seen her around before. She visits the garden pretty often."

    p "I hear the gardeners talk about her when she's not around."

    p "Most of the time they say how cold she can be but I don't understand why?"

    p "How can someone be cold? It's so warm inside."

    p "Oh! She's coming."

    v "I can't believe him. After all the effort I put into this gown."

    v "Not even a glance. A head turn would have been enough for me."

    p "Did something happen?"

    v "{i}Sigh{/i}. I don't understand why he didn't look at me today."

    v "Hm? is this a new plant?"

    v "I've never seen you before."


   
label mpp1_interview:
    #interview segment

    menu: 
        v "What did you want to talk about?"

        "Who's He?" if q1 == False:
            jump who_he

        "What's a gown?" if q2 == False:
            jump what_gown

    if q1 == True and q2 == True:
        jump idk_1


#option 1: who's he?
label who_he: 
    v "I was referring to my fiance."

    $ q1 = True

    jump mpp1_interview

#option 2: what's a gown?
label what_gown: 
    v "A gown is what I'm wearing right now."

    $ q2 = True

    jump mpp1_interview


label idk_1:
    v "I just wish he paid attention to me today."
    v "He seemed so distant tonight."
    v "What should I do?"
    
    #reaction choices
    menu:

        "Move on":
            jump move_on

        "Confront":
            jump confront

#option 1: move on (good)
label move_on:
    p "From what I heard, it sounds like it might be your imagination."

    $ react1_good = True

    jump mpp1_end

#option 2: confront (bad)
label confront:
    p "From what I heard, I think you should talk to him about it."

    $ react1_good = False

    jump mpp1_end

label mpp1_end:
    v "You know, I never would have thought talking to a plant would make me feel better."
    p "Anytime! I'm happy to help."
    v "Would you be willing to talk again?"
    p "Always!"
    v "Perhaps I will keep our conversations a secret, who knows how other people will react to find that I talk to plants when I'm alone, haha."

    jump mpp2_start

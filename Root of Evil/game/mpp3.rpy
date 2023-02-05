# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# Main plot point 3

label mpp3_start:
    play music bg_default

    scene bg_greenhouse
    with fade

    p "I haven't heard from the Duchess since yesterday."
    p "Hope she comes back and tells me what happens."
    p "It feels good to feel such a connection to someone."

    stop music fadeout 1.2

    play sound sfx_click
    "{i}Click.{/i}"

    show exp_p_question onlayer screens at plant_bubble zorder 1
    p "Is she back?"
    hide exp_p_question onlayer screens
    p "I hear more footsteps this time."
    p "Wonder if the gardeners are back."

    play music bg_finale

    show villainess_default at right
    with dissolve
    v "Ok, we're alone now. What did you want to talk about?"

    show exp_p_question onlayer screens at plant_bubble zorder 1
    p "Is that the Duchess? Who is she talking to?"
    hide exp_p_question onlayer screens

    f "I heard what happened yesterday."

    v "What are you talking about?"

    f "You think I wouldn't hear about it?"

    v "I'm not sure I know what you are talk-"

    f "That you slapped her?"

    show exp_v_exclaim at right_bubble behind villainess_default
    v "!!"
    hide exp_v_exclaim
    v "Wha-"

    f "You harrased her! I can't believe yo-'"

    show exp_v_exclaim at right_bubble behind villainess_default
    v "You can't believe me?! I can't believe your behaviour recently!"
    v "Jumping to her aid instead of your actual fiancee. Your wife-to-be."
    v "You're always with her!"
    hide exp_v_exclaim

    v "You think I wouldn't notice!"
    v "How awfully close the two of you are..."

    f "..."

    v "Would you care to explain yourself on why you seem to care more for her than me?"

    f "That's exactly what I'm here to talk to you about."

    show exp_v_question at right_bubble behind villainess_default
    v "...?"
    hide exp_v_question

    f "You're right, the two of us are close."
    f "I've only known her for a short period of time but I feel closer to her than I've ever felt with you in our entire relationship."

    v "What are you saying...."

    f "I love her."

    show exp_v_exclaim at right_bubble behind villainess_default
    v "!!"
    hide exp_v_exclaim

    f "She knows the real me."
    f "..."
    f "I want to annul our engagement agreement."
    f "We're no longer getting married."

    show exp_v_exclaim at right_bubble behind villainess_default
    v "!!!!!"
    hide exp_v_exclaim

    f "I apologize for not saying anything sooner."
    f "I don't want you to misunderstand me."
    f "I can't lie to myself anymore. I want to be with her."
    f "Farewell."

    p "He's leaving."
    show exp_p_question onlayer screens at plant_bubble zorder 1
    p "What's that in the Duchess' hand?"
    p "A gardening knife?"
    hide exp_p_question onlayer screens
    p "There's something radiating off the Duchess."
    p "And it's resonating inside of...."

    v "Hah...Hah...."
    v "Where do you think you're going?"
    v "You can't just walk away from me like this."
    v "I can't give you up so easily."
    v "I refuse."
    v "To let."
    v "Anybody else..."
    v "H A V E Y O U!!!"
    stop music

    jump fiance_gone



label fiance_gone:
    scene bg_black
    with fade
    
    play sound sfx_stab 

    "{i}S H A N K !{/i}"
    
    play music sfx_heartbeat

    f "Agh!"
    f "!!!"
    f "I...I..I'm..."
    f "...S...So....r...ry..."

    play sound sfx_thud

    "{i}Thud{/i}"

    show villainess_default at right with dissolve 
    show exp_v_exclaim at right_bubble behind villainess_default
    v "!!!!!!!"
    hide exp_v_exclaim
    v "W-Wha...."
    v "What...."
    v "What happened to you?"

    p "Thanks to you."
    p "I was finally able to grow big and strong."

    v "Y...You...Killed...H-"
    v "..Why?"

    stop music

    play sound sfx_noqanda

    #reaction choices
    menu:
  
        "Isn't this what you wanted?":
            jump mpp3_end



#Option 1: Isn't this what you wanted?
label mpp3_end:
    p "Thanks to you."
    p "I can finally."
    p "Bloom."       

    #END
    #We can put an ending card here if we want, otherwise it just goes back to the title screen ^^
    scene bg_endcard
    $ renpy.pause () 

    # This ends the game.
    return



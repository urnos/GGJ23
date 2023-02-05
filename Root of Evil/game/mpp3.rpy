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
    p "It feels good to feel such a connection to someone..."

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

    v "Ok, we're alone now."
    
    show exp_v_question at right_bubble behind villainess_default
    v "What did you want to talk about?"
    hide exp_v_question

    show exp_p_question onlayer screens at plant_bubble zorder 1
    p "Is that the Duchess? Who is she talking to?"
    hide exp_p_question onlayer screens

    f "I heard what happened yesterday."

    show exp_v_question at right_bubble behind villainess_default
    v "What are you talking about?"
    hide exp_v_question

    f "You think I wouldn't hear about it?"

    v "I'm not sure I know what you are talk-"

    f "That you slapped her?!"

    show exp_v_exclaim at right_bubble behind villainess_default
    v "!!"
    hide exp_v_exclaim
    v "Wha-"

    f "You harrased her! I can't believe yo-'"

    show exp_v_exclaim at right_bubble behind villainess_default
    v "You can't believe me?! I can't believe your behaviour recently!"
    v "Jumping to her aid instead of your actual fiancee. Your wife-to-be."
    v "You're always with her!"
    v "You think I wouldn't notice!"
    hide exp_v_exclaim

    v "How awfully close the two of you are..."

    f "..."

    show exp_v_question at right_bubble behind villainess_default
    v "Would you care to explain yourself on why you seem to care more for her than me?"
    hide exp_v_question

    f "That's exactly what I'm here to talk to you about."

    show exp_v_question at right_bubble behind villainess_default
    v "...?"
    hide exp_v_question

    f "You're right, the two of us are close."
    f "I've only known her for a short period of time but I feel closer to her than I've ever felt with you in our entire relationship."

    show exp_v_question at right_bubble behind villainess_default
    v "What are you saying...."
    hide exp_v_question

    f "I love her."

    show exp_v_exclaim at right_bubble behind villainess_default
    v "!!"
    hide exp_v_exclaim

    f "She knows the real me."
    f "..."
    f "I want to annul our engagement agreement."

    show exp_v_exclaim at right_bubble behind villainess_default
    v "!!!!!"
    hide exp_v_exclaim

    f "I apologize for not saying anything sooner."
    f "I don't want you to misunderstand me."
    f "I can't lie to myself anymore. I want to be with her."
    f "Farewell."

    p "{i}He's leaving.{/i}"
    show exp_p_question onlayer screens at plant_bubble zorder 1
    p "{i}What's that in the Duchess' hand?{/i}"
    p "{i}A gardening knife?{/i}"
    hide exp_p_question onlayer screens
    p "{i}There's something radiating off the Duchess.{/i}"
    p "{i}And it's resonating inside of....{/i}"

    v "Hah...Hah...."

    v "Where do you think you're going?"
    v "You can't just walk away from me like this!"
    v "I can't give you up so easily!"
    v "{b}{i}I refuse..."
    v "{b}{i}To let..."
    v "{b}{i}Anybody else..."
    v "{size=+10}{b}{i}H A V E {space=10} Y O U!!!{/i}{/b}{/size}"

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
    p "Now..."
    p "I can finally..."

    hide villainess_default at right with dissolve
    play sound sfx_scream fadeout 0.25

    p "{b}{i}{size=+10}Bloom.{/i}{/b}{/size}"       
    

    #END
    #We can put an ending card here if we want, otherwise it just goes back to the title screen ^^
    scene bg_endcard
    $ renpy.pause () 

    # This ends the game.
    return



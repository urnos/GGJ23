# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# Main plot point 2

label mpp2_start:

    play music bg_default

    scene bg_greenhouse

    p "It's been some time since the Duchess began to visit me in the garden."
    p "She always comes in the day when nobody else is around. Usually telling others to leave if they end up hearing our conversations."
    p "She's explained to me what life is like outside the garden."
    p "I've learned a lot since I started speaking with her."
    p "Sometimes she'll ask me questions, like how to take care of me."
    p "The best way to care for a plant like me is to keep on talking to me, talking to someone always makes me feel better."
    p "That way I can grow and learn like I've always wanted."

    stop music fadeout 1.2

    play sound sfx_click

    "{i}Click.{/i}"

    show exp_p_joy onlayer screens at plant_bubble zorder 1
    p "{i}She's here!{/i}"
    hide exp_p_joy onlayer screens

    p "{i}I sense strong emotions coming from her direction.{/i}"

    play music bg_v_jealous fadein 1.2

    show villainess_default at right
    with dissolve

    show exp_v_angry at right_bubble behind villainess_default
    v "Who does he think he's taking to?!"
    v "Defending a girl over your own fiance?"
    v "The tea wasn't even being spilled on purpose she just happened to be in the way when the pot tipped over."
    v "And he thinks he can just accuse me without even trying to listen."
    v"The nerve of that girl playing the victim!"
    hide exp_v_angry

    show exp_p_question onlayer screens at plant_bubble zorder 1
    p "What's wrong?"
    hide exp_p_question onlayer screens

    show exp_v_angry at right_bubble behind villainess_default
    v "That stupid girl thinks she can get away with this, I can't believe her."
    hide exp_v_angry

    v "You won't believe what happened."
    v "We were all enjoying ourselves for a small gathering of afternoon tea."
    v "When I only knocked over the tea pot in her direction and it spilled all over her."

    show exp_p_question onlayer screens at plant_bubble zorder 1
    p "{i}Tea?{/i}"
    hide exp_p_question onlayer screens

    show exp_v_exclaim at right_bubble behind villainess_default
    v "Then my fiance suddenly accuses me that I spilt it on purpose!"
    hide exp_v_exclaim

    v "Not even giving me a chance to explain."

    show exp_v_angry at right_bubble behind villainess_default
    v "Then he goes up and leaves with the girl, leaving me all alone."
    hide exp_v_angry

    v "How could he?"
    v "He's been acting very friendly with her recently...."
    v "...."
    v "Could he be...."
    v "No, he wouldn't even think about leaving me for her."
    v "We're engaged for goodness sake."

    show exp_p_question onlayer screens at plant_bubble zorder 1
    p "{i}Who's leaving?{/i}"
    hide exp_p_question onlayer screens

    v "I have an underlying suspicion that my fiance may be have a relationship with someone else."
    v "And with the wedding soon approaching!"
    v "He wouldn't!"

    show exp_v_question at right_bubble behind villainess_default
    v "Would he...?"
    hide exp_v_question

    p "{i}Her emotions are so strong today.{/i}"
    p "{i}It's good that she's letting her feelings out.{/i}"

    stop music fadeout 1.0

    play sound sfx_qanda fadein 0.1 

    $ q1 = False
    $ q2 = False

    jump mpp2_interview

    label mpp2_interview:
    #interview segment

    #when the sfx is done then fade in bgm music

    define qa2bgm_isPlaying = False
    #start the track only if the q&a bgm isn't playing
    if qa2bgm_isPlaying == False:
        play  music bg_mpp2_qanda fadeout 1.5 fadein 2.0 volume 0.5
        #turn q&a music toggle on 
        $ qa2bgm_isPlaying = True

    menu: 

        "Who is the girl?" if q1 == False:
            jump who_girl

        "Can you share him" if q2 == False:
            jump share_him

    if q1 == True and q2 == True:
        jump question_finish_2


    label who_girl:
        v "That girl, is my lady in waiting."
        v "A personal assistant."

        show exp_p_question onlayer screens at plant_bubble zorder 1
        p "Assistant?"
        hide exp_p_question onlayer screens

        v "Someone who helps me take care of responsibilities."
        v "I noticed that she seems to be getting fairly close with my fiance."

        show exp_v_exclaim at right_bubble behind villainess_default
        v "He seemed more upset about the tea than she was!"
        hide exp_v_exclaim

        show exp_p_question onlayer screens at plant_bubble zorder 1
        p "What's tea?"
        hide exp_p_question onlayer screens

        v "It's a type of liquid you drink. Just like how you drink water."

        show exp_p_question onlayer screens at plant_bubble zorder 1
        p "Really? Then why would he get upset about that?"
        hide exp_p_question onlayer screens
        p "You were just giving her water."

        v "Hah, it may seem like that to you but it's more complicated than that."
        v "We don't drink water through roots like you do."
        v "I didn't even recognize the handkerchief he pulled out to clean the tea."

        show exp_v_question at right_bubble behind villainess_default
        v "Does he not carry my tokens anymore?"
        hide exp_v_question

        v "Strange..."

        $ q1 = True

        jump mpp2_interview

    label share_him:

        show exp_v_angry at right_bubble behind villainess_default
        v "Share him? Why in my right mind do that?"
        hide exp_v_angry

        show exp_p_question onlayer screens at plant_bubble zorder 1
        p "But I heard from gardeners that sharing is a good thing."
        hide exp_p_question onlayer screens

        v "That's not how this type of relationship works."
        v "Do you think you can share the same pot with other plants?"
        v "You both take nourishment from the same soil and have so much room in there to grow."
        v "Growing beside others would be harder for you."
        v "It's not like you can get up and move somewhere else, you only have one pot to grow in and it's yours."
        v "When your roots settle in, you're there for good."

        show exp_p_question onlayer screens at plant_bubble zorder 1
        p "So your relationship is like a potted plant?"
        hide exp_p_question onlayer screens

        v "That's one way of putting it."
        v "I won't be able to grow if I have someone else growing in the same pot as me, there just isn't enough room."

        p "That makes sense."
        
        $ q2 = True

        jump mpp2_interview



    #after asking both questions
    label question_finish_2:  

    v "I can't just stand by and have that girl steal him away."

    show exp_v_angry at right_bubble behind villainess_default
    v "Who does she think she is, waltzing in and ruining my reputation."
    hide exp_v_angry

    v "I have to do something before it's too late."
    v "Just a reminder of where her place is."
    v "I'll just have to find a good time to be alone with her."

    #reaction choices
    menu:
 

        "Discourage":
            jump discourage

        "Encourage":
            jump encourage


    #Option 1: Discourage (Good)
    label discourage:
        p "Will going after her when you're angry really help?"
        p "What if your fiance finds out and gets really upset again?"
        p "Then you're back to where you sprouted."
        p "Getting back at her like that won't help anybody."
        p "You should ask her and talk it out."
        p "Ask what she thinks about you and your fiance."

        v "I guess that is understandable."

        p "Speak to her alone and get her to understand what's going on."
        p "I think you'll be able to settle things."

        jump mpp2_end


    #Option 2: Encourage (Bad)
    label encourage:
        p "I think you should ask her what she thinks about your fiance."
        p "Seems to me that she's the root of your problems."
        p "You should act on it before those roots dig too deep into your pot!"

        v "You're right."

        p "You shouldn't need to share what you need to grow too."

        v "Exactly, I need to put an end to this. Now."
        
        p "I think you'll be able to settle things."

        jump mpp2_end

    label mpp2_end:
        v "I should take my leave then."
        v "Start thinking about how to get to her."

        p "Everything will work out in the end."

        v "Thank you for listening."
        v "I'll be going now."

        p "Goodbye and goodluck!"

        stop music fadeout 2.0
        jump mpp3_start 
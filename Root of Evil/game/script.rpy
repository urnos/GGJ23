# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# Introduction scene, Main plot point 1

label start:
    
    play music bg_default

    scene bg_greenhouse

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

    stop music fadeout 1.2

    play sound sfx_click

    "{i}Click.{/i}"

    play music bg_v_mad

    p "Who's that?"

    show villainess_default at right
    with dissolve

    show exp_p_question at plant_bubble zorder 1 onlayer screens
    show villainess_default

    p "Is that the Duchess?"
    hide exp_p_question onlayer screens

    p "I hear the gardeners talk about her when she's not around."

    p "Most of the time they say how cold she can be but I don't understand why?"

    p "How can someone be cold? It's so warm inside."

    show exp_p_exclaim onlayer screens at plant_bubble zorder 1
    p "Oh! She's coming."
    hide exp_p_exclaim onlayer screens

    show exp_v_angry at right_bubble behind villainess_default
    v "I can't believe him. After all the effort I put into this gown."
    hide exp_v_angry

    v "Not even a glance. A head turn would have been enough for me."

    p "Did something happen?"

    v "{i}Sigh{/i}. I don't understand why he didn't look at me today."

    show exp_v_question at right_bubble behind villainess_default
    v "Hm? is this a new plant?"
    hide exp_v_question

    v "I've never seen you before."

    v "What a small sprout."

    v "Your roots must still be growing if your that small."

    v "You need to grow big and tall if you want to survive."

    show exp_p_exclaim onlayer screens at plant_bubble zorder 1
    p "I would if I had someone to talk to!"
    hide exp_p_exclaim onlayer screens

    show exp_v_question at right_bubble behind villainess_default
    v "..."
    hide exp_v_question

    v "Who said that?"

    show exp_p_exclaim onlayer screens at plant_bubble zorder 1
    p "Did she just hear me!?"
    hide exp_p_exclaim onlayer screens
    
    show exp_v_exclaim at right_bubble behind villainess_default
    v "How is this possible? I've heard rumours of plants that can talk but I didn't believe in it!"
    hide exp_v_exclaim

    p "It's true! I've always been able to talk too!"

    show exp_v_question at right_bubble behind villainess_default
    v "You have?"
    hide exp_v_question

    p "Of course!"

    p "I won't be so lonely now that I can talk to you!"

    p "You can talk to me too. I heard you talking to yourself!"

    v "You heard that?"

    p "Yes, I did. Maybe we can talk about it!" 

    stop music fadeout 1.0 

    play sound sfx_qanda fadein 0.1

    jump mpp1_interview


   
label mpp1_interview:
    #interview segment

    #when the sfx is done then fade in bgm music 

    define qabgm_isPlaying = False
    #start the track only if the q&a bgm isn't playing
    if qabgm_isPlaying == False:
        play  music bg_mpp1_qanda fadeout 1.5 fadein 2.0 volume 0.5
        #turn q&a music toggle on 
        $ qabgm_isPlaying = True

    show exp_v_question_reversed at right_back_bubble behind villainess_default
    menu: 
        
        v "What did you want to talk about?"

        "Who's He?" if q1 == False:
            jump who_he

        "What's a gown?" if q2 == False:
            jump what_gown

    if q1 == True and q2 == True:
        jump question_finish_1


#option 1: who's he?
label who_he: 
    hide exp_v_question_reversed
    v "I was referring to my fiance."

    v "We were hosting a ball to celebrate our engagement but he didn't pay attention to me, not once today."

    show exp_p_question onlayer screens at plant_bubble zorder 1
    p "What's a fiance?"
    hide exp_p_question onlayer screens

    v "A fiance is someone you promise to be married to in the future."

    show exp_p_question onlayer screens at plant_bubble zorder 1
    p "Married?"
    hide exp_p_question onlayer screens

    v "Marriage is when two people spend the rest of their life together."

    v "They grow together and support each other."

    p "Together. For the rest of their lives..."

    p "Why not get married now?"

    show exp_v_joy at right_bubble behind villainess_default
    v "Hehe, getting married takes time, there's a lot of things to be prepared before then."
    hide exp_v_joy

    $ q1 = True

    jump mpp1_interview

#option 2: what's a gown?
label what_gown: 
    hide exp_v_question_reversed
    v "A gown is what I'm wearing right now."

    v "It's also called a dress, I was wearing it at the engagement party hoping to impress my fiance."

    show exp_p_question onlayer screens at plant_bubble zorder 1
    p "Does everyone wear a gown?"
    hide exp_p_question onlayer screens

    v "Well you don't have to wear a gown if you don't want to. Not everyone can wear one."

    show exp_p_question onlayer screens at plant_bubble zorder 1
    p "Maybe he also doesn't know what a gown is?"
    hide exp_p_question onlayer screens

    v "I would think he does. But maybe you're right. He might as well not know."

    $ q2 = True

    jump mpp1_interview

#after asking both questions
label question_finish_1:
    hide exp_v_question_reversed
    v "I just wish he paid attention to me today."
    v "He seemed so distant tonight."
    show exp_v_frustrated at right_bubble behind villainess_default
    v "I don't know..."
    hide exp_v_frustrated
    
    #reaction choices
    menu:

        "Let it go":
            jump move_on

        "Talk about it":
            jump confront

#option 1: let it go (good)
label move_on:
    p "I think you should let it go."

    p "From what I hear, some people can't see things that are right in from of them."

    p "Not sure how, but I remember someone coming in here and saying that."

    v "It's a little more complex then that."

    show exp_p_question onlayer screens at plant_bubble zorder 1
    p "Is it?"
    hide exp_p_question onlayer screens

    show exp_v_angry at right_bubble behind villainess_default
    v "It was our engagement party, how could he have not seen his soon to be wife."
    hide exp_v_angry

    v "He spent his time talking to other people."

    p "Maybe he was too busy to notice. I don't think a gown is something that would stop you from being together. You might be thinking too much."

    v "{i}Sigh{/i}. I suppose you have a point."

    show exp_p_exclaim onlayer screens at plant_bubble zorder 1
    p "Just let it go, you always have tomorrow to see him!"
    hide exp_p_exclaim onlayer screens

    v "You're right."

    $ react1_good = True

    jump mpp1_end

#option 2: talk about it (bad)
label confront:
    p "I think you should talk to him about it."

    p "Maybe he didn't realize the gown you were wearing."

    show exp_v_angry at right_bubble behind villainess_default
    v "But how could he? He's my fiance, you don't just forget about your soon wife-to-be like that."
    hide exp_v_angry

    p "Why don't you talk to him about it? It seems like you are really mad about it. "

    v "I think you have a point."

    show exp_p_exclaim onlayer screens at plant_bubble zorder 1
    p "Just talk it out, you can always talk to him tomorrow!"
    hide exp_p_exclaim onlayer screens

    v "You're right."

    $ react1_good = False

    jump mpp1_end

label mpp1_end:
    v "You know, I never would have thought talking to a plant would make me feel better."
    p "Anytime! I'm happy to help."
    v "Would you be willing to talk again?"
    p "Always!"
    v "Perhaps I will keep our conversations a secret, who knows how other people will react to find that I talk to plants when I'm alone, haha."

    stop music fadeout 1.0
    jump mpp2_start

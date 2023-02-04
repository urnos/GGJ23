# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define audio.bg_default = "sound/default_bg.mp3"
define audio.sfx_click = "sound/sfx_click.mp3"
define audio.bg_v_mad = "sound/v_mad.mp3"
define audio.sfx_qanda = "sound/sfx_qanda.wav"
define audio.bg_mpp1_qanda = "sound/mpp1_qanda.mp3"
define audio.bg_mpp2_qanda = "sound/mpp2_qanda.mp3"

define p = Character("Plant", color="#27824B")
define v = Character("Villainess", color="#B22732")

image villainess_default = "villainess.png"

image exp_v_joy = "exp_v_joy.png"
image exp_v_exclaim = "exp_v_exclaim.png"
image exp_v_angry = "exp_v_angry.png"
image exp_v_frustrated = "exp_v_frustrated.png"
image exp_v_question = "exp_v_question.png"
image exp_v_question_reversed = "exp_v_question_reverse.png"

image exp_p_joy = "exp_p_joy.png"
image exp_p_exclaim = "exp_p_exclaim.png"
image exp_p_angry = "exp_p_angry.png"
image exp_p_frustrated = "exp_p_frustrated.png"
image exp_p_question = "exp_p_question.png"

image bg_greenhouse = "TempBG_RoF.png"

define q1 = False
define q2 = False

define react1_good = False

transform right:
    xalign 0.85
    yalign 1.0

transform right_bubble:
    xalign 0.55
    yalign 0.35

transform right_back_bubble:
    xalign 0.98
    yalign 0.1

transform plant_bubble:
    xalign 0.075
    yalign 0.7
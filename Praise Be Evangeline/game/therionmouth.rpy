
init python:
    THERION_REST_TIME = 1.5
    THERION_CYCLE_TIME = 4.2

    def therion_hand_shake_jump(trans, st, at):
        t = st % THERION_CYCLE_TIME
        amp = 6.0 if t < (THERION_CYCLE_TIME - THERION_REST_TIME) else 2.0
        trans.xoffset = renpy.random.uniform(-amp, amp)
        trans.yoffset = renpy.random.uniform(-amp, amp)
        return 0.04

transform therion_tremble_jump:
    function therion_hand_shake_jump

image tm_mouth_jump:
    "BG/MOUTH THERION/MOUTHPULL1.png"
    pause 0.15
    "BG/MOUTH THERION/MOUTHPULL2.png"
    pause 0.6
    "BG/MOUTH THERION/MOUTHPULL1.png"
    pause 0.12
    "BG/MOUTH THERION/MOUTHPULL2.png"
    pause 0.6
    "BG/MOUTH THERION/MOUTHPULL1.png"
    pause 0.12
    "BG/MOUTH THERION/MOUTHPULL2.png"
    pause 0.91
    "BG/MOUTH THERION/MOUTHPULL1.png"
    pause 0.2
    "BG/MOUTH THERION/MOUTHNORMAL.png"
    pause 1.5
    repeat

image tm_hand_left_jump_frames:
    "BG/MOUTH THERION/LEFTHANDPULL.png"
    pause 2.7
    "BG/MOUTH THERION/LEFTHANDNOR.png"
    pause 1.5
    repeat

image tm_hand_right_jump_frames:
    "BG/MOUTH THERION/RIGHTHANDPULL.png"
    pause 2.7
    "BG/MOUTH THERION/RIGHTHANDNOR.png"
    pause 1.5
    repeat

image tm_eyes:
    "BG/MOUTH THERION/EYEOPEN.png"
    pause 3.0
    "BG/MOUTH THERION/EYEHALF1.png"
    pause 0.06
    "BG/MOUTH THERION/EYEHALF2.png"
    pause 0.06
    "BG/MOUTH THERION/EYECLOSED.png"
    pause 0.1
    "BG/MOUTH THERION/EYEHALF2.png"
    pause 0.06
    "BG/MOUTH THERION/EYEHALF1.png"
    pause 0.06
    repeat


image tm_mouth:
    "BG/MOUTH THERION/MOUTHNORMAL.png"
    pause 1.5
    "BG/MOUTH THERION/MOUTHPULL1.png"
    pause 0.15
    "BG/MOUTH THERION/MOUTHPULL2.png"
    pause 0.6
    "BG/MOUTH THERION/MOUTHPULL1.png"
    pause 0.12
    "BG/MOUTH THERION/MOUTHPULL2.png"
    pause 0.6
    "BG/MOUTH THERION/MOUTHPULL1.png"
    pause 0.12
    "BG/MOUTH THERION/MOUTHPULL2.png"
    pause 0.91
    "BG/MOUTH THERION/MOUTHPULL1.png"
    pause 0.2
    repeat


init python:
    def therion_hand_shake_hard(trans, st, at):
        trans.xoffset = renpy.random.uniform(-9.0, 9.0)
        trans.yoffset = renpy.random.uniform(-9.0, 9.0)
        return 0.03

transform therion_tremble_hard:
    function therion_hand_shake_hard

image therion_mouth_jump stare = Composite(
    (2500, 1406),
    (0, 0), "BG/MOUTH THERION/BASE.png",
    (0, 0), "BG/MOUTH THERION/MOUTHPULL2.png",
    (0, 0), "BG/MOUTH THERION/EYEOPEN.png",
    (0, 0), At("BG/MOUTH THERION/LEFTHANDPULL.png", therion_tremble_hard),
    (0, 0), At("BG/MOUTH THERION/RIGHTHANDPULL.png", therion_tremble_hard))

image tm_hand_left_jump = At("tm_hand_left_jump_frames", therion_tremble_jump)
image tm_hand_right_jump = At("tm_hand_right_jump_frames", therion_tremble_jump)

image therion_mouth_cg = Composite(
    (2500, 1406),
    (0, 0), "BG/MOUTH THERION/BASE.png",
    (0, 0), "tm_mouth",
    (0, 0), "tm_eyes",
    (0, 0), "tm_hand_left",
    (0, 0), "tm_hand_right")

image therion_mouth_jump = Composite(
    (2500, 1406),
    (0, 0), "BG/MOUTH THERION/BASE.png",
    (0, 0), "tm_mouth_jump",
    (0, 0), "tm_eyes",
    (0, 0), "tm_hand_left_jump",
    (0, 0), "tm_hand_right_jump")

transform therion_fit:
    xpos 960 ypos 540
    xanchor 0.5 yanchor 0.5
    xoffset 0 yoffset 0
    zoom 0.768

transform therion_slam:
    xpos 960 ypos 540
    xanchor 0.5 yanchor 0.5
    xoffset 0 yoffset 0
    zoom 0.9
    pause 0.1
    linear 0.07 zoom 1.17
    easein 0.4 zoom 0.9

transform therion_pullback:
    xpos 960 ypos 540
    xanchor 0.5 yanchor 0.5
    xoffset 0 yoffset 0
    zoom 0.9
    ease 1.0 zoom 0.768

transform jumpscare_slam:
    align (0.5, 0.5)
    zoom 1.3
    easeout 0.12 zoom 1.0

define flashred = Fade(0.03, 0.0, 0.3, color="#c00000")

define rattle = Move((12, 8), (-12, -8), .04, bounce=True, repeat=True, delay=.6)
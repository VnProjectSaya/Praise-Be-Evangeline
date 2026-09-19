###### beginning battle anim
define SHADOW_ZOOM = 0.42
define SHADOW_YPOS = 0.99
define EDGE_MARGIN = 0.18
define T_APPROACH = 1.0
define T_CLASH_TOTAL = 1.5
define T_TRAVEL = 2.0
define T_EDGE_HOLD = 0.8
define LEG_TIME = T_APPROACH + T_CLASH_TOTAL + T_TRAVEL + T_EDGE_HOLD

init python:
    def _clash_thud(trans, st, at):
        renpy.sound.play("audio/thud.mp3")
        return None

    def _clash_shake(trans, st, at):
        # visual jitter
        if st < 0.3:
            trans.xoffset = renpy.random.randint(-10, 10)
            trans.yoffset = renpy.random.randint(-10, 10)
            return 0.02
        else:
            trans.xoffset = 0
            trans.yoffset = 0
            return None

image shadow_manleft:
    "Shadow/MANLEFT1.png"
    pause 0.5
    "Shadow/MANLEFT2.png"
    pause 0.5
    "Shadow/MANLEFT3.png"
    pause 0.5
    "Shadow/MANLEFT2.png"
    pause 0.5
    repeat

image shadow_manright:
    "Shadow/MANRIGHT1.png"
    pause 0.5
    "Shadow/MANRIGHT2.png"
    pause 0.5
    "Shadow/MANRIGHT3.png"
    pause 0.5
    "Shadow/MANRIGHT2.png"
    pause 0.5
    repeat


transform manleft_fight:
    xzoom SHADOW_ZOOM  yzoom SHADOW_ZOOM
    xanchor 0.5 yanchor 1.0
    xpos EDGE_MARGIN ypos SHADOW_YPOS
    block:
        easeout T_APPROACH xpos 0.5
        pause T_CLASH_TOTAL
        easein T_TRAVEL xpos (1.0 - EDGE_MARGIN)
        pause T_EDGE_HOLD
        xzoom -SHADOW_ZOOM
        easeout T_APPROACH xpos 0.5
        pause T_CLASH_TOTAL
        easein T_TRAVEL xpos EDGE_MARGIN
        pause T_EDGE_HOLD
        xzoom SHADOW_ZOOM
        repeat

transform manright_fight:
    xzoom SHADOW_ZOOM  yzoom SHADOW_ZOOM
    xanchor 0.5 yanchor 1.0
    xpos (1.0 - EDGE_MARGIN) ypos SHADOW_YPOS
    block:
        easeout T_APPROACH xpos 0.5
        function _clash_shake
        pause (T_CLASH_TOTAL - 0.3)
        easein T_TRAVEL xpos EDGE_MARGIN
        pause T_EDGE_HOLD
        xzoom -SHADOW_ZOOM
        easeout T_APPROACH xpos 0.5
        function _clash_shake
        pause (T_CLASH_TOTAL - 0.3)
        easein T_TRAVEL xpos (1.0 - EDGE_MARGIN)
        pause T_EDGE_HOLD
        xzoom SHADOW_ZOOM
        repeat

transform manleft_final_approach:
    xzoom SHADOW_ZOOM  yzoom SHADOW_ZOOM
    xanchor 0.5 yanchor 1.0
    ypos SHADOW_YPOS
    easeout 0.6 xpos 0.47

transform manright_final_approach:
    xzoom SHADOW_ZOOM  yzoom SHADOW_ZOOM
    xanchor 0.5 yanchor 1.0
    ypos SHADOW_YPOS
    easeout 0.6 xpos 0.53

transform manleft_final_reset:
    xzoom SHADOW_ZOOM  yzoom SHADOW_ZOOM
    xanchor 0.5 yanchor 1.0
    xpos EDGE_MARGIN ypos SHADOW_YPOS

transform manright_final_reset:
    xzoom SHADOW_ZOOM  yzoom SHADOW_ZOOM
    xanchor 0.5 yanchor 1.0
    xpos (1.0 - EDGE_MARGIN) ypos SHADOW_YPOS

transform screen_shake:
    xoffset 0 yoffset 0
    linear 0.03 xoffset 16 yoffset -12
    linear 0.03 xoffset -16 yoffset 12
    linear 0.03 xoffset 12 yoffset -16
    linear 0.03 xoffset -10 yoffset 8
    linear 0.03 xoffset 6 yoffset -6
    linear 0.05 xoffset 0 yoffset 0

init python:
    def _clash_impact(trans, st, at):
        if st == 0:
            renpy.sound.play("audio/thud.mp3")
            renpy.transition(vpunch, layer='master')
        return None

transform clash_timer:
    block:
        pause T_APPROACH
        function _clash_impact
        pause (LEG_TIME - 0.3)
        function _clash_impact
        pause (LEG_TIME - T_APPROACH - 0.3)
        repeat


define SHADOW_YPOS_FALLEN = SHADOW_YPOS + 0.06

transform manright_collapse:
    xzoom -SHADOW_ZOOM  yzoom SHADOW_ZOOM
    xanchor 0.5 yanchor 1.0
    xpos 0.5 ypos SHADOW_YPOS
    parallel:
        easein 1.0 ypos SHADOW_YPOS_FALLEN
    parallel:
        easein 1.2 alpha 0.0


###### THERION BATTLE ANIM 1

image therion_bam:
    "Shadow/THERIONBAM1.png"
    anchor (0.5, 0.5)
    pos (300, 650)
    rotate 0
    zoom 0.9

    easein 0.3 pos (270, 540) rotate -10 zoom 0.95

    easeout 0.15 pos (330, 590) rotate 4 zoom 0.85

    "Shadow/THERIONBAM2.png"
    easeout 0.18 pos (880, 220) rotate -22 zoom 1.0
    easein 0.06 pos (850, 190) rotate -16 zoom 1.05

    "Shadow/THERIONBAM3.png"
    linear 0.07 pos (1400, 480) rotate 35 zoom 1.15
    pause 0.1


image man_fallback:
    "Shadow/MANFALLBACK1.png"
    anchor (0.5, 0.5)
    pos (1200, 711)
    rotate 0
    zoom 0.95

    pause 0.69

    "Shadow/MANFALLBACK2.png"
    linear 0.05 pos (1330, 719) rotate -8 zoom 0.93

    "Shadow/MANFALLBACK3.png"
    linear 0.02 pos (1500, 731) rotate -15 zoom 0.9
    pause 0.4

## therion attack2

image therion_swing:
    "Shadow/THERIONSWING1.png"
    xzoom -1.0
    anchor (0.5, 0.5)
    pos (1620, 727)
    rotate 0
    zoom 0.65

    easein 0.3 pos (1560, 719) rotate -6

    easeout 0.15 pos (1600, 730) rotate 3

    "Shadow/THERIONSWING2.png"
    easeout 0.18 pos (1050, 727) rotate -10
    easein 0.06 pos (1000, 723) rotate -6

    "Shadow/THERIONSWING3.png"
    linear 0.07 pos (520, 727) rotate 8
    pause 0.1


image man_defend:
    "Shadow/MANDEFEND1.png"
    xzoom -1.0
    anchor (0.5, 0.5)
    pos (380, 669)
    rotate 0
    zoom 0.75

    pause 0.69

    "Shadow/MANDEFEND2.png"
    linear 0.04 pos (350, 669) rotate -5

    "Shadow/MANDEFEND2.png"
    linear 0.03 pos (300, 671) rotate -18
    pause 0.4


label therion_swing_attack:

    scene bg RED

    show therion_swing
    show man_defend

    pause 0.76
    play sound "audio/bash1.mp3"
    scene black
    with hpunch

    pause 0.5

    return

image bg MM1 = "MM1.PNG"
image bg MM2 = "MM2.PNG"

image bg RED = "BG/RED.jpg"
image bg arena_day = "BG/Arena_Day.png"
image bg arena_day_lit = "BG/Arena_Day_Lit.png"
image bg arena_day_lit_crowd = "BG/Arena_Day_Lit_Crowd.png"

image bg temple_corridor_day = "BG/Temple_Corridor_Day.png"
image bg temple_corridor_night = "BG/Temple_Corridor_Night.png"

image bg temple_hall_day = "BG/Temple_Hall_Day.png"
image bg temple_hall_night_cool = "BG/Temple_Hall_Night_Cool.png"
image bg temple_hall_night_warm = "BG/Temple_Hall_Night_Warm.png"

image bg temple_night_dark = "BG/Temple_Night_Dark.png"

image bg village_night = "BG/Village_night.png"
image bg village_night_loop = "BG/Village_Night_Loop.png"

image dream_frame = "Frame/Dream Frame/dream_frame.PNG"

screen dream_frame_overlay():
    zorder 200
    if "menu" not in renpy.get_showing_tags(layer="screens"):
        add "dream_frame"

init python:
    config.overlay_screens.append("dream_frame_overlay")

# FIREFLY ANIM

transform firefly_small:

    zoom renpy.random.uniform(0.22, 0.45)
    xpos renpy.random.uniform(0.02, 0.98)
    ypos renpy.random.uniform(0.05, 0.95)
    alpha renpy.random.uniform(0.65, 1.0)

    parallel:

        ease renpy.random.uniform(2.5, 4.0) xpos renpy.random.uniform(0.00, 1.00) ypos renpy.random.uniform(0.78, 0.92)
        pause renpy.random.uniform(0.1, 0.8)

        ease renpy.random.uniform(2.5, 4.5) xpos renpy.random.uniform(0.00, 1.00) ypos renpy.random.uniform(0.58, 0.76)
        pause renpy.random.uniform(0.2, 1.0)

        ease renpy.random.uniform(2.5, 4.5) xpos renpy.random.uniform(0.00, 1.00) ypos renpy.random.uniform(0.38, 0.62)
        pause renpy.random.uniform(0.2, 1.2)

        ease renpy.random.uniform(2.5, 4.5) xpos renpy.random.uniform(0.00, 1.00) ypos renpy.random.uniform(0.20, 0.45)
        pause renpy.random.uniform(0.2, 1.0)

        ease renpy.random.uniform(2.5, 4.5) xpos renpy.random.uniform(0.00, 1.00) ypos renpy.random.uniform(-0.10, 0.25)

    parallel:

        pause renpy.random.uniform(0.5, 3.0)
        ease 1.0 alpha 0.15
        ease 1.4 alpha 1.0

        pause renpy.random.uniform(0.8, 3.5)
        ease 0.8 alpha 0.25
        ease 1.6 alpha 1.0

        pause renpy.random.uniform(0.5, 3.0)
        ease 1.0 alpha 0.1
        ease 1.5 alpha 1.0

    pause renpy.random.uniform(0.0, 3.0)

    ease renpy.random.uniform(1.0, 2.5) alpha 0.0

    # Restart from underneath the screen
    ypos 1.08
    xpos renpy.random.uniform(0.02, 0.98)
    alpha renpy.random.uniform(0.65, 1.0)

    repeat


transform firefly_medium:

    zoom renpy.random.uniform(0.40, 0.70)
    xpos renpy.random.uniform(0.02, 0.98)
    ypos renpy.random.uniform(0.05, 0.95)
    alpha renpy.random.uniform(0.70, 1.0)

    parallel:

        ease renpy.random.uniform(3.0, 5.0) xpos renpy.random.uniform(0.00, 1.00) ypos renpy.random.uniform(0.80, 0.94)
        pause renpy.random.uniform(0.2, 1.0)

        ease renpy.random.uniform(3.0, 5.0) xpos renpy.random.uniform(0.00, 1.00) ypos renpy.random.uniform(0.60, 0.78)
        pause renpy.random.uniform(0.2, 1.2)

        ease renpy.random.uniform(3.0, 5.0) xpos renpy.random.uniform(0.00, 1.00) ypos renpy.random.uniform(0.40, 0.63)
        pause renpy.random.uniform(0.2, 1.2)

        ease renpy.random.uniform(3.0, 5.0) xpos renpy.random.uniform(0.00, 1.00) ypos renpy.random.uniform(0.18, 0.43)
        pause renpy.random.uniform(0.2, 1.0)

        ease renpy.random.uniform(3.0, 5.0) xpos renpy.random.uniform(0.00, 1.00) ypos renpy.random.uniform(-0.10, 0.25)

    parallel:

        pause renpy.random.uniform(1.0, 4.0)
        ease 1.2 alpha 0.15
        ease 1.7 alpha 1.0

        pause renpy.random.uniform(1.0, 4.0)
        ease 1.0 alpha 0.20
        ease 1.8 alpha 1.0

        pause renpy.random.uniform(0.5, 3.0)
        ease 1.2 alpha 0.10
        ease 1.5 alpha 1.0

    pause renpy.random.uniform(0.0, 4.0)

    ease renpy.random.uniform(1.0, 2.5) alpha 0.0

    ypos 1.08
    xpos renpy.random.uniform(0.02, 0.98)
    alpha renpy.random.uniform(0.70, 1.0)

    repeat


transform firefly_large:

    zoom renpy.random.uniform(0.70, 1.15)
    blur 1.5
    xpos renpy.random.uniform(0.02, 0.98)
    ypos renpy.random.uniform(0.05, 0.95)
    alpha renpy.random.uniform(0.60, 0.90)

    parallel:

        ease renpy.random.uniform(3.5, 5.5) xpos renpy.random.uniform(0.00, 1.00) ypos renpy.random.uniform(0.80, 0.94)
        pause renpy.random.uniform(0.3, 1.2)

        ease renpy.random.uniform(3.5, 5.5) xpos renpy.random.uniform(0.00, 1.00) ypos renpy.random.uniform(0.60, 0.78)
        pause renpy.random.uniform(0.3, 1.4)

        ease renpy.random.uniform(3.5, 5.5) xpos renpy.random.uniform(0.00, 1.00) ypos renpy.random.uniform(0.40, 0.63)
        pause renpy.random.uniform(0.3, 1.4)

        ease renpy.random.uniform(3.5, 5.5) xpos renpy.random.uniform(0.00, 1.00) ypos renpy.random.uniform(0.18, 0.43)
        pause renpy.random.uniform(0.3, 1.2)

        ease renpy.random.uniform(3.5, 5.5) xpos renpy.random.uniform(0.00, 1.00) ypos renpy.random.uniform(-0.10, 0.25)

    parallel:

        pause renpy.random.uniform(1.5, 4.5)
        ease 1.5 alpha 0.15
        ease 2.0 alpha 0.85

        pause renpy.random.uniform(1.0, 4.0)
        ease 1.3 alpha 0.20
        ease 2.0 alpha 0.85

    pause renpy.random.uniform(0.0, 5.0)

    ease renpy.random.uniform(1.5, 3.0) alpha 0.0
    ypos 1.08
    xpos renpy.random.uniform(0.02, 0.98)
    alpha renpy.random.uniform(0.60, 0.90)

    repeat


# FIREFLY SCREEN

screen fireflies():

    # Small distant
    for i in range(30):
        add "firefly.png" at firefly_small

    # Medium fireflies
    for i in range(15):
        add "firefly.png" at firefly_medium

    # Large foreground fireflies
    for i in range(6):
        add "firefly.png" at firefly_large

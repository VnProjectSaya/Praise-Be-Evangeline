init python:
    if "bg_layer" not in config.layers:
        config.layers.insert(0, "bg_layer")

define SHADOW_ZOOM = 0.42
define SHADOW_YPOS = 0.99
define EDGE_MARGIN = 0.18
define T_APPROACH = 1.0
define T_CLASH_TOTAL = 1.5
define T_TRAVEL = 2.0
define T_EDGE_HOLD = 0.8
define LEG_TIME = T_APPROACH + T_CLASH_TOTAL + T_TRAVEL + T_EDGE_HOLD
init python:
    def stop_atl_at_current_pos(trans, st, at):
        return None
image villager1_sway:
    "Shadow/VILLAGER1FRAME1.png"
    pause 9.5
    "Shadow/VILLAGER1FRAME2.png"
    pause 0.5
    repeat

image villager2_sway:
    "Shadow/VILLAGER2FRAME1.png"
    pause 9.5
    "Shadow/VILLAGER2FRAME2.png"
    pause 0.5
    repeat

image villager3_sway:
    "Shadow/VILLAGER3FRAME1.png"
    pause 9.5
    "Shadow/VILLAGER3FRAME2.png"
    pause 0.5
    repeat

init python:
    def _clash_thud(trans, st, at):
        renpy.sound.play("audio/thud.mp3")
        return None

    def _clash_shake(trans, st, at):
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
init:

    python:

        import math

        class Shaker(object):

            anchors = {
                'top' : 0.0,
                'center' : 0.5,
                'bottom' : 1.0,
                'left' : 0.0,
                'right' : 1.0,
                }

            def __init__(self, start, child, dist):
                if start is None:
                    start = child.get_placement()
                self.start = [ self.anchors.get(i, i) for i in start ]
                self.dist = dist
                self.child = child

            def __call__(self, t, sizes):
                def fti(x, r):
                    if x is None:
                        x = 0
                    if isinstance(x, float):
                        return int(x * r)
                    else:
                        return x

                xpos, ypos, xanchor, yanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]

                xpos = xpos - xanchor
                ypos = ypos - yanchor

                nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
                ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)

                return (int(nx), int(ny), 0, 0)

        def _Shake(start, time, child=None, dist=100.0, **properties):

            move = Shaker(start, child, dist=dist)

            return renpy.display.layout.Motion(move,
                          time,
                          child,
                          add_sizes=True,
                          **properties)

        Shake = renpy.curry(_Shake)

init:
    $ sshake = Shake((0, 0, 0, 0), 1.0, dist=15)

image bg MM1 = "MM1.PNG"
image bg MM2 = "MM2.PNG"
image bg MM3 = "MM3.PNG"

image bg RED = "BG/RED.jpg"
image bg arena_day = "BG/Arena_Day.png"
image bg arena_day_lit = "BG/Arena_Day_Lit.png"
image bg arena_day_lit_crowd = "BG/Arena_Day_Lit_Crowd.png"

image bg temple_corridor_day = "BG/Temple_Corridor_Day.png"
image temple_corridor_day1 = "BG/Temple_Corridor_Day.png"
image bg temple_corridor_night = "BG/Temple_Corridor_Night.png"
image temple_corridor_night1 = "BG/Temple_Corridor_Night.png"

init python:
    red_eerie_matrix = TintMatrix("#ec4343") * BrightnessMatrix(0.1)

image bg temple_corridor_red:
    "BG/Temple_Corridor_Night.png"
    matrixcolor red_eerie_matrix

image temple_corridor_red1:
    "BG/Temple_Corridor_Night.png"
    matrixcolor red_eerie_matrix

image bloodtrail = "BG/blood.png"
image leg = "BG/leg.png"

image bg_corridor_loop_red:
    subpixel True
    contains:
        "temple_corridor_red1"
        xpos 0 ypos 0
    contains:
        "temple_corridor_red1"
        xpos -1920 ypos 0
    block:
        xpos 0
        linear 25.0 xpos 1920
        repeat

image bg_corridor_loop:
    subpixel True
    contains:
        "BG/temple_corridor_day.png"
        xpos 0 ypos 0
    contains:
        "BG/temple_corridor_day.png"
        xpos 1920 ypos 0
    block:
        xpos 0
        linear 32.0 xpos -1920
        repeat
image bg_corridor_loop_night:
    subpixel True
    contains:
        "BG/Temple_Corridor_Night.png"
        xpos 0 ypos 0
    contains:
        "BG/Temple_Corridor_Night.png"
        xpos 1920 ypos 0
    block:
        xpos 0
        linear 32.0 xpos -1920
        repeat
image bg temple_hall_day = "BG/Temple_Hall_Day.png"
image bg temple_hall_night_cool = "BG/Temple_Hall_Night_Cool.png"
image bg temple_hall_night_warm = "BG/Temple_Hall_Night_Warm.png"

image bg temple_night_dark = "BG/Temple_Night_Dark.png"

image bg village_night = "BG/Village_night.png"
image bg village_night_loop = "BG/Village_Night_Loop.png"

image bg study_night_dark = "BG/Study_Night_Dark.png"
image bg study_night_lit  = "BG/Study_Night_Lit.png"

image bg eva_bedroom_day = "BG/Eva_Bedroom_Day.png"
image bg eva_bedroom_day_flowers = "BG/Eva_Bedroom_Day_Flowers.png"
image bg eva_bedroom_night_dark = "BG/Eva_Bedroom_Night_Dark.png"
image bg eva_bedroom_night_flowers_dark = "BG/Eva_Bedroom_Night_Flowers_Dark.png"
image bg eva_bedroom_night_flowers_lit = "BG/Eva_Bedroom_Night_Flowers_Lit.png"
image bg eva_bedroom_night_lit = "BG/Eva_Bedroom_Night_Lit.png"
default no_rollback_scene = False

image red_flash = Solid("#7a0000")

transform peek_door_left_wide:
    subpixel True
    xanchor 1.0 yanchor 0.0 ypos 0.0
    xpos 0.14 xoffset 0
    easein 0.35 xpos -0.02

transform peek_door_right_wide:
    subpixel True
    xanchor 0.0 yanchor 0.0 ypos 0.0
    xpos 0.86 xoffset 0
    easein 0.35 xpos 1.02
image peek_door = Solid("#000", xysize=(config.screen_width, config.screen_height))

transform peek_door_left:
    subpixel True
    xanchor 1.0 xpos 0.5
    yanchor 0.0 ypos 0.0
    pause 0.8
    easein 0.25 xpos 0.49
    pause 0.7
    easein 0.2 xpos 0.475
    pause 0.4
    ease 2.6 xpos 0.20
    block:
        ease 3.5 xoffset 5
        ease 3.5 xoffset -5
        repeat

transform peek_door_right:
    subpixel True
    xanchor 0.0 xpos 0.5
    yanchor 0.0 ypos 0.0
    pause 0.8
    easein 0.25 xpos 0.51
    pause 0.7
    easein 0.2 xpos 0.525
    pause 0.4
    ease 2.6 xpos 0.80
    block:
        ease 3.5 xoffset 5
        ease 3.5 xoffset -5
        repeat

define push_stop = PushMove(2.0, "pushleft")
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


screen fireflies():

    for i in range(30):
        add "firefly.png" at firefly_small

    for i in range(15):
        add "firefly.png" at firefly_medium

    for i in range(6):
        add "firefly.png" at firefly_large


define DUMMY2_X = 0

transform fit_canvas_left:
    xanchor 0.0 yanchor 0.0
    xpos DUMMY2_X ypos 0
    zoom 0.876

image dummy2_idle   = "Shadow/DUMMYTWO.png"
image dummy2_cut    = "Shadow/DUMMYSPLITTWO.png"
image dummy2_top    = "Shadow/DUMMYSPLITTOPTWO.png"
image dummy2_bottom = "Shadow/DUMMYSPLITBOTTOMTWO.png"

transform therion_swing_move_flip:
    xanchor 0.0 yanchor 0.0
    ypos 0
    zoom 0.876
    xzoom -1.0
    xpos (DUMMY2_X + 220)
    blur 0.0
    linear 0.10 xpos (DUMMY2_X + 60)   blur 4.0
    linear 0.05 xpos (DUMMY2_X - 160)  blur 14.0
    linear 0.15 xpos (DUMMY2_X - 400)  blur 0.0

image slash_impact_flash_two:
    Solid("#FFFFFF")
    size (1500, 14)
    rotate -4
    xpos (DUMMY2_X + 740) ypos 797
    anchor (0.5, 0.5)
    alpha 0.0
    linear 0.03 alpha 1.0
    linear 0.12 alpha 0.0

transform dummy2_top_away:
    xanchor 0.0 yanchor 0.0
    xpos DUMMY2_X ypos 0
    zoom 0.876
    alpha 1.0
    parallel:
        easein 0.6 yoffset -220 rotate 4
    parallel:
        pause 0.1
        linear 0.5 alpha 0.0

transform dummy2_bottom_away:
    xanchor 0.0 yanchor 0.0
    xpos DUMMY2_X ypos 0
    zoom 0.876
    alpha 1.0
    parallel:
        easein 0.6 yoffset 220 rotate -4
    parallel:
        pause 0.15
        linear 0.45 alpha 0.0

transform fit_canvas:
    xanchor 0.0 yanchor 0.0
    xpos 160 ypos 0
    zoom 0.876

image dummy_idle   = "Shadow/DUMMYONE.png"
image dummy_cut    = "Shadow/DUMMYSPLIT.png"
image dummy_top    = "Shadow/DUMMYSPLITTOP.png"
image dummy_bottom = "Shadow/DUMMYSPLITBOTTOM.png"


image therion_slash_seq:
    "Shadow/THERIONSLASH1.png"
    pause 0.10
    "Shadow/THERIONSLASH2.png"
    pause 0.05
    "Shadow/THERIONSLASH3.png"
    pause 0.15

transform therion_swing_move:
    xanchor 0.0 yanchor 0.0
    ypos 0
    zoom 0.876
    xpos -60
    blur 0.0
    linear 0.10 xpos 100 blur 4.0
    linear 0.05 xpos 320 blur 14.0
    linear 0.15 xpos 560 blur 0.0

transform slash_nudge(xo=0, yo=0):
    xoffset xo
    yoffset yo

image slash_impact_flash:
    Solid("#FFFFFF")
    size (1500, 14)
    rotate 15
    xpos 960 ypos 760
    anchor (0.5, 0.5)
    alpha 0.0
    linear 0.03 alpha 1.0
    linear 0.12 alpha 0.0

transform dummy_top_away:
    xanchor 0.0 yanchor 0.0
    xpos 160 ypos 0
    zoom 0.876
    alpha 1.0
    parallel:
        easein 0.6 yoffset -220 rotate -4
    parallel:
        pause 0.1
        linear 0.5 alpha 0.0

transform dummy_bottom_away:
    xanchor 0.0 yanchor 0.0
    xpos 160 ypos 0
    zoom 0.876
    alpha 1.0
    parallel:
        easein 0.6 yoffset 220 rotate 4
    parallel:
        pause 0.15
        linear 0.45 alpha 0.0

image barrage_slash_1:
    Solid("#FFFFFF")
    rotate 45
    size (60, 2000)
    anchor (0.5, 0.5)
    xpos 960 ypos 540
    zoom 0.15
    alpha 0.85
    easeout 0.05 zoom 1.0 alpha 1.0
    pause 0.06
    linear 0.15 alpha 0.0

image barrage_slash_2:
    Solid("#FFFFFF")
    rotate -45
    size (60, 2000)
    anchor (0.5, 0.5)
    xpos 960 ypos 540
    zoom 0.15
    alpha 0.85
    easeout 0.05 zoom 1.0 alpha 1.0
    pause 0.06
    linear 0.15 alpha 0.0

image barrage_slash_3:
    Solid("#FFFFFF")
    rotate 60
    size (60, 2000)
    anchor (0.5, 0.5)
    xpos 960 ypos 540
    zoom 0.15
    alpha 0.85
    easeout 0.05 zoom 1.0 alpha 1.0
    pause 0.06
    linear 0.15 alpha 0.0

image barrage_finisher_x1:
    Solid("#FFFFFF")
    rotate 45
    size (50, 2000)
    xpos 960 ypos 540
    anchor (0.5, 0.5)
    linear 0.15 alpha 0.0

image barrage_finisher_x2:
    Solid("#FFFFFF")
    rotate -45
    size (50, 2000)
    xpos 960 ypos 540
    anchor (0.5, 0.5)
    linear 0.15 alpha 0.0

image barrage_flash:
    Solid("#FF0000")
    size (1920, 1080)
    alpha 0.0
    linear 0.04 alpha 0.55
    linear 0.18 alpha 0.0

image blood_evangeline = "Evangeline/Blood.png"
image therion_hand = "BG/therionhandwipe.png"


transform eva_face_zoom:
    zoom 1.2
    xpos -210
    ypos -131
    matrixcolor TintMatrix("#5a7099")

transform blood_zoom_still:
    zoom 1.2
    xpos -210
    ypos -131
    matrixcolor TintMatrix("#5a7099")

transform hand_wipe_rest:
    xanchor 0.16 yanchor 0.17
    zoom 1.1
    matrixcolor TintMatrix("#5a7099")
    xpos 1001 ypos 520
    ease 0.2 xpos 988  ypos 532
    ease 0.2 xpos 1012 ypos 518
    ease 0.3 xpos 1001 ypos 540

transform blood_wipe_fade:
    zoom 1.66
    xpos -660
    ypos -333
    matrixcolor TintMatrix("#5a7099")
    alpha 1.0
    pause 0.6
    linear 0.25 alpha 0.5
    linear 0.25 alpha 0.0

image villager1 = "Shadow/VILLAGER1.png"
image villager2 = "Shadow/VILLAGER2.png"
image villager3 = "Shadow/VILLAGER3.png"


transform village_bg_push:
    subpixel True
    anchor (0.5, 0.5) pos (0.5, 0.5)
    zoom 1.05
    blur 3
    pause 2.5
    linear 6.0 zoom 1.28 xoffset -40

transform therion_behind:
    subpixel True
    xanchor 0.5 yanchor 0.14
    xpos 0.64 ypos 0.30 zoom 0.3 alpha 0.0
    blur 5
    linear 1.0 alpha 1.0
    pause 2.0
    linear 6.0 zoom 0.40


transform eva_float:
    subpixel True
    xanchor 0.5 yanchor 0.14
    xpos 0.48 ypos 0.34 zoom 0.3
    pause 2.5
    linear 6.0 zoom 0.44
    parallel:
        ease 2.2 yoffset -14
        ease 2.2 yoffset 0
        repeat

transform villager1_pov:
    zoom 1.05
    pause 2
    linear 3.0 zoom 1.35 xoffset -180 alpha 0.0

transform villager2_pov:
    zoom 1.1
    xoffset -40
    pause 2
    linear 3.0 zoom 1.55 yoffset 220 alpha 0.0

transform villager3_pov:
    zoom 1.05
    xoffset -30
    pause 2
    linear 3.0 zoom 1.35 xoffset 180 alpha 0.0

transform eva_float_end:
    subpixel True
    xanchor 0.5 yanchor 0.14
    xpos 0.48 ypos 0.34 zoom 0.44
    parallel:
        ease 2.2 yoffset -14
        ease 2.2 yoffset 0
        repeat

image eva_hand = "BG/Evahand.png"
image cg_therion_mouth = "CG/therion_mouth.png"
image letterbox_bar = Solid("#000", xsize=1920, ysize=110)


transform therion_face_zoom:
    subpixel True
    xanchor 0.5 yanchor 1.0
    xpos 0.5 ypos 1.0
    zoom 1.2
    yoffset 3160
    xoffset -147

transform therion_pullout:
    subpixel True
    ease 1.2 zoom 0.58 yoffset 1000 xoffset 0

transform therion_rage:
    subpixel True
    xanchor 0.5 yanchor 1.0
    xpos 0.5 ypos 1.0
    zoom 0.58
    yoffset 1000
    block:
        linear 0.05 xoffset -6
        linear 0.05 xoffset 5
        linear 0.05 xoffset -3
        linear 0.05 xoffset 4
        repeat

transform therion_settle:
    subpixel True
    xanchor 0.5 yanchor 1.0
    xpos 0.5 ypos 1.0
    zoom 0.58
    yoffset 1000
    ease 0.4 xoffset 0

transform eva_hand_reach:
    subpixel True
    anchor (0, 0)
    zoom 0.6
    pos (-470, 706)
    ease 2.2 pos (340, 536)
    ease 0.6 pos (362, 515)
    block:
        ease 0.9 pos (356, 521)
        ease 0.9 pos (366, 509)
        repeat

transform eva_hand_flinch:
    subpixel True
    linear 0.12 pos (315, 556)
    pause 0.25
    ease 1.0 pos (-510, 756)
transform bar_top_in:
    xpos 0 ypos -110
    ease 0.8 ypos 0

transform bar_bottom_in:
    xpos 0 yanchor 1.0 ypos 1080 yoffset 110
    ease 0.8 yoffset 0

transform bar_top_out:
    ease 0.8 ypos -110

transform bar_bottom_out:
    ease 0.8 yoffset 110


transform horror_flash:
    alpha 0.0
    pause 0.05
    alpha 1.0
    pause 0.06
    alpha 0.0
    pause 0.15
    alpha 1.0
    pause 0.04
    alpha 0.0
    pause 0.35
    alpha 1.0
    block:
        pause 2.5
        alpha 0.0
        pause 0.05
        alpha 1.0
        pause 0.07
        alpha 0.0
        pause 0.04
        alpha 1.0
        repeat

image white = Solid("#ffffff")

image therion_flowers = "BG/FLOWERS/therion.png"

image eva_wings_flap:
    "BG/FLOWERS/eva1.png"
    pause 0.8
    "BG/FLOWERS/eva2.png"
    pause 0.8
    repeat

define cg_scale = 0.64


transform therion_parallax:
    subpixel True
    anchor (0.5, 0.5) pos (0.5, 0.5)
    zoom cg_scale * 1.3
    alpha 0.0
    parallel:
        easein 0.8 alpha 1.0
    parallel:
        easeout_cubic 2.8 zoom cg_scale

transform eva_parallax:
    subpixel True
    anchor (0.5, 0.5) pos (0.5, 0.5)
    yoffset 650
    zoom cg_scale * 1.2
    parallel:
        easeout_cubic 2.8 yoffset 0
    parallel:
        easeout_cubic 2.8 zoom cg_scale


transform horror_jolt:
    subpixel True
    linear 0.04 xoffset -12 yoffset 6
    linear 0.04 xoffset 10 yoffset -8
    linear 0.05 xoffset -6 yoffset 4
    ease 0.2 xoffset 0 yoffset 0

transform rage_shake:
    subpixel True
    xoffset 0 yoffset 0
    block:
        linear 0.04 xoffset -16 yoffset 8
        linear 0.04 xoffset 14 yoffset -10
        linear 0.04 xoffset -10 yoffset 6
        linear 0.04 xoffset 8 yoffset -4
        repeat 3
    block:
        linear 0.06 xoffset -3 yoffset 2
        linear 0.06 xoffset 3 yoffset -2
        repeat

transform layer_reset:
    ease 0.3 xoffset 0 yoffset 0
image therion_frames:
    "BG/therionbattle.png"
    pause 1
    "BG/therionbattle1.png"
    pause 1
    "BG/therionbattle2.png"
    pause 1
    "BG/therionbattle1.png"
    pause 1
    repeat
image therioncg reveal:
    "therion_frames"
    subpixel True
    xpos 0.5 ypos 0.5
    anchor (0.20, 0.24)
    zoom 1.0
    alpha 0.0

    linear 0.3 alpha 1.0
    pause 0.7

    ease 1.2 anchor (0.54, 0.31) zoom 1.1
    pause 0.7

    ease 1.6 anchor (0.54, 0.55) zoom 0.39

    block:
        ease 1.6 yoffset -12
        ease 1.6 yoffset 0
        repeat

image bg evahorror = "BG/EvaHorror.jpg"

image bg village_reveal:
    "bg village_night"
    subpixel True
    xpos 0.5 ypos 0.5

    anchor (0.3334, 0.3334)
    zoom 1.5
    pause 1.0

    ease 1.2 anchor (0.5, 0.3125) zoom 1.6
    pause 0.7

    ease 1.6 anchor (0.5, 0.5) zoom 1.0


image therioncg jump:
    "therion_frames"
    subpixel True
    xpos 0.5 ypos 0.5
    anchor (0.54, 0.55)
    zoom 0.39
    transform_anchor True

    ease 0.14 yoffset 45 yzoom 0.96
    ease 0.08 yoffset 30 yzoom 1.0

    parallel:
        easeout 0.4 yoffset -1300
    parallel:
        easein 0.4 xoffset 1800
    parallel:
        ease 0.4 rotate 12


image bg village_jump:
    "bg village_night"
    subpixel True
    xpos 0.5 ypos 0.5
    anchor (0.5, 0.5)
    zoom 1.0

    ease 0.14 zoom 1.03 yoffset 10
    ease 0.08 yoffset 6

    parallel:
        easeout 0.4 yoffset 18
    parallel:
        easein 0.4 xoffset -20
    parallel:
        easein 0.4 zoom 1.05

init python:

    class ScreamJitter(object):
        def __init__(self, amount, rate):
            self.amount = amount
            self.rate = rate

        def __call__(self, trans, st, at):
            trans.xoffset = renpy.random.randint(-self.amount, self.amount)
            trans.yoffset = renpy.random.randint(-self.amount, self.amount)
            return self.rate

    class ScreamShake(object):
        def __init__(self, start, duration, amount, rate=0.03):
            self.start = start
            self.duration = duration
            self.amount = amount
            self.rate = rate

        def __call__(self, trans, st, at):
            t = st - self.start
            if t >= self.duration:
                trans.xoffset = 0
                trans.yoffset = 0
                return None
            a = max(1, int(self.amount * (1.0 - t / self.duration)))
            trans.xoffset = renpy.random.randint(-a, a)
            trans.yoffset = renpy.random.randint(-a, a)
            return self.rate


image scream_bg = Transform("BG/SCREAM/BG.png", zoom=0.768)

image scream_smoke:
    "BG/SCREAM/SMOKE1.png"
    pause 0.35
    "BG/SCREAM/SMOKE2.png"
    pause 0.35
    repeat

transform scream_pupil_jitter:
    function ScreamJitter(4, 0.03)

transform scream_arm_jitter:
    function ScreamJitter(3, 0.045)

image scream_woman = Fixed(

    "BG/SCREAM/BODY.png",
    "scream_smoke",
    At("BG/SCREAM/PUPILS.png", scream_pupil_jitter),
    At("BG/SCREAM/ARMS.png", scream_arm_jitter),
    fit_first=True,
)

transform scream_jumpscare:
    subpixel True
    xpos 0.46 ypos 0.32
    xanchor 0.46 yanchor 0.32
    zoom 0.3
    linear 0.12 zoom 1.9
    easeout 0.35 zoom 0.768
    function ScreamShake(0.47, 1.0, 30)

# ══════════════════════════════════════════════
# PAST CG — BURNING VILLAGE, FIRST MEETING
# Path : BG/PAST CG/
# All PNGs are 3000x1687 canvases -> zoom 0.6402 = 1920x1080
#
# STAGING
#   Sprites are full canvases painted in place. Both pivot on the
#   fingertip point (canvas 1427, 780 -> anchor 0.4757, 0.4624),
#   parked at (960, 535), zoom 0.83. Offset 0 = fingers touching.
#   0.83 is the floor: any smaller and the canvas cuts (Eva's wing top,
#   her legs on the right, Therion's bottom) slip out from behind the frame.
#   Master layer pushes 1.0 -> 1.1 from the center, so the touch point
#   never moves while the camera does.
#   Touch point / glow: (960, 535)
# ══════════════════════════════════════════════


# ══════════════════════════════════════════════
# IMAGES
# ══════════════════════════════════════════════

image bg past_fire:
    "BG/PAST CG/BG.png"
    zoom 0.6402

# Therion: frame 1 while he slides in and trembles
image ther_past idle:
    "BG/PAST CG/therion1.png"
    zoom 0.6402

# reach plays once and holds on frame 3, no repeat
image ther_past reach:
    zoom 0.6402
    "BG/PAST CG/therion1.png"
    pause 0.5
    "BG/PAST CG/therion2.png"
    pause 0.14
    "BG/PAST CG/therion3.png"

# Eva: 2 frame flap forever + small hover bob
# bob lives inside the image so the stage transforms can move her freely
# (kept small: a bigger dip shows the cut at the top of her wing)
image eva_past fly:
    zoom 0.6402
    parallel:
        "BG/PAST CG/eva1.png"
        pause 0.09
        "BG/PAST CG/eva.png"
        pause 0.09
        repeat
    parallel:
        ease 1.3 yoffset -12
        ease 1.3 yoffset 6
        repeat


# ══════════════════════════════════════════════
# CAMERA
# ══════════════════════════════════════════════

# slow creep into the fire before anyone shows up (BG only)
transform past_bg_push:
    subpixel True
    xanchor 0.5 yanchor 0.5 xpos 0.5 ypos 0.5
    zoom 1.0
    ease 6.0 zoom 1.05

# master layer push from the center, show it AFTER scene
transform past_cam_in:
    subpixel True
    xanchor 0.5 yanchor 0.5 xpos 0.5 ypos 0.5
    zoom 1.0
    ease 2.2 zoom 1.1


# ══════════════════════════════════════════════
# THERION
# ══════════════════════════════════════════════

# "Momma!" : fades + slides up from bottom left, stops a bit off his mark
transform ther_past_in:
    subpixel True
    anchor (0.4757, 0.4624) pos (960, 535) zoom 0.83
    xoffset -520 yoffset 420 alpha 0.0
    easeout 1.4 xoffset -60 yoffset 40 alpha 1.0

# drifts onto his mark while the camera pushes = parallax against the BG
transform ther_past_settle:
    subpixel True
    anchor (0.4757, 0.4624) pos (960, 535) zoom 0.83
    xoffset -60 yoffset 40 alpha 1.0
    ease 2.2 xoffset 0 yoffset 0

# "can't breathe" : knees going, small trembles with a little sag between
transform ther_past_shake:
    subpixel True
    anchor (0.4757, 0.4624) pos (960, 535) zoom 0.83
    xoffset 0 yoffset 0
    block:
        linear 0.05 xoffset -5 yoffset 2
        linear 0.05 xoffset 4 yoffset 4
        linear 0.05 xoffset -4 yoffset 3
        linear 0.05 xoffset 3 yoffset 5
        linear 0.06 xoffset 0 yoffset 4
        ease 0.5 yoffset 0
        pause 0.4
        repeat

# still, on his mark, for the reach
transform ther_past_hold:
    subpixel True
    anchor (0.4757, 0.4624) pos (960, 535) zoom 0.83
    xoffset 0 yoffset 0


# ══════════════════════════════════════════════
# EVA
# ══════════════════════════════════════════════

# from up right, stops close and hovers
transform eva_past_in:
    subpixel True
    anchor (0.4757, 0.4624) pos (960, 535) zoom 0.83
    xoffset 760 yoffset -600
    easeout 2.2 xoffset 150 yoffset -40

# glides the last stretch until their fingers meet
transform eva_past_touch:
    subpixel True
    anchor (0.4757, 0.4624) pos (960, 535) zoom 0.83
    xoffset 150 yoffset -40
    ease 1.1 xoffset 0 yoffset 0


# ══════════════════════════════════════════════
# TOUCH GLOW (reuses the holy_* helpers from birb.rpy)
# fires the moment it's shown, then a white bloom swells out of the
# fingertips and swallows the screen
# ══════════════════════════════════════════════

transform past_touch_point:
    anchor (0.5, 0.5)
    pos (960, 535)

transform touch_bloom_in:
    blend "add"
    alpha 0.0 zoom 0.1
    pause 0.3
    ease 0.3 alpha 1.0
    easein 2.6 zoom 3.4

transform touch_core_in:
    blend "add"
    alpha 0.0 zoom 0.3
    easein 0.4 alpha 1.0 zoom 1.1
    ease 0.6 zoom 1.0
    block:
        ease 1.6 zoom 1.06 alpha 0.85
        ease 1.6 zoom 1.0 alpha 1.0
        repeat

transform touch_rays_in:
    blend "add"
    alpha 0.0 zoom 0.6
    parallel:
        ease 0.6 alpha 1.0 zoom 1.0
        block:
            ease 2.0 alpha 0.7
            ease 2.0 alpha 1.0
            repeat
    parallel:
        linear 40.0 rotate 360
        repeat

transform touch_thin_in:
    blend "add"
    alpha 0.0
    pause 0.2
    ease 0.5 alpha 1.0
    block:
        ease 1.3 alpha 0.6
        ease 1.3 alpha 1.0
        repeat

transform touch_motes_in:
    blend "add"
    alpha 0.0
    pause 0.4
    ease 0.8 alpha 1.0

image touch_glow = Fixed(
    holy_mid(At(holy_orb(1200, HOLY_WHITE, 0.14, 8), touch_bloom_in)),
    holy_mid(At(holy_burst(8, 2000, 130, HOLY_GOLD, 0.10), touch_rays_in)),
    holy_mid(At(holy_burst(12, 1400, 30, HOLY_WHITE, 0.20), touch_thin_in)),
    holy_mid(At(holy_orb_stack(), touch_core_in)),
    holy_mid(At("holy_motes_raw", touch_motes_in)),
    xysize=(2000, 2000))

# finishes the envelope, stays a little see-through so the pose ghosts behind it
image touch_flash:
    Solid("#fff6e0")
    alpha 0.0
    pause 1.2
    ease 1.6 alpha 0.82
    block:
        ease 2.0 alpha 0.74
        ease 2.0 alpha 0.82
        repeat
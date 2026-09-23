###### beginning battle anim
define SHADOW_ZOOM = 0.42
define SHADOW_YPOS = 0.99
define EDGE_MARGIN = 0.18
define T_APPROACH = 1.0
define T_CLASH_TOTAL = 1.5
define T_TRAVEL = 2.0
define T_EDGE_HOLD = 0.8
define LEG_TIME = T_APPROACH + T_CLASH_TOTAL + T_TRAVEL + T_EDGE_HOLD

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
                #
                self.start = [ self.anchors.get(i, i) for i in start ]  # central position
                self.dist = dist    # maximum distance, in pixels, from the starting point
                self.child = child
                
            def __call__(self, t, sizes):
                # Float to integer... turns floating point numbers to
                # integers.                
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
    #

init:
    $ sshake = Shake((0, 0, 0, 0), 1.0, dist=15)
    
image bg MM1 = "MM1.PNG"
image bg MM2 = "MM2.PNG"

image bg RED = "BG/RED.jpg"
image bg arena_day = "BG/Arena_Day.png"
image bg arena_day_lit = "BG/Arena_Day_Lit.png"
image bg arena_day_lit_crowd = "BG/Arena_Day_Lit_Crowd.png"

image bg temple_corridor_day = "BG/Temple_Corridor_Day.png"
image temple_corridor_day1 = "BG/Temple_Corridor_Day.png"
image bg temple_corridor_night = "BG/Temple_Corridor_Night.png"
image temple_corridor_night1 = "BG/Temple_Corridor_Night.png"


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

image bg eva_bedroom_day = "BG/Eva_Bedroom_Day.png"
image bg eva_bedroom_day_flowers = "BG/Eva_Bedroom_Day_Flowers.png"
image bg eva_bedroom_night_dark = "BG/Eva_Bedroom_Night_Dark.png"
image bg eva_bedroom_night_flowers_dark = "BG/Eva_Bedroom_Night_Flowers_Dark.png"
image bg eva_bedroom_night_flowers_lit = "BG/Eva_Bedroom_Night_Flowers_Lit.png"
image bg eva_bedroom_night_lit = "BG/Eva_Bedroom_Night_Lit.png"

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


# THERION DECAPIATEEEE

transform fit_canvas:
    xanchor 0.0 yanchor 0.0
    xpos 160 ypos 0
    zoom 0.876

image dummy_idle   = "Shadow/DUMMYONE.png"
image dummy_cut    = "Shadow/DUMMYSPLIT.png"
image dummy_top    = "Shadow/DUMMYSPLITTOP.png"     # severed top half
image dummy_bottom = "Shadow/DUMMYSPLITBOTTOM.png"  # basee


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
    linear 0.10 xpos 100 blur 4.0     # windup
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

###blood wipe scene

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
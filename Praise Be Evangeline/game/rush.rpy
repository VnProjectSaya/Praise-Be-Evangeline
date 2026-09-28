
define SPIN_PIVOT = (720, 430)

transform arena_world_spin:
    subpixel True
    transform_anchor True
    anchor (720 / 1920.0, 430 / 1080.0) pos SPIN_PIVOT
    zoom 1.5 rotate 0 blur 8
    parallel:
        ease 3.0 rotate 6
        ease 3.0 rotate -6
        repeat
    parallel:
        ease 1.5 zoom 1.58
        ease 1.5 zoom 1.5
        repeat

transform arena_world_settle:
    subpixel True
    transform_anchor True
    anchor (720 / 1920.0, 430 / 1080.0) pos SPIN_PIVOT
    ease 0.8 rotate 0 zoom 1.3 blur 3

transform arena_world_still:
    subpixel True
    transform_anchor True
    anchor (720 / 1920.0, 430 / 1080.0) pos SPIN_PIVOT
    rotate 0 zoom 1.3 blur 0

transform eva_spin_focus:
    subpixel True
    xzoom 1.0 blur 0
    anchor (0.484, 0.177) pos SPIN_PIVOT
    zoom 0.53 xoffset 0 yoffset 0
    block:
        ease 2.0 yoffset -6
        ease 2.0 yoffset 0
        repeat

init python:
    def eva_tremble_fn(trans, st, at):
        trans.xoffset = renpy.random.uniform(-3.0, 3.0)
        trans.yoffset = renpy.random.uniform(-2.0, 2.0)
        return 0.04

transform eva_spin_shake:
    subpixel True
    xzoom 1.0 blur 0
    anchor (0.484, 0.177) pos SPIN_PIVOT zoom 0.53
    function eva_tremble_fn

transform eva_pulled_back:
    subpixel True
    ease 0.8 pos (800, 470) zoom 0.40 xoffset 0 yoffset 0

transform eva_dragged:
    subpixel True
    ease 0.5 pos (820, 500) zoom 0.35

transform eva_turned:
    subpixel True
    xzoom -1.0 blur 0
    xanchor 0.5 yanchor 1.0 xpos 1020 ypos 1.0
    zoom 0.36 yoffset 350
    block:
        ease 1.8 yoffset 335
        ease 1.8 yoffset 350
        repeat

transform therion_guard_front:
    subpixel True
    anchor (0.530, 0.151) pos (1180, 420)
    zoom 0.75 blur 6
    block:
        ease 2.5 yoffset 8
        ease 2.5 yoffset 0
        repeat

transform therion_pulled_back:
    subpixel True
    ease 0.8 pos (1140, 440) zoom 0.54 blur 2 yoffset 0

transform therion_dragged:
    subpixel True
    ease 0.5 pos (1130, 470) zoom 0.47

transform therion_shove:
    subpixel True
    xanchor 0.5 yanchor 1.0 xpos 760 ypos 1.0
    zoom 0.37 yoffset 400 blur 0

transform knight_rush_l:
    subpixel True
    xzoom -1.0
    anchor (0.607, 0.026) ypos 150
    zoom 0.66 blur 6 xpos -600
    ease 0.45 xpos 500
    block:
        ease 1.6 yoffset -10
        ease 1.6 yoffset 0
        repeat

transform knight_rush_r:
    subpixel True
    xzoom 1.0
    anchor (0.393, 0.026) ypos 150
    zoom 0.66 blur 6 xpos 2500
    ease 0.45 xpos 1420
    block:
        ease 1.6 yoffset -10
        ease 1.6 yoffset 0
        repeat

transform knight_press_l:
    subpixel True
    ease 0.5 xpos 560
    block:
        ease 1.6 yoffset -10
        ease 1.6 yoffset 0
        repeat

transform knight_press_r:
    subpixel True
    ease 0.5 xpos 1360
    block:
        ease 1.6 yoffset -10
        ease 1.6 yoffset 0
        repeat
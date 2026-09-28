
transform panel_left_in:
    crop (480, 0, 960, 1080)
    xpos -960 ypos 0
    easein 1.0 xpos 0

transform panel_right_in:
    crop (480, 0, 960, 1080)
    xpos 1920 ypos 0
    easein 1.0 xpos 960

transform panel_left:
    crop (480, 0, 960, 1080)
    xpos 0 ypos 0

transform panel_right:
    crop (480, 0, 960, 1080)
    xpos 960 ypos 0

transform split_divider:
    xanchor 0.5 xpos 960 ypos 0
    alpha 0.0
    pause 0.8
    linear 0.4 alpha 1.0

transform eva_face:
    zoom 0.7
    xanchor 465 yanchor 910
    xpos 480 ypos 130
    block:
        ease 2.0 yoffset -12
        ease 2.0 yoffset 0
        repeat

transform therion_face:
    zoom 0.7
    xanchor 802 yanchor 851
    xpos 1440 ypos 130

transform eva_stage1:
    matrixcolor SaturationMatrix(0.1) * TintMatrix("#3a3f4a") * BrightnessMatrix(-0.2)
transform eva_stage2:
    matrixcolor SaturationMatrix(0.35) * TintMatrix("#565a63") * BrightnessMatrix(-0.1)
transform eva_stage3:
    matrixcolor SaturationMatrix(0.65) * TintMatrix("#8a8578")
transform eva_stage4:
    matrixcolor TintMatrix("#fff0d6")

transform therion_stage1:
    matrixcolor TintMatrix("#fff2d9")
transform therion_stage2:
    matrixcolor SaturationMatrix(0.75) * TintMatrix("#f2ead6")
transform therion_stage3:
    matrixcolor SaturationMatrix(0.45) * TintMatrix("#d9d2c9") * BrightnessMatrix(-0.05)
transform therion_stage4:
    matrixcolor SaturationMatrix(0.15) * TintMatrix("#9aa0a3") * BrightnessMatrix(-0.15)

image split_line = Solid("#000000", xsize=4, ysize=1080)


image bg past_fire:
    "BG/PAST CG/BG.png"
    zoom 0.6402

image ther_past idle:
    "BG/PAST CG/therion1.png"
    zoom 0.6402

image ther_past reach:
    zoom 0.6402
    "BG/PAST CG/therion1.png"
    pause 0.5
    "BG/PAST CG/therion2.png"
    pause 0.14
    "BG/PAST CG/therion3.png"

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


transform past_bg_push:
    subpixel True
    xanchor 0.5 yanchor 0.5 xpos 0.5 ypos 0.5
    zoom 1.0
    ease 6.0 zoom 1.05

transform past_cam_in:
    subpixel True
    xanchor 0.5 yanchor 0.5 xpos 0.5 ypos 0.5
    zoom 1.0
    ease 2.2 zoom 1.1


transform ther_past_in:
    subpixel True
    anchor (0.4757, 0.4624) pos (960, 535) zoom 0.83
    xoffset -520 yoffset 420 alpha 0.0
    easeout 1.4 xoffset -60 yoffset 40 alpha 1.0

transform ther_past_settle:
    subpixel True
    anchor (0.4757, 0.4624) pos (960, 535) zoom 0.83
    xoffset -60 yoffset 40 alpha 1.0
    ease 2.2 xoffset 0 yoffset 0

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

transform ther_past_hold:
    subpixel True
    anchor (0.4757, 0.4624) pos (960, 535) zoom 0.83
    xoffset 0 yoffset 0


transform eva_past_in:
    subpixel True
    anchor (0.4757, 0.4624) pos (960, 535) zoom 0.83
    xoffset 760 yoffset -600
    easeout 2.2 xoffset 150 yoffset -40

transform eva_past_touch:
    subpixel True
    anchor (0.4757, 0.4624) pos (960, 535) zoom 0.83
    xoffset 150 yoffset -40
    ease 1.1 xoffset 0 yoffset 0


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

image touch_flash:
    Solid("#fff6e0")
    alpha 0.0
    pause 1.2
    ease 1.6 alpha 0.82
    block:
        ease 2.0 alpha 0.74
        ease 2.0 alpha 0.82
        repeat

image bg cellar = "BG/cellar.png"


define grade_day0   = TintMatrix("#ffffff") * SaturationMatrix(0.45) * ContrastMatrix(0.95) * BrightnessMatrix(-0.03)
define grade_day1   = TintMatrix("#ffffff") * SaturationMatrix(0.60) * ContrastMatrix(0.97) * BrightnessMatrix(-0.02)
define grade_day2   = TintMatrix("#ffffff") * SaturationMatrix(0.75) * ContrastMatrix(1.00) * BrightnessMatrix(-0.01)
define grade_dusk   = TintMatrix("#7084c8") * SaturationMatrix(0.75) * ContrastMatrix(1.00) * BrightnessMatrix(-0.04)
define grade_bright = TintMatrix("#ffffff") * SaturationMatrix(1.15) * ContrastMatrix(1.05) * BrightnessMatrix(0.02)
define grade_soft   = TintMatrix("#fff1ee") * SaturationMatrix(1.00) * ContrastMatrix(0.90) * BrightnessMatrix(0.05)

transform grade_set(m):
    matrixcolor m

transform grade_shift(old, new, t=2.0):
    matrixcolor old
    ease t matrixcolor new


transform fire_glow:
    matrixcolor TintMatrix("#ffb48a") * BrightnessMatrix(0.0)
    block:
        ease 0.18 matrixcolor TintMatrix("#ffc79a") * BrightnessMatrix(0.07)
        ease 0.22 matrixcolor TintMatrix("#ff9a78") * BrightnessMatrix(-0.02)
        ease 0.14 matrixcolor TintMatrix("#ffd0a0") * BrightnessMatrix(0.09)
        ease 0.30 matrixcolor TintMatrix("#ffa884") * BrightnessMatrix(0.01)
        repeat

transform fire_bg_flicker:
    matrixcolor BrightnessMatrix(0.0)
    block:
        ease 0.25 matrixcolor BrightnessMatrix(0.04)
        ease 0.30 matrixcolor BrightnessMatrix(-0.03)
        ease 0.20 matrixcolor BrightnessMatrix(0.05)
        ease 0.35 matrixcolor BrightnessMatrix(0.0)
        repeat


transform therion_face_l:
    zoom 0.7
    xanchor 784 yanchor 861
    xpos 480 ypos 130

transform eva_face_r:
    zoom 0.7
    xanchor 543 yanchor 924
    xpos 1440 ypos 130
    block:
        ease 2.0 yoffset -12
        ease 2.0 yoffset 0
        repeat

define ADULT_HEAD_Y = 280

transform therion_kid_morph_out:
    xanchor 0.616 yanchor 0.351
    xpos 480 ypos 130
    zoom 0.7 alpha 1.0 blur 0
    parallel:
        ease 1.5 zoom 0.6
    parallel:
        ease 1.5 ypos ADULT_HEAD_Y
    parallel:
        ease 1.5 blur 10
    parallel:
        linear 1.5 alpha 0.0

transform eva_kid_morph_out:
    xanchor 0.426 yanchor 0.377
    xpos 1440 ypos 130
    zoom 0.7 alpha 1.0 blur 0
    parallel:
        ease 1.5 zoom 0.6
    parallel:
        ease 1.5 ypos ADULT_HEAD_Y
    parallel:
        ease 1.5 blur 10
    parallel:
        linear 1.5 alpha 0.0

transform therion_adult_l:
    crop (709, 0, 1280, 1800)
    xanchor 0.5 xpos 480
    zoom 0.75
    ypos (130 - 272)
    alpha 0.0 blur 10
    parallel:
        ease 1.5 ypos (ADULT_HEAD_Y - 272)
    parallel:
        ease 1.5 alpha 1.0
    parallel:
        ease 1.5 blur 0

transform eva_adult_r:
    crop (320, 0, 1280, 1800)
    xzoom -1.0
    xanchor 0.5 xpos 1440
    zoom 0.75
    ypos (130 - 259)
    alpha 0.0 blur 10
    parallel:
        ease 1.5 ypos (ADULT_HEAD_Y - 259)
    parallel:
        ease 1.5 alpha 1.0
    parallel:
        ease 1.5 blur 0
    parallel:
        block:
            ease 2.0 yoffset -14
            ease 2.0 yoffset 0
            repeat

transform layer_grade(s, b):
    matrixcolor SaturationMatrix(s) * BrightnessMatrix(b)

transform layer_grade_shift(s1, b1, s2, b2, t=1.0):
    matrixcolor SaturationMatrix(s1) * BrightnessMatrix(b1)
    ease t matrixcolor SaturationMatrix(s2) * BrightnessMatrix(b2)

transform panel_left_out:
    crop (480, 0, 960, 1080)
    xpos 0 ypos 0
    easeout 1.0 xpos -960

transform panel_right_out:
    crop (480, 0, 960, 1080)
    xpos 960 ypos 0
    easeout 1.0 xpos 1920

transform split_divider_out:
    xanchor 0.5 xpos 960 ypos 0
    alpha 1.0
    linear 0.4 alpha 0.0


transform arena_takeover:
    crop (480, 0, 960, 1080)
    anchor (0.5, 0.5) pos (480, 540) zoom 1.0
    ease 2.0 crop (0, 0, 1920, 1080) pos (960, 680) zoom 2.2

transform arena_final:
    anchor (0.5, 0.5) pos (960, 680) zoom 2.2

transform corridor_under:
    crop (480, 0, 960, 1080)
    xpos 960 ypos 0
    linear 2.0 alpha 0.0


transform therion_to_kneel:
    crop None
    xanchor 0.5396 yanchor 0.0
    xpos 480 ypos (ADULT_HEAD_Y - 272)
    zoom 0.75
    ease 2.0 xpos 1098 ypos 317 zoom 0.506

transform eva_to_box:
    crop None
    xzoom -1.0
    xanchor 0.5 yanchor 0.0
    xpos 1440 ypos (ADULT_HEAD_Y - 259)
    zoom 0.75
    ease 2.0 xpos 806 ypos 220 zoom 0.1496 yoffset 0

transform eva_in_box:
    xzoom -1.0
    xanchor 0.5 yanchor 0.0
    xpos 806 ypos 220
    zoom 0.1496
    crop (0, 0, 1920, 1710)
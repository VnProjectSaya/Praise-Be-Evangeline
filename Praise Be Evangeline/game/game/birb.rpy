# ══════════════════════════════════════════════
# BIRB — bird, camera parallax, POV hands, holy glow
# Paths: BG/bird.png, BG/bird2.png, BG/hand.png
#
# SIZING (BG native 1920x1080, bird PNG 992x1216, visible bird ~855x1134)
#   Wide shot : bird at (1551, 231), zoom 0.10 -> ~86x113 px, behind Therion's head
#   Close-up  : BG x2.6 anchored top-right (never shows a black edge)
#               bird at (960, 600), zoom 0.26 -> ~222x295 px
#               Bird pos/zoom are linear in BG zoom, so the same ease +
#               duration keeps it glued to the glass during the push.
#   POV       : BG x3.2 + blur, bird leaves the glass onto the hands
#               bird at (960, 680), zoom 0.34 -> ~290x385 px
#               hand.png (1920x1080, palm cup at 912,620) at (960, 740), zoom 1.15
#
# CHARACTER MARKS (start and end of scene)
#   Eva 0.30 / zoom 0.285,  Therion 0.70 / zoom 0.27
# ══════════════════════════════════════════════

init -1 python:
    HOLY_GOLD  = "#ffe9a8"
    HOLY_WHITE = "#fffaf0"

    def holy_mid(d):
        return Transform(d, anchor=(0.5, 0.5), pos=(0.5, 0.5))

    def holy_diamond(color, w, h, alpha=1.0):
        # square turned 45° = diamond, stretch it = tapered ray
        d = Transform(Solid(color), xysize=(100, 100), rotate=45)
        return Transform(d, xzoom=w / 141.4, yzoom=h / 141.4, alpha=alpha)

    def holy_orb(size, color, alpha, pieces=6):
        # squares rotated 15° apart overlap into a soft disc:
        # the middle stacks every layer, the rim only one
        s = int(size * 0.72)
        kids = [Transform(Solid(color), xysize=(s, s), rotate=i * 90.0 / pieces,
                          alpha=alpha, anchor=(0.5, 0.5), pos=(0.5, 0.5))
                for i in range(pieces)]
        return Fixed(*kids, xysize=(size, size))

    def holy_orb_stack():
        return Fixed(
            holy_mid(holy_orb(1100, HOLY_GOLD, 0.05)),
            holy_mid(holy_orb(520, HOLY_GOLD, 0.10)),
            holy_mid(holy_orb(200, HOLY_WHITE, 0.30)),
            xysize=(1100, 1100))

    def holy_burst(count, length, width, color, alpha):
        # spokes through the centre, each one a tapered diamond
        kids = [Transform(holy_diamond(color, width, length, alpha),
                          rotate=i * 180.0 / count, anchor=(0.5, 0.5), pos=(0.5, 0.5))
                for i in range(count)]
        return Fixed(*kids, xysize=(length, length))


# ══════════════════════════════════════════════
# CAMERA — BACKGROUND
# ══════════════════════════════════════════════

transform cam_push_window:
    subpixel True
    xanchor 1.0 yanchor 0.0 xpos 1.0 ypos 0.0
    zoom 1.0 blur 0.0
    ease 1.8 zoom 2.6

# POV: push past the window, glass goes soft behind the hands
transform cam_pov:
    subpixel True
    xanchor 1.0 yanchor 0.0 xpos 1.0 ypos 0.0
    ease 1.4 zoom 3.2 blur 14.0

transform cam_pull_back:
    subpixel True
    xanchor 1.0 yanchor 0.0 xpos 1.0 ypos 0.0
    ease 1.8 zoom 1.0 blur 0.0


# ══════════════════════════════════════════════
# CAMERA — CHARACTERS (parallax: they travel much farther than the BG)
# ══════════════════════════════════════════════

transform eva_parallax_out:
    subpixel True
    xzoom -1 xanchor 0.5 yanchor 1.0 ypos 1.0
    ease 1.8 xpos -0.45 zoom 0.55 yoffset 650

transform therion_parallax_out:
    subpixel True
    xzoom 1 xanchor 0.5 yanchor 1.0 ypos 1.0
    ease 1.8 xpos 1.60 zoom 0.55 yoffset 650

transform eva_parallax_back:
    subpixel True
    xzoom -1 xanchor 0.5 yanchor 1.0 ypos 1.0
    ease 1.8 xpos 0.30 zoom 0.285 yoffset 48
    block:
        ease 1.8 yoffset 28
        ease 1.8 yoffset 48
        repeat

transform therion_parallax_back:
    subpixel True
    xzoom 1 xanchor 0.5 yanchor 1.0 ypos 1.0
    ease 1.8 xpos 0.70 zoom 0.27 yoffset 90


# ══════════════════════════════════════════════
# CAMERA — BIRD, HANDS, GLOW
# ══════════════════════════════════════════════

transform bird_glass_wide:
    subpixel True
    anchor (0.5, 0.5)
    pos (1551, 231)
    zoom 0.10

transform bird_glass_push:
    subpixel True
    anchor (0.5, 0.5)
    ease 1.8 pos (960, 600) zoom 0.26

# bird leaves the glass and drops onto the palms, closer = bigger
transform bird_to_hands:
    subpixel True
    anchor (0.5, 0.5)
    pause 0.3
    ease 1.1 pos (960, 680) zoom 0.34

# hands come up from under the frame, then breathe a little
transform hands_rise:
    subpixel True
    anchor (0.475, 0.574) pos (960, 740) zoom 1.15
    yoffset 900
    easeout 1.0 yoffset 0
    block:
        ease 2.2 yoffset 8
        ease 2.2 yoffset 0
        repeat

transform hands_lower:
    subpixel True
    anchor (0.475, 0.574) pos (960, 740) zoom 1.15
    easein 1.0 yoffset 900

transform glow_pov:
    anchor (0.5, 0.5)
    pos (960, 680)


# ══════════════════════════════════════════════
# HANDS
# ══════════════════════════════════════════════

image hand = "BG/hand.png"


# ══════════════════════════════════════════════
# BIRD ANIMATIONS
# offsets are in bird-image pixels; the camera zoom shrinks them on screen
# ══════════════════════════════════════════════

image bird_flap:
    "BG/bird.png"
    pause 0.07
    "BG/bird2.png"
    pause 0.07
    repeat

image bird_flap_panic:
    "BG/bird.png"
    pause 0.045
    "BG/bird2.png"
    pause 0.045
    repeat

image bird_flap_slow:
    "BG/bird.png"
    pause 0.12
    "BG/bird2.png"
    pause 0.12
    repeat

image bird_flap_stiff:
    # metronome flapping, dead even = wrong
    "BG/bird.png"
    pause 0.15
    "BG/bird2.png"
    pause 0.15
    repeat

image bird knock:
    subpixel True
    "bird_flap"
    rotate 0 xoffset 0 yoffset 0 xzoom 1.0 yzoom 1.0
    block:
        choice 2:
            # one hard slam
            ease 0.45 xoffset -200 yoffset 60 rotate -6
            linear 0.06 xoffset 70 yoffset -10 rotate 10
            "BG/bird2.png"
            linear 0.04 xzoom 0.9 yzoom 1.05
            pause 0.12
            "bird_flap"
            easeout 0.35 xoffset -160 yoffset 110 rotate -3 xzoom 1.0 yzoom 1.0
            ease 0.4 xoffset -40 yoffset 20 rotate 0
        choice 1:
            # frantic double tap
            ease 0.25 xoffset -120 yoffset 30 rotate -4
            linear 0.05 xoffset 60 rotate 8
            linear 0.08 xoffset -60 rotate 0
            linear 0.05 xoffset 70 rotate 11
            "BG/bird2.png"
            pause 0.1
            "bird_flap"
            easeout 0.4 xoffset -180 yoffset 90 rotate -5
            ease 0.3 xoffset -40 yoffset 20 rotate 0
        repeat

# caught: thrashing on her palms, small random jolts, no travel
image bird struggle:
    subpixel True
    "bird_flap_panic"
    rotate 0 xoffset 0 yoffset 0
    block:
        choice:
            linear 0.08 xoffset -40 yoffset 20 rotate -5
        choice:
            linear 0.08 xoffset 35 yoffset -15 rotate 6
        choice:
            linear 0.06 xoffset 10 yoffset 30 rotate -2
        choice:
            linear 0.1 xoffset -20 yoffset -25 rotate 4
        repeat

# heart slows, panic winds down, light hits at 1.9s -> metronome
image bird blessed:
    subpixel True
    rotate 0 xoffset 0 yoffset 0
    "bird_flap_panic"
    linear 0.1 xoffset -40 yoffset 20 rotate -5
    linear 0.1 xoffset 35 yoffset -15 rotate 6
    linear 0.1 xoffset -30 yoffset 25 rotate -4
    linear 0.1 xoffset 30 yoffset -10 rotate 5
    linear 0.1 xoffset -20 yoffset 15 rotate -3
    linear 0.1 xoffset 20 yoffset -10 rotate 3
    "bird_flap"
    ease 0.3 xoffset -10 yoffset 8 rotate -2
    ease 0.3 xoffset 8 yoffset -4 rotate 1
    "bird_flap_slow"
    ease 0.7 xoffset 0 yoffset 0 rotate 0
    "bird_flap_stiff"

image bird glassy:
    subpixel True
    "bird_flap_stiff"
    matrixcolor SaturationMatrix(1.0) * BrightnessMatrix(0.0)
    pause 0.5
    ease 0.6 matrixcolor SaturationMatrix(0.0) * BrightnessMatrix(0.18)
    pause 1.4
    # snaps clear, no fade, tiny jolt
    matrixcolor SaturationMatrix(1.0) * BrightnessMatrix(0.0)
    xoffset 25
    pause 0.05
    xoffset 0

image bird robot:
    subpixel True
    rotate 0 xoffset 0 yoffset 0
    block:
        "bird_flap_stiff"
        pause 1.2
        # head snaps, wings keep ticking
        rotate 14
        pause 0.4
        rotate -9
        pause 0.3
        rotate 0
        pause 0.6
        # glitch: stalls mid-flap, then servo buzz
        "BG/bird.png"
        pause 0.5
        xoffset 12
        pause 0.03
        xoffset -12
        pause 0.03
        xoffset 12
        pause 0.03
        xoffset 0
        repeat

image bird leave:
    subpixel True
    "bird_flap_stiff"
    rotate 0 xoffset 0 yoffset 0 alpha 1.0
    pause 0.3
    # rises off the palms in stairs
    yoffset -90
    pause 0.25
    yoffset -180
    pause 0.25
    yoffset -270
    pause 0.35
    # snaps to its heading, flies off in a straight line and fades out
    rotate -35
    pause 0.3
    linear 1.4 xoffset 1600 yoffset -1400 alpha 0.0


# ══════════════════════════════════════════════
# HOLY GLOW (all Solid() shapes, additive)
# waits ~1.6s for the heartbeat to slow, then blooms out of the palms
# ══════════════════════════════════════════════

transform mote_rise(x, y, delay):
    anchor (0.5, 0.5) xpos x ypos y alpha 0.0 zoom 0.6
    pause delay
    block:
        ypos y alpha 0.0 zoom 0.6 rotate 0
        ease 0.4 alpha 1.0 zoom 1.0
        linear 2.2 ypos (y - 260) alpha 0.0 rotate 90
        pause 0.3
        repeat

transform holy_core_in:
    blend "add"
    alpha 0.0 zoom 0.4
    pause 1.6
    easein 0.5 alpha 1.0 zoom 1.15
    ease 0.8 zoom 1.0
    block:
        ease 1.6 zoom 1.06 alpha 0.85
        ease 1.6 zoom 1.0 alpha 1.0
        repeat

transform holy_rays_in:
    blend "add"
    alpha 0.0
    pause 1.8
    ease 0.6 alpha 1.0
    block:
        ease 2.0 alpha 0.7
        ease 2.0 alpha 1.0
        repeat

transform holy_thin_in:
    blend "add"
    alpha 0.0
    pause 1.9
    ease 0.5 alpha 1.0
    block:
        ease 1.3 alpha 0.6
        ease 1.3 alpha 1.0
        repeat

transform holy_motes_in:
    blend "add"
    alpha 0.0
    pause 1.9
    ease 0.8 alpha 1.0

image holy_sparkle = Fixed(
    holy_mid(holy_diamond(HOLY_WHITE, 10, 60)),
    holy_mid(holy_diamond(HOLY_WHITE, 60, 10)),
    xysize=(70, 70))

image holy_motes_raw = Fixed(
    At("holy_sparkle", mote_rise(250, 420, 0.0)),
    At("holy_sparkle", mote_rise(440, 380, 0.5)),
    At("holy_sparkle", mote_rise(330, 480, 0.9)),
    At("holy_sparkle", mote_rise(470, 470, 1.4)),
    At("holy_sparkle", mote_rise(210, 360, 1.8)),
    At("holy_sparkle", mote_rise(390, 300, 2.3)),
    xysize=(700, 700))

image holy_glow = Fixed(
    holy_mid(At(holy_burst(8, 2000, 130, HOLY_GOLD, 0.10), holy_rays_in)),
    holy_mid(At(holy_burst(12, 1400, 30, HOLY_WHITE, 0.20), holy_thin_in)),
    holy_mid(At(holy_orb_stack(), holy_core_in)),
    holy_mid(At("holy_motes_raw", holy_motes_in)),
    xysize=(2000, 2000))

image holy_flash:
    Solid("#fff2cc")
    alpha 0.0
    pause 1.7
    easein 0.2 alpha 0.8
    easeout 1.6 alpha 0.12


# ══════════════════════════════════════════════
# ARENA — DAY, THREE CONVICTS
# Camera : master layer tilted -3°, zoom 1.1
#          (a 1920x1080 frame rotated 3° needs at least x1.092
#           or the black corners peek in)
#          show the layer AFTER `scene`, scene resets it
# Marks  : Eva 0.40 / zoom 0.25, facing right
#          Therion 0.53 / zoom 0.26, behind her
# Convicts: villager PNGs are full 1920x1080 canvases, figure painted
#          in place, so each one anchors on its own figure centre
#          villager1  fig x 315  (~650 tall)  -> screen 0.22, zoom 1.15
#          villager2  fig x 960  (~925 tall)  -> screen 0.60, zoom 1.0
#          villager3  fig x 1636 (~640 tall)  -> screen 0.78, zoom 1.15
#          all three heads land around y 455
# Glow   : left (422, 680) / mid (1152, 680) / right (1498, 680)
# ══════════════════════════════════════════════

define CONVICT_L = (0.22, 315 / 1920.0, 1.15, 125)
define CONVICT_M = (0.60, 0.5, 1.0, 300)
define CONVICT_R = (0.78, 1636 / 1920.0, 1.15, 125)

transform eva_arena:
    subpixel True
    xzoom -1 xanchor 0.5 yanchor 1.0 ypos 1.0
    xpos 0.40 zoom 0.25 yoffset 48
    block:
        ease 1.8 yoffset 28
        ease 1.8 yoffset 48
        repeat

# face: -1 = facing right, 1 = facing left
# lean: + toward the right, - toward the left
transform eva_arena_bless(face=-1, lean=30):
    subpixel True
    xzoom face xanchor 0.5 yanchor 1.0 ypos 1.0
    xpos 0.40 zoom 0.25
    ease 0.5 xoffset lean yoffset 20
    pause 1.6
    ease 1.2 xoffset 0 yoffset 48
    block:
        ease 1.8 yoffset 28
        ease 1.8 yoffset 48
        repeat

# she turns her back on the two she's finished with
transform eva_arena_flip:
    subpixel True
    xanchor 0.5 yanchor 1.0 ypos 1.0
    xpos 0.40 zoom 0.25
    xzoom -1.0
    ease 0.3 xzoom 1.0
    block:
        ease 1.8 yoffset 28
        ease 1.8 yoffset 48
        repeat

transform therion_arena:
    subpixel True
    xanchor 0.5 yanchor 1.0 ypos 1.0
    xpos 0.53 zoom 0.26 yoffset 90

# c = one of CONVICT_L / CONVICT_M / CONVICT_R
# anchor is a fraction, so it stays on the figure at any zoom
# grey, dim, slow breathing
transform convict_pov(c):
    subpixel True
    xanchor c[1] yanchor 1.0 xpos c[0] ypos 1.0
    zoom c[2] yoffset c[3]
    matrixcolor SaturationMatrix(0.0) * BrightnessMatrix(-0.35) * TintMatrix("#ffffff")
    block:
        ease 2.6 yoffset (c[3] - 8)
        ease 2.6 yoffset c[3]
        repeat

# gloom lifts into warm light right as the glow blooms (1.7s, bird timing)
transform convict_blessed(c):
    subpixel True
    xanchor c[1] yanchor 1.0 xpos c[0] ypos 1.0
    zoom c[2] yoffset c[3]
    matrixcolor SaturationMatrix(0.0) * BrightnessMatrix(-0.35) * TintMatrix("#ffffff")
    pause 1.7
    ease 1.2 matrixcolor SaturationMatrix(0.0) * BrightnessMatrix(0.30) * TintMatrix("#ffe9a8")
    block:
        ease 2.6 yoffset (c[3] - 8)
        ease 2.6 yoffset c[3]
        repeat

transform convict_glow(x, y):
    anchor (0.5, 0.5) pos (x, y) zoom 0.32

# softer than holy_flash, and it fully clears since there are three of these
image arena_flash:
    Solid("#fff2cc")
    alpha 0.0
    pause 1.7
    easein 0.2 alpha 0.55
    easeout 1.4 alpha 0.0

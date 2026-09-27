
define PURIFY_DIR = "BG/PURIFICATIONMINIGAME/"

define purify_bg_dark = PURIFY_DIR + "BGRED.jpg"
define purify_bg_holy = PURIFY_DIR + "BGHOLY.jpg"
define purify_hand    = PURIFY_DIR + "EVAHAND.png"

define purify_villagers = [
    ("lady",  PURIFY_DIR + "ladyred.png",  PURIFY_DIR + "ladyholy.png",  (285, 575)),
    ("man",   PURIFY_DIR + "manred.png",   PURIFY_DIR + "manholy.png",   (945, 615)),
    ("woman", PURIFY_DIR + "womanred.png", PURIFY_DIR + "womanholy.png", (1580, 600)),
]

define PURIFY_HAND_ZOOM = 0.15
define purify_cursor = MouseDisplayable(
    Transform(purify_hand, zoom=PURIFY_HAND_ZOOM),
    int(267 * PURIFY_HAND_ZOOM), int(2 * PURIFY_HAND_ZOOM)
)

default purify_done = []


image bg_purify_holy = Transform("BG/PURIFICATIONMINIGAME/BGHOLY.jpg", xysize=(1920, 1080))
image villager_lady  = Transform("BG/PURIFICATIONMINIGAME/ladyholy.png",  crop=(74, 220, 597, 1186),  zoom=0.768)
image villager_man   = Transform("BG/PURIFICATIONMINIGAME/manholy.png",   crop=(903, 149, 651, 1257), zoom=0.768)
image villager_woman = Transform("BG/PURIFICATIONMINIGAME/womanholy.png", crop=(1815, 222, 553, 1184), zoom=0.768)

define VLADY_X  = 286
define VMAN_X   = 943
define VWOMAN_X = 1606

image purify_flash_img = Solid("#fffbe6")


init python:
    def purify_fit(img, **kw):
        return Transform(img, xysize=(1920, 1080), **kw)

    def purify_villager(vid):
        if vid in store.purify_done:
            return
        store.purify_done.append(vid)
        renpy.play("audio/light.mp3", channel="audio")
        renpy.restart_interaction()

    def make_purify_burst():
        f = Fixed(xysize=(1500, 1500))

        for size, a in ((420, 0.10), (300, 0.14), (200, 0.20), (120, 0.35), (60, 0.6)):
            for r in (0, 45):
                f.add(Transform(Solid("#fff6c8", xysize=(size, size)),
                                rotate=r, alpha=a, align=(0.5, 0.5)))

        for i, ang in enumerate(range(0, 180, 15)):
            if i % 2 == 0:
                ray = Solid("#fff4b0", xysize=(16, 1500))
            else:
                ray = Solid("#ffffff", xysize=(8, 900))
            f.add(Transform(ray, rotate=ang, align=(0.5, 0.5), alpha=0.8))

        return f

image purify_burst = make_purify_burst()


transform purify_burst_at(c):
    pos c
    anchor (0.5, 0.5)
    blend "add"
    on appear:
        alpha 0.0
    on show:
        zoom 0.05
        alpha 1.0
        rotate 0
        parallel:
            easeout 0.35 zoom 1.1
            linear 0.9 zoom 1.4
        parallel:
            pause 0.35
            linear 0.9 alpha 0.0
        parallel:
            linear 1.25 rotate 30

transform purify_flash:
    on appear:
        alpha 0.0
    on show:
        alpha 0.55
        linear 0.4 alpha 0.0

transform purify_appear(t=0.6):
    on appear:
        alpha 1.0
    on show:
        alpha 0.0
        linear t alpha 1.0
    on hide:
        linear 0.3 alpha 0.0

transform purify_vanish:
    on appear, show:
        alpha 1.0
    on hide:
        linear 0.6 alpha 0.0

transform purify_hint_pulse:
    on appear, show:
        alpha 0.0
        linear 0.8 alpha 1.0
        block:
            linear 1.2 alpha 0.6
            linear 1.2 alpha 1.0
            repeat
    on hide:
        linear 0.4 alpha 0.0


transform villager_spot(x):
    anchor (0.5, 1.0)
    pos (x, 1080)

transform villager_hop(x):
    anchor (0.5, 1.0)
    pos (x, 1080)
    easein 0.12 yoffset -25
    easeout 0.18 yoffset 0

transform villager_wobble_out(x, dist, t=2.4):
    anchor (0.5, 1.0)
    transform_anchor True
    pos (x, 1080)
    parallel:
        linear t xoffset dist
    parallel:
        block:
            ease 0.3 rotate 7
            ease 0.3 rotate -7
            repeat
    parallel:
        block:
            easein 0.15 yoffset -14
            easeout 0.15 yoffset 0
            repeat


screen purification_minigame():
    layer "master"
    modal True

    on "show"     action SetField(config, "mouse_displayable", purify_cursor)
    on "hide"     action SetField(config, "mouse_displayable", None)
    on "replaced" action SetField(config, "mouse_displayable", None)

    $ all_done = len(purify_done) >= len(purify_villagers)

    add purify_fit(purify_bg_dark)
    showif all_done:
        add purify_fit(purify_bg_holy) at purify_appear(1.5)

    for vid, dark, holy, center in purify_villagers:
        showif vid in purify_done:
            add purify_fit(holy) at purify_appear(0.6)
        showif vid not in purify_done:
            imagebutton:
                idle purify_fit(dark)
                hover purify_fit(dark, matrixcolor=BrightnessMatrix(0.12))
                focus_mask True
                action Function(purify_villager, vid)
                at purify_vanish

    for vid, dark, holy, center in purify_villagers:
        showif vid in purify_done:
            add Solid("#fffbe6") at purify_flash
        showif vid in purify_done:
            add "purify_burst" at purify_burst_at(center)

    if all_done:
        timer 2.5 action Return()

screen purification_hint():
    layer "screens"
    zorder 50

    showif len(purify_done) < len(purify_villagers):
        text "Click on villager to purify them":
            xalign 0.5
            ypos 60
            size 42
            color "#fff6d0"
            outlines [(3, "#2a0000", 0, 0)]
            at purify_hint_pulse
label purification_minigame:
    $ purify_done = []
    $ _purify_old_qm = quick_menu
    $ quick_menu = False

    show screen purification_hint
    call screen purification_minigame
    hide screen purification_hint

    $ quick_menu = _purify_old_qm

    scene bg_purify_holy
    show villager_lady  at villager_spot(VLADY_X)
    show villager_man   at villager_spot(VMAN_X)
    show villager_woman at villager_spot(VWOMAN_X)

    $ renpy.block_rollback()
    return
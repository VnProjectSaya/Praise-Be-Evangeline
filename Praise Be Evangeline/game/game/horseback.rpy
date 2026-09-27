
image carriage_bg_a = "BG/LOOPBG.jpg"
image carriage_bg_b = "BG/LOOPBG.jpg"


transform carriage_sway:
    subpixel True
    xoffset 0
    yoffset 0

    parallel:
        block:
            easein 1.8 xoffset 3
            easeout 1.5 xoffset -1
            easein 2.2 xoffset -3
            easeout 1.8 xoffset 1
            ease 1.7 xoffset 0
            repeat

    parallel:
        block:
            easein 1.4 yoffset 2
            easeout 1.6 yoffset -3
            easein 2.0 yoffset 1
            easeout 1.5 yoffset -2
            ease 1.5 yoffset 0
            repeat
transform carriage_therion_bob:
    ypos 0
    linear 0.5 ypos 12
    linear 0.5 ypos 0
    repeat


image carriage_eva_hair:
    zoom 0.64
    "BG/CARRIAGE CG/EVAHAIR1.png"
    pause 4.5
    "BG/CARRIAGE CG/EVAHAIR2.png"
    pause 4.5
    repeat


image carriage_eva_eyes:
    zoom 0.64
    "BG/CARRIAGE CG/EVAEYEOPEN.png"
    pause 6.0
    "BG/CARRIAGE CG/EVAEYEHALF.png"
    pause 0.08
    "BG/CARRIAGE CG/EVAEYECLOSED.png"
    pause 0.08
    "BG/CARRIAGE CG/EVAEYEHALF.png"
    pause 0.08
    "BG/CARRIAGE CG/EVAEYEOPEN.png"
    repeat

image carriage_eva_eyes_half:
    zoom 0.64
    "BG/CARRIAGE CG/EVAEYEHALF.png"
    pause 4.0
    "BG/CARRIAGE CG/EVAEYECLOSED.png"
    pause 0.1
    "BG/CARRIAGE CG/EVAEYEHALF.png"
    pause 4.0
    repeat


image carriage_therion_eyes_half:
    zoom 0.64
    "BG/CARRIAGE CG/THERIONEYEHALF.png"
    pause 4.0
    "BG/CARRIAGE CG/THERIONEYECLOSED.png"
    pause 0.1
    "BG/CARRIAGE CG/THERIONEYEHALF.png"
    pause 4.0
    repeat

image carriage_eva_wings:
    zoom 0.64
    contains:
        "BG/CARRIAGE CG/EVAWING1.png"
    contains:
        "BG/CARRIAGE CG/EVAWING2.png"
        alpha 0.0
        ease 3.0 alpha 1.0
        ease 3.0 alpha 0.0
        repeat


layeredimage carriage_eva:
    group wings:
        attribute wings default "carriage_eva_wings"

    group body:
        attribute body default Transform("BG/CARRIAGE CG/EYABODY.png", zoom=0.64)

    group mouth:
        attribute smile default Transform("BG/CARRIAGE CG/EVAMOUTHSMILE.png", zoom=0.64)
        attribute oh Transform("BG/CARRIAGE CG/EVAMOUTHOH.png", zoom=0.64)

    group eyes:
        attribute normal default "carriage_eva_eyes"
        attribute half "carriage_eva_eyes_half"

    group brows:
        attribute brownormal default Transform("BG/CARRIAGE CG/BROWNORMAL.png", zoom=0.64)
        attribute browsad Transform("BG/CARRIAGE CG/BROWSAD.png", zoom=0.64)

    group hair:
        attribute hair default "carriage_eva_hair"


image carriage_frame = Transform("BG/CARRIAGE CG/carriage.png", zoom=0.64)

transform night_tint:
    matrixcolor BrightnessMatrix(-0.35) * TintMatrix("#3a5aa8")
image carriage_therion_eyes:
    zoom 0.64
    "BG/CARRIAGE CG/THERIONEYEOPEN.png"
    pause 6.0
    "BG/CARRIAGE CG/THERIONEYEHALF.png"
    pause 0.08
    "BG/CARRIAGE CG/THERIONEYECLOSED.png"
    pause 0.08
    "BG/CARRIAGE CG/THERIONEYEHALF.png"
    pause 0.08
    "BG/CARRIAGE CG/THERIONEYEOPEN.png"
    repeat

image carriage_therion_eyesyan:
    zoom 0.64
    "BG/CARRIAGE CG/THERIONEYEOPENYAN.png"
    pause 6.0
    "BG/CARRIAGE CG/THERIONEYEHALFYAN.png"
    pause 0.08
    "BG/CARRIAGE CG/THERIONEYECLOSED.png"
    pause 0.08
    "BG/CARRIAGE CG/THERIONEYEHALFYAN.png"
    pause 0.08
    "BG/CARRIAGE CG/THERIONEYEOPENYAN.png"
    repeat

layeredimage carriage_therion:
    group body:
        attribute body default Transform("BG/CARRIAGE CG/THERIONBODY.png", zoom=0.64)

    group mouth:
        attribute smile default Transform("BG/CARRIAGE CG/THERIONMOUTHSMILE.png", zoom=0.64)
        attribute grin Transform("BG/CARRIAGE CG/THERIONMOUTHGRIN.png", zoom=0.64)
        attribute oh Transform("BG/CARRIAGE CG/THERIONMOUTHOH.png", zoom=0.64)
        attribute frown Transform("BG/CARRIAGE CG/THERIONMOUTHFROWN.png", zoom=0.64)
        attribute yandere Transform("BG/CARRIAGE CG/THERIONMOUTHYAN.png", zoom=0.64)

    group eyes:
        attribute normal default "carriage_therion_eyes"
        attribute yan default "carriage_therion_eyesyan"
        attribute half "carriage_therion_eyes_half"

    group brows:
        attribute brownormal default Transform("BG/CARRIAGE CG/THERIONBROWNORMAL.png", zoom=0.64)
        attribute browfurrow Transform("BG/CARRIAGE CG/THERIONBROWFURROW.png", zoom=0.64)
        attribute browangry Transform("BG/CARRIAGE CG/THERIONBROWANGRY.png", zoom=0.64)

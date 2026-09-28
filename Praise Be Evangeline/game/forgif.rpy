
image therion_eva_base:
    "BG/anim/baseframe1.png"
    pause 1.0
    "BG/anim/basefram2.png" with Dissolve(1.5)
    pause 2.5
    "BG/anim/baseframe1.png" with Dissolve(1.5)
    pause 1.5
    repeat

image therion_eva_blink:
    "BG/anim/therioneyeopen.png"
    pause 3.8
    "BG/anim/therioneyehalf.png"
    pause 0.05
    "BG/anim/therioneyeclosed.png"
    pause 0.1
    "BG/anim/therioneyehalf.png"
    pause 0.05
    repeat

image therion_eva_hands:
    "BG/anim/topframe1.png"
    pause 5.0
    "BG/anim/topframe2.png"
    pause 0.12
    "BG/anim/topframe3.png"
    pause 0.12
    "BG/anim/topframe4.png"
    pause 0.12
    "BG/anim/topframe5.png"
    pause 5.0
    "BG/anim/topframe4.png"
    pause 0.12
    "BG/anim/topframe3.png"
    pause 0.12
    "BG/anim/topframe2.png"
    pause 0.12
    repeat

image cg therion_eva = Transform(
    Fixed(
        "therion_eva_base",
        "BG/anim/evaeyenormal.png",
        "therion_eva_blink",
        "therion_eva_hands",
        xysize=(3000, 1687),
    ),
    xysize=(1920, 1080),
)
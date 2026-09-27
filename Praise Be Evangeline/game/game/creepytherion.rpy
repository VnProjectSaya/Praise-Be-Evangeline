transform therion_fit:
    xysize (1920, 1080)

transform therion_blur(amount=0.0):
    blur amount

transform therion_jumpscare:
    subpixel True
    zoom 1.0
    ease 0.05 zoom 1.18
    ease 0.12 zoom 1.0

# Faster wipe durations for snappy eye blinks
define eye_close_wipe = ImageDissolve("BG/CREEPYTHERION/eye.png", 0.05, ramplen=128)
define eye_open_wipe = ImageDissolve("BG/CREEPYTHERION/eye.png", 0.08, ramplen=128)

image therion_base = "BG/CREEPYTHERION/BASE.png"
image therion_mouth1 = "BG/CREEPYTHERION/MOUTH1.png"
image therion_blink_dark = Solid("#000000", xysize=(1920, 1080))

# Fast rip through mouth frames on jumpscare: normal mouth -> wide smile -> full tear
image therion_mouth_jumpscare:
    "BG/CREEPYTHERION/MOUTH1.png"
    pause 0.03
    "BG/CREEPYTHERION/MOUTH2.png"
    pause 0.03
    "BG/CREEPYTHERION/MOUTH3.png"

# White flash on reveal
image therion_flash:
    Solid("#FFFFFF")
    alpha 0.0
    pause 0.06
    linear 0.02 alpha 0.9
    linear 0.18 alpha 0.0

# Eye animation sequence
image therion_creepy_eyes:
    "BG/CREEPYTHERION/FULLEYE.png"
    pause 5.0
    "BG/CREEPYTHERION/HALFEYE.png"
    pause 0.06
    "BG/CREEPYTHERION/QUARTEREYE.png"
    pause 0.06
    "BG/CREEPYTHERION/CLOSEDEYE.png"
    pause 0.08
    "BG/CREEPYTHERION/QUARTEREYE.png"
    pause 0.06
    "BG/CREEPYTHERION/HALFEYE.png"
    pause 0.06
    "BG/CREEPYTHERION/FULLEYE.png"
    repeat
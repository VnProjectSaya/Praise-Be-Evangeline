
# Size 2500 x 3500

image therion_body:
    "Therion/Body_anim_1.png"
    pause 2.5
    "Therion/Body_anim_2.png"
    pause 2.5
    repeat

image therion_body1:
    "Therion/Body1_anim_1.png"
    pause 2.5
    "Therion/Body1_anim_2.png"
    pause 2.5
    repeat
image therion_eye_open:
    "Therion/Eye/Open.png"
    pause 6.0
    "Therion/Eye/Half.png"
    pause 0.08
    "Therion/Eye/Closed.png"
    pause 0.08
    "Therion/Eye/Half.png"
    pause 0.08
    "Therion/Eye/Open.png"
    repeat

image therion_eye_half:
    "Therion/Eye/Half.png"
    pause 6.08
    "Therion/Eye/Closed.png"
    pause 0.08
    "Therion/Eye/Half.png"
    pause 0.08
    "Therion/Eye/Open.png"
    repeat

image therion_eye_luv:
    "Therion/Eye/Open_Luv.png"
    pause 6.0
    "Therion/Eye/Half_Luv.png"
    pause 0.08
    "Therion/Eye/Closed.png"
    pause 0.08
    "Therion/Eye/Half_Luv.png"
    pause 0.08
    "Therion/Eye/Open_Luv.png"
    repeat
image therion_eye_luvhalf:
    "Therion/Eye/Half_Luv.png"
    pause 6.08
    "Therion/Eye/Closed.png"
    pause 0.08
    "Therion/Eye/Half_Luv.png"
    pause 0.08
    "Therion/Eye/Open_Luv.png"
    repeat
image therion_eye_shook:
    "Therion/Eye/Op_Shook.png"
    pause 6.0
    "Therion/Eye/Half_Shook.png"
    pause 0.08
    "Therion/Eye/Closed.png"
    pause 0.08
    "Therion/Eye/Half_Shook.png"
    pause 0.08
    "Therion/Eye/Op_Shook.png"
    repeat

image therion_mouth_distort:
    "Therion/Mouth/Laugh.png"
    xoffset 0
    pause 0.9
    "Therion/Mouth/Distort_Grin.png"
    xoffset 6
    pause 0.05
    "Therion/Mouth/Laugh.png"
    xoffset -4
    pause 0.04
    "Therion/Mouth/Distort_Grin.png"
    xoffset 0
    pause 1.4
    "Therion/Mouth/Laugh.png"
    pause 0.06
    "Therion/Mouth/Distort_Grin.png"
    xoffset 8
    pause 0.03
    "Therion/Mouth/Laugh.png"
    xoffset 0
    pause 0.5
    "Therion/Mouth/Distort_Grin.png"
    pause 0.08
    repeat
init python:
    def therion_pupil_jitter(trans, st, at):
        trans.xoffset = renpy.random.randint(-4, 4)
        trans.yoffset = renpy.random.randint(-2, 2)
        return renpy.random.choice([0.03, 0.04, 0.06, 0.08, 0.12, 0.25, 0.6])
transform therion_pupil_shake:
    function therion_pupil_jitter
image therion_eye_creepy = Fixed(
    "Therion/Eye/Creepy.png",
    AlphaMask(
        At("Therion/Eye/Creepy_Pupil.png", therion_pupil_shake),
        "Therion/Eye/Creepy_Mask.png",
    ),
)

layeredimage therion:
    group body:
        attribute body0 default "therion_body"
        attribute body1 "therion_body1"
    always "Therion/nose.png"

    group brows:
        attribute browneutral default "Therion/Brow/Neutral.png"
        attribute browmad "Therion/Brow/Mad.png"
        attribute browsad "Therion/Brow/Sad.png"
        attribute browskeptical "Therion/Brow/Skeptical.png"

    group blush:
        attribute noblush default Null()
        attribute blush "Therion/blush.png"

    group eyes:
        attribute open default "therion_eye_open"
        attribute half "therion_eye_half"
        attribute luv "therion_eye_luv"
        attribute luvhalf "therion_eye_luvhalf"
        attribute shook "therion_eye_shook"
        attribute closed "Therion/Eye/Closed.png"
        attribute creepy "therion_eye_creepy"

    group mouth:
        attribute neutral default "Therion/Mouth/Neutral.png"
        attribute smile "Therion/Mouth/Smile.png"
        attribute grin "Therion/Mouth/Grin.png"
        attribute smug "Therion/Mouth/Smug.png"
        attribute laugh "Therion/Mouth/Laugh.png"
        attribute frown "Therion/Mouth/Frown.png"
        attribute annoyed "Therion/Mouth/Annoyed.png"
        attribute angry "Therion/Mouth/Angry.png"
        attribute gritannoyed "Therion/Mouth/GritAnnoyed.png"
        attribute gritangry "Therion/Mouth/GritAngry.png"
        attribute distort "therion_mouth_distort"

    group hair:
        attribute hair1 default "Therion/hair1.png"
        attribute hair2 "Therion/hair2.png"

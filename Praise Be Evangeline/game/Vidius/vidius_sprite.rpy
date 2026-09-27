
image vidius_body_calm:
    "Vidius/Body_Anim_2.png"
    pause 0.5
    "Vidius/Body_Anim_1.png"
    pause 9.5
    repeat

image vidius_body_blood:
    "Vidius/Body_Anim_Blood2.png"
    pause 0.5
    "Vidius/Body_Anim_Blood1.png"
    pause 9.5
    repeat

image vidius_body_agitated:
    "Vidius/Body_Anim_2.png"
    pause 0.4
    "Vidius/Body_Anim_1.png"
    pause 2.1
    "Vidius/Body_Anim_2.png"
    pause 0.4
    "Vidius/Body_Anim_1.png"
    pause 2.1
    repeat

image vidius_eye_blink_normal:
    "Vidius/Eye/Open_Normal.png"
    pause 6.0
    "Vidius/Eye/Half_Normal.png"
    pause 0.08
    "Vidius/Eye/Closed.png"
    pause 0.08
    "Vidius/Eye/Half_Normal.png"
    pause 0.08
    "Vidius/Eye/Open_Normal.png"
    repeat

image vidius_eye_blink_shocked:
    "Vidius/Eye/Open_Shocked.png"
    pause 6.0
    "Vidius/Eye/Half_Shocked.png"
    pause 0.08
    "Vidius/Eye/Closed.png"
    pause 0.08
    "Vidius/Eye/Half_Shocked.png"
    pause 0.08
    "Vidius/Eye/Open_Shocked.png"
    repeat


image vidius_shadow_multiply:
    "Vidius/Shadows.png"
    blend "multiply"


layeredimage vidius:
    group body:
        attribute calm default "vidius_body_calm"
        attribute agitated "vidius_body_agitated"
        attribute blood "vidius_body_blood"

    group brows:
        attribute browneutral default "Vidius/Brow/Neutral.png"
        attribute browmad "Vidius/Brow/Mad.png"
        attribute browsad "Vidius/Brow/Sad.png"

    group eyes:
        attribute eyenormal default "vidius_eye_blink_normal"
        attribute eyeshocked "vidius_eye_blink_shocked"
        attribute eyeclosed "Vidius/Eye/Closed.png"
        attribute noeyes Null()

    group mouth:
        attribute neutral default "Vidius/Mouth/Neutral.png"
        attribute smile "Vidius/Mouth/Smile.png"
        attribute frown "Vidius/Mouth/Frown.png"
        attribute angry "Vidius/Mouth/Angry.png"
        attribute shockedm "Vidius/Mouth/Shocked.png"
        attribute surprised "Vidius/Mouth/Surprised.png"

    group shadow:
        attribute noshadow default Null()
        attribute shadow "vidius_shadow_multiply"

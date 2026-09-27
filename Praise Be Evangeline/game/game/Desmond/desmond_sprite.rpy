
image desmond_body_calm:
    "Desmond/Body_Anim_2.png"
    pause 0.5
    "Desmond/Body_Anim_1.png"
    pause 4

    repeat

image desmond_body_agitated:
    "Desmond/Body_Anim_2.png"
    pause 0.25
    "Desmond/Body_Anim_1.png"
    pause 2.35
    "Desmond/Body_Anim_2.png"
    pause 0.25
    "Desmond/Body_Anim_1.png"
    pause 2.35
    repeat

image desmond_eye_closed = "Desmond/Eye/Closed.png"
# EYEBLINK LOOP
image desmond_eye_blink_normal:
    "Desmond/Eye/Open_Normal.png"
    pause 6.0
    "Desmond/Eye/Half_Normal.png"
    pause 0.08
    "Desmond/Eye/Closed.png"
    pause 0.08
    "Desmond/Eye/Half_Normal.png"
    pause 0.08
    "Desmond/Eye/Open_Normal.png"
    repeat

image desmond_eye_blink_shocked:
    "Desmond/Eye/Open_Shocked.png"
    pause 6.0
    "Desmond/Eye/Half_Shocked.png"
    pause 0.08
    "Desmond/Eye/Closed.png"
    pause 0.08
    "Desmond/Eye/Half_Shocked.png"
    pause 0.08
    "Desmond/Eye/Open_Shocked.png"
    repeat


image desmond_shadow_multiply:
    "Desmond/Shadow.png"
    blend "multiply"


layeredimage desmond:
    group body:
        attribute calm default "desmond_body_calm"
        attribute agitated "desmond_body_agitated"

    group brows:
        attribute browneutral default "Desmond/Brow/Neutral.png"
        attribute browmad "Desmond/Brow/Mad.png"
        attribute browsad "Desmond/Brow/Sad.png"

    group eyes:
        attribute normal default "desmond_eye_blink_normal"
        attribute shocked "desmond_eye_blink_shocked"
        attribute closed "desmond_eye_closed"

    group mouth:
        attribute neutral default "Desmond/Mouth/Neutral.png"
        attribute smile "Desmond/Mouth/Smile.png"
        attribute laugh "Desmond/Mouth/Laugh.png"
        attribute stern "Desmond/Mouth/Stern.png"
        attribute angry "Desmond/Mouth/Angry.png"
        attribute grit "Desmond/Mouth/Grit.png"
        attribute surprised "Desmond/Mouth/Surprised.png"

    group shadow:
        attribute noshadow default Null()
        attribute shadow "desmond_shadow_multiply"

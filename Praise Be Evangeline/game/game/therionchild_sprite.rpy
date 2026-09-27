
image therionchild_body:
    "TherionChild/Body_anim_2.png"
    pause 0.5
    "TherionChild/Body_anim_1.png"
    pause 9.5
    repeat


image therionchild_eye_blink_normal:
    "TherionChild/Eye/Open.png"
    pause 6.0
    "TherionChild/Eye/Half.png"
    pause 0.08
    "TherionChild/Eye/Closed.png"
    pause 0.08
    "TherionChild/Eye/Half.png"
    pause 0.08
    "TherionChild/Eye/Open.png"
    repeat

image therionchild_eye_blink_empty:
    "TherionChild/Eye/Open_Empty.png"
    pause 6.0
    "TherionChild/Eye/Half_Empty.png"
    pause 0.08
    "TherionChild/Eye/Closed.png"
    pause 0.08
    "TherionChild/Eye/Half_Empty.png"
    pause 0.08
    "TherionChild/Eye/Open_Empty.png"
    repeat

image therionchild_eye_blink_half:
    "TherionChild/Eye/Half.png"
    pause 6.0
    "TherionChild/Eye/Closed.png"
    pause 0.08
    "TherionChild/Eye/Half.png"
    repeat

image therionchild_eye_blink_half_empty:
    "TherionChild/Eye/Half_Empty.png"
    pause 6.0
    "TherionChild/Eye/Closed.png"
    pause 0.08
    "TherionChild/Eye/Half_Empty.png"
    repeat


layeredimage therionchild:
    always "therionchild_body"

    group brows:
        attribute browneutral default "TherionChild/Brow/Neutral.png"
        attribute browmad "TherionChild/Brow/Mad.png"
        attribute browsad "TherionChild/Brow/Sad.png"

    group eyes:
        attribute normal default "therionchild_eye_blink_normal"
        attribute empty "therionchild_eye_blink_empty"
        attribute half "therionchild_eye_blink_half"
        attribute halfempty "therionchild_eye_blink_half_empty"
        attribute closed "TherionChild/Eye/Closed.png"

    group mouth:
        attribute worried default "TherionChild/Mouth/Worried.png"
        attribute happy "TherionChild/Mouth/Happy.png"
        attribute smile "TherionChild/Mouth/Smile.png"
        attribute frown "TherionChild/Mouth/Frown.png"
        attribute angry "TherionChild/Mouth/Angry.png"
        attribute surprised "TherionChild/Mouth/Surprised.png"

    group tears:
        attribute notears default Null()
        attribute tears "TherionChild/tears.png"

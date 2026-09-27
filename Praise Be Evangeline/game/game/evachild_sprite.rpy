
image evachild_body_calm:
    "EvaChild/Body_anim_2.png"
    pause 0.5
    "EvaChild/Body_anim_1.png"
    pause 9.5
    repeat

image evachild_body_agitated:
    "EvaChild/Body_anim_2.png"
    pause 0.4
    "EvaChild/Body_anim_1.png"
    pause 2.1
    "EvaChild/Body_anim_2.png"
    pause 0.4
    "EvaChild/Body_anim_1.png"
    pause 2.1
    repeat


image evachild_eye_blink_normal:
    "EvaChild/Eye/Open.png"
    pause 6.0
    "EvaChild/Eye/Half.png"
    pause 0.08
    "EvaChild/Eye/Closed.png"
    pause 0.08
    "EvaChild/Eye/Half.png"
    pause 0.08
    "EvaChild/Eye/Open.png"
    repeat

image evachild_eye_blink_empty:
    "EvaChild/Eye/Open_Empty.png"
    pause 6.0
    "EvaChild/Eye/Half_Empty.png"
    pause 0.08
    "EvaChild/Eye/Closed.png"
    pause 0.08
    "EvaChild/Eye/Half_Empty.png"
    pause 0.08
    "EvaChild/Eye/Open_Empty.png"
    repeat

image evachild_eye_blink_half:
    "EvaChild/Eye/Half.png"
    pause 6.0
    "EvaChild/Eye/Closed.png"
    pause 0.08
    "EvaChild/Eye/Half.png"
    repeat

image evachild_eye_blink_half_empty:
    "EvaChild/Eye/Half_Empty.png"
    pause 6.0
    "EvaChild/Eye/Closed.png"
    pause 0.08
    "EvaChild/Eye/Half_Empty.png"
    repeat


layeredimage evachild:
    group body:
        attribute calm default "evachild_body_calm"
        attribute agitated "evachild_body_agitated"

    group brows:
        attribute browneutral default "EvaChild/Brow/Neutral.png"
        attribute browmad "EvaChild/Brow/Mad.png"
        attribute browsad "EvaChild/Brow/Sad.png"

    group eyes:
        attribute normal default "evachild_eye_blink_normal"
        attribute empty "evachild_eye_blink_empty"
        attribute half "evachild_eye_blink_half"
        attribute halfempty "evachild_eye_blink_half_empty"
        attribute closed "EvaChild/Eye/Closed.png"

    group mouth:
        attribute happy default "EvaChild/Mouth/Happy.png"
        attribute smile "EvaChild/Mouth/smile.png"
        attribute frown "EvaChild/Mouth/Frown.png"
        attribute angry "EvaChild/Mouth/Angry.png"
        attribute oh "EvaChild/Mouth/Oh.png"

    group blush:
        attribute noblush default Null()
        attribute blush "EvaChild/blush.png"

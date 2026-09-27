
image eva_body_calm:
    "Evangeline/Body_Anim_2.png"
    pause 0.5
    "Evangeline/Body_Anim_1.png"
    pause 9.5
    repeat

image eva_body_agitated:
    "Evangeline/Body_Anim_2.png"
    pause 0.4
    "Evangeline/Body_Anim_1.png"
    pause 2.1
    "Evangeline/Body_Anim_2.png"
    pause 0.4
    "Evangeline/Body_Anim_1.png"
    pause 2.1
    repeat



image eva_normal_eye_blink_happy:
    "Evangeline/Eye/Open_Normal.png"
    pause 6.0
    "Evangeline/Eye/Half_Normal.png"
    pause 0.08
    "Evangeline/Eye/Closed_Happy.png"
    pause 0.08
    "Evangeline/Eye/Half_Normal.png"
    pause 0.08
    "Evangeline/Eye/Open_Normal.png"
    repeat

image eva_normal_eye_blink_sad:
    "Evangeline/Eye/Open_Normal.png"
    pause 6.0
    "Evangeline/Eye/Half_Normal.png"
    pause 0.08
    "Evangeline/Eye/Closed_Sad.png"
    pause 0.08
    "Evangeline/Eye/Half_Normal.png"
    pause 0.08
    "Evangeline/Eye/Open_Normal.png"
    repeat

image eva_yandere_eye_blink_happy:
    "Evangeline/Eye/Open_Shocked_Yandere.png"
    pause 3.0
    "Evangeline/Eye/Half_Shocked_Yandere.png"
    pause 0.06
    "Evangeline/Eye/Closed_Happy.png"
    pause 0.06
    "Evangeline/Eye/Half_Shocked_Yandere.png"
    pause 0.06
    "Evangeline/Eye/Open_Shocked_Yandere.png"
    repeat

image eva_yandere_eye_blink_sad:
    "Evangeline/Eye/Open_Shocked_Yandere.png"
    pause 3.0
    "Evangeline/Eye/Half_Shocked_Yandere.png"
    pause 0.06
    "Evangeline/Eye/Closed_Sad.png"
    pause 0.06
    "Evangeline/Eye/Half_Shocked_Yandere.png"
    pause 0.06
    "Evangeline/Eye/Open_Shocked_Yandere.png"
    repeat


image eva_shadow_multiply:
    "Evangeline/Shadow.png"
    blend "multiply"


layeredimage eva:
    group body:
        attribute calm default "eva_body_calm"
        attribute agitated "eva_body_agitated"

    group brows:
        attribute browneutral default "Evangeline/Brow/Neutral.png"
        attribute browhappy "Evangeline/Brow/Happy.png"
        attribute browmad "Evangeline/Brow/Mad.png"
        attribute browsad "Evangeline/Brow/Sad.png"
        attribute browevil "Evangeline/Brow/Evil.png"

    group eyes:
        attribute normal_happy default "eva_normal_eye_blink_happy"
        attribute normal_sad "eva_normal_eye_blink_sad"
        attribute yandere_happy "eva_yandere_eye_blink_happy"
        attribute yandere_sad "eva_yandere_eye_blink_sad"
        attribute closed_happy "Evangeline/Eye/Closed_Happy.png"
        attribute closed_sad "Evangeline/Eye/Closed_Sad.png"

    group mouth:
        attribute neutral default "Evangeline/Mouth/Neutral.png"
        attribute smile "Evangeline/Mouth/Smile.png"
        attribute laugh "Evangeline/Mouth/Laugh.png"
        attribute frown "Evangeline/Mouth/Frown.png"
        attribute angry "Evangeline/Mouth/Angry.png"
        attribute shocked "Evangeline/Mouth/Shocked.png"
        attribute what "Evangeline/Mouth/What.png"
        attribute yandereevilsmile "Evangeline/Mouth/YandereEvilSmile.png"
        attribute yanderesmug "Evangeline/Mouth/YandereSmug.png"

    group shadow:
        attribute noshadow default Null()
        attribute shadow "eva_shadow_multiply"

    group blush:
        attribute noblush default Null()
        attribute blush "Evangeline/Blush.png"

    always "Evangeline/Hair.png"

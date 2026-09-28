
label prologue:

    $ no_rollback_scene = False
    $ config.rollback_enabled = True

    $ current_frame = "dream"

    play music "hinokageri.mp3"


    scene black
    with fade

    show bg eva_bedroom_night_dark as bg_left at panel_left_in, eva_stage1
    show bg village_night_loop as bg_right at panel_right_in, therion_stage1
    show split_line at split_divider
    pause 1.2

    show evachild calm browneutral normal smile noblush at eva_face, eva_stage1
    show therionchild browneutral normal worried notears at therion_face, therion_stage1
    with dissolve

    en "Once upon a time, a girl lost her mother, and the world grew muted." (multiple=2)
    tn "Whole damn country was falling apart. No Saintess for years, everything gone to hell." (multiple=2)

    show therionchild browneutral normal frown notears

    en "She was seven when it happened. None knew why, only that it was so." (multiple=2)
    tn "I was nine when the last one keeled over dead. People stopped believing in miracles." (multiple=2)

    show evachild calm browsad half frown noblush
    show therionchild browsad half worried notears

    en "At the end, her mother asked for one promise: that she would be happy." (multiple=2)
    tn "My mum said saints were gone for good. You make do with what's left." (multiple=2)

    show evachild calm browsad normal frown noblush
    show therionchild browmad normal angry notears

    en "She gave her word like a good daughter, oblivious to what she had pledged." (multiple=2)
    tn "Make do. That's grown-up for 'shut up and suffer.' Took a while to figure that out." (multiple=2)

    show bg eva_bedroom_night_dark as bg_left at panel_left, eva_stage2
    show bg village_night_loop as bg_right at panel_right, therion_stage2
    show evachild calm browsad half frown noblush at eva_face, eva_stage2
    show therionchild browmad half angry notears at therion_face, therion_stage2
    with dissolve

    en "Her father was a holy man, and holy men are not supposed to break." (multiple=2)
    tn "Dad said holy men exist to govern us, wear fancy clothes to keep folks hoping. What bullshit." (multiple=2)

    show evachild calm browsad half frown noblush
    show therionchild browmad half angry notears

    en "Yet he shattered in secret." (multiple=2)
    tn "My parents worked themselves to bone. Get up, work, sleep, repeat till you drop." (multiple=2)

    show evachild calm browsad closed frown noblush
    show therionchild browneutral half worried notears

    en "His sermons continued, but his laughter died with her mother." (multiple=2)
    tn "Mum prayed every night through the wall. Dad ignored it. I never cared for any of it." (multiple=2)

    show evachild calm browsad half frown noblush

    en "Years slipped away, and the holy seat remained vacant." (multiple=2)
    tn "That empty throne on top didn't mean a bloody thing." (multiple=2)

    show bg eva_bedroom_night_dark as bg_left at panel_left, eva_stage3
    show bg village_night_loop as bg_right at panel_right, therion_stage3
    show evachild calm browsad half frown noblush at eva_face, eva_stage3
    show therionchild browmad half angry notears at therion_face, therion_stage3
    with dissolve

    en "Her father filled the void with ledgers and distant problems, leaving her behind." (multiple=2)
    tn "Even with an Archbishop, not a single damn thing changed." (multiple=2)

    show evachild calm browneutral half smile noblush
    show therionchild browmad normal angry notears

    en "So the girl learned to be good, playing her part as his dutiful daughter." (multiple=2)
    tn "So what were all those prancing fools in robes actually for?" (multiple=2)

    en "Then a thought struck her: if one could not feel sorrow, pain could never touch them." (multiple=2)
    tn "Grief's for idiots expecting things to get better. I clocked out when my dad got stabbed." (multiple=2)

    show evachild agitated browneutral normal happy blush
    show therionchild browneutral normal worried notears

    en "It seemed, to a girl of seven, a very clever thought indeed." (multiple=2)
    tn "Dad told me: 'Be clever, shut your mouth, and hold onto your things.'" (multiple=2)

    show bg eva_bedroom_night_dark as bg_left at panel_left, eva_stage4
    show bg village_night_loop as bg_right at panel_right, therion_stage4
    show evachild agitated browneutral normal happy blush at eva_face, eva_stage4
    show therionchild browmad half angry notears at therion_face, therion_stage4
    with dissolve

    en "She wanted a world with no grief left, a paradise built by her own hands." (multiple=2)
    tn "Because what you wanted didn't matter. You show 'em what you've got, the world steals it." (multiple=2)

    show therionchild browmad normal angry notears

    en "Imagine... a world where everyone is smiling!" (multiple=2)
    tn "The whole stinking lot can rot, for all I care." (multiple=2)

    show evachild calm browneutral normal smile noblush
    show therionchild browsad half worried tears

    en "She resolved to build it herself, no matter what it required." (multiple=2)
    tn "Then one night, everything burned." (multiple=2)

    scene black
    with dissolve

    en "It was not long before her first opportunity presented itself." (multiple=2)
    tn "Last time I ever saw my family." (multiple=2)

    show bg past_fire at past_bg_push
    with Dissolve(1.5)

    en "Unwatched, she slipped into the night and followed the smoke to a burning village." (multiple=2)
    tn "The village went up in flames. Thought I was dead for sure." (multiple=2)

    en "There, afraid and alone, was a boy." (multiple=2)
    tn "Then I saw a girl." (multiple=2)

    show ther_past idle at ther_past_in

    voice "VA/JASON/zero/T1.mp3"
    t "Momma! Momma, where's—I can't find her—"

    show layer master at past_cam_in
    show ther_past idle at ther_past_settle
    show eva_past fly at eva_past_in

    voice "VA/RAKUMAROO/Chapter 00/Ch0_Eva01.mp3"
    e "It is quite all right! Give me your hand!"

    show ther_past idle at ther_past_shake

    voice "VA/JASON/zero/T2.mp3"
    t "My legs feel weak... I can't breathe—"

    show eva_past fly at eva_past_touch
    show ther_past reach at ther_past_hold
    pause 1.2

    show touch_glow at past_touch_point
    show touch_flash

    en "She was far too small to carry him, so she reached towards him with her peculiar gift." (multiple=2)
    tn "This tiny hand reaches through the smoke out of fucking nowhere and yanked the hurt out." (multiple=2)

    scene black
    with Dissolve(1.5)

    camera


    scene bg past_fire at fire_bg_flicker:
        xysize (1920, 1080)

    show therionchild empty browsad worried tears at fire_glow:
        crop (472, 1000, 1347, 2500)
        zoom 0.32
        xanchor 0.5 yanchor 1.0
        xpos 0.3 ypos 1.0
        xzoom -1.0

    show evachild normal browneutral smile at fire_glow:
        crop (0, 1000, 1367, 2500)
        zoom 0.32
        xanchor 0.5 yanchor 1.0
        xpos 0.7 ypos 1.0
        xzoom -1.0
        yoffset -12
        block:
            ease 1.5 yoffset -24
            ease 1.5 yoffset -8
            repeat
    with dissolve

    voice "VA/JASON/zero/T3.mp3"
    t "... It doesn't hurt anymore."

    voice "VA/RAKUMAROO/Chapter 00/Ch0_Eva02.mp3"
    e "There now. Isn't that ever so much better?"

    en "He stopped sobbing even when tears still came out of him." (multiple=2)
    tn "Felt nothing. Absolute bugger all. But I was crying anyway. Didn't know why." (multiple=2)

    show therionchild halfempty
    voice "VA/JASON/zero/T4.mp3"
    t "What is this weird feeling on my chest?"

    show evachild happy
    voice "VA/RAKUMAROO/Chapter 00/Ch0_Eva03.mp3"
    e "Sssh! You are safe now! Follow me!"

    show evachild at fire_glow:
        ease 0.25 xzoom 1.0
        parallel:
            ease 1.6 xpos 1.3
        parallel:
            block:
                ease 1.5 yoffset -24
                ease 1.5 yoffset -8
                repeat

    show therionchild at fire_glow:
        pause 0.5
        parallel:
            linear 2.2 xpos 1.25
        parallel:
            block:
                ease 0.18 yoffset -8
                ease 0.18 yoffset 0
                repeat

    pause 2.4

    scene black
    with dissolve


    camera at grade_set(grade_day0)
    scene bg cellar
    with dissolve

    en "She concealed him in a disused storeroom behind the kitchens, telling no one." (multiple=2)
    tn "Parents gone, house ashes. So I went wherever she dragged me." (multiple=2)

    show therionchild empty browneutral worried notears:
        crop (472, 1000, 1347, 2500)
        zoom 0.32
        xanchor 0.5 yanchor 1.0
        xpos 0.3 ypos 1.0
        xzoom -1.0

    show evachild normal browneutral smile:
        crop (0, 1000, 1367, 2500)
        zoom 0.32
        xanchor 0.5 yanchor 1.0
        xpos 0.7 ypos 1.0
        xzoom -1.0
        yoffset -12
        block:
            ease 1.5 yoffset -24
            ease 1.5 yoffset -8
            repeat
    with dissolve

    show evachild browsad oh
    voice "VA/RAKUMAROO/Chapter 00/Ch0_Eva04.mp3"
    e "Now, you must remain utterly silent. If anyone discovers you, I shall be in deep trouble!"

    voice "VA/JASON/zero/T5.mp3"
    t "... Okay."

    show evachild browneutral happy
    voice "VA/RAKUMAROO/Chapter 00/Ch0_Eva05.mp3"
    e "What is your name?"

    voice "VA/JASON/zero/T6.mp3"
    t "Therion."

    show evachild smile:
        ease 0.2 yoffset -50
        ease 0.35 yoffset -16
        block:
            ease 1.5 yoffset -24
            ease 1.5 yoffset -8
            repeat
    voice "VA/RAKUMAROO/Chapter 00/Ch0_Eva06.mp3"
    e "What a curious name! Mine is Evangeline."

    show therionchild frown
    voice "VA/JASON/zero/T7.mp3"
    t "That's a weird name. Nobody in my alley's called that."

    show evachild agitated browmad angry:
        ease 0.12 yoffset 10
        ease 0.10 yoffset -8
        ease 0.10 yoffset 10
        ease 0.10 yoffset -8
        ease 0.10 yoffset 10
        ease 0.30 yoffset -12
        block:
            ease 1.5 yoffset -24
            ease 1.5 yoffset -8
            repeat
    voice "VA/RAKUMAROO/Chapter 00/Ch0_Eva07.mp3"
    e "It is NOT weird! Evangeline is a sacred Saintess name from centuries ago! It is practically the most grand name in existence."

    show therionchild halfempty frown:
        ease 0.3 xzoom 1.0
    voice "VA/JASON/zero/T8.mp3"
    t "... Whatever."

    show evachild calm

    scene black
    with dissolve


    camera at grade_set(grade_day1)
    scene bg cellar

    show therionchild empty browneutral worried:
        crop (472, 1000, 1347, 2500)
        zoom 0.32
        xanchor 0.5 yanchor 1.0
        xpos 0.3 ypos 1.0
        xzoom 1.0
    with dissolve

    show evachild normal browneutral smile:
        crop (0, 1000, 1367, 2500)
        zoom 0.32
        xanchor 0.5 yanchor 1.0
        xpos 0.7 ypos 1.0
        xzoom -1.0
        yoffset -420 alpha 0.0
        ease 1.8 yoffset -12 alpha 1.0
        block:
            ease 1.5 yoffset -24
            ease 1.5 yoffset -8
            repeat

    en "He spoke little that first day, sitting where she left him, staring into nothingness." (multiple=2)
    tn "Girl was glowing. Like magic. Thought she was a goddess or something. I just stared, brain completely blank." (multiple=2)

    show evachild oh
    voice "VA/RAKUMAROO/Chapter 00/Ch0_Eva08.mp3"
    e "Are you still hungry? I can fetch more bread."

    voice "VA/JASON/zero/T10.mp3"
    t "No."

    voice "VA/RAKUMAROO/Chapter 00/Ch0_Eva09.mp3"
    e "Are you cold?"

    voice "VA/JASON/zero/T10.mp3"
    t "No."

    show evachild browsad frown
    voice "VA/RAKUMAROO/Chapter 00/Ch0_Eva10.mp3"
    e "Are you sad?"

    show therionchild halfempty
    voice "VA/JASON/zero/T11.mp3"
    t "Don't know."

    show evachild smile:
        ease 1.4 xpos 0.47 yoffset 24

    en "Unsure how to respond, she sat beside him upon the dusty floor." (multiple=2)
    tn "She parks herself right next to me. Close enough I could count every single one of her eyelashes." (multiple=2)

    scene black
    with dissolve


    camera at grade_set(grade_day2)
    scene bg cellar

    show therionchild halfempty browneutral worried:
        crop (472, 1000, 1347, 2500)
        zoom 0.32
        xanchor 0.5 yanchor 1.0
        xpos 0.3 ypos 1.0
        xzoom -1.0
    with dissolve

    show evachild normal browneutral smile:
        crop (0, 1000, 1367, 2500)
        zoom 0.32
        xanchor 0.5 yanchor 1.0
        ypos 1.0
        xzoom -1.0
        xpos 1.15 yoffset -80
        ease 1.4 xpos 0.72 yoffset -10
        ease 0.3 yoffset 0
        parallel:
            linear 1.2 xpos 0.6
        parallel:
            block:
                ease 0.15 yoffset -6
                ease 0.15 yoffset 0
                repeat 4

    en "Then he began to speak a little more." (multiple=2)
    tn "Then my brain started working again. Just the one thought, but it was enough." (multiple=2)

    voice "VA/JASON/zero/T12.mp3"
    t "Bread again?"

    show evachild browsad oh
    voice "VA/RAKUMAROO/Chapter 00/Ch0_Eva11.mp3"
    e "Sorry! I can't risk being found out! Hang on a little bit more!"

    voice "VA/JASON/zero/T13.mp3"
    t "Thank you."

    show evachild browneutral smile
    voice "VA/RAKUMAROO/Chapter 00/Ch0_Eva12.mp3"
    e "You are very welcome."

    show evachild:
        ease 0.25 yoffset 25
        pause 0.2
        ease 0.3 yoffset 0

    en "She produced a set of jacks stolen from her nursery, scattering them across the flagstones." (multiple=2)
    tn "She brought stuff. Didn't care what. Her hands were soft, never done a day's work in her life." (multiple=2)

    show evachild happy
    voice "VA/RAKUMAROO/Chapter 00/Ch0_Eva13.mp3"
    e "Hey, I'm bored. Let's play! Do you know how to play jacks?"

    voice "VA/JASON/zero/T10.mp3"
    t "No."

    voice "VA/RAKUMAROO/Chapter 00/Ch0_Eva14.mp3"
    e "It is simple. Watch me."

    show evachild:
        block:
            ease 0.18 yoffset -40
            ease 0.22 yoffset 30
            ease 0.18 yoffset -35
            ease 0.30 yoffset 0
            pause 0.2
            repeat 2

    t "..."

    voice "VA/RAKUMAROO/Chapter 00/Ch0_Eva15.mp3"
    e "Now you try!"

    show therionchild:
        pause 0.3
        block:
            linear 0.20 yoffset -30
            linear 0.25 yoffset 22
            linear 0.20 yoffset -26
            linear 0.30 yoffset 0
            pause 0.3
            repeat 2

    voice "VA/JASON/zero/T14.mp3"
    t "Like this?"

    show evachild:
        ease 0.15 yoffset -20
        ease 0.2 yoffset 0
    voice "VA/RAKUMAROO/Chapter 00/Ch0_Eva16.mp3"
    e "Yes! You're a natural, Therion!"

    voice "VA/JASON/zero/T15.mp3"
    t "I have a good teacher."

    show evachild closed happy:
        block:
            ease 0.08 yoffset -8
            ease 0.08 yoffset 0
            repeat 4

    pause 0.8

    show therionchild empty smile:
        block:
            linear 0.12 yoffset -8
            linear 0.12 yoffset 0
            pause 0.1
            repeat 3

    en "She giggled, and after a beat, he imitated the sound, albeit very awkwardly." (multiple=2)
    tn "Tried to copy what she did. Laughing. 'Hahaha.' Yeah. Close enough." (multiple=2)

    show evachild normal oh
    voice "VA/RAKUMAROO/Chapter 00/Ch0_Eva17.mp3"
    e "Oh, you finally laugh!"

    show therionchild halfempty smile
    voice "VA/JASON/zero/T16.mp3"
    t "... I ain't scared of things anymore. Not since you touched me."

    show evachild smile
    voice "VA/RAKUMAROO/Chapter 00/Ch0_Eva18.mp3"
    e "That's good to hear~ I'll make sure you'll never feel scared again!"

    show therionchild empty worried
    voice "VA/JASON/zero/T17.mp3"
    t "Mm. I think I don't feel anything anymore."

    show evachild:
        ease 0.4 xpos 0.48
        ease 0.12 xoffset -10
        ease 0.12 xoffset 0
        ease 0.12 xoffset -10
        ease 0.12 xoffset 0
        pause 0.3
        ease 0.5 xpos 0.6

    en "Failing to understand, she patted his hand like a nursemaid and resumed the game." (multiple=2)
    tn "She touched my hand. I memorized every inch of it. The warmth, the weight... Without that, I would've got nothing." (multiple=2)


    show evachild normal smile:
        ease 0.25 xzoom 1.0
        ease 1.2 xpos 0.7 yoffset -60
        block:
            ease 1.5 yoffset -72
            ease 1.5 yoffset -56
            repeat

    voice "VA/RAKUMAROO/Chapter 00/Ch0_Eva19.mp3"
    e "Okay, I have to go home now or Papa will be mad."

    show therionchild halfempty worried:
        parallel:
            linear 0.9 xpos 0.38
        parallel:
            block:
                ease 0.15 yoffset -6
                ease 0.15 yoffset 0
                repeat 3

    voice "VA/JASON/zero/T17a.mp3"
    t "You're coming back again tomorrow, right?"

    show evachild happy
    voice "VA/RAKUMAROO/Chapter 00/Ch0_Eva20.mp3"
    e "Of course! I'll come back every day! I saved you! That makes you mine now."

    show evachild smile:
        ease 0.3 xzoom -1.0
        block:
            ease 1.5 yoffset -72
            ease 1.5 yoffset -56
            repeat

    voice "VA/RAKUMAROO/Chapter 00/Ch0_Eva21.mp3"
    e "Now, say: 'I belong to Evangeline.'"

    show therionchild empty worried
    voice "VA/JASON/zero/T17b.mp3"
    t "... I belong to Evangeline."

    camera at grade_shift(grade_day2, grade_bright, 1.5)
    show evachild closed happy:
        block:
            ease 0.09 yoffset -72
            ease 0.09 yoffset -58
            repeat 5
        block:
            ease 1.5 yoffset -72
            ease 1.5 yoffset -56
            repeat

    voice "VA/RAKUMAROO/Chapter 00/Ch0_Eva22.mp3"
    e "Hahaha~!"

    en "She laughed, delighted, giving no thought to the weight of his words." (multiple=2)
    tn "Her laugh was the only sound left in the world worth listening to." (multiple=2)

    show evachild normal happy:
        transform_anchor True
        parallel:
            block:
                ease 1.6 xpos 0.12 ypos 0.76 rotate -12
                ease 0.3 xzoom 1.0 rotate 0
                ease 1.8 xpos 0.88 ypos 0.87 rotate 12
                ease 0.3 xzoom -1.0 rotate 0
                ease 1.4 xpos 0.55 ypos 0.72 rotate -10
                ease 1.0 xpos 0.7 ypos 0.89 rotate -4
                repeat
        parallel:
            ease 0.3 yoffset 0
            block:
                ease 0.14 yoffset -22
                ease 0.26 yoffset 0
                repeat

    show therionchild normal worried:
        xzoom -1.0
        block:
            pause 0.85
            ease 0.2 xzoom 1.0
            pause 1.57
            ease 0.2 xzoom -1.0
            pause 3.58
            repeat

    en "Days passed, she noticed his eyes tracking her every movement across the room." (multiple=2)
    tn "A few days later I had more than one feeling back. Tried mimicking everything she did so I could pretend to be normal again." (multiple=2)

    en "She found it rather sweet, in a tragic sort of way." (multiple=2)
    tn "Wondered if I could stay close to something so pretty." (multiple=2)

    show evachild smile:
        ease 1.2 xpos 0.64 ypos 1.0 yoffset -12 rotate 0 xzoom -1.0
        block:
            ease 1.5 yoffset -24
            ease 1.5 yoffset -8
            repeat

    show therionchild:
        ease 0.2 xzoom -1.0

    voice "VA/RAKUMAROO/Chapter 00/Ch0_Eva23.mp3"
    e "Therion, you are staring again."

    voice "VA/JASON/zero/T18.mp3"
    t "You're in the room. What else am I gonna look?"

    show evachild oh
    voice "VA/RAKUMAROO/Chapter 00/Ch0_Eva24.mp3"
    e "The wall, perhaps? The ceiling? You used to stare at those for hours."

    show therionchild smile
    voice "VA/JASON/zero/T19.mp3"
    t "Those are boring. You're better."

    show evachild closed happy:
        ease 0.15 yoffset -40
        ease 0.3 yoffset -12
        block:
            ease 1.5 yoffset -24
            ease 1.5 yoffset -8
            repeat
    voice "VA/RAKUMAROO/Chapter 00/Ch0_Eva25.mp3"
    e "Aww!"

    show therionchild normal smile:
        parallel:
            linear 0.6 xpos 0.44
        parallel:
            block:
                ease 0.15 yoffset -6
                ease 0.15 yoffset 0
                repeat 2

    voice "VA/JASON/zero/T19a.mp3"
    t "...You really are."

    show evachild normal oh blush

    en "She felt a sudden warmth in her cheeks, entirely perplexed by it." (multiple=2)
    tn "Her cheeks went pink. Wondered if someone had slapped her." (multiple=2)

    camera at grade_shift(grade_bright, grade_soft, 2.5)

    show evachild half smile
    voice "VA/RAKUMAROO/Chapter 00/Ch0_Eva26.mp3"
    e "Well. That is very sweet of you, Therion."

    voice "VA/JASON/zero/T19b.mp3"
    t "Yeah."

    show evachild normal happy:
        ease 0.2 yoffset -36
        ease 0.4 yoffset -12
        block:
            ease 1.5 yoffset -24
            ease 1.5 yoffset -8
            repeat

    en "She smiled, and her heart gave a strange leap." (multiple=2)
    tn "She smiled at me. First time my chest didn't feel completely dead." (multiple=2)

    en "She found herself wishing he would never look away." (multiple=2)
    tn "I wanted her to smile at me forever." (multiple=2)

    scene black
    with fade

    stop music fadeout 1.0

    en "Please, don't stop." (multiple=2)
    tn "Please, again." (multiple=2)
    with fade


    pause 1.0

    play music "eva.mp3"

    camera at grade_set(grade_bright)
    scene bg cellar

    show therionchild normal browneutral worried notears:
        crop (472, 1000, 1347, 2500)
        zoom 0.32
        xanchor 0.5 yanchor 1.0
        xpos 0.25 ypos 1.0
        xzoom -1.0

    show evachild normal browneutral happy calm noblush:
        crop (0, 1000, 1367, 2500)
        zoom 0.32
        xanchor 0.5 yanchor 1.0
        xpos 0.5 ypos 1.0
        xzoom -1.0
        yoffset -12
        block:
            ease 1.5 yoffset -24
            ease 1.5 yoffset -8
            repeat
    with dissolve

    show evachild:
        ease 1.4 yoffset -110
        pause 0.8
        ease 0.12 yoffset -20
        ease 0.15 yoffset -34
        ease 0.2 yoffset -20
        block:
            ease 1.5 yoffset -32
            ease 1.5 yoffset -16
            repeat
    voice "VA/RAKUMAROO/Chapter 00/Ch0_Eva27.mp3"
    e "... And then Saint Carvilia held forth her hands over the entire parish, and everyone simply STOPPED feeling sorrow! Just like that! In a single moment!"

    show therionchild halfempty
    voice "VA/JASON/zero/T20.mp3"
    t "Cool."

    show evachild agitated browmad angry:
        ease 0.2 xoffset -30
        pause 0.6
        ease 0.4 xoffset 0
        block:
            ease 1.5 yoffset -24
            ease 1.5 yoffset -8
            repeat
    voice "VA/RAKUMAROO/Chapter 00/Ch0_Eva28.mp3"
    e "It is VASTLY more than cool, Therion! It is the most vital occurrence in the entire history of the church."

    show therionchild normal smile
    voice "VA/JASON/zero/T21.mp3"
    t "... The coolest."

    show evachild calm browneutral smile

    en "Every other child would call her weird, but Therion never did. He never judged." (multiple=2)
    tn "I liked her tales. Or maybe it was her voice I liked best. Couldn't bloody decide." (multiple=2)

    show evachild:
        ease 1.0 xpos 0.37 yoffset 0
        pause 0.3
        block:
            ease 0.1 xoffset -6
            ease 0.1 xoffset 0
            pause 0.25
            repeat 4

    en "She brought a ribbon of blue silk, one of her mother's keepsakes, tying it around his wrist without asking." (multiple=2)

    show therionchild surprised
    tn "She tied a ribbon on my wrist. Her fingers touched the skin of my arm for three seconds while she knotted it. What the hell did that mean?" (multiple=2)

    show evachild happy:
        parallel:
            linear 1.0 xpos 0.5
        parallel:
            block:
                ease 0.15 yoffset -6
                ease 0.15 yoffset 0
                repeat 3
        ease 0.4 yoffset -12
        block:
            ease 1.5 yoffset -24
            ease 1.5 yoffset -8
            repeat
    voice "VA/RAKUMAROO/Chapter 00/Ch0_Eva29.mp3"
    e "There. Now everyone shall know you belong to someone."

    show therionchild smile
    voice "VA/JASON/zero/T22.mp3"
    t "Mm."

    show evachild smile:
        ease 0.2 yoffset -50
        ease 0.35 yoffset -16
        block:
            ease 1.5 yoffset -24
            ease 1.5 yoffset -8
            repeat

    en "She was entirely certain then: if she was to be a Saintess, he would be her sworn protector." (multiple=2)
    tn "Naturally." (multiple=2)

    en "Then he asked her a question no one had ever dared utter." (multiple=2)
    tn "Then I finally asked." (multiple=2)

    show therionchild worried
    voice "VA/JASON/zero/T23.mp3"
    t "Does it hurt? When you do that thing with your hands?"

    show evachild oh:
        ease 0.3 xoffset 20
        block:
            ease 1.5 yoffset -24
            ease 1.5 yoffset -8
            repeat
    voice "VA/RAKUMAROO/Chapter 00/Ch0_Eva30.mp3"
    e "What thing?"

    show therionchild browsad:
        ease 0.5 xpos 0.29
    voice "VA/JASON/zero/T24.mp3"
    t "The pulling. You pulled something out of my chest during the fire. I felt it."

    show evachild happy
    voice "VA/RAKUMAROO/Chapter 00/Ch0_Eva31.mp3"
    e "Oh, that! A tiny sting at first, perhaps. But then it feels quite warm, actually."

    show therionchild browneutral
    voice "VA/JASON/zero/T9.mp3"
    t "What did it actually do?"

    show evachild:
        ease 0.6 yoffset -70
        block:
            ease 1.5 yoffset -82
            ease 1.5 yoffset -62
            repeat
    voice "VA/RAKUMAROO/Chapter 00/Ch0_Eva32.mp3"
    e "I took your pain away so you should never be sad again!"

    show therionchild halfempty smile
    voice "VA/JASON/zero/T25.mp3"
    t "Huh. Thanks."

    show evachild closed happy:
        block:
            ease 0.08 yoffset -70
            ease 0.08 yoffset -62
            repeat 4
        ease 0.6 yoffset -12
        block:
            ease 1.5 yoffset -24
            ease 1.5 yoffset -8
            repeat
    voice "VA/RAKUMAROO/Chapter 00/Ch0_Eva33.mp3"
    e "You are very welcome~"


    scene bg cellar

    show therionchild normal browneutral worried:
        crop (472, 1000, 1347, 2500)
        zoom 0.32
        xanchor 0.5 yanchor 1.0
        xpos 0.25 ypos 1.0
        xzoom -1.0
    with fade

    show evachild normal browneutral smile calm:
        crop (0, 1000, 1367, 2500)
        zoom 0.32
        xanchor 0.5 yanchor 1.0
        ypos 1.0
        xzoom -1.0
        xpos 1.15 yoffset -80
        ease 1.6 xpos 0.45 yoffset -12
        block:
            ease 1.5 yoffset -24
            ease 1.5 yoffset -8
            repeat

    en "She brought a book from her room, her name inscribed inside the cover." (multiple=2)
    tn "She gave me a book with her name on it. I read it over and over and over so many times the ink started smudging." (multiple=2)

    voice "VA/RAKUMAROO/Chapter 00/Ch0_Eva34.mp3"
    e "You may keep it. But you must promise to return it the moment I ask."

    voice "VA/JASON/zero/T26.mp3"
    t "Promise."

    show evachild browmad frown:
        ease 0.3 xoffset -25
        block:
            ease 1.5 yoffset -24
            ease 1.5 yoffset -8
            repeat
    voice "VA/RAKUMAROO/Chapter 00/Ch0_Eva35.mp3"
    e "It is my ABSOLUTE FAVORITE book, Therion. If you misplace it, I shall be dreadfully cross."

    show therionchild frown
    voice "VA/JASON/zero/T27.mp3"
    t "Won't lose it."

    show evachild browneutral oh:
        ease 0.4 xoffset -45
        block:
            ease 1.5 yoffset -24
            ease 1.5 yoffset -8
            repeat
    voice "VA/RAKUMAROO/Chapter 00/Ch0_Eva36.mp3"
    e "Do you swear?"

    show therionchild empty browneutral frown:
        parallel:
            linear 0.5 xpos 0.3
        parallel:
            ease 0.15 yoffset -6
            ease 0.15 yoffset 0
    voice "VA/JASON/zero/T28.mp3"
    t "Swear it. On my life."

    show evachild happy:
        ease 0.4 xoffset 0 yoffset -60
        ease 0.35 yoffset -16
        block:
            ease 1.5 yoffset -24
            ease 1.5 yoffset -8
            repeat
    voice "VA/RAKUMAROO/Chapter 00/Ch0_Eva37.mp3"
    e "On your life! Excellent. It is the most important book ever."

    en "She loved that he had sworn on his life. It sounded a lot like a knight's oath." (multiple=2)
    tn "She could've asked for my actual life right there, and I'd have handed it over on a plate." (multiple=2)

    show therionchild normal worried

    show evachild normal happy:
        transform_anchor True
        parallel:
            block:
                ease 0.25 xzoom 1.0
                ease 1.2 xpos 0.85 ypos 0.78 rotate 10
                ease 0.25 xzoom -1.0 rotate 0
                ease 1.0 xpos 0.62 ypos 0.9 rotate -10
                ease 0.4 ypos 0.97 rotate 0
                ease 0.6 ypos 0.82
                ease 0.9 xpos 0.45 ypos 0.86 rotate -8
                ease 0.3 rotate 0
                repeat
        parallel:
            ease 0.3 yoffset 0
            block:
                ease 0.14 yoffset -22
                ease 0.26 yoffset 0
                repeat

    en "Weeks pass, she had begun rearranging his storeroom." (multiple=2)
    tn "She moved her things in. Made the room hers by extension. I don't mind." (multiple=2)

    en "She bragged to the kitchen staff about her secret boy as one brags of a fine dress. She omitted his name, calling him 'mine'." (multiple=2)
    tn "Heard her through the door once. Telling someone: 'My boy in the storeroom. I saved him. He is mine.' Loved hearing that, if I'm honest." (multiple=2)

    show evachild smile:
        ease 1.0 xpos 0.42 ypos 1.0 yoffset -12 rotate 0 xzoom -1.0
        block:
            ease 1.5 yoffset -24
            ease 1.5 yoffset -8
            repeat
    show therionchild smile

    en "She was proud of him. He was hers and hers alone." (multiple=2)
    tn "That room was my world, and I loved it." (multiple=2)

    scene bg cellar:
        zoom 1.35
        xalign 0.4 yalign 0.35

    show therionchild normal browneutral smile notears:
        crop (472, 1000, 1347, 2500)
        zoom 0.46
        xanchor 0.5 yanchor 1.0
        xpos 0.2 ypos 1511
        xzoom -1.0

    show evachild normal browneutral smile calm noblush:
        crop (0, 1000, 1367, 2500)
        zoom 0.46
        xanchor 0.5 yanchor 1.0
        xpos 0.47 ypos 1511
        xzoom -1.0
        yoffset -20
        block:
            ease 1.5 yoffset -40
            ease 1.5 yoffset -14
            repeat
    with dissolve

    en "Then, her father discovered them." (multiple=2)
    tn "Then the old man walked in." (multiple=2)

    show desmond shocked browsad surprised calm noshadow behind therionchild, evachild:
        zoom 0.5
        xanchor 0.5 yanchor 1.0
        ypos 1900
        xzoom 1.0
        xpos 1.3
        parallel:
            linear 1.6 xpos 0.86
        parallel:
            block:
                ease 0.3 yoffset -14
                ease 0.3 yoffset 0
                repeat 3

    show evachild oh:
        ease 0.15 yoffset -90
        ease 0.25 xzoom 1.0 yoffset -28
        block:
            ease 1.5 yoffset -40
            ease 1.5 yoffset -14
            repeat

    show therionchild worried

    voice "VA/GARFUNKEL/CH0/DES1.mp3"
    de "Eva? Eva, whose child is this? What has happened here?"

    show evachild agitated happy:
        ease 0.2 yoffset -80
        ease 0.3 yoffset -28
        ease 0.2 yoffset -80
        ease 0.3 yoffset -28
        block:
            ease 1.5 yoffset -40
            ease 1.5 yoffset -14
            repeat
    voice "VA/RAKUMAROO/Chapter 00/Ch0_Eva38.mp3"
    e "I saved him, Papa! There was a fire, and I found him, and I made all his hurting go away! Just like in Mama's stories!"

    show desmond agitated browmad angry:
        parallel:
            linear 0.5 xpos 0.82
        parallel:
            ease 0.25 yoffset -14
            ease 0.25 yoffset 0
    voice "VA/GARFUNKEL/CH0/DES2.mp3"
    de "No, you didn't just...! You took EVERYTHING away, Eva!"

    show evachild happy:
        ease 0.6 xpos 0.36
        block:
            ease 1.5 yoffset -40
            ease 1.5 yoffset -14
            repeat
    show therionchild halfempty worried
    voice "VA/RAKUMAROO/Chapter 00/Ch0_Eva39.mp3"
    e "Yes! But see!? He doesn't cry anymore! I fixed it too!"

    show desmond calm shocked browsad surprised shadow

    en "Her father did not look proud. He looked horrified, exactly as he had the day Mama died. She did not know why." (multiple=2)

    show therionchild normal frown
    tn "He stared at me like I was some bloody monster. Okay, I probably looked like one next to her anyway." (multiple=2)

    show desmond:
        ease 0.12 xpos 0.88 yoffset -14
        ease 0.3 yoffset 0
    voice "VA/GARFUNKEL/CH0/DES3.mp3"
    de "No... What have you done...?"

    show evachild agitated browmad angry:
        ease 0.3 xpos 0.44
        ease 0.12 yoffset 18
        ease 0.10 yoffset -14
        ease 0.10 yoffset 18
        ease 0.10 yoffset -14
        ease 0.10 yoffset 18
        ease 0.30 yoffset -20
        block:
            ease 1.5 yoffset -40
            ease 1.5 yoffset -14
            repeat
    voice "VA/RAKUMAROO/Chapter 00/Ch0_Eva40.mp3"
    e "I HELPED him! The way I am going to help everyone, someday, once I have practiced enough!"

    show desmond noshadow browmad surprised
    voice "VA/GARFUNKEL/CH0/DES4.mp3"
    de "Practiced?!"

    show evachild:
        ease 0.12 xoffset 25 yoffset 18
        ease 0.10 yoffset -14
        ease 0.10 yoffset 18
        ease 0.10 yoffset -14
        ease 0.10 yoffset 18
        ease 0.30 xoffset 0 yoffset -20
        block:
            ease 1.5 yoffset -40
            ease 1.5 yoffset -14
            repeat
    voice "VA/RAKUMAROO/Chapter 00/Ch0_Eva41.mp3"
    e "Yes! Saint Carvilia practiced for YEARS before she got it right! I'll try to be better than her!"

    show desmond agitated normal browmad grit:
        parallel:
            linear 0.6 xpos 0.8
        parallel:
            ease 0.3 yoffset -14
            ease 0.3 yoffset 0
    voice "VA/GARFUNKEL/CH0/DES5.mp3"
    de "This is not a storybook, Eva! This is someone else's LIFE!"

    show evachild calm browsad oh:
        ease 0.5 xpos 0.52
        block:
            ease 1.5 yoffset -40
            ease 1.5 yoffset -14
            repeat
    voice "VA/RAKUMAROO/Chapter 00/Ch0_Eva42.mp3"
    e "But Papa—!"

    show desmond agitated normal browmad angry
    voice "VA/GARFUNKEL/CH0/DES6.mp3"
    de "... That is quite enough!"

    show faceless_knight as knight_a behind therionchild:
        crop (101, 0, 1476, 3495)
        zoom 0.53
        xanchor 0.5 yanchor 1.0
        ypos 1893
        xzoom 1.0
        xpos 1.3
        parallel:
            linear 2.2 xpos 0.07
        parallel:
            block:
                ease 0.25 yoffset -12
                ease 0.25 yoffset 0
                repeat 4
        pause 0.4
        ease 0.2 xzoom -1.0
        parallel:
            linear 2.4 xpos 1.22
        parallel:
            block:
                ease 0.3 yoffset -12
                ease 0.3 yoffset 0
                repeat 4

    show faceless_knight as knight_b behind therionchild:
        crop (101, 0, 1476, 3495)
        zoom 0.53
        xanchor 0.5 yanchor 1.0
        ypos 1893
        xzoom 1.0
        xpos 1.3
        parallel:
            linear 1.7 xpos 0.36
        parallel:
            block:
                ease 0.25 yoffset -12
                ease 0.25 yoffset 0
                repeat 3
        pause 0.9
        ease 0.2 xzoom -1.0
        parallel:
            linear 2.4 xpos 1.51
        parallel:
            block:
                ease 0.3 yoffset -12
                ease 0.3 yoffset 0
                repeat 4

    show therionchild halfempty worried:
        pause 2.6
        ease 0.12 xzoom 1.0 yoffset -32
        linear 2.4 xpos 1.35

    show evachild agitated browsad oh

    show desmond normal browsad stern

    en "He sent the boy away that same week, to the orphanage at the far edge of the grounds. He would not yield, no matter how she begged or refused her food." (multiple=2)
    tn "So that was that. Garbage goes in the bin. I knew how the world worked by then. I was nine, not bloody stupid." (multiple=2)

    hide knight_a
    hide knight_b
    hide therionchild

    show evachild browmad angry:
        ease 0.15 xoffset -70 yoffset -34
        ease 0.06 xoffset -62
        ease 0.06 xoffset -76
        ease 0.06 xoffset -64
        ease 0.25 xoffset -70 yoffset -20
        block:
            ease 1.5 yoffset -40
            ease 1.5 yoffset -14
            repeat
    voice "VA/RAKUMAROO/Chapter 00/Ch0_Eva43.mp3"
    e "He is MINE, Papa! I saved him! You cannot simply take him away!"

    show desmond agitated browmad angry:
        ease 0.15 yoffset -14
        ease 0.2 yoffset 0
    voice "VA/GARFUNKEL/CH0/DES7.mp3"
    de "He is not an OBJECT, Eva! He is a child! And he needs to be far away from—"

    show evachild calm normal browneutral frown:
        ease 0.8 yoffset 0
    voice "VA/RAKUMAROO/Chapter 00/Ch0_Eva44.mp3"
    e "From me?"

    show desmond calm closed browsad neutral
    voice "VA/GARFUNKEL/CH0/DES8.mp3"
    de "... Go to your room, Eva."


    stop music fadeout 1.0
    camera at grade_shift(grade_bright, grade_day0, 2.5)
    show evachild halfempty browneutral frown:
        ease 0.4 xzoom -1.0
        pause 0.6
        linear 6.0 xpos -0.4

    voice "VA/RAKUMAROO/Chapter 00/Ch0_Eva45.mp3"
    e "..."

    voice "VA/RAKUMAROO/Chapter 00/Ch0_Eva46.mp3"
    e "Yes, Papa."

    scene black
    with dissolve

    en "She went and tried not to weep. Crying was for weak girls who would never become a Saintess." (multiple=2)
    tn "They dragged me out by the arms. I let 'em, because fighting would've made it worse for her." (multiple=2)


    play music "hinokageri_orchestra.mp3"

    camera
    $ renpy.show_layer_at([], layer="master")

    show layer master at layer_grade(0.45, -0.18)

    show bg arena_day as bg_left at panel_left_in
    show bg temple_corridor_day as bg_right at panel_right_in
    show split_line at split_divider
    pause 1.2

    show therionchild browsad empty worried notears at therion_face_l
    show evachild calm browsad half frown noblush at eva_face_r
    with dissolve

    en "She wanted him back from that day forward. There had to be a way." (multiple=2)
    tn "They took my light away and shoved me in a room full of other brats with dead eyes, just like mine." (multiple=2)

    show therionchild browmad halfempty frown notears
    show evachild calm browsad normal frown noblush

    en "She compiled lists of things she would do when she had him again. Teach him to read properly, ensure no one could ever steal him a second time." (multiple=2)
    tn "I counted the days until I was old enough to get the hell out of that place." (multiple=2)

    show therionchild browmad empty angry notears
    show evachild calm browmad half frown noblush

    en "She practiced her gift on insects first, then birds that hit the chapel glass, then a stray hound with dull, starving eyes." (multiple=2)
    tn "I practiced beating the crap out of other boys so I wouldn't end up stabbed like my dad." (multiple=2)

    show therionchild browmad halfempty angry notears
    show evachild calm browsad half frown noblush

    en "The hound never barked again. It sat at her feet for the rest of its life, perfectly calm and happy, and she loved it dearly." (multiple=2)
    tn "Heard a rumor she had a dog. Followed her like a shadow, wouldn't move unless she said so. I got replaced by a mutt. I wanted it gone. Soon. Very soon." (multiple=2)

    show therionchild browneutral empty frown notears
    show evachild calm browmad normal frown noblush

    en "She told her father the hound was proof her methods were improving. He looked only horrified and said nothing at all." (multiple=2)
    tn "The old man wanted me nowhere near her. Probably told himself it was kindness, keeping me where I couldn't do damage." (multiple=2)

    camera
    show layer master at layer_grade_shift(0.45, -0.18, 0.75, -0.08, 1.5)
    show therionchild at therion_kid_morph_out
    show evachild at eva_kid_morph_out
    show therion body1 browneutral half frown noblush at therion_adult_l
    show eva calm browneutral normal_happy smile noblush at eva_adult_r
    pause 1.6
    hide therionchild
    hide evachild

    en "Years passed rather quickly." (multiple=2)
    tn "Years passed, and then the mutt died." (multiple=2)

    show therion body1 browmad open gritangry noblush
    show eva calm browhappy normal_happy smile noblush

    en "She grew taller. She grew stronger. And most importantly, her certainty became absolute." (multiple=2)
    tn "Got taller. Meaner. Pretty handy with my fists, too." (multiple=2)

    show therion body1 browskeptical half frown noblush
    show eva agitated browhappy normal_happy laugh blush

    en "By twelve, she had purified her first person. A thief in chains. He wept afterward and thanked her, and she glowed for a week." (multiple=2)
    tn "By twelve, I put three boys in the yard with broken arms. Wasn't even trying that hard, to be honest." (multiple=2)

    show therion body1 browmad half gritannoyed noblush
    show eva calm browneutral normal_happy smile noblush

    en "Her papa no longer corrected her for saying practice. She took the silence as agreement." (multiple=2)
    tn "By then nobody argued with me either. Made things easier to break." (multiple=2)

    show therion body1 browneutral open frown noblush
    show eva calm browhappy normal_happy smile blush

    en "Papa mentioned the sick house first, as though the notion had only just occurred to him. She thought it rather touching, that he trusted her enough to suggest it." (multiple=2)
    tn "Round then's when they started handing me real jobs, not just yard scraps." (multiple=2)

    show therion body1 browmad open gritangry noblush
    show eva calm browhappy closed_happy laugh noblush

    en "By fourteen, she had done an entire ward of the sick house, every patient smiling and serene, none asking to leave, which the healers called a magnificent success." (multiple=2)
    tn "By fourteen, they stopped sending kids my age to the yard. Started sending men. I broke those bastards too." (multiple=2)

    camera
    show layer master at layer_grade_shift(0.75, -0.08, 1.0, 0.0)
    show therion body1 browneutral luv frown blush
    show eva agitated browhappy normal_happy laugh blush

    en "By fifteen, she was the youngest Saintess in a hundred years. The cathedral filled with light. Her father stood beside her with shaking hands, and she thought he was proud." (multiple=2)
    tn "By fifteen, I heard there's a new Saintess. Youngest in a century. My light is officially a Saintess." (multiple=2)

    show therion body1 browsad luvhalf frown blush
    show eva calm browneutral yandere_happy smile noblush

    en "She kept track of him through the years. Where he was. What he had become. She asked after him once a year, as though it cost her nothing." (multiple=2)
    tn "I still have that bit of blue ribbon from the first week. Wore it down to a thread. Held it at night when it's dark. Pathetic, I know." (multiple=2)

    show therion body1 browsad half gritannoyed noblush
    show eva calm browneutral normal_happy smile noblush

    en "The reports came back the same each time: troubled, violent, solitary. She read each one twice and folded it carefully into a box beneath her bed." (multiple=2)
    tn "Never got a single letter. Figured she forgot. Why would she remember trash like me?" (multiple=2)

    show therion body1 browsad closed frown noblush
    show eva calm browneutral closed_happy smile noblush

    en "She offered a prayer for him every night, whispered at the end of her Saintess's prayer where nobody else could hear." (multiple=2)
    tn "Said her name instead of praying. Both are the same damned thing, far as I was concerned." (multiple=2)

    camera
    show layer master at layer_grade_shift(1.0, 0.0, 1.35, 0.06)
    show therion body1 browneutral open frown noblush
    show eva calm browneutral normal_happy smile noblush

    en "And then came the day of the trial." (multiple=2)
    tn "Then some clerk mentioned it offhand. Protector needed. Trial by combat. Winner gets the post—Saintess's knight." (multiple=2)

    show therion body1 browmad shook gritangry noblush
    show eva agitated browhappy normal_happy smile blush

    en "But of course, she found his name at the candidates list and assigned weaker enemies to him without anyone knowing." (multiple=2)
    tn "Her knight. HERS. I signed up before the clerk finished his sentence." (multiple=2)

    show therion body1 browskeptical open gritannoyed noblush
    show eva calm browneutral normal_happy smile noblush

    en "She sat in her box above the sand and waited, patient as a fairytale, for her knight to appear." (multiple=2)
    tn "Twenty men in the yard that morning. Bigger than me, most of 'em. Hah, didn't matter. None of 'em had my reasons." (multiple=2)

    show therion body1 browsad half frown noblush
    show eva calm browsad normal_happy smile blush

    en "I don't think he'd remember the Saintess was me, but I sure do hope so." (multiple=2)
    tn "Don't think she'd remember a street rat, but maybe I should pretend as if I'm a proper knight." (multiple=2)

    show therion body1 browmad open angry noblush
    show eva calm browneutral normal_happy smile noblush

    en "She thought she was ready for whoever it would be." (multiple=2)
    tn "I'd been ready since I was nine." (multiple=2)

    show bg temple_corridor_day as bg_right at corridor_under behind bg_left
    show bg arena_day as bg_left at arena_takeover
    show split_line at split_divider_out
    show therion at therion_to_kneel
    show eva at eva_to_box
    pause 2.0


    hide bg_right
    hide split_line
    show bg arena_day_lit_crowd as bg_left at arena_final
    show therion body1 browneutral half frown noblush hair2
    show eva at eva_in_box
    $ renpy.transition(dissolve)
    $ renpy.pause(0.5, hard=True)

    show eva normal_happy browsad neutral

    voice "VA/RAKUMAROO/Eva10.mp3"
    e "... Are you quite all right, Sir Therion?"

    show therion body1 browneutral smile hair2

    voice "VA/JASON/Therion2.mp3"
    t "Never better. Never better, My Lady."

    en "She was not ready." (multiple=2)
    tn "Ready as I'll ever be, I told myself." (multiple=2)

    show layer master at layer_grade_shift(1.35, 0.06, 1.0, 0.0, 1.0)
    $ renpy.pause(1.0, hard=True)

    $ renpy.show_layer_at([], layer="master")
    camera

    if monstrous_points > deluded_points:
        jump therion_ruins
    else:
        jump therion_glory
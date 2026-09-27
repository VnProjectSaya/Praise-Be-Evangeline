label therion_glory:

    scene black
    with fade

    play music "shizumiyukutsuki.mp3"

    $ current_frame = "twisted"

    pause 1.0

    scene bg study_night_lit:
        subpixel True
        anchor (0.5, 0.5)
        pos (960, 540)
        zoom 0.7

    show layer master:
        subpixel True
        anchor (0.5, 0.5)
        pos (960, 500)
        zoom 1.7
        xoffset 0
        yoffset 0

    show eva browneutral yandere_sad neutral zorder 1:
        matrixcolor ColorizeMatrix("#152238", "#f4dcb3")
        subpixel True
        xzoom 1
        zoom 0.227
        xanchor 0.5
        yanchor 1.0
        xpos 0.67
        ypos 1.0
        yoffset 5
        alpha 0.0
        ease 0.8 alpha 1.0
        block:
            ease 2.0 yoffset -10
            ease 2.0 yoffset 0
            repeat

    voice "VA/RAKUMAROO/GLORY/E1.mp3"
    e "Therion."

    show therion browneutral half neutral zorder 2:
        matrixcolor ColorizeMatrix("#152238", "#f4dcb3")
        subpixel True
        transform_anchor True
        xzoom -1
        zoom 0.235
        xanchor 0.5
        yanchor 1.0
        xpos -0.1
        ypos 1.0
        yoffset 70
        parallel:
            easein 1.6 xpos 0.34
        parallel:
            ease 0.2 yoffset 62
            ease 0.2 yoffset 70
            repeat 4
        block:
            ease 2.5 yoffset 76
            ease 2.5 yoffset 70
            repeat

    voice "VA/JASON/GLORY/G1.mp3"
    t "Yeah, Saintess. Standing right here."

    tn "Saintess called. When I get in, the archbishop is running away through the study door like a coward."

    voice "VA/RAKUMAROO/GLORY/E2.mp3"
    e "The Archbishop struck the Bishop. Vidius is breathing poorly, and my father cannot be linked to this room when the servants arrive."

    show therion browskeptical open neutral

    tn "Huh. She's never asked me to clean up a mess directly before. Usually I just take the hint and gut the problem."

    voice "VA/RAKUMAROO/GLORY/E3.mp3"
    e "Please. I require you to attend to it. For the bishop's comfort, not mine."

    show therion browneutral open neutral

    voice "VA/JASON/GLORY/G2.mp3"
    t "I'll handle it."

    show therion browneutral luvhalf smile blush

    tn "Ah. The old man did the damage, not my girl. My sacred light doesn't get her hands dirty. 'Course she fucking doesn't."

    show therion browneutral open neutral noblush

    voice "VA/JASON/GLORY/G3.mp3"
    t "How do you want it to look?"

    voice "VA/RAKUMAROO/GLORY/E4.mp3"
    e "An accident. The east stairwell is steep, and no one will doubt a tumble."

    voice "VA/JASON/GLORY/G4.mp3"
    t "Got it."

    voice "VA/RAKUMAROO/GLORY/E5.mp3"
    e "Thank you, Therion. I should like to see it done myself, if you don't mind. I shall not be in your way."

    # Therion walks to the body and bends down
    show therion browneutral half neutral:
        ease 1.0 xpos 0.40
        ease 0.6 rotate 9 yoffset 150

    tn "Alright. Let's have a look at you, Bishop."

    # the haul: two heaves up from below the screen
    show vidius browsad eyeclosed frown shadow zorder 3:
        matrixcolor ColorizeMatrix("#152238", "#f4dcb3")
        subpixel True
        transform_anchor True
        zoom 0.2
        anchor (0.5, 0.26)
        xpos 0.5
        ypos 1500
        rotate -14
        easein 0.45 ypos 900 rotate -9
        pause 0.25
        easein 0.5 ypos 640 rotate -6
        block:
            ease 1.4 rotate -3
            ease 1.4 rotate -7
            repeat

    show therion browmad open gritannoyed:
        easein 0.45 rotate 4 yoffset 110
        pause 0.25
        easein 0.5 rotate 0 yoffset 70
        block:
            ease 2.5 yoffset 76
            ease 2.5 yoffset 70
            repeat

    tn "Tch, heavy bastard. Heavier than Caelor by a mile. All those fancy church feasts adding up, I reckon."

    voice "VA/TORA/Vidius/Glory Ending/Vidius_Glory_1.mp3"
    vidius "...ngh..."

    show therion browneutral shook neutral

    tn "Oh. That ain't just gas escaping."

    show vidius browsad eyenormal frown

    tn "The bastard's still alive."

    # lifts him higher, feet off the floor
    show therion browneutral half grin
    show vidius:
        easein 0.35 ypos 500 rotate -2
        block:
            ease 1.3 rotate 3
            ease 1.3 rotate -3
            repeat

    voice "VA/JASON/GLORY/G5.mp3"
    t "Hi, Your Grace."

    voice "VA/TORA/Vidius/Glory Ending/Vidius_Glory_2.mp3"
    vidius "Put me... down..."

    # a little swing, like winding up a toss
    show therion browneutral half smug
    show vidius:
        easeout 0.25 xoffset -30 rotate 8
        easein 0.35 xoffset 0 rotate -2
        block:
            ease 1.3 rotate 3
            ease 1.3 rotate -3
            repeat

    voice "VA/JASON/GLORY/G6.mp3"
    t "Bye, Your Grace."

    show vidius agitated browmad eyeshocked angry noshadow:
        block:
            linear 0.06 rotate -12 xoffset -7
            linear 0.06 rotate 2 xoffset 5
            linear 0.07 rotate -9 xoffset -4
            linear 0.07 rotate -3 xoffset 3
            repeat 4
        ease 0.2 rotate -4 xoffset 0
        block:
            linear 0.08 xoffset -2
            linear 0.08 xoffset 2
            repeat

    voice "VA/TORA/Vidius/Glory Ending/Vidius_Glory_3.mp3"
    vidius "NO! I said—put me DOWN—"

    # the slip
    show therion browneutral shook gritannoyed
    show vidius:
        easein 0.12 ypos 610 rotate -10
        easeout 0.25 ypos 540 rotate -4
        block:
            linear 0.08 xoffset -2
            linear 0.08 xoffset 2
            repeat

    tn "Whoops, nearly lost my grip right there. Should've held higher, the blood's making the robes slippery as grease."

    # dropped on his feet, shoves Therion back
    show vidius:
        easein 0.2 ypos 539 rotate 0 xoffset 0
        pause 0.1
        easeout 0.12 xoffset -28
        easein 0.25 xoffset 0
        block:
            linear 0.1 xoffset -2
            linear 0.1 xoffset 2
            repeat
    show therion browmad open annoyed:
        pause 0.3
        easeout 0.15 xoffset -20 rotate -4
        easein 0.4 xpos 0.35 xoffset 0 rotate 0

    voice "VA/TORA/Vidius/Glory Ending/Vidius_Glory_4.mp3"
    vidius "You! You're her knight, you—"

    show therion browneutral half smug

    voice "VA/JASON/GLORY/G7.mp3"
    t "Sure am."

    show vidius:
        easein 0.2 xoffset -18
        block:
            linear 0.1 xoffset -20
            linear 0.1 xoffset -16
            repeat

    voice "VA/TORA/Vidius/Glory Ending/Vidius_Glory_5.mp3"
    vidius "Listen to me! She is a false saintess!"

    show therion browmad open frown

    tn "The fuck did Vidius just say about her?"

    voice "VA/TORA/Vidius/Glory Ending/Vidius_Glory_6.mp3"
    vidius "You have to help me tell everyone—"

    show therion browskeptical half grin

    voice "VA/JASON/GLORY/G8.mp3"
    t "Tell it to who, mate? Ain't nobody in this dark hallway but you and me."

    # Therion reaches, Vidius backs off shaking
    show therion:
        ease 0.5 xpos 0.41
    show vidius browmad eyeshocked shockedm:
        ease 0.4 xoffset 20
        block:
            linear 0.05 xoffset 17
            linear 0.05 xoffset 23
            repeat

    voice "VA/TORA/Vidius/Glory Ending/Vidius_Glory_7.mp3"
    vidius "Get your hands off me, get—"

    # the scratch
    show therion browmad shook gritangry:
        easeout 0.08 xoffset -18 rotate -3
        easein 0.3 xoffset 0 rotate 0
    show vidius:
        block:
            linear 0.05 rotate -6 xoffset 14
            linear 0.05 rotate 5 xoffset 26
            repeat 5
        ease 0.2 rotate 0 xoffset 20

    tn "Vidius is really fighting now. Kicking. Biting, actually—the mad bastard just scratched my fucking wrist!"

    show therion browneutral creepy neutral

    tn "I could crush Vidius's neck right here. One good squeeze and bam, done."

    show eva browmad yandere_sad frown

    voice "VA/RAKUMAROO/GLORY/E6.mp3"
    e "Therion, Vidius is still—"

    # Vidius flips to face her
    show vidius browmad eyeshocked angry:
        xzoom -1
        easein 0.1 xoffset 34
        easeout 0.1 xoffset 26

    voice "VA/TORA/Vidius/Glory Ending/Vidius_Glory_8.mp3"
    vidius "YOU!"

    # lunge and shove
    show vidius:
        easein 0.35 xpos 0.6 xoffset 0
        easeout 0.1 xoffset 14
        easein 0.2 xoffset 0
        block:
            linear 0.08 xoffset -2
            linear 0.08 xoffset 2
            repeat
    show eva agitated browsad yandere_sad shocked:
        transform_anchor True
        pause 0.35
        easeout 0.15 xpos 0.72 rotate 6
        easein 0.4 rotate 0
    show therion browmad shook gritangry:
        easeout 0.2 xoffset 18
        easein 0.3 xoffset 0
    show layer master:
        subpixel True
        anchor (0.5, 0.5)
        pos (960, 500)
        zoom 1.7
        pause 0.35
        linear 0.04 xoffset 16 yoffset -4
        linear 0.04 xoffset -12 yoffset 3
        linear 0.05 xoffset 6 yoffset -2
        linear 0.06 xoffset 0 yoffset 0
    tn "Fuck! The damn bishop twisted clean out of my arms! Should've pinned the shoulders."

    show vidius:
        ease 1.6 xpos 0.63
        block:
            linear 0.08 xoffset -2
            linear 0.08 xoffset 2
            repeat

    tn "Bastard is reaching for my light."

    show therion browmad open gritangry zorder 4:
        easein 0.3 xpos 0.56

    voice "VA/JASON/GLORY/G9.mp3"
    t "DON'T YOU TOUCH HER!"

    # slam into the left wall
    show vidius:
        xzoom -1
        easein 0.18 xpos 0.26 rotate -6
        easeout 0.2 rotate 0
        block:
            linear 0.06 xoffset -3 rotate -1
            linear 0.06 xoffset 3 rotate 0
            repeat
    show therion:
        xzoom 1
        easein 0.2 xpos 0.44
    show layer master:
        subpixel True
        anchor (0.5, 0.5)
        pos (960, 500)
        zoom 1.7
        pause 0.15
        linear 0.04 xoffset 22 yoffset -6
        linear 0.04 xoffset -18 yoffset 5
        linear 0.04 xoffset 12 yoffset -3
        linear 0.05 xoffset -6 yoffset 2
        linear 0.06 xoffset 0 yoffset 0

    tn "Slammed the bishop back against the stone wall. Still moving, though. Hands grabbing at the air where my Saintess is standing."
    # Therion shaking him
    show vidius:
        # a few hard jerks against the grip
        easein 0.08 xoffset -5 rotate -1.5
        easeout 0.12 xoffset 3 rotate 1
        easein 0.06 xoffset -4 rotate -1
        easeout 0.15 xoffset 2 rotate 0.5
        easein 0.07 xoffset -3 rotate -1
        ease 0.2 xoffset 0 rotate 0
        # then a low, uneven tremble
        block:
            linear 0.05 xoffset -1.5
            linear 0.07 xoffset 1
            linear 0.04 xoffset -1
            linear 0.09 xoffset 1.5
            linear 0.06 xoffset 0
            pause 0.1
            repeat
    voice "VA/TORA/Vidius/Glory Ending/Vidius_Glory_9.mp3"
    vidius "You ARE A MONSTER!"

    voice "VA/TORA/Vidius/Glory Ending/Vidius_Glory_10.mp3"
    vidius "Everyone must know who you really are!"

    show therion browmad creepy 

    tn "I'll break every finger the damn bishop has got. Start with the left, work through, won't be reaching for my girl ever again."

    # Eva settles
    show eva calm browevil closed_sad frown  with Dissolve(1.0)
    show eva:
        ease 1.2 xpos 0.69

    voice "VA/RAKUMAROO/GLORY/E7.mp3"
    e "... There is no choice. You are too far gone."

    voice "VA/RAKUMAROO/GLORY/E8.mp3"
    e "I will save you from the darkness inside yourself, Vidius."

    # ---- the light, centered on Eva's hands ----
    show expression Solid("#ffd76a", xysize=(700, 700)) as gold_halo zorder 8:
        subpixel True
        anchor (0.5, 0.5)
        pos (1325, 670)
        rotate 45
        blend "add"
        blur 160
        alpha 0.0
        zoom 0.3
        ease 1.5 alpha 0.45 zoom 1.0
        block:
            ease 2.0 zoom 1.08 alpha 0.5
            ease 2.0 zoom 1.0 alpha 0.42
            repeat

    show expression Solid("#fff4cc", xysize=(180, 180)) as gold_core zorder 9:
        subpixel True
        anchor (0.5, 0.5)
        pos (1325, 670)
        rotate 45
        blend "add"
        blur 40
        alpha 0.0
        zoom 0.2
        ease 1.0 alpha 0.9 zoom 1.0
        block:
            ease 0.9 zoom 1.12
            ease 0.9 zoom 0.95
            repeat

    show gold_rays as gold_rays zorder 7:
        subpixel True
        anchor (0.5, 0.5)
        pos (1325, 670)
        blend "add"
        blur 10
        alpha 0.0
        zoom 0.4
        parallel:
            ease 2.0 alpha 0.3 zoom 1.0
        parallel:
            linear 60 rotate 360
            repeat

    show gold_rays_fine as gold_rays_fine zorder 7:
        subpixel True
        anchor (0.5, 0.5)
        pos (1325, 670)
        blend "add"
        blur 4
        alpha 0.0
        zoom 0.4
        parallel:
            ease 2.0 alpha 0.25 zoom 1.0
        parallel:
            rotate 360
            linear 45 rotate 0
            repeat

    show expression SnowBlossom(gold_mote(), count=40, border=50, xspeed=(-15, 15), yspeed=(-90, -35), fast=True) as gold_motes zorder 10:
        alpha 0.0
        ease 1.5 alpha 0.8

    show expression Solid("#ffcf5a") as gold_wash zorder 11:
        blend "add"
        alpha 0.0
        ease 2.0 alpha 0.12

    # sprites turn gold
    show vidius:
        parallel:
            ease 1.5 matrixcolor ColorizeMatrix("#5c3d12", "#fff3cf")
        parallel:
            block:
                linear 0.05 xoffset -1.5
                linear 0.07 xoffset 1
                linear 0.04 xoffset -1
                linear 0.09 xoffset 1.5
                linear 0.06 xoffset 0
                pause 0.1
                repeat
    show therion browneutral shook neutral:
        ease 1.5 matrixcolor ColorizeMatrix("#5c3d12", "#fff3cf")
    show eva:
        parallel:
            ease 1.5 matrixcolor ColorizeMatrix("#5c3d12", "#fff3cf")
        parallel:
            ease 1.5 yoffset -15
            block:
                ease 2.0 yoffset -20
                ease 2.0 yoffset -12
                repeat

    tn "There's the light."

    tn "Holy fucking shit, the gold..."

    show therion browneutral luvhalf smile

    tn "Every bad feeling in my head just... dies. Again."

    # ---- light intensifies ----
    show gold_halo:
        subpixel True
        anchor (0.5, 0.5)
        pos (1325, 670)
        blend "add"
        blur 160
        ease 1.2 alpha 0.7 zoom 1.5
        block:
            ease 1.2 zoom 1.6 alpha 0.75
            ease 1.2 zoom 1.5 alpha 0.65
            repeat
    show gold_wash:
        blend "add"
        ease 1.2 alpha 0.25
    show gold_rays:
        subpixel True
        anchor (0.5, 0.5)
        pos (1325, 670)
        blend "add"
        blur 10
        parallel:
            ease 1.2 alpha 0.5 zoom 1.2
        parallel:
            linear 30 rotate 360
            repeat

    show vidius agitated browmad eyeshocked shockedm:
        parallel:
            ease 1.2 matrixcolor ColorizeMatrix("#8a6424", "#ffffff")
        parallel:
            block:
                easein 0.07 xoffset -6 rotate -2
                easeout 0.1 xoffset 4 rotate 1.5
                easein 0.06 xoffset -3 rotate -1
                easeout 0.12 xoffset 5 rotate 1
                repeat
    show therion:
        ease 1.2 matrixcolor ColorizeMatrix("#8a6424", "#ffffff")
    show eva:
        parallel:
            ease 1.2 matrixcolor ColorizeMatrix("#8a6424", "#ffffff")
        parallel:
            block:
                ease 2.0 yoffset -20
                ease 2.0 yoffset -12
                repeat

    voice "VA/TORA/Vidius/Glory Ending/Vidius_Glory_11.mp3"
    vidius "Wh— what are you doing, get it OFF, get it OFF ME—"

    show therion browneutral half grin

    tn "Vidius stopped clawing at my chest. Fighting the magic now instead and the bastard is losing."

    # ---- Vidius goes still ----
    show vidius calm browneutral eyeshocked smile:
        ease 0.6 xoffset 0 rotate 0

    voice "VA/TORA/Vidius/Glory Ending/Vidius_Glory_12.mp3"
    vidius "I can't— What was I—"

    voice "VA/TORA/Vidius/Glory Ending/Vidius_Glory_13.mp3"
    vidius "...Saintess..."

    show eva browhappy normal_happy smile

    voice "VA/RAKUMAROO/GLORY/E9.mp3"
    e "There. Isn't that so much better?"

    voice "VA/TORA/Vidius/Glory Ending/Vidius_Glory_14.mp3"
    vidius "...better..."

    show therion browneutral half smile

    tn "It's done. The damn bishop ain't no threat anymore."

    show therion browneutral luvhalf smile

    tn "She's still got her hand out. Fingers glowing at the tips."

    # ---- zoom in on Therion, eyes closed, bathed in light ----
    show therion browsad closed smile blush
    show layer master:
        subpixel True
        anchor (0.5, 0.5)
        pos (960, 500)
        zoom 1.7
        ease 2.5 pos (1259, 612) zoom 2.6

    tn "God, her hands are beautiful."

    tn "I want to hold one so badly my head hurts."

    show therion browmad closed frown

    tn "... Stop thinking about it, you haven't earned it yet, damn Therion."

    show therion browsad closed smile

    tn "But someday."

    tn "I'll be good enough by then."


    # ---- light goes out ----
    show gold_core:
        ease 1.2 alpha 0.0 zoom 0.2
    show gold_halo:
        ease 1.8 alpha 0.0 zoom 0.8
    show gold_rays:
        ease 1.5 alpha 0.0
    show gold_rays_fine:
        ease 1.5 alpha 0.0
    show gold_motes:
        ease 2.0 alpha 0.0
    show gold_wash:
        ease 2.0 alpha 0.0
    show vidius:
        ease 2.0 matrixcolor ColorizeMatrix("#152238", "#f4dcb3")
    show therion:
        ease 2.0 matrixcolor ColorizeMatrix("#152238", "#f4dcb3")
    show eva:
        parallel:
            ease 2.0 matrixcolor ColorizeMatrix("#152238", "#f4dcb3")
        parallel:
            ease 2.0 yoffset 5
            block:
                ease 2.0 yoffset -10
                ease 2.0 yoffset 0
                repeat

    pause 2.0

    hide gold_core
    hide gold_halo
    hide gold_rays
    hide gold_rays_fine
    hide gold_motes
    hide gold_wash

    # eyes open, then back out to all three
    show therion browneutral luvhalf smile blush
    pause 0.8

    show layer master:
        subpixel True
        anchor (0.5, 0.5)
        pos (1259, 612)
        zoom 2.6
        ease 1.5 pos (960, 500) zoom 1.7

    show therion:
        xzoom -1
    with dissolve

    tn "There she is."

    tn "There's my light."

    show eva browneutral normal_happy smile

    voice "VA/RAKUMAROO/GLORY/E10.mp3"
    e "Please take care of the rest, Therion."

    show therion browneutral open smile noblush

    voice "VA/JASON/GLORY/G10.mp3"
    t "You got it."

    scene black
    with fade

    tn "...There. All done."

    tn "Ha."

    tn "I took care of everyone who could've given her flowers."

    tn "Every single one of 'em."

    scene bg temple_corridor_day
    show layer master:
        subpixel True
        anchor (0.5, 0.5)
        pos (960, 540)
        zoom 1.0
        xoffset 0
        yoffset 0
    with fade

    # Therion at mid-left, listening in
    show therion browneutral half neutral behind petra, ansel:
        xzoom -1
        subpixel True
        transform_anchor True
        zoom 0.22
        xanchor 0.5 yanchor 1.0
        xpos 0.18 ypos 1.0 yoffset 40
        ease 0.34 xpos 0.25
        block:
            ease 1.8 yoffset 20
            ease 1.8 yoffset 40
            repeat

    # Petra facing Ansel, back to Therion
    show petra idle browmad shocked shockedm:
        xzoom -1
        subpixel True
        zoom 0.25
        xanchor 0.5 yanchor 1.0
        xpos 0.63 ypos 1.0 yoffset 40
        block:
            ease 2.1 yoffset 18
            ease 2.1 yoffset 40
            repeat

    # Ansel facing Petra
    show ansel idle browsad frown shocked:
        xzoom 1
        subpixel True
        zoom 0.25
        xanchor 0.5 yanchor 1.0
        xpos 0.78 ypos 1.0 yoffset 40
        block:
            ease 2.4 yoffset 22
            ease 2.4 yoffset 40
            repeat
    with dissolve

    $ renpy.pause(0.5, hard=True)

    # Petra leans in with a little excited hop
    show petra panic browneutral shocked surprised:
        easeout 0.12 yoffset 10
        easein 0.15 yoffset 30
        ease 0.3 xoffset 18
        block:
            ease 1.2 yoffset 18
            ease 1.2 yoffset 34
            repeat

    petra "Did you hear? Bishop Vidius, reaching for the Saintess's own gift to take it for the bishop! The light doesn't share kindly, that's what the infirmary sisters are saying."

    # Ansel leans in close, keeping it quiet
    show ansel browsad normal frown:
        ease 0.5 xoffset -20
        block:
            ease 2.4 yoffset 22
            ease 2.4 yoffset 40
            repeat
    show petra idle browsad shocked shockedm

    ansel "Doesn't know the bishop's own name now. Small mercy 'em still breathing at all."

    # push in on Therion
    show layer master:
        subpixel True
        anchor (0.5, 0.5)
        pos (960, 540)
        zoom 1.0
        ease 2.0 pos (1680, 504) zoom 1.8
    show therion browneutral half smug


    tn "That's the rumor by sunrise. Nobody asked me a fucking thing. She'd already calculated how this play runs."

    show therion browneutral half grin

    tn "Good. Saves me the damn effort."

    show therion browskeptical half grin

    tn "Vidius is smiling down in the infirmary bed with a stupid grin and sits there all day staring at blank stone."

    show therion browmad half smug

    tn "Serves 'em right."

    scene bg eva_bedroom_day:
        subpixel True
        anchor (0.5, 0.5)
        zoom 1.5
        xpos 0.5
        ypos 0.5
    show layer master:
        subpixel True
        anchor (0.5, 0.5)
        pos (960, 540)
        zoom 1.0
    show eva browneutral normal_sad neutral:
        subpixel True
        xzoom -1
        zoom 0.55
        xanchor 0.5
        yanchor 1.0
        xpos 0.30
        yalign 1.0
        yoffset 750
        block:
            ease 2.0 yoffset 734
            ease 2.0 yoffset 750
            repeat
    with fade

    # Therion walks in from the right
    show therion browneutral half neutral behind eva:
        subpixel True
        transform_anchor True
        xzoom 1
        zoom 0.58
        xanchor 0.5
        yanchor 1.0
        xpos 1.2
        yalign 1.0
        yoffset 1000
        parallel:
            easein 1.4 xpos 0.70
        parallel:
            ease 0.2 yoffset 985
            ease 0.2 yoffset 1000
            repeat 3
        block:
            ease 2.5 yoffset 990
            ease 2.5 yoffset 1000
            repeat

    show eva browhappy normal_happy smile

    voice "VA/RAKUMAROO/GLORY/E11.mp3"
    e "Therion. There you are."

    show therion browneutral open smile

    voice "VA/JASON/GLORY/G11.mp3"
    t "Right here, Saintess. Ain't going anywhere."

    show eva browneutral normal_sad neutral

    voice "VA/RAKUMAROO/GLORY/E12.mp3"
    e "Is it done?"

    show therion browneutral half smug

    voice "VA/JASON/GLORY/G12.mp3"
    t "Everyone believes the lie. Damn bishop can't hurt you anymore."

    show eva browhappy normal_happy smile

    voice "VA/RAKUMAROO/GLORY/E13.mp3"
    e "Wonderful. Come here. Let me look at you."

    # she pulls him in, both closer to center
    show eva:
        ease 0.6 xpos 0.35
        block:
            ease 2.0 yoffset 734
            ease 2.0 yoffset 750
            repeat
    show therion browneutral shook angry blush:
        pause 0.15
        easein 0.35 xpos 0.65 rotate -1.5
        ease 0.5 rotate 0
        block:
            ease 2.5 yoffset 990
            ease 2.5 yoffset 1000
            repeat

    tn "She just grabbed my hands."

    show therion browsad shook neutral blush

    tn "Both of 'em."
    show therion browneutral luv grin blush

    tn "Holy shit. That's new."

    show eva browsad normal_happy frown

    voice "VA/RAKUMAROO/GLORY/E14.mp3"
    e "Oh, you're getting your poor hands dirty!"

    show therion browneutral half smile blush

    voice "VA/JASON/GLORY/G13.mp3"
    t "It's nothing."

    show eva browmad normal_sad frown

    voice "VA/RAKUMAROO/GLORY/E15.mp3"
    e "Nonsense. Without you, Vidius would've spread false rumors about us and I'd be hanged."

    play music "hinokageri.mp3"

    # small lean toward him
    show eva browhappy closed_happy smile blush:
        ease 0.8 xoffset 15
        block:
            ease 2.0 yoffset 734
            ease 2.0 yoffset 750
            repeat

    voice "VA/RAKUMAROO/GLORY/E16.mp3"
    e "Thank you, Therion. You are very sweet."

    show therion browsad luv smile blush

    tn "She said that all soft and velvety-like."

    tn "Nobody's ever said a damn thing like that to me."

    show therion browsad shook smile blush

    voice "VA/JASON/GLORY/G14.mp3"
    t "Uh... I'm... glad you think so."

    show eva browhappy yandere_happy smile noblush

    voice "VA/RAKUMAROO/GLORY/E17.mp3"
    e "Yes, I do~"

    voice "VA/RAKUMAROO/GLORY/E18.mp3"
    e "You're such a good boy, and you are mine~"

    show therion browneutral luv neutral blush

    tn "... Oh."

    scene black 
    with vpunch

    tn "My knees are giving out like some pathetic bastard now and I don't give a fuck."

    tn "She smiles, pulls me toward her, sits on the edge of the mattress and puts my head on her lap."

    scene glory_cg normal at glory_rest
    with Dissolve(1.2)

    voice "VA/RAKUMAROO/GLORY/E19.mp3"
    e "Oh, my Therion~ Whatever would I do without you?"

    voice "VA/JASON/GLORY/G15.mp3"
    t "You won't ever have to find out."

    tn "Her hand's in my hair."

    tn "What is this?"

    tn "Her fucking hand is in my hair."

    tn "She's stroking it. Over and over, and my whole scalp is on fire but I'd willingly burn for it."

    tn "She's mine, and I'm hers. As long as I'm breathing, nobody gets close enough to dim her. Nobody."

    tn "Her fingers just slipped behind my ear and found the ugly burn from the fire."

    tn "She's tracing it, like she's known where it sat this whole goddamn time."

    voice "VA/RAKUMAROO/GLORY/E20.mp3"
    e "I have wanted to touch this for such a long time. From the fire, isn't it?"

    voice "VA/JASON/GLORY/G16.mp3"
    t "... You know about this?"

    voice "VA/RAKUMAROO/GLORY/E21.mp3"
    e "Therion. I have always known."

    scene bg eva_bedroom_day:
        subpixel True
        anchor (0.5, 0.5)
        zoom 1.5
        xpos 0.5
        ypos 0.5
    show layer master:
        subpixel True
        anchor (0.5, 0.5)
        pos (960, 540)
        zoom 1.0
    show eva browneutral normal_sad neutral shadow:
        subpixel True
        xzoom -1
        zoom 0.55
        xanchor 0.5
        yanchor 1.0
        xpos 0.30
        yalign 1.0
        yoffset 750
        block:
            ease 2.0 yoffset 734
            ease 2.0 yoffset 750
            repeat
    # rises facing away, twisting, then whips around to face her
    show therion browsad shook frown blush behind eva:
        subpixel True
        transform_anchor True
        xzoom -1
        zoom 0.58
        xanchor 0.5
        yanchor 1.0
        xpos 0.70
        yalign 1.0
        yoffset 1200
        rotate 10
        pause 0.6
        easein 0.45 yoffset 1000 rotate -3
        ease 0.15 rotate 0
        ease 0.25 xzoom 1.0
        block:
            ease 2.5 yoffset 990
            ease 2.5 yoffset 1000
            repeat
    with fade

    tn "I sit up immediately."

    show therion browmad shook frown noblush

    voice "VA/JASON/GLORY/G17.mp3"
    t "How long have you known?"

    show eva browneutral normal_happy smile

    voice "VA/RAKUMAROO/GLORY/E22.mp3"
    e "Since before you were sent away. Since before you returned with a fabricated village that does not exist on any map."

    show eva browsad closed_sad smile blush

    voice "VA/RAKUMAROO/GLORY/E22B.mp3"
    e "…I remember your name."

    tn "Bloody hell."

    show therion browskeptical half frown

    voice "VA/JASON/GLORY/G18.mp3"
    t "So you know I'm not really from Aezalath."

    # yandere from here on
    show eva browhappy yandere_happy yanderesmug noblush noshadow

    voice "VA/RAKUMAROO/GLORY/E23.mp3"
    e "Yes, I have always known. I only preferred that nobody else did."

    show eva browevil yandere_happy yandereevilsmile

    voice "VA/RAKUMAROO/GLORY/E24.mp3"
    e "And I helped rig the trial for you, so you'd win and become my knight~"

    show therion browmad shook gritannoyed

    voice "VA/JASON/GLORY/G19.mp3"
    t "Every fight... Every man I— you rigged all of it?"

    show eva agitated browsad yandere_sad what

    voice "VA/RAKUMAROO/GLORY/E25.mp3"
    e "Heavens, not the fights themselves. I would not insult you that way!"

    show eva calm browhappy yandere_happy smile

    voice "VA/RAKUMAROO/GLORY/E26.mp3"
    e "You won those on your own merits, every single one."

    show eva browevil yandere_happy yanderesmug

    voice "VA/RAKUMAROO/GLORY/E27.mp3"
    e "I simply made certain you were given the opportunity to."

    show therion browsad half neutral

    voice "VA/JASON/GLORY/G20.mp3"
    t "How long...?"

    # small lean toward him
    show eva browevil yandere_happy yandereevilsmile:
        ease 0.8 xoffset 15
        block:
            ease 2.0 yoffset 734
            ease 2.0 yoffset 750
            repeat

    voice "VA/RAKUMAROO/GLORY/E28.mp3"
    e "Since the day my father sent you away. I decided then that I would have you back the moment I was able to."

    show therion browneutral luv grin blush

    tn "So she planned this. She wants ME."

    # he scoots back, giddy
    show therion browsad luv laugh blush:
        ease 0.15 yoffset 985
        ease 0.15 yoffset 1000
        ease 0.5 xpos 0.76
        block:
            ease 2.5 yoffset 990
            ease 2.5 yoffset 1000
            repeat

    tn "ME."

    show eva browhappy yandere_happy yandereevilsmile

    voice "VA/RAKUMAROO/GLORY/E29.mp3"
    e "Therion, why are you scooting away? Do come back here~"

    scene glory_cg yandere at glory_rest
    with Dissolve(1.0)

    tn "She taps on her lap and I drop back down again."

    show glory_cg at glory_pulse

    tn "I can hear my pulse going crazy."

    voice "VA/RAKUMAROO/GLORY/E30.mp3"
    e "Stay here, by my side, as you should be~"

    tn "Gods."

    show glory_cg at glory_lean

    tn "She's leaning down. Her hair falls around my face, brushing my forehead. My brain's fuzzy like mad."

    voice "VA/JASON/GLORY/G21.mp3"
    t "Evangeline..."

    voice "VA/RAKUMAROO/GLORY/E31.mp3"
    e "Yes, my knight?"

    tn "Her face is right there. Close enough that if I lifted my head two inches our mouths would—"

    tn "Hold that fucking thought, boy."

    scene glory_cg normal at glory_lean
    with Dissolve(1.0)

    voice "VA/JASON/GLORY/G22.mp3"
    t "Saintess, you can't just say shit like that to a man and expect him to—"

    voice "VA/RAKUMAROO/GLORY/E31A.mp3"
    e "I know I cannot. That is rather the cruelty of it."

    voice "VA/RAKUMAROO/GLORY/E31B.mp3"
    e "A Saintess remains pure, Therion."

    voice "VA/RAKUMAROO/GLORY/E31C.mp3"
    e "Until another is found to take the office from me, until I am done making the world an ever-smiling place..."

    voice "VA/RAKUMAROO/GLORY/E31D.mp3"
    e "I cannot be yours, not fully."

    show glory_cg at glory_settle

    tn "So that's where the bloody line is."

    tn "But one day."

    tn "One day there'll be another girl in white carrying that light of hers."

    tn "And on that day I'm gonna hold her and I ain't letting go till I've had my fill."

    tn "Even if it takes a lifetime."

    voice "VA/JASON/GLORY/G23.mp3"
    t "I'll wait."

    voice "VA/RAKUMAROO/GLORY/E32.mp3"
    e "What?"

    voice "VA/JASON/GLORY/G24.mp3"
    t "However long it takes. I'll wait. Done it thirteen years already, what's a few more?"

    voice "VA/RAKUMAROO/GLORY/E33.mp3"
    e "Such an impossible man~"

    voice "VA/JASON/GLORY/G25.mp3"
    t "Probably, yeah."

    voice "VA/RAKUMAROO/GLORY/E34.mp3"
    e "Mm~"

    voice "VA/RAKUMAROO/GLORY/E35.mp3"
    e "You are so beautiful. Has anyone ever told you that?"

    voice "VA/JASON/GLORY/G26.mp3"
    t "Can't say they have, Saintess."

    voice "VA/RAKUMAROO/GLORY/E36.mp3"
    e "Then everyone you have ever met is a fool."

    tn "I'll butcher anyone who tries to pull her away from me."

    tn "Her thumb traces my cheekbone and I want to freeze in this moment, even if we stay in here until one of us dies."

    tn "Is that insane? Probably."

    tn "Don't care."

    voice "VA/RAKUMAROO/GLORY/E37.mp3"
    e "I wish the rules were different."

    voice "VA/JASON/GLORY/G27.mp3"
    t "This is enough."

    voice "VA/RAKUMAROO/GLORY/E38.mp3"
    e "I know it isn't for you."

    voice "VA/JASON/GLORY/G28.mp3"
    t "... Heh, yeah. But I'll take it."

    show glory_cg at glory_close

    tn "She bends lower. Forehead against mine."

    tn "Her breath touches my lips."

    tn "She ain't gonna kiss me. I know the whole holy circus rules."

    tn "But this is more than I've ever had in my miserable life."

    voice "VA/RAKUMAROO/GLORY/E39.mp3"
    e "Someday, Therion."

    tn "Her lips brush mine when she says it. Right there. Almost. Almost..."

    voice "VA/JASON/GLORY/G29.mp3"
    t "Someday."

    show glory_cg at glory_settle

    tn "She pulls back."

    tn "Her hands linger on my cheeks for one second. Two. Three. Four..."

    tn "I'm always fucking counting, huh."

    tn "She lets go, then her fingers slide back into my hair."

    tn "Then I open my stupid mouth."


    voice "VA/JASON/GLORY/G30.mp3"
    t "Saintess, I think something's wrong with my face."

    voice "VA/RAKUMAROO/GLORY/E40.mp3"
    e "What do you mean?"

    show glory_cg smile at glory_settle

    voice "VA/JASON/GLORY/G31.mp3"
    t "It's doing the thing. On its own. Don't have to force it."

    voice "VA/RAKUMAROO/GLORY/E41.mp3"
    e "Oh. Oh, I see."

    voice "VA/RAKUMAROO/GLORY/E42.mp3"
    e "That is called smiling, Therion. You are simply happy."

    voice "VA/JASON/GLORY/G32.mp3"
    t "Huh."

    voice "VA/JASON/GLORY/G33.mp3"
    t "Happy."

    tn "Her thumb traces the burn again. The mark she's carried in her mind for thirteen years without telling me."

    voice "VA/RAKUMAROO/GLORY/E43.mp3"
    e "Mhmm~ Smiling looks good on you."

    tn "Someday she's gonna be mine."

    tn "All mine."

    tn "Evangeline."

    voice "VA/JASON/GLORY/G34.mp3"
    t "Yeah."

    scene black
    with dissolve

    voice "VA/JASON/GLORY/G35.mp3"
    t "I think I'm... happy."

    # For the first time, his smile is real.

label epilogue_deluded:

    scene bg MM3:
        subpixel True
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
        zoom 1.0
        ease 15 zoom 0.6
    with fade
    show screen fireflies

    play music "hinokageri_orchestra.mp3"

    narrator "Once upon a time, there lived a Saintess, and beside her stood her faithful knight."

    narrator "She possessed the most magnificent grace in all the realm, capable of lifting one's sorrow."

    narrator "Beneath her gentle touch, souls grew warm again, smiling as everything became wonderfully, delightfully simple."

    narrator "Her knight cherished her beyond the measure of earthly love. The old chronicles say he counted every breath she ever drew, and in all his years, he never once lost tally."

    narrator "Wherever her slippers trod, he followed. Wherever he took his stand, she lingered. They were never sundered, not for a single hour, from the moment he knelt upon the flagstones until the final line was written."

    narrator "Side by side, they traversed the kingdom, province by province, soul by soul."

    narrator "She would extend her glowing palms, and the grey misery dissolved. Every face turned upward in a soft, radiant grin, every tongue chanting: 'Thank you, Saintess. Thank you.'"

    narrator "She cured the entire realm in the end. From far-flung hamlets to grand cities, not a single tear was left to fall."

    narrator "Every face wore a smile. Every doorway remained unbolted, for none possessed the desire to steal; every granary stood open, for none felt the urge to hoard."

    narrator "The bustling markets fell silent, for no one desired worldly goods. The courts dissolved, for no one committed wrong."

    narrator "How magnificent! An entire kingdom hushed in absolute peace, every spirit light as down, every gaze turned in the exact same placid direction."

    narrator "Her knight never vacated her side. Not when the highways grew long, nor when the final village was cleansed and there remained nothing left in creation to fix."

    narrator "How lovely, indeed."

    narrator "The Saintess and her knight cured the whole world, and the whole world smiled back at them in adoration, smiles that never once faded away."

    narrator "... And they lived happily ever after."

    $ persistent.main_menu = 3
    $ config.main_menu_music = mm_tracks[3]


    return

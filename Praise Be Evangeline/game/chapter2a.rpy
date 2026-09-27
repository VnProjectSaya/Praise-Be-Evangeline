label creepy:

    play music "fuyunotoudai.mp3"

    scene bg temple_corridor_day

    with fade


    # Eva hovering at mid-left
    show eva browsad neutral behind petra, ansel:
        xzoom -1                         # Facing right toward clerics
        subpixel True
        zoom 0.25
        xanchor 0.5 yanchor 1.0
        xpos 0.18 ypos 1.0 yoffset 40
        ease 0.34 xpos 0.25 
        block:
            ease 1.8 yoffset 20
            ease 1.8 yoffset 40
            repeat

    # Petra hovering at mid-right
    show petra idle browmad shocked shockedm:
        xzoom -1                         # Facing left
        subpixel True
        zoom 0.25
        xanchor 0.5 yanchor 1.0
        xpos 0.6 ypos 1.0 yoffset 40
        block:
            ease 2.1 yoffset 18
            ease 2.1 yoffset 40
            repeat

    # Ansel hovering next to Petra
    show ansel idle browsad frown shocked:
        xzoom 1                          # Facing left
        subpixel True
        zoom 0.25
        xanchor 0.5 yanchor 1.0
        xpos 0.79 ypos 1.0 yoffset 40
        block:
            ease 2.4 yoffset 22
            ease 2.4 yoffset 40
            repeat
    with dissolve

    $ renpy.pause(0.5, hard=True)

    voice "VA/TORA/Petra/2B/Petra_2B_1.mp3"
    petra "—cut straight through to the bone, I’m telling you! Clean through the tendon! As if a butcher did it!"

    # ============================================================
    # CAMERA ZOOMS IN ON PETRA & ANSEL
    # ============================================================

    camera:
        subpixel True
        xanchor 0.75 yanchor 0.5
        xpos 0.75 ypos 0.5
        easein 1.5 zoom 1.4

    voice "VA/SOPHIE/Ansel1.mp3"
    ansel "Petra, please! Have a shred of decency—"

    voice "VA/TORA/Petra/2B/Petra_2B_2.mp3"
    petra "And his fingers, Ansel! Clipped off one by one! They said it's missing one finger, they don't know where it is!"

    # Preserve Ansel's hover cycle when changing expression
    show ansel browsad shocked shockedm:
        block:
            ease 2.4 yoffset 22
            ease 2.4 yoffset 40
            repeat
    with dissolve

    voice "VA/SOPHIE/Ansel2.mp3"
    ansel "Mercy on us... where did they find them?"

    voice "VA/TORA/Petra/2B/Petra_2B_3.mp3"
    petra "Up in the bell tower! They're set up like a praying pair of hands!"

    # Preserve Petra's hover cycle when changing expression
    show petra browmad surprised shocked:
        block:
            ease 2.1 yoffset 18
            ease 2.1 yoffset 40
            repeat
    with dissolve

    voice "VA/TORA/Petra/2B/Petra_2B_4.mp3"
    petra "Only there wasn't an ounce of a body attached to them! And shoved between the knuckles, somebody had—"

    show ansel browsad angry shocked:
        block:
            ease 2.4 yoffset 22
            ease 2.4 yoffset 40
            repeat
    with dissolve

    voice "VA/SOPHIE/Ansel3.mp3"
    ansel "Gods above, stop! I'm going to throw up my breakfast...!"

    show petra browmad shocked shockedm:
        block:
            ease 2.1 yoffset 18
            ease 2.1 yoffset 40
            repeat
    with dissolve

    voice "VA/TORA/Petra/2B/Petra_2B_5.mp3"
    petra "They also said his mouth was wired wide! Copper thread pulled through the cheeks until the skin—"

    # ============================================================
    # CAMERA ZOOMS OUT TO REVEAL EVA
    # ============================================================

    camera:
        subpixel True
        easeout 1.2 zoom 1.0 xalign 0.5 yalign 0.5

    $ renpy.pause(1.2, hard=True)

    show eva browneutral normal_happy smile:
        block:
            ease 1.8 yoffset 20
            ease 1.8 yoffset 40
            repeat
    with dissolve

    voice "VA/RAKUMAROO/CHAPTER 2B/E1.mp3"
    e "Good afternoon!"

    show ansel browmad shocked shockedm:
        xzoom 1 subpixel True zoom 0.25 xanchor 0.5 yanchor 1.0 xpos 0.82 ypos 1.0
        parallel:
            # Base wing-floating hover loop
            block:
                ease 2.4 yoffset 22
                ease 2.4 yoffset 40
                repeat
        parallel:
            # Rapid trembling shake
            block:
                easein 0.03 xoffset -6
                easeout 0.03 xoffset 6
                repeat 5

    
    show petra browmad :
        xzoom 1 subpixel True zoom 0.25 xanchor 0.5 yanchor 1.0 xpos 0.70 ypos 1.0
        parallel:
            # Base wing-floating hover loop
            block:
                ease 2.1 yoffset 18
                ease 2.1 yoffset 40
                repeat
        parallel:
            # Rapid trembling shake (slightly desynced for natural feel)
            block:
                easein 0.025 xoffset 5
                easeout 0.025 xoffset -5
                repeat 5
    with dissolve

    
    voice "VA/TORA/Petra/2B/Petra_2B_6.mp3"
    petra "S-S-Saintess!"

    show ansel browneutral surprised normal:
        block:
            ease 2.4 yoffset 22
            ease 2.4 yoffset 40
            repeat
    with dissolve

    voice "VA/SOPHIE/Ansel4.mp3"
    ansel "Oh!"
    
    voice "VA/SOPHIE/Ansel5.mp3"
    ansel "Oh, goodness... g-good afternoon!"

    show eva browneutral normal_sad what:
        block:
            ease 1.8 yoffset 20
            ease 1.8 yoffset 40
            repeat
    with dissolve

    voice "VA/RAKUMAROO/CHAPTER 2B/E2.mp3"
    e "Whatever are you two discussing so intently?"

    show petra browneutral surprised normal:
        block:
            ease 2.1 yoffset 18
            ease 2.1 yoffset 40
            repeat
    with dissolve

    voice "VA/TORA/Petra/2B/Petra_2B_7.mp3"
    petra "N-Nothing of import! Kitchen business, Saintess!"

    show eva browneutral normal_happy smile:
        block:
            ease 1.8 yoffset 20
            ease 1.8 yoffset 40
            repeat
    with dissolve

    voice "VA/RAKUMAROO/CHAPTER 2B/E3a.mp3"
    e "Goodness, I had no idea meal planning was so intense! You look deathly pale, Petra."

    show petra browneutral smile normal:
        block:
            ease 2.1 yoffset 18
            ease 2.1 yoffset 40
            repeat
    with dissolve

    voice "VA/TORA/Petra/2B/Petra_2B_8.mp3"
    petra "Ahahaha! Do I? Must be the unflattering light in this corridor—"

    show ansel browsad frown normal:
        block:
            ease 2.4 yoffset 22
            ease 2.4 yoffset 40
            repeat
    with dissolve

    voice "VA/SOPHIE/Ansel6.mp3"
    ansel "Oh dear, yes... we were merely—"

    show petra browneutral smile normal:
        block:
            ease 2.1 yoffset 18
            ease 2.1 yoffset 40
            repeat
    with dissolve

    voice "VA/TORA/Petra/2B/Petra_2B_9.mp3"
    petra "Rations! For the autumn festival! So much to oversee!"

    voice "VA/RAKUMAROO/CHAPTER 2B/E4.mp3"
    e "I see! You seem terribly devoted to your duties. I do admire such earnest work."

    voice "VA/TORA/Petra/2B/Petra_2B_10.mp3"
    petra "Th-Thank you, Saintess."

    show ansel browneutral smile normal:
        block:
            ease 2.4 yoffset 22
            ease 2.4 yoffset 40
            repeat
    with dissolve

    voice "VA/SOPHIE/Ansel7.mp3"
    ansel "Yes... th-thank you."

    voice "VA/RAKUMAROO/CHAPTER 2B/E5.mp3"
    e "Carry on, then. Pray do not let me interrupt."

        # ============================================================
    # INFINITE SCROLLING & EVA GLIDES PAST THE CLERICS
    # ============================================================

    # Remove the static bg from line 5 so it stops covering the scroll.
    # bg1 starts at xpos 0, same spot, so this swap is invisible.
    hide bg

    show temple_corridor_day1 as bg1 onlayer bg_layer:
        subpixel True
        xpos 0 ypos 0
        block:
            xpos 0
            linear 25.0 xpos -1920
            repeat

    show temple_corridor_day1 as bg2 onlayer bg_layer:
        subpixel True
        xpos 1920 ypos 0
        block:
            xpos 1920
            linear 25.0 xpos 0
            repeat

    # Eva glides forward while keeping her floating hover cycle
    show eva browneutral normal_happy smile:
        xzoom -1
        subpixel True
        zoom 0.25
        xanchor 0.5 yanchor 1.0
        xpos 0.25 ypos 1.0 yoffset 40
        parallel:
            block:
                ease 1.2 yoffset 16
                ease 1.2 yoffset 40
                repeat
        parallel:
            linear 8.0 xpos 0.50

    # Petra & Ansel hover as they drift off-screen left
    show petra:
        subpixel True
        linear 6.0 xpos -0.30
        block:
            ease 2.1 yoffset 18
            ease 2.1 yoffset 40
            repeat

    show ansel:
        subpixel True
        linear 6.0 xpos -0.18
        block:
            ease 2.1 yoffset 18
            ease 2.1 yoffset 40
            repeat

    en "Kitchen business. Did a cook lose a digit slicing meat for the feast, I wonder?"

    en "I found one of those last night by the east window. I put it away safely so nobody would step on it."

    en "Perhaps I ought to return it. The kitchens do seem terribly frantic today."

    # ============================================================
    # 1. EVA KEEPS WALKING, BG KEEPS SCROLLING
    # (both already running from the cleric scene, nothing to restart)
    # ============================================================

    $ renpy.pause(2.0, hard=True)

    # ============================================================
    # 2. EVA STOPS WALKING (bg keeps scrolling)
    # ============================================================

    show eva:
        block:
            ease 1.8 yoffset 20
            ease 1.8 yoffset 40
            repeat
    # ============================================================
    # 3. KNIGHT ENTERS WHILE BG SMOOTHLY DECELERATES TO A STOP
    # ============================================================

    hide petra
    hide ansel

    show temple_corridor_day1 as bg1 onlayer bg_layer:
        subpixel True
        easeout 3.0 xoffset -145

    show temple_corridor_day1 as bg2 onlayer bg_layer:
        subpixel True
        easeout 3.0 xoffset -145

    show faceless_knight behind eva:
        xzoom 1
        subpixel True
        zoom 0.25
        xanchor 0.5 yanchor 1.0
        xpos 1.30 ypos 1.0 yoffset 100
        parallel:
            easein 3.0 xpos 0.78

    $ renpy.pause(3.0, hard=True)

    # ============================================================
    # 4. EVA REACTS, BG IS NOW FULLY STILL
    # ============================================================

    show eva browneutral normal_sad what
    with dissolve

    $ renpy.pause(0.5, hard=True)

    en "That is not Sir Caelor."
    show eva browneutral normal_happy smile with dissolve

    voice "VA/RAKUMAROO/CHAPTER 2B/E6.mp3"
    e "Good day! Wherever has Sir Caelor run off to?"

    voice "VA/JEFFEREY/Guard1.mp3"

    guard "C-Couldn't say, Saintess, only ordered to cover the post at sunrise."

    voice "VA/RAKUMAROO/CHAPTER 2B/E7b.mp3"
    e "A sudden promotion, I imagine?"

    voice "VA/JEFFEREY/Guard2.mp3"

    guard "I wasn't told the circumstances, Saintess. Only to stand guard and remain silent."

    voice "VA/RAKUMAROO/CHAPTER 2B/E7.mp3"
    e "Well, I am certain he is smiling broadly wherever he ends up!"

    voice "VA/JEFFEREY/Guard3.mp3"

    guard "Y-Yes, Saintess."

    show layer master:
        subpixel True
        anchor (0.5, 0.5) pos (960, 540)
        ease 2.5 zoom 1.7 xpos 960 ypos 580

    show layer bg_layer:
        subpixel True
        anchor (0.5, 0.5) pos (960, 540)
        ease 2.5 zoom 1.7 xpos 960 ypos 580

    en "I wonder where he has been taken now..."

    en "I certainly shall never forget how gently he tended to my scar."

    show eva closed_sad frown shadow

    stop music

    en "He possessed such remarkably soft fingers..."

    scene black
    with fade

    en "I trace the piece resting inside my pocket, marveling at how smooth the skin remains."

    en "I can only hope whoever receives the rest of him truly appreciates his delicate nature."

    stop music fadeout 1.0

    scene black
    $ current_frame = "twisted"
    pause 0.5

    scene bg study_night_lit 

    show desmond browneutral neutral neutral at right:
        # Applies dark cold blue to shadows and warm candle yellow to highlights
        matrixcolor ColorizeMatrix("#152238", "#f4dcb3")
        xzoom 1
        zoom 0.23
        alpha 0.0
        yoffset 100
        ease 0.6 alpha 1.0
        block:
            ease 3.0 yoffset 105
            ease 3.0 yoffset 95
            repeat

    en "Later that afternoon, the Archbishop summons me to his study."

    play music "shizumiyukutsuki.mp3"

    show eva browneutral neutral neutral:
        # Matches the lighting on Desmond
        matrixcolor ColorizeMatrix("#152238", "#f4dcb3")
        xzoom -1
        zoom 0.23
        xanchor 0.5
        yanchor 1.0
        xpos -0.2
        yalign 1.0
        yoffset 70
        alpha 0.0
        rotate 15

        easein 3 xpos 0.5 alpha 1.0 rotate 0

        block:
            ease 2.0 yoffset 80
            ease 2.0 yoffset 75
            repeat

    pause 1.0

    show layer master:
        subpixel True
        anchor (0.5, 0.5)
        pos (960, 540)
        zoom 1.0
        pause 0.5
        ease 3.0 zoom 1.7 xpos 600 ypos 500

    show desmond browneutral stern normal with dissolve

    voice "VA/GARFUNKEL/CH3A/Des1.mp3"
    de "Evangeline. Attend me."

    show eva browneutral normal_happy smile with dissolve

    voice "VA/RAKUMAROO/CHAPTER 2B/E8.mp3"
    e "Yes, Archbishop? Is everything well?"

    show desmond browmad stern normal with dissolve

    voice "VA/GARFUNKEL/CH3A/Des2.mp3"
    de "A minor incident occurred near the east corridor last night. A matter for the stewards, nothing to alarm you."

    show eva browneutral normal_happy smile with dissolve

    voice "VA/RAKUMAROO/CHAPTER 2B/E3.mp3"
    e "Mercy, how curious!"

    show desmond browmad stern shocked with dissolve

    voice "VA/GARFUNKEL/CH3A/Des3.mp3"
    de "I am conducting routine inquiries. Was your sworn knight at his post outside your chamber door all night?"

    show eva browneutral normal_sad neutral with dissolve

    e "..."

    show eva browneutral normal_happy smile with dissolve

    voice "VA/RAKUMAROO/CHAPTER 2B/E9.mp3"
    e "...Sir Therion? Oh, absolutely, Archbishop. He was right beside me all evening."

    show desmond browmad shocked stern with dissolve

    voice "VA/GARFUNKEL/CH3A/Des4.mp3"
    de "... He did not leave his post at any point?"

    voice "VA/RAKUMAROO/CHAPTER 2B/E10.mp3"
    e "Not once. He remained at my side from sundown to sunrise."

    show desmond browneutral neutral normal with dissolve

    voice "VA/GARFUNKEL/CH3A/Des5.mp3"
    de "... Very well. That will be all, Saintess."

    # Eva flips left (xzoom 1) and glides just a few steps over (xpos 0.38)
    show eva browneutral normal_sad neutral:
        xzoom 1
        parallel:
            block:
                ease 2.0 yoffset 80
                ease 2.0 yoffset 75
                repeat
        parallel:
            ease 1.0 xpos 0.45

    # Brief pause to let her stop moving
    $ renpy.pause(1.0, hard=True)

    e "..."

    # Eva completes her exit out of the zoomed frame
    show eva:
        parallel:
            block:
                ease 2.0 yoffset 80
                ease 2.0 yoffset 75
                repeat
        parallel:
            ease 2.5 xpos -0.3

    pause 0.8

    # Back in her private chambers. Therion rests against the wall.

    scene bg eva_bedroom_night_lit:
        subpixel True
        anchor (0.5, 0.5)
        zoom 1.2
        xpos 0.5
        ypos 0.5
    with fade

    # Eva is on the RIGHT (0.70), facing LEFT (1)
    show eva browneutral normal_happy frown:
        # Darker blueish night tint
        matrixcolor TintMatrix("#7a93b2") * BrightnessMatrix(-0.1)
        subpixel True
        xzoom 1
        zoom 0.55
        xanchor 0.5
        yanchor 1.0
        xpos 0.70
        yalign 1.0
        yoffset 800
        block:
            ease 2.0 yoffset 734
            ease 2.0 yoffset 750
            repeat
    with dissolve

    # Therion is on the LEFT (0.30), facing RIGHT (-1)
    show therion body0 half browskeptical frown:
        # Matches Eva's night tint
        matrixcolor TintMatrix("#7a93b2") * BrightnessMatrix(-0.1)
        subpixel True
        xzoom -1
        zoom 0.58
        xanchor 0.5
        yanchor 1.0
        xpos 0.30
        yalign 1.0
        yoffset 1000
    with dissolve

    voice "VA/RAKUMAROO/CHAPTER 2B/E11.mp3"
    e "Sir Therion... a quick question, if you don't mind?"

    show therion browneutral smile open with dissolve

    voice "VA/JASON/Therion109.mp3"
    t "Ask away, Saintess."

    voice "VA/RAKUMAROO/CHAPTER 2B/E12.mp3"
    e "The clergy are practically trembling over some scandal... something about severed limbs in the gallery?"

    voice "VA/RAKUMAROO/CHAPTER 2B/E13.mp3"
    e "I find myself dreadfully intrigued."

    show therion browneutral neutral half with dissolve

    voice "VA/JASON/Therion110.mp3"
    t "Heard the gossip."

    show eva browneutral normal_sad what with dissolve

    voice "VA/RAKUMAROO/CHAPTER 2B/E14.mp3"
    e "Do you know who did it?"

    voice "VA/JASON/Therion111.mp3"
    t "Not yet, my lady. Looking into it."

    show eva browneutral normal_happy smile with dissolve

    voice "VA/RAKUMAROO/CHAPTER 2B/E15.mp3"
    e "Do pursue it, won't you? I should love for you to clear the matter up."

    show therion browneutral smug luv with dissolve

    voice "VA/JASON/Therion112.mp3"
    t "Consider it handled."

    # Therion leaves backwards with 3 steps to the left (off-screen)
    show therion:
        subpixel True
        parallel:
            # 3 backward steps
            block:
                ease 0.5 yoffset 950
                ease 0.5 yoffset 1000
                repeat 3
        parallel:
            # Glides leftward off-screen while fading
            easeout 3.0 xpos -0.25 alpha 0.0

    pause 3.0
    hide therion

    show eva browsad yandere_happy frown shadow with dissolve

    en "This man lies with such a straight face."

    scene black
    with fade

    en "Sir Caelor never did return to his post."

    scene bg eva_bedroom_day
    with fade

    # Eva on the LEFT (0.30), facing RIGHT (-1)
    show eva browneutral normal_happy smile:
        subpixel True
        xzoom -1
        zoom 0.285
        xanchor 0.5
        yanchor 1.0
        xpos 0.30
        yalign 1.0
        yoffset 48
        block:
            ease 1.8 yoffset 28
            ease 1.8 yoffset 48
            repeat
    with dissolve

    en "A few days elapse before Therion returns to tell me the gallery business has been resolved."

    # Therion walks in from the RIGHT (1.25 -> 0.70), facing LEFT (1)
    show therion body0 browneutral neutral open:
        subpixel True
        xzoom 1
        zoom 0.27
        xanchor 0.5
        yanchor 1.0
        xpos 1.25
        yalign 1.0
        yoffset 90
        parallel:
            block:
                ease 0.5 yoffset 75
                ease 0.5 yoffset 90
                repeat
        parallel:
            easeout 2.5 xpos 0.70

    $ renpy.pause(2.5, hard=True)

    show therion body0 browneutral neutral open:
        subpixel True
        xzoom 1
        zoom 0.27
        xanchor 0.5
        yanchor 1.0
        xpos 0.70
        yalign 1.0
        yoffset 90

    voice "VA/JASON/Therion113.mp3"
    t "Dealt with, Saintess. Whoever caused that disturbance won't be bothering you again."

    show eva browneutral normal_happy smile with dissolve

    voice "VA/RAKUMAROO/CHAPTER 2B/E16.mp3"
    e "Oh, what a relief! A kitchen hand, do you think? I did wonder if someone had simply been careless with the butcher's knife."

    show therion browsad frown half with dissolve

    voice "VA/JASON/Therion114.mp3"
    t "Yeah. Something like that."

    voice "VA/RAKUMAROO/CHAPTER 2B/E17.mp3"
    e "Well, I am delighted it is finished. I do so enjoy when everything is kept in its proper place."

    show therion browsad frown closed with dissolve

    voice "VA/JASON/Therion115.mp3"
    t "Yeah. Me... too."

    play sound "audio/bird.mp3"

    show bird knock behind therion at bird_glass_wide
    $ renpy.pause(1.2, hard=True)

    show bg eva_bedroom_day at cam_push_window
    show bird at bird_glass_push
    show eva at eva_parallax_out
    show therion at therion_parallax_out
    $ renpy.pause(1.8, hard=True)

    show therion browmad neutral open

    voice "VA/JASON/Therion116.mp3"
    t "Want me to deal with that?"

    show eva browsad normal_sad frown

    voice "VA/RAKUMAROO/CHAPTER 2B/E18.mp3"
    e "Wait! Do not harm it, simply shoo it away."

    # POV: hands rise, bird drops onto them still panicking
    show eva browneutral normal_happy smile
    show hand behind bird at hands_rise
    show bird struggle at bird_to_hands
    show bg eva_bedroom_day at cam_pov
    $ renpy.pause(1.4, hard=True)

    en "I reach out and cup the creature in my palms before he can strike. It thrashes against my fingers, as they always do at first."

    show eva browneutral normal_sad smile
    play sound "audio/light.mp3"
    show bird blessed
    show holy_glow at glow_pov
    show holy_flash

    en "I feel its tiny heart slow beneath my thumb. The blessing in my hands flows through its feathers, releasing a wave of light that floods the room, bathing Therion's silhouette as well as mine."

    show bird glassy

    en "The bird's eyes turn glassy and blank before snapping clear again."

    show eva browhappy normal_happy smile
    hide holy_glow
    hide holy_flash
    with Dissolve(1.2)
    show bird robot

    voice "VA/RAKUMAROO/CHAPTER 2B/E19.mp3"
    e "There now. Off you go."

    show bird leave

    en "It finds the open window and flies off into the dusk."

    # hands sink away, camera pulls back, everyone returns to their marks
    hide bird
    show hand at hands_lower
    show bg eva_bedroom_day at cam_pull_back
    show eva at eva_parallax_back
    show therion at therion_parallax_back
    $ renpy.pause(1.8, hard=True)
    hide hand

    show therion browmad frown shook hair2 with dissolve

    en "But then, Therion lets out a choked breath."

    # Eva glides closer to him (moving from 0.30 to 0.45) while maintaining her hover
    show eva browneutral normal_sad what:
        parallel:
            block:
                ease 1.8 yoffset 28
                ease 1.8 yoffset 48
                repeat
        parallel:
            ease 1.5 xpos 0.45
    with dissolve

    voice "VA/RAKUMAROO/CHAPTER 2B/E20.mp3"
    e "Is everything quite all right, Therion?"

    # The scene slowly pushes in to focus closely on both of them
    show layer master:
        subpixel True
        anchor (0.5, 0.5) pos (960, 540)
        ease 1.5 zoom 1.4 xpos 750 ypos 650

    show therion creepy distort hair1:
        subpixel True
        # Re-declare base positioning so he doesn't snap to default coordinates
        xzoom 1
        zoom 0.27
        xanchor 0.5
        yanchor 1.0
        xpos 0.70
        yalign 1.0
        parallel:
            block:
                # Fast, subtle 4-pixel shudder around his base yoffset of 90
                linear 0.04 xoffset 4 yoffset 92
                linear 0.04 xoffset -4 yoffset 88
                linear 0.04 xoffset 2 yoffset 91
                linear 0.04 xoffset -2 yoffset 89
                linear 0.04 xoffset 0 yoffset 90
                pause 2.0
                repeat
    with hpunch 
    $ current_frame = "horror"

    if monstrous_points > deluded_points:

        stop music
        

        voice "VA/JASON/Therion117.mp3"
        t "S-S-Saintess."

        voice "VA/JASON/Therion118.mp3"
        t "Something's... I know something's... I can feel it in my—"

        voice "VA/JASON/Therion119.mp3"
        t "Kh-khh—"

        show eva browneutral normal_sad what with dissolve

        voice "VA/RAKUMAROO/CHAPTER 2B/E21.mp3"
        e "Therion?"

        voice "VA/JASON/Therion120.mp3"
        t "I'm good. I'm g-good, Saintess, I'm—"

        voice "VA/RAKUMAROO/CHAPTER 2B/E22.mp3"
        e "Oh dear. Your face is doing something rather extraordinary."

        voice "VA/JASON/Therion121.mp3"
        t "Don't. Don't look at it! I haven't got it right yet—"

        en "His mouth hangs open. One corner hitches wildly upward while the other remains frozen and dead."

        en "I have seen Therion smile perhaps three times since we met. This is a grotesque imitation."

        show eva browsad normal_sad frown with dissolve

        voice "VA/RAKUMAROO/CHAPTER 2B/E23.mp3"
        e "Therion, you are frightening me."

        voice "VA/JASON/Therion122.mp3"
        t "No! No, that ain't what I— I don't want that! I never want that! I want you to feel—"

        with hpunch

        voice "VA/JASON/Therion123.mp3"
        t "Ss-Saintess, I forget what my face is supposed to—"

        show eva browneutral normal_sad what with dissolve

        voice "VA/RAKUMAROO/CHAPTER 2B/E24.mp3"
        e "Supposed to do?"

        voice "VA/JASON/Therion124.mp3"
        t "Nghghhahhahh—"

        play sound "audio/bam.mp3"
        show layer master:
            anchor (0.5, 0.5) pos (960, 540) zoom 1.0
        show therion_mouth_jump at therion_slam with flashred
        with vpunch
        $ renpy.pause(1.5, hard=True)

        voice "VA/JASON/Therion125.mp3"
        t "S-See? There! That's—this is what it looks like, right? When someone's happy? This is—"

        play music "kurakunagaitunnel.mp3"

        en "Red crescents bleed where his nails dig into his own cheek, physically dragging his skin into an unnatural expression."

        en "The smile stretches and holds as his fingers refuse to let go; as if his face had forgotten how to do it on its own."

        voice "VA/RAKUMAROO/CHAPTER 2B/E25.mp3"
        e "Sir Therion. What precisely is occurring with your face?"

        voice "VA/JASON/Therion126.mp3"
        t "It stops. Sometimes. No big deal!"

        voice "VA/RAKUMAROO/CHAPTER 2B/E26.mp3"
        e "What do you mean, it stops?"

        voice "VA/JASON/Therion127.mp3"
        t "Some days my muscles forget what a face is s-supposed to do! I know what emotions are, I've studied it every day, but—"

        voice "VA/JASON/Therion128.mp3"
        t "Nghhhh—!"

        voice "VA/JASON/Therion129.mp3"
        t "But it's fine! I just have to force it! Like this!"

        show eva browsad normal_sad frown with dissolve

        show therion_mouth_jump stare at therion_pullback
        en "I take one step backward. His eyes drop to my shoes instantly."

        voice "VA/JASON/Therion130.mp3"
        t "You moved."

        voice "VA/JASON/Therion131.mp3"
        t "You moved away from me."

        voice "VA/RAKUMAROO/CHAPTER 2B/E27.mp3"
        e "Therion—"

        voice "VA/JASON/Therion132.mp3"
        t "Do... not... walk... AWAY FROM ME!!" with rattle

        en "The shout booms through the room. His hands shake, leaving bloody half-moon marks in his skin."

        show therion browsad angry half with dissolve

        voice "VA/JASON/Therion133.mp3"
        t "I'm sorry. I'm s-sorry... I didn't mean to—that was too loud. I scared you!"

        show therion browsad gritannoyed half with dissolve

        voice "VA/JASON/Therion134.mp3"
        t "Please don't go. I'll practice!"

        voice "VA/JASON/Therion136.mp3"
        t "I'll get the expression right, I'll force it over and over and over and over and over and over until I don't have to think about it anymore, just please don't walk away!"

        show layer master:
            subpixel True
            anchor (0.5, 0.5) pos (960, 540)
            zoom 1.4 xpos 750 ypos 650
        show therion browsad half angry hair2:
            subpixel True
            xzoom 1
            zoom 0.31
            xanchor 0.5
            yoffset 200
        show eva browmad normal_sad what
        hide therion_mouth_jump
        with dissolve

        voice "VA/RAKUMAROO/CHAPTER 2B/E36.mp3"
        e "Sir Therion. You are dismissed. Go take a rest."

        show therion browsad frown half with dissolve

        voice "VA/JASON/Therion137.mp3"
        t "D-Dismissed. Right. Yeah. I'll go and—it'll be fixed by morning. It HAS to be."

        voice "VA/JASON/Therion138.mp3"
        t "G-Goodnight, my lady."

        show therion:
            subpixel True
            # Step 1
            easein 0.25 xpos 0.82 yoffset 210
            easeout 0.20 yoffset 200
            pause 0.25
            # Step 2
            easein 0.25 xpos 0.95 yoffset 210
            easeout 0.20 yoffset 200
            pause 0.25
            # Step 3 (exits frame)
            easein 0.30 xpos 1.15 yoffset 210
            easeout 0.20 yoffset 200

        en "He walks out backward, watching me until the door closes."

        en "I stay awake for hours after he leaves."

        show eva browneutral yandere_sad frown with dissolve

        en "... Hmm."

    else:

        voice "VA/JASON/Therion139.mp3"
        t "Everything is... fine."

        voice "VA/JASON/Therion140.mp3"
        t "Ngh—"

        show eva browneutral normal_sad what with dissolve

        voice "VA/RAKUMAROO/CHAPTER 2B/E29.mp3"
        e "Therion? Heavens, what is wrong?"

        voice "VA/JASON/Therion141.mp3"
        t "Kh... khhhh... I'm fine, Saintess. I'm perfectly..."

        voice "VA/RAKUMAROO/CHAPTER 2B/E30.mp3"
        e "Oh dear, your face is doing something rather terrifying!"

        voice "VA/JASON/Therion142.mp3"
        t "I'm trying to smile. For you. Because you're here and that makes me—"

        voice "VA/JASON/Therion143.mp3"
        t "Glad. Yes. That's the word. Glad."

        en "His mouth hangs open awkwardly. One side pulls upward while the other is paralyzed."

        show eva browneutral normal_sad what with dissolve

        en "I have seen Therion smile perhaps three times since he took his oath. This is not it."

        show eva browsad normal_sad frown with dissolve

        voice "VA/RAKUMAROO/CHAPTER 2B/E31.mp3"
        e "Therion, please, you are frightening me!"

        voice "VA/JASON/Therion144.mp3"
        t "No! I want you to feel safe with me! That's my whole—that's the only reason I—"

        stop music

        play sound "audio/bam.mp3"
        show layer master:
            anchor (0.5, 0.5) pos (960, 540) zoom 1.0
        show therion_mouth_jump at therion_slam with flashred
        with vpunch
        $ renpy.pause(1.5, hard=True)

        voice "VA/JASON/Therion145.mp3"
        t "Hhhah... Hhhah... See? See!? I fixed it! It looks right now, isn't it!?"

        voice "VA/JASON/Therion146.mp3"
        t "Nghghhahhahh—"

        en "Oh dear, should I fetch a healer?"

        en "I am about to move towards the door, but then—"

        play music "kurakunagaitunnel.mp3"

        voice "VA/JASON/Therion147.mp3"
        t "Wait! No, no! Sorry, I'll try again!"

        with hpunch

        voice "VA/JASON/Therion148.mp3"
        t "... Better?"

        en "Bloody crescents form where his nails dig into his own flesh, manually hoisting his cheeks into an imitation of happiness."

        en "The smile remains frozen and unnatural, while his hands tremble against his face."

        en "My heart aches watching him struggle so violently to retain his humanity for my sake."

        en "If only he just stops fighting it."

        voice "VA/RAKUMAROO/CHAPTER 2B/E32.mp3"
        e "Sir Therion... please stop. You are hurting yourself!"

        voice "VA/JASON/Therion149.mp3"
        t "Yes. Stop. Sometimes my face stops and I have to fix it."

        voice "VA/RAKUMAROO/CHAPTER 2B/E33.mp3"
        e "What do you mean, it stops?"

        voice "VA/JASON/Therion150.mp3"
        t "The moving. I remember every expression I've ever seen on a man."

        voice "VA/JASON/Therion151.mp3"
        t "But... If I don't hold it steady, like this—"

        with sshake

        en "He pulls himself even wider and blood starts coming out."

        voice "VA/JASON/Therion152.mp3"
        t "Nghhhh—!"

        voice "VA/JASON/Therion153.mp3"
        t "—it goes unnatural and I'd scare you!"
        show eva browsad normal_sad frown with dissolve

        show therion_mouth_jump at therion_pullback
        en "I take one gentle step backward to give him room."

        show therion_mouth_jump stare
        en "His eyes lock onto my boots."

        voice "VA/JASON/Therion154.mp3"
        t "You moved."

        voice "VA/JASON/Therion155.mp3"
        t "From me."

        show eva browsad normal_sad frown with dissolve

        voice "VA/RAKUMAROO/CHAPTER 2B/E34.mp3"
        e "Therion, pray calm yourself—"

        voice "VA/JASON/Therion156.mp3"
        t "DO NOT WALK AWAY FROM ME!!" with rattle

        en "The shout rattles the windowpanes. His hands shake as he lowers them, tearing the skin of his face a little."

        show eva browneutral normal_sad shocked with dissolve

        voice "VA/RAKUMAROO/CHAPTER 2B/E35.mp3"
        e "...!"

        show layer master:
            subpixel True
            anchor (0.5, 0.5) pos (960, 540)
            zoom 1.4 xpos 750 ypos 650
        show therion browsad half angry hair2:
            subpixel True
            xzoom 1
            zoom 0.29
            xanchor 0.5
            yanchor 1.0
            xpos 0.70
            yalign 1.0
            xoffset 0
            yoffset 55
            ease 0.8 yoffset 105
            block:
                linear 0.04 xoffset 3 yoffset 107
                linear 0.04 xoffset -3 yoffset 103
                linear 0.04 xoffset 2 yoffset 106
                linear 0.04 xoffset -2 yoffset 104
                linear 0.04 xoffset 0 yoffset 105
                pause 0.4
                repeat
        hide therion_mouth_jump
        with dissolve

        voice "VA/JASON/Therion157.mp3"
        t "Oh no."

        voice "VA/JASON/Therion158.mp3"
        t "I'm sorry. I'm s-sorry, that was too loud! I know that was wrong!"

        show therion browsad gritannoyed half with dissolve

        voice "VA/JASON/Therion159.mp3"
        t "Please, please, please, please, please, please, please, please, please don't go."

        voice "VA/JASON/Therion160.mp3"
        t "I'll practice, I'll practice, I'll practice until it works again, I just need you to stay where I can see you. Please."

        show eva browsad normal_happy frown with dissolve

        en "Oh, you poor, broken darling..."

        show eva browsad normal_sad frown with dissolve

        voice "VA/RAKUMAROO/CHAPTER 2B/E36.mp3"
        e "Sir Therion. You are dismissed. Go take a rest."

        show therion browsad frown half with dissolve

        voice "VA/JASON/Therion161.mp3"
        t "Dismissed. Yeah. I'll go and—tomorrow the smile will work. It HAS to be."

        show therion browsad distort half with dissolve

        voice "VA/JASON/Therion162.mp3"
        t "G-Goodnight, my lady."

        show therion:
            subpixel True
            # Step 1
            easein 0.25 xpos 0.82 yoffset 113
            easeout 0.20 yoffset 105
            pause 0.25
            # Step 2
            easein 0.25 xpos 0.95 yoffset 113
            easeout 0.20 yoffset 105
            pause 0.25
            # Step 3 (exits frame)
            easein 0.30 xpos 1.15 yoffset 113
            easeout 0.20 yoffset 105

        en "He walks out backward, stepping into the dark corridors without breaking eye contact."

        en "I remain by the window long after he disappears."

        show eva browsad yandere_sad frown with dissolve

        voice "VA/RAKUMAROO/CHAPTER 2B/E38.mp3"
        e "Oh, Therion... What have I done to you?"
    scene black
    with fade


    scene black
    stop music

    en "Therion is himself again by morning."

    en "Or rather, he's become far sweeter than I ever dared anticipate."

    $ current_frame = "dream"

    scene white
    show therion_flowers at therion_parallax
    show eva_wings_flap at eva_parallax
    $ renpy.pause(2.6, hard=True)

    play music "hinokageri.mp3"

    en "He greets me at my doorway, holding a tied bundle of fresh, Evangeline Lilac flowers."

    en "And resting upon his features is a smile, no longer the grotesque mask he dragged across his cheeks yesterday."

    en "Somehow... he looks stunningly handsome."

    voice "VA/JASON/Therion163.mp3"
    t "Mornin', Saintess."

    voice "VA/RAKUMAROO/CHAPTER 2B/E39.mp3"
    e "Sir Therion! Good gracious... what is all this?"

    voice "VA/JASON/Therion164.mp3"
    t "For you. Picked 'em near the eastern wall."
    voice "VA/JASON/Therion165.mp3"
    t "Ain't proper, I know. The Archbishop'd probably have me flogged if he caught me."

    voice "VA/JASON/Therion166.mp3"
    t "But ever since someone left those blooms on your desk... I couldn't stop thinking about it."

    voice "VA/JASON/Therion167.mp3"
    t "Couldn't stand the thought of another man giving you pretty things. It had to be me."

    voice "VA/RAKUMAROO/CHAPTER 2B/E40.mp3"
    e "Therion... they are lovely. Thank you."

    en "I take the bouquet, cradling the stems against my chest."

    en "His expression is so gentle that my hand moves on its own."

    scene black

    scene bg eva_bedroom_day:
        subpixel True
        anchor (0.7, 0.4)
        zoom 1.5
        xpos 0.5
        ypos 0.5
    with fade

    show therion body0 browneutral smile open hair1 at therion_face_zoom
    with Dissolve(1.0)

    show eva_hand at eva_hand_reach zorder 5

    en "I raise my palm toward his face, wanting to feel the warmth of his cheek."

    en "Then I remember."

    stop music
    play sound "audio/flash.mp3"

    show therion_mouth_jump at therion_slam, horror_flash zorder 11
    show layer master at horror_jolt
    with flashred

    en "The clawing. The bloody crescents carved into his skin. The sickening sound of him forcing his jaw into a shape his mind could no longer make."

    hide therion_mouth_jump with Dissolve(0.1)
    show eva_hand at eva_hand_flinch

    en "I draw back."

    hide eva_hand with Dissolve(0.3)

    show therion browmad frown creepy with dissolve

    en "Therion catches the hesitation. The smile falters, a dark shadow hovering above his gaze."

    voice "VA/JASON/Therion168.mp3"
    t "You... pulled away."

    $ current_frame = "twisted"

    # camera pulls out, bars slide away
    show therion at therion_pullout

    voice "VA/RAKUMAROO/CHAPTER 2B/E41.mp3"
    e "I—"

    play music "seijaku.mp3"
    show therion browmad angry at therion_rage
    show layer master at rage_shake
    with dissolve

    voice "VA/JASON/Therion169.mp3"
    t "I got the face right, Saintess! I fixed it! Worked on it until sunrise so it wouldn't scare you!"

    voice "VA/JASON/Therion170.mp3"
    t "What the hell is wrong with it now!?" with vpunch

    voice "VA/RAKUMAROO/CHAPTER 2B/E42.mp3"
    e "Therion, I am simply being mindful of my station! If the Archbishop—"

    show layer master at layer_reset
    show therion browmad frown shook at therion_settle
    with dissolve

    voice "VA/JASON/Therion171.mp3"
    t "... Oh. Right."

    t "..."

    e "..."

    show therion luvhalf frown browsad

    voice "VA/JASON/Therion172.mp3"
    t "We should go. The Archbishop is expecting you."

    voice "VA/RAKUMAROO/CHAPTER 2B/E43.mp3"
    e "... Yes. We should."
    scene black
    with fade

    pause 0.5

    show layer master:
        subpixel True
        anchor (0.5, 0.5) pos (960, 540)
        rotate -3 zoom 1.1

    scene bg arena_day_lit

    play music "oath.mp3"

    show layer master:
        subpixel True
        anchor (0.5, 0.5) pos (960, 540)
        rotate -3 zoom 1.1

    show therion body0 browmad open frown at therion_arena
    show eva browneutral normal_happy smile at eva_arena

    show villager1 at convict_pov(CONVICT_L)
    show villager2 at convict_pov(CONVICT_M)
    show villager3 at convict_pov(CONVICT_R)
    with fade

    en "The Church was kind enough to bring the condemned directly to my courtyard, sparing me the journey."

    en "The Archbishop insists it is safer after Murrayfield. I am so deeply grateful for his consideration."

    en "A small line of chained convicts stands waiting before the dais, kept secure by our diligent temple guards."

    en "Three souls today. Misguided individuals who have strayed down a tragic path."

    en "I pray that by evening, each of them may be relieved of their heavy burdens. I am so eager to help them!"

    en "Therion takes his post beside me, eyes screening everyone before I start."

    voice "VA/JASON/Therion173.mp3"
    t "Twelve clergy, seven women, five children. Guard detail of six, two half asleep."

    show therion browmad shook gritannoyed with dissolve

    voice "VA/JASON/Therion173a.mp3"
    t "Anyone in the front row gets ideas, I'll have 'em down before you can blink."

    show therion browmad open frown with dissolve
    show eva browneutral normal_happy smile with dissolve

    voice "VA/RAKUMAROO/CHAPTER 2B/E44.mp3"
    e "That will not be necessary, Sir Therion."

    voice "VA/RAKUMAROO/CHAPTER 2B/E45.mp3"
    e "Let us begin."

    # ── BLESS: RIGHT ──
    
    show eva browhappy closed_happy smile at eva_arena_bless(-1, 30)
    play sound "audio/light.mp3"
    show villager3 at convict_blessed(CONVICT_R)
    show holy_glow as glow_r at convict_glow(1498, 680)
    show arena_flash as flash_r
    $ renpy.pause(3.2, hard=True)

    show eva normal_happy
    hide glow_r
    hide flash_r
    with Dissolve(1.0)

    show therion smile

    # ── BLESS: MIDDLE ──
    
    show eva browhappy closed_happy smile at eva_arena_bless(-1, 20)
    play sound "audio/light.mp3"
    show villager2 at convict_blessed(CONVICT_M)
    show holy_glow as glow_m at convict_glow(1152, 680)
    show arena_flash as flash_m
    $ renpy.pause(3.2, hard=True)

    show eva normal_happy
    hide glow_m
    hide flash_m
    with Dissolve(1.0)

    en "The first two purifications go so wonderfully! The grey gloom lifts away from them immediately."

    en "The both of them weeps with joy as the sacred light touches them, ah, how beautiful!"

    en "Oh, Heavens, allow me a long life so I can keep easing another's suffering like this!"

    show eva browneutral normal_sad neutral with dissolve

    # ── FLIP TO FAR LEFT ──
    show eva at eva_arena_flip
    $ renpy.pause(0.4, hard=True)

    en "The final prisoner appears so frail, far younger than the others. Her hair is matted and her wrists are bleeding."

    show eva browneutral normal_sad what with dissolve

    en "She has glared at me the entire time, what intense anguish!"

    show eva browhappy normal_happy smile with dissolve

    en "Poor lady... I pray this modest blessing brings comfort to her troubled heart."

    en "As I am about to cast my light..."

    scene scream_bg
    show scream_woman at scream_jumpscare
    play sound "VA/SOPHIE/Woman2b/Woman1.ogg"
    pause 1.5

    stop music

    $ current_frame = "horror"

    woman "AAHAHHHHHHH—!"

    play music "organ.mp3"

    en "...Why is her voice so distorted? Is she rejecting the blessing!?"

    stop sound

    voice "VA/SOPHIE/Woman2b/Woman2.ogg"

    woman "AAAHH... IT HURTS, IT HURTS! WHAT ARE YOU PULLING OUT—"

    voice "VA/SOPHIE/Woman2b/Woman3.ogg"

    woman "SOMETHING IS COMING OUT OF ME! PLEASE, HELP—"

    en "No! That is wrong! Why does she cling to her agony? Why won't she let it die?!"

    voice "VA/SOPHIE/Woman2b/Woman4.ogg"

    woman "STOP HER! SHE'S DIGGING INTO MY CHEST, IT BURNS, IT BURNS—"

    voice "VA/SOPHIE/Woman2b/Woman5.ogg"

    woman "PLEASE, PLEASE, PLEASE FOR THE LOVE OF GODS, STOP IT—"

    en ".... Why!?"

    en "Why fight me?! Feelings are the cause of such suffering! I am mending her! Why won't she just let go?!"

    voice "VA/SOPHIE/Woman2b/Woman6.ogg"

    woman "PLEASE! I ONLY STOLE BREAD FOR MY BABIES! WHY DO YOU PUNISH ME LIKE THIS!?"

    en "Her skin grows translucent. I can see the dark veins pulsing in her neck, the shadow of her skull beneath."

    voice "VA/SOPHIE/Woman2b/Woman7.ogg"

    woman "YOU'RE NOT A SAINTESS, YOU'RE A MONSTER—"

    en "She hurls herself against the iron, clawing right for my eyes."

    # Therion crosses the platform in a single motion and drives the scythe through her before her hand reaches Evangeline anim

    scene black
    with fade

    en "But Therion moves faster than a shadow."

        
    scene bg RED

    show dummy2_idle as dummy2 at fit_canvas_left
    pause 0.2

    show therion_slash_seq as therion_flip at therion_swing_move_flip
    pause 0.10

    play sound "VA/SOPHIE/Woman2b/Woman1.ogg"

    pause 0.1

    play sound "audio/slash.mp3"

    show dummy2_cut as dummy2 at fit_canvas_left
    pause 0.0005

    show slash_impact_flash_two
    show layer master at hpunch
    pause 0.15

    hide therion_flip
    hide slash_impact_flash_two
    hide dummy2

    show dummy2_top at dummy2_top_away
    show dummy2_bottom at dummy2_bottom_away
    pause 0.7

    hide dummy2_top
    hide dummy2_bottom
    pause 0.3

    en "The heavy scythe drives straight through her, severing her torso from her legs."

    scene black
    with sshake

    en "Her mouth remains locked in a silent shriek. Her hand stays outstretched even as her body collapses."

    en "So much blood..."


    show layer master:
        subpixel True
        anchor (0.5, 0.5) pos (960, 540)
        rotate -8 zoom 1.24

    scene bg arena_day_lit at arena_world_spin

    show layer master:
        subpixel True
        anchor (0.5, 0.5) pos (960, 540)
        rotate -8 zoom 1.24

    show eva calm shadow browsad yandere_sad what at eva_spin_focus
    show therion body0 browmad angry shook at therion_guard_front
    with Dissolve(0.5)

    en "How can a soul being emptied of feeling hold such warmth?"

    show therion browmad gritangry shook with dissolve

    voice "VA/JASON/Therion174.mp3"
    t "Behind me. Now!"

    show eva agitated browmad yandere_sad frown at eva_spin_shake with dissolve

    voice "VA/RAKUMAROO/CHAPTER 2B/E46.mp3"
    e "I... why did she fight for her pain, Therion? Why did she hate me for saving her?!"

    show therion browmad angry shook with dissolve

    voice "VA/JASON/Therion175.mp3"
    t "I said {i}now{/i}, Saintess."

    show eva browneutral yandere_sad frown at eva_spin_focus with dissolve

    en "The light has faded, but the sensation lingers in my palms."

    en "... It felt glorious. Before."

    en "Odd... Usually stripping a person down to absolute nothingness felt like pure ecstasy."

    show eva browsad yandere_sad what with dissolve

    en "Yet now, it feels hollow."

    show bg arena_day_lit at arena_world_settle
    show eva at eva_pulled_back
    show therion at therion_pulled_back
    show faceless_knight as knight_l at knight_rush_l
    show faceless_knight as knight_r at knight_rush_r
    $ renpy.pause(0.8, hard=True)

    voice "VA/GARFUNKEL/CH3A/Des6.mp3"
    de "Get her inside! Right now!"

    en "The Archbishop rushes across the platform faster than I have ever seen him move, grabbing a soldier's arm so hard the man winces."

    voice "VA/GARFUNKEL/CH3A/Des7.mp3"
    de "If there is so much as a scratch on her tomorrow, you will answer to me!"

    show eva at eva_dragged
    show therion at therion_dragged
    show faceless_knight as knight_l at knight_press_l
    show faceless_knight as knight_r at knight_press_r
    $ renpy.pause(0.5, hard=True)

    en "Guards seize my arms and drag me backward. I try to turn, to look at the woman's body."

    en "I still don't understand."

    en "Why would anyone fight to keep the very grief that destroys them?"

    scene black
    with fade

    en "But Therion shoves hard against my back, driving me toward the heavy doors. His fingers dig into my shoulder until it aches."
    show bg temple_corridor_day
    $ renpy.pause(0.5, hard=True)

    show eva browmad yandere_sad shocked:
        xzoom -1
        subpixel True
        zoom 0.25
        xanchor 0.5
        yanchor 1.0
        yalign 1.0
        yoffset 40
        xpos 1.25
        parallel:
            easeout_quad 2.2 xpos 0.46
            ease 0.4 xpos 0.445
            ease 0.5 xpos 0.45
        parallel:
            block:
                ease 2.0 yoffset 24
                ease 2.0 yoffset 40
                repeat

    show therion browmad frown:
        subpixel True
        zoom 0.23
        xanchor 0.5
        yanchor 1.0
        yalign 1.0
        yoffset 40
        xpos 1.40
        easeout_quad 2.2 xpos 0.64
        ease 0.4 xpos 0.625
        ease 0.5 xpos 0.63

    $ renpy.pause(3.1, hard=True)

    voice "VA/JASON/Therion176.mp3"
    t "Don't look back. Whatever she said, it was just crazy talk."

    show eva:
        parallel:
            ease 0.45 xpos 0.47
        parallel:
            block:
                ease 2.0 yoffset 24
                ease 2.0 yoffset 40
                repeat
    show therion:
        pause 0.1
        ease 0.45 xpos 0.645

    show eva browmad yandere_sad frown with dissolve

    voice "VA/RAKUMAROO/CHAPTER 2B/E47.mp3"
    e "She fought for her pain, Therion. She wanted to keep it. Why!?"

    show therion:
        ease 0.45 xpos 0.625
    show eva:
        parallel:
            pause 0.1
            ease 0.45 xpos 0.45
        parallel:
            block:
                ease 2.0 yoffset 24
                ease 2.0 yoffset 40
                repeat

    show therion browmad frown shook with dissolve

    voice "VA/JASON/Therion177.mp3"
    t "She was a filthy criminal, Saintess. Criminals say crazy shit—"

    show eva:
        parallel:
            ease 0.45 xpos 0.47
            block:
                linear 0.05 xoffset 3
                linear 0.05 xoffset -3
                repeat 3
            linear 0.05 xoffset 0
        parallel:
            block:
                ease 2.0 yoffset 24
                ease 2.0 yoffset 40
                repeat
    show therion:
        pause 0.1
        ease 0.45 xpos 0.645

    show eva browneutral yandere_sad shocked with dissolve

    voice "VA/RAKUMAROO/CHAPTER 2B/E48.mp3"
    e "She called me a monster."

    show therion browsad half frown with dissolve

    voice "VA/JASON/Therion178.mp3"
    t "No, don't listen to her."

    show therion browneutral smile luv with dissolve

    voice "VA/JASON/Therion179.mp3"
    t "You are the most divine thing I've ever seen in my life. Fuck everyone else."

    show eva browneutral yandere_sad what with dissolve

    e "..."

    show eva:
        parallel:
            ease 0.5 xzoom 1.0
        parallel:
            block:
                ease 2.0 yoffset 24
                ease 2.0 yoffset 40
                repeat

    $ renpy.pause(0.7, hard=True)

    show eva:
        parallel:
            ease 3.2 xpos -0.30
        parallel:
            block:
                ease 2.0 yoffset 24
                ease 2.0 yoffset 40
                repeat
    show therion:
        pause 0.3
        ease 3.2 xpos -0.20

    $ renpy.pause(2.0, hard=True)

    hide eva
    hide therion
    with easeoutleft

    show vidius eyeshocked frown:
        subpixel True
        zoom 0.21
        xanchor 0.5
        yanchor 1.0
        yalign 1.0
        yoffset 40
        xpos 0.70
        parallel:
            block:
                ease 2.8 yoffset 45
                ease 2.8 yoffset 49
                repeat

    with easeinright

    $ renpy.pause(0.6, hard=True)

    show layer master:
        subpixel True
        xanchor 0.70
        yanchor 0.55
        xpos 0.70
        ypos 0.55
        easein_quad 1.2 zoom 1.4 xpos 0.62 ypos 0.50
    vidius "..."

    stop music


    scene black with fade

    en "The Archbishop insists I remain confined to my wing until the dust settles."

    en "But as always, I never listen to him."

    play music "haikyo.mp3"


    $ mg_reset()

    scene bg temple_corridor_night

    show eva browneutral normal_sad what:
        subpixel True
        zoom 0.25
        xanchor 0.5
        yanchor 1.0
        yalign 1.0
        matrixcolor TintMatrix(MG_NIGHT_TINT)
        function mg_eva_tf

    show eva as eva_shadow behind eva:
        subpixel True
        rotate_pad False
        transform_anchor True
        xanchor 0.5
        yanchor 1.0
        ypos MG_WALL_FLOOR
        zoom MG_EVA_SHADOW_ZOOM
        xzoom MG_EVA_SHADOW_WIDEN
        yzoom MG_EVA_SHADOW_YSTRETCH
        rotate MG_SHADOW_LEAN
        alpha MG_EVA_SHADOW_ALPHA
        blur MG_SHADOW_BLUR
        matrixcolor TintMatrix("#000000")
        function mg_eshadow_tf

    with dissolve

    en "Though the torches seem unusually dim tonight..."

    en "I do not recall this gallery being quite so long. Have the walls stretched, or are my eyes deceiving me?"

    show vidius as vshadow behind eva:
        subpixel True
        rotate_pad False
        transform_anchor True
        xanchor 0.5
        yanchor 1.0
        ypos MG_WALL_FLOOR + MG_SHADOW_DROP
        matrixcolor TintMatrix("#000000")
        blur MG_SHADOW_BLUR
        zoom MG_SHADOW_ZOOM
        xzoom MG_SHADOW_WIDEN
        yzoom MG_SHADOW_YSTRETCH
        rotate MG_SHADOW_LEAN
        xpos 1.9
        alpha 0.0
        parallel:
            easeout_quad 2.8 xpos mg_shadow_x
        parallel:
            ease 1.5 alpha MG_SHADOW_ALPHA
        function mg_vshadow_tf

    $ renpy.pause(3.0, hard=True)


    en "Oh my."

    en "There is another shadow cast against the stone, directly beside mine."

    while mg_stage < 4:

        call screen eva_shadow_walk

        if _return == "steps":

            show eva browneutral normal_happy smile with dissolve

            en "Surely it is only Therion following close behind. He grows so terribly possessive when I am distressed, and today was enough to rattle anyone."

            show eva browneutral normal_sad what with dissolve

            en "Though... {w}that silhouette is far too massive to be Therion."

            en "It does not move like him, either. Therion's steps are sure-footed, this thing... floats."

            en "..."

        elif _return == "look_back":

            show eva browneutral normal_sad frown with dissolve

            en "Empty."

            en "How strange. I would have sworn on the scriptures someone was breathing against my neck."

        elif _return == "look_front":

            show eva browmad normal_sad frown with dissolve

            voice "VA/RAKUMAROO/CHAPTER 2B/E49.mp3"
            e "Therion, if that is you, say so. I have had quite enough surprises for one day."

            show eva browneutral normal_sad frown with dissolve

            en "Silence."

            show eva browneutral normal_happy smile with dissolve

            en "Well. Whatever you are, you certainly know how to hover just beyond sight."

    $ renpy.block_rollback()
    

    en "I think I shall go inside, slide the bolt, and pretend none of this ever happened."

    scene black
    with fade

    $ quick_menu = True

    en "Yes. Everything will be... {w}all right by tomorrow."

label vidius_confrontation:

    voice "VA/GARFUNKEL/CH3A/Des8.mp3"
    de "I said STOP it!"

    voice "VA/TORA/Vidius/2B/Vidius_2B_1.mp3"
    vidius "NO! LISTEN TO ME!"

    scene bg eva_bedroom_night_dark:
        subpixel True
        anchor (0.5, 0.5)
        zoom 1.5
        xpos 0.5
        ypos 0.5
    with fade

    show eva browneutral normal_sad what shadow:
        matrixcolor TintMatrix("#368ab1")
        subpixel True
        xzoom -1
        zoom 0.55
        xanchor 0.5
        yanchor 1.0
        xpos 0.30
        yalign 1.0
        yoffset 800
        block:
            ease 2.0 yoffset 734
            ease 2.0 yoffset 750
            repeat
    with sshake

    en "Shouting jolts me from a restless sleep long after midnight."

    en "Father never shouts. In all my years, he has spoken only with measured, absolute grace."

    en "I slip from my bed to see what has undone him."

    $ renpy.block_rollback()
    $ config.rollback_enabled = False
    $ no_rollback_scene = True

    scene bg study_night_dark

    play sound "audio/creak.mp3"

    show peek_door as peek_l at peek_door_left zorder 50
    show peek_door as peek_r at peek_door_right zorder 50

    show vidius agitated browmad eyeshocked shockedm:
        subpixel True
        zoom 0.27
        xanchor 0.5 yanchor 1.0
        xpos 0.26 yalign 1.0
        yoffset 176
        xzoom -1
        matrixcolor TintMatrix("#9fb0d6")
        parallel:
            block:
                ease 2.2 xpos 0.30
                ease 0.3 xzoom 1
                ease 2.2 xpos 0.22
                ease 0.3 xzoom -1
                repeat
        parallel:
            block:
                ease 2.8 yoffset 162
                ease 2.8 yoffset 190
                repeat

    pause 4.0

    voice "VA/TORA/Vidius/2B/Vidius_2B_2.mp3"
    vidius "The poor woman was SCREAMING, Desmond!"

    voice "VA/TORA/Vidius/2B/Vidius_2B_3.mp3"
    vidius "Four decades I've observed purifications! Every Saintess in history absorbed the parish's grief into her own heart!"

    show desmond agitated browmad shocked stern:
        subpixel True
        zoom 0.30
        xanchor 0.5 yanchor 1.0
        xpos 0.96 yalign 1.0
        yoffset 222
        xzoom 1
        matrixcolor TintMatrix("#9fb0d6")
        alpha 0.0
        parallel:
            easein 1.6 xpos 0.76 alpha 1.0
        parallel:
            block:
                ease 3.0 yoffset 210
                ease 3.0 yoffset 234
                repeat

    voice "VA/GARFUNKEL/CH3A/Des9.mp3"
    de "And my daughter carries that sacred burden like everyone else."

    show vidius browmad eyeshocked angry:
        parallel:
            ease 0.15 xzoom -1
        parallel:
            easein 0.4 xpos 0.34
        parallel:
            block:
                ease 2.8 yoffset 162
                ease 2.8 yoffset 190
                repeat
    with dissolve

    voice "VA/TORA/Vidius/2B/Vidius_2B_4.mp3"
    vidius "Your daughter is DIFFERENT! She took everything away, not carry it!"

    show vidius:
        parallel:
            pause 0.1
            easein 0.4 xpos 0.28
        parallel:
            block:
                ease 2.8 yoffset 162
                ease 2.8 yoffset 190
                repeat
    show desmond browmad shocked angry:
        parallel:
            easein 0.35 xpos 0.70
        parallel:
            block:
                ease 3.0 yoffset 210
                ease 3.0 yoffset 234
                repeat
    with dissolve

    voice "VA/GARFUNKEL/CH3A/Des10.mp3"
    de "Enough, Vidius!"

    show vidius browmad eyeshocked surprised:
        parallel:
            easein 0.35 xpos 0.34
        parallel:
            block:
                ease 2.8 yoffset 162
                ease 2.8 yoffset 190
                repeat
    show desmond:
        parallel:
            pause 0.1
            easein 0.4 xpos 0.74
        parallel:
            block:
                ease 3.0 yoffset 210
                ease 3.0 yoffset 234
                repeat
    with dissolve

    voice "VA/TORA/Vidius/2B/Vidius_2B_5.mp3"
    vidius "NO! Now Murrayfield makes sense!"

    voice "VA/TORA/Vidius/2B/Vidius_2B_6.mp3"
    vidius "I thought nothing of it because she is YOUR daughter, and you are the ARCHBISHOP—"

    show vidius browmad eyeshocked shockedm:
        parallel:
            easein 0.35 xpos 0.36
        parallel:
            block:
                ease 2.8 yoffset 162
                ease 2.8 yoffset 190
                repeat
    show desmond:
        parallel:
            pause 0.1
            easein 0.4 xpos 0.78
        parallel:
            block:
                ease 3.0 yoffset 210
                ease 3.0 yoffset 234
                repeat
    with dissolve

    voice "VA/TORA/Vidius/2B/Vidius_2B_7.mp3"
    vidius "And then I saw a prisoner—someone we should've purified—get slaughtered on your platform!"

    show desmond browmad shocked stern with dissolve

    voice "VA/GARFUNKEL/CH3A/Des11.mp3"
    de "The knight acted to protect the Saintess! The woman was about to attack!"

    show vidius browmad eyeshocked angry:
        parallel:
            ease 0.12 xoffset 18
            ease 0.35 xoffset 0
        parallel:
            block:
                ease 2.8 yoffset 162
                ease 2.8 yoffset 190
                repeat
    with dissolve

    voice "VA/TORA/Vidius/2B/Vidius_2B_8.mp3"
    vidius "Because her very soul was being DRAGGED OUT!"

    show vidius:
        parallel:
            pause 0.1
            easein 0.4 xpos 0.28
        parallel:
            block:
                ease 2.8 yoffset 162
                ease 2.8 yoffset 190
                repeat
    show desmond browmad shocked grit:
        parallel:
            easein 0.35 xpos 0.70
        parallel:
            block:
                ease 3.0 yoffset 210
                ease 3.0 yoffset 234
                repeat
    with dissolve

    voice "VA/GARFUNKEL/CH3A/Des12.mp3"
    de "A troubled soul resisted grace. It happens!"

    show vidius browmad eyeshocked frown with dissolve

    voice "VA/TORA/Vidius/2B/Vidius_2B_9.mp3"
    vidius "Not in forty years of church records, apparently!"

    show vidius browmad eyeshocked angry:
        parallel:
            block:
                linear 0.04 xoffset -7
                linear 0.04 xoffset 7
                repeat 6
            linear 0.04 xoffset 0
        parallel:
            block:
                ease 2.8 yoffset 162
                ease 2.8 yoffset 190
                repeat
    with dissolve

    voice "VA/TORA/Vidius/2B/Vidius_2B_10.mp3"
    vidius "Show me one chronicle! ONE page where a purified soul called the Saintess a MONSTER!"

    en "Monster."

    en "What a cruel, silly word."

    show vidius:
        parallel:
            pause 0.1
            easein 0.4 xpos 0.26
        parallel:
            block:
                ease 2.8 yoffset 162
                ease 2.8 yoffset 190
                repeat
    show desmond browmad shocked stern:
        parallel:
            easein 0.35 xpos 0.68
        parallel:
            block:
                ease 3.0 yoffset 210
                ease 3.0 yoffset 234
                repeat
    with dissolve

    voice "VA/GARFUNKEL/CH3A/Des13.mp3"
    de "The archives are vast. Had you searched properly—"

    show vidius browmad eyeshocked shockedm:
        parallel:
            easein 0.35 xpos 0.34
        parallel:
            block:
                ease 2.8 yoffset 162
                ease 2.8 yoffset 190
                repeat
    show desmond:
        parallel:
            pause 0.1
            easein 0.4 xpos 0.76
        parallel:
            block:
                ease 3.0 yoffset 210
                ease 3.0 yoffset 234
                repeat
    with dissolve

    voice "VA/TORA/Vidius/2B/Vidius_2B_11.mp3"
    vidius "I SEARCHED EVERY VAULT! Every recorded rite! Not one account resembles the horror happening under your nose!"

    show vidius browmad eyeshocked angry:
        parallel:
            ease 0.12 xoffset 18
            ease 0.35 xoffset 0
        parallel:
            block:
                ease 2.8 yoffset 162
                ease 2.8 yoffset 190
                repeat
    with dissolve

    voice "VA/TORA/Vidius/2B/Vidius_2B_12.mp3"
    vidius "ADMIT IT! Something is dreadfully WRONG with your daughter, and you stood there letting it happen!"

    show desmond browmad shocked grit with dissolve

    voice "VA/GARFUNKEL/CH3A/Des14.mp3"
    de "Lower your voice, Vidius."

    show desmond browmad shocked stern with dissolve

    voice "VA/GARFUNKEL/CH3A/Des15.mp3"
    de "My daughter has saved more souls in one year than any Saintess in a century. The results are undeniable."

    show vidius browmad eyeshocked shockedm:
        parallel:
            easein 0.35 xpos 0.36
        parallel:
            block:
                ease 2.8 yoffset 162
                ease 2.8 yoffset 190
                repeat
    show desmond:
        parallel:
            pause 0.1
            easein 0.4 xpos 0.80
        parallel:
            block:
                ease 3.0 yoffset 210
                ease 3.0 yoffset 234
                repeat
    with dissolve

    voice "VA/TORA/Vidius/2B/Vidius_2B_13.mp3"
    vidius "RESULTS?! A woman lies DEAD!"

    show vidius browmad eyeshocked surprised with dissolve

    voice "VA/TORA/Vidius/2B/Vidius_2B_14.mp3"
    vidius "And her KNIGHT! That mercenary, I saw him standing at the halls one night and he had to force a smile open!"

    show vidius browmad eyeshocked angry with dissolve

    voice "VA/TORA/Vidius/2B/Vidius_2B_15.mp3"
    vidius "Has she used her light on him as well?! Was he emptied?!"

    show desmond browmad shocked angry with dissolve

    voice "VA/GARFUNKEL/CH3A/Des16.mp3"
    de "Sir Therion is bound to his oath. That is all that concerns you."

    show vidius browmad eyeshocked frown:
        parallel:
            ease 0.35 xzoom 1
            ease 1.8 xpos 0.16
        parallel:
            block:
                ease 2.8 yoffset 162
                ease 2.8 yoffset 190
                repeat
    with dissolve

    voice "VA/TORA/Vidius/2B/Vidius_2B_16.mp3"
    vidius "...That's it. I can't let this continue any longer."

    show vidius browmad eyeshocked angry with dissolve

    voice "VA/TORA/Vidius/2B/Vidius_2B_17.mp3"
    vidius "I am riding to the conclave tonight and tell everyone there about what's happening here—"

    show desmond browmad shocked surprised:
        parallel:
            easein 0.9 xpos 0.58
        parallel:
            block:
                ease 3.0 yoffset 210
                ease 3.0 yoffset 234
                repeat
    with dissolve

    voice "VA/GARFUNKEL/CH3A/Des17.mp3"
    de "You would destroy the only thing I have left worth protecting?"

    show vidius browmad eyeshocked angry:
        parallel:
            ease 0.3 xzoom -1
        parallel:
            block:
                ease 2.8 yoffset 162
                ease 2.8 yoffset 190
                repeat
    with dissolve

    voice "VA/TORA/Vidius/2B/Vidius_2B_18.mp3"
    vidius "I would stop you before another body is buried by her!"

    show desmond browmad shocked grit:
        parallel:
            block:
                linear 0.04 xoffset -7
                linear 0.04 xoffset 7
                repeat 6
            linear 0.04 xoffset 0
        parallel:
            block:
                ease 3.0 yoffset 210
                ease 3.0 yoffset 234
                repeat
    with dissolve

    voice "VA/GARFUNKEL/CH3A/Des18.mp3"
    de "She is my daughter, Vidius!"

    show vidius browmad eyeshocked shockedm with dissolve

    voice "VA/TORA/Vidius/2B/Vidius_2B_19.mp3"
    vidius "No. The woman is right. She is a MONSTER—"

    # hide peek_l
    # hide peek_r

    $ no_rollback_scene = False
    $ config.rollback_enabled = True
    $ renpy.block_rollback()

    show desmond:
        parallel:
            easein 0.18 xpos 0.34
        parallel:
            block:
                ease 3.0 yoffset 210
                ease 3.0 yoffset 234
                repeat
    show vidius:
        parallel:
            pause 0.15
            easein 0.2 xpos 0.10 rotate -15
        parallel:
            block:
                ease 2.8 yoffset 162
                ease 2.8 yoffset 190
                repeat
    pause 0.2

    play sound "VA/GARFUNKEL/CH3A/Des19.mp3"
    show red_flash zorder 40:
        alpha 1.0
    with hpunch

    en "Bishop Vidius stops talking."

    hide vidius

    $ renpy.block_rollback()
    $ config.rollback_enabled = False
    $ no_rollback_scene = True

    show bg study_night_dark:
        subpixel True
        xanchor 0.5 yanchor 0.5
        xpos 0.5 ypos 0.5
        zoom 2.1
        blur 10
        matrixcolor TintMatrix("#c24a4a")
        block:
            rotate 0
            linear 90.0 rotate 360
            repeat

    show desmond browsad surprised shocked:
        subpixel True
        xanchor 0.5 yanchor 0.46
        xpos 0.3 ypos 1.6
        zoom 1.3
        xzoom 1
        rotate 0
        alpha 1.0
        xoffset 0
        yoffset 140
        matrixcolor TintMatrix("#e8b4b4")
        block:
            linear 0.07 xoffset -2
            linear 0.07 xoffset 2
            repeat

    show peek_door as peek_l at peek_door_left_wide
    show peek_door as peek_r at peek_door_right_wide
    show red_flash:
        pause 0.2
        linear 0.8 alpha 0.0
    pause 1.0
    hide peek_l
    hide peek_r
    hide red_flash

    voice "VA/GARFUNKEL/CH3A/Des20.mp3"
    de "Haa... Haa..."

    show desmond browsad grit shocked with dissolve

    voice "VA/GARFUNKEL/CH3A/Des21.mp3"
    de "What have I done...? What have I done...?"

    show eva browneutral yandere_sad neutral behind desmond:
        subpixel True
        xanchor 0.5 yanchor 0.12
        xpos 0.56 ypos 0.30
        zoom 0.38
        yoffset 0
        blur 4
        matrixcolor TintMatrix("#e8b4b4")
        alpha 0.0
        parallel:
            ease 1.2 alpha 1.0
        parallel:
            block:
                ease 3.2 yoffset -10
                ease 3.2 yoffset 10
                repeat

    en "Poor Papa. He looks so small kneeling there, hands trembling over the pooling crimson."

    voice "VA/RAKUMAROO/CHAPTER 2B/E50.mp3"
    e "Papa."

    show desmond browsad surprised shocked with dissolve:
        xzoom -1

    voice "VA/GARFUNKEL/CH3A/Des22.mp3"
    de "Eva...!"

    show desmond browsad surprised shocked with dissolve:
        xzoom 1

    voice "VA/GARFUNKEL/CH3A/Des23.mp3"
    de "You shouldn't be here! Go back to bed, darling, please—"

    show eva browneutral yandere_happy smile with dissolve

    voice "VA/RAKUMAROO/CHAPTER 2B/E51.mp3"
    e "It is quite all right. I am here now."

    show eva:
        ease 1.2 ypos 0.32 zoom 0.6 blur 2 yoffset 0

    en "I kneel beside him. The dark stain spreads quickly. I nudge the corner of the velvet rug over it with my slipper so he doesn't have to stare."

    voice "VA/RAKUMAROO/CHAPTER 2B/E52.mp3"
    e "There now. That is much better."

    show desmond browmad surprised shocked with dissolve:
        xzoom -1

    voice "VA/GARFUNKEL/CH3A/Des24.mp3"
    de "Better?! Eva, look at my hands!"

    show eva browneutral yandere_sad neutral with dissolve

    voice "VA/RAKUMAROO/CHAPTER 2B/E53.mp3"
    e "I see."

    show desmond browmad angry shocked with dissolve

    voice "VA/GARFUNKEL/CH3A/Des25.mp3"
    de "We have to stop this!"

    show eva browneutral yandere_happy smile with dissolve

    voice "VA/RAKUMAROO/CHAPTER 2B/E54.mp3"
    e "Stop? Why would we stop?"

    voice "VA/GARFUNKEL/CH3A/Des26.mp3"
    de "The purifications! Look what they're doing to people!"

    voice "VA/GARFUNKEL/CH3A/Des27.mp3"
    de "He was going to the conclave... They would have locked you away forever! I couldn't let them take you—"

    show desmond browsad grit shocked with dissolve

    voice "VA/GARFUNKEL/CH3A/Des28.mp3"
    de "I am a priest, Eva! I am meant to protect—"

    show eva browneutral yandere_happy smile:
        ease 1.2 ypos 0.32 zoom 0.8 blur 1 yoffset 0
    with dissolve

    en "I place a soothing hand upon his shaking shoulder."

    voice "VA/RAKUMAROO/CHAPTER 2B/E55.mp3"
    e "Papa, listen to me."

    voice "VA/RAKUMAROO/CHAPTER 2B/E56.mp3"
    e "I shall fix it. I will refine the rite until it is completely gentle. No more screaming, they won't feel a thing."

    voice "VA/RAKUMAROO/CHAPTER 2B/E57.mp3"
    e "Then no one will ask questions, because everyone will be happy."

    show desmond browmad angry shocked:
        block:
            linear 0.04 xoffset -8
            linear 0.04 xoffset 8
            repeat 6
        block:
            linear 0.07 xoffset -2
            linear 0.07 xoffset 2
            repeat
    with dissolve

    voice "VA/GARFUNKEL/CH3A/Des29.mp3"
    de "Fix it HOW?! It keeps getting worse! Look at Therion! The lad can barely hold his own face together!"

    show eva browhappy yandere_happy smile with dissolve

    voice "VA/RAKUMAROO/CHAPTER 2B/E58.mp3"
    e "Sir Therion is completely devoted to me. His heart is mine, and that is all that matters."

    show desmond browmad grit shocked:
        block:
            linear 0.04 xoffset -8
            linear 0.04 xoffset 8
            repeat 6
        block:
            linear 0.07 xoffset -2
            linear 0.07 xoffset 2
            repeat
    with dissolve

    voice "VA/GARFUNKEL/CH3A/Des30.mp3"
    de "He is BROKEN!"

    show eva browneutral yandere_happy smile with dissolve

    voice "VA/RAKUMAROO/CHAPTER 2B/E59.mp3"
    e "He is safe. He cannot be harmed by feelings anymore. I haven't gotten the light quite right yet, but I will."

    voice "VA/RAKUMAROO/CHAPTER 2B/E60.mp3"
    e "I am the Saintess, Papa! Who better to cure grief forever?"

    show desmond browsad surprised shocked with dissolve

    voice "VA/GARFUNKEL/CH3A/Des31.mp3"
    de "And what if you can't?!"

    voice "VA/RAKUMAROO/CHAPTER 2B/E61.mp3"
    e "Then I shall keep trying until I do."

    show desmond browmad angry shocked:
        block:
            linear 0.04 xoffset -8
            linear 0.04 xoffset 8
            repeat 6
        block:
            linear 0.07 xoffset -2
            linear 0.07 xoffset 2
            repeat
    with dissolve

    voice "VA/GARFUNKEL/CH3A/Des32.mp3"
    de "How many more, Eva?! How many more bodies am I meant to cover for?!"

    show eva browneutral yandere_sad neutral shadow:
        ease 1.2 ypos 0.3 zoom 0.58 blur 1
    with dissolve

    voice "VA/RAKUMAROO/CHAPTER 2B/E62.mp3"
    e "As many as it takes."

    show desmond browsad surprised shocked with dissolve:
        xzoom 1

    voice "VA/GARFUNKEL/CH3A/Des33.mp3"
    de "You can't mean that..."

    show eva browneutral yandere_happy smile with dissolve

    voice "VA/RAKUMAROO/CHAPTER 2B/E63.mp3"
    e "Every Saintess struggled at first! Saint Carvilia lost an entire village before perfecting her grace. These things require practice."

    show desmond browmad angry shocked with dissolve

    voice "VA/GARFUNKEL/CH3A/Des34.mp3"
    de "They didn't leave people EMPTY!"

    voice "VA/RAKUMAROO/CHAPTER 2B/E64.mp3"
    e "They leave people AT EASE. You've seen their smiles, Papa. You've seen how peaceful they look once freed from love and grief."

    show desmond browsad grit shocked with dissolve

    voice "VA/GARFUNKEL/CH3A/Des35.mp3"
    de "They smile because they can't do anything else!"

    en "I consider this for a moment, smiling softly."

    voice "VA/RAKUMAROO/CHAPTER 2B/E65.mp3"
    e "Is that not the sweetest thing?"

    show desmond browsad surprised shocked with dissolve

    voice "VA/GARFUNKEL/CH3A/Des36.mp3"
    de "Eva—"

    voice "VA/RAKUMAROO/CHAPTER 2B/E66.mp3"
    e "Without love, there is no pain when it is lost. I am giving them a world where no one ever cries."

    show desmond browsad grit shocked with dissolve

    voice "VA/GARFUNKEL/CH3A/Des37.mp3"
    de "...Your mother would be heartbroken."

    show eva browmad yandere_sad angry:
        block:
            linear 0.04 xoffset -7
            linear 0.04 xoffset 7
            repeat 6
        linear 0.04 xoffset 0
    with dissolve

    voice "VA/RAKUMAROO/CHAPTER 2B/E67.mp3"
    e "Papa, how dare! She would be PROUD!"

    show desmond browsad surprised shocked with dissolve

    voice "VA/GARFUNKEL/CH3A/Des38.mp3"
    de "Eva—"

    show eva agitated browmad yandere_sad shocked:
        parallel:
            easein 0.08 zoom 0.72
            pause 0.25
            ease 0.6 zoom 0.58
        parallel:
            block:
                linear 0.04 xoffset -10
                linear 0.04 xoffset 10
                repeat 8
            linear 0.04 xoffset 0
    with vpunch

    voice "VA/RAKUMAROO/CHAPTER 2B/E68.mp3"
    e "She would never want us dragged before a conclave! She would want a world free of the agony we suffered when she died!"

    show eva calm browneutral yandere_happy smile with dissolve

    voice "VA/RAKUMAROO/CHAPTER 2B/E69.mp3"
    e "That is what I am building. For her. For everyone."

    en "I have no desire to be cruel. I only wish for the darkness to vanish. All of it. Everywhere."

    en "If a few mishaps occur while I learn, that is simply the cost of a miracle."

    show eva browevil yandere_happy yandereevilsmile noshadow:
        parallel:
            ease 1.6 ypos 0.28 zoom 0.36 blur 3
        parallel:
            ease 1.6 yoffset 0
            block:
                ease 3.2 yoffset -10
                ease 3.2 yoffset 10
                repeat
    with dissolve

    voice "VA/RAKUMAROO/CHAPTER 2B/E70.mp3"
    e "So."

    voice "VA/RAKUMAROO/CHAPTER 2B/E71.mp3"
    e "The stairs, Papa."

    show desmond browsad surprised shocked with dissolve

    voice "VA/GARFUNKEL/CH3A/Des39.mp3"
    de "What?"

    show eva browevil yandere_happy yanderesmug with dissolve

    voice "VA/RAKUMAROO/CHAPTER 2B/E72.mp3"
    e "Bishop Vidius fell down the steep stairs in the east wing. It was dark. Everyone will be so grieved to hear of the accident."

    show desmond browmad surprised shocked with dissolve

    voice "VA/GARFUNKEL/CH3A/Des40.mp3"
    de "You... you've planned this."

    show eva browevil yandere_happy yandereevilsmile with dissolve

    voice "VA/RAKUMAROO/CHAPTER 2B/E73.mp3"
    e "I think of everything, Papa. It is my duty."

    show desmond browsad neutral closed:
        ease 0.6 xoffset 0
    with dissolve

    de "..."

    show desmond browsad neutral normal:
        subpixel True
        xanchor 0.5 yanchor 0.46
        xpos 0.3 ypos 1.6
        zoom 1.3
        xzoom -1
        rotate 0
        alpha 1.0
        xoffset 0
        yoffset 140
        matrixcolor TintMatrix("#e8b4b4")
    with dissolve

    voice "VA/GARFUNKEL/CH3A/Des41.mp3"
    de "Go fetch your knight."

    jump prologue
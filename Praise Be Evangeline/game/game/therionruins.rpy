label therion_ruins:

    scene black
    with fade

    play music "shizumiyukutsuki.mp3"

    $ current_frame = "horror"


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

    tn "Saintess called. When I get in, she's standing over a bloodied Vidius. The archbishop already ran away through the study door like a coward."

    show therion browneutral half smug

    tn "Right. I get it. I've cleaned up messes like this before."

    voice "VA/RAKUMAROO/RUINS/E1.mp3"
    e "Vidius fell, Therion. Down the east stairwell. That is all anyone needs to know. See that it looks that way."

    show therion browneutral half neutral

    voice "VA/JASON/RUINS/R1.mp3"
    t "Yeah, no problem."

    # walks to the body and bends down
    show therion browneutral half smug:
        ease 1.0 xpos 0.40
        ease 0.6 rotate 9 yoffset 150

    tn "Easy. Pick Vidius up, drag the corpse, toss it down the stairs, smash the skull a bit more to match the drop."

    # half lift, Vidius hangs limp
    show vidius browsad eyeclosed frown shadow zorder 3:
        matrixcolor ColorizeMatrix("#152238", "#f4dcb3")
        subpixel True
        transform_anchor True
        zoom 0.2
        anchor (0.5, 0.26)
        xpos 0.5
        ypos 1500
        rotate -14
        easein 0.6 ypos 640 rotate -8
        block:
            ease 1.4 rotate -5
            ease 1.4 rotate -9
            repeat

    show therion browmad open gritannoyed:
        easein 0.6 rotate 3 yoffset 100
        block:
            ease 2.5 yoffset 104
            ease 2.5 yoffset 98
            repeat

    tn "Lift on three. One, two…"

    # everything stops
    show vidius:
        ease 0.3 rotate -7
    show therion browneutral open neutral:
        ease 0.3 yoffset 100

    tn "Wait."

    tn "Vidius's hand."

    # the twitch
    show vidius:
        linear 0.04 xoffset 2
        linear 0.04 xoffset -1
        linear 0.05 xoffset 0
        pause 0.4
        linear 0.03 xoffset 1.5
        linear 0.05 xoffset 0

    tn "The bishop's fucking fingers just twitched."

    show vidius browsad eyenormal frown

    voice "VA/TORA/Vidius/Ruins Ending/Vidius_Ruin_1.mp3"
    vidius "Sss... someone's... still—"

    # Therion nearly drops him
    show therion browmad shook gritangry:
        easeout 0.08 xoffset -14
        easein 0.25 xoffset 0
    show vidius:
        easein 0.1 ypos 690 rotate -12
        easeout 0.25 ypos 650 rotate -7

    tn "Fuck! Fuck! Vidius ain't dead!"

    show therion browskeptical shook frown

    tn "She said Vidius fell. I think the bastard didn't."

    tn "Or maybe Vidius DID fall, but the damn fall didn't finish the job."

    show therion browneutral creepy smug

    tn "Don't care. As long as she's safe, I'd help her murder the whole conclave."

    show eva agitated browsad normal_sad shocked:
        easeout 0.15 yoffset 60
        easein 0.3 yoffset 75

    voice "VA/RAKUMAROO/RUINS/E2.mp3"
    e "Oh. Oh, the bishop is— Therion, set the body down! Gently!"

    # set down, slumped against the floor
    show vidius:
        ease 1.0 ypos 700 rotate -10 xoffset 0
        block:
            linear 0.05 xoffset -1
            linear 0.07 xoffset 1
            linear 0.06 xoffset 0
            pause 0.3
            repeat
    show therion browskeptical half grin:
        ease 1.0 rotate 0 yoffset 70
        block:
            ease 2.5 yoffset 76
            ease 2.5 yoffset 70
            repeat

    voice "VA/JASON/RUINS/R2.mp3"
    t "You want me to just—pop, done, clean? Can make it look like the fall did it."

    # Eva pushes in, Therion steps aside
    show eva agitated browsad yandere_sad what:
        easein 0.4 xpos 0.6 rotate -8 yoffset 120
    show therion browneutral shook neutral:
        easeout 0.4 xpos 0.33

    voice "VA/RAKUMAROO/RUINS/E3.mp3"
    e "No! I can fix this! I can— move, let me—"

    # OPTIONAL: an unstable glow at her hands, flickering
    show expression Solid("#ffe7a0", xysize=(140, 140)) as gold_core zorder 9:
        subpixel True
        anchor (0.5, 0.5)
        pos (1130, 720)
        rotate 45
        blend "add"
        blur 35
        alpha 0.0
        block:
            linear 0.12 alpha 0.45 zoom 1.05
            linear 0.08 alpha 0.15 zoom 0.9
            linear 0.2 alpha 0.55 zoom 1.1
            linear 0.05 alpha 0.1
            pause 0.15
            linear 0.18 alpha 0.4 zoom 1.0
            linear 0.1 alpha 0.2
            repeat
    # shaking hands
    show eva frown:
        block:
            linear 0.05 xoffset -1.5
            linear 0.06 xoffset 1.5
            linear 0.05 xoffset -1
            linear 0.07 xoffset 1
            repeat

    show therion browneutral luvhalf neutral

    tn "Her hands are reaching out, shaking."

    show therion browsad luvhalf frown

    tn "Those hands were always perfect. She seems kinda unsure."

    show vidius agitated browmad eyeshocked shockedm noshadow:
        easein 0.08 xoffset -5 rotate -12
        easeout 0.12 xoffset 3 rotate -9
        easein 0.06 xoffset -4 rotate -11
        ease 0.2 xoffset 0 rotate -10
        block:
            linear 0.05 xoffset -1.5
            linear 0.07 xoffset 1
            linear 0.04 xoffset -1
            linear 0.09 xoffset 1.5
            linear 0.06 xoffset 0
            pause 0.1
            repeat

    voice "VA/TORA/Vidius/Ruins Ending/Vidius_Ruin_2.mp3"
    vidius "No—! Don't let her—!"

    show eva browsad yandere_happy  what

    voice "VA/RAKUMAROO/RUINS/E4.mp3"
    e "Shh. Hold still. I am only going to help."

    show vidius browmad eyeshocked angry

    voice "VA/TORA/Vidius/Ruins Ending/Vidius_Ruin_3.mp3"
    vidius "You! Knight—!"

    show therion browmad half annoyed

    voice "VA/JASON/RUINS/R3.mp3"
    t "Therion, mate. And shut your trap, you're making her nervous."

    # lunges toward Therion
    show vidius:
        easein 0.1 xoffset -18 rotate -14
        easeout 0.2 xoffset -10 rotate -11
        block:
            linear 0.05 xoffset -11.5
            linear 0.07 xoffset -9
            linear 0.04 xoffset -11
            linear 0.09 xoffset -8.5
            linear 0.06 xoffset -10
            pause 0.1
            repeat

    voice "VA/TORA/Vidius/Ruins Ending/Vidius_Ruin_4.mp3"
    vidius "She's USING you! Everything she touches turns to NOTHING!"

    show therion browmad open angry:
        easein 0.1 xoffset 12
        easeout 0.2 xoffset 0

    voice "VA/JASON/RUINS/R4.mp3"
    t "Don't need to hear this bullshit. I already KNOW what her touch does!"

    show therion browneutral luv smile blush

    tn "When she touched me with the light every goddamn voice in my head telling me to tear the world apart just went blank."

    show therion browneutral luv grin blush

    tn "And I fucking love it."

    voice "VA/RAKUMAROO/RUINS/E5.mp3"
    e "Stop squirming! I am trying to HELP you—!"

    # ---- flares gold at first, her usual blocky light ----
    show expression Solid("#fff4cc", xysize=(160, 160)) as gold_core zorder 9:
        subpixel True
        anchor (0.5, 0.5)
        pos (1126, 722)
        rotate 45
        blend "add"
        blur 30
        alpha 0.0
        zoom 0.4
        ease 0.5 alpha 0.8 zoom 1.0
        block:
            ease 0.6 zoom 1.1
            ease 0.6 zoom 0.95
            repeat

    show therion browneutral luvhalf neutral

    tn "The magic flares."

    tn "I know her light better than my own name. White and gold, I've worshipped every spark of it."

    # the gold starts to stutter
    show gold_core:
        subpixel True
        anchor (0.5, 0.5)
        pos (1126, 722)
        blend "add"
        blur 30
        block:
            linear 0.1 alpha 0.3
            linear 0.15 alpha 0.7
            linear 0.05 alpha 0.1
            pause 0.2
            linear 0.1 alpha 0.6
            repeat

    show therion browskeptical open frown

    tn "..."

    tn "Wait a goddamn minute."

    stop music

    play music "audio/void.mp3"
    show gold_core:
        ease 0.4 alpha 0.0 zoom 0.6

    show expression VoidCircle(90, "#5a0000", pad=80) as void_glow zorder 8:
        subpixel True
        anchor (0.5, 0.5)
        pos (1126, 722)
        blur 30
        alpha 0.0
        zoom 0.5
        ease 0.6 alpha 0.7 zoom 1.0
        block:
            ease 0.5 zoom 1.1 alpha 0.8
            ease 0.7 zoom 0.95 alpha 0.6
            repeat

    show expression VoidCircle(46, "#000000", "#8b0f0f", 5) as void_core zorder 9:
        subpixel True
        anchor (0.5, 0.5)
        pos (1126, 722)
        blur 1
        alpha 0.0
        zoom 0.3
        ease 0.5 alpha 1.0 zoom 1.0
        block:
            ease 0.4 zoom 1.08
            ease 0.6 zoom 0.94
            ease 0.3 zoom 1.03
            repeat

    show expression VoidBubbles(count=14, spread=50, rise=190, seed=7) as void_bubbles zorder 10:
        subpixel True
        anchor (0.5, 1.0)
        pos (1126, 722)
        yoffset 40
        alpha 0.0
        ease 0.8 alpha 1.0

    show expression Solid("#3a0d0d") as void_wash zorder 11:
        blend "multiply"
        alpha 0.0
        ease 1.5 alpha 0.5

    # sprites drain toward a sick red-grey

    show vidius:
        parallel:
            ease 1.5 matrixcolor ColorizeMatrix("#0a0203", "#d8c0c0")
        parallel:
            block:
                easein 0.07 xoffset -6 rotate -12
                easeout 0.1 xoffset 4 rotate -8.5
                easein 0.06 xoffset -3 rotate -11
                easeout 0.12 xoffset 5 rotate -9
                repeat
    show therion browneutral shook frown:
        ease 1.5 matrixcolor ColorizeMatrix("#0a0203", "#d8c0c0")
    show eva:
        parallel:
            ease 1.5 matrixcolor ColorizeMatrix("#0a0203", "#d8c0c0")
        parallel:
            block:
                linear 0.05 xoffset -5.5
                linear 0.06 xoffset -2.5
                linear 0.05 xoffset -5
                linear 0.07 xoffset -3
                repeat

    tn "It's black."

    show therion browmad shook gritangry
    show layer master:
        subpixel True
        anchor (0.5, 0.5)
        pos (960, 500)
        zoom 1.7
        linear 0.04 xoffset 6 yoffset -2
        linear 0.04 xoffset -5 yoffset 2
        linear 0.05 xoffset 0 yoffset 0

    tn "WHY IS IT BLACK?!"

    tn "What the FUCK?!"

    play sound "audio/darkmagic.mp3"

    # ---- beam hits: black flash covers the swap to the blood body ----
    show expression Solid("#000000") as void_flash zorder 20:
        alpha 0.95
        linear 0.5 alpha 0.0

    show vidius blood nobrow noeyes nomouth shadow:
        ease 0.1 xoffset 0 rotate -10
        block:
            linear 0.04 xoffset -3 rotate -11.5
            linear 0.04 xoffset 2 rotate -8.5
            linear 0.05 xoffset -2 rotate -11
            linear 0.04 xoffset 3 rotate -9
            repeat

    # front half: hands to his face
    show expression Solid("#6e0808", xysize=(191, 26)) as void_beam_rim zorder 5:
        subpixel True
        transform_anchor True
        anchor (0.0, 0.5)
        pos (1126, 722)
        rotate 197.4
        blur 6
        xzoom 0.0
        easein 0.15 xzoom 1.0
        block:
            linear 0.08 yzoom 1.25
            linear 0.1 yzoom 0.85
            repeat

    show expression Solid("#000000", xysize=(191, 12)) as void_beam zorder 6:
        subpixel True
        transform_anchor True
        anchor (0.0, 0.5)
        pos (1126, 722)
        rotate 197.4
        blur 1
        xzoom 0.0
        easein 0.15 xzoom 1.0
        block:
            linear 0.06 yzoom 1.15
            linear 0.09 yzoom 0.9
            repeat

        # back half: behind his head, through the hole and off screen
    show expression Solid("#6e0808", xysize=(800, 26)) as void_beam_back_rim zorder 2:
        subpixel True
        transform_anchor True
        anchor (0.0, 0.5)
        pos (944, 665)
        rotate 197.4
        blur 6
        xzoom 0.0
        pause 0.15
        easein 0.25 xzoom 1.0
        block:
            linear 0.08 yzoom 1.25
            linear 0.1 yzoom 0.85
            repeat

    show expression Solid("#000000", xysize=(800, 12)) as void_beam_back zorder 2:
        subpixel True
        transform_anchor True
        anchor (0.0, 0.5)
        pos (944, 665)
        rotate 197.4
        blur 1
        xzoom 0.0
        pause 0.15
        easein 0.25 xzoom 1.0
        block:
            linear 0.06 yzoom 1.15
            linear 0.09 yzoom 0.9
            repeat

    # black magic filling the hole from behind
    show expression VoidCircle(90, "#5a0000", pad=70) as void_hole_glow zorder 2:
        subpixel True
        anchor (0.5, 0.5)
        pos (944, 665)
        blur 25
        alpha 0.0
        pause 0.15
        ease 0.3 alpha 0.7
    show expression VoidCircle(32, "#000000", "#8b0f0f", 4) as void_hole zorder 2:
        subpixel True
        anchor (0.5, 0.5)
        pos (944, 665)
        alpha 0.0
        pause 0.15
        linear 0.1 alpha 1.0
        block:
            ease 0.5 zoom 1.1
            ease 0.5 zoom 0.95
            repeat
    show expression VoidBubbles(count=10, spread=16, rise=170, min_r=3, max_r=9, seed=3) as void_leak zorder 2:
        subpixel True
        anchor (0.5, 1.0)
        pos (944, 665)
        yoffset 40

    show layer master:
        subpixel True
        anchor (0.5, 0.5)
        pos (960, 500)
        zoom 1.7
        block:
            linear 0.04 xoffset 10 yoffset -3
            linear 0.04 xoffset -8 yoffset 3
            linear 0.05 xoffset 6 yoffset -2
            linear 0.04 xoffset -5 yoffset 2
            repeat 6
        linear 0.1 xoffset 0 yoffset 0

        # Therion throws himself out of the beam's path
    show therion browsad shook gritannoyed:
        parallel:
            pause 0.08
            easeout 0.32 xpos -0.2
        parallel:
            easein 0.08 yoffset 95
            easeout 0.14 yoffset 10
            easein 0.18 yoffset 70
        parallel:
            easein 0.08 rotate 3
            easeout 0.14 rotate -12
            ease 0.2 rotate -5
        rotate 0

    voice "VA/TORA/Vidius/Ruins Ending/Vidius_Ruin_6.mp3"
    vidius "AAAAAGHHHHHH—!"

    # the beam dies on her "No!"
    show void_beam:
        linear 0.1 alpha 0.0
    show void_beam_rim:
        linear 0.15 alpha 0.0
    show void_beam_back:
        linear 0.1 alpha 0.0
    show void_beam_back_rim:
        linear 0.15 alpha 0.0

    show eva browsad yandere_sad shocked

    voice "VA/RAKUMAROO/RUINS/E6.mp3"
    e "No! That isn't right—!"

    tn "That scream... {w}that ain't human speech. I've heard men die in battles. But this... never heard anything so vile."

    show therion browsad shook frown

    tn "And her light... This ain't my saintess' color."

    # ---- beam cuts out, he goes still ----
    show void_beam:
        linear 0.1 alpha 0.0
    show void_beam_rim:
        linear 0.15 alpha 0.0
    show void_beam_back:
        linear 0.1 alpha 0.0
    show void_beam_back_rim:
        linear 0.15 alpha 0.0

    show vidius:
        ease 0.2 xoffset 0 rotate -10
        pause 0.9
        linear 0.03 xoffset 2
        linear 0.06 xoffset 0

    show therion browmad shook gritangry

    tn "Holy shit."

    tn "The black light just blew a hole through Vidius's head."

    show void_hole:
        ease 0.8 alpha 0.0 zoom 0.4
    show void_hole_glow:
        ease 0.8 alpha 0.0
    show void_leak:
        ease 1.0 alpha 0.0
    show layer master:
        subpixel True
        anchor (0.5, 0.5)
        pos (960, 500)
        zoom 1.7
        xoffset 0
        yoffset 0
        ease 1.2 pos (1011, 20) zoom 3.2

    tn "I can see the floor through HIS GODDAMN SKULL."

    # ---- Eva jerks back, stumbles out toward Therion ----
    show layer master:
        subpixel True
        anchor (0.5, 0.5)
        pos (1011, 20)
        zoom 3.2
        ease 0.6 pos (960, 500) zoom 1.7

    # she recoils and starts to go down
    show eva agitated browsad normal_sad shocked zorder 4:
        easeout 0.12 xoffset 14 rotate 4
        easein 0.4 xpos 0.64 xoffset 0 rotate 9 yoffset 170
        easein 0.25 rotate 13 yoffset 230
        # caught, falls back against him
        easeout 0.2 rotate 10 yoffset 195
        ease 0.5 rotate 8 yoffset 190
        block:
            linear 0.06 xoffset -1.5
            linear 0.08 xoffset 1.5
            repeat

    # Therion dashes in behind her from the left
    show therion browmad shook gritangry:
        xpos -0.2
        xzoom -1
        rotate 0
        yoffset 70
        pause 0.1
        easeout 0.5 xpos 0.7 rotate 6
        xzoom 1
        easein 0.2 rotate -3 yoffset 80
        ease 0.4 rotate 0 yoffset 75
        block:
            ease 2.5 yoffset 80
            ease 2.5 yoffset 75
            repeat

    show void_core:
        ease 0.6 alpha 0.0 zoom 0.4
    show void_glow:
        ease 0.6 alpha 0.0
    show void_bubbles:
        ease 0.8 alpha 0.0

    show vidius:
        ease 0.8 ypos 740 rotate -16

    voice "VA/RAKUMAROO/RUINS/E7.mp3"
    e "... No!"

    # Vidius slides off the bottom of the frame
    show vidius:
        easein 0.5 ypos 1600 rotate -35
    show layer master:
        subpixel True
        anchor (0.5, 0.5)
        pos (960, 500)
        zoom 1.7
        pause 0.4
        linear 0.04 xoffset 5 yoffset 4
        linear 0.05 xoffset -4 yoffset -2
        linear 0.06 xoffset 0 yoffset 0

    show therion browmad creepy gritangry

    tn "I manage to catch her as soon as she fell."

    hide gold_core
    hide void_core
    hide void_glow
    hide void_bubbles
    hide void_beam
    hide void_beam_rim
    hide void_beam_back
    hide void_beam_back_rim
    hide void_hole
    hide void_hole_glow
    hide void_leak
    hide void_flash
    hide vidius

    # Therion helps her up
    show eva agitated browsad yandere_sad what:
        ease 0.9 xpos 0.62 rotate 0 yoffset 75
        block:
            linear 0.05 xoffset -1.5 rotate -0.3
            linear 0.07 xoffset 1.5 rotate 0.3
            linear 0.04 xoffset -1 rotate 0
            linear 0.06 xoffset 1
            repeat
    show therion browmad creepy gritannoyed:
        ease 0.8 rotate 0 yoffset 70
        block:
            linear 0.05 xoffset -1
            linear 0.06 xoffset 1
            linear 0.04 xoffset -0.5
            linear 0.07 xoffset 1
            linear 0.05 xoffset 0
            pause 0.2
            repeat

    tn "I set Vidius down when she told me to, but shit, what the HELL."

    show therion browsad gritannoyed

    tn "My light is beautiful."

    tn "The most beautiful thing in this garbage world, and I'd butcher every priest in this cathedral just to feel it on my skin for one more second."

    show therion browmad gritangry

    tn "That was not the gold."

    tn "That was the same black muck that spills out of the unpurified when I gut them. I know the look, I know the STENCH."

    tn "This time it came from HER."

    show therion browsad gritannoyed

    tn "From my Saintess."

    show therion browmad gritangry

    tn "From MY Evangeline."

    # Therion unsteady on his feet, jitter underneath
    show therion:
        parallel:
            block:
                linear 0.05 xoffset -1
                linear 0.06 xoffset 1
                linear 0.04 xoffset -0.5
                linear 0.07 xoffset 1
                linear 0.05 xoffset 0
                pause 0.2
                repeat

    tn "Fuck. Fuck. Fuck. Fuck."

    tn "My guts are twisting. My instincts are tearing me in half. Part of me wants to kill anything that looks at her funny, but another half of me wants to jump out the window and run till I die."

    show therion browsad gritannoyed

    tn "I'm gonna be sick."

    # Eva screaming: sharp jolts, harder tremble
    show eva browsad yandere_sad shocked:
        # one small flinch as she starts shouting
        easein 0.1 yoffset 71
        ease 0.4 yoffset 75
        parallel:
            # ragged breathing
            block:
                ease 0.7 yoffset 72
                ease 0.9 yoffset 76
                ease 0.5 yoffset 73
                ease 1.1 yoffset 75
                repeat
        parallel:
            # fine tremor with stillness in between
            block:
                linear 0.04 xoffset -0.8
                linear 0.05 xoffset 0.6
                linear 0.04 xoffset -0.4
                linear 0.06 xoffset 0
                pause 0.35
                linear 0.05 xoffset 0.7
                linear 0.04 xoffset -0.5
                linear 0.07 xoffset 0
                pause 0.6
                repeat
    voice "VA/RAKUMAROO/RUINS/E8.mp3"
    e "I did not mean—! My light has never done that before, Therion, I swear to you, it has NEVER—"

    # back to shaking
    show eva browsad yandere_sad frown:
        ease 0.3 xoffset 0 rotate 0
        block:
            linear 0.05 xoffset -1.5 rotate -0.3
            linear 0.07 xoffset 1.5 rotate 0.3
            linear 0.04 xoffset -1 rotate 0
            linear 0.06 xoffset 1
            repeat
    show therion browsad gritannoyed

    voice "VA/JASON/RUINS/R6.mp3"
    t "I know, Saintess. I've been watching."

    show therion browmad gritangry

    tn "Do I? Do I fucking know that?! Five minutes ago the world made sense. Now..."

    show therion browsad gritannoyed
    show eva browsad yandere_sad what

    tn "Now she's staring at black slime on her hands, wiping it on her dress, crying... and I don't know what she is."

    tn "Is she my Saintess? The divine who saved the bird in her hands? The woman I gave my soul to?"

    show therion browmad gritangry

    tn "Or is she a fiend that just melted a person's head?"

    show therion browsad gritannoyed

    voice "VA/JASON/RUINS/R7.mp3"
    t "Man, look at her. She's so scared."

    # push in on the two of them
    show layer master:
        subpixel True
        anchor (0.5, 0.5)
        pos (960, 500)
        zoom 1.7
        ease 2.0 pos (131, 524) zoom 2.7

    tn "I want to hold her 'till she stops shaking."

    show therion browmad gritangry

    tn "I also want to smash my head against the pavement."

    show therion browsad gritannoyed

    tn "I want her magic on me. Silence the noise in my head. But what if the black comes out? What if she touches me and leaves a hole where my face used to be?"

    show therion browneutral gritannoyed

    tn "... But dying in her hands doesn't sound so bad."

    scene black

    with fade

    play music "organ.mp3"

    tn "I got rid of what was left of Vidius. Crushed the remains, dumped the meat, scrubbed the stone."

    tn "Knelt outside her door right after, because that's where I belong. Only place in this godforsaken world that makes any damn sense."

    tn "She didn't open it."

    tn "Tried to hold myself together. Stood guard at dawn. Trailed her down the gallery like I always do..."

    tn "Counting her strides. One, two, three..."

    tn "Fucking lost count at fourteen."

    voice "VA/JASON/RUINS/LOL.mp3"
    t "Heh. Heheheheh."

    tn "Lost count? ME!"

    tn "I once counted her breathing for nine straight hours just to keep my head silent."

    tn "Now I can't."

    tn "My body doesn't want to go near her anymore. I don't know why."

    tn "Maybe the magic she left in me reacted to the magic she now has. I don't understand any of that bullshit."

    tn "She noticed."

    tn "She notices every fucking thing about me. Of course. She's the Saintess. She probably knew I was breaking before I did."

    $ rc_reset()
    $ rc_set("therion", 0.56)
    $ rc_set("eva", -0.2)

    scene bg temple_corridor_night

    # dark overcast, slow drifting flicker
    show rc_overcast zorder 30:
        blend "multiply"
        alpha 0.58
        block:
            ease 4.0 alpha 0.64
            linear 0.12 alpha 0.72
            linear 0.18 alpha 0.62
            ease 5.0 alpha 0.55
            ease 3.0 alpha 0.62
            linear 0.1 alpha 0.69
            linear 0.25 alpha 0.6
            ease 4.5 alpha 0.58
            repeat

    show therion browsad creepy gritannoyed:
        matrixcolor TintMatrix(RC_NIGHT_TINT) * BrightnessMatrix(-0.15)
        subpixel True
        transform_anchor True
        zoom 0.23
        xanchor 0.5
        yanchor 1.0
        yalign 1.0
        yoffset 40
        parallel:
            function rc_ther_tf

    show therion as rc_ther_shadow behind therion:
        subpixel True
        rotate_pad False
        transform_anchor True
        xanchor 0.5
        yanchor 1.0
        ypos RC_WALL_FLOOR
        zoom RC_THER_SHADOW_ZOOM
        blur RC_SHADOW_BLUR
        matrixcolor TintMatrix("#000000")
        alpha 0.0
        function rc_tshadow_tf

    show layer master:
        subpixel True
        anchor (0.5, 0.5)
        pos (960, 540)
        zoom 1.0
        ease 4.0 pos (960, 560) zoom 1.12

    with fade

    # Eva hurries in from the left
    $ rc_path("eva", (0.38, 2.2, "easeout_quad"))

    show eva browneutral yandere_sad neutral:
        matrixcolor TintMatrix(RC_NIGHT_TINT) * BrightnessMatrix(-0.15)
        subpixel True
        transform_anchor True
        xzoom -1
        zoom 0.25
        xanchor 0.5
        yanchor 1.0
        yalign 1.0
        yoffset 40
        parallel:
            function rc_eva_tf
        parallel:
            block:
                ease 2.0 yoffset 24
                ease 2.0 yoffset 40
                repeat

    show eva as rc_eva_shadow behind eva, therion:
        subpixel True
        rotate_pad False
        transform_anchor True
        xanchor 0.5
        yanchor 1.0
        ypos RC_WALL_FLOOR
        zoom RC_EVA_SHADOW_ZOOM
        blur RC_SHADOW_BLUR
        matrixcolor TintMatrix("#000000")
        alpha 0.0
        function rc_eshadow_tf

    tn "I see her coming, 'cause I know the sound of her slippers better than my own name."

    # ---- she shoves him, keeps her hand on his chest ----
    $ rc_path("eva", (0.46, 0.25, "easein"), (0.45, 0.3))
    $ rc_path("therion", (0.60, 0.12, "easeout"), (0.595, 0.35, "easein"), delay=0.2)

    show eva browmad yandere_sad frown
    show therion browmad creepy gritangry:
        pause 0.2
        easeout 0.12 rotate 2
        easein 0.35 rotate 0
    show layer master:
        subpixel True
        anchor (0.5, 0.5)
        pos (960, 560)
        zoom 1.12
        pause 0.25
        linear 0.04 xoffset 5
        linear 0.05 xoffset -4
        linear 0.06 xoffset 0

    tn "She presses her hand flat against my chest."

    show therion browsad creepy gritannoyed

    tn "Yesterday I'd have died for this. Heart stops, I hit the floor, dumbest fucking smile on my face, die a happy man."

    tn "That's what I've wanted since I was nine years old and she tied a silk ribbon around my wrist."

    # skin crawling: subtle tremor from here on
    show therion browmad creepy gritangry:
        parallel:
            function rc_ther_tf
        parallel:
            block:
                linear 0.05 xoffset -0.8
                linear 0.06 xoffset 0.6
                linear 0.05 xoffset 0
                pause 0.4
                linear 0.04 xoffset 0.7
                linear 0.06 xoffset -0.4
                linear 0.05 xoffset 0
                pause 0.7
                repeat

    tn "But now my skin is crawling."

    tn "WHY IS MY SKIN CRAWLING?! She's touching me. She's TOUCHING me! This is the only thing I have ever wanted!"

    show eva browneutral yandere_sad neutral

    voice "VA/RAKUMAROO/RUINS/E9.mp3"
    e "You are avoiding me, Sir Therion."

    show therion browsad creepy gritannoyed

    voice "VA/JASON/RUINS/R8.mp3"
    t "Just tired, Saintess. Rough night n' all."

    show eva browneutral yandere_happy neutral

    voice "VA/RAKUMAROO/RUINS/E10.mp3"
    e "You are never 'just' anything."

    # ---- three steps back, both darken ----
    $ rc_path("therion", (0.635, 0.25, "easein"), (0.635, 0.4), (0.675, 0.25, "easein"), (0.675, 0.4), (0.715, 0.25, "easein"))

    show therion browmad creepy frown:
        parallel:
            function rc_ther_tf
        parallel:
            easein 0.25 yoffset 48
            easeout 0.2 yoffset 40
            pause 0.2
            easein 0.25 yoffset 48
            easeout 0.2 yoffset 40
            pause 0.2
            easein 0.25 yoffset 48
            easeout 0.2 yoffset 40
        parallel:
            ease 2.0 matrixcolor TintMatrix(RC_NIGHT_TINT) * BrightnessMatrix(-0.22)
        parallel:
            block:
                linear 0.05 xoffset -0.8
                linear 0.06 xoffset 0.6
                linear 0.05 xoffset 0
                pause 0.4
                linear 0.04 xoffset 0.7
                linear 0.06 xoffset -0.4
                linear 0.05 xoffset 0
                pause 0.7
                repeat
    show eva browneutral yandere_sad what:
        parallel:
            function rc_eva_tf
        parallel:
            ease 2.0 matrixcolor TintMatrix(RC_NIGHT_TINT) * BrightnessMatrix(-0.22)
        parallel:
            block:
                ease 2.0 yoffset 24
                ease 2.0 yoffset 40
                repeat

    tn "My legs move away before my brain can stop 'em. Three steps back. Correct military distance for a knight and his Saintess, exactly what those bastards beat into us during training."

    show therion browsad creepy gritannoyed

    tn "I've never given a fuck about regulation distance. Not once in my life. Who cares about church manuals when you can stand close enough to smell her?"

    tn "But my body just did it on its own."

    # ---- Eva, one step forward ----
    $ rc_path("eva", (0.51, 0.6))
    show eva browneutral yandere_sad frown

    voice "VA/RAKUMAROO/RUINS/E11.mp3"
    e "Therion. Come back."

    show therion browneutral creepy frown

    voice "VA/JASON/RUINS/R9.mp3"
    t "I am at the proper distance, Saintess."

    show eva browmad yandere_sad what

    voice "VA/RAKUMAROO/RUINS/E12.mp3"
    e "Since when do you care about proper distance?"

    show therion browsad creepy gritannoyed

    voice "VA/JASON/RUINS/R10.mp3"
    t "Since now."

    show eva browmad yandere_sad angry

    voice "VA/RAKUMAROO/RUINS/E13.mp3"
    e "Come. Back. Here."

    # ---- she closes the gap ----
    $ rc_path("eva", (0.60, 1.2))
    show eva browmad yandere_sad frown

    tn "She closes the gap herself. Reaches for my chest again."

    # one fast step back
    $ rc_path("therion", (0.76, 0.18, "easeout"))
    show therion browmad creepy gritangry:
        parallel:
            function rc_ther_tf
        parallel:
            easeout 0.18 yoffset 48
            easein 0.2 yoffset 40
        parallel:
            block:
                linear 0.05 xoffset -0.8
                linear 0.06 xoffset 0.6
                linear 0.05 xoffset 0
                pause 0.4
                linear 0.04 xoffset 0.7
                linear 0.06 xoffset -0.4
                linear 0.05 xoffset 0
                pause 0.7
                repeat

    voice "VA/JASON/RUINS/R11.mp3"
    t "—!"

    tn "Another step backwards."

    show eva browsad yandere_sad what

    voice "VA/RAKUMAROO/RUINS/E14.mp3"
    e "... What are you doing?"

    show therion browsad creepy gritannoyed

    voice "VA/JASON/RUINS/R12.mp3"
    t "I-I don't know, Saintess. Something's wrong with me."

    show eva browsad yandere_sad frown

    voice "VA/RAKUMAROO/RUINS/E15.mp3"
    e "Why are you running away from me?"

    show therion browmad creepy gritangry

    voice "VA/JASON/RUINS/R13.mp3"
    t "I'm not! My body just—"

    show eva browmad yandere_sad shocked

    voice "VA/RAKUMAROO/RUINS/E16.mp3"
    e "Your BODY?"

    # ---- Eva trembles ----
    show eva browmad yandere_sad yanderesmug:
        parallel:
            function rc_eva_tf
        parallel:
            block:
                ease 2.0 yoffset 24
                ease 2.0 yoffset 40
                repeat
        parallel:
            block:
                linear 0.04 xoffset -0.8
                linear 0.05 xoffset 0.6
                linear 0.04 xoffset -0.4
                linear 0.06 xoffset 0
                pause 0.35
                linear 0.05 xoffset 0.7
                linear 0.04 xoffset -0.5
                linear 0.07 xoffset 0
                pause 0.6
                repeat

    voice "VA/RAKUMAROO/RUINS/E17.mp3"
    e "Hah!"

    show eva browmad yandere_sad angry

    voice "VA/RAKUMAROO/RUINS/E18.mp3"
    e "You're lying. You just hate me now!"

    show therion browsad creepy gritangry

    voice "VA/JASON/RUINS/R14.mp3"
    t "No, saintess, please! I want to, I swear I do, but something in me won't let me! My legs have their own ideas and they're all fucking terrible ones—"

    # ---- trembles again, a little harder ----
    show eva browmad yandere_sad yandereevilsmile:
        parallel:
            function rc_eva_tf
        parallel:
            block:
                ease 2.0 yoffset 24
                ease 2.0 yoffset 40
                repeat
        parallel:
            block:
                linear 0.04 xoffset -1.2
                linear 0.05 xoffset 1
                linear 0.04 xoffset -0.6
                linear 0.06 xoffset 0
                pause 0.25
                linear 0.05 xoffset 1
                linear 0.04 xoffset -0.8
                linear 0.07 xoffset 0
                pause 0.4
                repeat

    voice "VA/RAKUMAROO/RUINS/E19.mp3"
    e "Therion, you're mine! You promised!"

    show therion browsad creepy frown

    voice "VA/JASON/RUINS/R15.mp3"
    t "Yes, Saintess."

    voice "VA/RAKUMAROO/RUINS/E21.mp3"
    e "No, you sound like you hate me now!"

    # ---- he moves back again, darker ----
    $ rc_shadow_alpha = 0.65
    $ rc_path("therion", (0.80, 0.25, "easeout"))

    show therion browmad creepy gritannoyed:
        parallel:
            function rc_ther_tf
        parallel:
            easeout 0.25 yoffset 48
            easein 0.2 yoffset 40
        parallel:
            ease 1.5 matrixcolor TintMatrix(RC_NIGHT_TINT) * BrightnessMatrix(-0.3)
        parallel:
            block:
                linear 0.05 xoffset -0.8
                linear 0.06 xoffset 0.6
                linear 0.05 xoffset 0
                pause 0.4
                linear 0.04 xoffset 0.7
                linear 0.06 xoffset -0.4
                linear 0.05 xoffset 0
                pause 0.7
                repeat
    show eva:
        parallel:
            function rc_eva_tf
        parallel:
            ease 1.5 matrixcolor TintMatrix(RC_NIGHT_TINT) * BrightnessMatrix(-0.3)
        parallel:
            block:
                ease 2.0 yoffset 24
                ease 2.0 yoffset 40
                repeat
        parallel:
            block:
                linear 0.04 xoffset -1.2
                linear 0.05 xoffset 1
                linear 0.04 xoffset -0.6
                linear 0.06 xoffset 0
                pause 0.25
                linear 0.05 xoffset 1
                linear 0.04 xoffset -0.8
                linear 0.07 xoffset 0
                pause 0.4
                repeat

    voice "VA/JASON/RUINS/R16.mp3"
    t "I'm trying—"

    show eva browmad yandere_sad angry

    voice "VA/RAKUMAROO/RUINS/E22.mp3"
    e "If you ARE trying then you won't be OVER THERE!"

    voice "VA/RAKUMAROO/RUINS/E23.mp3"
    e "What changed?! Don't you care for me anymore!?"

    # ---- he shakes, the room shakes, shadows climb ----
    $ rc_shadow_alpha = 0.8
    $ rc_shadow_stretch = 1.25

    show therion browmad creepy gritangry:
        parallel:
            function rc_ther_tf
        parallel:
            ease 1.0 matrixcolor TintMatrix(RC_NIGHT_TINT) * BrightnessMatrix(-0.4)
        parallel:
            block:
                linear 0.04 xoffset -1.5
                linear 0.05 xoffset 1.2
                linear 0.04 xoffset -0.8
                linear 0.05 xoffset 1
                linear 0.06 xoffset 0
                pause 0.15
                repeat
    show eva:
        parallel:
            function rc_eva_tf
        parallel:
            ease 1.0 matrixcolor TintMatrix(RC_NIGHT_TINT) * BrightnessMatrix(-0.4)
        parallel:
            block:
                ease 2.0 yoffset 24
                ease 2.0 yoffset 40
                repeat
    show layer master:
        subpixel True
        anchor (0.5, 0.5)
        pos (960, 560)
        zoom 1.12
        block:
            linear 0.05 xoffset 6 yoffset -2
            linear 0.05 xoffset -5 yoffset 2
            linear 0.06 xoffset 3 yoffset -1
            linear 0.06 xoffset -2 yoffset 1
            repeat 3
        linear 0.1 xoffset 0 yoffset 0
    show rc_overcast:
        blend "multiply"
        block:
            ease 3.0 alpha 0.7
            linear 0.12 alpha 0.78
            linear 0.18 alpha 0.68
            ease 4.0 alpha 0.64
            ease 3.0 alpha 0.7
            repeat

    voice "VA/JASON/RUINS/R17.mp3"
    t "Because your light is gone!"

    # she goes completely still
    show eva browneutral yandere_sad shocked:
        parallel:
            function rc_eva_tf
        parallel:
            ease 0.3 xoffset 0
        parallel:
            block:
                ease 2.0 yoffset 24
                ease 2.0 yoffset 40
                repeat

    e "..."

    show eva browmad yandere_sad angry

    voice "VA/RAKUMAROO/RUINS/E24.mp3"
    e "No. My light is NOT gone!"

    show therion browmad creepy gritangry:
        parallel:
            function rc_ther_tf
        parallel:
            block:
                linear 0.05 xoffset -0.8
                linear 0.06 xoffset 0.6
                linear 0.05 xoffset 0
                pause 0.4
                linear 0.04 xoffset 0.7
                linear 0.06 xoffset -0.4
                linear 0.05 xoffset 0
                pause 0.7
                repeat

    voice "VA/JASON/RUINS/R18.mp3"
    t "It is! You laid your hands on Vidius and it came out pitch dark! Then Vidius's whole FACE was—"

    # ---- she stomps ----
    show eva browmad yandere_sad angry:
        parallel:
            function rc_eva_tf
        parallel:
            easein 0.08 yoffset 52
            easeout 0.18 yoffset 38
            easein 0.08 yoffset 52
            ease 0.3 yoffset 40
            block:
                ease 2.0 yoffset 24
                ease 2.0 yoffset 40
                repeat
    show layer master:
        subpixel True
        anchor (0.5, 0.5)
        pos (960, 560)
        zoom 1.12
        pause 0.08
        linear 0.04 yoffset 4
        linear 0.05 yoffset 0
        pause 0.14
        linear 0.04 yoffset 4
        linear 0.05 yoffset 0

    voice "VA/RAKUMAROO/RUINS/E25.mp3"
    e "STOP! I DON'T WANT TO HEAR IT ANYMORE!"

    # ---- she turns and runs off to the left ----
    $ rc_eva_face = 1.0
    $ rc_path("eva", (-0.3, 1.2, "easein"), delay=0.3)
    show eva browsad yandere_sad what

    tn "She turns. Runs. Saintess has never run from a damn thing in her entire life."

    hide eva
    hide rc_eva_shadow

    tn "Now she's running from ME."

    # creepy eyes gone: shocked, sad
    show therion browsad shook frown

    tn "Saintess. My Saintess. My Evangeline."

    tn "What the fuck is wrong with me?"

    tn "I just made the only person who ever silenced the screaming in my head cry, and I can't even chase her because my legs refuse to move in her direction."

    # his shadow climbs, the dark closes in
    $ rc_shadow_alpha = 0.9
    $ rc_shadow_stretch = 1.6

    show therion browsad shook gritannoyed:
        parallel:
            function rc_ther_tf
        parallel:
            ease 3.0 matrixcolor TintMatrix(RC_NIGHT_TINT) * BrightnessMatrix(-0.55)
        parallel:
            block:
                linear 0.04 xoffset -1.2
                linear 0.05 xoffset 1
                linear 0.04 xoffset -0.6
                linear 0.06 xoffset 0
                pause 0.25
                repeat
    show rc_overcast:
        blend "multiply"
        ease 3.0 alpha 0.8
        block:
            ease 3.0 alpha 0.84
            linear 0.1 alpha 0.9
            linear 0.2 alpha 0.8
            ease 3.0 alpha 0.78
            repeat

    tn "Saintess. Saintess. Saintess. Saintess. Evangeline. Evangeline. Evangeline. Eva. Eva. EVA—"

    with fade

    scene black
    with fade

    play music "audio/horror3.mp3"

    tn "Three weeks since the mess with Vidius."

    tn "Three fucking weeks. Every morning I scream at my legs, 'today's the day, you useless bastards'. Today we walk right up to her, stand beside her like we used to."

    tn "Legs tell me to go fuck myself."

    tn "Today's the exact same nightmare."

    # =========================================================
    # SAME CORRIDOR, DIM RED
    # =========================================================
    $ rc_reset()
    $ rc_set("therion", 0.58)
    $ rc_set("eva", 0.42)
    $ rc_shadow_alpha = 0.6

    scene bg temple_corridor_night

    show rc_overcast_red zorder 30:
        blend "multiply"
        alpha 0.42
        block:
            ease 3.5 alpha 0.5
            linear 0.15 alpha 0.6
            linear 0.25 alpha 0.47
            ease 4.0 alpha 0.4
            ease 2.5 alpha 0.48
            linear 0.1 alpha 0.58
            linear 0.3 alpha 0.44
            ease 4.0 alpha 0.42
            repeat

    show therion browsad shook gritannoyed:
        matrixcolor TintMatrix("#c9a0a0") * BrightnessMatrix(-0.12)
        subpixel True
        transform_anchor True
        zoom 0.23
        xanchor 0.5
        yanchor 1.0
        yalign 1.0
        yoffset 40
        parallel:
            function rc_ther_tf

    show therion as rc_ther_shadow behind therion:
        subpixel True
        rotate_pad False
        transform_anchor True
        xanchor 0.5
        yanchor 1.0
        ypos RC_WALL_FLOOR
        zoom RC_THER_SHADOW_ZOOM
        blur RC_SHADOW_BLUR
        matrixcolor TintMatrix("#2e0404")
        alpha 0.0
        function rc_tshadow_tf

    show eva browneutral yandere_happy neutral:
        matrixcolor TintMatrix("#c9a0a0") * BrightnessMatrix(-0.12)
        subpixel True
        transform_anchor True
        xzoom -1
        zoom 0.25
        xanchor 0.5
        yanchor 1.0
        yalign 1.0
        yoffset 40
        parallel:
            function rc_eva_tf
        parallel:
            block:
                ease 2.0 yoffset 24
                ease 2.0 yoffset 40
                repeat

    show eva as rc_eva_shadow behind eva, therion:
        subpixel True
        rotate_pad False
        transform_anchor True
        xanchor 0.5
        yanchor 1.0
        ypos RC_WALL_FLOOR
        zoom RC_EVA_SHADOW_ZOOM
        blur RC_SHADOW_BLUR
        matrixcolor TintMatrix("#2e0404")
        alpha 0.0
        function rc_eshadow_tf

    show layer master:
        subpixel True
        anchor (0.5, 0.5)
        pos (960, 560)
        zoom 1.12
        xoffset 0
        yoffset 0

    with fade

    # ---- Eva pushes into him, he gives ground ----
    $ rc_path("eva", (0.49, 0.3, "easein"))
    $ rc_path("therion", (0.625, 0.15, "easeout"), (0.62, 0.3), delay=0.2)

    show eva browmad yandere_sad frown
    show therion browmad shook gritangry:
        parallel:
            function rc_ther_tf
        parallel:
            pause 0.2
            easeout 0.12 rotate 2
            easein 0.35 rotate 0
        parallel:
            block:
                linear 0.05 xoffset -0.8
                linear 0.06 xoffset 0.6
                linear 0.05 xoffset 0
                pause 0.4
                linear 0.04 xoffset 0.7
                linear 0.06 xoffset -0.4
                linear 0.05 xoffset 0
                pause 0.7
                repeat
    show layer master:
        subpixel True
        anchor (0.5, 0.5)
        pos (960, 560)
        zoom 1.12
        pause 0.25
        linear 0.04 xoffset 4
        linear 0.05 xoffset -3
        linear 0.06 xoffset 0

    show eva browneutral yandere_happy neutral

    voice "VA/RAKUMAROO/RUINS/E26.mp3"
    e "Give me your wrist."

    show therion browsad shook frown

    voice "VA/JASON/RUINS/R19.mp3"
    t "Saintess?"

    show eva browmad yandere_sad angry

    voice "VA/RAKUMAROO/RUINS/E27.mp3"
    e "Your WRIST, Therion. Offer it to me. This instant."

    show therion browneutral shook frown

    tn "Oh."

    tn "I recognize that ribbon. I wore a strip of it on my other arm for five years till the threads rotted through and snapped off during a contract."

    # she draws in close to tie it
    $ rc_path("eva", (0.52, 0.8))
    show eva browneutral yandere_happy neutral

    tn "She loops the silk around my joint, pulls it taut, and ties the other end directly to her own wrist."

    show therion browsad shook gritannoyed

    tn "I test the tension. Fuck me. This thing is reinforced."

    show eva browhappy yandere_happy smile

    voice "VA/RAKUMAROO/RUINS/E28.mp3"
    e "There. Now we are connected again."

    show therion browsad shook frown

    voice "VA/JASON/RUINS/R20.mp3"
    t "Saintess, I—"

    show eva browevil yandere_happy yanderesmug

    voice "VA/RAKUMAROO/RUINS/E29.mp3"
    e "I won't let you run away from me again. Not now. Not EVER."

    # ---- Therion shakes ----
    show therion browsad shook gritannoyed:
        parallel:
            function rc_ther_tf
        parallel:
            block:
                linear 0.04 xoffset -1.2
                linear 0.05 xoffset 1
                linear 0.04 xoffset -0.6
                linear 0.06 xoffset 0
                pause 0.25
                linear 0.05 xoffset 1
                linear 0.04 xoffset -0.8
                linear 0.07 xoffset 0
                pause 0.4
                repeat

    tn "I want to hurl."

    tn "A few years back, if she'd bound us together like this, I'd have thought I died and went to heaven."

    tn "Now I've got her silk tied to my pulse and my stomach is churning like I drank poison."

    scene black
    with fade

    tn "Why."

    tn "WHY THE FUCK CAN'T I JUST BE HAPPY?!"

    # =========================================================
    # BACK TO THE BLUE CORRIDOR
    # =========================================================
    $ rc_reset()
    $ rc_eva_face = 1.0
    $ rc_eflip = 1.0
    $ rc_set("eva", 1.2)
    $ rc_set("therion", 1.42)

    scene bg temple_corridor_night

    show rc_overcast zorder 30:
        blend "multiply"
        alpha 0.58
        block:
            ease 4.0 alpha 0.64
            linear 0.12 alpha 0.72
            linear 0.18 alpha 0.62
            ease 5.0 alpha 0.55
            ease 3.0 alpha 0.62
            linear 0.1 alpha 0.69
            linear 0.25 alpha 0.6
            ease 4.5 alpha 0.58
            repeat

    # Eva walks in from the right, facing left
    show eva browneutral normal_sad neutral:
        matrixcolor TintMatrix(RC_NIGHT_TINT) * BrightnessMatrix(-0.15)
        subpixel True
        transform_anchor True
        xzoom 1
        zoom 0.25
        xanchor 0.5
        yanchor 1.0
        yalign 1.0
        yoffset 40
        parallel:
            function rc_eva_tf
        parallel:
            block:
                ease 2.0 yoffset 24
                ease 2.0 yoffset 40
                repeat

    show eva as rc_eva_shadow behind eva, therion:
        subpixel True
        rotate_pad False
        transform_anchor True
        xanchor 0.5
        yanchor 1.0
        ypos RC_WALL_FLOOR
        zoom RC_EVA_SHADOW_ZOOM
        blur RC_SHADOW_BLUR
        matrixcolor TintMatrix("#000000")
        alpha 0.0
        function rc_eshadow_tf

    # Therion follows: hunched forward, heavy uneven steps
    show therion browneutral creepy frown:
        matrixcolor TintMatrix(RC_NIGHT_TINT) * BrightnessMatrix(-0.2)
        subpixel True
        transform_anchor True
        zoom 0.23
        xanchor 0.5
        yanchor 1.0
        yalign 1.0
        yoffset 55
        rotate -3
        parallel:
            function rc_ther_tf
        parallel:
            block:
                ease 0.45 yoffset 62 rotate -4
                ease 0.5 yoffset 55 rotate -2.5
                ease 0.4 yoffset 63 rotate -3.6
                ease 0.6 yoffset 55 rotate -2.2
                repeat 2
            ease 0.6 yoffset 56 rotate -3
            # standing, a slow unsteady sway
            block:
                ease 2.2 rotate -3.8
                ease 2.6 rotate -2.4
                repeat

    show therion as rc_ther_shadow behind therion:
        subpixel True
        rotate_pad False
        transform_anchor True
        xanchor 0.5
        yanchor 1.0
        ypos RC_WALL_FLOOR
        zoom RC_THER_SHADOW_ZOOM
        blur RC_SHADOW_BLUR
        matrixcolor TintMatrix("#000000")
        alpha 0.0
        function rc_tshadow_tf

    show layer master:
        subpixel True
        anchor (0.5, 0.5)
        pos (960, 560)
        zoom 1.12
        xoffset 0
        yoffset 0

    $ rc_path("eva", (0.40, 4.2, "easeout_quad"))
    $ rc_path("therion", (0.60, 4.6, "easeout_quad"))

    play music "audio/horror2.mp3"

    with fade

    tn "I'm tethered to the Saintess like a goddamn hound. I sit outside her bathing chamber every single morning, 'cause whet else can I do?"

    tn "My head should be ecstatic. She's locked me to her side. I get to sleep at her room. I'm her only guard."

    # he turns away from her
    $ rc_ther_turn = 0.6
    $ rc_ther_face = -1.0

    tn "My flesh feels like it's stripping off muscle by muscle."

    # she turns to look at him
    $ rc_eva_face = -1.0
    show eva browsad yandere_sad what

    voice "VA/RAKUMAROO/RUINS/E30.mp3"
    e "Therion, why are you looking away? Are you disgusted with me?"

    # he forces himself back around, slowly
    $ rc_ther_turn = 1.8
    $ rc_ther_face = 1.0

    tn "I force my neck around. I can manage that much. Barely."

    show eva browhappy normal_happy smile

    voice "VA/RAKUMAROO/RUINS/E31.mp3"
    e "Good, now that is better."

    tn "She smiled."

    tn "I think."

    tn "I don't know, it's so fucking dark now."

    tn "And now my skin is burning so bad I want to tear my own wrist off."

    scene black
    with fade

    play music "audio/horror3.mp3"

    tn "Time... {w}passes."

    tn "Food... {w}dust. Throat... {w}closed."

    tn "Saint... {w}ess. S... {w}S..."

    tn "Cold cold cold cold."

    tn "Brain... {w}blank."

    tn "Word... {w}for thing. Thing... {w}in chest. {w}Gone."

    # =========================================================
    # DAY CORRIDOR, EERILY DARK
    # =========================================================
    $ rc_reset()
    $ rc_set("eva", 0.42)
    $ rc_set("therion", 0.60)
    $ rc_shadow_alpha = 0.6

    scene bg temple_corridor_day

    show rc_overcast zorder 30:
        blend "multiply"
        alpha 0.45
        block:
            ease 4.5 alpha 0.52
            linear 0.12 alpha 0.6
            linear 0.2 alpha 0.5
            ease 5.0 alpha 0.44
            ease 3.5 alpha 0.5
            ease 4.0 alpha 0.45
            repeat

    show eva browneutral yandere_sad frown:
        matrixcolor SaturationMatrix(0.7) * BrightnessMatrix(-0.15)
        subpixel True
        transform_anchor True
        xzoom -1
        zoom 0.25
        xanchor 0.5
        yanchor 1.0
        yalign 1.0
        yoffset 40
        parallel:
            function rc_eva_tf
        parallel:
            block:
                ease 2.0 yoffset 24
                ease 2.0 yoffset 40
                repeat

    show eva as rc_eva_shadow behind eva, therion:
        subpixel True
        rotate_pad False
        transform_anchor True
        xanchor 0.5
        yanchor 1.0
        ypos RC_WALL_FLOOR
        zoom RC_EVA_SHADOW_ZOOM
        blur RC_SHADOW_BLUR
        matrixcolor TintMatrix("#000000")
        alpha 0.0
        function rc_eshadow_tf

    # Therion: hunched, slow uneven sway, face locked
    show therion browsad creepy distort:
        matrixcolor SaturationMatrix(0.7) * BrightnessMatrix(-0.15)
        subpixel True
        transform_anchor True
        zoom 0.23
        xanchor 0.5
        yanchor 1.0
        yalign 1.0
        yoffset 55
        rotate -3
        parallel:
            function rc_ther_tf
        parallel:
            block:
                ease 2.2 rotate -4.2 xoffset -2
                ease 1.7 rotate -2.0 xoffset 1
                ease 2.6 rotate -3.6 xoffset -1
                ease 1.9 rotate -2.4 xoffset 1.5
                repeat

    show therion as rc_ther_shadow behind therion:
        subpixel True
        rotate_pad False
        transform_anchor True
        xanchor 0.5
        yanchor 1.0
        ypos RC_WALL_FLOOR
        zoom RC_THER_SHADOW_ZOOM
        blur RC_SHADOW_BLUR
        matrixcolor TintMatrix("#000000")
        alpha 0.0
        function rc_tshadow_tf

    show layer master:
        subpixel True
        anchor (0.5, 0.5)
        pos (960, 560)
        zoom 1.12
        xoffset 0
        yoffset 0

    with fade

    voice "VA/RAKUMAROO/RUINS/E32.mp3"
    e "Sir Therion. A word, if you please."

    show therion:
        parallel:
            function rc_ther_tf
        parallel:
            easein 0.12 rotate -5 yoffset 58
            linear 0.04 xoffset -1.5
            linear 0.05 xoffset 1.2
            linear 0.04 xoffset -1
            pause 0.08
            linear 0.03 xoffset 1.5 rotate -5.6
            linear 0.05 xoffset -0.8
            linear 0.06 xoffset 0 rotate -4.4
            pause 0.12
            linear 0.04 xoffset -1
            linear 0.05 xoffset 0.6
            linear 0.06 xoffset 0
            ease 0.5 rotate -3 yoffset 55
            block:
                ease 2.2 rotate -4.2 xoffset -2
                ease 1.7 rotate -2.0 xoffset 1
                ease 2.6 rotate -3.6 xoffset -1
                ease 1.9 rotate -2.4 xoffset 1.5
                repeat

    voice "VA/JASON/RUINS/R21.mp3"
    t "Saintess."

    voice "VA/RAKUMAROO/RUINS/E33.mp3"
    e "You have not touched your breakfast in three days."

        # strain, a heavier lurch like a gag
    show therion:
        parallel:
            function rc_ther_tf
        parallel:
            easein 0.1 rotate -6 yoffset 60
            linear 0.04 xoffset 1.2
            linear 0.05 xoffset -1.5
            pause 0.1
            linear 0.04 xoffset 1 rotate -6.5
            linear 0.06 xoffset -0.6
            linear 0.05 xoffset 0 rotate -5
            pause 0.15
            linear 0.03 xoffset -1.2
            linear 0.06 xoffset 0
            ease 0.6 rotate -3 yoffset 55
            block:
                ease 2.2 rotate -4.2 xoffset -2
                ease 1.7 rotate -2.0 xoffset 1
                ease 2.6 rotate -3.6 xoffset -1
                ease 1.9 rotate -2.4 xoffset 1.5
                repeat

    voice "VA/JASON/RUINS/R22.mp3"
    t "Hurl."

    voice "VA/RAKUMAROO/RUINS/E34.mp3"
    e "You have not said anything to me other than a word at a time."

        # strain
    show therion:
        parallel:
            function rc_ther_tf
        parallel:
            easein 0.14 rotate -4.8 yoffset 57
            linear 0.05 xoffset -1.2
            linear 0.04 xoffset 1
            pause 0.12
            linear 0.04 xoffset -1.4 rotate -5.4
            linear 0.05 xoffset 0.7
            linear 0.06 xoffset 0 rotate -4.2
            pause 0.1
            linear 0.04 xoffset 0.8
            linear 0.05 xoffset 0
            ease 0.5 rotate -3 yoffset 55
            block:
                ease 2.2 rotate -4.2 xoffset -2
                ease 1.7 rotate -2.0 xoffset 1
                ease 2.6 rotate -3.6 xoffset -1
                ease 1.9 rotate -2.4 xoffset 1.5
                repeat

    voice "VA/JASON/RUINS/R23.mp3"
    t "Word."

    e "..."

    voice "VA/RAKUMAROO/RUINS/E35.mp3"
    e "No, this won't do. You've changed. You don't love me anymore."

    show eva browneutral yandere_happy yanderesmug

    voice "VA/RAKUMAROO/RUINS/E36.mp3"
    e "…Or perhaps you need to be purified?"

    # his sway gets a faint tremor under it
    show therion:
        parallel:
            function rc_ther_tf
        parallel:
            block:
                ease 2.2 rotate -4.2
                ease 1.7 rotate -2.0
                ease 2.6 rotate -3.6
                ease 1.9 rotate -2.4
                repeat
        parallel:
            block:
                linear 0.05 xoffset -0.8
                linear 0.06 xoffset 0.6
                linear 0.05 xoffset 0
                pause 0.4
                linear 0.04 xoffset 0.7
                linear 0.06 xoffset -0.4
                linear 0.05 xoffset 0
                pause 0.7
                repeat

    tn "No."

    tn "No. No. No. No."

    show eva browhappy yandere_happy yandereevilsmile

    voice "VA/RAKUMAROO/RUINS/E37.mp3"
    e "Yes, yes, that's it! And then you'd be my Therion again."

        # strain, then back to sway with the tremor
    show therion:
        parallel:
            function rc_ther_tf
        parallel:
            easein 0.12 rotate -5.2 yoffset 58
            pause 0.9
            ease 0.5 rotate -3 yoffset 55
            block:
                ease 2.2 rotate -4.2
                ease 1.7 rotate -2.0
                ease 2.6 rotate -3.6
                ease 1.9 rotate -2.4
                repeat
        parallel:
            linear 0.04 xoffset -1.5
            linear 0.05 xoffset 1.2
            linear 0.04 xoffset -1
            pause 0.1
            linear 0.03 xoffset 1.5
            linear 0.05 xoffset -0.8
            linear 0.06 xoffset 0
            pause 0.15
            linear 0.04 xoffset -1
            linear 0.06 xoffset 0
            block:
                linear 0.05 xoffset -0.8
                linear 0.06 xoffset 0.6
                linear 0.05 xoffset 0
                pause 0.4
                linear 0.04 xoffset 0.7
                linear 0.06 xoffset -0.4
                linear 0.05 xoffset 0
                pause 0.7
                repeat

    voice "VA/JASON/RUINS/R24.mp3"
    t "Stop..."

    show eva browsad yandere_happy yanderesmug

    voice "VA/RAKUMAROO/RUINS/E38.mp3"
    e "I promise you this won't hurt. Please know that I'm only doing it because I love you, Therion."

    tn "Love?"

    # =========================================================
    # SHE STEPS IN, THE BLACK LIGHT GATHERS, THE LIGHT FAILS
    # =========================================================
    $ rc_path("eva", (0.46, 0.8))
    $ rc_shadow_alpha = 0.8
    $ rc_shadow_stretch = 1.2

    show eva browevil yandere_happy yandereevilsmile:
        parallel:
            function rc_eva_tf
        parallel:
            ease 1.5 matrixcolor SaturationMatrix(0.45) * BrightnessMatrix(-0.28)
        parallel:
            block:
                ease 2.0 yoffset 24
                ease 2.0 yoffset 40
                repeat

    show therion:
        parallel:
            function rc_ther_tf
        parallel:
            ease 1.5 matrixcolor SaturationMatrix(0.45) * BrightnessMatrix(-0.28)
        parallel:
            block:
                ease 2.2 rotate -4.2
                ease 1.7 rotate -2.0
                ease 2.6 rotate -3.6
                ease 1.9 rotate -2.4
                repeat
        parallel:
            block:
                linear 0.05 xoffset -0.8
                linear 0.06 xoffset 0.6
                linear 0.05 xoffset 0
                pause 0.4
                linear 0.04 xoffset 0.7
                linear 0.06 xoffset -0.4
                linear 0.05 xoffset 0
                pause 0.7
                repeat

    play music "audio/void.mp3"
    show void_glow zorder 8:
        subpixel True
        anchor (0.5, 0.5)
        pos (907, 590)
        blur 30
        alpha 0.0
        zoom 0.5
        pause 0.8
        ease 0.8 alpha 0.7 zoom 1.0
        block:
            ease 0.5 zoom 1.1 alpha 0.8
            ease 0.7 zoom 0.95 alpha 0.6
            repeat

    show void_core zorder 9:
        subpixel True
        anchor (0.5, 0.5)
        pos (907, 590)
        blur 1
        alpha 0.0
        zoom 0.3
        pause 0.8
        ease 0.6 alpha 1.0 zoom 1.0
        block:
            ease 0.4 zoom 1.08
            ease 0.6 zoom 0.94
            ease 0.3 zoom 1.03
            repeat

    show void_bubbles zorder 10:
        subpixel True
        anchor (0.5, 1.0)
        pos (907, 590)
        yoffset 40
        alpha 0.0
        pause 0.8
        ease 1.0 alpha 1.0

    show void_wash zorder 29:
        blend "multiply"
        alpha 0.0
        ease 2.0 alpha 0.4

    # failing-lamp flicker on the overcast
    show rc_overcast:
        blend "multiply"
        block:
            linear 0.08 alpha 0.72
            linear 0.1 alpha 0.55
            pause 0.6
            linear 0.05 alpha 0.8
            linear 0.15 alpha 0.6
            ease 1.2 alpha 0.64
            linear 0.06 alpha 0.78
            linear 0.06 alpha 0.58
            linear 0.05 alpha 0.75
            linear 0.2 alpha 0.6
            ease 1.8 alpha 0.66
            repeat

    # split-second blackouts
    show void_flash as rc_blink zorder 40:
        alpha 0.0
        block:
            pause 2.3
            linear 0.03 alpha 0.85
            pause 0.06
            linear 0.03 alpha 0.0
            pause 0.12
            linear 0.02 alpha 0.6
            linear 0.05 alpha 0.0
            pause 3.1
            linear 0.03 alpha 0.9
            pause 0.1
            linear 0.04 alpha 0.0
            pause 1.4
            repeat

    voice "VA/RAKUMAROO/RUINS/E39.mp3"
    e "Now, don't move. I'm going to fix you in a moment."

    tn "Oh."

    tn "She... fixing... me..."
    play music "audio/horror2.mp3"
    play sound "audio/burst.mp3"
    scene tburst_face at tburst_face_move
    show tburst_blood at tburst_blood_move

    tn "No."

    tn "Tar."

    tn "Black. Black. Black."

    tn "Flesh... melting."

    tn "Pain? Where... is... pain."

    tn "None."

    voice "VA/RAKUMAROO/RUINS/E40.mp3"
    e "Oh no! Therion! WHY!?"

    voice "VA/RAKUMAROO/RUINS/E41.mp3"
    e "This is not supposed to happen!"

    tn "Drip, drip."

    voice "VA/RAKUMAROO/RUINS/E42.mp3"
    e "No, no, no… I just want you to LOVE me again, not this!"

    tn "Fix."

    tn "Void."

    tn "Inside... empty."

    tn "All... dark."

    voice "VA/RAKUMAROO/RUINS/E43.mp3"
    e "Therion, I'm so sorry! I'll fix this. Hold on, please!"

    # A sound from the doorway. A gasp.

    scene evadeath_bg
    show evadeath_eva at evadeath_shake1
    camera at evadeath_cam

    voice "VA/SHINS/CLERGYMAN01_That Black light_03.mp3"

    clergyman "That black light…! That's not the Saintess'!"

    voice "VA/RAKUMAROO/RUINS/E44.mp3"
    e "It is not what it looks like—"

    play music "audio/mob.mp3"
    show evadeath_eva at evadeath_shake2
    show evadeath_hand1 at evadeath_hand1_move
    show evadeath_hand3 at evadeath_hand3_move

    voice "VA/RAKUMAROO/RUINS/E45.mp3"
    e "Do NOT touch me, I am your Saintess, I was ONLY TRYING TO—"

    voice "VA/SOPHIE/Clergywoman1.mp3"

    ansel "THAT WOMAN WAS RIGHT! SHE IS A MONSTER!"

    voice "VA/RAKUMAROO/RUINS/E46.mp3"
    e "I am NOT! LISTEN TO ME—"

    show evadeath_hand2 at evadeath_hand2_move
    show evadeath_hand4 at evadeath_hand4_move

    voice "VA/SHINS/CLERGYMAN02_Get her_02.mp3"
    clergyman "GET HER!"

    voice "VA/RAKUMAROO/RUINS/E47.mp3"
    e "Take your hands off me, I ORDER you to—"

    show evadeath_eva at evadeath_shake3

    voice "VA/RAKUMAROO/RUINS/E49.mp3"
    e "Therion! THERION!"

    voice "VA/RAKUMAROO/RUINS/E50.mp3"
    e "HELP ME! PLEASE!"

    show evadeath_eva at evadeath_shake2

    voice "VA/RAKUMAROO/RUINS/E51.mp3"
    e "I'm so sorry, please don't be mad at me!"

    show evadeath_eva at evadeath_shake3

    voice "VA/RAKUMAROO/RUINS/E52.mp3"
    e "Why aren't you saying anything!? THERION!"

    tn "Eva..."

    voice "VA/SOPHIE/Crowd1.mp3"

    woman "KILL THE FALSE SAINTESS KILL HER!"

    voice "VA/RAKUMAROO/RUINS/E54.mp3"
    e "NO! No, please, I only wanted to fix him, I only ever FIX things, please, PLEASE—"

    voice "VA/RAKUMAROO/RUINS/E55.mp3"
    e "PAPA! PAPA, HELP!"

    voice "VA/GARFUNKEL/RUINS/Des1.mp3"
    de "Stop! STOP RIGHT NOW, she is your Saintess—"

    voice "VA/GARFUNKEL/RUINS/Des4.mp3"
    de "Eva! EVA!"

    voice "VA/RAKUMAROO/RUINS/E55A.mp3"
    e "Papa—!"

    voice "VA/GARFUNKEL/RUINS/Des5.mp3"
    de "EVA! UGH…!"

    # A heavy impact. Bone on stone.
    play sound "audio/bash1.mp3"

    with sshake
    pause 0.2
    play sound "VA/GARFUNKEL/RUINS/DesGurgle.mp3"

    # Silence from Desmond.

    voice "VA/RAKUMAROO/RUINS/E56.mp3"
    e "PAPA!"

    voice "VA/RAKUMAROO/RUINS/E58.mp3"
    e "Papa, get up, please get up, PAPA—"

    show evadeath_eva at evadeath_shake2

    voice "VA/RAKUMAROO/RUINS/E59.mp3"
    e "No no no no no—"

    show evadeath_eva at evadeath_shake3

    voice "VA/RAKUMAROO/RUINS/E60.mp3"
    e "PLEASE! I am the Saintess, I only want to help you people—"

    voice "VA/RAKUMAROO/RUINS/E61.mp3"
    e "Please. PLEASE—"

    voice "VA/RAKUMAROO/RUINS/E62.mp3"
    e "THERION—"

    scene black
    with sshake

    play sound "VA/RAKUMAROO/RUINS/E63.mp3"

    tn "...Ev..a."

    pause 0.8

label epilogueruins:

    scene bg MM2:
        subpixel True
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
        zoom 2.0
        ease 15 zoom 1
    with fade
    play music "MainMenu.mp3"

    narrator "Once upon a time, there lived a maiden in white who loved too fiercely, and in all the wrong ways."

    narrator "Or so the fable goes."

    narrator "The holy books name her the Lost Saintess. They struck her from the choir rolls, painted over her portraits, and set masons to scrape her likeness from every chapel pillar."

    narrator "Her touch brought no salvation, only ruins. From every poor soul that knelt before her, she stole not merely grief, but their tears, their joy, and the very spark of their humanity."

    narrator "She left them smiling like porcelain dolls, and called it holy."

    narrator "It took a full century of patient labor by true Saintesses to undo the ruin her hands had wrought."

    narrator "She and her father perished on the selfsame night. The mob showed no clemency. The Archbishop tried to shield her with his own body, but they tore him away like a dead vine from a wall."

    narrator "Even in death, his fingers remained locked in hers. They had to snap the bones to part them."

    narrator "I think of those broken fingers whenever the chapel bells toll."

    narrator "Of her knight, the monster, almost nothing remains. No tombstone marks his rest, and no ledger remembers the orphan boy he once was."

    narrator "Some say he fled into the wild. Others claim he was already a hollow husk before the mob arrived—that she had reached inside him so often that nothing remained."

    narrator "A dying stable boy once swore he saw a mercenary dragged away in chains, his eyes wide, vacant, and fixed upon the sky."

    narrator "One pale hand reached out toward nothing at all, rigid as iron, refusing to drop."

    narrator "And that, my dear, is why every Saintess learns her sacred vow before her own name."

    narrator "To give everything to her people. To keep nothing for herself."

    narrator "For a Saintess who yields to her own heart will surely bring the darkness down."

    narrator "..."

    $ persistent.main_menu = 2
    $ config.main_menu_music = mm_tracks[2]

    return

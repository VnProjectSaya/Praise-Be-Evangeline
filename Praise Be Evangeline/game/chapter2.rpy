label morning_intrusion:

    scene black
    with fade

    en "The carriage ride back from Murrayfield passes in blissful silence."

    en "Sir Therion was still staring so intently at me when I opened my eyes from my slumber."

    en "He really DID keep his gaze upon me throughout the whole trip, without faltering."

    en "Gracious me, I was so terribly flustered I scarcely knew where to look!"

    $ current_frame = "dream"

    play music "Lovely.mp3"

    pause 0.2

    scene bg temple_hall_day

    show layer master:
        subpixel True
        anchor (0.5, 0.5)
        zoom 1.3
        xpos 620
        ypos 600

    show desmond browmad stern:
        subpixel True
        zoom 0.22
        xanchor 0.5
        yanchor 1.0
        xpos 0.4
        yalign 1.0
        yoffset 50
        xzoom -1
        block:
            ease 3.0 yoffset 55
            ease 3.0 yoffset 45
            repeat
    with fade

    show eva browsad neutral:
        subpixel True
        xzoom 1
        zoom 0.25
        xanchor 0.5
        yanchor 1.0
        yalign 1.0
        xpos 1.25
        yoffset 40
        easein 1.2 xpos 0.65
        block:
            ease 2.0 yoffset 24
            ease 2.0 yoffset 40
            repeat
    show therion body0 browneutral annoyed behind eva:
        subpixel True
        xzoom 1
        zoom 0.23
        xanchor 0.5
        yanchor 1.0
        yalign 1.0
        xpos 1.35
        yoffset 40
        easein 1.2 xpos 0.82

    pause 1.3  

    en "The Archbishop himself meets us at the entry."

    show desmond browmad neutral with dissolve
    pause 0.6

    show desmond browmad stern with dissolve
    pause 0.7


    en "He says that the conclave will view my work favourably, yet he avoids looking at Sir Therion even once."

    show desmond browmad stern:
        subpixel True
        xzoom 1
        easeout 1.2 xpos -0.2

    pause 0.8  

    scene black
    with fade

    $ renpy.pause(0.1, hard=True)

    show bg temple_corridor_day
    $ renpy.pause(0.5, hard=True)

    show eva browsad neutral:
        xzoom -1
        subpixel True
        zoom 0.25
        xanchor 0.5
        yanchor 1.0
        yalign 1.0
        xpos 0.30
        yoffset 40
        block:
            ease 2.0 yoffset 24
            ease 2.0 yoffset 40
            repeat

    show ansel neutral:
        subpixel True
        zoom 0.25
        xanchor 0.5
        yanchor 1.0
        yalign 1.0
        yoffset 40
        xpos 0.78

    $ renpy.pause(0.2, hard=True)

    show temple_corridor_day1 behind eva:
        subpixel True
        xpos 0
        easeout_quad 2.0 xpos -150

    show bg_corridor_loop behind eva:
        subpixel True
        xpos 1920
        easeout_quad 2.0 xpos 1770

    show eva:
        easeout_quad 2.0 xpos 0.40

    show ansel:
        easeout_quad 2.0 xpos 0.58

    $ renpy.pause(2.0, hard=True)

    show eva browneutral neutral:
        xzoom -1
        subpixel True
        zoom 0.25
        xanchor 0.5
        yanchor 1.0
        yalign 1.0
        xpos 0.40
        yoffset 40
        block:
            ease 2.0 yoffset 24
            ease 2.0 yoffset 40
            repeat

    show ansel neutral:
        subpixel True
        zoom 0.25
        xanchor 0.5
        yanchor 1.0
        yalign 1.0
        yoffset 40
        xpos 0.58
    with dissolve

    $ renpy.pause(0.2, hard=True)

    show ansel neutral:
        subpixel True
        zoom 0.25
        xanchor 0.5
        yanchor 1.0
        yalign 1.0
        xpos 0.58
        easeout 0.4 yoffset 65   # Dips down into a bow
        easein 0.4 yoffset 40    # Rises back up

    $ renpy.pause(0.8, hard=True)
    show eva browneutral neutral with dissolve

    show eva browneutral neutral with dissolve

    en "Within a week, I cannot cross the south gallery without a cleric pausing to bless my name."

    pause 0.5

    show eva:
        easeout 5 xpos 1.3

    show ansel:
        easeout 5 xpos -0.3

    pause 0.3

    scene black
    with Fade(1.0, 0.5, 1.0)

    pause 0.5

    en "How delightful it is, to be adored by so many people!"

    pause 2.0


    stop music
    pause 0.1 
    voice "VA/JASON/Therion39.mp3"


    t "Mornin', Saintess."

# 1. INITIAL STATE: Closed/Normal mouth (MOUTH1) with heavy blur
    show therion_base at therion_fit, therion_blur(90.0) as therion_pov
    show therion_mouth1 at therion_fit, therion_blur(90.0) as therion_mouth
    $ renpy.pause(0.5, hard=True)

    # 2. BLINK 1 (FAST): Close eyes dark
    show therion_blink_dark as therion_pov
    show therion_blink_dark as therion_mouth
    with eye_close_wipe
    $ renpy.pause(0.04, hard=True)

    # Reopen sharper — still holding normal mouth (MOUTH1)
    show therion_base at therion_fit, therion_blur(60.0) as therion_pov
    show therion_mouth1 at therion_fit, therion_blur(60.0) as therion_mouth
    with eye_open_wipe
    $ renpy.pause(0.25, hard=True)

    # 3. BLINK 2 (FASTEST): Close eyes dark right before jumpscare
    show therion_blink_dark as therion_pov
    show therion_blink_dark as therion_mouth
    with eye_close_wipe
    $ renpy.pause(0.04, hard=True)

    # 4. SNAP REVEAL: Crisp image + Mouth rips open from MOUTH1 -> MOUTH2 -> MOUTH3
    show therion_base at therion_fit, therion_jumpscare as therion_pov:
        blur None

    show therion_mouth_jumpscare at therion_fit, therion_jumpscare as therion_mouth:
        blur None

    show therion_creepy_eyes at therion_fit, therion_jumpscare
    show therion_flash as therion_flash
    with eye_open_wipe
    

    play sound "audio/bam.mp3"

    with sshake

    $ renpy.pause(0.5, hard=True)

    $ current_frame = "twisted"

    play music "seijaku1.mp3"

    en "I wake to find him right in front of my face, close enough that I feel his breath before I hear his voice."

    voice "VA/RAKUMAROO/Chapter 2A/Ch2A_Eva01.mp3"
    e "THERION!"

    with vpunch

    voice "VA/JASON/Therion40.mp3"
    t "Hey, calm down. It's just me~"

    voice "VA/RAKUMAROO/Chapter 2A/Ch2A_Eva02.mp3"
    e "What are you doing in my chambers!?"

    voice "VA/JASON/Therion41.mp3"
    t "Heard your breathing go funny in your sleep. Bad dream?"

    scene bg eva_bedroom_day:
        subpixel True
        anchor (0.5, 0.5)
        zoom 1.5
        xpos 0.5
        ypos 0.5
    with fade

    show eva browneutral normal_sad what shadow:
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

    show therion browneutral smug shook behind eva:
        subpixel True
        zoom 0.58
        xanchor 0.5
        yanchor 1.0
        xpos 0.70
        yalign 1.0
        yoffset 1000
    with dissolve

    voice "VA/RAKUMAROO/Chapter 2A/Ch2A_Eva03.mp3"
    e "I... I cannot recall my dreams. How long have you been standing there?"

    voice "VA/JASON/Therion42.mp3"
    t "Picked the lock at midnight. Had to be standing right here in case you needed me."

    show eva browneutral normal_sad frown shadow with dissolve

    voice "VA/RAKUMAROO/Chapter 2A/Ch2A_Eva04.mp3"
    e "Midnight! That is seven whole hours, Sir Therion!"

    voice "VA/JASON/Therion43.mp3"
    t "Six and a half. You turned over at four and your hand fell out from under the quilt."

    show therion browneutral annoyed shook with dissolve

    voice "VA/JASON/Therion44.mp3"
    t "Gahh~ I wanted to hold it. But I am a man of my oath, restraint and all that."

    show eva browneutral normal_sad what shadow with dissolve

    voice "VA/RAKUMAROO/Chapter 2A/Ch2A_Eva05.mp3"
    e "I— well, really—"

    show therion browneutral grin shook with dissolve

    voice "VA/JASON/Therion45.mp3"
    t "So watching you is enough for me. Heheh."

    en "Well, he looks like he wanted to consume me but I admire the restraint!"

    voice "VA/RAKUMAROO/Chapter 2A/Ch2A_Eva06.mp3"
    e "You stood guard the entire night?"

    show therion browneutral smug shook with dissolve

    voice "VA/JASON/Therion46.mp3"
    t "Told you I would, didn't I?"

    en "I hardly know how to respond. The histories do mention knights who watched their Saintesses through the night. I have never imagined what it might feel like to be on the receiving end."

    show eva browneutral normal_sad frown shadow with dissolve

    voice "VA/RAKUMAROO/Chapter 2A/Ch2A_Eva07.mp3"
    e "You... could have simply knocked on the door."

    show therion browmad gritangry shook with dissolve

    voice "VA/JASON/Therion47.mp3"
    t "And if you didn't answer? What if some bastard got in first and I'm standing outside a locked room like a damn fool?"

    en "He has a point."

    stop music fadeout 1.0
    $ current_frame = "dream"
    show eva browsad normal_sad neutral noshadow with dissolve

    voice "VA/RAKUMAROO/Chapter 2A/Ch2A_Eva08.mp3"
    e "Did you sleep at all?"

    play music "utsuriyukujidai.mp3"

    show therion browneutral annoyed half with dissolve

    voice "VA/JASON/Therion48.mp3"
    t "Nope."

    voice "VA/RAKUMAROO/Chapter 2A/Ch2A_Eva09.mp3"
    e "Have you fed yourself?"

    show therion browneutral smug half with dissolve

    voice "VA/JASON/Therion49.mp3"
    t "Nnnope."

    show eva browneutral normal_happy smile with dissolve

    voice "VA/RAKUMAROO/Chapter 2A/Ch2A_Eva10.mp3"
    e "Well, as I am awake and unharmed now, you may go and fetch some breakfast."

    show therion browmad frown open with dissolve

    voice "VA/JASON/Therion50.mp3"
    t "Go where?"

    show eva browhappy closed_happy with dissolve

    voice "VA/RAKUMAROO/Chapter 2A/Ch2A_Eva11.mp3"
    e "The kitchens, naturally!"

    show therion browsad frown half with dissolve

    voice "VA/JASON/Therion51.mp3"
    t "But I can't see you from the kitchens. Too far."

    show eva browmad normal_sad neutral with dissolve

    voice "VA/RAKUMAROO/Chapter 2A/Ch2A_Eva12.mp3"
    e "Therion."

    show therion browneutral smile open with dissolve

    voice "VA/JASON/Therion52.mp3"
    t "My lady?"

    show eva browmad normal_sad angry with dissolve

    voice "VA/RAKUMAROO/Chapter 2A/Ch2A_Eva13.mp3"
    e "Out. Eat. I shall still be alive upon your return, you have my word as Saintess."

    show therion browskeptical annoyed half with dissolve

    voice "VA/JASON/Therion53.mp3"
    t "Your word?"

    show eva browhappy normal_happy smile with dissolve

    voice "VA/RAKUMAROO/Chapter 2A/Ch2A_Eva14.mp3"
    e "Mmhm. My solemn, unbreakable word."

    show therion browmad gritannoyed shook  with dissolve

    voice "VA/JASON/Therion54.mp3"
    t "If you're wrong about that, I'll burn this whole temple to the foundation stone."

    show eva browsad closed_happy shocked with dissolve

    voice "VA/RAKUMAROO/Chapter 2A/Ch2A_Eva15.mp3"
    e "Oh, surely you jest!"

    voice "VA/JASON/Therion55.mp3"
    t "... Do I look like I'm joking?"

    show eva browsad normal_sad frown with dissolve

    voice "VA/RAKUMAROO/Chapter 2A/Ch2A_Eva16.mp3"
    e "Oh dear."

    show eva browneutral normal_happy smile with dissolve

    voice "VA/RAKUMAROO/Chapter 2A/Ch2A_Eva17.mp3"
    e "Think of it this way. A starving knight cannot protect anyone, can he? What good are you to me fainting in the corridor?"

    show therion browmad annoyed open with dissolve

    voice "VA/JASON/Therion56.mp3"
    t "I will not faint."

    play sound "audio/tummy.mp3"

    with sshake

    show therion browsad frown half blush with dissolve

    t "..."

    show eva browhappy normal_happy laugh with dissolve

    voice "VA/RAKUMAROO/Chapter 2A/Ch2A_Eva18.mp3"
    e "...Hah!"

    voice "VA/RAKUMAROO/Chapter 2A/Ch2A_Eva19.mp3"
    e "See? Your stomach has just told me it is clearly hungry!"

    show therion browmad annoyed half with dissolve

    voice "VA/JASON/Therion57.mp3"
    t "Tch."

    voice "VA/JASON/Therion58.mp3"
    t "Alright, alright. I'm going."

    show therion:
        subpixel True
        easeout 4.0 xpos 1.25 yoffset 1080 alpha 0.0

    pause 4.0
    hide therion

    en "He leaves very slowly, stepping backward the way he always does."

    show eva browsad normal_happy frown with dissolve

    en "I shall have to mention to the Archbishop that Sir Therion requires a proper schedule. A knight who does not eat or sleep will wear himself to nothing, and then where should I be?"

    en "I DO appreciate that his mind is completely focused on me, but still...!"

    scene black
    with fade

    en "Thankfully, he obeys long enough to feed himself, though he returns to his post immediately after."

    en "The days that follow are blissfully uneventful, allowing me to savour my growing standing within the cathedral."

    scene bg temple_corridor_day:
        subpixel True
        blur 13
        zoom 1.35
    with dissolve

    show therion body0 hair2 frown at center:
        subpixel True
        zoom 0.38
        xoffset 280
        yoffset 600
        blur 12

    show eva normal_sad neutral noshadow at center:
        subpixel True
        zoom 0.62
        xoffset -180
        yoffset 800
    with dissolve

    en "I spend my mornings conducting purification rites in the sanctuary, laying hands upon the afflicted while Therion watches from the shadows like a hawk."

    
    en "In the end, they are all smiling widely as they walk home."

    show eva closed_happy neutral noshadow at center:
        subpixel True
        zoom 0.62
        xzoom -1
        xoffset -180
        yoffset 800
    with dissolve


    show ansel neutral:
        subpixel True                       
        zoom 0.72
        xanchor 0.5 yanchor 1.0
        xpos 0.7 ypos 1.7
        yoffset 400
        blur 3.0
        matrixcolor BrightnessMatrix(-1.0)  
    with dissolve

    # Evangeline softens her look for the afflicted
    show eva browhappy smile with dissolve


    en "The rest of my hours pass in a pleasant blur of formal prayers, receiving adoring clerics, tending to the floral offerings left at the altar, and so on and so forth."

    scene black
    
    with dissolve

    stop music fadeout 1.0
    
    en "By dusk, my duties draw to a close, as I am now thoroughly exhausted yet delightfully fulfilled."

    play music "desmond.mp3"

    scene bg temple_hall_night_warm

    # 1. Vidius flies in to far-left (xpos -0.35 -> 0.22)
    

    # 2. Desmond flies in to mid-left (xpos -0.15 -> 0.38)
    show desmond browmad stern:
        subpixel True
        xzoom -1
        zoom 0.23
        xanchor 0.5 yanchor 1.0
        xpos -0.15 yalign 1.0
        yoffset 170
        alpha 0.0
        rotate -15
        matrixcolor TintMatrix("#a88870")
        easein 3.0 xpos 0.38 alpha 1.0 rotate 0
        block:
            ease 3.0 yoffset 160
            ease 3.0 yoffset 184
            repeat
    show vidius browneutral smile:
        xzoom -1
        subpixel True
        zoom 0.20
        xanchor 0.5 yanchor 1.0
        xpos -0.35 yalign 1.0
        yoffset 130
        alpha 0.0
        rotate -12
        matrixcolor TintMatrix("#a88870")
        easein 3.2 xpos 0.22 alpha 1.0 rotate 0
        block:
            ease 2.8 yoffset 120
            ease 2.8 yoffset 140
            repeat

    # 3. Eva fixed on the right side, left of Therion (xpos 0.68)
    show eva browneutral:
        subpixel True
        zoom 0.25
        xanchor 0.5 yanchor 1.0
        xpos 0.68 yalign 1.0
        yoffset 40
        matrixcolor TintMatrix("#a88870")
        block:
            ease 2.0 yoffset 24
            ease 2.0 yoffset 40
            repeat

    # 4. Therion fixed on the far-right (xpos 0.82)
    show therion body0 browneutral frown open behind eva:
        subpixel True
        zoom 0.25
        xanchor 0.5 yanchor 1.0
        xpos 0.82 yalign 1.0
        yoffset 40
        matrixcolor TintMatrix("#a88870")
    with dissolve

    pause 3.2

    # Eva reacts as they arrive
    show eva normal_happy what:
        subpixel True
        zoom 0.25
        xanchor 0.5 yanchor 1.0
        xpos 0.68 yalign 1.0
        yoffset 40
        matrixcolor TintMatrix("#a88870")
        block:
            ease 2.0 yoffset 24
            ease 2.0 yoffset 40
            repeat
    pause 1.0

    show layer master:
        subpixel True
        anchor (0.5, 0.5)
        pos (960, 540)
        zoom 1.0
        pause 0.5
        ease 3.0 zoom 1.22 xpos 920 ypos 540

    en "That brief peace is broken, however, on an evening during the Archbishop's inspection, just as I prepare to retire to my chambers."

    en "Standing beside him is a guest I have not seen before."


    show desmond browmad stern normal with dissolve

    voice "VA/GARFUNKEL/CH2A/Des1.mp3"
    de "Saintess. A word."

    voice "VA/GARFUNKEL/CH2A/Des2.mp3"
    de "This is Bishop Vidius, representing the eastern chapter. Bishop Vidius is visiting to observe cathedral protocol for the season."

    show eva browhappy normal_happy smile blush with dissolve

    voice "VA/RAKUMAROO/Chapter 2A/Ch2A_Eva20.mp3"
    e "Bishop! What a pleasure. I hope the eastern province speaks favorably of our work?"

    
    voice "VA/TORA/Vidius/2A/Vidius_2A_1.mp3"
    vidius "Exceedingly so, Saintess. Reports of your miraculous touch reached the chapter house, though seeing the documented numbers truly compels belief."

    voice "VA/RAKUMAROO/Chapter 2A/Ch2A_Eva21.mp3"
    e "Gracious, Bishop! You shall make me terribly full of myself."

    show eva browhappy normal_happy neutral blush with dissolve

    en "The eastern province is terribly far away... To think they speak of me there!"

    en "I can feel myself blushing furiously. I am not at all accustomed to being known so far abroad!"

    show desmond browmad angry normal with dissolve

    voice "VA/GARFUNKEL/CH2A/Des3.mp3"
    de "Sir Therion. Dismissed. We wish to speak to the saintess alone."

    show therion browmad annoyed open with dissolve

    voice "VA/JASON/Therion59.mp3"
    t "I'm fine right here."

    show desmond browmad angry shocked with dissolve

    voice "VA/GARFUNKEL/CH2A/Des4.mp3"
    de "That was an order, boy."

    show therion browmad gritangry open with dissolve

    voice "VA/JASON/Therion60.mp3"
    t "Not moving away, Archbishop."

    show desmond agitated browmad angry shocked with hpunch:
        ease 0.1 xoffset 30
        block:
            ease 3.0 yoffset 160
            ease 3.0 yoffset 184
            repeat

    voice "VA/GARFUNKEL/CH2A/Des5.mp3"
    de "You insolent—!"

    show eva browsad normal_sad shocked with dissolve

    en "Oh no, the Archbishop appears ready to strike him down...! What if Therion gets demoted?"

    show eva browsad normal_sad what with dissolve

    voice "VA/RAKUMAROO/Chapter 2A/Ch2A_Eva22.mp3"
    e "Pray, calm yourself, Archbishop! Sir Therion is sworn to guard my person. I could not possibly ask my defender to violate his sacred duty."

    show desmond browneutral neutral closed with dissolve

    de "..."

    show desmond browmad stern normal with dissolve

    voice "VA/GARFUNKEL/CH2A/Des6.mp3"
    de "As long as the brute holds his tongue."

    show therion browneutral neutral open with dissolve

    voice "VA/JASON/Therion61.mp3"
    t "So be it."

    show vidius browneutral neutral normal with dissolve


    voice "VA/TORA/Vidius/2A/Vidius_2AAdd_1.mp3"
    vidius "I would like to ask something from you, Saintess. About the village you purified."

    voice "VA/TORA/Vidius/2A/Vidius_2AAdd_2.mp3"
    vidius "On my way here, I stopped by Murrayfield to ask for directions..."

    show vidius browsad frown normal with dissolve

    voice "VA/TORA/Vidius/2A/Vidius_2AAdd_3.mp3"
    vidius "But not a single soul answered me."

    show vidius browmad eyeshocked frown with dissolve

    voice "VA/TORA/Vidius/2A/Vidius_2A_2.mp3"
    vidius "Purifications have been witnessed many times over, Saintess. Yet a village turning completely silent afterward remains unheard of."

    show desmond browneutral smile normal with dissolve

    voice "VA/GARFUNKEL/CH2A/Des7.mp3"
    de "The Saintess's methods are thoroughly effective. That is precisely the purpose of sending such talent, is it not?"

    show vidius browneutral smile normal with dissolve

    voice "VA/TORA/Vidius/2A/Vidius_2A_3.mp3"
    vidius "Indeed. Apologies for the intrusion, Saintess."

    show eva browhappy normal_happy smile with dissolve

    voice "VA/RAKUMAROO/Chapter 2A/Ch2A_Eva23.mp3"
    e "Think nothing of it, Bishop Vidius."

    en "If the people are silent, then they must be perfectly happy. No one is shedding a tear or causing a disturbance."

    en "Whatever could he possibly find amiss amidst such absolute peace?"

    show desmond browneutral neutral normal with dissolve

    voice "VA/GARFUNKEL/CH2A/Des8.mp3"
    de "Bishop Vidius will observe several purifications this term. Ensure the schedule accommodates the visit."

    voice "VA/RAKUMAROO/Chapter 2A/Ch2A_Eva24.mp3"
    e "Of course, Archbishop. I shall be so very pleased for the company."

    voice "VA/GARFUNKEL/CH2A/Des9.mp3"
    de "Allow an escort to guide our guest to the east wing."

    show eva browneutral normal_sad what with dissolve

    # 2. Vidius turns left, tilts, and flies out first
    show vidius browneutral smile normal:
        subpixel True
        xzoom 1                          # Turn facing left
        ease 0.3 rotate -2              # Tilt into departure stride
        easeout 2.5 xpos -0.40 alpha 0.0 # Fly offscreen left

    # 3. Desmond turns left, tilts, and follows behind Vidius
    show desmond browneutral neutral normal:
        subpixel True
        xzoom 1                          # Turn facing left
        pause 0.1                        # Stagger behind Vidius
        ease 0.3 rotate -2             # Tilt into flight angle
        easeout 2.4 xpos -0.25 alpha 0.0 # Exit left behind Vidius

    # 4. Eva and Therion move slightly toward center (xpos 0.54 and 0.70)
    show eva browneutral normal_sad what:
        subpixel True
        zoom 0.25
        xanchor 0.5 yanchor 1.0
        matrixcolor TintMatrix("#a88870")
        easeout 2.5 xpos 0.54 yalign 1.0
        block:
            ease 2.0 yoffset 24
            ease 2.0 yoffset 40
            repeat

    show therion body0 browneutral frown open behind eva:
        subpixel True
        zoom 0.25
        xanchor 0.5 yanchor 1.0
        matrixcolor TintMatrix("#a88870")
        easeout 2.5 xpos 0.70 yalign 1.0
    # 5. Camera transitions smoothly from (xpos 920) rightward toward Eva & Therion
    show layer master:
        subpixel True
        anchor (0.5, 0.5)
        pos (960, 540)
        ease 2.5 zoom 1.38 xpos 780 ypos 540

    # Wait for movement and camera pan to finish
    $ renpy.pause(2.5, hard=True)

    hide desmond
    hide vidius

    en "Off they go."
    
    en "As he calls for a guide, I can see the Archbishop's hand resting upon Bishop Vidius's shoulder a touch firmer than simple etiquette requires."

    en "The Archbishop never offers physical gestures. How very curious."

    show eva browhappy normal_happy smile with dissolve

    en "Alas, that is church politics for you! Dreadfully tedious affairs, not for a Saintess to bother with, I suppose."

    show eva browneutral normal_sad what:
        ease 0.3 xzoom -1 xoffset -30
        block:
            ease 2.0 yoffset 24
            ease 2.0 yoffset 40
            repeat

    voice "VA/RAKUMAROO/Chapter 2A/Ch2A_Eva25.mp3"
    e "Therion, be a darling and fetch me a bite to eat?"

    voice "VA/RAKUMAROO/Chapter 2A/Ch2A_Eva26.mp3"
    e "Deliver it to my bedchamber, I am retiring there now."

    show therion browneutral smile open with dissolve

    voice "VA/JASON/Therion62.mp3"
    t "On it, Saintess. Back in a flash."

    scene black
    with fade

   
# 1. Base Night Scene Setup
    show bg temple_corridor_night
    en "Ooh, these cold passages are remarkably frightening without Sir Therion by my side."

    en "To think I already feel so helplessly vulnerable the very moment we are parted!"
    $ renpy.pause(0.5, hard=True)

    # 2. Faceless Knight and Caelor facing each other on the left
    # Knight on far-left (xzoom 1: facing right), Caelor on his right (xzoom -1: facing left)
    show faceless_knight:
        subpixel True
        xzoom -1                          # Facing right toward Caelor
        zoom 0.25
        xanchor 0.5 yanchor 1.0 ypos 1.0
        xpos 0.22 yoffset 40
        matrixcolor TintMatrix("#5a7099")

    show caelor smile:
        subpixel True                    # Facing left toward Knight
        zoom 0.25
        xanchor 0.5 yanchor 1.0 ypos 1.0
        xpos 0.36 yoffset 40
        matrixcolor TintMatrix("#5a7099")

    # 3. Eva starts on the right side (xzoom -1: facing left)
    show eva browsad neutral:
        subpixel True                    # Facing left toward Caelor
        zoom 0.25
        xanchor 0.5 yanchor 1.0 ypos 1.0
        xpos 0.82 yoffset 40
        matrixcolor TintMatrix("#5a7099")
        block:
            ease 2.0 yoffset 24
            ease 2.0 yoffset 40
            repeat
    with fade

    $ renpy.pause(1.0, hard=True)

    # ============================================================
    # MOTION: KNIGHT LEAVES LEFT / EVA WALKS LEFT TO CAELOR
    # ============================================================

    $ quick_menu = False

    # Knight turns left and exits to the left wing
    show faceless_knight:
        xzoom 1                        # Turn around to face left
        easeout 2.0 xpos -0.20 alpha 0.0

    # Background parallax loop sits BEHIND ALL CHARACTERS
    show temple_corridor_night1 behind faceless_knight:
        subpixel True
        xpos 0
        easeout_quad 2.5 xpos 200

    show bg_corridor_loop_night behind faceless_knight:
        subpixel True
        xpos -1920
        easeout_quad 2.5 xpos -1720

    # Eva walks from right to left, stopping at Caelor's right side (0.82 -> 0.48)
    show eva:
        easeout_quad 2.5 xpos 0.58

    $ renpy.pause(2.0, hard=True)

    # Caelor turns around to face Eva as she reaches him (xzoom 1 = facing right)
    show caelor:
        ease 0.3 xzoom -1

    $ renpy.pause(0.5, hard=True)

    # Lock characters in standing pose
    show eva browneutral neutral:
        subpixel True                     # Facing left toward Caelor
        zoom 0.25
        xanchor 0.5 yanchor 1.0 ypos 1.0
        xpos 0.58 yoffset 40
        matrixcolor TintMatrix("#5a7099")
        block:
            ease 2.0 yoffset 24
            ease 2.0 yoffset 40
            repeat

    show caelor:
        subpixel True
        zoom 0.25
        xanchor 0.5 yanchor 1.0 ypos 1.0
        xpos 0.36 yoffset 40
        matrixcolor TintMatrix("#5a7099")
    with dissolve


    show layer master:
        subpixel True
        anchor (0.5, 0.5)
        pos (960, 540)
        ease 2.5 zoom 1.85 xpos 1050 ypos 600
    $ renpy.pause(2.5, hard=True)

    hide faceless_knight

    hide faceless_knight

    voice "VA/SHINS/CAELOR01_G-Good evening_03.mp3"
    caelor "G-Good evening, Saintess! Hope the day's treatin' you real fine!"

    show eva browneutral normal_sad what with dissolve

    en "I know every soul in this cathedral. This young man is entirely new."

    show eva browhappy normal_happy smile with dissolve

    voice "VA/RAKUMAROO/Chapter 2A/Ch2A_Eva27.mp3"
    e "Oh! I don't believe we've met. Are you new to the guard, Sir?"

    show caelor browneutral surprised with dissolve

    voice "VA/SHINS/CAELOR02_Yessum_03.mp3"
    caelor "Yessum— Saintess, beg pardon! Just started this week, matter of fact!"

    voice "VA/RAKUMAROO/Chapter 2A/Ch2A_Eva28.mp3"
    e "How lovely! Welcome. What is your name, pray tell?"

    show caelor browneutral excited with dissolve

    voice "VA/SHINS/CAELOR03_here you are_02.mp3"
    caelor "Caelor, Saintess! Grew up on all them old stories about the Saintesses, and here you are, right as rain, standin' right in front of me!"

    
    voice "VA/SHINS/CAELOR04_Can't hardly believe it_01.mp3"
    caelor "Can't hardly believe it, you walkin' these very halls every mornin' and me gettin' to be the one—*Cough!* *Cough!*"

    show caelor browneutral surprised:
        subpixel True
        zoom 0.25
        xanchor 0.5 yanchor 1.0 ypos 1.0
        xpos 0.36 yoffset 40
        matrixcolor TintMatrix("#5a7099")
        # Rapid coughing spasm
        ease 0.03 xoffset 12 yoffset 58
        ease 0.03 xoffset -10 yoffset 24
        ease 0.03 xoffset 14 yoffset 62
        ease 0.03 xoffset -12 yoffset 20
        ease 0.03 xoffset 8 yoffset 52
        ease 0.03 xoffset -6 yoffset 28
        ease 0.03 xoffset 10 yoffset 56
        ease 0.03 xoffset -8 yoffset 32
        # Settle back to normal
        ease 0.10 xoffset 0 yoffset 40


    show eva browhappy normal_happy laugh with dissolve

    voice "VA/RAKUMAROO/Chapter 2A/Ch2A_Eva29.mp3"
    e "Goodness, do breathe, Caelor! I promise I won't bite."

    show caelor browneutral awed:
        subpixel True
        zoom 0.25
        xanchor 0.5 yanchor 1.0 ypos 1.0
        xpos 0.36 yoffset 40
        matrixcolor TintMatrix("#5a7099")
        # Shaking head left and right twice
        ease 0.08 xoffset -18
        ease 0.08 xoffset 18
        ease 0.08 xoffset -12
        ease 0.08 xoffset 12
        ease 0.08 xoffset 0
    voice "VA/SHINS/CAELOR05_Not scary at all_02.mp3"
    caelor "No ma'am! Not scary at all, you're the plumb opposite!"

    voice "VA/SHINS/CAELOR06_When you held out your hands_05.mp3"
    caelor "When you held out your hands durin' the rite last week, I watched from up in the gallery, and I swear I couldn't look away! Couldn't've if I'd tried!"

    show eva browhappy normal_happy smile with dissolve

    voice "VA/RAKUMAROO/Chapter 2A/Ch2A_Eva30.mp3"
    e "You watched my purification from the gallery? How charming of you!"

    show caelor browneutral excited with dissolve

    voice "VA/SHINS/CAELOR07_Every single second_06.mp3"
    caelor "Every single second! The way that light poured off your fingers, n' the whole room went POOF! And everybody just looked so peaceful after!"

    voice "VA/SHINS/CAELOR08_And I thought to myself_07.mp3"
    caelor "And I thought to myself, I wanna be near that! Wanna be right where that magic happens every day!"

    show caelor browsad hmm with dissolve

    voice "VA/SHINS/CAELOR09_So I applied_03.mp3"
    caelor "So I applied for a post here! Reckon' folks thought I'd gone mad in the head, but I just—"

    show eva browneutral normal_sad what with dissolve

    voice "VA/RAKUMAROO/Chapter 2A/Ch2A_Eva31.mp3"
    e "You requested this post simply to be near my light?"

    voice "VA/SHINS/CAELOR10_that sounds awful silly_02.mp3"
    caelor "I know that sounds awful silly!"

    voice "VA/SHINS/CAELOR11_Saintess is the closest thing_07.mp3"
    caelor "My mama always said the Saintess is the closest thing to the divine we'll ever lay eyes on, and I thought..."

    show caelor browneutral happy with dissolve

    voice "VA/SHINS/CAELOR11a_Hallway.mp3"
    caelor "If I could just stand in the same hallway... Well, that'd be enough for me!"

    en "A completely different knight has petitioned to join my escort now?"

    en "The holy texts speak of warriors pledging themselves to the Church's chosen, but I truly thought the chroniclers were exaggerating."

    show eva browsad normal_happy smile blush with dissolve

    en "I am hardly a grand figure worthy of such fervour. It is all so deeply humbling!"

    en "How does one properly respond to such an abundance of earnest admiration?"

    voice "VA/RAKUMAROO/Chapter 2A/Ch2A_Eva32.mp3"
    e "Well, Caelor. I am so very glad you are here. The temple is lucky to have someone so devoted."

    show caelor browneutral awed with dissolve

    voice "VA/SHINS/CAELOR12_You really reckon so_03.mp3"
    caelor "You really reckon so?!"

    voice "VA/RAKUMAROO/Chapter 2A/Ch2A_Eva33.mp3"
    e "I truly do, Sir!"

    show caelor browneutral excited with dissolve

    voice "VA/SHINS/CAELOR13_Thank you Saintess_01.mp3"
    caelor "Thank you, Saintess! Thank you kindly! Won't let you down, I swear on it! Best guard this corridor's ever had, you just watch!"

    voice "VA/RAKUMAROO/Chapter 2A/Ch2A_Eva34.mp3"
    e "I am sure you shall be magnificent!"

    voice "VA/RAKUMAROO/Chapter 2A/Ch2A_Eva EXTRA.mp3"
    e "Good night, Caelor!"


    voice "VA/SHINS/CAELOR14_Good day Saintess_01.mp3"
    caelor "Blessings upon you!"

    
    scene black
    with dissolve

    stop music fadeout 1.0

    
    en "He is still beaming as I step around the corner. His expression is so wonderfully bright."

    en "To know I could provide him with even a small measure of comfort... It brings me joy! I only hope I can always be of service."

    en "The evening concludes peacefully, and soon a new day dawns."

    en "It is only upon returning from my prayers that I discover a delightful surprise resting upon my writing desk."

    play music "bishopshort.mp3"

    # 1. SCENE LOCK: Focused close-up on flowers
   

    $ renpy.pause(0.5, hard=True)

    # 2. CAMERA PULL BACK: Holds focus left-center (xpos 1080) so flowers are fully visible
    show layer master:
        subpixel True
        anchor (0.5, 0.5)
        pos (1220, 730)
        zoom 1.55
        ease 2.5 zoom 1.20 xpos 1080 ypos 540
    scene bg eva_bedroom_day_flowers:
        subpixel True
        anchor (0.5, 0.5)
        zoom 1.55
        xpos 1530 ypos 730
    with fade

    # Eva enters from right toward the flowers on the desk
    show eva browhappy normal_happy smile:
        subpixel True
        xzoom 1                          # Facing left toward flowers
        zoom 0.48
        xanchor 0.5 yanchor 1.0 ypos 1.0
        xpos 0.88 yoffset 520
        easeout_quad 2.5 xpos 0.42       # Stops safely in front of desk/flowers
        block:
            ease 2.0 yoffset 504
            ease 2.0 yoffset 520
            repeat

    $ renpy.pause(2.5, hard=True)

    en "Flowers! Freshly cut, arranged beautifully without a card or name anywhere among them."

    en "To think someone left these just for me! A nameless admirer...!? It feels exactly like the thrilling romance novels Father strictly forbids me from reading."

    # 3. EVA STEPS CLOSER TO FLOWERS, THERION ENTERS FROM RIGHT
    show eva:
        easeout_quad 1.2 xpos 0.34

    show therion body0 browmad gritangry shook behind eva:
        subpixel True
        xzoom 1                          # Facing left toward Eva/Flowers
        zoom 0.52
        xanchor 0.5 yanchor 1.0 ypos 1.0
        xpos 1.15 xoffset -200 yoffset 790
        easeout_quad 1.8 xpos 0.72       # Steps in near door
    with dissolve

    $ renpy.pause(1.8, hard=True)

    en "Sir Therion walks in after me, glaring at the blooms as though wishing to set them ablaze."

    if monstrous_points > deluded_points:

        show eva browhappy normal_happy smile with dissolve:
            xzoom -1
            ease 0.3 xoffset -20
            block:
                ease 2.0 yoffset 504
                ease 2.0 yoffset 520
                repeat
        with dissolve


        voice "VA/RAKUMAROO/Chapter 2A/Ch2A_Eva35.mp3"
        e "Sir Therion, look at what a secret admirer left upon my desk. Is that not the most darling gesture?"

        show therion browmad annoyed shook with dissolve

        voice "VA/JASON/Therion62a.mp3"
        t "No."

        show eva browmad normal_sad frown with dissolve

        voice "VA/RAKUMAROO/Chapter 2A/Ch2A_Eva36.mp3"
        e "No? How terribly unromantic of you."

        show therion browmad gritangry shook with dissolve

        voice "VA/JASON/Therion63.mp3"
        t "Somebody invaded this wing. My wing. Where were you when it happened? Where?"

        show eva browneutral normal_sad what with dissolve

        voice "VA/RAKUMAROO/Chapter 2A/Ch2A_Eva37.mp3"
        e "I was at morning devotions, precisely as I am every day."

        show therion browmad gritannoyed shook with dissolve

        voice "VA/JASON/Therion64.mp3"
        t "Devotions take forty minutes. Forty minutes someone had this room all to themselves."

        show eva browhappy normal_happy laugh with dissolve

        voice "VA/RAKUMAROO/Chapter 2A/Ch2A_Eva38.mp3"
        e "My word, you make a bouquet sound like a crime!"

        show therion browmad gritangry shook with dissolve

        voice "VA/JASON/Therion65.mp3"
        t "Because it is! Somebody touched your desk. Your private things. Could've touched {b}YOU{/b}."

        show eva browneutral normal_sad shocked with dissolve

        voice "VA/RAKUMAROO/Chapter 2A/Ch2A_Eva39.mp3"
        e "You are gripping your scythe awfully tight."

        show therion browmad angry shook with dissolve

        voice "VA/JASON/Therion66.mp3"
        t "Somebody walked into your sanctuary, left something, and I missed it. That's bad. That's real bad."

        show therion browmad smug shook with dissolve

        voice "VA/JASON/Therion67.mp3"
        t "Vidius. Or the new kid, Caelor. Nobody else stares at you long enough to think about flowers."

        show therion browmad gritannoyed shook with dissolve

        voice "VA/JASON/Therion68.mp3"
        t "I look at you longer than both of 'em put together and I didn't even— ah, hell."

        show eva browneutral normal_happy shocked blush with dissolve

        voice "VA/RAKUMAROO/Chapter 2A/Ch2A_Eva40.mp3"
        e "Sir Therion!"

        show therion browsad gritannoyed shook with dissolve

        voice "VA/JASON/Therion69.mp3"
        t "I should've been the one putting things on your desk. Not whoever this was."

        show eva browmad normal_happy frown noblush with dissolve

        voice "VA/RAKUMAROO/Chapter 2A/Ch2A_Eva41.mp3"
        e "Do calm yourself. It is likely nothing sinister."

        show therion browmad angry shook with dissolve

        voice "VA/JASON/Therion70.mp3"
        t "I ain't taking chances with you. Then the flowers go."

        show eva browsad normal_sad shocked with dissolve

        voice "VA/RAKUMAROO/Chapter 2A/Ch2A_Eva42.mp3"
        e "There is truly no need to be so panicked—"

        show therion browmad gritangry shook with dissolve

        voice "VA/JASON/Therion71.mp3"
        t "Could be poison dusted on the petals. Could be a hex in the leaves. I'm not having that sitting near your face."

        show therion browmad frown shook with dissolve

        voice "VA/JASON/Therion72.mp3"
        t "Just give me a minute."

        show therion:
            ease 0.3 xzoom -1 xoffset +20
            pause 0.2
            

        en "He paces the carpet restlessly, tallying on his fingers."

        show therion browmad frown shook with dissolve:
            ease 0.3 xzoom 1 xoffset -20

        voice "VA/JASON/Therion73.mp3"
        t "Caelor gets off post at sundown. Bishop Vidius dines in the east wing, locked in."

        show eva browsad normal_sad what with dissolve

        voice "VA/RAKUMAROO/Chapter 2A/Ch2A_Eva43.mp3"
        e "You actually memorize everyone's schedule?"

        show therion browmad gritannoyed shook with dissolve

        voice "VA/JASON/Therion74.mp3"
        t "Everyone's. I know where every bastard is and I still missed this."

        show eva browhappy normal_happy laugh with dissolve

        voice "VA/RAKUMAROO/Chapter 2A/Ch2A_Eva44.mp3"
        e "Well. At least I shall never suffer from a lack of your attention."

        show therion browneutral grin shook with dissolve

        voice "VA/JASON/Therion75.mp3"
        t "No. You won't. My head doesn't work for anything else anymore. Only you."

        show eva browhappy normal_happy smile with dissolve

        voice "VA/RAKUMAROO/Chapter 2A/Ch2A_Eva45.mp3"
        e "In that case... dispose of the flowers if it grants you peace. And ensure no one else enters my chambers without your express permission."

        show therion browmad grin shook with dissolve

        voice "VA/JASON/Therion76.mp3"
        t "Yeah. That I can do."

        show therion browneutral frown shook :
            
            # Heavy, reluctant backward steps (moving right to offscreen xpos 1.25)
            easein_quad 0.4 xpos 0.78 
            easeout_quad 0.4 xpos 0.84 
            easein_quad 0.4 xpos 0.96 
            easeout_quad 0.4 xpos 1.08 
            easein_quad 0.5 xpos 1.25 alpha 0.0

    else:

        show eva browhappy normal_happy smile with dissolve:
            xzoom -1
            ease 0.3 xoffset -20
            block:
                ease 2.0 yoffset 504
                ease 2.0 yoffset 520
                repeat
        with dissolve

        voice "VA/RAKUMAROO/Chapter 2A/Ch2A_Eva46.mp3"
        e "Sir Therion, look what someone left for me! Is that not the sweetest thing?"

        show therion browskeptical annoyed shook with dissolve

        voice "VA/JASON/Therion77.mp3"
        t "When'd you find those?"

        show eva browhappy normal_happy laugh with dissolve

        voice "VA/RAKUMAROO/Chapter 2A/Ch2A_Eva47.mp3"
        e "Just now! Sitting right here when I returned from prayers. Still cool to the touch."

        show therion browmad gritannoyed shook with dissolve

        voice "VA/JASON/Therion78.mp3"
        t "This wing is on my watch. Door was shut when I walked the hall at fourth bell."

        show eva browhappy normal_happy smile with dissolve

        voice "VA/RAKUMAROO/Chapter 2A/Ch2A_Eva48.mp3"
        e "Oh, I shouldn't think it sinister at all! Merely someone being terribly kind to their Saintess."

        show therion browmad angry shook with dissolve

        voice "VA/JASON/Therion79.mp3"
        t "Who?"

        voice "VA/RAKUMAROO/Chapter 2A/Ch2A_Eva49.mp3"
        e "That is the grand mystery, isn't it? Though I do harbor my suspicions."

        show therion browskeptical smug shook with dissolve

        voice "VA/JASON/Therion80.mp3"
        t "Your suspicions."

        voice "VA/RAKUMAROO/Chapter 2A/Ch2A_Eva50.mp3"
        e "Bishop Vidius, perhaps? The bishop seemed quite taken with cathedral affairs, and flowers are a very bishop sort of gesture, do you not think?"

        show therion browmad gritangry shook with dissolve

        voice "VA/JASON/Therion81.mp3"
        t "Vidius."

        show eva browhappy normal_happy smile with dissolve

        voice "VA/RAKUMAROO/Chapter 2A/Ch2A_Eva51.mp3"
        e "Or perhaps young Caelor! He seems like the sort of dear boy to pick flowers just to make a lady smile."

        show therion browmad smug shook with dissolve

        voice "VA/JASON/Therion82.mp3"
        t "The new guard."

        show eva browmad normal_sad frown with dissolve

        voice "VA/RAKUMAROO/Chapter 2A/Ch2A_Eva52.mp3"
        e "Sir Therion, must you glare at a harmless bouquet as though it offended your honor?"

        show therion browskeptical annoyed shook with dissolve

        voice "VA/JASON/Therion83.mp3"
        t "I'm thinking, Saintess. Who was in this room? The list is short, and I ain't on it."

        show eva browhappy normal_happy laugh with dissolve

        voice "VA/RAKUMAROO/Chapter 2A/Ch2A_Eva53.mp3"
        e "It could be anyone! I am rather tremendously adored, you know. Half the cathedral might have left them."

        show therion browmad angry shook with dissolve

        voice "VA/JASON/Therion84.mp3"
        t "Somebody stood right here. At your desk. Could've touched anything while you were gone."

        show eva browneutral normal_sad what with dissolve

        
        voice "VA/RAKUMAROO/Chapter 2A/Ch2A_Eva54.mp3"
        e "Well, let me check..."

        show eva browneutral normal_sad what with dissolve:
            xzoom -1
            ease 0.3 xzoom 1 
            ease 0.2 xoffset -100
            pause 1
            ease 0.3  xzoom -1 xoffset 0
            block:
                ease 2.0 yoffset 504
                ease 2.0 yoffset 520
                repeat
        with dissolve

        # eva moves around the room

        show eva browhappy normal_happy smile with dissolve

        voice "VA/RAKUMAROO/Chapter 2A/Ch2A_Eva55.mp3"
        e "No, nothing has been disturbed."

        show therion browmad frown with dissolve

        voice "VA/JASON/Therion85.mp3"
        t "I'll find out who."

        show eva browmad normal_sad frown with dissolve

        voice "VA/RAKUMAROO/Chapter 2A/Ch2A_Eva56.mp3"
        e "There is no need for a scene. It was a kindness!"

        show therion browmad gritangry shook with dissolve

        voice "VA/JASON/Therion88.mp3"
        t "I'm gonna find out who. Then I'm gonna find out everything about 'em. So it doesn't happen again."

        show eva browsad normal_sad what with dissolve

        voice "VA/RAKUMAROO/Chapter 2A/Ch2A_Eva57.mp3"
        e "Why ever would you require all those details?"

        show therion browmad grin shook with dissolve

        voice "VA/JASON/Therion89.mp3"
        t "So I can have a quiet little chat with 'em."

        show eva browhappy normal_sad frown with dissolve

        voice "VA/RAKUMAROO/Chapter 2A/Ch2A_Eva58.mp3"
        e "Somehow I doubt that chat would be very pleasant."

        show eva:
            xzoom 1
        with dissolve

        en "I arrange the bouquet on my writing desk while he keeps muttering to himself."

        show eva browhappy normal_happy smile with dissolve

        voice "VA/RAKUMAROO/Chapter 2A/Ch2A_Eva59.mp3"
        e "There now! Does that not look lovely?"

        show therion browmad annoyed shook:
            ease 0.3 xoffset -800

        show eva browneutral normal_sad shocked:
            ease 0.4 xoffset +600 xzoom 1
            block:
                ease 2.0 yoffset 504
                ease 2.0 yoffset 520
                repeat

        voice "VA/JASON/Therion90.mp3"
        t "Hold on. Lemme check 'em first. Could be poison. Or a curse."

        
        en "He lifts the bouquet and inspects every stem with terrifying intensity. He actually licks one of the petals."

        show therion browskeptical annoyed shook with dissolve

        voice "VA/JASON/Therion91.mp3"
        t "Hrm. Clean."

        show eva browhappy normal_happy laugh with dissolve

        voice "VA/RAKUMAROO/Chapter 2A/Ch2A_Eva60.mp3"
        e "You see? Perfectly harmless!"

        show therion browmad annoyed shook with dissolve

        voice "VA/JASON/Therion92.mp3"
        t "Caelor gets off post at sundown. Bishop Vidius dines in the east wing, locked inside."

        show eva browsad normal_sad what with dissolve

        voice "VA/RAKUMAROO/Chapter 2A/Ch2A_Eva61.mp3"
        e "I'm sorry? Do you know everyone's schedule?"

        show therion browneutral smug shook with dissolve

        voice "VA/JASON/Therion93.mp3"
        t "Part of the job."

        show eva browmad normal_happy frown with dissolve

        voice "VA/RAKUMAROO/Chapter 2A/Ch2A_Eva62.mp3"
        e "Well, then. Now that you are satisfied regarding the flowers, you may go, Sir Therion. I have letters to write, and I shan't have you hovering."

        show therion browneutral frown shook with dissolve

        voice "VA/JASON/Therion94.mp3"
        t "Right. Outside."

        show eva browhappy normal_happy smile with dissolve

        voice "VA/RAKUMAROO/Chapter 2A/Ch2A_Eva63.mp3"
        e "As you wish, my knight."

        show therion browneutral frown shook :
            subpixel True
            xzoom 1                          # Keeps facing left toward the flowers/Eva
            zoom 0.54
            
            # Heavy, reluctant backward steps (moving right to offscreen xpos 1.25)
            easein_quad 0.4 xpos 0.78 
            easeout_quad 0.4 xpos 0.84 
            easein_quad 0.4 xpos 0.96 
            easeout_quad 0.4 xpos 1.08 
            easein_quad 0.5 xpos 1.25 alpha 0.0
        show eva what:
            pause 1.2
            ease 1.0 xzoom -1 xoffset 0

        $ renpy.pause(2.1, hard=True)

    en "He exits backward as usual, counting every stride, and I hear him hit the outer wall with a heavy thud, resting his scythe against the stone."

    en "If it wasn't Therion's doing, then who?"

    scene black

    with fade

    en "I never do learn who left the bouquet. Perhaps it is better left unsolved. Some secrets are far more exciting kept in the dark."

    en "My day unfolds quite as mundane as usual, which suits me perfectly."

    scene black
    with fade

    # 1. Base Day Scene Setup
    show bg temple_corridor_day

    # 2. Caelor stationed slightly left (xpos 0.66, facing left toward Eva)
    show caelor smile:
        subpixel True
        xzoom 1                          # Facing left toward Eva
        zoom 0.25
        xanchor 0.5 yanchor 1.0 ypos 1.0
        xpos 0.66 yoffset 40             # Adjusted slightly left

    # 3. Eva starts on the left side (xzoom -1: facing right toward Caelor)
    show eva browsad neutral:
        subpixel True
        xzoom -1                         # Facing right toward Caelor
        zoom 0.25
        xanchor 0.5 yanchor 1.0 ypos 1.0
        xpos 0.15 yoffset 40
        block:
            ease 2.0 yoffset 24
            ease 2.0 yoffset 40
            repeat
    with fade

    $ renpy.pause(1.0, hard=True)

    # Background parallax loop sits BEHIND ALL CHARACTERS (scrolls left as Eva moves right)
    show temple_corridor_day1 behind caelor:
        subpixel True
        xpos 0
        easeout_quad 2.5 xpos -200

    show bg_corridor_loop behind caelor:
        subpixel True
        xpos 1920
        easeout_quad 2.5 xpos 1720

    # Eva walks from left to right, stopping at a comfortable distance (0.15 -> 0.44)
    show eva:
        easeout_quad 2.5 xpos 0.44

    $ renpy.pause(2.5, hard=True)

    # Lock characters in standing pose
    show eva browneutral neutral:
        subpixel True
        xzoom -1                         # Facing right toward Caelor
        zoom 0.25
        xanchor 0.5 yanchor 1.0 ypos 1.0
        xpos 0.44 yoffset 40
        block:
            ease 2.0 yoffset 24
            ease 2.0 yoffset 40
            repeat

    show caelor:
        subpixel True
        xzoom 1                          # Facing left toward Eva
        zoom 0.25
        xanchor 0.5 yanchor 1.0 ypos 1.0
        xpos 0.66 yoffset 40
    with dissolve

    # ============================================================
    # CAMERA CLOSE-UP: CENTERED FRAMING ON BOTH CHARACTERS
    # ============================================================

    show layer master:
        subpixel True
        anchor (0.5, 0.5)
        pos (960, 540)
        ease 2.5 zoom 1.70 xpos 800 ypos 520

    $ renpy.pause(2.5, hard=True)
    en "Ah, there is Sir Caelor once more! Stationed along my path for the third time this week."

    show caelor idle browneutral excited with dissolve

    voice "VA/SHINS/CAELOR15_Mornin' to you_02.mp3"
    caelor "Saintess! Mornin' to you!"

    voice "VA/RAKUMAROO/Chapter 2A/Ch2A_Eva64.mp3"
    e "Good morning, Sir Caelor. Settling in well?"

    show caelor browneutral awed with dissolve

    voice "VA/SHINS/CAELOR16_Better'n I deserve_02.mp3"
    caelor "Better'n I deserve! Keep thinkin' I'll wake up to find it's all a mistake and I'm back muckin' stables!"

    voice "VA/RAKUMAROO/Chapter 2A/Ch2A_Eva65.mp3"
    e "Nonsense. You were appointed for a reason."

    show caelor browsad hmm with dissolve

    voice "VA/SHINS/CAELOR17_You truly reckon so_06.mp3"
    caelor "You truly reckon so?"

    show eva browhappy normal_happy smile with dissolve

    voice "VA/RAKUMAROO/Chapter 2A/Ch2A_Eva66.mp3"
    e "I do."

    show eva browneutral normal_sad what with dissolve
    show layer master:
        subpixel True
        anchor (0.5, 0.5)
        zoom 1.70
        xpos 800
        ypos 520
        easein 1.5 zoom 1.78 xpos 850 ypos 540

    show caelor:
        subpixel True
        xzoom 1
        zoom 0.25
        xanchor 0.5
        yanchor 1.0
        xpos 0.66
        ypos 1.0
        yoffset 40

        # Slight tilt toward Eva
        easein 1.0 xpos 0.63 yoffset 65

        pause 0.4

        # Return to original position
        easeout 0.8 xpos 0.66 yoffset 40


    en "Sir Caelor steps forward and takes my hand before I can offer it, bowing low to press his lips to my knuckles."

    show caelor excited closed:
        subpixel True
        xzoom 1
        zoom 0.25
        xanchor 0.5 yanchor 1.0 ypos 1.0
        easeout 1.0 xpos 0.66 yoffset 40
    voice "VA/SHINS/CAELOR18_Wanted to say it proper_07.mp3"
    caelor "Wanted to say it proper, what an honor this is. Didn't get the words right the first time. You were walkin' off and I just stood there gapin' like a trout!"

    show eva browhappy normal_happy smile with dissolve

    voice "VA/RAKUMAROO/Chapter 2A/Ch2A_Eva67.mp3"
    e "How terribly gallant, Sir Caelor."

    show caelor browneutral normal surprised with dissolve

    voice "VA/SHINS/CAELOR19_Oh—Saintess_02.mp3"
    caelor "Oh— Saintess, what's this here?"

    show caelor:
        subpixel True
        xpos 0.63
        ypos 1.0
        yoffset 40
        easein 1.2 xpos 0.58 yoffset 85

    show layer master:
        subpixel True
        anchor (0.5, 0.5)
        zoom 1.70
        xpos 800
        ypos 520
        easein 1.5 zoom 2.2 xpos 850 ypos 535

    voice "VA/SHINS/CAELOR20_Got a scar on your hand_04.mp3"
    caelor "Got a scar on your hand. Hadn't noticed that before."

    show eva browneutral normal_sad neutral with dissolve

    voice "VA/RAKUMAROO/Chapter 2A/Ch2A_Eva68.mp3"
    e "Ah, it's from my very first purification rite. I hardly think of it anymore."

    show caelor browsad hmm with dissolve

    voice "VA/SHINS/CAELOR21_Does it still give you trouble_03.mp3"
    caelor "Does it still give you trouble?"

    show eva browhappy normal_happy smile with dissolve

    voice "VA/RAKUMAROO/Chapter 2A/Ch2A_Eva69.mp3"
    e "Heavens, no. Years behind me."

    voice "VA/SHINS/CAELOR22_scars trap old hurt_01.mp3"
    caelor "Mama always said scars trap old hurt deep down. Oughta have somebody check it, make sure nothin's still tender underneath."

    show eva browsad normal_sad frown with dissolve

    voice "VA/RAKUMAROO/Chapter 2A/Ch2A_Eva70.mp3"
    e "I... see. I'll get it examined. Thank you."


    en "He continues to hold my hand, far past the bounds of proper decorum."

    show caelor browneutral hmm with dissolve

    en "His thumb traces the mark, agonizingly slow."

    
    menu:

        "Let him continue":

            stop music fadeout 0.5

            show therion body0 browmad gritangry hair2 shook:
                subpixel True
                xanchor 0.5
                yanchor 1.0
                xpos 0.89
                ypos 1.0
                zoom 0.22

            # Dramatic but smooth pull-back
            show layer master:
                subpixel True
                anchor (0.5, 0.5)
                zoom 1.95
                xpos 850
                ypos 535
                easein 1.5 zoom 1.0 xpos 960 ypos 540

            # Therion at the far right edge
            

            en "I leave my hand in his. Out of the corner of my eye, I catch Therion watching."

            show eva browneutral normal_sad neutral with dissolve

            en "Only then do I slowly draw back."

            show eva:
                subpixel True
                easein 0.5 xoffset -15
                block:
                    ease 2.0 yoffset 24
                    ease 2.0 yoffset 40
                    repeat

            $ monstrous_points += 1

        "Withdraw your hand":

            stop music fadeout 0.5

            show therion body0 browmad gritangry hair2 shook:
                subpixel True
                xanchor 0.5
                yanchor 1.0
                xpos 0.89
                ypos 1.0
                zoom 0.22

            # Dramatic but smooth pull-back
            show layer master:
                subpixel True
                anchor (0.5, 0.5)
                zoom 1.95
                xpos 850
                ypos 535
                easein 1.5 zoom 1.0 xpos 960 ypos 540

            en "Out of the corner of my eye, I catch Therion watching."

            show eva browmad normal_sad frown with dissolve

            # Eva jerks her hand away
            show eva:
                subpixel True
                easein 0.2 xoffset -35
                block:
                    ease 2.0 yoffset 24
                    ease 2.0 yoffset 40
                    repeat

            voice "VA/RAKUMAROO/Chapter 2A/Ch2A_Eva71.mp3"
            e "... That's quite enough."

            show caelor browsad surprised with dissolve

            # Caelor recoils
            show caelor:
                subpixel True
                easein 0.2 xoffset 25

            voice "VA/SHINS/CAELOR23_O-Oh S-Sorry Saintess_02.mp3"
            caelor "O-Oh! S-Sorry Saintess!"

            $ deluded_points += 1

    show eva browhappy normal_happy smile with dissolve

    voice "VA/RAKUMAROO/Chapter 2A/Ch2A_Eva72.mp3"
    e "Well! I really must be getting on. Duties call."

    show caelor browneutral happy with dissolve

    voice "VA/SHINS/CAELOR24_Of course Saintess_07.mp3"
    caelor "Of course, Saintess. I'll be right here if you need anythin' at all!"

    voice "VA/RAKUMAROO/Chapter 2A/Ch2A_Eva73.mp3"
    e "I am sure you will."


    scene bg temple_corridor_day:
        blur 13
        zoom 1.35
        ease 8.0 zoom 1.5

    # Therion, foreground
    show therion body0 hair2 gritangry at center:
        zoom 0.40
        xoffset 170
        yoffset 545
        blur 6

        parallel:
            ease 10.0 zoom 0.46
            repeat

        parallel:
            easeout 0.65 yoffset 565
            easein 1.15 yoffset 545
            repeat

        parallel:
            ease 0.9 xoffset 176
            ease 0.9 xoffset 164
            repeat

    # Eva
    show eva browsad frown at center:
        zoom 0.56
        xoffset -125
        yoffset 905

        parallel:
            ease 10.0 zoom 0.64
            repeat

        parallel:
            easeout 0.7 yoffset 890
            easein 0.7 yoffset 905
            repeat

        parallel:
            ease 1.4 xoffset -117
            ease 1.4 xoffset -133
            repeat


    # Caelor, farther behind them on the right
    show caelor browneutral hmm  behind therion:
        subpixel True
        xanchor 0.5
        yanchor 1.0
        xpos 0.76
        ypos 1.0
        zoom 0.24
        yoffset 360
        blur 7

    # Camera slowly follows Eva and Therion
    show layer master:
        subpixel True
        anchor (0.5, 0.5)
        zoom 1.0
        xpos 960
        ypos 540
        ease 4.0 zoom 1.10 xpos 940 ypos 575
    with fade

    pause 1.5

    # Caelor gradually falls farther behind
    show caelor:
        subpixel True
        ease 5.0 xpos 0.90 zoom 0.18 yoffset 400 blur 10

    pause 2.0

    
    play music "norowaretapiano.mp3"


    if monstrous_points > deluded_points:

        $ current_frame = "twisted"

        show eva browhappy normal_happy laugh with dissolve

        voice "VA/RAKUMAROO/Chapter 2A/Ch2A_Eva74.mp3"
        e "Sir Therion, did you witness that? What an absolute sweetheart!"

        show therion body0 browmad gritannoyed half with dissolve

        voice "VA/JASON/Therion95.mp3"
        t "Yeah. Real sweet."

        show eva browhappy normal_happy smile with dissolve

        voice "VA/RAKUMAROO/Chapter 2A/Ch2A_Eva75.mp3"
        e "He noticed my scar! Hardly anyone ever looks closely enough for that."

        show therion browmad angry shook with dissolve

        voice "VA/JASON/Therion96.mp3"
        t "He held your hand for eleven seconds."

        show eva browneutral normal_sad what with dissolve

        voice "VA/RAKUMAROO/Chapter 2A/Ch2A_Eva76.mp3"
        e "I beg your pardon?"

        voice "VA/JASON/Therion97.mp3"
        t "Eleven. That's waaay past a normal greeting."

        show therion browmad gritangry shook with dissolve

        play sound "audio/scrape.mp3"

        en "I can hear him scraping his scythe in surfaces."

        # He finally disappears off to the right
        show caelor:
            ease 2.5 xpos 1.12 zoom 0.12 alpha 0.0 blur 13

        pause 2.5

        show eva browsad normal_sad frown with dissolve

        voice "VA/RAKUMAROO/Chapter 2A/Ch2A_Eva77.mp3"
        e "Does this bother you so much?"

        voice "VA/JASON/Therion98.mp3"
        t "Yeah. He put his fu— filthy hands on my Saintess. I can't just let that slide."


        show eva browneutral normal_sad neutral with dissolve

        voice "VA/RAKUMAROO/Chapter 2A/Ch2A_Eva78.mp3"
        e "It is only a scar, Therion."

        show therion browmad angry shook hair1 with hpunch

        voice "VA/JASON/Therion99.mp3"
        t "Ain't a single inch of you that's 'only' anything!"

        show eva browneutral normal_sad what with dissolve

        en "His voice booms through the gallery, startling a passing cleric."

        show eva browmad normal_sad frown with dissolve

        voice "VA/RAKUMAROO/Chapter 2A/Ch2A_Eva79.mp3"
        e "... Mind your tone."

        show therion browsad frown half with dissolve

        voice "VA/JASON/Therion100.mp3"
        t "Right. Sorry, Saintess."

        show therion browsad frown luvhalf hair2 with dissolve

        voice "VA/JASON/Therion101.mp3"
        t "Every time I close my eyes, I see his thumb stroking your skin. It's driving me out of my damn mind."

        show eva browhappy normal_happy smile with dissolve

        voice "VA/RAKUMAROO/Chapter 2A/Ch2A_Eva80.mp3"
        e "You know, Sir Therion... I believe Sir Caelor has the makings of someone rather special. I do hope he rises rapidly through the ranks."

        show therion browsad frown half with dissolve

        voice "VA/JASON/Therion102.mp3"
        t "Please don't say that."

        show eva browneutral normal_sad what with dissolve

        voice "VA/RAKUMAROO/Chapter 2A/Ch2A_Eva81.mp3"
        e "Why ever not?"

        show therion browmad gritangry shook with dissolve

        voice "VA/JASON/Therion103.mp3"
        t "Because there won't be any ranks left for him to climb if I—"

        en "He cuts himself off hard, teeth grinding."

        show therion browsad frown half with dissolve

        voice "VA/JASON/Therion104.mp3"
        t "Forget it."

        show eva browneutral normal_sad frown with dissolve

        voice "VA/RAKUMAROO/Chapter 2A/Ch2A_Eva82.mp3"
        e "You are making remarkably little sense today."

        show therion browsad neutral half with dissolve

        voice "VA/JASON/Therion105.mp3"
        t "I know. Sorry. Give me till evening. I'll be right by then."


    else:

        $ current_frame = "twisted"

        show eva browhappy normal_happy smile with dissolve

        voice "VA/RAKUMAROO/Chapter 2A/Ch2A_Eva83.mp3"
        e "Sir Therion, did you witness that? What a lovely young knight!"

        voice "VA/RAKUMAROO/Chapter 2A/Ch2A_Eva84.mp3"
        e "He noticed my scar and was so sweet about it! Very few people bother to look closely enough."

        show therion body0 browmad gritannoyed closed with dissolve

        t "..."

        show eva browneutral normal_sad what with dissolve

        voice "VA/RAKUMAROO/Chapter 2A/Ch2A_Eva85.mp3"
        e "Sir Therion?"

        t "..."

        voice "VA/RAKUMAROO/Chapter 2A/Ch2A_Eva86.mp3"
        e "You are awfully quiet today."

        voice "VA/JASON/Therion106.mp3"
        t "Nice kid."

        show eva browhappy normal_happy smile with dissolve

        voice "VA/RAKUMAROO/Chapter 2A/Ch2A_Eva87.mp3"
        e "He is! I am so glad you think so."

        voice "VA/JASON/Therion107.mp3"
        t "Wonder what else he's planning to look at."

        show eva browneutral normal_sad what with dissolve

        voice "VA/RAKUMAROO/Chapter 2A/Ch2A_Eva88.mp3"
        e "Pardon?"

        show therion browsad frown half with dissolve

        voice "VA/JASON/Therion108.mp3"
        t "Nothin', Saintess. Forget it."

        # He finally disappears off to the right
        show caelor:
            ease 2.5 xpos 1.12 zoom 0.12 alpha 0.0 blur 13

        pause 2.5


        show eva browhappy normal_happy smile with dissolve

        voice "VA/RAKUMAROO/Chapter 2A/Ch2A_Eva89.mp3"
        e "There is truly nothing to worry about. Only one protector matters to me, Sir Therion. The rest are merely pleasant scenery."

        show therion browmad neutral closed with dissolve

        en "He walks the rest of the hall without another word."

        play sound "audio/scrape.mp3"

        en "I can hear the sound of his scythe scraping through the surfaces, though."

        show eva browneutral normal_sad what with dissolve

        en "Hm."

    scene black
    with fade

    stop sound


    en "Evening prayers run terribly late, and by the time the last hymn concludes, the cathedral corridors are completely dark."

    scene black
    with fade

# ============================================================
    # FIRST & SECOND IMAGE PARALLAX SETUP (Gapless Infinite Scroll)
    # ============================================================

    show bg temple_corridor_red as bg1 behind eva:
        subpixel True
        xpos 0 ypos 0
        block:
            xpos 0
            linear 25.0 xpos 1920
            repeat

    show temple_corridor_red1 as bg2 behind eva:
        subpixel True
        xpos -1920 ypos 0
        block:
            xpos -1920
            linear 25.0 xpos 0
            repeat

    # ============================================================
    # EVA WALKING SETUP
    # ============================================================

    show eva browsad neutral:
        subpixel True
        xzoom 1                          # Facing left
        zoom 0.25
        xanchor 0.5 yanchor 1.0 ypos 1.0
        xpos 0.75 yoffset 40
        matrixcolor red_eerie_matrix
        
        parallel:
            block:
                ease 0.6 yoffset 24
                ease 0.6 yoffset 40
                repeat
        parallel:
            linear 500 xpos 0.20        # Creeps slowly from right to left
    with fade

    $ renpy.pause(1.0, hard=True)

    play music "Eva.mp3"

    en "Good heavens, it is dreadfully dark in here... Gather your courage, Evangeline, just sing a soft melody to keep the fright away."

    en "I wish Sir Therion were here. Yet I must manage on my own tonight! He requires proper sleep, and I have been terribly worried about him exhausting himself on my account."

# Panel 1: Slides on-screen from left (-1920 to 0) over 10s, then loops 0 -> 1920
    show bloodtrail as blood1 behind eva:
        subpixel True
        matrixcolor red_eerie_matrix
        xpos -1920 ypos 0
        linear 10.0 xpos 0
        block:
            xpos 0
            linear 25.0 xpos 1920
            repeat

    # Panel 2: Waits 10s off-screen, then seamlessly follows Panel 1 (-1920 -> 0)
    show bloodtrail as blood2 behind eva:
        subpixel True
        matrixcolor red_eerie_matrix
        xpos -1920 ypos 0
        pause 10.0
        block:
            xpos -1920
            linear 25.0 xpos 0
            repeat

    # Eva halts her vertical walking bounce and stands stationary
    show eva browneutral normal_sad what:
        subpixel True
        xzoom 1
        zoom 0.25
        xanchor 0.5 yanchor 1.0 ypos 1.0
        yoffset 40
        matrixcolor red_eerie_matrix

        parallel:
            block:
                ease 0.6 yoffset 24
                ease 0.6 yoffset 40
                repeat
    with dissolve

    # Dialogue advances freely while the blood glides across continuously underneath
    en "Now what on earth is that?"

    en "It looks as though someone spilled a pitcher of thick wine. Except wine doesn't cling to stone in such sticky clumps."

    stop music fadeout 1.0

    $ current_frame = "horror"


    show eva browsad normal_sad what with dissolve

    play music "audio/drag.mp3"

    voice "VA/RAKUMAROO/Chapter 2A/Ch2A_Eva90.mp3"
    e "Goodness me... whatever is that scraping noise?"

    en "Someone appears to be moving heavy furniture in the dark. At this hour?"

    show leg behind eva:
        subpixel True
        matrixcolor red_eerie_matrix
        xpos 0 ypos 0
        easein 1.8 xpos 150
    $ renpy.pause(1.8, hard=True)

    show bg temple_corridor_red as bg1 behind eva:
        subpixel True
    show temple_corridor_red1 as bg2 behind eva:
        subpixel True
    show bloodtrail as blood1 behind eva:
        subpixel True
    show bloodtrail as blood2 behind eva:
        subpixel True

    show leg behind eva:
        subpixel True
        matrixcolor red_eerie_matrix
        xpos 150 ypos 0

        # Multi-stage heavy dragging motion
        ease 0.4 xpos 80                 # Smooth first drag back
        pause 0.25
        ease 0.3 xpos 110                # Slight forward slide/slip
        pause 0.3
        ease 0.4 xpos 40                 # Second smooth drag back
        pause 0.2
        ease 0.6 xpos -1920              # Pulled completely off-screen

    show eva browhappy normal_happy smile with dissolve

    en "Oh! Someone has left a boot behind."

    en "Though I suppose if one is lugging heavy objects through the dark, one might lose all manner of things."

    show eva browneutral normal_sad what:
        ease 0.5 xoffset -200
        parallel:
            block:
                ease 0.6 yoffset 24
                ease 0.6 yoffset 40
                repeat


    en "Hmm? What is that?"

    show eva browsad normal_sad what with dissolve

    en "It is really hard to see anything in here at this hour!"

    show eva browhappy normal_happy smile with dissolve

    en "... I really must speak to the Archbishop about the lighting in this wing."

    en "And the servants really must clean this before sunrise. Stone stains so dreadfully if neglected."

    # ============================================================
    # WING FLAP TAKEOFF + TILT & FLIGHT OFF-SCREEN
    # ============================================================

    # 1. Bob up on wing flap, step forward, and tilt forward (-5 degrees)
    show eva browhappy normal_happy smile:
        subpixel True
        parallel:
            # Lift off, then continuously bob up and down in mid-air
            easein 0.35 yoffset -80 xoffset -250
            block:
                ease 0.5 yoffset -50
                ease 0.5 yoffset -80
                repeat
        parallel:
            # Slight forward tilt into flight direction
            easein 0.4 rotate -5.0

    en "I hover carefully over the deepest crimson, mindful of my hem. It would be a nightmare to track that into my bedchamber."

    # ============================================================
    # FLIGHT EXIT OFF-SCREEN
    # ============================================================

    show eva browhappy normal_happy smile:
        subpixel True
        rotate -5.0
        parallel:
            # Continues hovering bobbing cycle
            block:
                ease 0.5 yoffset -50
                ease 0.5 yoffset -80
                repeat
        parallel:
            # Glides smoothly off-screen left
            linear 4.5 xpos -0.30

    scene black with dissolve

    $ renpy.pause(1.5, hard=True)

    en "On my way back to my room, I found a soft, pale little scrap, cold to the touch."

    scene bg evahorror
    with fade

    en "I pick up the small piece by its very tip and put it in my robe pocket. No sense in making the mess any worse."

    en "Well, whoever lost these has clearly found their way home without them."

    en "I do hope they aren't wandering the cloisters barefoot. The stone carries a dreadful chill at night."

    scene black
    with fade

    stop music fadeout 1.0

    en "All things considered, I sleep quite soundly."

    en "Morning arrives, bathed in a gentle sunlight that makes the evening prior feel almost like a bad dream."

    en "It is only once I have dressed and set out for breakfast that I discover the night was not forgotten at all."

    jump creepy


default monstrous_points = 0
default deluded_points = 0

label opening_scene:

    scene bg MM1
    show screen fireflies


    en "Once upon a time, the world was horrid."

    en "Men fought wars over borders that meant nothing at all, fields starved while granaries sat locked."

    en "Neighbours stole from neighbours. Friends sold each other out for coin, or worse, out of sheer spite."

    en "A thoroughly miserable little world, all told."

    en "Then came a Saintess."

    en "She walked among the suffering and took their anger and pain into her own two hands. And oh, how wonderful it was!"

    en "War stopped. Hunger eased. Thieves and murderers wept for what they had taken."

    en "People spoke to each other kindly again, simply because she had reminded them how."

    en "That is what a Saintess is for, you see. To carry everyone's sorrow."

    en "I think it is the most holy of works there is."

    en "Some maidens are already born with such gifts, others are trained to wield them. In time, they become a Saintess."

    en "I begged to hear the story of every Saintess every single night. I never once grew tired of it."

    en "I would imagine my own two hands doing just that. Lifting someone's grief right out of them. Bearing the burdens of the whole wide world."

    en "Oh, how desperately I wanted to be a Saintess!"

    en "A silly child's dream, of course."

    en "Yet I never stopped wanting it."

    scene black

    hide screen fireflies

    en "Years passed the way they do in stories, so quickly you didn't even notice it."

    en "I grew up, but the dream remained."

    en "A hundred years of waiting, with the world managing on its own, dreadfully."

    en "Until a new saintess emerged."

    en "... Me."

    en "Now, every day I offer the exact same prayer, just as every Saintess before me had, all the way back to the very first."

    scene bg temple_hall_day
    show eva closed_sad frown browneutral at right:
        xzoom -1
        zoom 0.25
        alpha 0.0
        xoffset -180
        yoffset 40
        ease 0.6 alpha 1.0
        block:
            ease 2.0 yoffset -16
            ease 2.0 yoffset 0
            repeat

    voice "VA/RAKUMAROO/Eva1.mp3"
    e "Grant them peace."

    voice "VA/RAKUMAROO/Eva2.mp3"
    e "Grant them rest."

    voice "VA/RAKUMAROO/Eva3.mp3"
    e "Let no one outside these walls carry what they cannot bear."

    voice "VA/RAKUMAROO/Eva4.mp3"
    e "Let me—and me alone—take on their sorrow."

    show desmond browmad stern:
        xzoom -1
        zoom 0.22
        xanchor 0.5
        yanchor 1.0
        xpos -0.2
        yalign 1.0
        yoffset 170
        alpha 0.0
        rotate 15

        easein 3 xpos 0.5 alpha 1.0 rotate 0

        block:
            ease 3.0 yoffset 160
            ease 3.0 yoffset 184
            repeat

    pause 1.0

    show eva normal_happy what:
        ease 0.3 xzoom 1
        block:
            ease 2.0 yoffset -16
            ease 2.0 yoffset 0
            repeat
    pause 1.0

    show layer master:
        subpixel True
        anchor (0.5, 0.5)
        pos (960, 540)
        zoom 1.0
        pause 0.5
        ease 3.0 zoom 1.7 xpos 600 ypos 500

    voice "VA/RAKUMAROO/Eva5.mp3"
    e "Good morning, Fath—"

    show desmond stern

    voice "VA/GARFUNKEL/Desmond1.mp3"
    de "Archbishop."

    voice "VA/GARFUNKEL/Desmond2.mp3"
    de "We kneel in the house of the divine, Saintess. Pray remember where you are."

    show eva calm browsad normal_sad frown blush

    voice "VA/RAKUMAROO/Eva6.mp3"
    e "Of course. Forgive me, Archbishop."

    voice "VA/GARFUNKEL/Desmond3.mp3"
    de "The trial takes place today."

    voice "VA/GARFUNKEL/Desmond4.mp3"
    de "Your sworn protector shall be chosen at high noon. See that you attend until the very end."

    en "And with that, he takes his leave."

    show desmond stern:
        xzoom 1
        rotate 0
        easeout 1.5 xpos -0.2 alpha 0.0 rotate -15

    pause 0.5

    en "..."
    show eva calm browhappy normal_happy smile noshadow noblush:
        ease 1.0 xoffset -500

        parallel:
            ease 2.5 yoffset -16
            ease 2.5 yoffset 0
            repeat

    en "A knight!"

    en "Every Saintess in the histories had one, and every account makes it sound like the most tremendous honour a soul could receive."

    en "Sir Laurentius carried Saint Carvilia's prayer book into battle himself, ensuring she was never without protection, even from a hundred miles away!"

    en "Lord Reynhardt stood outside Saint Bellamy's door for eleven straight days during the famine riots. Eleven whole days! Never once abandoning his post."

    en "What extraordinary devotion. To commit one's whole life to standing beside another, keeping them from harm!"

    en "Ah, I do hope mine is just as steadfast!"

    en "Who could it possibly be?"

    show eva calm normal_sad browneutral neutral:
        block:
            ease 5.0 yoffset -16
            ease 5.0 yoffset 0
            repeat
    show eva browsad

    en "I wish..."

    en "... No. You shan't, Evangeline."

    scene black
    with fade

    en "But what if...?"


    stop music fadeout 1.0

    en "The Archbishop has reserved a balcony for me high above the sand, so that I may watch undisturbed by the crowd."

    scene bg arena_day_lit_crowd
    with fade

    play music "trials.mp3"

    show eva normal_happy smile:
        zoom 0.06
        xanchor 0.5
        yanchor 1.0
        xpos 890
        ypos 447
        xzoom -1

        matrixcolor ColorizeMatrix("#ba7570", "#ba7570")

        crop (0, 0, 1.0, 0.57)
        crop_relative True


    show desmond stern:
        zoom 0.05
        xanchor 0.5
        yanchor 1.0
        xpos 1030
        ypos 447
        xzoom 1

        matrixcolor ColorizeMatrix("#ba7570", "#ba7570")

        crop (0, 0, 1.0, 0.57)
        crop_relative True

    en "Below, two men circle one another with wooden clubs and shields."

    # Combat anim

    show shadow_manleft at manleft_fight
    show shadow_manright at manright_fight
    show expression Null() as clash_sound at clash_timer


    en "Dear me. I can scarcely bear to look, even knowing their weapons are blunted!"

    en "Grown men trading blows over a duty that ought to be bestowed freely, rather than seized by force? Utterly barbaric."

    en "I really must speak with the Archbishop about abolishing this spectacle altogether. Let the Saintess select her own protector and spare everyone the bloodshed."

    hide clash_sound

    show shadow_manleft at manleft_final_reset
    show shadow_manright at manright_final_reset

    show shadow_manleft at manleft_final_approach
    show shadow_manright at manright_final_approach
    pause 0.6

    $ _clash_impact(None, 0, 0)
    pause 0.4

    show shadow_manright at manright_collapse
    play sound "audio/thud.mp3"
    pause 0.3
    hide shadow_manleft
    with dissolve
    pause 1.5

    voice "VA/JEFFEREY/Announcer1.mp3"
    announcer "And now...{w} Therion of Aelazath!"

    show therion body1 browmad hair2 at right:
        zoom 0.23
        alpha 0.0
        xoffset -180
        yoffset 40
        ease 0.6 alpha 1.0
    with dissolve

    pause 1.02

    en "Oh."

    show layer master:
        subpixel True
        anchor (0.5, 0.5)
        pos (960, 540)
        zoom 1.0

        # nzoooommmmmmmmnyommm
        ease 3.5 zoom 1.5 xpos 450 ypos 600

    en "He is..."

    en "He's the youngest of everyone. Every other combatant out there looks a lot taller than him!"

    en "I pray those men do not slaughter him outright!"

    scene bg RED

    show therion_bam
    show man_fallback

    pause 0.76
    play sound "audio/bash1.mp3"
    scene black
    with hpunch

    pause 0.5

    en "Oh Dear. Just look at him go! He is swifter than the rest, and infinitely more savage."

    scene bg RED

    show therion_swing
    show man_defend

    pause 0.76
    play sound "audio/bash1.mp3"
    scene black
    with hpunch

    pause 0.5

    en "...I do wonder which of them will hold out the longest against him."

    scene bg arena_day_lit_crowd
    with fade

    show eva normal_happy smile:
        zoom 0.068
        xanchor 0.5
        yanchor 1.0
        xpos 890
        ypos 447
        xzoom -1

        matrixcolor ColorizeMatrix("#ba7570", "#ba7570")

        crop (0, 0, 1.0, 0.57)
        crop_relative True


    show desmond stern:
        zoom 0.063
        xanchor 0.5
        yanchor 1.0
        xpos 1030
        ypos 447
        xzoom 1

        matrixcolor ColorizeMatrix("#ba7570", "#ba7570")

        crop (0, 0, 1.0, 0.57)
        crop_relative True

    show therion body1 browmad hair2 at center:
        zoom 0.23
        alpha 0.0
        xoffset -50
        yoffset 40
        ease 0.6 alpha 1.0
    with dissolve


    voice "VA/JEFFEREY/Announcer2.mp3"
    announcer "Victor of the trial, Sir Therion of Aelazath!"

    show layer master:
        subpixel True
        anchor (0.5, 0.5)
        pos (960, 540)
        zoom 1.0
        ease 4.0 zoom 3.3 xpos 960 ypos 900

    show therion body1 browmad hair2:
        ease 3.5 yoffset 1200 alpha 0.0

    show eva browneutral neutral:
        ease 4.0 matrixcolor IdentityMatrix()

    show desmond stern:
        ease 4.0 matrixcolor IdentityMatrix()

    pause 4.0

    en "Thank heavens the violence has stopped!"

    en "I say, was this contest not supposed to be wholly bloodless?"

    show eva calm browsad normal_happy what

    en "Why are the men on the sand not moving? Are they dead?"

    show desmond

    voice "VA/GARFUNKEL/Desmond5.mp3"
    de "Are you unwell?"

    show eva calm browsad normal_sad frown

    voice "VA/RAKUMAROO/Eva7.mp3"
    e "No, Archbishop. Only a little shaken."

    show desmond calm browmad normal angry

    voice "VA/GARFUNKEL/Desmond6.mp3"
    de "Excellent. Clear the sand, every last body off it. The Saintess shall not stand amidst such filth."

    en "...Bodies. So they are indeed dead."

    menu:
        "Ask that they be buried properly":

            show eva calm browsad normal_sad frown

            voice "VA/RAKUMAROO/Eva8.mp3"
            e "Archbishop, might the fallen at least be granted proper rites? They died in service of choosing my knight."

            show desmond calm browmad normal stern

            voice "VA/GARFUNKEL/Desmond7.mp3"
            de "They perished because they were inadequate. Rites are reserved for the faithful, not the fallen."

            show eva browneutral neutral
            show eva frown

            voice "VA/RAKUMAROO/Eva9.mp3"
            e "Of course, Archbishop. Forgive me."

            show desmond:
                easeout 1.5 xpos 1100 alpha 0.0
            pause 1.0

            en "He dismisses the thought without a second glance. Still, I suppose it was worth asking, at least."

            $ deluded_points += 1

        "Say nothing":

            show eva normal_happy browneutral neutral

            show desmond:
                easeout 1.5 xpos 1100 alpha 0.0
            pause 1.0

            en "It is not my place to question how the Archbishop conducts his arena."

            en "They lost, after all. There is precious little to mourn in that."

            $ monstrous_points += 1

    hide desmond
    show eva normal_happy browneutral neutral

    stop music fadeout 1.0

    en "I can hardly look away, even so."
    show layer master:
        subpixel True
        anchor (0.5, 0.5)
        zoom 3.3
        xpos 960
        ypos 900

        ease 2.5 zoom 2.2 xpos 960 ypos 680

    show therion body1 browneutral smile hair2:
        ease 2.5 yoffset 40 alpha 1.0 xoffset 40

    $ renpy.pause(2.5, hard=True)

    voice "VA/JASON/Therion1.mp3"
    t "My Lady. It's done."

    show therion body1 browneutral smile hair2:
        ease 0.8 yoffset 100

    en "He kneels directly before me, still bearing the stains of his trial, and offers his hand with ease."

    show eva calm browhappy normal_happy smile

    en "Goodness, what broad shoulders he has, even hunched down like that."

    show eva calm browsad normal_sad frown

    en "Yet I see a slight tremor there... Could he have sustained severe wounds?"

    voice "VA/RAKUMAROO/Eva10.mp3"
    e "... Are you quite all right, Sir Therion?"

    voice "VA/JASON/Therion2.mp3"
    t "Never better. Never better, My Lady."

    scene black
    with fade

    stop music fadeout 1.0

    play music "oath.mp3"

    scene bg temple_hall_day
    with fade


    show desmond browmad stern at left:
        xzoom -1
        zoom 0.22
        xanchor 0.5
        yanchor 1.0
        xpos 0.4
        yalign 1.0
        yoffset 0

        block:
            ease 3.0 yoffset 10
            ease 3.0 yoffset -5
            repeat

    en "They take him away to be seen to, and we move from the arena towards the grand temple hall."

    show therion body0 browneutral frown hair1 at right:
        zoom 0.23
        xoffset -290
        yoffset 0

    with dissolve

    en "When he reappears, freshly washed and armoured, traces of blood still linger here and there. Clearly, the attendants have not been terribly thorough."

    en "That won't do. We need to fix that later."

    show layer master:
        subpixel True
        anchor (0.5, 0.5)
        pos (960, 540)
        zoom 1.0

        ease 3.0 zoom 1.6 xpos 790 ypos 700

    pause 3.0

    show therion body0 browmad closed:
        transform_anchor True
        yanchor 1.0
        ease 1.2 rotate -5 yoffset 50

    en "The Archbishop holds a bible over his head as he pronounces the vows."

    voice "VA/GARFUNKEL/Desmond8.mp3"
    de "Therion. Do you swear, before this court and before the Saintess herself, to guard her life above your own, in all places, at all times, without exception?"

    voice "VA/JASON/Therion3.mp3"
    t "I swear it."

    voice "VA/GARFUNKEL/Desmond9.mp3"
    de "Do you swear to place her safety before your own comfort, your own desires, your own name, for as long as you hold this post?"

    voice "VA/JASON/Therion4.mp3"
    t "I do."

    voice "VA/GARFUNKEL/Desmond11.mp3"
    de "You will surrender your sword arm to her needs. Your sleep to her watch. Your breath to her last. Speak it."

    voice "VA/JASON/Therion5.mp3"
    t "I will surrender my sword arm, my sleep, my breath."

    show therion browmad shook smile with dissolve

    voice "VA/JASON/Therion6.mp3"
    t "... My entire life."

    show therion body0 browmad closed
    with dissolve

    en "Well. That last part is not in the oath at all. I would know, I have read it many times."

    en "Yet that sounds really romantic isn't it?"

    voice "VA/GARFUNKEL/Desmond12.mp3"
    de "Then rise, Sir Therion. Sworn protector of the Saintess."

    show therion browneutral open with dissolve:
        transform_anchor True
        yanchor 1.0
        ease 1.2 rotate 0 yoffset 0

    en "He rises as instructed, though he pays the Archbishop absolutely no heed..."

    show layer master:
        subpixel True
        anchor (0.5, 0.5)
        zoom 1.6
        xpos 790
        ypos 700

        ease 1.5 zoom 2.5 xpos 300 ypos 700

    show therion browskeptical luvhalf smile with dissolve

    en "Oh, gracious me."

    en "...He has been looking at {i}me{/i} instead."

    en "Well, of course he is. He did just swear his oath to me, after all!"

    en "To be the center of such attention! I scarcely know where to look!"

    scene bg temple_corridor_day:
        zoom 1.4
        yoffset -250

    show eva browsad what blush at center with dissolve:
        zoom 0.4
        yoffset 300
        ease 0.3 xzoom 1
        block:
            ease 2.0 yoffset 305
            ease 2.0 yoffset 295
            repeat

    pause 1.0

    en "I recall from the chronicles that Saint Miriel once regarded her own champion in this manner."

    en "They wed before the year ended, and she forfeited her holy office completely."

    en "Fallen from grace due to a brief stare... Oh, how deeply mortifying!"

    show eva frown blush with dissolve

    en "Naturally, I am doing no such thing! I am merely... {w}looking. That is all!"

    en "My face is burning, though. Odd, considering the chill in here."

    show bg temple_corridor_day:
        ease 3.5 blur 12 zoom 1.45 yoffset -250

    show layer master:
        subpixel True
        anchor (0.5, 0.5)
        pos (960, 540)
        zoom 1.0

        ease 3.5 zoom 1.5 ypos 550

    en "His stare remains fixed upon me, dropping to my hands before swiftly rising to catch my gaze again. I don't know what he is searching for."

    show eva normal_sad

    en "Still, as I am the Saintess, I think it's acceptable. He must familiarize himself with the woman he protects. There is no other reason for it!"

    scene bg temple_hall_day
    with fade

    show desmond browmad stern at left:
        xzoom -1
        zoom 0.22
        xanchor 0.5
        yanchor 1.0
        xpos 0.4
        yalign 1.0
        yoffset 0

        # Idle float loop
        block:
            ease 3.0 yoffset 10
            ease 3.0 yoffset -5
            repeat


    show therion body0 browneutral frown hair1 at right:
        zoom 0.23
        xoffset -290
        yoffset 0

    with dissolve

    voice "VA/GARFUNKEL/Desmond13.mp3"
    de "That will be all, Sir Therion. Stand guard outside her door, just as the rest did. Matins shall relieve you."

    show therion browneutral annoyed with dissolve

    voice "VA/JASON/Therion7.mp3"
    t "Just outside, then?"

    show desmond browmad angry with dissolve

    voice "VA/GARFUNKEL/Desmond14.mp3"
    de "Did I stutter, lad?"

    show therion browneutral neutral with dissolve

    voice "VA/JASON/Therion8.mp3"
    t "No, my lord."

    show desmond browmad stern with dissolve

    voice "VA/GARFUNKEL/Desmond15.mp3"
    de "Then go."

    show therion:
        easeout 0.4 xoffset -240
        pause 0.15
        easeout 0.4 xoffset -190
        pause 0.15
        easeout 0.4 xoffset -140
        pause 0.3

        pause 0.2

        easeout 1.5 xoffset 150 alpha 0.0

    en "He backs away three full paces before turning around, still tracking me over his shoulder as if I might vanish."

    en "Charming. {w}Rather dramatic, but charming."

    show desmond:
        xzoom 1
        parallel:
            ease 1.5 xpos 0.55
        parallel:
            block:
                ease 3.0 yoffset 10
                ease 3.0 yoffset -5
                repeat

    show eva noblush browneutral neutral:
        xzoom -1
        zoom 0.25
        xanchor 0.5
        yanchor 1.0
        xpos -0.2
        yalign 1.0
        yoffset 0
        alpha 0.0

        parallel:
            easeout 1.5 xpos 0.25 alpha 1.0
        parallel:
            block:
                ease 3.0 yoffset 10
                ease 3.0 yoffset -5
                repeat

    show layer master:
        subpixel True
        anchor (0.5, 0.5)
        zoom 1.0
        xpos 960
        ypos 540

        ease 3.5 zoom 1.6 xpos 1250 ypos 600

    voice "VA/GARFUNKEL/Desmond16.mp3"
    de "Saintess."

    voice "VA/RAKUMAROO/Eva11.mp3"
    e "Yes, Archbishop?"

    show desmond browmad stern with dissolve

    voice "VA/GARFUNKEL/Desmond17.mp3"
    de "You are not to be alone with that man."

    show eva shocked with dissolve

    voice "VA/RAKUMAROO/Eva12.mp3"
    e "I beg your pardon?"

    voice "VA/GARFUNKEL/Desmond18.mp3"
    de "He is a fresh recruit and untried. I find him off-putting."

    voice "VA/GARFUNKEL/Desmond19.mp3"
    de "A proper meeting will be arranged once I am convinced he knows his boundaries."

    show eva browsad angry with dissolve

    en "Boundaries! As though I need managing. I am the Saintess, and he is my protector. Surely the arrangements between us are mine to make?"

    show eva browsad neutral with dissolve

    voice "VA/RAKUMAROO/Eva13.mp3"
    e "Of course, Archbishop. Whatever you think the best."

    en "I am lying through my teeth."

    scene black
    with fade

    en "Days pass."

    en "And he is simply everywhere."

    scene bg temple_corridor_day:
        blur 13
        zoom 1.35
        ease 8.0 zoom 1.5
    with dissolve

    show therion body0 hair2 at center:
        zoom 0.52
        xoffset 190
        yoffset 560
        blur 6

        parallel:
            easeout 0.65 yoffset 595
            easein 1.15 yoffset 560
            repeat
        parallel:
            ease 0.9 xoffset 196
            ease 0.9 xoffset 184
            repeat

    show eva browsad frown at center:
        zoom 0.72
        xoffset -150
        yoffset 960

        parallel:
            easeout 0.7 yoffset 945
            easein 0.7 yoffset 960
            repeat
        parallel:
            ease 1.4 xoffset -142
            ease 1.4 xoffset -158
            repeat
    with dissolve

    en "The passage by my quarters. The sanctuary... He's always three steps away, without fail."

    en "Ah, well. It is his duty to remain near. That is only proper."

    en "Yet duty alone fails to explain why he reaches every threshold seconds before I do, as if reading my very mind."

    scene bg temple_corridor_night:
        matrixcolor TintMatrix("#5a7099")
    with fade

    show therion body0 browneutral hair1 at right:
        zoom 0.23
        xoffset -200
        yoffset 0
        matrixcolor TintMatrix("#0b1326") * BrightnessMatrix(-0.6)

    show eva browsad neutral at left:
        xzoom -1
        zoom 0.25
        xoffset -400
        yoffset 40
        matrixcolor TintMatrix("#5a7099")

        easeout 1.5 xoffset 200

        block:
            ease 0.7 yoffset 30
            ease 0.7 yoffset 40
            repeat

    en "I changed my route down a random corridor for no real reason, and he was already waiting for me."

    show therion:
        ease 0.6 matrixcolor TintMatrix("#5a7099")
        parallel:
            easeout 0.5 xoffset -320
        parallel:
            easeout 0.5 yoffset 5
            easein 0.5 yoffset 0
    with dissolve

    scene black
    with fade

    en "I kept the change of plans entirely to myself."

    en "I expect seasoned fighters naturally pick up such tricks. Guessing where one might walk, and all that."

    en "Yes, that is it. He is merely terribly good at his work. Nothing more to it than that!"

    scene black
    with fade

    en "The Archbishop summons me before breakfast, which is never a good sign."

    play music "journey.mp3"

    scene bg temple_hall_day

    show layer master:
        subpixel True
        anchor (0.5, 0.5)
        zoom 1.7
        xpos 600
        ypos 500
    with fade

    show eva normal_happy what at right:
        xzoom 1
        zoom 0.25
        alpha 1.0
        xoffset -180
        yoffset 0
        block:
            ease 2.0 yoffset -16
            ease 2.0 yoffset 0
            repeat

    show desmond browmad stern:
        xzoom -1
        zoom 0.22
        xanchor 0.5
        yanchor 1.0
        xpos 0.5
        yalign 1.0
        yoffset 184
        alpha 1.0
        rotate 0
        block:
            ease 3.0 yoffset 160
            ease 3.0 yoffset 184
            repeat
    with dissolve

    voice "VA/RAKUMAROO/Eva14.mp3"
    e "Were you looking for me, Archbishop?"

    voice "VA/GARFUNKEL/Desmond20.mp3"
    de "There is a village two days west. Murrayfield."

    show desmond browmad stern with dissolve

    voice "VA/GARFUNKEL/Desmond21.mp3"
    de "They have strayed from the light. Theft, violence... The usual moral decay."

    show eva browsad shocked with dissolve

    voice "VA/RAKUMAROO/Eva15.mp3"
    e "How dreadful. Have they fallen back into savagery, then?"

    voice "VA/GARFUNKEL/Desmond22.mp3"
    de "Indeed. You will see them cleansed completely. Every soul, Saintess. Not merely the ringleaders."

    show eva browsad what with dissolve

    voice "VA/RAKUMAROO/Eva16.mp3"
    e "The entire village? Good heavens, Archbishop, however many souls is that?"

    voice "VA/GARFUNKEL/Desmond23.mp3"
    de "Enough to require your presence."

    show eva browsad frown with dissolve

    voice "VA/RAKUMAROO/Eva17.mp3"
    e "Am I sufficient for such a task on my own?"

    show desmond browmad angry with dissolve

    voice "VA/GARFUNKEL/Desmond24.mp3"
    de "I shouldn't have to remind you that faith in your office is maintained by results."

    show eva browsad neutral with dissolve

    voice "VA/RAKUMAROO/Eva18.mp3"
    e "Yes, Archbishop."

    show desmond browsad neutral with dissolve

    voice "VA/GARFUNKEL/Desmond25.mp3"
    de "See that no harm comes to you out there."

    show desmond browneutral neutral with dissolve

    voice "VA/GARFUNKEL/Desmond26.mp3"
    de "Therion accompanies you. Alongside a proper detachment of temple knights."


    voice "VA/JASON/Therion9.mp3"
    t "Don't need six idiots tripping over their own swords. I'll handle it."
    show layer master:
        subpixel True
        anchor (0.5, 0.5)
        zoom 1.3
        xpos 620
        ypos 600

    show eva:
        xzoom -1
        xoffset -290

        block:
            ease 2.0 yoffset -16
            ease 2.0 yoffset 0
            repeat

    show desmond:
        xoffset -70

        block:
            ease 3.0 yoffset 160
            ease 3.0 yoffset 184
            repeat
    with move

    show therion body0 browneutral annoyed behind eva:
        zoom 0.23
        xanchor 0.5
        yanchor 1.0
        xpos 0.85
        yalign 1.0
        yoffset 15
        xoffset 50

    with easeinright

    voice "VA/GARFUNKEL/Desmond27.mp3"
    de "You take the escort assigned, boy, or she leaves with them while you remain."

    show therion browmad annoyed with dissolve

    voice "VA/JASON/Therion10.mp3"
    t "With respect, my lord, they'll slow me down. Can't keep her safe if I'm babysitting half the garrison."

    show desmond browmad grit with dissolve

    voice "VA/GARFUNKEL/Desmond28.mp3"
    de "You do not dictate the terms in my house."

    show eva browsad what with dissolve:
        xzoom 1
        block:
            ease 2.0 yoffset -16
            ease 2.0 yoffset 0
            repeat

    voice "VA/RAKUMAROO/Eva19.mp3"
    e "Archbishop, truly, I think Sir Therion may be right!"

    show desmond shocked agitated browmad angry with hpunch:
        block:
            ease 3.0 yoffset 160
            ease 3.0 yoffset 184
            repeat

    voice "VA/GARFUNKEL/Desmond29.mp3"
    de "No! You will not go anywhere alone with that man. I forbid it, Ev— Saintess!"

    show eva browsad shocked with dissolve:
        block:
            ease 2.0 yoffset -16
            ease 2.0 yoffset 0
            repeat

    en "... Oh."

    show desmond normal browsad neutral with dissolve:
        block:
            ease 3.0 yoffset 160
            ease 3.0 yoffset 184
            repeat
    
    voice "VA/GARFUNKEL/Desmond29a.mp3"
    de "...Saintess. Forgive me. Long morning."

    en "He never stumbles over his words. My mind, meanwhile, is busy devising an excuse to dismiss The Arcbishop's ideas for the upcoming journey."

    en "Oh, to be entirely alone with Sir Therion! We require a driver, naturally, but any further escorts would make it far too crowded."

    show eva browsad frown with dissolve:
        block:
            ease 2.0 yoffset -16
            ease 2.0 yoffset 0
            repeat

    voice "VA/RAKUMAROO/Eva20.mp3"
    e "But, Archbishop. Why waste temple forces on a simple village call? You saw how he fought during his trial!"

    show eva browsad what with dissolve:
        block:
            ease 2.0 yoffset -16
            ease 2.0 yoffset 0
            repeat

    voice "VA/RAKUMAROO/Eva21.mp3"
    e "The man could likely pacify Murrayfield before our soldiers even pack their rations!"

    voice "VA/RAKUMAROO/Eva22.mp3"
    e "And I am certain Sir Therion would far rather prove himself on his own than be propped up by men who could be protecting our holy capital instead!"

    show therion smug with dissolve

    voice "VA/JASON/Therion11.mp3"
    t "Damn right."

    show desmond closed browmad neutral with dissolve:
        block:
            ease 3.0 yoffset 160
            ease 3.0 yoffset 184
            repeat

    de "..."

    show desmond browsad neutral with dissolve:
        block:
            ease 3.0 yoffset 160
            ease 3.0 yoffset 184
            repeat

    voice "VA/GARFUNKEL/Desmond33.mp3"
    de "Fine. Take him."

    show desmond browneutral neutral with dissolve:
        block:
            ease 3.0 yoffset 160
            ease 3.0 yoffset 184
            repeat

    voice "VA/GARFUNKEL/Desmond32.mp3"
    de "See it done within the week. Both of you."

    show desmond:
        xzoom 1
        parallel:
            easeout 2.0 xpos -0.3 alpha 0.0
        parallel:
            ease 0.3 rotate -10
        parallel:
            block:
                ease 0.5 yoffset 170
                ease 0.5 yoffset 184
                repeat

    pause 2.0

    stop music fadeout 0.5

    scene black
    with fade

    en "Gracious me, I am in an absolute state today. This anxiety makes stomaching my morning meal entirely impossible"

    en "The Archbishop sends his finest carriage regardless, bless his soul."

    stop music fadeout 0.5

    scene black
    show carriage_bg_a as carriage_bg_a zorder 0:
        xpos 0
        linear 20.0 xpos 1920
        repeat
    show carriage_bg_b as carriage_bg_b zorder 0:
        xpos -1920
        linear 20.0 xpos 0
        repeat
    show carriage_therion body brownormal normal frown as therion_cg at carriage_therion_bob zorder 10
    show carriage_frame at carriage_sway zorder 20
    show carriage_eva body wings brownormal normal smile as eva_cg at carriage_sway zorder 30
    with dissolve

    play music "therion.mp3"

    en "Therion is barred from sitting inside with me, of course. So he rides parallel, close enough that I could reach through the window frame and touch his armour."

    en "It seems such a pity. The carriage fits four comfortably, and I do far better with company."

    # carriage + therion anim starts here

    voice "VA/RAKUMAROO/Eva23.mp3"
    e "Sir Therion, you will wear down the path if you ride any closer!"

    show carriage_therion body brownormal normal oh as therion_cg with dissolve

    voice "VA/JASON/Therion12.mp3"
    t "I'm keeping my eyes on you till we die, Saintess. Try and stop me."

    show carriage_eva body wings brownormal normal oh as eva_cg with dissolve

    en "My word, what a terribly wild thing to say to a holy maiden!"

    show carriage_eva body wings brownormal normal smile as eva_cg with dissolve

    en "... But I don't mind it."

    show carriage_eva body wings browsad half oh as eva_cg with dissolve

    en "Goodness, what a thought for a Saintess to have."

    show expression Solid("#ff8c1a33") as orange_overlay zorder 25
    with fade


    show carriage_therion body brownormal normal frown as therion_cg with dissolve
    show carriage_eva body wings brownormal normal smile as eva_cg with dissolve

    t "..."

    e "..."

    t "..."

    voice "VA/RAKUMAROO/Eva24.mp3"
    e "You have had a balance of two words together since we departed. Are you sulking, or merely dull company today?"

    show carriage_therion body browfurrow half frown as therion_cg with dissolve

    voice "VA/JASON/Therion13.mp3"
    t "Counting, Saintess."

    show carriage_eva body wings brownormal normal oh as eva_cg with dissolve

    voice "VA/RAKUMAROO/Eva25.mp3"
    e "Counting what, pray tell?"

    voice "VA/JASON/Therion14.mp3"
    t "Your breaths, my lady. Every one since noon. Four thousand six hundred and twelve."

    show carriage_eva body wings brownormal normal oh as eva_cg with dissolve

    voice "VA/RAKUMAROO/Eva26.mp3"
    e "You have been counting my breathing?"

    show carriage_therion body browfurrow normal smile as therion_cg with dissolve

    voice "VA/JASON/Therion15.mp3"
    t "Means you're alive, Saintess. Alive means safe. Safe means I'm doing my job."

    show carriage_therion body browangry normal grin as therion_cg with dissolve

    voice "VA/JASON/Therion16.mp3"
    t "That count slips even once, I kill whatever made it slip. Don't give a damn what it is."

    show carriage_eva body wings browsad normal oh as eva_cg with dissolve

    voice "VA/RAKUMAROO/Eva27.mp3"
    e "You have truly thought through this entire dreadful business, haven't you?"

    voice "VA/JASON/Therion17.mp3"
    t "Anyone touches you loses the limb. Stare too long at my charge, I cut the sight right out of their skull. That oughtta teach ‘em a lesson."

    show carriage_eva body wings browsad normal oh as eva_cg with dissolve

    voice "VA/RAKUMAROO/Eva28.mp3"
    e "My word!"

    show carriage_therion body browfurrow normal oh as therion_cg with dissolve

    voice "VA/JASON/Therion18.mp3"
    t "You asked, Saintess. Just being honest."

    menu:
        "Let Him":

            show carriage_eva body wings brownormal normal smile as eva_cg with dissolve

            voice "VA/RAKUMAROO/Eva29.mp3"
            e "Well! I shan't complain of being so carefully guarded. Carry on, Sir Therion."

            en "If he insists on watching me so closely, who am I to stop him?"

            $ monstrous_points += 1

        "Forbid Him":

            show carriage_eva body wings browsad normal oh as eva_cg with dissolve

            voice "VA/RAKUMAROO/Eva30.mp3"
            e "Dear me, counting every breath? You will drive yourself mad if you keep that up."

            show carriage_therion body browfurrow half grin as therion_cg with dissolve

            voice "VA/JASON/Therion19.mp3"
            t "... Heh. What a funny thing to say, My Lady."

            show carriage_eva body wings browsad half smile as eva_cg with dissolve

            en "I cannot find it in myself to forbid him, seeing how deeply he treasures the duty."

            $ deluded_points += 1

    show carriage_therion body brownormal normal frown as therion_cg with dissolve
    show carriage_eva body wings browsad normal smile as eva_cg with dissolve

    en "And he speaks of slaughter as lightly as one mentions the weather."

    en "It sounds awfully like a soul in urgent need of guidance, does it not?"

    show carriage_eva body wings brownormal normal smile as eva_cg with dissolve

    en "Hmm... I am entirely certain I can teach him gentler ways."

    en "Guiding him toward virtue will be a marvelous endeavour!"


    en "The final stretch passes without event, though Sir Therion scans the treeline constantly."


    show carriage_bg_a at carriage_sway:
        matrixcolor TintMatrix("#5a7099") * BrightnessMatrix(-0.30)
        xpos 0
        linear 20.0 xpos 1920
        repeat

    show carriage_bg_b at carriage_sway:
        matrixcolor TintMatrix("#5a7099") * BrightnessMatrix(-0.30)
        xpos -1920
        linear 20.0 xpos 0
        repeat

    show carriage_therion body brownormal normal smile as therion_cg zorder 10:
        matrixcolor TintMatrix("#5a7099") * BrightnessMatrix(-0.20)

    show carriage_frame zorder 20 at carriage_sway:
        matrixcolor TintMatrix("#5a7099") * BrightnessMatrix(-0.35)

    show carriage_eva body wings brownormal normal smile as eva_cg zorder 30:
        matrixcolor TintMatrix("#5a7099") * BrightnessMatrix(-0.20)
    with dissolve


    en "Murrayfield emerges just as night falls upon the road. Fitting, really. As though the town hid until the daylight perished."
    play music "village.mp3"

    scene bg village_night
    with fade

    $ current_frame = "twisted"

    show eva closed_sad frown browneutral at left:
        xzoom -1
        zoom 0.25
        xoffset 180
        yoffset 40
        matrixcolor TintMatrix("#5a7099")
        block:
            ease 2.0 yoffset -16
            ease 2.0 yoffset 0
            repeat

    show therion body0 browneutral frown hair1 behind villager1_sway:
        xzoom -1
        zoom 0.24
        xanchor 0.5
        yanchor 1.0
        xpos 0.41
        yalign 1.0
        yoffset 40
        matrixcolor TintMatrix("#5a7099")
    with dissolve

    en "Mercy, the utter neglect. One would imagine the living abandoned this pit decades ago."

    show eva agitated yandere_sad browsad shocked with dissolve:
        block:
            ease 2.0 yoffset -16
            ease 2.0 yoffset 0
            repeat

    show villager1_sway:
        zoom 0.25
        xanchor 0.5
        yanchor 1.0
        yalign 1.0
        yoffset 40
        xpos 1.2
        easein 0.8 xpos 0.65

    pause 0.4

    show villager2_sway:
        zoom 0.24
        xanchor 0.5
        yanchor 1.0
        yalign 1.0
        yoffset 40
        xpos 1.2
        easein 0.8 xpos 0.76

    pause 0.4

    show villager3_sway:
        zoom 0.26
        xanchor 0.5
        yanchor 1.0
        yalign 1.0
        yoffset 40
        xpos 1.2
        easein 0.8 xpos 0.87

    en "I hear something moving in the darkness. A few shadows walking closer."

    show therion browmad annoyed with dissolve

    voice "VA/JASON/Therion20.mp3"
    t "Behind me, Saintess. Right now."

    show eva browmad smile with dissolve

    voice "VA/RAKUMAROO/Eva31.mp3"
    e "I am hardly made of glass, Sir Therion."

    show therion laugh with dissolve

    voice "VA/JASON/Therion21.mp3"
    t "Ha. Glass? You're a diamond, Milady."
    play sound "audio/shing.mp3"
    scene bg village_reveal
    show therioncg reveal
    pause 4.8

    en "He ignores the standard knightly longsword in favour of that wicked scythe, unclasping it one-handed and sweeping the curved steel low against the grass."

    en "He looks like something straight out of the ancient paintings."

    en "Paintings of the angel of death, that is."

    voice "VA/JASON/Therion22.mp3"
    t "Let me deal with these fu— these filth."

    menu:
        "Try to purify the criminals":

            voice "VA/RAKUMAROO/Eva32.mp3"
            e "Wait! Let me try— they needn't die for this!"

            en "But alas, as I try to purify them, they raise their weapons higher."
            en "These barbarians have no interest in salvation. They rush towards us like hounds."

            $ deluded_points += 1

        "Step aside":

            en "If he insists."

            en "I step back and let Therion handle it. A Saintess needn't dirty her own hands."

            $ monstrous_points += 1
    play sound "audio/whoosh.mp3"

    show bg village_jump
    show therioncg jump
    pause 0.7

    scene bg RED


    show dummy_idle at fit_canvas
    pause 0.1


    show dummy_idle as dummy at fit_canvas
    pause 0.1

    show therion_slash_seq at therion_swing_move
    pause 0.10

    play sound "audio/slash.mp3"

    show dummy_cut as dummy at fit_canvas
    hide dummy_idle
    pause 0.0005

    show slash_impact_flash at fit_canvas
    show layer master at hpunch
    pause 0.15

    hide therion_slash_seq
    hide slash_impact_flash
    hide dummy
    hide dummy_cut

    show dummy_top at dummy_top_away
    show dummy_bottom at dummy_bottom_away
    pause 0.7

    hide dummy_top
    hide dummy_bottom
    pause 0.3

    scene black
    with fade

    pause 0.3

    play sound "audio/slashes.mp3"


    show barrage_slash_1 as burst at slash_nudge(-140, -70)
    pause 0.24

    hide burst
    show barrage_slash_2 as burst at slash_nudge(160, 50)
    pause 0.24

    hide burst
    show barrage_slash_3 as burst at slash_nudge(-80, 10)
    pause 0.26

    hide burst
    show barrage_finisher_x1
    show barrage_finisher_x2
    show barrage_flash
    show layer master at hpunch
    pause 0.45

    hide barrage_finisher_x1
    hide barrage_finisher_x2
    hide barrage_flash

    pause 0.35

    en "The slaughter ends quickly. Limbs are severed away with terrifying ease."

    show eva browsad neutral at eva_face_zoom
    show blood_evangeline at blood_zoom_still
    with Dissolve(0.4)
    en "Heavens, I fear those awful sounds will stay with me forever."

    show eva browmad neutral at eva_face_zoom

    en "...Now my own duty begins. A settlement left to wallow in sin becomes utterly tainted."

    en "And such profound corruption requires eradication, not salvation."

    show eva browsad frown at eva_face_zoom with dissolve
    en "How very dreadful."

    show eva browsad frown with Dissolve(0.4)

    # Slower, cinematic camera zoom into the touch point
    show layer master:
        subpixel True
        anchor (0.521, 0.481)
        pos (1001, 520)
        zoom 1.0
        pause 0.2
        easein_quad 1.2 zoom 2.0 anchor (0.521, 0.380) pos (1001, 410)

    en "Therion faces me once more, sets down the weapon, and uses his thumb to wipe a stray droplet of blood from my face."

    show eva shocked blush at eva_face_zoom
    show blood_evangeline at blood_zoom_still
    show therion_hand at hand_wipe_rest
    with Dissolve(0.4)

    en "Oh my! S-Since when did that land there?"

    pause 0.7

    hide blood_evangeline with Dissolve(0.5)

    voice "VA/JASON/Therion23.mp3"
    t "Hold still, my lady. Got some filthy stuff on you. Lemme get it off."

    show eva browhappy blush at eva_face_zoom with dissolve
    en "His hand is rough, yet he is terribly gentle about it. Far gentler than a man wielding such a weapon has any right to be."

    hide therion_hand with dissolve

    show layer master:
        subpixel True
        zoom 2.0
        anchor (0.521, 0.380)
        pos (1001, 410)
        ease 2.0 zoom 1.0 anchor (0.5, 0.5) pos (960, 540)

    en "My heart is still racing from the attack."

    show eva browsad neutral blush with dissolve

    en "Yet how strange that it races faster still even after his hand moves away."
    scene bg village_night:
        subpixel True
        anchor (0.5, 0.5)
        zoom 1.5
        xpos 0.5
        ypos 0.5
    with fade

    show eva browsad oh blush:
        subpixel True
        xzoom -1
        zoom 0.55
        xanchor 0.5
        yanchor 1.0
        xpos 0.30
        yalign 1.0
        yoffset 800
        matrixcolor TintMatrix("#5a7099")
        block:
            ease 2.0 yoffset 734
            ease 2.0 yoffset 750
            repeat

    show therion body0 browneutral frown hair1:
        subpixel True
        zoom 0.58
        xanchor 0.5
        yanchor 1.0
        xpos 0.70
        yalign 1.0
        yoffset 1000
        matrixcolor TintMatrix("#5a7099")
    with dissolve

    voice "VA/RAKUMAROO/Eva33.mp3"
    e "T-Thank you, Therion. Good heavens, are you uninjured? Let me check you!"

    show therion smile with dissolve

    voice "VA/JASON/Therion24.mp3"
    t "Never better, my lady. Never in my whole sorry life."

    show eva browhappy smile blush with dissolve

    voice "VA/RAKUMAROO/Eva34.mp3"
    e "I... yes. Splendid."

    show therion laugh with dissolve

    voice "VA/JASON/Therion25.mp3"
    t "Heh."

    show therion browneutral neutral with dissolve

    en "He laughs, snapping his wrist to send the last drop of blood flying into the grass."


    show eva browneutral neutral with dissolve

    en "Once the slaughter ceases, the locals emerge from their hovels, gathering in the square, row upon row."

    show eva browsad frown with dissolve

    en "Good heavens, what a crowd! Look at those pale, miserable faces! Not a single smile to be found!"

    show eva browhappy neutral with dissolve

    en "How my heart aches for them. We absolutely must put an end to this nightmare without delay!"

    show therion browmad frown with dissolve

    voice "VA/JASON/Therion26.mp3"
    t "Saintess."

    show eva browhappy frown with dissolve

    voice "VA/RAKUMAROO/Eva35.mp3"
    e "Yes, Therion?"

    voice "VA/JASON/Therion27.mp3"
    t "Third row. Bloke on the end. Don't like his face."

    show eva browsad what with dissolve

    voice "VA/RAKUMAROO/Eva36.mp3"
    e "He is only nervous, Sir Therion. They all are."

    show therion shook browmad grin with dissolve

    voice "VA/JASON/Therion28.mp3"
    t "I can fix that for you. Permanently."

    show eva browmad angry with dissolve

    voice "VA/RAKUMAROO/Eva37.mp3"
    e "You shall do no such thing, Therion! We are here to rescue these people, not terrorise them!"

    show therion browskeptical annoyed half with dissolve

    voice "VA/JASON/Therion29.mp3"
    t "Right. Yeah. Whatever you say, Saintess."

    # Base layer setup
    show layer master:
        subpixel True
        anchor (0.5, 0.5) pos (960, 540) zoom 1.0

    scene bg village_night_loop at village_bg_push

    show therion body0 browneutral open neutral hair2 at therion_behind:
        matrixcolor TintMatrix("#5a7099")
    show eva calm browmad normal_happy shocked  at eva_float:
        matrixcolor TintMatrix("#5a7099")

    show villager1 at villager1_pov
    show villager2 at villager2_pov
    show villager3 at villager3_pov
    with fade

    voice "VA/RAKUMAROO/Eva38.mp3"
    e "Be not afraid, my good people! I am here, and not a single one of you need to carry your burdens a moment longer!"

    voice "VA/RAKUMAROO/Eva39.mp3"
    e "Hold your heads high! I intend to see every last one of you set right before the night ends."

    $ renpy.pause(1.5, hard=True)

    hide villager1
    hide villager2
    hide villager3

    en "Some are openly weeping as I speak... Oh, the poor dears, to have waited so long in such misery."

    # GAMEPLAY: purification minigame
    call purification_minigame from _call_purification_minigame


    voice "VA/RAKUMAROO/Eva40.mp3"
    e "There now! Do you not feel ever so much better?"

    show villager_woman at villager_hop(VWOMAN_X)
    voice "VA/SOPHIE/Woman1.mp3"
    woman "Yes, Saintess."

    show villager_man at villager_hop(VMAN_X)
    voice "VA/JEFFEREY/Man1.mp3"
    man "Praise be the Saintess!"

    show villager_lady at villager_wobble_out(VLADY_X, -800)
    pause 0.6
    show villager_woman at villager_wobble_out(VWOMAN_X, 700)
    pause 0.6
    show villager_man at villager_wobble_out(VMAN_X, 1400, 2.8)

    en "Look at how happy they appear now!"

    hide villager_lady
    hide villager_woman
    hide villager_man

    pause 2.5

    en "I am so profoundly grateful we arrived in time!"

    scene bg village_night_loop:
        subpixel True
        anchor (0.5, 0.5)
        zoom 1.5
        xpos 0.5
        ypos 0.5
        blur 6
        matrixcolor TintMatrix("#5a7099")
    with fade

    show therion shook grin hair2 at center:
        subpixel True
        zoom 0.52
        xoffset 320
        yoffset 760
        blur 12
        matrixcolor TintMatrix("#5a7099") * BrightnessMatrix(-0.35)
        block:
            pause 0.25
            xoffset 321 yoffset 761
            pause 0.20
            xoffset 319 yoffset 759
            pause 0.30
            xoffset 322 yoffset 761
            pause 0.22
            xoffset 319 yoffset 760
            repeat

    show eva browsad frown at center:
        subpixel True
        zoom 0.72
        xoffset -180
        yoffset 1180
        matrixcolor TintMatrix("#5a7099")

    with dissolve

    voice "VA/JASON/Therion30.mp3"
    t "The light..."

    en "I hear him muttering behind my shoulder, so softly I am likely not intended to catch it."

    show therion shook grin hair2:
        subpixel True
        zoom 0.52
        xoffset 320
        yoffset 760
        blur 12
        matrixcolor TintMatrix("#5a7099") * BrightnessMatrix(-0.35)
        block:
            pause 0.18
            xoffset 322 yoffset 761
            pause 0.15
            xoffset 318 yoffset 759
            pause 0.20
            xoffset 322 yoffset 762
            pause 0.16
            xoffset 318 yoffset 760
            repeat

    voice "VA/JASON/Therion31.mp3"
    t "Yeah, my light... my light..."

    show eva what with dissolve:
        subpixel True
        zoom 0.72
        xoffset -180
        yoffset 1180
        matrixcolor TintMatrix("#5a7099")
        xzoom -1

    with dissolve

    voice "VA/RAKUMAROO/Eva41.mp3"
    e "Did you say something, Therion?"

    show therion luvhalf browsad frown hair1:
        subpixel True
        zoom 0.52
        xoffset 320
        yoffset 760
        blur 0
        matrixcolor TintMatrix("#5a7099") * BrightnessMatrix(0)
    with dissolve

    voice "VA/JASON/Therion32.mp3"
    t "No, Saintess. Talking to myself."

    show eva browsad what with dissolve

    en "Hmm."

    en "The smiles do not sit entirely naturally on a few of them. A touch too stretched, perhaps."

    show eva browsad neutral with dissolve

    en "Curious. I suppose the shadows play tricks upon my vision."

    scene black
    with fade

    en "I make my way to the carriage, Therion tracking my steps. He extends his arm to steady me."

    voice "VA/JASON/Therion33.mp3"
    t "In you get, my lady. Sit. Damn, you look wiped."

    show carriage_bg_a as carriage_bg_a zorder 0:
        matrixcolor TintMatrix("#5a7099") * BrightnessMatrix(-0.30)
        xpos 0
        linear 20.0 xpos 1920
        repeat
    show carriage_bg_b as carriage_bg_b zorder 0:
        matrixcolor TintMatrix("#5a7099") * BrightnessMatrix(-0.30)
        xpos -1920
        linear 20.0 xpos 0
        repeat


    show carriage_therion body browfurrow normal frown as therion_cg zorder 10:
        matrixcolor TintMatrix("#5a7099") * BrightnessMatrix(-0.20)

    show carriage_frame zorder 20:
        matrixcolor TintMatrix("#5a7099") * BrightnessMatrix(-0.35)

    show carriage_eva body wings brownormal normal oh as eva_cg zorder 30:
        matrixcolor TintMatrix("#5a7099") * BrightnessMatrix(-0.20)
    with dissolve

    
    show carriage_eva body wings brownormal normal smile as eva_cg with dissolve

    voice "VA/RAKUMAROO/Eva42.mp3"
    e "I am entirely well, Sir Therion, truly! It was a routine purification, I have performed dozens of them!"

    show carriage_therion body brownormal normal smile as therion_cg with dissolve

    voice "VA/JASON/Therion34.mp3"
    t "Yeah, well, every one of 'em drains you. Close your eyes. I'll be right here."

    show carriage_therion body brownormal normal smile as therion_cg at carriage_therion_bob zorder 10:
        matrixcolor TintMatrix("#5a7099") * BrightnessMatrix(-0.20)

    show carriage_frame at carriage_sway zorder 20:
        matrixcolor TintMatrix("#5a7099") * BrightnessMatrix(-0.35)

    show carriage_eva body wings brownormal normal smile as eva_cg at carriage_sway zorder 30:
        matrixcolor TintMatrix("#5a7099") * BrightnessMatrix(-0.20)

    voice "VA/RAKUMAROO/Eva43.mp3"
    e "Right here doing what, precisely?"

    show carriage_therion body browfurrow normal frown as therion_cg with dissolve

    voice "VA/JASON/Therion35.mp3"
    t "Staring down the road, staring at you. No difference to me."

    show carriage_eva body wings browsad half oh as eva_cg with dissolve

    voice "VA/RAKUMAROO/Eva44.mp3"
    e "Are you saying you plan to watch me sleep?"

    show carriage_therion body browfurrow half oh as therion_cg with dissolve

    voice "VA/JASON/Therion36.mp3"
    t "Did I... fuck, did I say something bad? Damn it. I mean, if you hate it, my lady, I'll turn around—"

    show carriage_eva body wings brownormal normal smile as eva_cg with dissolve

    voice "VA/RAKUMAROO/Eva45.mp3"
    e "It is a thoroughly bizarre way to offer protection, Therion."

    show carriage_therion body browfurrow yandere yan as therion_cg with dissolve

    voice "VA/JASON/Therion37.mp3"
    t "Bizarre, yeah?"

    show carriage_eva body wings browsad half oh as eva_cg with dissolve

    voice "VA/JASON/Therion38.mp3"
    t "Hehe... Then change me. Command it, and I'll break myself into whatever pleases you."

    
    en "... Oh dear."

    stop music fadeout 1.0

    # END OF CHAPTER ONE

    jump morning_intrusion

label test_animations:

    scene black

    show eva calm neutral normal_happy neutral:
        zoom 0.3333
        xanchor 0.5
        xalign 0.5
        yanchor 1.0
        yalign 1.0
        ease 3.5 yoffset -30
        ease 3.5 yoffset 0
        repeat
    "Eva test anim."
    pause
    hide eva

    show therion neutral:
        zoom 0.2857
        xanchor 0.5
        xalign 0.5
        yanchor 1.0
        yalign 1.0
    "Therion test anim."
    pause
    hide therion

    show desmond calm neutral normal neutral:
        zoom 0.2422
        xanchor 0.5
        xalign 0.5
        yanchor 1.0
        yalign 1.0
        ease 2.0 yoffset -30
        ease 2.0 yoffset 0
        repeat
    "Desmond test anim."
    pause
    hide desmond

    show vidius calm neutral normal neutral:
        zoom 0.25
        xanchor 0.5
        xalign 0.5
        yanchor 1.0
        yalign 1.0
        ease 2.0 yoffset -30
        ease 2.0 yoffset 0
        repeat
    "Vidius test anim."
    pause
    hide vidius

    $ persistent.ending_any = True
    return

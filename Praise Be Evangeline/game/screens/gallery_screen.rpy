### GALLERY SCREEN ############################################################
##
##

############################################################
### SETUP ###
############################################################
transform ts_gal_resize():
    fit "contain"
    xsize 1920


default persistent.cg1_seen = False
default persistent.cg2_seen = False
default persistent.cg3_seen = False
default persistent.cg4_seen = False

default persistent.cgending_death_seen = False
default persistent.cgending_therionexplode_seen = False

default persistent.cg_horrortownspeople_seen = False
default persistent.cg_womanscream_seen = False
default persistent.cg_therionmouth_seen = False
default persistent.cg_creepytherion_seen = False

init python:
    GAL_THUMB_SIZE = (335, 188)
    GAL_BTN_SIZE = (355, 207)

    gal = Gallery()

    gal.idle_border = "gui/gallery/gal_idle_foreground.webp"
    gal.hover_border = "gui/gallery/gal_hover_foreground1.webp"
    gal.locked_button = "gui/gallery/gal_locked.webp"



    GAL_BTNS = [
        "cg1", "cg3", "cg4",
        "cgending_death", "cgending_therionexplode",
        "cg_horrortownspeople", "cg_womanscream", "cg_therionmouth", "cg_creepytherion",
        "cg_glory"
    ]
    ### Add CGs ########
    # TODO: Replace to diff persistents if wanted
    ## CG1
    gal.button("cg1")
    gal.condition("persistent.cg1_seen or persistent.ending_any")
    gal.image("cg1")

    ## CG3
    gal.button("cg3")
    gal.condition("persistent.cg3_seen or persistent.ending_any")
    gal.image("cg3")


    ## CG4
    gal.button("cg4")
    gal.condition("persistent.cg4_seen or persistent.ending_any")
    gal.image("cg4")


    ### ENDINGS
    gal.button("cgending_death")
    gal.condition("persistent.cgending_death_seen or persistent.ending_ruins")
    gal.image("cgending_death")


    gal.button("cgending_therionexplode")
    gal.condition("persistent.cgending_therionexplode_seen or persistent.ending_ruins")
    gal.image("cgending_therionexplode")


    ### MISC
    gal.button("cg_horrortownspeople")
    gal.condition("persistent.cg_horrortownspeople_seen or persistent.ending_any")
    gal.image("cg_horrortownspeople")

    gal.button("cg_womanscream")
    gal.condition("persistent.cg_womanscream_seen or persistent.ending_any")
    gal.image("cg_womanscream")

    gal.button("cg_therionmouth")
    gal.condition("persistent.cg_therionmouth_seen or persistent.ending_any")
    gal.image("cg_therionmouth")

    gal.button("cg_creepytherion")
    gal.condition("persistent.cg_creepytherion_seen or persistent.ending_any")
    gal.image("cg_creepytherion")

    gal.button("cg_glory")
    gal.condition("persistent.ending_glory")
    gal.image("cg_glory")



## IMAGES THAT YOU WILL BE SHOWING IN GAME
image cg1 = Transform("cgs/cg1_placeholder.webp", fit="contain", xsize=1920)
image cg3 = Transform("cgs/cg2.webp", fit="contain", xsize=1920)
image cg4 = Transform("cgs/battle.webp", fit="contain", xsize=1920)

## ENDINGS
image cgending_death = Transform("cgs/ruins2.webp", fit="contain", xsize=1920)
image cgending_therionexplode = Transform("cgs/ruins1.webp", fit="contain", xsize=1920)

image cg_horrortownspeople = Transform("cgs/HORROR_townspeoplemerged.webp", fit="contain", xsize=1920)
image cg_womanscream = Transform("cgs/woman_scream_placeholder.webp", fit="contain", xsize=1920)
image cg_therionmouth = Transform("cgs/therion_mouth_merged_placeholder.webp", fit="contain", xsize=1920)
image cg_creepytherion = Transform("cgs/creepy_therion_placeholder.webp", fit="contain", xsize=1920)

image cg_glory = Transform("cgs/glory.webp", fit="contain", xsize=1920)

############################################################
### SCREEN ###
############################################################
# TODO: have it only display some using page end

screen gallery():
    default page = 0

    tag storybook_frame

    style_prefix "gallery"

    add "menu_background"

    frame:
        background "gui/gallery/gallery_frame.webp"
        xysize (1254, 729)
        align (0.5, 0.5)

        label _("GALLERY")

        ## images
        $ start = page * 6
        $ end = start + 6

        grid 3 2:
            align (0.5, 0.5)
            for btn in GAL_BTNS[start:end]:
                fixed:
                    xysize GAL_BTN_SIZE
                    add "gui/gallery/gal_idle_background.webp"
                    add gal.make_button(btn, AlphaMask(Transform(btn, xysize=GAL_BTN_SIZE), mask="gui/gallery/gal_mask.webp"))


        ## PAGES ##
        hbox:
            xalign 0.5 yalign 1.0 yoffset -50
            spacing 50
            for i in range(0, 2):
                textbutton "{}".format(i + 1):
                    if current_frame == "twisted" or last_known_frame == "twisted":
                        text_hover_color TWISTED_COLOR
                        text_selected_color TWISTED_COLOR
                    elif current_frame == "dream" or last_known_frame == "dream":
                        text_hover_color DREAM_COLOR
                        text_selected_color DREAM_COLOR
                    elif current_frame == "horror" or last_known_frame == "horror":
                        text_hover_color HORROR_COLOR
                        text_selected_color HORROR_COLOR
                    action SetScreenVariable("page", i)


    ## STORY FRAME ##
    use storybook_frame()

    ## REUTRN BUTTON ##
    button:
        xysize (522, 82)
        xoffset -115
        ypos 25
        padding (150, 20, 25, 15)
        background "gui/frame_round_brown.webp"
        foreground Transform("gui/qm/arrow_idle_icon.webp", yalign=0.5, xpos=180)
        hover_foreground Transform("return_hover_arrow", yalign=0.5, xpos=180)
        text _("RETURN"):
            xpos 100
            hover_italic True
            idle_color GOLD
            if current_frame == "twisted" or last_known_frame == "twisted":
                hover_color TWISTED_COLOR
                
            elif current_frame == "dream" or last_known_frame == "dream":
                hover_color DREAM_COLOR
                
            elif current_frame == "horror" or last_known_frame == "horror":
                hover_color HORROR_COLOR
        keysym "game_menu"
        action (ShowMenu("main_menu_extras") if main_menu else Return())



############################################################
### STYLES ###
############################################################
style gallery_label:
    xalign 0.5
    ypos 15


style gallery_label_text:
    outlines [(3, GOLD, 0, 0)]
    color BROWN
    font NOTOSERIF

style gallery_button_text:
    size 35
    color BROWN
    hover_color BLUE
    selected_color BLUE
    font NOTOSERIF


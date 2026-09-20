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
        "cg1", "cg2", "cg3", "cg4",
        "cgending_death", "cgending_therionexplode",
        "cg_horrortownspeople", "cg_womanscream", "cg_therionmouth", "cg_creepytherion"
    ]
    ### Add CGs ########
    # TODO: Replace to diff persistents if wanted
    ## CG1
    gal.button("cg1")
    gal.condition("persistent.cg1_seen")
    gal.image("cg1")

    ## CG2
    gal.button("cg2")
    gal.condition("persistent.cg2_seen")
    gal.image("cg2")


    ## CG3
    gal.button("cg3")
    gal.condition("persistent.cg3_seen")
    gal.image("cg3")


    ## CG4
    gal.button("cg4")
    gal.condition("persistent.cg4_seen")
    gal.image("cg4")


    ### ENDINGS
    gal.button("cgending_death")
    gal.condition("persistent.cgending_death_seen")
    gal.image("cgending_death")


    gal.button("cgending_therionexplode")
    gal.condition("persistent.cgending_therionexplode_seen")
    gal.image("cgending_therionexplode")


    ### MISC
    gal.button("cg_horrortownspeople")
    gal.condition("persistent.cg_horrortownspeople_seen")
    gal.image("cg_horrortownspeople")

    gal.button("cg_womanscream")
    gal.condition("persistent.cg_womanscream_seen")
    gal.image("cg_womanscream")

    gal.button("cg_therionmouth")
    gal.condition("persistent.cg_therionmouth_seen")
    gal.image("cg_therionmouth")

    gal.button("cg_creepytherion")
    gal.condition("persistent.cg_creepytherion_seen")
    gal.image("cg_creepytherion")






## IMAGES THAT YOU WILL BE SHOWING IN GAME
image cg1 = Transform("cgs/cg1_placeholder.webp", fit="contain", xsize=1920)
image cg2 = Transform("cgs/cg2_placeholder.webp", fit="contain", xsize=1920)
image cg3 = Transform("cgs/cg3_placeholder.webp", fit="contain", xsize=1920)
image cg4 = Transform("cgs/cg4_placeholder.webp", fit="contain", xsize=1920)

## ENDINGS
image cgending_death = Transform("cgs/ending_death_placeholder.webp", fit="contain", xsize=1920)
image cgending_therionexplode = Transform("cgs/ending_therionexplode_placeholder.webp", fit="contain", xsize=1920)

image cg_horrortownspeople = Transform("cgs/horrortownspeople_placeholder.webp", fit="contain", xsize=1920)
image cg_womanscream = Transform("cgs/woman_scream_placeholder.webp", fit="contain", xsize=1920)
image cg_therionmouth = Transform("cgs/therion_mouth_merged_placeholder.webp", fit="contain", xsize=1920)
image cg_creepytherion = Transform("cgs/creepy_therion_placeholder.webp", fit="contain", xsize=1920)

############################################################
### SCREEN ###
############################################################
# TODO: have it only display some using page end

screen gallery():
    default page = 0
    
    tag menu

    style_prefix "gallery"

    # TODO: Make this change later.
    add "gui/menu_background1.webp"

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
            for i in range(1, 3):
                textbutton "{}".format(i) action NullAction()


    ### RETURN BTN ###
    


############################################################
### STYLES ###
############################################################
style gallery_label:
    xalign 0.5
    ypos 15


style gallery_label_text:
    outlines [(3, GOLD, 0, 0)]
    color BROWN

style gallery_button_text:
    size 35
    color BROWN
    hover_color BLUE


## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save
## https://www.renpy.org/doc/html/screen_special.html#load


## The width and height of thumbnails used by the save slots.
define config.thumbnail_width = 264
define config.thumbnail_height = 148

define config.autosave_slots = 1

screen save():

    tag storybook_frame

    use file_slots(_("Save"))


screen load():

    tag storybook_frame

    use file_slots(_("Load"))


screen file_slots(title):
    add "gui/menu_background1.webp"

    viewport id "slvp":
        draggable True mousewheel True pagekeys True
        scrollbars None

        xysize (900, 800)
        align (0.5, 0.5)

        has vbox:
            spacing 15

        # OTDO: ADd autosave if time
        for i in range(20):
            $ slot = i + 1

            button:
                style_prefix "slot"
                action FileAction(slot, page=1)

                hbox:
                    spacing 25
                    if FileLoadable(slot):
                        add AlphaMask(FileScreenshot(slot), mask="gui/button/slot_mask.webp")
                    else:
                        add "gui/button/slot_mask.webp"

                    vbox:
                        spacing 3

                        label "{:02}.".format(slot) + FileSaveName(slot).upper()
                        if FileLoadable(slot):
                            text FileTime(format="{#file_time}TIME: %r")
                            text FileTime(format="{#file_time}DATE: %x")
                        else:
                            text _("TIME: --:--:--")
                            text _("DATE: --/--/--")



    ## SCROLLBAR ##
    vbar value YScrollValue("slvp"):
        ysize 1080
        xpos 1613


    ## STORYBOOK
    use storybook_frame()

    ## REUTRN BUTTON ##
    button:
        xysize (522, 82)
        xoffset -115
        ypos 25
        padding (150, 20, 25, 15)
        background "gui/frame_round_brown.webp"
        foreground Transform("gui/qm/arrow_[prefix_]icon.webp", yalign=0.5, xpos=180)
        text _("RETURN"):
            xpos 100
            idle_color GOLD
            hover_color BLUE
        
        
        action Return()



############################################################
### STYLES ###
############################################################
style slot_button:
    xysize (880, 206)
    background "gui/button/slot_[prefix_]background.webp"
    padding (30, 27)

style slot_label_text:
    insensitive_color GRAY
    color BROWN
    insensitive_outlines [(3, "#00000000", 0, 0)]
    outlines [(3, GOLD, 0, 0)]
    hover_outlines [(3, BLUE, 0, 0)]
    size 35

style slot_text:
    insensitive_color GRAY
    color BROWN
    size 25



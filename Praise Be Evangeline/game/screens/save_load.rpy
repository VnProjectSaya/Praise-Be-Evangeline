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
    add "menu_background"

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
                            text FileTime(slot, format="{#file_time}TIME: %r")
                            text FileTime(slot, format="{#file_time}DATE: %x")
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
        foreground Transform("gui/qm/arrow_idle_icon.webp", yalign=0.5, xpos=180)
        hover_foreground Transform("return_hover_arrow", yalign=0.5, xpos=180)
        text _("RETURN"):
            xpos 100
            idle_color GOLD
            if current_frame == "twisted" or last_known_frame == "twisted":
                hover_color TWISTED_COLOR
                
            elif current_frame == "dream" or last_known_frame == "dream":
                hover_color DREAM_COLOR
                
            elif current_frame == "horror" or last_known_frame == "horror":
                hover_color HORROR_COLOR

        keysym "game_menu"
        action Return()



############################################################
### STYLES ###
############################################################
image slot_hover_button = ConditionSwitch(
    "current_frame == 'twisted' or last_known_frame == 'twisted'", "gui/button/slot_hover_background_twisted.webp",
    "current_frame == 'dream' or last_known_frame == 'dream'", "gui/button/slot_hover_background_dream.webp",
    "current_frame == 'horror' or last_known_frame == 'horror'", "gui/button/slot_hover_background_horror.webp",
)
style slot_button:
    xysize (880, 206)
    idle_background "gui/button/slot_idle_background.webp"
    hover_background "slot_hover_button"
    insensitive_background "gui/button/slot_insensitive_background.webp"
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



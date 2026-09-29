
## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action


style choice_vbox:
    xalign 0.5
    ypos 405
    yanchor 0.5
    spacing 33

image choice_hover_background = ConditionSwitch(
    "current_frame == 'twisted' or last_known_frame == 'twisted'", "gui/button/choice_hover_background_twisted.png",
    "current_frame == 'dream' or last_known_frame == 'dream'", "gui/button/choice_hover_background_dream.png",
    "current_frame == 'horror' or last_known_frame == 'horror'", "gui/button/choice_hover_background_horror.png",
)
style choice_button:
    is default # This means it doesn't use the usual button styling
    xminimum 600
    ysize 126
    background Frame("gui/button/choice_idle_background.png", 340, 0, 74, 0)
    hover_background Frame("choice_hover_background", 340, 0, 74, 0)
    insensitive_background Frame(Transform("gui/button/choice_idle_background.png", matrixcolor=SaturationMatrix(0.0)), 340, 0, 74, 0)
    padding (135, 35, 75, 35)

style choice_button_text:
    is default # This means it doesn't use the usual button text styling
    xalign 0.5 yalign 0.5
    color BROWN
    hover_italic True
    size 25
    font "gui/font/NotoSerif-Regular.ttf"

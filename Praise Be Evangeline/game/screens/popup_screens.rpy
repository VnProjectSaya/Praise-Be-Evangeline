
## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm


        

screen confirm(message, yes_action, no_action=None):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "#310e0084"

    vbox:
        spacing 25
        align (0.5, 0.5)

        frame:

            label _("ATTENTION"):
                xalign 0.5
                
                style "pref_label"

            text _(message) style "confirm_prompt"

            hbox:
                xalign 0.5 xoffset -50 yalign 1.0 yoffset -25
                spacing 35
                textbutton _("CONFIRM"):
                    action yes_action
                # Modified so you can just have a confirmation prompt
                if no_action is not None:
                    textbutton _("CANCEL"):
                        action no_action

    ## Right-click and escape answer "no".
    if no_action is not None:
        key "game_menu" action no_action
    else:
        key "game_menu" action yes_action

style confirm_frame:
    xsize 774
    ysize 325
    background Frame("gui/popup_frame.webp", 5, 100)
    padding (40, 35, 40, 35)
    xalign 0.5
    yalign 0.5

style confirm_vbox:
    align (0.5, 0.5)
    spacing 45


style confirm_prompt:
    textalign 0.5
    align (0.5, 0.5)
    size 25
    color BROWN
    font NOTOSERIF



style confirm_button:
    # xalign 0.5
    left_padding 65
    hover_foreground "gui/button/confirm_hover_foreground.webp"

style confirm_button_text:
    textalign 0.5
    font NOTOSERIF
    hover_italic True
    color BROWN
    hover_color BLUE
    


## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:
        has hbox

        text _("Skipping")

        text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
        text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
        text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## This transform is used to blink the arrows one after another.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat

style skip_hbox:
    spacing 9

style skip_frame:
    is empty
    ypos 15
    background Frame("gui/skip.png", 24, 8, 75, 8, tile=False)
    padding (24, 8, 75, 8)

style skip_text:
    size 24

style skip_triangle:
    is skip_text
    ## We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
    ## glyph in it.
    font "DejaVuSans.ttf"

## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        yoffset 0
        linear .25 yoffset 165
    on hide:
        linear .5 yoffset 0


style notify_frame:
    is empty
    xminimum 465
    anchor (0.5, 1.0) pos (0.5, 0.0)
    background Frame("gui/notify.webp", 60, 138, 60, 40, tile=False)
    padding (60, 110, 60, 30)

style notify_text:
    color "#6d4d3f"
    text_align 0.5 xalign 0.5
    line_spacing -2
    size 16




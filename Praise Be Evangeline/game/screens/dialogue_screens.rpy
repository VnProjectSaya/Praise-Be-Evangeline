
## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

default persistent.dialogue_alpha = 1.0

screen say(who, what):
    style_prefix "say"

    window:
        id "window"
        background Transform(Image("gui/textbox.png", xalign=0.5, yalign=1.0), alpha=persistent.dialogue_alpha)

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what" font persistent.dialogue_typeface color persistent.dialogue_color

    ## If there's a side image, display it in front of the text.
    add SideImage() xalign 0.0 yalign 1.0


## Make the namebox available for styling through the Character object.
init python:
    config.character_id_prefixes.append('namebox')

# Style for the dialogue window
style window:
    xalign 0.5
    yalign 1.0
    xysize (1231, 277)
    padding (40, 10, 40, 40)
    

# Style for the dialogue
style say_dialogue:
    adjust_spacing False
    ypos 60

# The style for dialogue said by the narrator
style say_thought:
    is say_dialogue

# Style for the box containing the speaker's name
style namebox:
    xpos 20
    xysize (None, None)
    background Frame("gui/namebox.png", 5, 5, 5, 5, tile=False, xalign=0.0)
    padding (5, 5, 5, 5)

# Style for the text with the speaker's name
style say_label:
    color '#f93c3e'
    xalign 0.0
    yalign 0.5
    size gui.name_text_size
    font gui.name_text_font


## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.
default persistent.expend_quick_menu = True

screen quick_menu():

    ## Ensure this appears on top of other screens.
    zorder 100

    if quick_menu:
        frame:
            background Frame("gui/frame_round_brown.webp", 20, 0, 20, 0)
            padding (40, 20, 123, 0) ysize 82
            anchor (1.0, 1.0) pos (1.0, 1.0) yoffset -32
            if persistent.expend_quick_menu:
                at transform:
                    ease 0.5 xoffset 56
            else:
                at transform:
                    ease 0.5 xoffset 450
            hbox:
                style_prefix "quick"
                align (0.0, 0.5) ysize 35 spacing 0

                use qm_button("back", _("Back"), Rollback())
                null width 2
                use qm_button("auto", _("Auto Forward"), Preference("auto-forward", "toggle"))
                null width 5
                use qm_button("skip", _("Skip"), Skip(), Skip(fast=True, confirm=True))
                null width 2
                use qm_button("log", _("History"), ShowMenu('history'))
                null width 12
                use qm_button("settings", _("Settings"), ShowMenu('preferences'))
                null width 20
                use qm_button("save", _("Save"), ShowMenu('save'))
                null width 20
                use qm_button("load", _("Load"), ShowMenu('load'))
                null width 18
                use qm_button("home", _("Main Menu"), MainMenu())
        fixed:
            xysize (35, 35) anchor (1.0,  1.0) pos (1.0, 1.0) offset (-2, -55)
            at transform:
                xzoom (-1.0 if persistent.expend_quick_menu else 1.0)
            use qm_button("arrow", _("Expand Quick Menu"), ToggleVariable("persistent.expend_quick_menu"))

screen qm_button(image_name, alt_text, action, alt_action=None):
    button:
        xysize (35, 35)
        background "gui/qm/{0}_idle_icon.webp".format(image_name)
        hover_background "gui/qm/{0}_hover_icon.webp".format(image_name)
        insensitive_background "gui/qm/{0}_insensitive_icon.webp".format(image_name)
        alt alt_text
        action action
        alternate alt_action
        at transform:
            ease 0.5 alpha (1.0 if persistent.expend_quick_menu or image_name == 'arrow' else -1.0)

## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_hbox:
    xalign 0.5
    yalign 1.0 yoffset -8
    spacing 8

style quick_button:
    background None
    padding (15, 6, 15, 0)

style quick_button_text:
    size 21
    selected_color '#f93c3e'
    idle_color "#aaa"

## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox
        spacing 15

        use nvl_dialogue(dialogue)

        ## Displays the menu, if given. The menu may be displayed incorrectly if
        ## config.narrator_menu is set to True.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit True

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## This controls the maximum number of NVL-mode entries that can be displayed at
## once.
define config.nvl_list_length = 6

# The style for the NVL "textbox"
style nvl_window:
    is default
    xfill True yfill True
    background "gui/nvl.png"
    padding (0, 15, 0, 30)

# The style for the text of the speaker's name
style nvl_label:
    is say_label
    xpos 645 xanchor 1.0
    ypos 0 yanchor 0.0
    xsize 225
    min_width 225
    textalign 1.0

# The style for dialogue in NVL
style nvl_dialogue:
    is say_dialogue
    xpos 675
    ypos 12
    xsize 885
    min_width 885

# The style for dialogue said by the narrator in NVL
style nvl_thought:
    is nvl_dialogue

style nvl_button:
    xpos 675
    xanchor 0.0


## Bubble screen ###############################################################
##
## The bubble screen is used to display dialogue to the player when using speech
## bubbles. The bubble screen takes the same parameters as the say screen, must
## create a displayable with the id of "what", and can create displayables with
## the "namebox", "who", and "window" ids.
##
## https://www.renpy.org/doc/html/bubble.html#bubble-screen

init python:
    def character_bubble_callback(image_tag):
        eva_image_tag = getattr(store, "e").image_tag
        theri_image_tag = getattr(store, "t").image_tag

        if image_tag == eva_image_tag:
            return ["eva_bottom_left", "eva_bottom_right", "eva_top_left", "eva_top_right", "eva_thought"]
        elif image_tag == theri_image_tag:
            return ["theri_bottom_left", "theri_bottom_right", "theri_top_left", "theri_top_right", "theri_thought"]
        else:
            return ["bottom_left", "bottom_right", "top_left", "top_right", "thought"]

define bubble.properties_callback = character_bubble_callback

image bubble_ctc:
    "gui/bubbles/ctc.webp"
    alpha 0.0 anchor (0.5, 0.0) pos (0.5, 1.0)
    parallel:
        ease 0.6 alpha 1.0

    parallel:
        ease 0.5 yoffset 3
        ease 0.5 yoffset 0
        repeat

screen bubble(who, what):
    style_prefix "bubble"
    default ctc = None

    window:
        id "window"
        at transform:
            alpha 1.0
        vbox:
            spacing 0

            if who is not None:

                window:
                    id "namebox"
                    style "bubble_namebox"

                    text who.upper():
                        id "who"

            text what:
                id "what"
                font persistent.dialogue_typeface
                color persistent.dialogue_color
        showif ctc:
            add "bubble_ctc"

style bubble_window:
    is empty
    xpadding 30
    padding (50, 60, 50, 70)

style bubble_namebox:
    is empty
    xalign 0.0
    top_padding 10

style bubble_who:
    is default
    xalign 0.0
    textalign 0.0
    color "#644628"
    outlines [(1, "#ddb654", 0, 0)]
    size 30

style bubble_what:
    is default
    align (0.0, 0.0)
    text_align 0.0
    #layout "subtitle"
    color "#6d4d3f"
    line_spacing -2
    size 16

define bubble.frame = Frame("gui/bubble.png", 55, 55, 55, 95)
define bubble.thoughtframe = Frame("gui/thoughtbubble.png", 55, 55, 55, 55)

define bubble.properties = {
    "bottom_left" : {
        "window_background" : Frame("gui/Bubble_Text/basic_bottom_left.webp", 150, 60, 150, 50),
        "window_xpadding" : 80,
        "window_bottom_padding" : 50,
        "window_top_padding" : 40,
    },

    "bottom_right" : {
        "window_background" : Frame("gui/Bubble_Text/basic_bottom_right.webp", 150, 60, 150, 50),
        "window_xpadding" : 80,
        "window_bottom_padding" : 50,
        "window_top_padding" : 40,
    },

    "top_left" : {
        "window_background" : Frame("gui/Bubble_Text/basic_top_left.webp", 150, 50, 150, 60),
        "window_xpadding" : 80,
        "window_bottom_padding" : 80,
        "window_top_padding" : 20,
    },

    "top_right" : {
        "window_background" : Frame("gui/Bubble_Text/basic_top_right.webp", 150, 50, 150, 60),
        "window_xpadding" : 80,
        "window_bottom_padding" : 80,
        "window_top_padding" : 20,
    },

    "thought" : {
        "window_background" : Frame("gui/Bubble_Text/Textbox/basic_textbox.webp", 257, 113, 257, 118),
        "window_xpadding" : 80,
        "window_bottom_padding" : 40,
        "window_top_padding" : 20,
    },

    "eva_bottom_left" : {
        "window_background" : Frame("gui/Bubble_Text/eva_bottom_left.webp", 80, 150, 80, 100),
        "window_bottom_padding" : 40,
        "window_top_padding" : 40,
    },

    "eva_bottom_right" : {
        "window_background" : Frame("gui/Bubble_Text/eva_bottom_right.webp", 80, 150, 80, 100),
        "window_bottom_padding" : 40,
        "window_top_padding" : 40,
    },

    "eva_top_left" : {
        "window_background" : Frame("gui/Bubble_Text/eva_top_left.webp", 80, 100, 80, 150),
        "window_top_padding" : 20,
    },

    "eva_top_right" : {
        "window_background" : Frame("gui/Bubble_Text/eva_top_right.webp", 80, 100, 80, 150),
        "window_top_padding" : 20,
    },

    "eva_thought" : {
        "window_background" : Frame("gui/Bubble_Text/Textbox/eva_textbox.webp", 80, 100, 80, 100),
        "window_top_padding" : 20,
        "window_bottom_padding" : 50,
    },

    "theri_bottom_left" : {
        "window_background" : Frame("gui/Bubble_Text/therion_bottom_left.webp", 80, 150, 80, 100),
        "window_bottom_padding" : 50,
        "window_top_padding" : 40,
    },

    "theri_bottom_right" : {
        "window_background" : Frame("gui/Bubble_Text/therion_bottom_right.webp", 80, 150, 80, 100),
        "window_bottom_padding" : 50,
        "window_top_padding" : 40,
    },

    "theri_top_left" : {
        "window_background" : Frame("gui/Bubble_Text/therion_top_left.webp", 80, 100, 80, 150),
        "window_top_padding" : 20,
    },

    "theri_top_right" : {
        "window_background" : Frame("gui/Bubble_Text/therion_top_right.webp", 80, 100, 80, 150),
        "window_top_padding" : 20,
    },

    "theri_thought" : {
        "window_background" : Frame("gui/Bubble_Text/Textbox/therion_textbox.webp", 80, 100, 80, 100),
        "window_top_padding" : 20,
        "window_bottom_padding" : 50,
    }
}

define bubble.expand_area = {
    "bottom_left" : (0, 0, 0, 22),
    "bottom_right" : (0, 0, 0, 22),
    "top_left" : (0, 22, 0, 0),
    "top_right" : (0, 22, 0, 0),
    "thought" : (0, 0, 0, 0),
}

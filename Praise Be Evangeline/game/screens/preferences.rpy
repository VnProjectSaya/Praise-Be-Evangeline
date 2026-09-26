
## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

############################################################
### SETUP ###
############################################################
init python:
    DEFAULT_AUTO_TIME = {
        25 : "Slow",
        15 : "Medium",
        5 : "Fast"
    }

    DEFAULT_FONT = {
        # path : title
        DEJAVU : "DejaVuSans",
        ATKINSON : "Atkinson-Hyperlegible-Regular",
        OPENDYS : "_OpenDyslexic3-Regular.ttf",
        NOTOSERIF : "gui/font/NotoSerif-Regular.ttf"
    }

    FONT_TITLE = {
        # path : title
        DEJAVU : "DejaVuSans",
        ATKINSON : "Atkinson-Hyperlegible",
        OPENDYS : "OpenDys",
        NOTOSERIF : "Default"
    }

    DEFAULT_TEXT_SPEED = {
        25 : "Slow",
        35 : "Medium",
        45 : "Fast",
        0 : "Instant"

    }

    def set_new_dialogue_color(picker):
        store.persistent.dialogue_color = picker.color.hexcode
        renpy.restart_interaction()

    def reset_dialogue_color(picker):
        picker.color = BROWN
        store.persistent.dialogue_color = BROWN
        renpy.restart_interaction()

default text_colorwheel = ColorPicker(400, 115,
    start_color = persistent.dialogue_color,
    mouseup_callback=set_new_dialogue_color
)

style cpicker_bar:
    xysize (400, 25)

    base_bar At("cpicker_base_bar", spectrum())
    thumb Transform(WHITE, xsize=5)
    left_gutter 5
    right_gutter 5

############################################################
### SCREEN ###
############################################################

screen preferences():
    tag storybook_frame

    # TODO: Make to change w var
    add "gui/menu_background1.webp"

    style_prefix "pref"

    hbox:
        xsize 1550
        align (0.5, 0.5)



        # GENERAL #
        frame:
            vbox:
                label _("GENERAL")

                null height 35

                grid 2 5:
                    text _("FULLSCREEN")
                    imagebutton auto "gui/button/check_%s_foreground.webp" action Preference("display", "toggle") align (1.0, 0.5)

                    text _("SHOW TRANSITIONS")
                    imagebutton auto "gui/button/check_%s_foreground.webp" action Preference("transitions", "toggle") align (1.0, 0.5)

                    text _("SKIP UNSEEN TEXT")
                    imagebutton auto "gui/button/check_%s_foreground.webp" action Preference("skip", "toggle") align (1.0, 0.5)

                    text _("SKIP AFTER CHOICES")
                    imagebutton auto "gui/button/check_%s_foreground.webp" action Preference("after choices", "toggle") align (1.0, 0.5)

                    text _("AUTO-WAIT TIME") xsize 145
                    hbox:
                        imagebutton auto "gui/button/left_%s_arrow.webp" action CycleField(preferences, "afm_time", list(DEFAULT_AUTO_TIME.keys()), reverse=True) align (0.0, 0.5)

                        text DEFAULT_AUTO_TIME[preferences.afm_time] xalign 0.5

                        imagebutton auto "gui/button/right_%s_arrow.webp" action CycleField(preferences, "afm_time", list(DEFAULT_AUTO_TIME.keys())) align (1.0, 0.5)

        # AUDIO #
        frame:
            vbox:
                label _("AUDIO")

                null height 35

                vbox:
                    spacing 5

                    $ bgmvol = int(preferences.get_mixer("music") * 100)
                    text _("BGM : {}%".format(bgmvol))
                    bar value Preference("music volume") style "pref_bar"

                    null height 15

                    $sfxvol = int(preferences.get_mixer("sfx") * 100)
                    text _("SFX : {}%".format(sfxvol))
                    bar value Preference("sound volume") style "pref_bar"



        # ACCESS #
        frame:
            vbox:
                label _("ACCESSIBILITY")

                null height 35

                vbox:
                    spacing 5

                    hbox:
                        xsize 400
                        xfill True

                        text _("TYPEFACE")
                        hbox:
                            imagebutton auto "gui/button/left_%s_arrow.webp" action CycleField(persistent, "dialogue_typeface", list(DEFAULT_FONT.keys()), reverse=True), Function(text_preview.update_text) align (0.0, 0.5)

                            text FONT_TITLE[persistent.dialogue_typeface] xalign 0.5 xsize 100 size 20

                            imagebutton auto "gui/button/right_%s_arrow.webp" action CycleField(persistent, "dialogue_typeface", list(DEFAULT_FONT.keys())), Function(text_preview.update_text) align (1.0, 0.5)

                    null height 10

                    vbox:
                        spacing 3
                        hbox:
                            xsize 400
                            xfill True

                            text _("TYPEFACE COLOR")
                            textbutton _("RESET"):
                                align (1.0, 1.0)

                                action Function(reset_dialogue_color, picker=text_colorwheel)

                                text_insensitive_color GRAY
                                text_color BROWN
                                text_hover_color BLUE
                                text_size 20
                        add text_colorwheel
                        bar value FieldValue(text_colorwheel, "hue_rotation", 1.0):
                            style "cpicker_bar"
                            xalign 0.5
                            released Function(text_preview.update_text)

                    null height 10

                    hbox:
                        xalign 0.0
                        xsize 400
                        text _("TEXT SPEED")
                        hbox:
                            xalign 1.0
                            imagebutton auto "gui/button/left_%s_arrow.webp" action CycleField(preferences, "text_cps", list(DEFAULT_TEXT_SPEED.keys()), reverse=True), Function(text_preview.update_text) align (0.0, 0.5)

                            text DEFAULT_TEXT_SPEED[preferences.text_cps] xalign 0.5

                            imagebutton auto "gui/button/right_%s_arrow.webp" action CycleField(preferences, "text_cps", list(DEFAULT_TEXT_SPEED.keys())), Function(text_preview.update_text) align (1.0, 0.5)

                    null height 10

                    $ tbalpha = int(persistent.dialogue_alpha * 100)
                    text _("TEXTBOX OPACITY : {}%".format(tbalpha))
                    bar value FieldValue(persistent, "dialogue_alpha", range=1.0) style "pref_bar"

                    null height 10

                    add text_preview:
                        xsize 400









    ## STORY FRAME ##
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
        keysym "game_menu"
        action Return()


### PREF
style pref_frame:
    xysize (514, 729)
    background Frame("gui/settings_frame.webp")
    padding (25, 15)

style pref_vbox:
    spacing 25
    xalign 0.5


style pref_grid:
    xfill True
    xsize 400
    yspacing 5

style pref_label:
    xalign 0.5

style pref_label_text:
    size 30
    font NOTOSERIF
    color BROWN
    outlines [(1, GOLD, 0, 0)]


style pref_text:
    font NOTOSERIF
    color BROWN
    size 25
    xsize 350
    yalign 0.5


style pref_hbox:
    xsize 180
    xfill True
    align (1.0, 0.5)

style pref_bar:
    is bar
    xsize 400


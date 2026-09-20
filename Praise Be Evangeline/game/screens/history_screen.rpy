
## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

define config.history_length = 250

image eva_pfp = "gui/log/eva_portrait.webp"
image therion_pfp = "gui/log/therion_portrait.webp"
image desmond_pfp = "gui/log/desmond_portrait.webp"
image vidius_pfp = "gui/log/vidius_portrait.webp"
image npc_pfp = "gui/log/npc_portrait.webp"

screen history():

    tag storybook_frame

    ## Avoid predicting this screen, as it can be very large.
    predict False

    add "gui/menu_background1.webp"

    
    viewport id "histvp":
        xysize (1200, 670)
        align (0.5, 0.5) xoffset 50

        mousewheel True draggable True pagekeys True
        scrollbars None yinitial 1.0

        has vbox:
            spacing 35

        style_prefix "history"

        for h in _history_list:
            if h.who == "Evangeline":
                hbox:
                    add "eva_pfp"
                    frame:
                        
                        background Frame("gui/Bubble_Text/eva_top_left.webp", 250, 70)

                        has vbox:
                            spacing 10

                        label h.who style "history_name":
                            substitute False
                            if "color" in h.who_args:
                                text_color h.who_args["color"]

                        $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                        text what:
                            substitute False
                            color persistent.dialogue_color
                            font persistent.dialogue_typeface

            elif h.who is not None:
                hbox:
                    frame:
                       
                        if h.who == "Therion":
                            background Frame("gui/Bubble_Text/therion_top_right.webp", 250, 70)
                        else:
                            background Frame("gui/Bubble_Text/basic_top_right.webp", 250, 70)

                        has vbox:
                            spacing 10

                        label h.who style "history_name":
                            substitute False
                            if "color" in h.who_args:
                                text_color h.who_args["color"]

                        $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                        text what:
                            substitute False
                            color persistent.dialogue_color
                            font persistent.dialogue_typeface

                    if h.who == "Therion":
                        add "therion_pfp"
                    elif h.who == "Desmond":
                        add "desmond_pfp"
                    elif h.who == "Bishop Vidius":
                        add "vidius_pfp"
                    else:
                        add "npc_pfp"

            elif h.who is None:
                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False
                    color persistent.dialogue_color
                    font persistent.dialogue_typeface
                    xsize 400
                    xalign 0.5

        if not _history_list:
            label _("The dialogue history is empty.")

    ## SCROLLBAR ##
    vbar value YScrollValue("histvp"):
        ysize 1080
        xpos 1613

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
            
        action Return()



## This determines what tags are allowed to be displayed on the history screen.

define gui.history_allow_tags = { "alt", "noalt", "rt", "rb", "art" }


style history_hbox:
    xsize 1000
    xfill True

style history_name:
    xalign 0.0

style history_name_text:
    size 30
    font NOTOSERIF
    outlines [(2, GOLD, 0, 0)]

style history_frame:
    xsize 800
    yminimum 250
    padding (70, 25)

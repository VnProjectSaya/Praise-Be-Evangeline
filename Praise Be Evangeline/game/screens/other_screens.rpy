
## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

## Text that is placed on the game's about screen. Place the text between the
## triple-quotes, and leave a blank line between paragraphs.

define gui.about = _p("""
EasyRenPyGui is made by {a=https://github.com/shawna-p}Feniks{/a} {a=https://feniksdev.com/}@feniksdev.com{/a}
""")


screen about():

    tag menu

    add "#21212db2" # The background; can be whatever

    use game_menu(_("About"))

    viewport:
        style_prefix 'game_menu'
        mousewheel True draggable True pagekeys True
        scrollbars "vertical"

        has vbox
        style_prefix "about"

        label "[config.name!t]"
        text _("Version [config.version!t]\n")

        if gui.about:
            text "[gui.about!t]\n"

        text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")


style about_label_text:
    size 36


## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.
screen help():
    tag storybook_frame

    # TODO: Make to change w var
    add "gui/menu_background1.webp"

    
    style_prefix "pref"

    hbox:
        xsize 1550
        align (0.5, 0.5)
        
        

        # KEYBOARD #
        frame:
            vbox:
                label _("KEYBOARD")

                null height 35
                
                viewport id "kbvp":
                    draggable True mousewheel True pagekeys True
                    scrollbars None 

                    ysize 500
                        

                    grid 2 12:
                        style_prefix "help"
                        
                        label _("Enter")
                        text _("Advances dialogue and activates the interface.")

                    
                        label _("Space")
                        text _("Advances dialogue without selecting choices.")

                    
                        label _("Arrow Keys")
                        text _("Navigate the interface.")

                    
                        label _("Escape")
                        text _("Accesses the game menu.")

                    
                        label _("Ctrl")
                        text _("Skips dialogue while held down.")

                    
                        label _("Tab")
                        text _("Toggles dialogue skipping.")

                    
                        label _("Page Up")
                        text _("Rolls back to earlier dialogue.")

                    
                        label _("Page Down")
                        text _("Rolls forward to later dialogue.")

                    
                        label "H"
                        text _("Hides the user interface.")

                    
                        label "S"
                        text _("Takes a screenshot.")

                    
                        label "V"
                        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")

                    
                        label "Shift+A"
                        text _("Opens the accessibility menu.")


            ## SCROLLBAR ##
            vbar value YScrollValue("kbvp"):
                ypos 85
                ysize 500
                xalign 1.0 xoffset 25
                top_gutter 0
                bottom_gutter 0

        # MOUSE #
        frame:
            vbox:
                label _("MOUSE")

                null height 35

                viewport id "mousevp":
                    draggable True mousewheel True pagekeys True
                    scrollbars None 

                    ysize 500

                    grid 2 5:
                        style_prefix "help"
                        label _("Left Click")
                        text _("Advances dialogue and activates the interface.")

                        label _("Middle Click")
                        text _("Hides the user interface.")

                        label _("Right Click")
                        text _("Accesses the game menu.")

                        label _("Mouse Wheel Up\nClick Rollback Side")
                        text _("Rolls back to earlier dialogue.")

                        label _("Mouse Wheel Down")
                        text _("Rolls forward to later dialogue.")

            ## SCROLLBAR ##
            vbar value YScrollValue("mousevp"):
                ypos 85
                ysize 500
                xalign 1.0 xoffset 25
                top_gutter 0
                bottom_gutter 0



        # GAMEPAD #
        if GamepadExists():
            frame:
                vbox:
                    label _("GAMEPAD")

                    null height 35

                    viewport id "gpvp":
                        draggable True mousewheel True pagekeys True
                        scrollbars None 

                        ysize 500

                        grid 2 6:
                            style_prefix "help"

                            label _("Right Trigger\nA/Bottom Button")
                            text _("Advances dialogue and activates the interface.")

                            label _("Left Trigger\nLeft Shoulder")
                            text _("Rolls back to earlier dialogue.")

                            label _("Right Shoulder")
                            text _("Rolls forward to later dialogue.")


                            label _("D-Pad, Sticks")
                            text _("Navigate the interface.")

                            label _("Start, Guide, B/Right Button")
                            text _("Accesses the game menu.")

                            label _("Y/Top Button")
                            text _("Hides the user interface.")

                        
                    
                    textbutton _("Calibrate") action GamepadCalibrate() style "help_button"

                ## SCROLLBAR ##
                vbar value YScrollValue("gpvp"):
                    ypos 85
                    ysize 500
                    xalign 1.0 xoffset 25
                    top_gutter 0
                    bottom_gutter 0
                    
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


      


# style help_button:
#     xmargin 12

# style help_label:
#     xsize 375
#     right_padding 30

# style help_label_text:
#     xalign 1.0
#     textalign 1.0

style help_grid:
    xfill True
    xsize 400
    ysize 500
    
    xspacing -25
    yspacing 25

style help_label_text:
    underline True
    size 20
    color BROWN
    xsize 125

style help_text:
    color BROWN
    size 20

style help_button:
    xalign 0.5
    yoffset -15

style help_button_text:
    color BROWN
    hover_color BLUE
    font NOTOSERIF

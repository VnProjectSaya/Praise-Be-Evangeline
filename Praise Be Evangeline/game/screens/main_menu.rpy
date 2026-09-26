
## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

## Replace this with your background image, if you like
default persistent.main_menu = 1 # TODO: Change this to the correct one as needed and update conditions below.

image main_menu_background = ConditionSwitch(
    "persistent.main_menu == 1", "gui/MM1.PNG",
    "persistent.main_menu == 2", "gui/MM2.PNG",
    "persistent.main_menu == 3", "gui/MM3.PNG"
)

transform ts_mm_btns():
    on idle:
        glow_outline(1, color="#43424200", mesh_pad=True, power=0.0)
    on hover:
        glow_outline(20, color="#FFFFFF",  mesh_pad=True, power=0.3)

transform ts_mm_enter():
    yoffset 200 alpha 0.0
    ease 0.7 yoffset 0 alpha 1.0

transform ts_mm_exit():
    ease 0.5 yoffset 200 alpha 0.0

screen main_menu():
    default page = 1
    default post_anim_action = None
    if post_anim_action != None:
        timer 0.5 action post_anim_action

    ## This ensures that any other menu screen is replaced.
    tag storybook_frame

    add "main_menu_background"

    style_prefix "mm"

    vbox:
        xalign 0.5
        ypos 700
        spacing 2

        if post_anim_action == None:
            at ts_mm_enter()
        else:
            at ts_mm_exit()

        hbox:
            xalign 0.5
            spacing 0
            textbutton _("Begin Story") sensitive post_anim_action == None action SetScreenVariable("post_anim_action", Start()) at ts_mm_btns()

            textbutton _("Continue") sensitive post_anim_action == None action SetScreenVariable("post_anim_action", ShowMenu("load")) at ts_mm_btns()
            textbutton _("Settings") sensitive post_anim_action == None action SetScreenVariable("post_anim_action", ShowMenu("preferences")) at ts_mm_btns()

        hbox:
            xalign 0.5
            spacing 0
            textbutton _("Extras") sensitive post_anim_action == None action SetScreenVariable("post_anim_action", ShowMenu("main_menu_extras")) at ts_mm_btns()

            if renpy.variant("pc"):

                ## The quit button is banned on iOS and unnecessary on Android and
                ## Web.
                textbutton _("Exit Story") action Quit(confirm=not main_menu) at ts_mm_btns()

screen main_menu_extras():
    default page = 1
    default post_anim_action = None
    if post_anim_action != None:
        timer 0.5 action post_anim_action

    ## This ensures that any other menu screen is replaced.
    tag storybook_frame

    add "main_menu_background"

    style_prefix "mm"

    vbox:
        xalign 0.5
        ypos 700
        spacing 2

        if post_anim_action == None:
            at ts_mm_enter()
        else:
            at ts_mm_exit()
        hbox:
            xalign 0.5
            spacing 0

            textbutton _("Gallery") sensitive post_anim_action == None action ShowMenu("gallery") at ts_mm_btns()
            textbutton _("Credits") sensitive post_anim_action == None action ShowMenu("credits") at ts_mm_btns()
            if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

                ## Help isn't necessary or relevant to mobile devices.
                textbutton _("Help") sensitive post_anim_action == None action ShowMenu("help") at ts_mm_btns()

        textbutton _("Back") sensitive post_anim_action == None action SetScreenVariable("post_anim_action", Return()) keysym "game_menu" at ts_mm_btns() xalign 0.5


style mm_button:
    xysize (520, 125)
    padding (35, 10, 15, 10)
    hover_background "gui/mm_hover_background.webp"

style mm_button_text:
    align (0.5, 0.5)
    size 50
    font NOTOSERIF
    axis { "weight" : 700}
    color WHITE
    hover_color GOLD

    outlines [(2, DBLUE, 0, 0)]
    hover_outlines [(2, DGOLD, 0, 0)]

    hover_italic True


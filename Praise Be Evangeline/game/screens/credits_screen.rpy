### CREDITS SCREEN ############################################################
##
##

############################################################
### SETUP ###
############################################################
init python:
    CREDITS = {
        "azureXtwilight" : ["Project Lead, Writer", "https://azurextwilight.itch.io/"],
        "owl_ideas" : ["Main Menu Artist", "https://www.instagram.com/owl_ideas?igshid=YTQwZjQ0NmI0OA%3D%3D"],
        "SBHUnter" : ["Proofreader/Editor", "https://sbhunter.itch.io/"],
        
        "JayJay" : ["Background Artist", "https://thisjayisred.itch.io/"],
        "ratifuu" : ["Horror CG Artist", "https://vgen.co/ratifuu_/"],
        "Puyoo" : ["CG Render Artist", "https://puyoo.itch.io/"],

        "CyborgNekoSica" : ["UI Artist", "https://cyborgnekosica.itch.io/"],
        "Otoke Neko" : ["UI Artist, UI Programmer", "https://otojang.itch.io/"],
        "Naiomh 'Storm' Murchan" : ["UI Programmer", "https://linktr.ee/stormstrom"],

        "Rebecca Mondry" : ["Voice of Evangeline", "https://rebeccamondry.carrd.co/"],
        "Jason Daryl-Hall" : ["Voice of Therion", "https://www.imdb.com/name/nm14320438/"],
        "Jakob Bottoms" : ["Voice of Archbishop Desmond", "https://jakobbottoms.carrd.co/"],
        "Tora" : ["Voice of Bishop Vidius", "https://www.instagram.com/threadtheocracy/"],
        "Jefferey Neris" : ["Voice of Knight", "https://jeffereyneris.carrd.co/"],
        "mistershins" : ["Voice of Caelor", "https://www.twitch.tv/mistershins"],
        "Sophie Nyx" : ["Voice of Nuns", "https://sophienyx.carrd.co/"],
        
    }


############################################################
### SCREEN ###
############################################################
screen credits():
    default page = 1
    
    tag storybook_frame

    style_prefix "cred"

    # TODO: Make this change later.
    add "gui/menu_background1.webp"

    frame:
        background "gui/gallery/gallery_frame.webp"
        xysize (1254, 729)
        align (0.5, 0.5)

        label _("CREDITS")
        $ start = (page-2) * 9
        $ end = start + 9

        ## PAGE 2
        if page == 2:    
            grid 3 3:
                style_prefix "credcred"
                for name, desc in list(CREDITS.items())[start:end]:
                    $ role = desc[0]
                    $ link = desc[1]

                    vbox:
                        textbutton name action OpenURL(link)
                        text role

        elif page == 3:    
            grid 3 3:
                style_prefix "credcred"
                for name, desc in list(CREDITS.items())[start:end]:
                    $ role = desc[0]
                    $ link = desc[1]

                    vbox:
                        textbutton name action OpenURL(link)
                        text role


        else:
            vbox:
                align (0.5, 0.5)

                text "[gui.about!t]\n" xalign 0.5

                text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]") xalign 0.5 xsize 800
       
        
        
        ## PAGES ##
        hbox:
            xalign 0.5 yalign 1.0 yoffset -50
            spacing 50
            for i in range(1, 4):
                textbutton "{}".format(i) action SetScreenVariable("page", i)


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


############################################################
### STYLE ###
############################################################
style cred_label:
    is gallery_label
style cred_label_text:
    is gallery_label_text

style cred_button_text:
    is gallery_button_text

style cred_text:
    size 25
    color BROWN


style credcred_grid:
    align (0.5, 0.5)
    xspacing 45
    yspacing 15

style credcred_button:
    xalign 0.5
    xysize (300, None)

style credcred_button_text:
    underline True
    size 35
    color BROWN
    hover_color BLUE
    text_align 0.5
    xalign 0.5


style credcred_text:
    size 25
    xalign 0.5
    color BROWN
    xsize 500



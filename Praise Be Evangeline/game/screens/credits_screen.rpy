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
        "CyborgNekoSica" : ["UI Artist", "https://cyborgnekosica.itch.io/"],
        "Otoke Neko" : ["UI Artist, UI Programmer", "https://otojang.itch.io/"],
        "Strom" : ["UI Programmer", "Add link here"]
    }


############################################################
### SCREEN ###
############################################################
screen credits():
    # reuse gallery
    tag menu

    # TODO: Make this change later.
    add "gui/menu_background1.webp"

    frame:
        background "gui/gallery/gallery_frame.webp"
        xysize (1254, 729)
        align (0.5, 0.5)

        label _("CREDITS")


        grid 4 3:


############################################################
### STYLE ###
############################################################

## This file contains options that can be changed to customize your game.
##
## Lines beginning with two '#' marks are comments, and you shouldn't uncomment
## them. Lines beginning with a single '#' mark are commented-out code, and you
## may want to uncomment them when appropriate.


## Basics ######################################################################

## A human-readable name of the game. This is used to set the default window
## title, and shows up in the interface and error reports.
##
## The _() surrounding the string marks it as eligible for translation.

define config.name = _("Praise Be Evangeline")


## Determines if the title given above is shown on the main menu screen. Set
## this to False to hide the title.

define gui.show_name = True


## The version of the game.

define config.version = "1.0"


## Text that is placed on the game's about screen. Place the text between the
## triple-quotes, and leave a blank line between paragraphs.

define gui.about = _p("""
""")


## A short name for the game used for executables and directories in the built
## distribution. This must be ASCII-only, and must not contain spaces, colons,
## or semicolons.

define build.name = "PraiseBeEvangeline"


## Sounds and music ############################################################

## These three variables control, among other things, which mixers are shown
## to the player by default. Setting one of these to False will hide the
## appropriate mixer.

define config.has_sound = True
define config.has_music = True
define config.has_voice = True


## To allow the user to play a test sound on the sound or voice channel,
## uncomment a line below and use it to set a sample sound to play.

# define config.sample_sound = "sample-sound.ogg"
# define config.sample_voice = "sample-voice.ogg"


## Uncomment the following line to set an audio file that will be played while
## the player is at the main menu. This file will continue playing into the
## game, until it is stopped or another file is played.
define mm_tracks = {
    1: "evangeline.mp3",
    3: "hinokageri_orchestra.mp3",
    2: "Mainmenu.mp3",
}
define config.main_menu_music = mm_tracks.get(persistent.main_menu, mm_tracks[1])


## Transitions #################################################################
##
## These variables set transitions that are used when certain events occur.
## Each variable should be set to a transition, or None to indicate that no
## transition should be used.

## Entering or exiting the game menu.

define config.enter_transition = dissolve
define config.exit_transition = dissolve


## Between screens of the game menu.

define config.intra_transition = dissolve


## A transition that is used after a game has been loaded.

define config.after_load_transition = None


## Used when entering the main menu after the game has ended.

define config.end_game_transition = None


## A variable to set the transition used when the game starts does not exist.
## Instead, use a with statement after showing the initial scene.


## Window management ###########################################################
##
## This controls when the dialogue window is displayed. If "show", it is always
## displayed. If "hide", it is only displayed when dialogue is present. If
## "auto", the window is hidden before scene statements and shown again once
## dialogue is displayed.
##
## After the game has started, this can be changed with the "window show",
## "window hide", and "window auto" statements.

define config.window = "hide"


## Transitions used to show and hide the dialogue window

define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)


## Preference defaults #########################################################

## Controls the default text speed. The default, 0, is infinite, while any other
## number is the number of characters per second to type out.

default preferences.text_cps = 0


## The default auto-forward delay. Larger numbers lead to longer waits, with 0
## to 30 being the valid range.

default preferences.afm_time = 15


## Save directory ##############################################################
##
## Controls the platform-specific place Ren'Py will place the save files for
## this game. The save files will be placed in:
##
## Windows: %APPDATA\RenPy\<config.save_directory>
##
## Macintosh: $HOME/Library/RenPy/<config.save_directory>
##
## Linux: $HOME/.renpy/<config.save_directory>
##
## This generally should not be changed, and if it is, should always be a
## literal string, not an expression.

define config.save_directory = "PraiseBeEvangeline-1785065843"

default preferences.volume.music = 0.55  # Sets music to 70% volume
default preferences.volume.voice = 1.0  # Sets voice acting to 100% volume
default preferences.volume.sfx = 0.8    # Sets sound effects to 80% volume

## Icon ########################################################################
##
## The icon displayed on the taskbar or dock.

define config.window_icon = "gui/window_icon.png"


## Build configuration #########################################################
##
## This section controls how Ren'Py turns your project into distribution files.

init python:

    ## The following functions take file patterns. File patterns are case-
    ## insensitive, and matched against the path relative to the base directory,
    ## with and without a leading /. If multiple patterns match, the first is
    ## used.
    ##
    ## In a pattern:
    ##
    ## / is the directory separator.
    ##
    ## * matches all characters, except the directory separator.
    ##
    ## ** matches all characters, including the directory separator.
    ##
    ## For example, "*.txt" matches txt files in the base directory, "game/
    ## **.ogg" matches ogg files in the game directory or any of its
    ## subdirectories, and "**.psd" matches psd files anywhere in the project.

    # This is for dev purposes only
    store.web_demo = False

    ## Classify files as None to exclude them from the built distributions.
    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.classify('game/image_tools', None)
    build.classify('game/**.psd', None)

    #if demo:
        #build.classify('ch2fluffy.rpy', None)
        #build.classify('ch2spicy.rpy', None)
        #build.classify('ch3.rpy', None)
        #build.classify('ch4.rpy', None)

    ## To archive files, classify them as 'archive'.
    if store.web_demo:
        build.classify('**/game/chapter2.rpy', None)
        build.classify('**/game/chapter2a.rpy', None)

        # Garfunkel
        build.classify("game/VA/GARFUNKEL/RUINS/**", None)
        build.classify("game/VA/GARFUNKEL/CH0/**", None)
        build.classify("game/VA/GARFUNKEL/CH2A/**", None)
        build.classify("game/VA/GARFUNKEL/CH3A/**", None)


        # EVA
        build.classify("game/VA/RAKUMAROO/GLORY/**", None)
        build.classify("game/VA/RAKUMAROO/RUINS/**", None)

        build.classify("game/EvaChild/**", None)
        

        # THERION
        build.classify("game/TherionChild/**", None)

        # ruins doesnt appear
        build.classify("game/VA/JASON/GLORY/**", None)
        build.classify("game/VA/JASON/RUINS/**", None)
        build.classify("game/VA/JASON/zero/**", None)

        build.classify("game/VA/JASON/Therion40.mp3", None)
        build.classify("game/VA/JASON/Therion41.mp3", None)
        build.classify("game/VA/JASON/Therion42.mp3", None)
        build.classify("game/VA/JASON/Therion43.mp3", None)
        build.classify("game/VA/JASON/Therion44.mp3", None)
        build.classify("game/VA/JASON/Therion45.mp3", None)
        build.classify("game/VA/JASON/Therion46.mp3", None)
        build.classify("game/VA/JASON/Therion47.mp3", None)
        build.classify("game/VA/JASON/Therion48.mp3", None)
        build.classify("game/VA/JASON/Therion49.mp3", None)
        build.classify("game/VA/JASON/Therion50.mp3", None)
        build.classify("game/VA/JASON/Therion51.mp3", None)
        build.classify("game/VA/JASON/Therion52.mp3", None)
        build.classify("game/VA/JASON/Therion53.mp3", None)
        build.classify("game/VA/JASON/Therion54.mp3", None)
        build.classify("game/VA/JASON/Therion55.mp3", None)
        build.classify("game/VA/JASON/Therion56.mp3", None)
        build.classify("game/VA/JASON/Therion57.mp3", None)
        build.classify("game/VA/JASON/Therion58.mp3", None)
        build.classify("game/VA/JASON/Therion59.mp3", None)
        build.classify("game/VA/JASON/Therion60.mp3", None)
        build.classify("game/VA/JASON/Therion61.mp3", None)
        build.classify("game/VA/JASON/Therion62.mp3", None)
        build.classify("game/VA/JASON/Therion63.mp3", None)
        build.classify("game/VA/JASON/Therion64.mp3", None)
        build.classify("game/VA/JASON/Therion65.mp3", None)
        build.classify("game/VA/JASON/Therion66.mp3", None)
        build.classify("game/VA/JASON/Therion67.mp3", None)
        build.classify("game/VA/JASON/Therion68.mp3", None)
        build.classify("game/VA/JASON/Therion69.mp3", None)
        build.classify("game/VA/JASON/Therion70.mp3", None)
        build.classify("game/VA/JASON/Therion71.mp3", None)
        build.classify("game/VA/JASON/Therion72.mp3", None)
        build.classify("game/VA/JASON/Therion73.mp3", None)
        build.classify("game/VA/JASON/Therion74.mp3", None)
        build.classify("game/VA/JASON/Therion75.mp3", None)
        build.classify("game/VA/JASON/Therion76.mp3", None)
        build.classify("game/VA/JASON/Therion77.mp3", None)
        build.classify("game/VA/JASON/Therion78.mp3", None)
        build.classify("game/VA/JASON/Therion79.mp3", None)
        build.classify("game/VA/JASON/Therion80.mp3", None)
        build.classify("game/VA/JASON/Therion81.mp3", None)
        build.classify("game/VA/JASON/Therion82.mp3", None)
        build.classify("game/VA/JASON/Therion83.mp3", None)
        build.classify("game/VA/JASON/Therion84.mp3", None)
        build.classify("game/VA/JASON/Therion85.mp3", None)
        build.classify("game/VA/JASON/Therion86.mp3", None)
        build.classify("game/VA/JASON/Therion87.mp3", None)
        build.classify("game/VA/JASON/Therion88.mp3", None)
        build.classify("game/VA/JASON/Therion89.mp3", None)
        build.classify("game/VA/JASON/Therion90.mp3", None)
        build.classify("game/VA/JASON/Therion91.mp3", None)
        build.classify("game/VA/JASON/Therion92.mp3", None)
        build.classify("game/VA/JASON/Therion93.mp3", None)
        build.classify("game/VA/JASON/Therion94.mp3", None)
        build.classify("game/VA/JASON/Therion95.mp3", None)
        build.classify("game/VA/JASON/Therion96.mp3", None)
        build.classify("game/VA/JASON/Therion97.mp3", None)
        build.classify("game/VA/JASON/Therion98.mp3", None)
        build.classify("game/VA/JASON/Therion99.mp3", None)
        build.classify("game/VA/JASON/Therion100.mp3", None)
        build.classify("game/VA/JASON/Therion101.mp3", None)
        build.classify("game/VA/JASON/Therion102.mp3", None)
        build.classify("game/VA/JASON/Therion103.mp3", None)
        build.classify("game/VA/JASON/Therion104.mp3", None)
        build.classify("game/VA/JASON/Therion105.mp3", None)
        build.classify("game/VA/JASON/Therion106.mp3", None)
        build.classify("game/VA/JASON/Therion107.mp3", None)
        build.classify("game/VA/JASON/Therion108.mp3", None)
        build.classify("game/VA/JASON/Therion109.mp3", None)
        build.classify("game/VA/JASON/Therion110.mp3", None)
        build.classify("game/VA/JASON/Therion111.mp3", None)
        build.classify("game/VA/JASON/Therion112.mp3", None)
        build.classify("game/VA/JASON/Therion113.mp3", None)
        build.classify("game/VA/JASON/Therion114.mp3", None)
        build.classify("game/VA/JASON/Therion115.mp3", None)
        build.classify("game/VA/JASON/Therion116.mp3", None)
        build.classify("game/VA/JASON/Therion117.mp3", None)
        build.classify("game/VA/JASON/Therion118.mp3", None)
        build.classify("game/VA/JASON/Therion119.mp3", None)
        build.classify("game/VA/JASON/Therion120.mp3", None)
        build.classify("game/VA/JASON/Therion121.mp3", None)
        build.classify("game/VA/JASON/Therion122.mp3", None)
        build.classify("game/VA/JASON/Therion123.mp3", None)
        build.classify("game/VA/JASON/Therion124.mp3", None)
        build.classify("game/VA/JASON/Therion125.mp3", None)
        build.classify("game/VA/JASON/Therion126.mp3", None)
        build.classify("game/VA/JASON/Therion127.mp3", None)
        build.classify("game/VA/JASON/Therion128.mp3", None)
        build.classify("game/VA/JASON/Therion129.mp3", None)
        build.classify("game/VA/JASON/Therion130.mp3", None)
        build.classify("game/VA/JASON/Therion131.mp3", None)
        build.classify("game/VA/JASON/Therion132.mp3", None)
        build.classify("game/VA/JASON/Therion133.mp3", None)
        build.classify("game/VA/JASON/Therion134.mp3", None)
        build.classify("game/VA/JASON/Therion135.mp3", None)
        build.classify("game/VA/JASON/Therion136.mp3", None)
        build.classify("game/VA/JASON/Therion137.mp3", None)
        build.classify("game/VA/JASON/Therion138.mp3", None)
        build.classify("game/VA/JASON/Therion139.mp3", None)
        build.classify("game/VA/JASON/Therion140.mp3", None)
        build.classify("game/VA/JASON/Therion141.mp3", None)
        build.classify("game/VA/JASON/Therion142.mp3", None)
        build.classify("game/VA/JASON/Therion143.mp3", None)
        build.classify("game/VA/JASON/Therion144.mp3", None)
        build.classify("game/VA/JASON/Therion145.mp3", None)
        build.classify("game/VA/JASON/Therion146.mp3", None)
        build.classify("game/VA/JASON/Therion147.mp3", None)
        build.classify("game/VA/JASON/Therion148.mp3", None)
        build.classify("game/VA/JASON/Therion149.mp3", None)
        build.classify("game/VA/JASON/Therion150.mp3", None)
        build.classify("game/VA/JASON/Therion151.mp3", None)
        build.classify("game/VA/JASON/Therion152.mp3", None)
        build.classify("game/VA/JASON/Therion153.mp3", None)
        build.classify("game/VA/JASON/Therion154.mp3", None)
        build.classify("game/VA/JASON/Therion155.mp3", None)
        build.classify("game/VA/JASON/Therion156.mp3", None)
        build.classify("game/VA/JASON/Therion157.mp3", None)
        build.classify("game/VA/JASON/Therion158.mp3", None)
        build.classify("game/VA/JASON/Therion159.mp3", None)
        build.classify("game/VA/JASON/Therion160.mp3", None)
        build.classify("game/VA/JASON/Therion161.mp3", None)
        build.classify("game/VA/JASON/Therion162.mp3", None)
        build.classify("game/VA/JASON/Therion163.mp3", None)
        build.classify("game/VA/JASON/Therion164.mp3", None)
        build.classify("game/VA/JASON/Therion165.mp3", None)
        build.classify("game/VA/JASON/Therion166.mp3", None)
        build.classify("game/VA/JASON/Therion167.mp3", None)
        build.classify("game/VA/JASON/Therion168.mp3", None)
        build.classify("game/VA/JASON/Therion169.mp3", None)
        build.classify("game/VA/JASON/Therion170.mp3", None)
        build.classify("game/VA/JASON/Therion171.mp3", None)
        build.classify("game/VA/JASON/Therion172.mp3", None)
        build.classify("game/VA/JASON/Therion173.mp3", None)
        build.classify("game/VA/JASON/Therion174.mp3", None)
        build.classify("game/VA/JASON/Therion175.mp3", None)
        build.classify("game/VA/JASON/Therion176.mp3", None)
        build.classify("game/VA/JASON/Therion177.mp3", None)
        build.classify("game/VA/JASON/Therion178.mp3", None)
        build.classify("game/VA/JASON/Therion179.mp3", None)

        # SHINS - doesnt appear in ch1
        build.classify('game/VA/SHINS/**', None)
        
        # TORA - doesnt appear in ch1
        build.classify('game/VA/TORA/**', None)

        # MISC
        build.classify("game/Petra/**", None)
        build.classify("game/Ansel/**", None)
        build.classify("game/Caelor_Knight/**", None)


        # AUDIO
        build.classify("game/audio/bam.mp3", None)
        build.classify("game/audio/bird.mp3", None)
        build.classify("game/audio/burst.mp3", None)
        build.classify("game/audio/darkmagic.mp3", None)
        build.classify("game/audio/door.mp3", None)
        build.classify("game/audio/drag.mp3", None)
        build.classify("game/audio/flash.mp3", None)
        build.classify("game/audio/horror2.mp3", None)
        build.classify("game/audio/horror3.mp3", None)
        build.classify("game/audio/mob.mp3", None)
        build.classify("game/audio/scrape.mp3", None)
        build.classify("game/audio/Therion124.mp3", None)
        build.classify("game/audio/thud.mp3", None)
        build.classify("game/audio/tummy.mp3", None)
        build.classify("game/audio/void.mp3", None)
        build.classify("game/audio/Woman2.mp3", None)


        # CG
        build.classify("game/BG/PAST CG/**", None)
        build.classify("game/BG/BURST/**", None)
        build.classify("game/BG/evadeath/**", None)
        build.classify("game/BG/CREEPYTHERION/**", None)
        build.classify("game/BG/MOUTH THERION/**", None)
        build.classify("game/BG/GLORY/**", None)
        build.classify("game/BG/FLOWERS/**", None)
        build.classify("game/BG/SCREAM/**", None)
        build.classify("game/BG/EvaHorror.jpg", None)
        build.classify("game/BG/Flashback.jpg", None)
        build.classify("game/BG/Eva_Bedroom_Night_Lit.png", None)
    ## WEB STUFF ENDS HERE



    build.classify('game/**.png', 'archive')
    build.classify('game/**.jpg', 'archive')
    build.classify('game/**.webp', 'archive')
    build.classify('game/**.svg', 'archive')
    build.classify('game/**.mp3', 'archive')
    build.classify('game/**.ogg', 'archive')

    build.classify('game/**.rpy', 'archive')
    build.classify('game/**.rpyc', None)
    ## Files matching documentation patterns are duplicated in a mac app build,
    ## so they appear in both the app and the zip file.

    build.documentation('*.html')
    build.documentation('*.txt')

    


## A Google Play license key is required to perform in-app purchases. It can be
## found in the Google Play developer console, under "Monetize" > "Monetization
## Setup" > "Licensing".

# define build.google_play_key = "..."


## The username and project name associated with an itch.io project, separated
## by a slash.

# define build.itch_project = "renpytom/test-project"

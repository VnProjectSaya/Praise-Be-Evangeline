# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define en = Character(None) # Eva's chara

define tn = Character(None) # Therion's internal narration (glory/ruins)
define narrator = Character(None) # neutral narration voice (glory/ruins)

define vidius = Character("Bishop Vidius")
define caelor = Character("Caelor")
define petra = Character("Petra")
define ansel = Character("Ansel")

define woman = Character("Woman")
define guard = Character("Guard")
define guard2 = Character("Guard")
define clergyman = Character("Clergyman")
define clergywoman = Character("Clergywoman")
define crowd = Character("Crowd")

define e = Character("Evangeline", kind=bubble, image="MISSING_EVA", who_color="#3d9e68", ctc_position="screen-variable", ctc="bubble_ctc", show_layer='bubbles')
define t = Character("Therion", kind=bubble, image="MISSING_THERI", who_color="#4952ab", ctc_position="screen-variable", ctc="bubble_ctc", show_layer='bubbles')
define de = Character("Desmond", kind=bubble, image="", ctc_position="screen-variable", ctc="bubble_ctc", show_layer='bubbles')
define announcer = Character("Announcer", kind=bubble, image="")

# The game starts here.
image GUI_Ref1 = "images/GUI_Ref1.png"
label start:
    $ renpy.show_screen("storybook_frame")
    jump opening_scene

# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define en = Character(None, kind=bubble, image="NAR_EVA", what_align=(0.5, 0.0), what_text_align=0.5, ctc_position="screen-variable", ctc="bubble_ctc") # Eva's chara

define tn = Character(None, kind=bubble, image="NAR_THERI", what_align=(0.5, 0.0), what_text_align=0.5, ctc_position="screen-variable", ctc="bubble_ctc") # Therion's internal narration (glory/ruins)
define narrator = Character(None, kind=bubble, image="NAR_GEN", what_align=(0.5, 0.0), what_text_align=0.5, ctc_position="screen-variable", ctc="bubble_ctc") # neutral narration voice (glory/ruins)

define vidius = Character("Vidius", kind=bubble, image="", ctc_position="screen-variable", ctc="bubble_ctc", show_layer='bubbles')
define caelor = Character("Caelor", kind=bubble, image="", ctc_position="screen-variable", ctc="bubble_ctc", show_layer='bubbles')
define petra = Character("Petra")
define ansel = Character("Ansel")

define guard = Character("Guard")
define guard2 = Character("Guard")
define clergyman = Character("Clergyman")
define clergywoman = Character("Clergywoman")
define man = Character("man", kind=bubble, image="", ctc_position="screen-variable", ctc="bubble_ctc", show_layer='bubbles')
define woman = Character("woman", kind=bubble, image="", ctc_position="screen-variable", ctc="bubble_ctc", show_layer='bubbles')
define crowd = Character("Crowd", kind=bubble, image="", ctc_position="screen-variable", ctc="bubble_ctc", show_layer='bubbles')

define e = Character("Evangeline", kind=bubble, image="MISSING_EVA", who_color="#3d9e68", ctc_position="screen-variable", ctc="bubble_ctc", show_layer='bubbles')
define t = Character("Therion", kind=bubble, image="MISSING_THERI", who_color="#4952ab", ctc_position="screen-variable", ctc="bubble_ctc", show_layer='bubbles')
define de = Character("Desmond", kind=bubble, image="", ctc_position="screen-variable", ctc="bubble_ctc", show_layer='bubbles')
define announcer = Character("Announcer", kind=bubble, image="")

image dream_frame = "Frame/Dream Frame/dream_frame.webp"

##Storm note: please show this on start instead as seen in the script file
screen storybook_frame():
    layer 'story_frame'

    if True:
        use dream_frame_overlay()
    else:
        use dream_frame_overlay() ##Replace with twisted one
screen dream_frame_overlay():
    layer 'story_frame'
    if "menu" not in renpy.get_showing_tags(layer="screens"):
        add "dream_frame"

# The game starts here.
image GUI_Ref1 = "images/GUI_Ref1.png"
label start:
    $ renpy.show_screen("storybook_frame")

    "just something"
    jump opening_scene

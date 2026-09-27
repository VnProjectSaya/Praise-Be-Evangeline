# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define en = Character(None, kind=bubble, image="NAR_EVA", what_align=(0.5, 0.0), what_text_align=0.5, ctc_position="screen-variable", ctc="bubble_ctc") # Eva's chara

define tn = Character(None, kind=bubble, image="NAR_THERI", what_align=(0.5, 0.0), what_text_align=0.5, ctc_position="screen-variable", ctc="bubble_ctc") # Therion's internal narration (glory/ruins)
define narrator = Character(None, kind=bubble, image="NAR_GEN", what_align=(0.5, 0.0), what_text_align=0.5, ctc_position="screen-variable", ctc="bubble_ctc") # neutral narration voice (glory/ruins)

define vidius = Character("Vidius", voice_tag = "vidius",kind=bubble, image="", ctc_position="screen-variable", ctc="bubble_ctc", show_layer='bubbles')
define caelor = Character("Caelor", voice_tag = "caelor",kind=bubble, image="", ctc_position="screen-variable", ctc="bubble_ctc", show_layer='bubbles')
define petra = Character("Petra", voice_tag = "petra",kind=bubble, image="", ctc_position="screen-variable", ctc="bubble_ctc", show_layer='bubbles')
define ansel = Character("Ansel", voice_tag = "ansel",kind=bubble, image="", ctc_position="screen-variable", ctc="bubble_ctc", show_layer='bubbles')

define clergyman = Character("Clergyman", voice_tag = "misc")
define clergywoman = Character("Clergywoman", voice_tag = "misc")
define man = Character("man", voice_tag="misc", kind=bubble, image="", ctc_position="screen-variable", ctc="bubble_ctc", show_layer='bubbles')
define woman = Character("woman", voice_tag="misc", kind=bubble, image="", ctc_position="screen-variable", ctc="bubble_ctc", show_layer='bubbles')
define crowd = Character("Crowd", voice_tag="misc", kind=bubble, image="", ctc_position="screen-variable", ctc="bubble_ctc", show_layer='bubbles')

define e = Character("Evangeline", voice_tag="evangeline", kind=bubble, image="MISSING_EVA", who_color="#3d9e68", ctc_position="screen-variable", ctc="bubble_ctc", show_layer='bubbles')
define t = Character("Therion", voice_tag="therion", kind=bubble, image="MISSING_THERI", who_color="#4952ab", ctc_position="screen-variable", ctc="bubble_ctc", show_layer='bubbles')
define de = Character("Desmond", voice_tag="desmond", kind=bubble, image="", ctc_position="screen-variable", ctc="bubble_ctc", show_layer='bubbles')
define announcer = Character("Announcer", voice_tag="misc", kind=bubble, image="")
define guard = Character("Guard", voice_tag="misc", kind=bubble, image="", ctc_position="screen-variable", ctc="bubble_ctc", show_layer='bubbles')

image dream_frame:
    anchor (0.5, 0.5) pos (0.5, 0.5)
    "Frame/Dream Frame/dream_frame.webp"
image twisted_frame:
    anchor (0.5, 0.5) pos (0.5, 0.5)
    "Frame/Twisted Frame/twisted_frame.webp"
image horror_frame:
    anchor (0.5, 0.5) pos (0.5, 0.5)
    "Frame/Horror Frame/horror_frame.webp"

default current_frame = "dream"
default last_known_frame = None
##Storm note: please show this on start instead as seen in the script file
screen storybook_frame():
    layer 'story_frame'
    if current_frame != last_known_frame:
        timer 0.6 action SetVariable("last_known_frame", current_frame)

    if current_frame == "twisted" or last_known_frame == "twisted":
        use twisted_frame_overlay()
    if current_frame == "dream" or last_known_frame == "dream":
        use dream_frame_overlay()
    if current_frame == "horror" or last_known_frame == "horror":
        use horror_frame_overlay()

screen dream_frame_overlay():
    layer 'story_frame'
    if "menu" not in renpy.get_showing_tags(layer="screens"):
        add "dream_frame":
            if current_frame != last_known_frame:
                at (frame_appear() if current_frame == "dream" else frame_hide())

screen twisted_frame_overlay():
    if "menu" not in renpy.get_showing_tags(layer="screens"):
        add "twisted_frame":
            if current_frame != last_known_frame:
                at (frame_appear() if current_frame == "twisted" else frame_hide())

screen horror_frame_overlay():
    if "menu" not in renpy.get_showing_tags(layer="screens"):
        add "horror_frame":
            if current_frame != last_known_frame:
                at (frame_appear() if current_frame == "horror" else frame_hide())

transform frame_appear():
    zoom 1.5 alpha 0.0
    ease 0.6 zoom 1.0 alpha 1.0

transform frame_hide():
    ease 0.6 zoom 1.5 alpha 0.0

# bg_layer renders at the very back.
# story_frame renders above master and transient, but below the UI screens.
# The game starts here.

label start:
    $ renpy.show_screen("storybook_frame")
    # Storm: To change the frame, just put the below without the comment
    # $ current_frame = "twisted"
    # $ current_frame = "horror"

    jump opening_scene

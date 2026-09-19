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

define e = Character("Evangeline")
define t = Character("Therion")
define de = Character("Desmond")
define announcer = Character("Announcer")

# The game starts here.

label start:
    jump opening_scene

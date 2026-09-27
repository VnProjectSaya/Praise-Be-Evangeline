################################################################################
##
## Gradient Shaders for Ren'Py
##
################################################################################
## This file includes several example gradients using the gradients declared
## in gradient_shaders.rpy.
##
## I suggest you put the line
# jump gradient_test
## somewhere after your start label to see the gradients in action.
##
## You may safely delete this file if you do not need the examples.
##
## If you use this code in your project,
## please credit me as Feniks @ feniksdev.com
## Also consider tossing me a ko-fi @ https://ko-fi.com/fen
################################################################################

################################################################################
## IMAGES
################################################################################
## Here are a few pre-defined gradients stored as images
## TRANSITIONS #################################################################
image white_to_black_angle = GradientDisplayable(["#FFF", "#000"],
## Gradients can be used for transitions via ImageDissolve!
    xysize=(config.screen_width, config.screen_height), kind="angle")
define circular_transition = ImageDissolve("white_to_black_angle", 2.0, 16)
image white_to_black_linear = GradientDisplayable(["#FFF", "#000"],
    xysize=(config.screen_width, config.screen_height), mirror=True, kind="linear")
define linear_gradient_transition = ImageDissolve("white_to_black_linear", 2.0, 16)
image white_to_black_radial = GradientDisplayable(["#FFF", "#000"],
    xysize=(config.screen_width, config.screen_height), kind="radial",
    elliptical=True)
define radial_gradient_transition = ImageDissolve("white_to_black_radial", 2.0, 16)

## REGULAR IMAGES ##############################################################
image linear_gradient1 = GradientDisplayable(
    ["#FA0952FF", "#f1611eff", "#FFCD7C"],
    xysize=(400, 400), kind="linear")
image linear_gradient2 = GradientDisplayable(
    ["#FA0952FF", "#f1611eff", "#FFCD7C"],
    thresholds=[0.3, 0.5, 0.7],
    xysize=(400, 400), kind="linear")
image linear_gradient3 = GradientDisplayable(
    ["#FA0952FF", "#f1611eff", "#FFCD7C"],
    scale=0.5, xysize=(400, 400), kind="linear")
image linear_gradient4 = GradientDisplayable(
    ["#FA0952FF", "#f1611eff", "#FFCD7C"],
    mirror=True, xysize=(400, 400), kind="linear")
image linear_gradient5 = GradientDisplayable(
    ["#FA0952FF", "#f1611eff", "#FFCD7C"],
    angle=45, xysize=(400, 400), kind="linear")
image linear_gradient6 = GradientDisplayable(
    ["#FA0952FF", "#f1611eff", "#FFCD7C"],
    angle=45, mirror=True, center=(0.3, 0.3),
    xysize=(400, 400), kind="linear")

image circular_gradient = GradientDisplayable(
    ["#FA0952FF", "#f1611eff", "#FFCD7C"],
    xysize=(500, 300), kind="radial")
image elliptical_gradient = GradientDisplayable(
    ["#FA0952FF", "#f1611eff", "#FFCD7C"],
    elliptical=True, xysize=(500, 300), kind="radial")
image circular_gradient 2 = GradientDisplayable(
    ["#FA0952FF", "#f1611eff", "#FFCD7C"],
    xysize=(500, 500), kind="radial")
image elliptical_gradient 2 = GradientDisplayable(
    ["#FA0952FF", "#f1611eff", "#FFCD7C"],
    elliptical=True, xysize=(500, 500), kind="radial")
image circular_gradient 3 = GradientDisplayable(
    ["#FA0952FF", "#f1611eff", "#FFCD7C"],
    xysize=(500, 500), scale=1.5, kind="radial")
image elliptical_gradient 4 = GradientDisplayable(
    ["#FA0952FF", "#f1611eff", "#FFCD7C", "#0000"],
    thresholds=[0.0, 0.3, 0.5, 0.7],
    elliptical=True, xysize=(500, 500), kind="radial")
image circular_gradient 4 = GradientDisplayable(
    ["#FA0952FF", "#f1611eff", "#FFCD7C", "#0000"],
    thresholds=[0.0, 0.3, 0.5, 0.7],
    xysize=(500, 500), scale=1.5, kind="radial")
image elliptical_gradient 5 = GradientDisplayable(
    ["#FA0952FF", "#f1611eff", "#FFCD7C", "#0000"],
    thresholds=[0.0, 0.3, 0.5, 0.7], center=(0.0, 0.0), scale=2.0,
    elliptical=True, xysize=(500, 500), kind="radial")
image circular_gradient 5 = GradientDisplayable(
    ["#FA0952FF", "#f1611eff", "#FFCD7C", "#0000"],
    thresholds=[0.0, 0.3, 0.5, 0.7], center=(0.0, 0.0),
    xysize=(500, 500), scale=3.0, kind="radial")

image angle_gradient = GradientDisplayable(
    ["#FA0952FF", "#f1611eff", "#FFCD7C"],
    xysize=(500, 500), kind="angle")
image angle_gradient 2 = GradientDisplayable(
    ["#FA0952FF", "#f1611eff", "#FFCD7C"],
    angle=45, xysize=(500, 500), kind="angle")
image angle_gradient 3 = GradientDisplayable(
    ["#FA0952FF", "#0000"],
    angle=180, xysize=(500, 500), kind="angle")
image angle_gradient 4 = GradientDisplayable(
    ["#FFEFB4FF", "#FF00A5FF","#FA0952FF", "#FF4B62FF",
    "#f1611eff", "#FE8D32FF", "#FF944CFF", "#FFCD7CFF",
    "#FFEFB4FF"],
    angle=270, xysize=(500, 500), kind="angle")

label gradient_test():
    scene expression "#ff8335"
    show white_to_black_angle
    "Here is a full-screen angle gradient. It can be used for transitions."
    scene expression "#21212d" with circular_transition
    "You can change many aspects of gradients by adjusting the arguments passed to them."
    show linear_gradient1:
        xalign 0.25 ycenter 0.5
    "The gradient on the left is a standard linear gradient with three colours."
    show linear_gradient2 as g2:
        xalign 0.75 ycenter 0.5
    "The gradient on the right has custom thresholds, so the colours start and end at different points."
    show linear_gradient3 as g2:
        xalign 0.75 ycenter 0.5
    "Now the gradient on the right has been scaled down to half its size."
    show linear_gradient4 as g2:
        xalign 0.75 ycenter 0.5
    "Linear gradients can also be mirrored, like on the right. This is useful for creating symmetrical gradients."
    show linear_gradient5 as g2:
        xalign 0.75 ycenter 0.5
    "The gradient on the right's angle has been changed to 45 degrees."
    show linear_gradient6 as g2:
        xalign 0.75 ycenter 0.5
    "You can also adjust the center of the gradient as well."
    scene expression "#292835"
    show circular_gradient:
        xalign 0.25 ycenter 0.5
    show elliptical_gradient:
        xalign 0.75 ycenter 0.5
    with radial_gradient_transition
    "Here are two radial gradients. The one on the left is circular, and the one on the right is elliptical."
    "An elliptical gradient will stretch based on the dimensions of the image, while a circular one will always be a circle."
    show circular_gradient 2
    show elliptical_gradient 2
    "But when the gradient is a square, they will look very similar."
    show circular_gradient 3
    "Especially if you increase the scale of the circular gradient. However, the circular gradient uses smoothstepping to blend the gradient while the elliptical one does not."
    show circular_gradient 4
    show elliptical_gradient 4
    "Remember also that you can provide transparent or semi-transparent colours to the gradients."
    show circular_gradient 5
    show elliptical_gradient 5
    "You can adjust the center of the radial gradients also."
    scene expression "#21212d"
    show angle_gradient at truecenter
    with linear_gradient_transition
    "Finally we'll look more closely at the angle gradient."
    show angle_gradient 2
    "You can provide it with different angles to change where the gradient begins."
    show angle_gradient 3
    "Remember you can use transparent colours for different effects as well."
    show angle_gradient 4
    "You can also provide the same colour for the start and end for a smoothly blended gradient all around."
    scene expression "#21212d"
    "And that's all for this label. You'll be taken to a screen with some additional effects when you click next."
    call screen sample_gradient_screen()
    return

screen sample_gradient_screen():
    style_prefix 'sample_gradient'
    hbox:
        xalign 0.5 spacing 120 yalign 0.1
        vbox:
            xmaximum 500
            hbox:
                add "gui/window_icon.png"
                add "gui/window_icon.png" at angle_gradient(["#FFF", "#000"])
            text "You can apply gradients to images. The transparency of the original is respected."

        vbox:
            xmaximum 500
            hbox:
                add "gui/window_icon.png":
                    at transform:
                        angle_gradient(
                            ["#FFEFB4FF", "#FF00A5FF","#FA0952FF", "#FF4B62FF",
                            "#f1611eff", "#FE8D32FF", "#FF944CFF", "#FFCD7CFF",
                            "#FFEFB4FF"], angle=0)
                        linear 6.0 angle_gradient(
                            ["#FFEFB4FF", "#FF00A5FF","#FA0952FF", "#FF4B62FF",
                            "#f1611eff", "#FE8D32FF", "#FF944CFF", "#FFCD7CFF",
                            "#FFEFB4FF"], angle=360)
                        repeat
                text "You can animate gradients." yalign 0.5
        vbox:
            hbox:
                add AlphaMask("gui/window_icon.png", GradientDisplayable(
                    ["#FFF", "#0000"], kind="radial", center=(0.5, 0.35),
                    thresholds=[0.4, 0.8]))
                add "gui/window_icon.png"
                add AlphaMask("gui/window_icon.png", GradientDisplayable(
                    ["#FFF", "#0000"], kind="linear",
                    thresholds=[0.6, 0.9], angle=90))
            text "Use it as a mask for other images!" xmaximum 500

    text "You can apply gradients to text, too!" font gui.name_text_font:
        align (0.5, 0.5) size 100 bold True at linear_gradient(
            ["#fce8a2ff", "#fcaa3eff", "#FFEFB4FF"],
            angle=90, scale=0.85)

    hbox:
        align (0.5, 0.8) spacing 25
        frame:
            background GradientDisplayable(
                ["#f93c3e", "#ff8335", "#0000"], elliptical=True,
                thresholds=[0.2, 0.5, 0.7], kind="radial")
            padding (45, 80)
            text "You can also use it as a frame."
        frame:
            background GradientDisplayable(
                ["#f93c3e", "#ff8335", "#0000"], angle=90,
                thresholds=[0.5, 0.8, 1.0], mirror=True)
            padding (25, 80)
            text "You can also use it as a frame."
        frame:
            background GradientDisplayable(
                ["#f93c3e", "#0000"], angle=0,
                thresholds=[0.6, 1.0], mirror=True)
            padding (80, 50) yalign 0.5
            text "You can also use it as a frame."
    textbutton "Return" align (1.0, 1.0) action Return()

style sample_gradient_text:
    color "#fff"
    font "DejaVuSans.ttf"
    outlines [(2, "#000")]
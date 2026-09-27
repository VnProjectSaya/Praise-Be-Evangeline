# Gradients for Ren'Py

The file gradient_shaders.rpy contains code for three different gradient shaders in Ren'Py. There is also a file, gradient_examples.rpy, with several examples using the shaders.

## Initial Setup

To start, place the two rpy files (`gradient_shaders.rpy` and `gradient_examples.rpy`) into your project's `game/` folder. You should jump to the example label `gradient_test` to see examples of how to use the gradients.

## Gradient Arguments

### Common Arguments

All three gradient shaders take the following arguments:

`colors`
    This should be a list of colour codes (e.g. "#FFFFFF") or Color objects which will be used for the gradient. Up to 16 colours may be supplied.

    e.g. `colors=["#FFFFFF", "#BBBBBB", "#888888", "#444444]`

`thresholds`
    This should be a list of the same length as the number of colours you provided. These numbers go from 0.0-1.0 and correspond to the "percent" where each new colour begins along the gradient. By default, the gradient colours will be evenly spread out (e.g. two colours have thresholds [0.0, 1.0], three colours have thresholds [0.0, 0.5, 1.0], etc.).

    You may adjust these however you like; for example, the thresholds [0.5, 1.0] means that the first 50% of the gradient is the first colour, and the last 50% is a blend between the first and second colours.

    e.g. `thresholds=[0.3, 0.6, 0.9]`

`center`
    This should be an (x, y) tuple. It can either be two integers - in which case it's an exact pixel position on the image - or two floats, in which case it's a percentage of the image size. The default center position is (0.5, 0.5).

    e.g. `center=(0.0, 0.5)` or `center=(100, 100)`

### Linear Gradient

A linear gradient goes in a straight line transitioning from one colour to the next. It takes the following arguments in addition to the common ones:

`scale`
    By default, the gradient will generally attempt to evenly divide up the available space among all provided colours. However, for diagonal gradients or non-square gradients, this may not take up all the space. You can increase the scale to increase the total amount of space the gradient covers. By default this is 1.0. It should be a number greater than 0.0.

    e.g. `scale=2.0`

`angle`
    The angle, in degrees, that this gradient displays with. By default, an angle of 0 results in a vertical gradient, with the colours changing from left-to-right. 90 results in a horizontal gradient, with the colours changing from top-to-bottom. This should be an integer from 0-360.

    e.g. `angle=45`

`mirror`
    False by default. If True, the linear gradient will be mirrored. So, if you provided the colours [white, gray, black], then a non-mirrored gradient would go from white to gray to black, but a mirrored gradient will go from white to gray to black to gray to white.

    e.g. `mirror=True`

### Radial Gradient

A radial gradient changes colours the farther it gets from the center point in a circle-shaped pattern. It takes the following arguments in addition to the common ones:

`scale`
    By default, the gradient will generally attempt to evenly divide up the available space among all provided colours. However, for diagonal gradients or non-square gradients, this may not take up all the space. You can increase the scale to increase the total amount of space the gradient covers. By default this is 1.0. It should be a number greater than 0.0.

    e.g. `scale=2.0`

`elliptical`
    False by default. `elliptical=False` will force the gradient to a circular shape. `elliptical=True`, by contrast, will be elliptical depending on the dimensions of the base image. So, if `elliptical=True` on a square image, you will get a circular gradient. But if the image is very long and not very wide, then the gradient will be more of an oval.

    Notably, when `elliptical=False` the gradient uses smoothstep shading. The `elliptical=True` gradient does not use smoothstep shading. This means that the colours are blended along a slightly different curve rather than strictly linearly.

    e.g. `elliptical=True`

### Angle Gradient

An angle gradient changes colours depending on how far the pixel is around a circle with a particular center point. If you imagine a clock, 0% is 12:00, 50% blended is 6:00, 75% blended is 9:00, etc. It takes the following arguments in addition to the common ones:

`angle`
    The angle, in degrees, where the gradient begins. By default, 0 is at 12:00. This should be a number from 0-360.

    e.g. `angle=270`

For the angle gradient, note also that if you provide the same colour as the beginning and end colours, you can smoothly blend between them without a distinct "beginning" angle.

## Transforms

To apply the gradient to a displayable (e.g. an image or text) in Ren'Py, there are three special transforms.

`linear_gradient(colors, thresholds=None, center=(0.5, 0.5), scale=1.0, angle=0, mirror=False)`

`radial_gradient(colors, thresholds=None, center=(0.5, 0.5), scale=1.0, elliptical=False)`

`angle_gradient(colors, thresholds=None, center=(0.5, 0.5), angle=0)`

See the headings on arguments for what each argument does. These transforms can be used anywhere a regular ATL transform can be used e.g.

```renpy
text "Welcome!" at linear_gradient(["#FF0", "#FF8"], mirror=True)
```

or

```renpy
show bubble at radial_gradient(["#F0F", "#00F"], scale=2.0)
```

## GradientDisplayable

To make it easier to declare a gradient directly as its own displayable instead of being applied on top of an existing displayable, you can use the GradientDisplayable function e.g.

```renpy
image faded_frame = GradientDisplayable(
    ["#f93c3e", "#0000"], angle=0,
    thresholds=[0.6, 1.0], mirror=True, kind="linear")
```

A `GradientDisplayable` takes the same arguments as the transforms above, and an additional argument `kind` which specifies which shader to use. The possible values of kind are `"linear"`, `"angle"`, and `"radial"`.

You may also pass in positional or size properties to `GradientDisplayable` which will be applied to the base displayable. By default, a GradientDisplayable without a specified size will take up as much space as is allocated to it.

## Final Notes

Remember also that you can supply gradients with transparent or translucent colours! For example, "#0000" is fully transparent - the last digit of a 3-digit hexcode or the last two digits of a 6-digit hexcode can be used for transparency.

I hope you like the shaders! You can check out my website, https://feniksdev.com for more Ren'Py tutorials, and subscribe to feniksdev.itch.io so you don't miss out on future Ren'Py tool releases.

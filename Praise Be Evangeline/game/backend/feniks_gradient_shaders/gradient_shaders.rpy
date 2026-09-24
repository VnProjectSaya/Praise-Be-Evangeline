################################################################################
##
## Gradient Shaders for Ren'Py
##
################################################################################
## This file includes three shaders and transforms for gradients in Ren'Py.
##
## You do not need to read through nor understand the shaders! Examples of how
## to use the shaders are in gradient_shader_examples.rpy. There is an example
## label (gradient_test) and a screen (sample_gradient_screen) with several
## examples on how to use the gradients. If you'd like to read up more on how
## it all works, the shaders and transforms have been documented below.
##
## I suggest you put the line
# jump gradient_test
## somewhere after your start label to see the gradients in action!
##
## If you use this code in your project,
## please credit me as Feniks @ feniksdev.com
## Also consider tossing me a ko-fi @ https://ko-fi.com/fen
################################################################################
## SHADERS
################################################################################
init python:
    ## A shader to create a linear gradient (where the colour changes based on
    ## how far the pixel is from a line. The angle may be changed; 0 is
    ## vertical (colours change from left to right) and 90 is horizontal
    ## (colours change from top to bottom).
    renpy.register_shader("feniks.linear_gradient", variables="""
        uniform mat4 u_one_to_four;
        uniform mat4 u_five_to_eight;
        uniform mat4 u_nine_to_twelve;
        uniform mat4 u_thirteen_to_sixteen;

        uniform mat4 u_thresholds;
        uniform float u_scale;
        uniform float u_angle;
        uniform vec2 u_center;
        uniform float u_mirror;
        uniform float u_calculate_center;

        uniform vec2 u_model_size;
        varying vec2 v_position;
        varying vec2 v_size;
        attribute vec4 a_position;
        varying vec2 v_coords;
    """, vertex_300="""
        v_coords = vec2(a_position.x / u_model_size.x, a_position.y / u_model_size.y);
        v_position = a_position.xy;
        v_size = u_model_size.xy;
    """, fragment_functions="""
        // Return the correct vec4 colour based on the provided index.
        // A convenience function due to lack of arrays.
        vec4 get_color(int ind, mat4 color1, mat4 color2, mat4 color3, mat4 color4) {
            if (ind < 4) {
                return color1[ind];
            } else if (ind < 8) {
                return color2[ind-4];
            } else if (ind < 12) {
                return color3[ind-8];
            } else {
                return color4[ind-12];
            }
        }

        // Return the number of the color this pixel falls below.
        vec2 find_threshold(mat4 thresholds, float num) {
            for (int i = 0; i < 4; i++) {
                for (int j = 0; j < 4; j++) {
                    if (num < thresholds[i][j]) {
                        return vec2(i, j);
                    }
                }
            }
            return vec2(3, 3);
        }
        int myRound(float num) {
            return int(num + 0.5);
        }
    """, fragment_300="""
        float num = 0.0;
        vec2 center = vec2(0.5);
        if (u_calculate_center > 0.5) {
            center = u_center / v_size;
        } else {
            center = u_center;
        }
        float scale = u_scale;

        if (u_mirror < 0.5) {
            // Don't mirror
            if (u_angle < 90.0) {
                center += vec2(-0.5, -0.5);
            } else if (u_angle < 180.0) {
                center += vec2(0.5, -0.5);
            } else if (u_angle < 270.0) {
                center += vec2(0.5, 0.5);
            } else {
                center += vec2(-0.5, 0.5);
            }
            scale *= 2.0;
        }

        // The lines are all parallel; get the distance from the center line.
        num = abs(dot(v_coords - center, vec2(cos(radians(u_angle)),
            sin(radians(u_angle)))));
        // Multiply by 2 because the distance is from the center to the edge.
        num *= 2.0;
        // Divide by scale
        num /= scale;
        num = min(num, 1.0);

        vec4 old_gl = gl_FragColor;
        vec4 new_color = vec4(0.0);

        vec4 first_color = vec4(0.0);
        vec4 second_color = vec4(0.0);
        vec2 thresh1 = vec2(0.0);
        vec2 thresh2 = vec2(0.0);

        // Calculate which thresholds the pixel falls between.
        thresh1 = find_threshold(u_thresholds, num);

        float threshold = thresh1.x*4.0 + thresh1.y;
        first_color = get_color(myRound(threshold), u_one_to_four, u_five_to_eight,
            u_nine_to_twelve, u_thirteen_to_sixteen);
        float threshold2 = max(threshold-1.0, 0.0);

        // Make sure the thresholds are within range
        if (thresh1.y > 0.0) {
            thresh2 = vec2(thresh1.x, thresh1.y-1.0);
        } else {
            thresh2 = vec2(thresh1.x-1.0, 3.0);
            if (thresh2.x < 0.0) {
                thresh2 = vec2(0.0, 0.0);
            }
        }

        second_color = get_color(myRound(threshold2), u_one_to_four, u_five_to_eight,
            u_nine_to_twelve, u_thirteen_to_sixteen);

        // Properly multiply the colour alphas
        first_color = vec4(first_color.rgb * first_color.a, first_color.a);
        second_color = vec4(second_color.rgb * second_color.a, second_color.a);

        // The amount to blend first_color and second_color
        float blend_amount = 0.0;

        // Make sure we're not dividing by zero
        if (u_thresholds[myRound(thresh1.x)][myRound(thresh1.y)] != u_thresholds[myRound(thresh2.x)][myRound(thresh2.y)]) {
            blend_amount = (num - u_thresholds[myRound(thresh2.x)][myRound(thresh2.y)]);
            blend_amount /= (u_thresholds[myRound(thresh1.x)][myRound(thresh1.y)]
                    - u_thresholds[myRound(thresh2.x)][myRound(thresh2.y)]);
            blend_amount = smoothstep(0.0, 1.0, blend_amount);
        }
        new_color = mix(second_color, first_color, blend_amount);
        if (new_color.a > 0.0) {
            // Divide the alpha to get the true colour so we can
            // premultiply the final alpha.
            new_color.r /= new_color.a;
            new_color.g /= new_color.a;
            new_color.b /= new_color.a;
        }
        float min_alpha = min(old_gl.a, new_color.a);
        // Apply the new colour to the image, using the alpha of the original.
        gl_FragColor = vec4(new_color.r*min_alpha,
            new_color.g*min_alpha,
            new_color.b*min_alpha,
            min_alpha);
    """)

    ## A shader to create a radial gradient (where the colour changes based on
    ## how far the pixel is from the center).
    renpy.register_shader("feniks.radial_gradient", variables="""
        uniform mat4 u_one_to_four;
        uniform mat4 u_five_to_eight;
        uniform mat4 u_nine_to_twelve;
        uniform mat4 u_thirteen_to_sixteen;

        uniform mat4 u_thresholds;

        uniform float u_elliptical;
        uniform float u_calculate_center;
        uniform vec2 u_center;
        uniform float u_scale;

        uniform vec2 u_model_size;
        varying vec2 v_position;
        varying vec2 v_size;
        attribute vec4 a_position;
        varying vec2 v_coords;
    """, vertex_300="""
        v_coords = vec2(a_position.x / u_model_size.x, a_position.y / u_model_size.y);
        v_position = a_position.xy;
        v_size = u_model_size.xy;
    """, fragment_functions="""
        // Return the correct vec4 colour based on the provided index.
        // A convenience function due to lack of arrays.
        vec4 get_color(int ind, mat4 color1, mat4 color2, mat4 color3, mat4 color4) {
            if (ind < 4) {
                return color1[ind];
            } else if (ind < 8) {
                return color2[ind-4];
            } else if (ind < 12) {
                return color3[ind-8];
            } else {
                return color4[ind-12];
            }
        }

        // Return the number of the color this pixel falls below.
        vec2 find_threshold(mat4 thresholds, float num) {
            for (int i = 0; i < 4; i++) {
                for (int j = 0; j < 4; j++) {
                    if (num < thresholds[i][j]) {
                        return vec2(i, j);
                    }
                }
            }
            return vec2(3, 3);
        }
        int myRound(float num) {
            return int(num + 0.5);
        }
    """, fragment_300="""
        float num = 0.0;
        vec2 center = vec2(0.5);

        if (u_calculate_center > 0.5) {
            center = u_center / v_size;
        } else {
            center = u_center;
        }

        // Distance from the center of the gradient circle.
        if (u_elliptical < 0.5) {
            num = distance(v_position, center * v_size);
            // Divisor is the distance from the center to the closest edge
            float div = min(v_size.x / 2.0, v_size.y / 2.0);
            num /= div;
            // Divide it by the scale
            num /= u_scale;
            num = min(num, 1.0);
            num = smoothstep(0.0, 1.0, num);
        } else {
            num = distance(center, v_coords);
            // Normalize because diagonals are longer than 1.0
            num = num / sqrt(2.0*pow(0.5, 2.0)) ;
            // Divide it by the scale
            num /= u_scale;
            num = min(num, 1.0);
        }

        vec4 old_gl = gl_FragColor;
        vec4 new_color = vec4(0.0);

        vec4 first_color = vec4(0.0);
        vec4 second_color = vec4(0.0);
        vec2 thresh1 = vec2(0.0);
        vec2 thresh2 = vec2(0.0);

        // Calculate which thresholds the pixel falls between.
        thresh1 = find_threshold(u_thresholds, num);

        int threshold = myRound(thresh1.x*4.0 + thresh1.y);
        first_color = get_color(threshold, u_one_to_four, u_five_to_eight,
            u_nine_to_twelve, u_thirteen_to_sixteen);
        int threshold2 = myRound(max(float(threshold)-1.0, 0.0));

        // Make sure the thresholds are within range
        if (thresh1.y > 0.0) {
            thresh2 = vec2(thresh1.x, thresh1.y-1.0);
        } else {
            thresh2 = vec2(thresh1.x-1.0, 3.0);
            if (thresh2.x < 0.0) {
                thresh2 = vec2(0.0, 0.0);
            }
        }

        second_color = get_color(threshold2, u_one_to_four, u_five_to_eight,
            u_nine_to_twelve, u_thirteen_to_sixteen);

        // Properly multiply the colour alphas
        first_color = vec4(first_color.rgb * first_color.a, first_color.a);
        second_color = vec4(second_color.rgb * second_color.a, second_color.a);

        // The amount to blend first_color and second_color
        float blend_amount = 0.0;

        // Make sure we're not dividing by zero
        if (u_thresholds[myRound(thresh1.x)][myRound(thresh1.y)] != u_thresholds[myRound(thresh2.x)][myRound(thresh2.y)]) {
            blend_amount = (num - u_thresholds[myRound(thresh2.x)][myRound(thresh2.y)]);
            blend_amount /= (u_thresholds[myRound(thresh1.x)][myRound(thresh1.y)]
                    - u_thresholds[myRound(thresh2.x)][myRound(thresh2.y)]);
            blend_amount = smoothstep(0.0, 1.0, blend_amount);
        }
        new_color = mix(second_color, first_color, blend_amount);
        if (new_color.a > 0.0) {
            // Divide the alpha to get the true colour so we can
            // premultiply the final alpha.
            new_color.r /= new_color.a;
            new_color.g /= new_color.a;
            new_color.b /= new_color.a;
        }
        float min_alpha = min(old_gl.a, new_color.a);
        // Apply the new colour to the image, using the alpha of the original.
        gl_FragColor = vec4(new_color.r*min_alpha,
            new_color.g*min_alpha,
            new_color.b*min_alpha,
            min_alpha);
    """)

    ## A shader to create an angle gradient (where the colour changes based on
    ## how far the pixel is along a circumference of a circle at the center).
    ## The default angle, 0, is at 12:00.
    renpy.register_shader("feniks.angle_gradient", variables="""
        uniform mat4 u_one_to_four;
        uniform mat4 u_five_to_eight;
        uniform mat4 u_nine_to_twelve;
        uniform mat4 u_thirteen_to_sixteen;

        uniform mat4 u_thresholds;
        uniform float u_angle;
        uniform float u_calculate_center;
        uniform vec2 u_center;

        uniform vec2 u_model_size;
        varying vec2 v_size;
        attribute vec4 a_position;
        varying vec2 v_coords;
    """, vertex_300="""
        v_coords = vec2(a_position.x / u_model_size.x, a_position.y / u_model_size.y);
        v_size = u_model_size.xy;
    """, fragment_functions="""
        // Return the correct vec4 colour based on the provided index.
        // A convenience function due to lack of arrays.
        vec4 get_color(int ind, mat4 color1, mat4 color2, mat4 color3, mat4 color4) {
            if (ind < 4) {
                return color1[ind];
            } else if (ind < 8) {
                return color2[ind-4];
            } else if (ind < 12) {
                return color3[ind-8];
            } else {
                return color4[ind-12];
            }
        }

        // Return the number of the color this pixel falls below.
        vec2 find_threshold(mat4 thresholds, float num) {
            for (int i = 0; i < 4; i++) {
                for (int j = 0; j < 4; j++) {
                    if (num < thresholds[i][j]) {
                        return vec2(i, j);
                    }
                }
            }
            return vec2(3, 3);
        }
        int myRound(float num) {
            return int(num + 0.5);
        }
    """, fragment_300="""
        vec2 center = vec2(0.5);
        float PI = 3.1415926535897932384626433832795;

        if (u_calculate_center > 0.5) {
            center = u_center / v_size;
        } else {
            center = u_center;
        }

        // Move the whole thing so the center is at (0, 0) for calculations
        vec2 new_coords = v_coords - center;
        // Use atan to determine the angle.
        float arc = (atan(new_coords.y, new_coords.x) + PI);
        // num is the % of that
        // Circumference = 2*pi*r -> radius is cancelled from arc length
        float num = min(arc / (2.0 * PI), 1.0);

        // Add to num to account for the provided angle.
        // The angle rotates counter-clockwise and we want to rotate clockwise
        num += (2.0*PI - radians(u_angle)) / (2.0*PI);
        if (num > 1.0 || num < 0.0) {
            num = mod(num, 1.0);
        }
        vec4 old_gl = gl_FragColor;
        vec4 new_color = vec4(0.0);

        vec4 first_color = vec4(0.0);
        vec4 second_color = vec4(0.0);
        vec2 thresh1 = vec2(0.0);
        vec2 thresh2 = vec2(0.0);

        // Calculate which thresholds the pixel falls between.
        thresh1 = find_threshold(u_thresholds, num);

        int threshold = myRound(thresh1.x*4.0 + thresh1.y);
        first_color = get_color(threshold, u_one_to_four, u_five_to_eight,
            u_nine_to_twelve, u_thirteen_to_sixteen);
        int threshold2 = myRound(max(float(threshold)-1.0, 0.0));

        // Make sure the thresholds are within range
        if (thresh1.y > 0.0) {
            thresh2 = vec2(thresh1.x, thresh1.y-1.0);
        } else {
            thresh2 = vec2(thresh1.x-1.0, 3.0);
            if (thresh2.x < 0.0) {
                thresh2 = vec2(0.0, 0.0);
            }
        }

        second_color = get_color(threshold2, u_one_to_four, u_five_to_eight,
            u_nine_to_twelve, u_thirteen_to_sixteen);

        // Properly multiply the colour alphas
        first_color = vec4(first_color.rgb * first_color.a, first_color.a);
        second_color = vec4(second_color.rgb * second_color.a, second_color.a);

        // The amount to blend first_color and second_color
        float blend_amount = 0.0;

        // Make sure we're not dividing by zero
        if (u_thresholds[myRound(thresh1.x)][myRound(thresh1.y)] != u_thresholds[myRound(thresh2.x)][myRound(thresh2.y)]) {
            blend_amount = (num - u_thresholds[myRound(thresh2.x)][myRound(thresh2.y)]);
            blend_amount /= (u_thresholds[myRound(thresh1.x)][myRound(thresh1.y)]
                    - u_thresholds[myRound(thresh2.x)][myRound(thresh2.y)]);
        }
        new_color = mix(second_color, first_color, blend_amount);
        if (new_color.a > 0.0) {
            // Divide the alpha to get the true colour so we can
            // premultiply the final alpha.
            new_color.r /= new_color.a;
            new_color.g /= new_color.a;
            new_color.b /= new_color.a;
        }
        float min_alpha = min(old_gl.a, new_color.a);
        // Apply the new colour to the image, using the alpha of the original.
        gl_FragColor = vec4(new_color.r*min_alpha,
            new_color.g*min_alpha,
            new_color.b*min_alpha,
            min_alpha);
    """)


################################################################################
## HELPER FUNCTIONS
################################################################################
init python:
    def GradientDisplayable(colors, thresholds=None, center=(0.5, 0.5),
            scale=1.0, angle=0, elliptical=False, mirror=False, **kwargs):
        """
        A convenience function to create a displayable with a gradient shader.
        The properties are the same as linear_gradient, radial_gradient, and
        angle_gradient below, with the additional property "kind" to specify
        which of the three to use. Any additional keyword arguments are passed
        to the Solid displayable, such as size or position properties.
        """
        kind = kwargs.pop("kind", "linear")
        if kind == "linear":
            tr = linear_gradient(colors, thresholds, center, scale, angle, mirror)
        elif kind == "radial":
            tr = radial_gradient(colors, thresholds, center, scale, elliptical)
        elif kind == "angle":
            tr = angle_gradient(colors, thresholds, center, angle)
        else:
            raise Exception("Invalid kind of gradient. Must be 'linear', 'radial', or 'angle'.")

        return At(Transform("#FFF", **kwargs), tr)

    def linear_gradient(colors, thresholds=None, center=(0.5, 0.5), scale=1.0,
            angle=0, mirror=False):
        """
        A convenience method which prepares input for a linear shader.

        Parameters:
        -----------
        colors : list of Color
            A list of colours to use in the gradient. Up to 16 colours may be
            provided.
        thresholds : list of float
            A list of numbers between 0.0 and 1.0 which determine where the
            colours change. The first number is where the first colour changes
            to the second, the second number is where the second colour changes
            to the third, etc. Up to 16 thresholds may be provided.
        scale : float
            The scale of the gradient. 1.0 is the default, and will fill the
            entire image in at least one dimension. < 1.0 makes the gradient
            smaller and > 1.0 makes it bigger.
        angle : float
            The angle of the gradient, in degrees. 0.0 is straight up and down.
        mirror : bool
            If True, the gradient will be mirrored. This is useful for creating
            symmetrical gradients.
        """
        (one_to_four, five_to_eight, nine_to_twelve, thirteen_to_sixteen,
            thresholds, calculate_center) = prep_gradient_args(colors,
                thresholds, center)

        ## Return the final transform
        return linear_gradient_transform(one_to_four, five_to_eight,
            nine_to_twelve, thirteen_to_sixteen, thresholds, angle, center,
            scale, calculate_center, mirror)

    def radial_gradient(colors, thresholds=None, center=(0.5, 0.5), scale=1.0,
            elliptical=False):
        """
        A convenience method which prepares input for a radial shader.

        Parameters:
        -----------
        colors : list of Color
            A list of colours to use in the gradient. Up to 16 colours may be
            provided.
        thresholds : list of float
            A list of numbers between 0.0 and 1.0 which determine where the
            colours change. The first number is where the first colour changes
            to the second, the second number is where the second colour changes
            to the third, etc. Up to 16 thresholds may be provided.
        center : tuple of float
            The center of the gradient, as a percentage of the image size.
            (0.5, 0.5) is the center of the image. (0.0, 0.0) is the top left
            corner, and (1.0, 1.0) is the bottom right corner.
            You may also provide exact pixel values which will be converted
            into floats.
        scale : float
            The scale of the gradient. 1.0 is the default, and will fill the
            entire image in at least one dimension. < 1.0 makes the radius
            smaller and > 1.0 makes it bigger.
        elliptical : bool
            If False, the radial gradient will be circular regardless of the
            dimensions of the image. If True, the gradient will be elliptical
            depending on the dimensions of the image.
        """
        (one_to_four, five_to_eight, nine_to_twelve, thirteen_to_sixteen,
            thresholds, calculate_center) = prep_gradient_args(colors,
                thresholds, center)

        ## Return the final transform
        return radial_gradient_transform(one_to_four, five_to_eight,
            nine_to_twelve, thirteen_to_sixteen, thresholds, elliptical,
            center, scale, calculate_center)

    def angle_gradient(colors, thresholds=None, center=(0.5, 0.5), angle=0):
        """
        A convenience method which prepares input for a radial shader.

        Parameters:
        -----------
        colors : list of Color
            A list of colours to use in the gradient. Up to 16 colours may be
            provided.
        thresholds : list of float
            A list of numbers between 0.0 and 1.0 which determine where the
            colours change. The first number is where the first colour changes
            to the second, the second number is where the second colour changes
            to the third, etc. Up to 16 thresholds may be provided.
        center : tuple of float
            The center of the gradient, as a percentage of the image size.
            (0.5, 0.5) is the center of the image. (0.0, 0.0) is the top left
            corner, and (1.0, 1.0) is the bottom right corner.
            You may also provide exact pixel values which will be converted
            into floats.
        angle : int
            The angle, in degrees, of the starting point of the gradient.
            0.0 has the gradient start at 12:00.
        """
        (one_to_four, five_to_eight, nine_to_twelve, thirteen_to_sixteen,
            thresholds, calculate_center) = prep_gradient_args(colors,
                thresholds, center)
        angle = int(angle+90)
        ## Return the final transform
        return angle_gradient_transform(one_to_four, five_to_eight, nine_to_twelve,
            thirteen_to_sixteen, thresholds, center, angle,
            calculate_center)

    def prep_gradient_args(colors, thresholds, center):
        """
        Prepare the colours and thresholds into a shader-friendly format
        (mostly matrices).

        Returns:
        --------
        matrix, matrix, matrix, matrix, matrix, bool
            The first four matrices correspond to 16 colours, and the fifth
            to the thresholds. The bool is whether the center is provided
            as a percentage or as pixels.
        """
        num_colors = len(colors)
        ## Fill out the colour list to 16 colours.
        while len(colors) < 16:
            colors.append(colors[-1])

        if not thresholds:
            ## Evenly space them from 0 - 1 based on number of colours
            thresholds = [x / float(num_colors-1) for x in range(num_colors)]

        ## Fill out the threshold list to 16 thresholds.
        while len(thresholds) < 16:
            thresholds.append(thresholds[-1])

        ## Is the center provided as a percentage or as pixels?
        if isinstance(center[0], float):
            calculate_center = False
        else:
            calculate_center = True

        ## Make the four matrices of colours.
        one_to_four = colors_to_matrix(*colors[0:4])
        five_to_eight = colors_to_matrix(*colors[4:8])
        nine_to_twelve = colors_to_matrix(*colors[8:12])
        thirteen_to_sixteen = colors_to_matrix(*colors[12:16])

        ## Turn the thresholds into a matrix. Need to transpose columns to rows.
        thresholds = Matrix(thresholds[0::4] + thresholds[1::4]
            + thresholds[2::4] + thresholds[3::4])

        return (one_to_four, five_to_eight, nine_to_twelve, thirteen_to_sixteen,
            thresholds, calculate_center)

    def colors_to_matrix(color1, color2, color3, color4):
        """
        Transform the provided four colours into a 4x4
        matrix with the colours in the right positions.
        """
        color1 = Color(color1).rgba
        color2 = Color(color2).rgba
        color3 = Color(color3).rgba
        color4 = Color(color4).rgba

        rows = [ ]
        for i in range(4):
            rows.append(color1[i])
            rows.append(color2[i])
            rows.append(color3[i])
            rows.append(color4[i])
        return Matrix(rows)

################################################################################
## TRANSFORMS
################################################################################
## Typically you won't call these directly, but instead use the helper
## functions provided above.
transform -100 linear_gradient_transform(color1, color2, color3, color4,
        thresholds, angle, center, scale, calculate_center, mirror):
    shader "feniks.linear_gradient"
    mesh True
    u_one_to_four color1
    u_five_to_eight color2
    u_nine_to_twelve color3
    u_thirteen_to_sixteen color4
    u_thresholds thresholds
    u_angle angle
    u_mirror (1.0 if mirror else 0.0)
    u_calculate_center (1.0 if calculate_center else 0.0)
    u_center center
    u_scale scale

transform -100 radial_gradient_transform(color1, color2, color3, color4,
        thresholds, elliptical, center, scale, calculate_center):
    shader "feniks.radial_gradient"
    mesh True
    u_one_to_four color1
    u_five_to_eight color2
    u_nine_to_twelve color3
    u_thirteen_to_sixteen color4
    u_thresholds thresholds
    u_elliptical (1.0 if elliptical else 0.0)
    u_calculate_center (1.0 if calculate_center else 0.0)
    u_center center
    u_scale scale

transform -100 angle_gradient_transform(color1, color2, color3, color4,
        thresholds, center, angle, calculate_center):
    shader "feniks.angle_gradient"
    mesh True
    u_one_to_four color1
    u_five_to_eight color2
    u_nine_to_twelve color3
    u_thirteen_to_sixteen color4
    u_thresholds thresholds
    u_angle angle
    u_calculate_center (1.0 if calculate_center else 0.0)
    u_center center


################################################################################
## Code to archive this file for a distributed game. Do not remove.
init python:
    build.classify("**gradient_shaders.rpy", None)
    build.classify("**gradient_shaders.rpyc", "archive")
################################################################################
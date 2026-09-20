































define -200 MAX_COLORIZE_COLORS = 7



define -200 COLORIZE_MESH_DEFAULT = False

init -100 python:
    
    
    
    
    
    renpy.register_shader("feniks.multicolor_image", variables="""
        uniform vec4 u_color1;
        uniform vec4 u_color2;
        uniform vec4 u_color3;
        uniform vec4 u_color4;
        uniform vec4 u_color5;
        uniform vec4 u_color6;
        uniform vec4 u_color7;
        uniform vec4 u_color8;
        uniform float u_horizontal;
        uniform float u_num_colors;
        uniform vec2 u_model_size;
        varying float v_gradient_x_done;
        varying float v_gradient_y_done;
        attribute vec4 a_position;
    """, vertex_300="""
        v_gradient_x_done = a_position.x / u_model_size.x;
        v_gradient_y_done = a_position.y / u_model_size.y;
    """, fragment_300="""
        float num = 0.0;
        // If the gradient is horizontal, use the x value instead of y.
        if (u_horizontal > 0.5) {
            num = v_gradient_x_done;
        } else {
            num = v_gradient_y_done;
        }

        vec4 old_gl = gl_FragColor;
        vec4 new_color = vec4(0.0);
        float num_segments = u_num_colors-1.0;
        float segment_length = 1.0 / num_segments;

        if (num <= segment_length * 1.0) {
            new_color = mix(u_color1, u_color2, 1.0 - (segment_length - num) / segment_length);
        } else if (num <= segment_length * 2.0) {
            new_color = mix(u_color2, u_color3, 1.0 - (segment_length * 2.0 - num) / segment_length);
        } else if (num <= segment_length * 3.0) {
            new_color = mix(u_color3, u_color4, 1.0 - (segment_length * 3.0 - num) / segment_length);
        } else if (num <= segment_length * 4.0) {
            new_color = mix(u_color4, u_color5, 1.0 - (segment_length * 4.0 - num) / segment_length);
        } else if (num <= segment_length * 5.0) {
            new_color = mix(u_color5, u_color6, 1.0 - (segment_length * 5.0 - num) / segment_length);
        } else if (num <= segment_length * 6.0) {
            new_color = mix(u_color6, u_color7, 1.0 - (segment_length * 6.0 - num) / segment_length);
        } else if (num <= segment_length * 7.0) {
            new_color = mix(u_color7, u_color8, 1.0 - (segment_length * 7.0 - num) / segment_length);
        // The same pattern as above may be followed here to add more colours,
        // if needed.
        } else {
            new_color = u_color8;
        }

        // Apply the new colour to the image, using the alpha of the original.
        gl_FragColor = vec4(new_color.r*old_gl.a,
            new_color.g*old_gl.a,
            new_color.b*old_gl.a,
            old_gl.a);
    """)
    
    
    
    
    
    renpy.register_shader("feniks.multi_colorize2", variables="""
        uniform mat4 u_highlight;
        uniform mat4 u_color;
        uniform mat4 u_color2;
        uniform mat4 u_color3;
        uniform mat4 u_color4;
        uniform mat4 u_color5;
        uniform mat4 u_shadow;

        uniform vec4 u_lightest;
        uniform vec4 u_midpoint;
        uniform vec4 u_midpoint2;
        uniform vec4 u_midpoint3;
        uniform vec4 u_midpoint4;
        uniform vec4 u_midpoint5;
        uniform vec4 u_darkest;

        uniform float u_blend;
        uniform sampler2D tex0;
        varying vec2 v_coords;
        uniform vec2 u_model_size;
        attribute vec4 a_position;
    """, vertex_300="""
        v_coords = vec2(a_position.x / u_model_size.x, a_position.y / u_model_size.y);
    """, fragment_functions="""

    float get_mix_pct(float lower, float upper, float value) {
        // Return the mix percentage based on the provided thresholds
        return max(min((value-lower)/(upper-lower), 1.0), 0.0);
    }
    bool within_threshold(float num1, float num2, float threshold) {
        // Return whether these numbers are within the threshold of each other
        // ie. are they close enough to be considered equal?
        // Useful so we can still classify colours as gray.
        return abs(num1-num2) <= threshold;
    }

    """, fragment_300="""
        // Grab the original colour
        vec4 og_color = texture2D(tex0, v_coords);

        // Contains a final mixed colour for the RGB channels.
        mat4 final_rgb = mat4(0.0);
        // Contains a final colour to be returned.
        vec4 final_color = vec4(0.0);

        float threshold = 0.004;

        mat4 left_color = mat4(0.0);
        mat4 right_color = mat4(0.0);
        float mix_pct = 1.0;

        // Divide the RGB channels by the alpha to get the "true" colour,
        // since we're dealing with premultiplied alpha.
        og_color = vec4(
            og_color.r/og_color.a,
            og_color.g/og_color.a,
            og_color.b/og_color.a,
            og_color.a);

        // When comparing, we deal with the maximum of the three RGB channels.
        float og_color_check = max(og_color.r, max(og_color.g, og_color.b));

        for (int i = 0; i < 4; ++i) {
            // Check if it's equal to or less than the shadow point
            if (og_color_check <= u_darkest[i]) {
                // Yes; it's just the shadow colour
                left_color[i] = u_shadow[i];
                right_color[i] = u_shadow[i];
            // Check if it's equal to or greater than the highlight point
            } else if (og_color_check >= u_lightest[i]) {
                // Yes; it's just the highlight colour
                left_color[i] = u_highlight[i];
                right_color[i] = u_highlight[i];
            // Check if it's between the shadow and the first midpoint
            } else if (og_color_check <= u_midpoint5[i]) {
                left_color[i] = u_shadow[i];
                right_color[i] = u_color5[i];
                mix_pct = get_mix_pct(u_darkest[i], u_midpoint5[i], og_color_check);
            // Check if it's between any midpoint pairs
            } else if (og_color_check <= u_midpoint4[i]) {
                left_color[i] = u_color5[i];
                right_color[i] = u_color4[i];
                mix_pct = get_mix_pct(u_midpoint5[i], u_midpoint4[i], og_color_check);
            } else if (og_color_check <= u_midpoint3[i]) {
                left_color[i] = u_color4[i];
                right_color[i] = u_color3[i];
                mix_pct = get_mix_pct(u_midpoint4[i], u_midpoint3[i], og_color_check);
            } else if (og_color_check <= u_midpoint2[i]) {
                left_color[i] = u_color3[i];
                right_color[i] = u_color2[i];
                mix_pct = get_mix_pct(u_midpoint3[i], u_midpoint2[i], og_color_check);
            } else if (og_color_check <= u_midpoint[i]) {
                left_color[i] = u_color2[i];
                right_color[i] = u_color[i];
                mix_pct = get_mix_pct(u_midpoint2[i], u_midpoint[i], og_color_check);
            } else if (og_color_check <= u_lightest[i]) {
                left_color[i] = u_color[i];
                right_color[i] = u_highlight[i];
                mix_pct = get_mix_pct(u_midpoint[i], u_lightest[i], og_color_check);
            }

            // If we're not blending, then all the colours have hard cutoffs
            if (u_blend < 0.5) {
                mix_pct = 1.0;
            }
            // Mix together the final colours
            // Premultiply the alpha into the two colours
            left_color[i] = vec4(
                left_color[i].r*left_color[i].a,
                left_color[i].g*left_color[i].a,
                left_color[i].b*left_color[i].a,
                left_color[i].a);
            right_color[i] = vec4(
                right_color[i].r*right_color[i].a,
                right_color[i].g*right_color[i].a,
                right_color[i].b*right_color[i].a,
                right_color[i].a);
            final_rgb[i] = mix(left_color[i], right_color[i], mix_pct);
        }

        vec4 red = final_rgb[0];
        vec4 green = final_rgb[1];
        vec4 blue = final_rgb[2];
        vec4 gray = final_rgb[3];

        if (within_threshold(og_color.r, og_color.g, threshold)
                && within_threshold(og_color.b, og_color.g, threshold)
                && within_threshold(og_color.r, og_color.b, threshold)) {
            // It's just a shade of gray; use the default colour
            gl_FragColor = vec4(
                gray.r*og_color.a,
                gray.g*og_color.a,
                gray.b*og_color.a,
                gray.a*og_color.a);
            return;
        }

        float min_channel = min(og_color.r, min(og_color.g, og_color.b));
        float max_channel = max(og_color.r, max(og_color.g, og_color.b));

        // E.g. if the channels are (0.9, 0.8, 0.9) then the final colour will
        // mix the RGB channels almost equally.
        // If the channels are 0.9, 0.6, 0.3 then R=0.5, G=0.33, B=0.16.
        float red_pct = (og_color.r - min_channel) / (max_channel - min_channel);
        float green_pct = (og_color.g - min_channel) / (max_channel - min_channel);
        float blue_pct = (og_color.b - min_channel) / (max_channel - min_channel);

        // Start by mixing the red and blue
        float red_blue_mix_pct = blue_pct / (red_pct + blue_pct);
        final_color = mix(red, blue, min(max(red_blue_mix_pct, 0.0), 1.0));

        // Now mix the green in
        float green_mix_pct = green_pct / (red_pct + blue_pct + green_pct);
        final_color = mix(final_color, green, min(max(green_mix_pct, 0.0), 1.0));

        // If the min RGB channel was not 0 then we mix the default colour in.
        // For a colour like (0.8, 0.2, 0.2) it should be blended a bit with
        // the default channel. It COULD have been (0.8, 0.0, 0.0), but wasn't.
        // The equivalent gray is 0.8, 0.8, 0.8, so it's 80% coloured and 20%
        // gray. So we should mix in 20% of the default colour.
        float default_mix_pct = min_channel/max_channel;
        final_color = mix(final_color, gray, min(max(default_mix_pct, 0.0), 1.0));

        // Finally, premultiply the alpha
        gl_FragColor = vec4(
            final_color.r*og_color.a,
            final_color.g*og_color.a,
            final_color.b*og_color.a,
            final_color.a*og_color.a);
        return;
    """)









transform -100 multicolor_image_transform(color1="#fff", color2=None, color3=None, color4=None, color5=None, color6=None, color7=None, color8=None, vertical=False, matrix=IdentityMatrix()):


    shader "feniks.multicolor_image"
    mesh True


    u_color1 Color(("#fff" if color1 is None else color1)).rgba
    u_color2 Color(("#fff" if color2 is None else color2)).rgba
    u_color3 Color(("#fff" if color3 is None else color3)).rgba
    u_color4 Color(("#fff" if color4 is None else color4)).rgba
    u_color5 Color(("#fff" if color5 is None else color5)).rgba
    u_color6 Color(("#fff" if color6 is None else color6)).rgba
    u_color7 Color(("#fff" if color7 is None else color7)).rgba
    u_color8 Color(("#fff" if color8 is None else color8)).rgba


    u_num_colors float(len([x for x in [color1, color2, color3, color4,
        color5, color6, color7, color8] if x is not None]))

    u_horizontal (1.0 if not vertical else 0.0)
    matrixcolor matrix




transform -100 multi_colorize_transform_rgb(highlight, midtone, midtone2, midtone3, midtone4, midtone5, shadow, lightest, midpoint, midpoint2, midpoint3, midpoint4, midpoint5, darkest, blend=True, mesh=COLORIZE_MESH_DEFAULT):


    shader "feniks.multi_colorize2"





    mesh mesh

    u_highlight highlight
    u_color midtone
    u_color2 midtone2
    u_color3 midtone3
    u_color4 midtone4
    u_color5 midtone5
    u_shadow shadow
    u_lightest lightest
    u_midpoint midpoint
    u_midpoint2 midpoint2
    u_midpoint3 midpoint3
    u_midpoint4 midpoint4
    u_midpoint5 midpoint5
    u_darkest darkest
    u_blend (1.0 if blend else 0.0)




init -100 python:
    
    
    def multi_colorize_rgb(red, green, blue, gray, red_thresh=None,
            green_thresh=None, blue_thresh=None, gray_thresh=None,
            blend=True, rgb_obj=False, mesh=COLORIZE_MESH_DEFAULT):
        """
        A convenience function to turn lists of colours and thresholds
        into a transform for the colorize shader.

        Parameters:
        -----------
        red, green, blue, gray : list
            A list of colours to be used for the colorization. There can be
            up to 7 colours.
        red_thresh, green_thresh, blue_thresh, gray_thresh : list
            A list of thresholds to be used for the colorization. There can
            be up to 7 thresholds. If not provided, they will be automatically
            calculated.
        blend : bool
            Whether to blend between the colours or not. If False, the colours
            will have hard cutoffs.
        rgb_obj : bool
            Whether the provided colours are already in an RGBColorize object
            or not. If True, the colours and thresholds will be used directly.
            If False, they will be converted to an RGBColorize object first.
        mesh : bool
            If True, the transform will use a mesh. If False, it will not.
        """
        if not rgb_obj:
            
            
            rgb = RGBColorize(gray, gray_thresh, red, red_thresh,
                green, green_thresh, blue, blue_thresh)
            red = rgb.red
            green = rgb.green
            blue = rgb.blue
            gray = rgb.gray
            red_thresh = rgb.red_thresh
            green_thresh = rgb.green_thresh
            blue_thresh = rgb.blue_thresh
            gray_thresh = rgb.gray_thresh
        
        
        args = [0]*MAX_COLORIZE_COLORS*2
        for i in range(MAX_COLORIZE_COLORS):
            args[i] = transform_to_matrix(red[i], green[i], blue[i], gray[i])
            args[i+MAX_COLORIZE_COLORS] = (red_thresh[i], green_thresh[i],
                blue_thresh[i], gray_thresh[i])
        
        return multi_colorize_transform_rgb(*args, blend=blend, mesh=mesh)
    
    def multi_colorize_img(st, at, img, var_name, color_splits):
        """
        A DynamicDisplayable which interpolates the colorization of an image
        based on a provided variable and a list of colour splits.

        Parameters:
        -----------
        st, at : float
            The shown timebase and animated timebase of the DynamicDisplayable.
            Automatically provided.
        img : Displayable
            The image to be recoloured.
        var_name : string
            The string name of the variable being tracked for the total percent
            between the provided colours.
        color_splits : RGBColorize[]
            This should be a list of RGBColorize objects with information on
            the colours and thresholds to be used for each individual colour.
        """
        
        value = getattr(store, var_name)
        
        num_colors = len(color_splits)
        section_size = 100 / (num_colors-1.0)
        
        first_color_index = value // section_size
        first_color_index = int(min(num_colors-2, first_color_index))
        
        pct = (value - (section_size*first_color_index)) / section_size
        
        first_color_split = color_splits[first_color_index]
        second_color_split = color_splits[first_color_index+1]
        
        colors1 = [first_color_split.red, first_color_split.green,
            first_color_split.blue, first_color_split.gray]
        colors2 = [second_color_split.red, second_color_split.green,
            second_color_split.blue, second_color_split.gray]
        thresholds1 = [first_color_split.red_thresh, first_color_split.green_thresh,
            first_color_split.blue_thresh, first_color_split.gray_thresh]
        thresholds2 = [second_color_split.red_thresh, second_color_split.green_thresh,
            second_color_split.blue_thresh, second_color_split.gray_thresh]
        
        colors = [ ]
        thresholds = [ ]
        
        for color_set1, colour_set2 in zip(colors1, colors2):
            chan_colours = [ ]
            for c1, c2 in zip(color_set1, colour_set2):
                chan_colours.append(Color(c1).interpolate(Color(c2), pct))
            colors.append(chan_colours)
        
        for thresh_set1, thresh_set2 in zip(thresholds1, thresholds2):
            thresh = [ ]
            for t1, t2 in zip(thresh_set1, thresh_set2):
                thresh.append((t2-t1)*pct + t1)
            thresholds.append(thresh)
        
        
        rgb = RGBColorize(colors[3], thresholds[3], colors[0], thresholds[0],
            colors[1], thresholds[1], colors[2], thresholds[2],
            num_shades=first_color_split.num_shades,
            blend=first_color_split.blend, mesh=first_color_split.mesh)
        
        
        return At(img, rgb.transform), None
    
    def multicolor_image(*colors, **properties):
        """
        A Function which simplifies passing properties off to the multicolor
        image transform and ensures it does not have more colours than it
        can handle.
        """
        if len(colors) > 0 and isinstance(colors[0], RGBColorize):
            
            
            
            mid_shade = (colors[0].num_shades-1) // 2
            colors = [c.gray[mid_shade] for c in colors]
        
        if len(colors) > 8:
            
            
            
            new_colors = colors[::-(-len(colors)//8)]
        else:
            new_colors = colors
        return multicolor_image_transform(*new_colors, **properties)
    
    
    class RGBColorize():
        """
        A class to make it easier to manage the information needed by the
        RGB colorize shader.

        Attributes:
        -----------
        gray : Color[]
            A list of Color objects for the gray recolouring of this image.
        red : Color[]
            A list of Color objects for the red channel of this image.
        green : Color[]
            A list of Color objects for the green channel of this image.
        blue : Color[]
            A list of Color objects for the blue channel of this image.
        gray_thresh : float[]
            A list of thresholds for the gray recolouring of this image.
        red_thresh : float[]
            A list of thresholds for the red channel of this image.
        green_thresh : float[]
            A list of thresholds for the green channel of this image.
        blue_thresh : float[]
            A list of thresholds for the blue channel of this image.
        rgb : bool
            True if this image has any RGB recolouring, False otherwise.
        red_num : int
            The number of red shades used by this image.
        green_num : int
            The number of green shades used by this image.
        blue_num : int
            The number of blue shades used by this image.
        num_shades : int
            The number of shades used by this image.
        blend : bool
            True if this image blends colours or not.
        mesh : bool
            True if this image should use a mesh or not.
        """
        def __init__(self, gray, gray_thresh=None, red=None, red_thresh=None,
                green=None, green_thresh=None, blue=None, blue_thresh=None,
                rgb=False, blend=True, mesh=COLORIZE_MESH_DEFAULT, name=None,
                num_shades=None):
            
            self.red = red or [ ]
            self.green = green or [ ]
            self.blue = blue or [ ]
            self.gray = gray or [ ]
            self.num_shades = num_shades or len(gray)
            self.gray_thresh = gray_thresh or [ ]
            self.red_thresh = red_thresh or [ ]
            self.green_thresh = green_thresh or [ ]
            self.blue_thresh = blue_thresh or [ ]
            self.red_num = len(self.red)
            self.green_num = len(self.green)
            self.blue_num = len(self.blue)
            self.rgb = rgb or any([self.red, self.green, self.blue])
            self.blend = blend
            self.mesh = mesh
            self.name = name
            
            
            if self.rgb:
                
                
                if all([self.green == self.gray, self.blue == self.gray,
                        self.red == self.gray,
                        self.red_thresh == self.gray_thresh,
                        self.green_thresh == self.gray_thresh,
                        self.blue_thresh == self.gray_thresh,
                        ]):
                    self.rgb = False
                    self.red = [ ]
                    self.green = [ ]
                    self.blue = [ ]
                    self.red_thresh = [ ]
                    self.green_thresh = [ ]
                    self.blue_thresh = [ ]
            
            self.convert_input()
            
            self.transform = multi_colorize_rgb(
                self.red, self.green, self.blue, self.gray,
                self.red_thresh, self.green_thresh, self.blue_thresh,
                self.gray_thresh, rgb_obj=True, blend=self.blend,
                mesh=self.mesh)
        
        def convert_input(self):
            """
            Convert current input into a form suitable to be passed off to
            the colorize shader.
            """
            self.gray = self.convert_color(self.gray)
            self.gray_thresh = self.convert_threshold(self.gray_thresh)
            
            self.red = self.convert_color(self.red or self.gray)
            self.green = self.convert_color(self.green or self.gray)
            self.blue = self.convert_color(self.blue or self.gray)
            self.red_thresh = self.convert_threshold(self.red_thresh or self.gray_thresh)
            self.green_thresh = self.convert_threshold(self.green_thresh or self.gray_thresh)
            self.blue_thresh = self.convert_threshold(self.blue_thresh or self.gray_thresh)
        
        def convert_color(self, colors):
            """
            Convert a list of colours to a form appropriate for the colorize
            shader.
            """
            try:
                colors = [Color(c) for c in colors]
            except Exception as e:
                
                
                colors = [Color(tuple(c)) for c in colors]
            
            colors += [colors[-1]]*(MAX_COLORIZE_COLORS-len(colors))
            return colors
        
        def convert_threshold(self, thresh):
            """
            Convert a list of thresholds to a form appropriate for the
            colorize shader.
            """
            thresh = list(thresh)
            if any([t > 1.0 for t in thresh]):
                old_thresh = list(thresh)
                thresh.clear()
                thresh.extend([t/255.0 for t in old_thresh])
            if not thresh:
                div = float(max(1, self.num_shades-1))
                thresh += [1.0/div*i for i in range(self.num_shades)]
                thresh.reverse()
            thresh += [0.0]*(MAX_COLORIZE_COLORS-len(thresh))
            return thresh
        
        def pretty_print(self):
            """
            Prettily format the colours used for this colorization. Returns
            a string which can be used to recreate this RGBColorize object.
            """
            ret = ""
            if not self.rgb:
                ret += "RGBColorize(["
                ret += ", ".join(['"{}"'.format(c.hexcode) for c in self.gray[:self.num_shades]])
                if self.num_shades > 1:
                    ret += "], ["
                    ret += ", ".join(["{}".format(round(t*255.0)) for t in self.gray_thresh[:self.num_shades]])
                if not self.blend:
                    ret += "], blend=False)"
                else:
                    ret += "])"
                return ret
            
            
            ret += "RGBColorize(gray=["
            ret += ", ".join(['"{}"'.format(c.hexcode) for c in self.gray[:self.num_shades]])
            ret += "]"
            
            if self.gray_thresh and self.num_shades > 1:
                ret += ", gray_thresh=["
                ret += ", ".join(["{}".format(round(t*255.0)) for t in self.gray_thresh[:self.num_shades]])
                ret += "]"
            
            if self.red[:self.red_num] != self.gray[:self.num_shades]:
                ret += ", red=["
                ret += ", ".join(['"{}"'.format(c.hexcode) for c in self.red[:self.red_num]])
                if self.red_thresh != self.gray_thresh and self.red_num > 1:
                    ret += "], red_thresh=["
                    ret += ", ".join(["{}".format(round(t*255.0)) for t in self.red_thresh[:self.red_num]])
                ret += "]"
            
            if self.green[:self.green_num] != self.gray[:self.num_shades]:
                ret += ", green=["
                ret += ", ".join(['"{}"'.format(c.hexcode) for c in self.green[:self.green_num]])
                if self.green_thresh != self.gray_thresh and self.green_num > 1:
                    ret += "], green_thresh=["
                    ret += ", ".join(["{}".format(round(t*255.0)) for t in self.green_thresh[:self.green_num]])
                ret += "]"
            
            if self.blue[:self.blue_num] != self.gray[:self.num_shades]:
                ret += ", blue=["
                ret += ", ".join(['"{}"'.format(c.hexcode) for c in self.blue[:self.blue_num]])
                if self.blue_thresh != self.gray_thresh and self.blue_num > 1:
                    ret += "], blue_thresh=["
                    ret += ", ".join(["{}".format(round(t*255.0)) for t in self.blue_thresh[:self.blue_num]])
                ret += "]"
            if not self.blend:
                ret += ", blend=False)"
            else:
                ret += ")"
            return ret
    
    
    def transform_to_matrix(red, green, blue, gray):
        """
        Transform the provided red, green, blue, and gray colours into a 4x4
        matrix with the colours in the right positions.
        """
        red = red.rgba
        green = green.rgba
        blue = blue.rgba
        gray = gray.rgba
        
        rows = [ ]
        for i in range(4):
            rows.append(red[i])
            rows.append(green[i])
            rows.append(blue[i])
            rows.append(gray[i])
        return Matrix(rows)



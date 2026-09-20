### TEXT PREWVIEW CDD ############################################################
##
## Window for previewing text options in settings.
##
############################################################

init -10 python:

    class PreviewText(renpy.Displayable):
        """
        A class to prewiew current text settings.

        Attributes:
        -----------
        text : string
            The text to display for this displayable preview.

        properties : dict
            Optional keyword arguments that will be applied to the text
            to style it.
        """

        def __init__(self, text, **properties):
            super(PreviewText, self).__init__()

            # Store original arguments for recreating the Text child later
            self.original_text = text
            self.original_properties = properties

            # Text displayable that represents PreviewText.
            self.current_child = self.new_text()

            # The "start time" of the animation
            self.start_st = None
            # The current st of the animation
            self.current_st = 0

        def new_text(self):
            """
            Create a new Text object with the current CPS, color, and size.
            """
            return Text(self.original_text, slow=True, slow_cps = preferences.text_cps, size=20, color=persistent.dialogue_color,
            font=persistent.dialogue_typeface,
                        **self.original_properties)


        def update_text(self):
            """
            Update the displayable to show the text at the new properties.
            """

            self.current_child = self.new_text()
            self.start_st = self.current_st



        def render(self, width, height, st, at):
            """
            Render the text too screen.
            """

            # Record when this animation is starting
            if self.start_st is None:
                self.start_st = st

            # Keep track of the current st
            self.current_st = st


            # Trigger this function again when possible,
            # to test and/or update all of this stuff again.
            renpy.redraw(self, 0)

            # Create a render (canvas).
            render = renpy.Render(width, height)

            # Calculate the "virtual" start time / Basically calculating how much time has passed.
            time_elapsed = st - self.start_st


            # Place the Text child onto it, with the adjusted st
            render.place(self.current_child, st = time_elapsed, at = at)
            
            # Return the render.
            return render



default text_preview = PreviewText("This is what would be the preview text. Change the color, typeface, and speed!")


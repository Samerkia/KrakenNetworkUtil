
# Function for colored output
# Usage:
#   print(f"{color(col='yellow', text='help')} {'This is white text'}")
# This will print 'help' in yellow and the rest of the text in the default white.
def color(r=None, g=None, b=None, text=None, col=None):
    colors = {
        "red": (255, 0, 0),
        "green": (0, 255, 0),
        "blue": (0, 0, 255),
        "yellow": (255, 255, 0),
        "cyan": (0, 255, 255),
        "magenta": (255, 0, 255),
        "white": (255, 255, 255),
        "black": (0, 0, 0)
    }

    # If a color name is provided, use the corresponding RGB values
    if col and col in colors:
        r, g, b = colors[col]

    # Check if RGB values are provided
    if r is not None and g is not None and b is not None and text is not None:
        return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)
    else:
        return text  # Default return of plain text if inputs are missing

# This will print an entire passed in string in the chosen color
# Good for a quick print message if it needs to be color coded
def colPr(r=None, g=None, b=None, text=None, col=None):
    colors = {
        "red": (255, 0, 0),
        "green": (0, 255, 0),
        "blue": (0, 0, 255),
        "yellow": (255, 255, 0),
        "cyan": (0, 255, 255),
        "magenta": (255, 0, 255),
        "white": (255, 255, 255),
        "black": (0, 0, 0)
    }

    # If a color name is provided, use the corresponding RGB values
    if col and col in colors:
        r, g, b = colors[col]

    # Check if RGB values are provided
    if r is not None and g is not None and b is not None and text is not None:
        print( "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text) )
    else:
        print(text)  # Default return of plain text if inputs are missing



import argparse

# Import generate and save functions for identicon creation
from identicons._generate import generate, save

def main():
    """
    Main function for the Identicons CLI tool. This function parses command-line
    arguments to generate an identicon image based on the provided text input,
    colors, and dimensions. The identicon is then saved to the specified output path.
    """
    parser = argparse.ArgumentParser(
        description='CLI tool to interface with the Identicons package and generate identicons from text input.'
    )

    # Text input argument
    parser.add_argument(
        '-t', '--text',
        required=True,
        help="Input text from which to generate the identicon."
    )

    # Output file path argument
    parser.add_argument(
        '-f', '--file',
        required=True,
        help="Path to the output file where the identicon will be saved."
    )

    # Primary color for identicon in hexadecimal
    parser.add_argument(
        '-p', '--primary',
        default='0xb4f8c8',
        type=str,
        required=False,
        help="Primary color for the identicon in hexadecimal format. Default is a mint green color."
    )

    # Secondary color for identicon in hexadecimal
    parser.add_argument(
        '-s', '--secondary',
        default='0xffffff',
        type=str,
        required=False,
        help="Secondary color for the identicon in hexadecimal format. Default is white."
    )

    # Width of the output image
    parser.add_argument(
        '-w', '--width',
        default=500,
        type=int,
        required=False,
        help="Specify the width of the output image in pixels. Default is 500."
    )

    # Height of the output image
    parser.add_argument(
        '-hi', '--height',
        default=500,
        type=int,
        required=False,
        help="Specify the height of the output image in pixels. Default is 500."
    )

    # Version argument
    parser.add_argument(
        '-v', '--version',
        action='version',
        version='%(prog)s 0.1.0',
        help='Display the version of the Identicons CLI tool.'
    )

    # Parse the arguments
    args = parser.parse_args()

    # Convert hexadecimal color values to integer
    primary, secondary = int(args.primary, 16), int(args.secondary, 16)
    
    # Generate identicon with specified text and colors
    icon = generate(args.text, primary, secondary)

    # Save the identicon to the specified file path with given dimensions
    save(icon, args.file, args.height, args.width)

# Entry point for script execution
if __name__ == "__main__":
    main()

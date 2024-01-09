import argparse

from identicons._generate import generate, save

def main():

    parser = argparse.ArgumentParser(description=f'CLI tool.')
    parser.add_argument(
        '-t', '--text',
        required=True,
        help="Input text from which to generate the identicon."
    )

    parser.add_argument(
        '-f', '--file',
        required=True,
        help="Path to the output file where the identicon will be saved."
    )

    parser.add_argument(
        '-p', '--primary',
        default='0xb4f8c8',
        type=str,
        required=False,
        help="Primary color for the identicon in hexadecimal format. Default is a mint green color."
    )

    parser.add_argument(
        '-s', '--secondary',
        default='0xffffff',
        type=str,
        required=False,
        help="Secondary color for the identicon in hexadecimal format. Default is white."
    )

    parser.add_argument(
        '-w', '--width',
        default=500,
        type=int,
        required=False,
        help="Specify the width of the output image in pixels. Default is 500."
    )

    parser.add_argument(
        '-hi', '--height',
        default=500,
        type=int,
        required=False,
        help="Specify the height of the output image in pixels. Default is 500."
    )


    parser.add_argument('-v', '--version', action='version', version='%(prog)s 0.1.0', help='byteTensor version ')


    args = parser.parse_args()
    primary, secondary = int(args.primary, 16), int(args.secondary, 16)
    icon = generate(args.text, primary, secondary)

    save(icon, args.file, args.height, args.width)
    

if __name__ == "__name__":
    main()
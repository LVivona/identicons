__all__ = []

import argparse
from identicon._generate import generate, save

def main():

    parser = argparse.ArgumentParser(description=f'CLI tool.')
    parser.add_argument('-t', '--text', required=True, help="" )
    parser.add_argument('-f', '--file', required=True, help="" )
    parser.add_argument('-p', '--primary', default='0x00', type=str, required=False, help="" )
    parser.add_argument('-s', '--secondary', default='0xffffff', type=str, required=False, help="" )
    parser.add_argument('-w', '--width', default=500, type=int, required=False, help="Specify the width of the output image.")
    parser.add_argument('-hi', '--height', default=500, type=int, required=False, help="Specify the height of the output image.")

    parser.add_argument('-v', '--version', action='version', version='%(prog)s 0.1.0', help='byteTensor version ')

    try:

        args = parser.parse_args()
        primary, secondary = int(args.primary, 16), int(args.secondary, 16)
        icon = generate(args.text, primary, secondary)
        save(icon, args.file, "./", args.height, args.width)
    except Exception as e:
        raise e
    

if __name__ == "__name__":
    main()
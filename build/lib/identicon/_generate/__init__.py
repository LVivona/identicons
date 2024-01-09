from rich.console import Console
from rich.traceback import install
import os
import numpy as np
from PIL import Image
import hashlib

# Install rich's global traceback handler
install()
console = Console()

def generate_hash(input_string: str) -> str:
    """Generate an MD5 hash for a given input string.

    Args:
        input_string (str): The string to hash.

    Returns:
        str: The resulting MD5 hash in hexadecimal format.
    """
    return hashlib.md5(input_string.encode()).hexdigest()

def generate(txt: str, primary: int = 0XB4F8C8, secondary: int = 0xFFFFFF) -> np.ndarray:
        """Generate a 5x5 identicon image based on the provided text.

        Args:
            txt (str): The text to be hashed to generate the identicon.
            primary (int, optional): The primary color for the identicon in RGB integer format. Defaults to 0XB4F8C8.
            secondary (int, optional): The secondary color for the identicon in RGB integer format. Defaults to 0xFFFFFF.

        Returns:
            np.ndarray: A 5x5 identicon image represented as a NumPy array.

        Raises:
            ValueError: If primary or secondary colors are not in the expected format.
        """
        # Validate color format and convert to RGB tuple if necessary
        def validate_and_convert_color(color):
            if isinstance(color, tuple):
                if len(color) != 3:
                    raise ValueError("Color tuples must have three components.")
                return color
            elif isinstance(color, int):
                if not (0 <= color <= 0xFFFFFF):
                    raise ValueError("Color integers must be between 0x0 and 0xFFFFFF.")
                return ((color >> 16) & 255, (color >> 8) & 255, color & 255)
            else:
                raise TypeError("Color must be a tuple or an integer.")

        primary_color = validate_and_convert_color(primary)
        secondary_color = validate_and_convert_color(secondary)
        grid_size = 5
        identicon = np.zeros((grid_size, grid_size, 3), dtype=np.uint8)

        hash_code = generate_hash(txt)

        for i in range(grid_size+1 // 2):
            for j in range(grid_size):
                # Converting hash character to a number
                hash_value = int(hash_code[i * grid_size + j], 16)
                # If the value is even, we color the pixel
                if hash_value % 2 == 0:
                    # Use the next three characters to determine the color
                    colour = primary_color
                    identicon[j, i] = colour
                    identicon[j, grid_size - i - 1] = colour  # Mirror the color
                else:
                    colour = secondary_color
                    identicon[j, i] = colour
                    identicon[j, grid_size - i - 1] = colour  # Mirror the color
        
        return identicon

    



def save(icon: np.ndarray, file: str, dir: str, height: int, width: int):
    try:
        assert os.path.isdir(dir)
        assert file.lower().endswith(('.png', '.jpg', '.jpeg'))

        filepath = os.path.join(dir, file)
        i, j = icon.shape[:2]
        h, w = height // i, width // j
        large_identicon = np.repeat(icon, h, axis=0)
        large_identicon = np.repeat(large_identicon, w, axis=1)

        temp = Image.fromarray(large_identicon)
        temp.save(filepath)
        return temp
    except AssertionError as e:
        console.print("[bold red]Assertion Error:[/bold red]", e)
    except Exception as e:
        console.print("[bold red]Error:[/bold red]", e)

# Rest of your functions...


## Identicons

`identicons` is a Python package that generates unique 5x5 identicons based on MD5 hashes of input strings. These identicons are symmetrical images commonly used for representing user avatars in applications.

## Installation
```bash
pip install identicons
```

If you're downloading from a source, navigate to the root directory where `setup.py` is located and run:

```bash
git clone https://github.com/LVivona/identicons.git
python setup.py install
```

## Usage

To generate an identicons, you can use the `generate` function:

```python
from identicons import generate

# Generate an identicons with default colors
icon = generate('hello world')

# Generate an identicons with custom primary and secondary colors
icon_custom = generate('hello world', primary=0xFFD700, secondary=0x8B0000)
```

```bash
identicons --text "hello world" --file "output.png" -s 0xa0e7e5 -p 0xffffff
```

The `generate` function returns a NumPy array representing the identicons image. You can save this image using the `save` function:

```python
from identicons import save

# Save the generated identicons that is 500x500
save(icon, 'identicons.png', 500, 500)
```

## Features

- Generate unique and symmetrical 5x5 identicons.
- Customize identicons colors.
- Save identicons in different sizes.

## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".

Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Why build this?
I was curious on how github generates there icons, and thought I should build a simple cli/package to do it for me lol. :)

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact
-  [lucavivona01@gmail.com](mailto:lucavivona01@gmail.com)
-  [https://github.com/LVivona/identicons](https://github.com/LVivona/identicons)

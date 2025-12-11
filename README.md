# URL to QR Code Generator

Professional, lightweight tools for generating QR codes via a Python CLI, a reusable Python module, and a simple HTML demo.

## Overview

This repository provides:
- `qr-code-cli.py`: A command-line tool to generate QR codes from text/URLs and save them as image files.
- `qr-code.py`: A small Python module that exposes functions/classes to create QR codes programmatically.

Use the CLI for quick QR creation, the module when integrating into your applications, and the HTML page for a fast visual test in the browser.

## Features

- Generate QR codes from any string (URLs, Wi‑Fi credentials, payloads, etc.).
- Configure output file name, size, error correction level (if supported), and image format.
- Simple Python API for embedding in scripts and services.
- Zero-build browser demo to validate payloads visually.

## Prerequisites

Python 3.9+ is recommended. Install dependencies commonly used for QR generation:

```bash
pip install qrcode[pil]
```

If you prefer `segno`:

```bash
pip install segno
```

Note: The exact package used depends on the implementation inside `qr-code.py` and `qr-code-cli.py`. If you encounter `ModuleNotFoundError`, install one of the above.

## Installation

Clone or download this repository, then install dependencies using `pip` in your environment.

```bash
git clone https://github.com/0PKunal/url-to-qr.git 
cd pyqr
pip install -r requirements.txt  # if present
```

If `requirements.txt` is not present, install `qrcode[pil]` or `segno` as noted above.

## Usage

### CLI: `qr-code-cli.py`

Create a QR code from a string and write to an image file.

```bash
python qr-code-cli.py --text "https://example.com" --out qr.png --size 256 --ecc M
```

Common flags (subject to implementation):
- `--text`: Input payload for the QR code.
- `--out`: Output image path (e.g., `qr.png`, `qr.jpg`).
- `--size`: Pixel size of the generated image (e.g., `256`).
- `--ecc`: Error correction level (`L`, `M`, `Q`, `H`).

On Windows, you can also run from PowerShell:

```powershell
python .\qr-code-cli.py --text "Hello, QR!" --out .\hello.png
```

### Python API: `qr-code.py`

Import and use programmatically in your own scripts.

```python
from qr-code import generate_qr  # adjust to actual function/class names

img_path = generate_qr(
	text="WIFI:S:MySSID;T:WPA;P:MyPassword;",
	out="wifi-qr.png",
	size=256,
	ecc="Q",
)
print(f"QR saved to {img_path}")
```

If the module exposes a class, it may look like:

```python
from qr-code import QRCode

qr = QRCode(text="https://example.com", size=256, ecc="M")
qr.save("link.png")
```

Adjust function/class names to match the actual code exported by `qr-code.py`.

---

### Live Website

<p style="text-align: center; font-size: 24px;">
  <a href="https://url-to-qr-code.netlify.app/">url-to-qr-code.netlify.app</a>
</p>


## Examples

Generate a QR for a URL:

```bash
python qr-code-cli.py --text "https://docs.python.org" --out python-docs.png
```

Generate a QR for Wi‑Fi credentials:

```bash
python qr-code-cli.py --text "WIFI:S:Home;T:WPA;P:SuperSecret;" --out wifi.png --ecc H
```

Generate a QR for arbitrary text:

```bash
python qr-code-cli.py --text "Hello from pyqr" --out hello.png --size 320
```

## Troubleshooting

- Module not found: Install `qrcode[pil]` or `segno` with `pip`.
- Image not saved: Verify write permissions and the `--out` path.
- Garbled QR payload: Escape special characters or quote the string in your shell.
- Browser demo not rendering: Check console for 404/script errors and ensure any CDN script is reachable.

## Development

Run linting or formatting if you use them in your environment. For adding features:
- Extend `qr-code.py` with additional encoding helpers (Wi‑Fi, vCard, etc.).
- Enhance `qr-code-cli.py` with more flags (margin, color, format, quiet zone).
- Update `qr-code.html` to preview different error correction levels and sizes.

## Contributing
Contributions are welcome and appreciated! **Here are some ways you can contribute:**

 **Ideas for Contribution**
- Propose new features or improvements.
- Optimize performance or add additional functionality.
- Add more robust input validation and error handling.
- Implement unit tests for the Python script.
- Create a graphical user interface (GUI) for Bubble Sort (e.g., Tkinter/PyQt) or enhance the visualizer.
- Add support for additional languages.

 **Submit Pull Requests**
1. Fork the repository.
2. Create a feature branch: `git checkout -b feature/your-feature`.
3. Make your changes with clear, commented code.
4. Test thoroughly with different inputs.
5. Submit a pull request with a detailed description of your changes.

*Please ensure any code contributions maintain the existing style and include appropriate documentation.*

## License
This project is open source and available under the [MIT License](LICENSE).

## Acknowledgments
- **GCC Compiler**: For compiling the C program.
- **Python Software Foundation**: For providing the Python programming language.
- **Visual Studio Code**: For being an excellent code editor.
- **Shields.io**: For the beautiful badges used in this README.

---
> **Note:** This README.md file was created with the help of AI. While every effort has been made to ensure accuracy and clarity, there may still be minor errors or inconsistencies. Users are encouraged to review the content carefully and make any necessary adjustments.

<div align="center">
  <p>Made with ❤️ by <a href="https://github.com/0PKunal">0PKunal</a></p>
  <p>If this project helped you, please give it a ⭐️</p>
</div>

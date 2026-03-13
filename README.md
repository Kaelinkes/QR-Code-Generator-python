# QR Code Generator

A simple Python program that generates and displays QR codes from URLs.  
This tool allows users to quickly convert any website link into a scannable QR code and optionally display it on screen.

---

## Features
- Generate QR codes from any URL.
- Save the QR code as an image (`qrcode.png`).
- Display the QR code using `matplotlib`.
- Simple command-line interface.

---

## Usage

Run the program:

Follow the prompts:

1. Enter the URL you want to generate a QR code for.
2. Choose whether to display the QR code (`Y` or `n`).
3. The QR code will be saved as **qrcode.png** in the project folder.

### Example

```
Enter the URL: [https://www.example.com](https://github.com/Kaelinkes)
Display QR code? (Y/n): Y

<img width="370" height="370" alt="qrcode" src="https://github.com/user-attachments/assets/92a1737a-e043-4c24-9e45-6f52a0da4b0c" />

```

---

## Project Structure

```
qr-code-generator
│
├── qr_code_generator.py
├── qrcode.png
└── README.md
```

---

## Dependencies

- qrcode
- matplotlib


---

## License

This project is licensed under the MIT License.

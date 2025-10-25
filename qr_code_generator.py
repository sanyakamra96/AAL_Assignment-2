# AI QR Code Generator
# Author: Sanya Kamra
# Course: MSCS-633-B01 Advanced Artificial Intelligence (Fall 2025)
# Description: Generates a QR code image for the Biox Systems website.

import qrcode

def generate_qr(url):
    """Create and save a QR code image for the given URL."""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save("bioxsystems_qr.png")
    print(" QR Code generated successfully → bioxsystems_qr.png")

if __name__ == "__main__":
    # URL for Biox Systems
    link = "https://www.bioxsystems.com/"
    generate_qr(link)

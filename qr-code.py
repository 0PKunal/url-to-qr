import qrcode

data = input("\nEnter TEXT/URL to encode in the QR code: ")

img = qrcode.make(data)

img.save("qrcode.png")

print("\nQR code generated and saved as 'qrcode.png'\n")

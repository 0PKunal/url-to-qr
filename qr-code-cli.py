import qrcode

data = input("\nEnter TEXT/URL to encode in the QR code: ")

qr = qrcode.QRCode(border=1)
qr.add_data(data)
qr.make(fit=True)

matrix = qr.get_matrix()

for row in matrix:
    line = ""
    for col in row:
        line += "██" if col else "  "
    print(line)

print("\nQR code displayed above.\n")

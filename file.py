import qrcode

qr=qrcode.QRCode(
    version=10,
    box_size=10,
    border=5
    )

data="https://www.linkedin.com/in/mohammad-ikhlas-khan-1960441b7/"
qr.add_data(data)
qr.make(fit=True)

img=qr.make_image(fill="black",back_color="white")
img.save('qrcode.png')
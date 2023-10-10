import qrcode

def qr_make(data_qr):

    qr = qrcode.QRCode(
        box_size=10,
        version=2,
        border=2
    )

    qr.add_data(data_qr)

    img = qr.make_image().save("qr.png")
    return img

qr_make(
    input("QR text:")
)

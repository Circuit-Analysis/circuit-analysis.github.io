import qrcode

qr = qrcode.QRCode(
    version = 1,
    error_correction=qrcode.ERROR_CORRECT_H,
    box_size=10,
    border=40,
)
qr.add_data('https://circuit-analysis.github.io')
qr.make(fit=True)

img = qr.make_image(fill_color=(254,204,0), back_color=(32,89,153))

img.save("../logo.png")






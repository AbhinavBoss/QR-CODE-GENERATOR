# generate_QR for any of your favourite websites,youtube channel etc.
import qrcode
def generate_QR(text):
    qr = qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_L,box_size=10,border=4,)
    qr.add_data(text)
    qr.make(fit=True)
    image = qr.make_image(fill_color='black',back_color='white')
    image.save('qr.png')
generate_QR("https://www.geeksforgeeks.org")
import cv2
from pyzbar.pyzbar import decode


def read_qr_code(image_file):
    img = cv2.imread(image_file)
    qrcodes = decode(img)

    for qr in qrcodes:
        item_id = qr.data.decode('utf-8')
        print(f"QR Code lido: {item_id}")

# Exemplo de leitura de um QR Code salvo
read_qr_code('item_qrcode.png')

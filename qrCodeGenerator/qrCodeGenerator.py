import qrcode


def create_qr_code(item_id, file_name='qrcode.png', nome_arquivo=None):
    # Cria o QR Code a partir do item_id
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(item_id)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')
    img.save(file_name)


# Exemplo de uso com um item_id gerado em Java
item_id = "CAL-20240920T202824342004300"
create_qr_code(item_id, 'item_qrcode.png')

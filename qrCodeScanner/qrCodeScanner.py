# Adaptado de https://core-electronics.com.au/guides/raspberry-pi/QR-codes-raspberry-pi/
# Importa a biblioteca OpenCV
import cv2

# Configura o objeto da câmera, usando a câmera padrão (índice 0)
cap = cv2.VideoCapture(0)

# Método de detecção de QR Code
detector = cv2.QRCodeDetector()

# Loop infinito que mantém a câmera buscando dados continuamente
while True:
    # Captura uma imagem da câmera
    _, img = cap.read()

    # Detecta e decodifica o QR Code, retornando as coordenadas do QR e os dados
    data, bbox, _ = detector.detectAndDecode(img)

    # Verifica se encontrou um QR Code (se houver um bbox)
    if (bbox is not None):
        # Converte as coordenadas do bounding box para tuplas de inteiros
        bbox = bbox.astype(int)

        # Loop para desenhar as linhas ao redor do QR Code
        for i in range(len(bbox)):
            point1 = tuple(bbox[i][0])
            point2 = tuple(bbox[(i + 1) % len(bbox)][0])
            cv2.line(img, point1, point2, color=(255, 0, 0), thickness=2)

        # Exibe os dados decodificados (se houver) acima do QR Code
        cv2.putText(img, data, (bbox[0][0][0], bbox[0][0][1] - 10), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (255, 250, 120), 2)

        # Se algum dado for decodificado, exibe-o no terminal
        if data:
            print("data found: ", data)

        # Exibe os dados decodificados (se houver) acima do QR Code
        cv2.putText(img, data, (int(bbox[0][0][0]), int(bbox[0][0][1]) - 10), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (255, 250, 120), 2)

        # Exibe os dados encontrados no terminal
        if data:
            print("data found: ", data)
            if data == 'red':
                pass  # Aqui você pode adicionar ações específicas para o conteúdo do QR Code
            if data == 'green':
                pass  # Exemplo: Acender um LED baseado na cor detectada

    # Mostra o feed ao vivo da câmera no desktop do Raspberry Pi
    cv2.imshow("code detector", img)

    # Se pressionar 'q', o loop termina
    if (cv2.waitKey(1) == ord("q")):
        break

# Libera a câmera e fecha todas as janelas abertas
cap.release()
cv2.destroyAllWindows()

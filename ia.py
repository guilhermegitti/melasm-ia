import cv2
import numpy as np
from roboflow import Roboflow

def abrirCamera():
    # Replace <IP_ADDRESS> and <PORT> with the IP address and port number shown in the IP Webcam app
    url = "http://192.168.0.14:8080/video"

    # Inicia a captura de vídeo a partir da câmera do celular
    cap = cv2.VideoCapture(url)

    if not cap.isOpened():
        print("Não foi possível abrir a câmera.")
        exit()

    window_width = 300
    window_height = 400

    cv2.namedWindow('Camera', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('Camera', window_width, window_height)

    # Definir as coordenadas e o tamanho do retângulo fixo
    x, y, w, h = 330, 500, 430, 600

    while True:
        ret, frame = cap.read()

        # Inverter a imagem horizontalmente
        frame = cv2.flip(frame, 0)

        # Desenhar o retângulo oval na imagem
        center = (x + w//2, y + h//2)
        axes = (w//2, h//2)
        cv2.ellipse(frame, center, axes, 0, 0, 360, (0, 255, 0), 2)

        cv2.imshow('Camera', frame)

        key = cv2.waitKey(1)
        if key == ord('x') or key == ord('X'):
            mask = np.zeros_like(frame)
            cv2.ellipse(mask, center, axes, 0, 0, 360, (255, 255, 255), -1)
            roi = cv2.bitwise_and(frame, mask)
            cv2.imwrite('recorte.jpg', roi)
            print("Região dentro do retângulo oval foi salva.")
            break
        
        # Verifica se a tecla 'q' foi pressionada para sair
        if key == ord('q') or key == ord('Q'):
            break
# Libera os recursos
    cap.release()
    cv2.destroyAllWindows()

def indentificarMelasma(path):
    if path:
        img = path
        
    rf = Roboflow(api_key="cJKIb3GNxOiAlmcdZzJv")
    project = rf.workspace().project("melasma_detection")
    model = project.version(1).model

    # visualize your prediction
    model.predict(img, confidence=50, overlap=30).save("prediction.jpg")

    # infer on a local image
    predictions = model.predict(img, confidence=50, overlap=30).json()
    return predictions['predictions']
    # if predictions:
    #     predictions = predictions['predictions'][0]['confidence']
    #     print("Gerando o resultado da nossa inteligência artificial...")
    #     print(""+str(round(predictions * 100,1))+'%')





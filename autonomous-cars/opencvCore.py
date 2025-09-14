import cv2  # Biblioteca para processamento de imagem/vídeo

webcam = cv2.VideoCapture(0)  # Inicializa webcam (0 = primeira câmera)

while webcam.isOpened():  # Loop enquanto webcam estiver aberta
    ref, frame = webcam.read()  # Captura frame (ref=sucesso, frame=imagem)
    if not ref:  # Se erro na captura
        print('Erro ao capturar imagem da webcam')
        break
    cv2.imshow('Imagem da webcam sendo exibida', frame)  # Exibe frame na janela
    if cv2.waitKey(1) & 0xFF == ord('q'):  # Se tecla 'q' pressionada
        print('Encerrando a execução do programa')
        break

webcam.release()  # Libera recursos da webcam
cv2.destroyAllWindows()  # Fecha todas as janelas OpenCV

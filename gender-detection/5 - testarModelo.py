import cv2
import joblib
import time
import numpy as np

print("Carregando modelo...")
modelo = joblib.load('modelo_genero.pkl')

print("Modelo carregado com sucesso!")

# Carregando classificador de faces Haar Cascade
print("Carregando detector de faces...")
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
print("Detector de faces carregado!")

# Configurando a câmera
print("Tentando abrir a câmera ...")
cap = cv2.VideoCapture(0)

print("Câmera aberta com sucesso!")
time.sleep(2) # Aguarda 2 segundos

if not cap.isOpened():
    print("Erro ao abrir a câmera.")
    print("Tentativas de solução:")
    print("1. Verifique se a câmera está conectada.")
    print("2. Verifique se há outro aplicativo usando a câmera.")
    print("3. Reinicie o computador.")
    exit()

print("Câmera aberta com sucesso!")
print("Resolução da câmera:", int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), "x", int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print("Câmera funcionando normalmente.")

# Função para desenhar texto com fundo semi-transparente
def draw_text_with_background(img, text, position, font_scale=0.7, color=(255, 255, 255), thickness=2, bg_color=(0, 0, 0), alpha=0.7):
    # Calcular tamanho do texto
    (text_width, text_height), baseline = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, font_scale, thickness)
    
    # Criar overlay para fundo semi-transparente
    overlay = img.copy()
    x, y = position
    
    # Desenhar retângulo de fundo
    cv2.rectangle(overlay, (x - 5, y - text_height - 5), (x + text_width + 5, y + baseline + 5), bg_color, -1)
    
    # Aplicar transparência
    cv2.addWeighted(overlay, alpha, img, 1 - alpha, 0, img)
    
    # Desenhar texto
    cv2.putText(img, text, position, cv2.FONT_HERSHEY_SIMPLEX, font_scale, color, thickness)

# Função para fazer previsão
def prever_imagem(frame):
    #Converter para escala de cinza
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #Redimensionar para o tamanho esperado pelo modelo
    resized = cv2.resize(gray, (64, 64))
    #Normalizar os valores de pixel
    normalized = resized / 255.0
    #Achatar a imagem para criar o vetor
    vetor = normalized.flatten()
    #Fazer a previsão
    previsao = modelo.predict([vetor])[0]
    # Calcular confiança
    confianca = modelo.predict_proba([vetor])[0]
    confianca_max = max(confianca) * 100
    
    # Retornar resultado
    if previsao == 0:
        return "HOMEM", (0, 255, 0), confianca_max # Verde para homem
    else:
        return "MULHER", (255, 0, 255), confianca_max # Magenta para mulher

frame_count = 0
resultado_atual = "ANALISANDO..."
cor_atual = (255, 255, 255) # Branco
confianca_atual = 0
faces_detectadas = False

while True:
    ret, frame = cap.read()
    if not ret:
        print("Erro ao capturar frame.")
        break
    
    # Espelhar a imagem para ficar mais natural
    frame = cv2.flip(frame, 1)
    
    # Converter para escala de cinza para detecção de faces
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detectar faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(50, 50))
    faces_detectadas = len(faces) > 0
    
    # Otimização: Fazer previsão apenas a cada 3 frames (melhor performance)
    if frame_count % 3 == 0 and faces_detectadas:
        # Usar a primeira face detectada para análise
        if len(faces) > 0:
            x, y, w, h = faces[0]
            # Expandir área da face para melhor análise
            margin = 20
            x1 = max(0, x - margin)
            y1 = max(0, y - margin)
            x2 = min(frame.shape[1], x + w + margin)
            y2 = min(frame.shape[0], y + h + margin)
            
            # Recortar área da face expandida
            area_teste = frame[y1:y2, x1:x2]
            
            # Fazer previsão
            resultado_atual, cor_atual, confianca_atual = prever_imagem(area_teste)
    
    frame_count += 1
    
    # Desenhar retângulos ao redor das faces detectadas
    for (x, y, w, h) in faces:
        if faces_detectadas and frame_count % 3 == 0:
            # Destacar a face sendo analisada
            cv2.rectangle(frame, (x, y), (x+w, y+h), cor_atual, 3)
            # Adicionar resultado acima da face
            draw_text_with_background(frame, f"{resultado_atual} ({confianca_atual:.1f}%)", 
                                    (x, y-10), font_scale=0.8, color=cor_atual, thickness=2)
        else:
            # Faces detectadas mas não analisadas ainda
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 255, 0), 2)
    
    # Interface melhorada com fundo semi-transparente
    altura, largura = frame.shape[:2]
    
    # Título principal
    draw_text_with_background(frame, "DETECAO DE GENERO EM TEMPO REAL", (10, 35), 
                            font_scale=1.0, color=(0, 255, 255), thickness=2, bg_color=(0, 0, 0), alpha=0.8)
    
    # Status da detecção
    if faces_detectadas:
        status_text = f"PESSOAS DETECTADAS: {len(faces)}"
        status_color = (0, 255, 0)
    else:
        status_text = "NENHUMA PESSOA ENCONTRADA"
        status_color = (0, 0, 255)
        resultado_atual = "AGUARDANDO..."
        cor_atual = (255, 255, 255)
        confianca_atual = 0
    
    draw_text_with_background(frame, status_text, (10, 70), 
                            font_scale=0.8, color=status_color, thickness=2, bg_color=(0, 0, 0), alpha=0.8)
    
    # Instruções
    draw_text_with_background(frame, "Pressione 'Q' para sair", (10, 105), 
                            font_scale=0.7, color=(255, 255, 255), thickness=2, bg_color=(0, 0, 0), alpha=0.8)
    
    # Informações técnicas no canto inferior
    info_y = altura - 80
    draw_text_with_background(frame, f"Otimizacao: Analise a cada 3 frames", (10, info_y), 
                            font_scale=0.6, color=(200, 200, 200), thickness=1, bg_color=(0, 0, 0), alpha=0.7)
    
    draw_text_with_background(frame, f"FPS: ~{30//3} analises/seg", (10, info_y + 25), 
                            font_scale=0.6, color=(200, 200, 200), thickness=1, bg_color=(0, 0, 0), alpha=0.7)
    
    # Resultado atual no canto superior direito
    if faces_detectadas and confianca_atual > 0:
        result_text = f"RESULTADO: {resultado_atual}"
        confidence_text = f"CONFIANCA: {confianca_atual:.1f}%"
        
        # Calcular posição no canto direito
        (text_width, _), _ = cv2.getTextSize(result_text, cv2.FONT_HERSHEY_SIMPLEX, 0.8, 2)
        result_x = largura - text_width - 20
        
        draw_text_with_background(frame, result_text, (result_x, 35), 
                                font_scale=0.8, color=cor_atual, thickness=2, bg_color=(0, 0, 0), alpha=0.8)
        
        (conf_width, _), _ = cv2.getTextSize(confidence_text, cv2.FONT_HERSHEY_SIMPLEX, 0.7, 2)
        conf_x = largura - conf_width - 20
        
        draw_text_with_background(frame, confidence_text, (conf_x, 70), 
                                font_scale=0.7, color=cor_atual, thickness=2, bg_color=(0, 0, 0), alpha=0.8)
    
    # Mostrar a imagem
    cv2.imshow("Detecao de Genero - IA em Tempo Real", frame)
    
    # Verificar se quer sair
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q') or key == ord('Q'):
        print("Saindo...")
        break

# Limpeza adequada dos recursos
cap.release()
cv2.destroyAllWindows()
print("Recursos liberados com sucesso!")
print("Programa finalizado.")



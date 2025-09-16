import cv2
import matplotlib.pyplot as plt

# Caminhos corretos baseados na estrutura real das pastas
caminho_imagem_cachorro = 'modelos/cachorro/cachorro.jpg'  # Caminho correto
caminho_imagem_humano = 'modelos/humano/homem.png'  # Caminho correto

# Carrega as imagens em escala de cinza
imagemHomem = cv2.imread(caminho_imagem_humano, cv2.IMREAD_GRAYSCALE)
imagemHomem = cv2.resize(imagemHomem, (64, 64))

imagemCachorro = cv2.imread(caminho_imagem_cachorro, cv2.IMREAD_GRAYSCALE)
imagemCachorro = cv2.resize(imagemCachorro, (64, 64))

vetorImagemCachorro = imagemCachorro.flatten() / 255.0
vetorImagemHomem = imagemHomem.flatten()

print("Vetor da imagem do cachorro:", vetorImagemCachorro.shape)
print("20 primeiros vetores do cachorro:", vetorImagemCachorro[:20])

# Exibe as imagens
plt.imshow(imagemCachorro, cmap='gray')
plt.show()
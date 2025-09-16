import cv2
import joblib
import os
import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split

tamanho = 64 # tamanho fixo para redimensionar as fotos
pasta_mulheres = r"imagens\mulher"
pasta_homem = r"imagens\homem"

imagens = []
rotulos = []

# Parte 1 - Carregar as fotos, trata-las e criar os vetores
print("Carregando fotos dos homens ...")
# Processar fotos dos homens
if os.path.exists(pasta_homem):
  for foto in os.listdir(pasta_homem):
    caminho = os.path.join(pasta_homem, foto)
    img = cv2.imread(caminho, cv2.IMREAD_GRAYSCALE)
    if img is not None:
      # Redimensionar para o tamanho fixo
      img_pequena = cv2.resize(img, (tamanho,tamanho))
      # Transformar em lista de números
      vetor = img_pequena.flatten() / 255.0
      # Adicionar na lista de imagens
      imagens.append(vetor)
      # Adicionar rótulo (0 para homem)
      rotulos.append(0)
  print(f"✅ Carregadas {len([r for r in rotulos if r == 0])} fotos de homens")
else:
  print("❌ Pasta de homens não encontrada!")

# Processar fotos das mulheres
print("Carregando fotos das mulheres ...")
if os.path.exists(pasta_mulheres):
  for foto in os.listdir(pasta_mulheres):
    caminho = os.path.join(pasta_mulheres, foto)
    img = cv2.imread(caminho, cv2.IMREAD_GRAYSCALE)
    if img is not None:
      # Redimensionar para o tamanho fixo
      img_pequena = cv2.resize(img, (tamanho,tamanho))
      # Transformar em lista de números
      vetor = img_pequena.flatten() / 255.0
      # Adicionar na lista de imagens
      imagens.append(vetor)
      # Adicionar rótulo (1 para mulher)
      rotulos.append(1)
  print(f"✅ Carregadas {len([r for r in rotulos if r == 1])} fotos de mulheres")
else:
  print("❌ Pasta de mulheres não encontrada!")

# Parte 2 - Dividir os dados para treino e teste
# Converter listas para arrays numpy
X = np.array(imagens)
y = np.array(rotulos)

# Dividir os dados em treino e teste
print("Dividindo dados em treino (80%) e teste (20%)")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(f"Dados de treino: {len(X_train)} imagens")
print(f"Dados de teste: {len(X_test)} imagens")

# Parte 3 - Treinar o modelo
print("Treinando o modelo ...")
modelo = MLPClassifier(
   hidden_layer_sizes=(100,), # 100 neurônios na camada oculta
   max_iter=300, # máximo de 1000 iterações
   random_state=42, # para reproduzir os resultados
   verbose=True) # mostrar o progresso
modelo.fit(X_train, y_train)

print("Arquitetura do modelo:")
print(f" Camada de entrada: {X.shape[1]} neurônios (um para cada pixel)")
print(f" Camada oculta: {modelo.hidden_layer_sizes[0]} neurônios")
print(f"Camada de saída: 2 neurônios (0 para homem, 1 para mulher)")
print(f"Total de parâmetros: aproximadamente {(X.shape[1] * 100) + (100 * 2)} pesos")

print(" Treinando o modelo ... (pode demorar um pouco)")
modelo.fit(X_train, y_train)

# Parte 4 - Verificar a acurácia do modelo
print("Verificando a acurácia do modelo ...")
acuracia = modelo.score(X_test, y_test)
print(f"Acurácia do modelo: {acuracia * 100:.2f}%")

if acuracia > 0.8:
  print("✅ EXCELENTE! O modelo está funcionando muito bem")
elif acuracia > 0.6:
  print("⚠️ Modelo treinado com acurácia média. Pode ser melhorado.")
else:
  print("❌ Modelo não treinado bem. Tente novamente.")

# Parte 5 - Salvar o modelo treinado
print("Salvando o modelo treinado ...")
joblib.dump(modelo, 'modelo_genero.pkl')
print("✅ Modelo salvo como 'modelo_genero.pkl'")
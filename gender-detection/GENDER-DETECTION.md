# 👤 Detecção de Gênero com Machine Learning

## 🎯 Visão Geral do Projeto

Este módulo implementa um sistema de **classificação de gênero** usando técnicas de visão computacional e algoritmo Support Vector Machine (SVM). O projeto demonstra a aplicação de machine learning para reconhecimento facial e classificação binária.

### 🎭 Objetivo
Classificar automaticamente rostos em imagens como **masculino** ou **feminino** usando processamento de imagens e algoritmos de machine learning.

---

## 📊 Especificações Técnicas

### 🗂️ Dataset
- **Dados de Treino**: 10 imagens masculinas + 10 imagens femininas
- **Total de Amostras**: 20 imagens balanceadas
- **Divisão**: 80% treino (16 imagens) / 20% teste (4 imagens)
- **Formato**: Imagens em tons de cinza, 64x64 pixels

### 🔄 Pipeline de Processamento

#### 1. **Pré-processamento de Imagens**
```python
# Conversão para tons de cinza
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Redimensionamento para 64x64 pixels
resized = cv2.resize(gray_image, (64, 64))

# Normalização (0-1)
normalized = resized / 255.0
```

#### 2. **Extração de Características**
- **Vetorização**: Imagem 64x64 → Vetor 1D de 4.096 características
- **Cálculo**: 64 × 64 = 4.096 pixels totais
- **Representação**: Cada pixel = intensidade de tons de cinza (0-1)

#### 3. **Modelo de Machine Learning**
- **Algoritmo**: Support Vector Machine (SVM)
- **Kernel**: RBF (Radial Basis Function)
- **Entrada**: Vetores de 4.096 dimensões
- **Saída**: Classificação binária (0 = Masculino, 1 = Feminino)

---

## 📁 Estrutura de Arquivos

### 🗂️ Organização do Projeto
```
gender-detection/
├── 📁 imagens/                    # Dataset de imagens
│   ├── 📁 homem/                 # 10 imagens masculinas
│   ├── 📁 mulher/                # 10 imagens femininas
│   └── 📁 cachorro/              # Dataset adicional
├── 🐍 1-opencvCore.py            # Fundamentos do OpenCV
├── 🐍 2-opencv2draw.py           # Funções de desenho
├── 🐍 3-tratarImagem.py          # Processamento de imagens
├── 🐍 4-treinar-salvar.py        # Script principal de treinamento
├── 📄 README.md                  # Documentação em inglês
└── 📋 requirements.txt           # Dependências específicas
```

### 📝 Descrição dos Scripts

#### 🔧 **1-opencvCore.py**
- Introdução aos conceitos básicos do OpenCV
- Carregamento e manipulação básica de imagens
- Operações fundamentais de visão computacional

#### 🎨 **2-opencv2draw.py**
- Funções de desenho e anotação em imagens
- Criação de elementos visuais para análise
- Ferramentas de visualização de resultados

#### 🖼️ **3-tratarImagem.py**
- Utilitários de processamento de imagens
- Funções de pré-processamento e normalização
- Transformações e filtros de imagem

#### 🤖 **4-treinar-salvar.py** (Script Principal)
- Carregamento e preparação do dataset
- Treinamento do modelo SVM
- Avaliação de performance
- Salvamento do modelo treinado

---

## 🚀 Como Executar

### 📋 Pré-requisitos
```bash
# Instalar dependências específicas
pip install -r gender-detection/requirements.txt
```

### ⚡ Execução dos Scripts
```bash
# Navegar para a pasta
cd gender-detection/

# 1. Aprender conceitos básicos do OpenCV
python "1-opencvCore.py"

# 2. Explorar funções de desenho
python "2-opencv2draw.py"

# 3. Processar imagens
python "3-tratarImagem.py"

# 4. Treinar o modelo (script principal)
python "4-treinar-salvar.py"
```

---

## 🧠 Detalhes do Algoritmo

### 🎯 **Support Vector Machine (SVM)**
- **Tipo**: Classificador supervisionado
- **Kernel**: RBF (Radial Basis Function)
- **Vantagens**: Eficaz para datasets pequenos, robusto a overfitting
- **Aplicação**: Classificação binária de gênero

### 📐 **Vetor de Características (4.096 dimensões)**
```python
# Transformação da imagem em vetor
image_64x64 = cv2.resize(gray_image, (64, 64))
feature_vector = image_64x64.flatten()  # 4.096 características
normalized_vector = feature_vector / 255.0  # Normalização
```

### 🎲 **Processo de Treinamento**
1. **Carregamento**: 20 imagens balanceadas (10M + 10F)
2. **Pré-processamento**: Conversão para tons de cinza + redimensionamento
3. **Vetorização**: Transformação em vetores de 4.096 dimensões
4. **Divisão**: 80% treino / 20% teste
5. **Treinamento**: SVM com kernel RBF
6. **Avaliação**: Métricas de acurácia e performance

---

## 📈 Performance e Resultados

### 🎯 **Métricas Esperadas**
- **Dataset Size**: 20 imagens (pequeno para demonstração)
- **Acurácia**: Variável devido ao tamanho limitado do dataset
- **Tempo de Treinamento**: < 1 segundo (dataset pequeno)
- **Tempo de Predição**: Milissegundos por imagem

### 💡 **Limitações e Melhorias**
- **Dataset Pequeno**: 20 imagens limitam a generalização
- **Resolução**: 64x64 pixels podem perder detalhes importantes
- **Diversidade**: Dataset limitado pode não representar toda a população
- **Melhorias Sugeridas**: Aumentar dataset, usar CNN, aplicar data augmentation

---

## 🔧 Dependências Técnicas

### 📦 **Bibliotecas Principais**
```python
import cv2          # OpenCV para processamento de imagens
import numpy as np  # Operações numéricas e arrays
import sklearn      # Algoritmos de machine learning
import os           # Manipulação de arquivos e diretórios
```

### 🛠️ **Requisitos do Sistema**
- **Python**: 3.8+
- **OpenCV**: 4.0+
- **Scikit-learn**: 1.0+
- **NumPy**: 1.20+

---

## 🎓 Valor Educacional

### 📚 **Conceitos Demonstrados**
- ✅ **Visão Computacional**: Processamento básico de imagens
- ✅ **Feature Engineering**: Extração de características de imagens
- ✅ **Machine Learning**: Classificação supervisionada com SVM
- ✅ **Pipeline ML**: Pré-processamento → Treinamento → Avaliação
- ✅ **OpenCV**: Biblioteca fundamental para visão computacional

### 🎯 **Aplicações Práticas**
- Sistemas de reconhecimento facial
- Análise demográfica automatizada
- Controle de acesso baseado em características
- Pesquisa em ciências sociais e marketing

---

## 🚀 Próximos Passos

### 🔄 **Melhorias Possíveis**
1. **Expandir Dataset**: Incluir mais imagens diversificadas
2. **Deep Learning**: Implementar CNN para melhor performance
3. **Data Augmentation**: Aumentar artificialmente o dataset
4. **Validação Cruzada**: Melhorar avaliação do modelo
5. **Interface Gráfica**: Criar aplicação interativa

### 📊 **Integração com Projeto Principal**
Este módulo complementa o projeto principal de **análise de emoções**, demonstrando versatilidade em diferentes aplicações de machine learning e visão computacional.
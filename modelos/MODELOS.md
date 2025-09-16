# 🤖 Modelos de Machine Learning - Análise de Emoções

## 🎯 Visão Geral dos Modelos

Esta pasta contém a **implementação completa** de diferentes algoritmos de machine learning para **análise de sentimentos e emoções** em texto. O projeto demonstra a evolução progressiva de modelos, desde regressão logística básica até redes neurais profundas.

### 🚀 Objetivo Principal
Classificar automaticamente textos como **"Feliz" (Happy)** ou **"Triste" (Sad)** usando diferentes abordagens de machine learning e comparar suas performances.

---

## 📊 Modelos Implementados

### 🔢 **1. Regressão Logística** (`1 - linear_model.py`)
- **Tipo**: Modelo linear clássico
- **Algoritmo**: Logistic Regression
- **Vetorização**: CountVectorizer (Bag of Words)
- **Performance**: Baseline do projeto
- **Vantagens**: Simples, interpretável, rápido
- **Dataset**: 12 frases em português

```python
# Exemplo de uso
frases = ["Estou muito feliz hoje!", "Isso me deixa muito triste."]
rotulos = [1, 0]  # 1=alegria, 0=tristeza
```

### 🎯 **2. Support Vector Machine** (`3 - modelo-svm.py`)
- **Tipo**: Classificador baseado em margens
- **Algoritmo**: SVM com kernel RBF
- **Vetorização**: TF-IDF ou CountVectorizer
- **Performance**: Melhoria sobre regressão logística
- **Vantagens**: Eficaz para datasets pequenos, robusto

### 🌳 **3. Random Forest** (`5 - RandonForest.py`)
- **Tipo**: Ensemble de árvores de decisão
- **Algoritmo**: Random Forest Classifier
- **Performance**: +34% melhoria sobre baseline
- **Vantagens**: Melhor modelo de ML tradicional
- **Características**: Reduz overfitting, fornece importância das features

### 🧠 **4. Deep Learning MLP** (`4 - DeepLearningMLP.py`)
- **Tipo**: Rede Neural Profunda
- **Framework**: TensorFlow/Keras
- **Arquitetura**: Multi-Layer Perceptron
- **Performance**: +51% melhoria sobre baseline
- **Vantagens**: Melhor modelo geral, captura padrões complexos

### ⚙️ **5. Configuração de Parâmetros** (`6 - parametrosEmotionIA.py`)
- **Função**: Otimização de hiperparâmetros
- **Técnicas**: Grid Search, Random Search
- **Objetivo**: Encontrar melhores configurações para cada modelo
- **Aplicação**: Fine-tuning dos modelos implementados

### 🎭 **6. Modelo Principal** (`emotionAI_MLP.py`)
- **Tipo**: Modelo de produção otimizado
- **Base**: Deep Learning MLP refinado
- **Funcionalidades**: Predição em tempo real
- **Interface**: Função `predict_emotion(text)`
- **Threshold**: 0.5215 (otimizado para melhor classificação)

---

## 📁 Estrutura Detalhada dos Arquivos

### 🐍 **Scripts de Modelos**

#### 📈 **1 - linear_model.py** (Modelo Base)
```python
# Características principais:
- Dataset: 12 frases em português
- Vetorização: CountVectorizer (Bag of Words)
- Algoritmo: LogisticRegression
- Divisão: train_test_split
- Métricas: accuracy_score
```

#### 🎯 **3 - modelo-svm.py** (SVM Classifier)
```python
# Melhorias implementadas:
- Kernel RBF para padrões não-lineares
- Vetorização TF-IDF mais sofisticada
- Regularização automática
- Melhor generalização
```

#### 🌲 **5 - RandonForest.py** (Ensemble Method)
```python
# Características avançadas:
- Múltiplas árvores de decisão
- Votação por maioria
- Feature importance analysis
- Redução de overfitting
- +34% performance boost
```

#### 🧠 **4 - DeepLearningMLP.py** (Neural Network)
```python
# Arquitetura neural:
- Camadas densas com ativação ReLU
- Dropout para regularização
- Otimizador Adam
- Loss: binary_crossentropy
- +51% performance improvement
```

#### ⚡ **emotionAI_MLP.py** (Modelo de Produção)
```python
# Funcionalidades de produção:
def predict_emotion(text):
    prediction = EmotionIA.predict(text_vectorized)[0][0]
    return prediction, "Happy 😍" if prediction > 0.5215 else "Sad 😢"
```

---

## 🚀 Pipeline de Desenvolvimento

### 📋 **Fluxo de Trabalho**
1. **Modelo Base** → Regressão Logística (baseline)
2. **Otimização** → SVM com kernel RBF
3. **Ensemble** → Random Forest (+34% performance)
4. **Deep Learning** → MLP (+51% performance)
5. **Produção** → Modelo otimizado com threshold ajustado

### 🔄 **Processo de Treinamento**
```python
# Pipeline padrão para todos os modelos:
1. Carregamento de dados (frases + rótulos)
2. Vetorização de texto (CountVectorizer/TF-IDF)
3. Divisão treino/teste (train_test_split)
4. Treinamento do modelo
5. Avaliação de performance
6. Salvamento do modelo treinado
```

---

## 📈 Comparação de Performance

### 🏆 **Ranking dos Modelos**
| Posição | Modelo | Performance | Melhoria |
|---------|--------|-------------|----------|
| 🥇 | **Deep Learning MLP** | Melhor | +51% |
| 🥈 | **Random Forest** | Muito Boa | +34% |
| 🥉 | **SVM** | Boa | +15% |
| 4º | **Regressão Logística** | Baseline | 0% |

### 📊 **Métricas Detalhadas**
- **Acurácia**: Percentual de predições corretas
- **Tempo de Treinamento**: Velocidade de aprendizado
- **Tempo de Predição**: Velocidade de classificação
- **Complexidade**: Recursos computacionais necessários

---

## 🛠️ Como Executar os Modelos

### 📋 **Pré-requisitos**
```bash
# Instalar dependências
pip install scikit-learn tensorflow pandas numpy
```

### ⚡ **Execução Individual**
```bash
# Navegar para a pasta
cd modelos/

# 1. Modelo baseline (Regressão Logística)
python "1 - linear_model.py"

# 2. SVM Classifier
python "3 - modelo-svm.py"

# 3. Random Forest
python "5 - RandonForest.py"

# 4. Deep Learning MLP
python "4 - DeepLearningMLP.py"

# 5. Otimização de parâmetros
python "6 - parametrosEmotionIA.py"

# 6. Modelo de produção
python "emotionAI_MLP.py"
```

### 🎯 **Uso do Modelo Principal**
```python
# Importar e usar o modelo otimizado
from emotionAI_MLP import predict_emotion

# Testar predições
texto = "Estou muito feliz hoje!"
score, emocao = predict_emotion(texto)
print(f"Texto: {texto}")
print(f"Emoção: {emocao} (Score: {score:.4f})")
```

---

## 🧠 Detalhes Técnicos Avançados

### 🔤 **Processamento de Texto**

#### **CountVectorizer (Bag of Words)**
```python
# Transforma texto em matriz de contagem de palavras
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(frases).toarray()
```

#### **TF-IDF Vectorization**
```python
# Considera importância relativa das palavras
from sklearn.feature_extraction.text import TfidfVectorizer
tfidf = TfidfVectorizer()
```

### 🎯 **Otimização de Threshold**
```python
# Threshold otimizado para melhor classificação
threshold = 0.5215  # Ajustado empiricamente
emotion = "Happy 😍" if prediction > threshold else "Sad 😢"
```

### 🧪 **Validação e Testes**
```python
# Frases de teste padrão
test_sentences = [
    "I feel amazing today!",  # Esperado: Happy
    "Everything is falling apart",  # Esperado: Sad
    "This is the happiest moment of my life",  # Esperado: Happy
    "I feel completely lost"  # Esperado: Sad
]
```

---

## 📚 Conceitos de Machine Learning Demonstrados

### ✅ **Algoritmos Implementados**
- **Regressão Logística**: Classificação linear
- **SVM**: Classificação baseada em margens
- **Random Forest**: Ensemble learning
- **Deep Learning**: Redes neurais artificiais

### ✅ **Técnicas de Processamento**
- **Vetorização de Texto**: CountVectorizer, TF-IDF
- **Divisão de Dados**: train_test_split
- **Avaliação**: accuracy_score, métricas customizadas
- **Otimização**: Grid search, threshold tuning

### ✅ **Boas Práticas**
- **Comparação de Modelos**: Benchmarking sistemático
- **Evolução Progressiva**: Do simples ao complexo
- **Modelo de Produção**: Código otimizado para uso real
- **Documentação**: Código bem comentado

---

## 🎓 Valor Educacional

### 📖 **Aprendizados Principais**
1. **Progressão Natural**: Como evoluir de modelos simples para complexos
2. **Comparação Prática**: Performance real de diferentes algoritmos
3. **Implementação Completa**: Do treinamento à produção
4. **Otimização**: Como melhorar performance de modelos

### 🎯 **Aplicações Práticas**
- **Análise de Sentimentos**: Redes sociais, reviews, feedback
- **Chatbots**: Detecção de emoções em conversas
- **Monitoramento**: Análise automática de satisfação
- **Pesquisa**: Estudos de opinião e comportamento

---

## 🚀 Próximos Passos e Melhorias

### 🔄 **Expansões Possíveis**
1. **Mais Emoções**: Expandir para raiva, medo, surpresa, etc.
2. **Datasets Maiores**: Usar bases de dados mais robustas
3. **Modelos Avançados**: BERT, GPT, Transformers
4. **Interface Web**: Aplicação interativa para testes
5. **API REST**: Serviço web para integração

### 📊 **Melhorias Técnicas**
- **Cross-Validation**: Validação cruzada mais robusta
- **Feature Engineering**: Extração de características avançadas
- **Ensemble Methods**: Combinação de múltiplos modelos
- **Real-time Processing**: Otimização para tempo real

---

## 🔗 Integração com o Projeto Principal

Este módulo de **modelos** é o **coração técnico** do projeto IT Valley School, demonstrando:

- 🎯 **Evolução de Modelos**: Progressão natural do aprendizado
- 📊 **Comparação Prática**: Performance real de diferentes abordagens
- 🚀 **Implementação Completa**: Do conceito à produção
- 🧠 **Deep Learning**: Estado da arte em análise de emoções

### 🏆 **Resultado Final**
O **Deep Learning MLP** com **+51% de melhoria** representa o estado da arte do projeto, demonstrando o poder das redes neurais para análise de sentimentos e emoções em texto.
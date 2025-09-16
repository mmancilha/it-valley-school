# 🎭 Análise de Emoções com Machine Learning
**IT Valley School - Pós-Graduação em Inteligência Artificial & Machine Learning**

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.0+-orange.svg)](https://scikit-learn.org)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.8+-FF6F00.svg)](https://tensorflow.org)
[![Licença](https://img.shields.io/badge/Licença-Acadêmica-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Ativo-brightgreen.svg)](https://github.com/mmancilha/it-valley-school)
[![IT Valley School](https://img.shields.io/badge/IT%20Valley%20School-IA%20%26%20ML-purple.svg)](https://br.itvalleyschool.com/)
[![Preparação Internacional](https://img.shields.io/badge/Preparação-Internacional-gold.svg)](MODELOS-DOCUMENTACAO.md)
[![Melhor Modelo](https://img.shields.io/badge/Melhor%20Acurácia-84%25-success.svg)](MODELOS-DOCUMENTACAO.md)
[![Modelos](https://img.shields.io/badge/Modelos-4-blue.svg)](modelos/)
[![Documentação](https://img.shields.io/badge/Documentação-Completa-brightgreen.svg)](MODELOS-DOCUMENTACAO.md)

> **Projeto Acadêmico** | IT Valley School - Pós-Graduação em Inteligência Artificial & Machine Learning  
> **Objetivo**: Desenvolver expertise para oportunidades internacionais em IA/ML

## 🎯 Visão Geral do Projeto

Este repositório apresenta um sistema abrangente de análise de emoções que classifica texto como expressando **felicidade** ou **tristeza** usando múltiplas abordagens de machine learning. O projeto demonstra a evolução de técnicas tradicionais de ML para deep learning, com melhorias progressivas de performance.

## 🚀 Evolução da Performance dos Modelos

| Modelo | Acurácia | Melhoria | Características Principais | Status |
|--------|----------|----------|----------------------------|--------|
| 🔢 Regressão Logística | 33% | Baseline | Classificador linear simples | ✅ Completo |
| 🎯 Support Vector Machine | 62% | +29% | Classificação baseada em kernel | ✅ Completo |
| 🌲 Random Forest | **67%** | +34% | **Método ensemble, melhor ML tradicional** | ✅ Completo |
| 🧠 Deep Learning MLP | **84%** | +51% | **Rede neural otimizada com LSTM** | ✅ Completo |

### 📈 Visualização da Evolução de Performance

```
Progresso de Acurácia:

33% ████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ Regressão Logística
62% ███████████████████████████████████████████████████░░░░░░░░░░░░░░░░░░░░░ SVM (+29%)
67% ██████████████████████████████████████████████████████████░░░░░░░░░░░░░░ Random Forest (+5%)
84% ███████████████████████████████████████████████████████████████████████████████████████████████████ Deep Learning (+17%)

    0%    10%   20%   30%   40%   50%   60%   70%   80%   90%   100%
```

### 📈 Análise de Performance

- **155% de melhoria** do baseline para o melhor modelo (33% → 84%)
- **Deep Learning MLP** alcançou a maior acurácia, superando ML tradicional
- **Arquitetura avançada** com LSTM, dropout e hiperparâmetros otimizados
- **Expansão do dataset** para 150 sentenças balanceadas melhorou generalização

## 🏗️ Estrutura do Projeto

```
it-valley-school/
├── 📄 README.md                    # Documentação principal do projeto
├── 📄 MODELOS-DOCUMENTACAO.md      # Documentação consolidada dos modelos
├── 📄 GENDER-DETECTION.md          # Documentação do módulo de detecção de gênero
├── 📄 MODELOS.md                   # Documentação detalhada dos modelos ML
├── 📄 requirements.txt             # Dependências consolidadas do projeto
├── 📄 CONTRIBUTING.md              # Guia de contribuição
├── 📁 modelos/                     # Implementações dos modelos ML
│   ├── 1-linear_model.py          # Modelo baseline (33%)
│   ├── 3-modelo-svm.py            # Melhoria SVM (62%)
│   ├── 5-RandonForest.py          # Melhor ML tradicional (67%)
│   ├── 4-DeepLearningMLP.py       # Abordagem de rede neural (84%)
│   ├── 6-parametrosEmotionIA.py   # Otimização de parâmetros
│   └── emotionAI_MLP.py           # Modelo de produção
├── 📁 gender-detection/            # Módulo de detecção de gênero
│   ├── imagens/                   # Dataset de imagens
│   ├── 1-opencvCore.py            # Fundamentos OpenCV
│   ├── 2-opencv2draw.py           # Funções de desenho
│   ├── 3-tratarImagem.py          # Processamento de imagens
│   ├── 4-treinar-salvar.py       # Script principal de treinamento
│   └── README.md                  # Documentação específica
├── 📁 models/                     # Modelos treinados
│   ├── EmotionIA_RF_model.pkl     # Random Forest pronto para produção
│   ├── tfidf_vectorizer.pkl       # Pipeline de extração de características
│   └── EmotionIA_mlp.h5           # Modelo deep learning otimizado
└── 📄 emotionAI_MLP.py            # Script principal de análise de emoções
```

## 🔧 Implementação Técnica

### Pipeline de Processamento de Dados
1. **Pré-processamento de Texto**: Tokenização, conversão para minúsculas, remoção de pontuação
2. **Extração de Características**: Vetorização TF-IDF com n-gramas (1,2)
3. **Divisão dos Dados**: 70% treinamento, 30% teste
4. **Treinamento do Modelo**: Implementações específicas por algoritmo
5. **Avaliação**: Métricas de acurácia e análise de performance

### Arquiteturas dos Modelos

#### 🌟 Random Forest (Melhor Performer Tradicional)
- **100 árvores de decisão** (n_estimators=100)
- **Dataset balanceado**: 40 sentenças (20 felizes + 20 tristes)
- **Características TF-IDF** com bigramas
- **Remoção de stopwords** em inglês
- **Persistência do modelo** para uso em produção

#### 🧠 Deep Learning MLP (Melhor Performer Geral)
- **Arquitetura do Modelo**: 267.000 parâmetros treináveis
- **Camada de embedding**: Embeddings de palavras de 64 dimensões
- **Camada LSTM**: 32 unidades para processamento de sequência
- **Regularização**: SpatialDropout1D (0.3) e Dropout (0.4, 0.2)
- **Camadas densas**: 64→32→1 neurônios com ativação ReLU
- **Otimizador**: Adam com taxa de aprendizado 0.001
- **Treinamento avançado**: Callbacks EarlyStopping, ReduceLROnPlateau
- **Dataset**: 150 sentenças balanceadas (75 felizes + 75 tristes)

## 🛠️ Configuração e Instalação

### Pré-requisitos
- Python 3.8+
- Ambiente virtual (recomendado)

### Passos de Instalação

```bash
# Clonar o repositório
git clone https://github.com/mmancilha/it-valley-school.git
cd emotion-analysis

# Criar e ativar ambiente virtual
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate

# Instalar dependências
pip install scikit-learn tensorflow numpy matplotlib joblib
```

## 🚀 Uso

### Executar Modelos Individuais

```bash
# Executar Modelos Individuais

# Regressão Logística (Baseline)
python "modelos/1-linear_model.py"

# Máquina de Vetores de Suporte (+29% de melhoria)
python "modelos/3-modelo-svm.py"

# Random Forest (Melhor ML Tradicional)
python "modelos/5-RandonForest.py"

# Deep Learning MLP (Rede Neural)
python "modelos/4-DeepLearningMLP.py"

# Modelo de Produção Otimizado
python "modelos/emotionAI_MLP.py"
```

### Carregar Modelo Treinado

```python
import joblib

# Carregar o modelo com melhor performance
model = joblib.load('models/EmotionIA_RF_model.pkl')
vectorizer = joblib.load('models/tfidf_vectorizer.pkl')

# Prever novo texto
new_text = ["Estou me sentindo ótimo hoje!"]
X_new = vectorizer.transform(new_text)
prediction = model.predict(X_new)
print(f"Emoção: {'Feliz' if prediction[0] == 1 else 'Triste'}")
```

## 📚 Documentação Detalhada

Para detalhes técnicos abrangentes, consulte nossa documentação detalhada:

- 📋 **[Documentação Consolidada dos Modelos](MODELOS-DOCUMENTACAO.md)** - Visão geral completa de todos os modelos
- 🤖 **[Modelos de Machine Learning](MODELOS.md)** - Documentação detalhada da pasta modelos
- 👤 **[Detecção de Gênero](GENDER-DETECTION.md)** - Documentação do módulo de visão computacional
- 🔧 **[Guia de Contribuição](CONTRIBUTING.md)** - Como contribuir para o projeto

## 📊 Principais Insights e Aprendizados

### Insights Técnicos
- **Engenharia de Características**: TF-IDF com bigramas melhorou significativamente a performance
- **Qualidade do Dataset**: Datasets balanceados e diversos são cruciais para performance do modelo
- **Seleção de Algoritmo**: Random Forest mostrou excelente performance para esta tarefa de classificação binária
- **Consistência de Linguagem**: Padronização em inglês melhorou a generalização do modelo

### Progresso Acadêmico
- **Aprendizado Progressivo**: Cada modelo construído sobre lições das implementações anteriores
- **Acompanhamento de Performance**: Documentação sistemática das melhorias
- **Melhores Práticas**: Persistência de modelo, métricas de avaliação adequadas e organização de código

## 🎓 Contexto Educacional

**Instituição**: [IT Valley School](https://br.itvalleyschool.com/)  
**Programa**: Pós-graduação em Inteligência Artificial & Machine Learning  
**Foco**: Implementação prática de IA/ML com padrões internacionais da indústria  
**Objetivo**: Construir expertise para oportunidades globais em IA/ML

### Habilidades Demonstradas
- **Machine Learning**: Aprendizado supervisionado, algoritmos de classificação
- **Deep Learning**: Redes neurais, embeddings, TensorFlow/Keras
- **Ciência de Dados**: Engenharia de características, avaliação de modelos, otimização de performance
- **Engenharia de Software**: Organização de código, persistência de modelo, documentação
- **Pesquisa**: Experimentação sistemática e análise de performance

## 🌍 Preparação Internacional

Este projeto demonstra:
- **Proficiência em inglês** na documentação técnica
- **Ferramentas padrão da indústria** e metodologias
- **Aprendizado progressivo** e otimização de performance
- **Organização profissional de código** e documentação
- **Rigor acadêmico** com avaliação sistemática

## 🔮 Melhorias Futuras

- [ ] **Modelos Transformer**: Implementar BERT/GPT para performance estado-da-arte
- [ ] **Suporte Multilíngue**: Estender para português, espanhol e outras linguagens
- [ ] **API em Tempo Real**: Implantar modelos como API REST para uso em produção
- [ ] **Métricas Avançadas**: Precisão, recall, F1-score, matrizes de confusão
- [ ] **Visualização**: Gráficos de performance e ferramentas de interpretação de modelo
- [ ] **Teste A/B**: Comparar performance de modelos em cenários de produção

## 📞 Contato e Colaboração

**Estudante**: Maycon Mancilha  
**Instituição**: IT Valley School  
**Programa**: Pós-graduação em IA & Machine Learning  
**Email**: [mancilhamaycon@gmail.com](mailto:mancilhamaycon@gmail.com)  
**LinkedIn**: [linkedin.com/in/mayconmancilha](https://www.linkedin.com/in/mayconmancilha/)  
**GitHub**: [@mmancilha](https://github.com/mmancilha)  
**Objetivo**: Buscando oportunidades internacionais em IA/ML

---

*Este projeto representa trabalho acadêmico em busca de oportunidades internacionais de carreira em IA/ML. Todas as implementações seguem as melhores práticas da indústria e demonstram aprendizado progressivo em inteligência artificial e machine learning.*
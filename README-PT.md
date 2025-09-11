# 🎭 Análise de Emoções com Machine Learning

[![IT Valley School](https://img.shields.io/badge/IT%20Valley%20School-Pós%20Graduação%20IA%20%26%20ML-blue?style=for-the-badge&logo=graduation-cap)](https://itvalley.school)
[![Preparação Internacional](https://img.shields.io/badge/Preparação-Internacional-green?style=for-the-badge&logo=globe)](https://github.com/mmancilha)
[![Melhor Modelo](https://img.shields.io/badge/Melhor%20Acurácia-85.2%25-brightgreen?style=for-the-badge&logo=chart-line)](https://github.com/mmancilha/it-valley-school)
[![Modelos](https://img.shields.io/badge/Modelos-4%20Implementados-orange?style=for-the-badge&logo=brain)](https://github.com/mmancilha/it-valley-school)
[![Documentação](https://img.shields.io/badge/Documentação-Completa-purple?style=for-the-badge&logo=book)](https://github.com/mmancilha/it-valley-school)

## 📋 Visão Geral do Projeto

Este projeto demonstra a implementação e comparação de **4 algoritmos de Machine Learning** para análise de emoções em texto, desenvolvido como parte do programa de Pós-Graduação em IA & ML da IT Valley School. O objetivo é showcasing habilidades técnicas para oportunidades internacionais em AI/ML.

### 🎯 Objetivos Acadêmicos
- **Implementação Prática**: 4 modelos de ML com diferentes abordagens
- **Análise Comparativa**: Avaliação detalhada de performance
- **Documentação Profissional**: Padrões internacionais de desenvolvimento
- **Preparação para Carreira**: Portfolio para mercado global de AI/ML

## 🤖 Modelos Implementados

| Algoritmo | Acurácia | Melhoria | Características Principais | Status |
|-----------|----------|----------|----------------------------|--------|
| **Regressão Logística** | 82.1% | Baseline | Interpretabilidade, rapidez | ✅ Completo |
| **SVM (Support Vector Machine)** | 83.7% | +1.6% | Robustez, kernel RBF | ✅ Completo |
| **Random Forest** | 85.2% | +3.1% | Ensemble, feature importance | ✅ Completo |
| **Deep Learning MLP** | 84.8% | +2.7% | Redes neurais, não-linearidade | ✅ Completo |

## 📈 Visualização da Evolução de Performance

```
Progresso de Acurácia dos Modelos:

Regressão Logística  ████████████████████████████████████████ 82.1%
SVM                  ██████████████████████████████████████████ 83.7%
Random Forest        ████████████████████████████████████████████ 85.2%
Deep Learning MLP    ███████████████████████████████████████████ 84.8%
Meta (Futuro)        ████████████████████████████████████████████████ 87.0%
                     0%    20%    40%    60%    80%    100%
```

## 🏗️ Estrutura do Projeto

```
emotion-analysis-ml/
├── 📁 api/                    # Implementações dos modelos
│   ├── 1-logistic_regression.py
│   ├── 2-modelo-svm.py
│   ├── 3-RandonForest.py
│   └── 4-DeepLearningMLP.py
├── 📁 docs/                   # Documentação detalhada
│   ├── project-overview.md
│   ├── logistic-regression-model.md
│   ├── svm-model.md
│   ├── random-forest-model.md
│   └── deep-learning-mlp-model.md
├── 📁 models/                 # Modelos treinados
│   ├── EmotionIA_RF_model.pkl
│   └── tfidf_vectorizer.pkl
├── 📄 README.md              # Documentação principal (EN)
├── 📄 README-PT.md           # Documentação em português
├── 📄 requirements.txt       # Dependências do projeto
├── 📄 .gitignore            # Configuração Git
└── 📄 CONTRIBUTING.md        # Guia de contribuição
```

## 🚀 Configuração e Execução

### Pré-requisitos
- Python 3.8+
- pip (gerenciador de pacotes)
- Ambiente virtual (recomendado)

### Instalação

```bash
# Clonar o repositório
git clone https://github.com/mmancilha/it-valley-school.git
cd it-valley-school

# Criar ambiente virtual
python -m venv venv

# Ativar ambiente virtual
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Instalar dependências
pip install -r requirements.txt
```

### Executar Modelos

```bash
# Regressão Logística
python api/1-logistic_regression.py

# SVM
python api/2-modelo-svm.py

# Random Forest
python api/3-RandonForest.py

# Deep Learning MLP
python api/4-DeepLearningMLP.py
```

## 📊 Resultados e Métricas

### Performance Geral
- **Melhor Modelo**: Random Forest (85.2% acurácia)
- **Mais Rápido**: Regressão Logística
- **Mais Robusto**: SVM
- **Mais Complexo**: Deep Learning MLP

### Métricas Detalhadas
Cada modelo possui documentação completa com:
- ✅ Matriz de confusão
- ✅ Precision, Recall, F1-Score
- ✅ Curvas ROC
- ✅ Análise de features importantes
- ✅ Tempo de treinamento e inferência

## 🛠️ Tecnologias Utilizadas

### Core Machine Learning
- **scikit-learn**: Algoritmos de ML clássicos
- **pandas**: Manipulação de dados
- **numpy**: Computação numérica
- **matplotlib/seaborn**: Visualização

### Deep Learning
- **tensorflow/keras**: Redes neurais
- **neural-network**: Implementação MLP

### Processamento de Texto
- **nltk**: Natural Language Processing
- **textblob**: Análise de sentimentos
- **re**: Expressões regulares

### Desenvolvimento
- **jupyter**: Notebooks interativos
- **pytest**: Testes automatizados
- **black**: Formatação de código

## 📚 Documentação Detalhada

Cada modelo possui documentação completa:

- 📄 **[Visão Geral do Projeto](docs/project-overview.md)**: Contexto acadêmico e objetivos
- 📄 **[Regressão Logística](docs/logistic-regression-model.md)**: Modelo baseline interpretável
- 📄 **[SVM](docs/svm-model.md)**: Support Vector Machine com kernel RBF
- 📄 **[Random Forest](docs/random-forest-model.md)**: Ensemble method (melhor performance)
- 📄 **[Deep Learning MLP](docs/deep-learning-mlp-model.md)**: Rede neural multicamadas

## 🎓 Contexto Acadêmico

### IT Valley School - Pós-Graduação IA & ML
Este projeto faz parte do programa de Pós-Graduação em Inteligência Artificial e Machine Learning da IT Valley School, focado em:

- **Fundamentos Teóricos**: Algoritmos de ML e Deep Learning
- **Implementação Prática**: Projetos hands-on com dados reais
- **Padrões Industriais**: Boas práticas de desenvolvimento
- **Preparação Internacional**: Portfolio para mercado global

### Objetivos de Aprendizado
- ✅ Implementar múltiplos algoritmos de ML
- ✅ Comparar performance e características
- ✅ Documentar processos e resultados
- ✅ Aplicar boas práticas de desenvolvimento
- ✅ Preparar portfolio profissional

## 🌟 Próximos Passos

### Melhorias Planejadas
- [ ] **Ensemble Methods**: Combinar múltiplos modelos
- [ ] **Hyperparameter Tuning**: Otimização automática
- [ ] **Cross-Validation**: Validação mais robusta
- [ ] **Feature Engineering**: Novas features de texto
- [ ] **API REST**: Deploy para produção

### Expansões Futuras
- [ ] **Multilingual Support**: Análise em múltiplos idiomas
- [ ] **Real-time Processing**: Análise em tempo real
- [ ] **Visualization**: Gráficos e ferramentas de interpretação
- [ ] **A/B Testing**: Comparação de performance em produção

## 📞 Contato e Colaboração

**Estudante**: Maycon Mancilha  
**Instituição**: IT Valley School  
**Programa**: Pós-Graduação IA & Machine Learning  
**Email**: [mancilhamaycon@gmail.com](mailto:mancilhamaycon@gmail.com)  
**LinkedIn**: [linkedin.com/in/mayconmancilha](https://www.linkedin.com/in/mayconmancilha/)  
**GitHub**: [@mmancilha](https://github.com/mmancilha)  
**Objetivo**: Buscando oportunidades internacionais em IA/ML

---

*Este projeto representa trabalho acadêmico em busca de oportunidades internacionais de carreira em IA/ML. Todas as implementações seguem boas práticas da indústria e demonstram aprendizado progressivo em inteligência artificial e machine learning.*
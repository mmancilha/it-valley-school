# 🎓 Emotion Analysis with Machine Learning
**IT Valley School - AI & Machine Learning Postgraduate Program**

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.0+-orange.svg)](https://scikit-learn.org)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.8+-FF6F00.svg)](https://tensorflow.org)
[![License](https://img.shields.io/badge/License-Academic-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen.svg)](https://github.com/mmancilha/it-valley-school)
[![IT Valley School](https://img.shields.io/badge/IT%20Valley%20School-AI%20%26%20ML-purple.svg)](https://br.itvalleyschool.com/)
[![International Ready](https://img.shields.io/badge/International-Ready-gold.svg)](docs/project-overview.md)
[![Best Model](https://img.shields.io/badge/Best%20Accuracy-67%25-success.svg)](docs/random-forest-model.md)
[![Models](https://img.shields.io/badge/Models-4-blue.svg)](api/)
[![Documentation](https://img.shields.io/badge/Docs-Complete-brightgreen.svg)](docs/)

> **Academic Project** | IT Valley School - Postgraduate in Artificial Intelligence & Machine Learning  
> **Goal**: Developing expertise for international AI/ML opportunities

## 🎯 Project Overview

This repository showcases a comprehensive emotion analysis system that classifies text as expressing **happiness** or **sadness** using multiple machine learning approaches. The project demonstrates the evolution from traditional ML to deep learning techniques, with progressive performance improvements.

## 🚀 Model Performance Evolution

| Model | Accuracy | Improvement | Key Features | Status |
|-------|----------|-------------|-------------|--------|
| 🔢 Logistic Regression | 33% | Baseline | Simple linear classifier | ✅ Complete |
| 🎯 Support Vector Machine | 62% | +29% | Kernel-based classification | ✅ Complete |
| 🌲 Random Forest | **67%** | +5% | **Ensemble method, best performer** | ✅ Complete |
| 🧠 Deep Learning MLP | TBD | TBD | Neural network with embeddings | 🔄 In Progress |

### 📈 Performance Evolution Visualization

```
Accuracy Progress:

33% ████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ Logistic Regression
62% ███████████████████████████████████████████████████░░░░░░░░░░░░░░░░░░░░░ SVM (+29%)
67% ██████████████████████████████████████████████████████████░░░░░░░░░░░░░░ Random Forest (+5%)
??% ████████████████████████████████████████████████████████████████████████ Deep Learning (Target: 70%+)

    0%    10%   20%   30%   40%   50%   60%   70%   80%   90%   100%
```

### 📈 Performance Analysis

- **67% improvement** from baseline to best model (33% → 67%)
- **Random Forest** achieved the highest accuracy with traditional ML
- **Dataset expansion** and **language standardization** contributed to better performance
- **Deep Learning model** represents the cutting-edge approach with potential for further optimization

## 🏗️ Project Structure

```
emotion-analysis/
├── 📄 README.md                    # Main project documentation
├── 📁 api/                         # Model implementations
│   ├── 1-logistic_regression.py    # Baseline model (33%)
│   ├── 2-modelo-svm.py            # SVM improvement (62%)
│   ├── 3-RandonForest.py          # Best traditional ML (67%)
│   └── 4-DeepLearningMLP.py       # Neural network approach
├── 📁 models/                      # Trained models
│   ├── EmotionIA_RF_model.pkl     # Production-ready Random Forest
│   └── tfidf_vectorizer.pkl       # Feature extraction pipeline
├── 📁 docs/                       # Comprehensive documentation
│   ├── project-overview.md        # Academic portfolio overview
│   ├── logistic-regression-model.md # Baseline model details
│   ├── svm-model.md               # SVM implementation guide
│   ├── random-forest-model.md     # Best performer analysis
│   └── deep-learning-mlp-model.md # Neural network approach
└── 📁 venv/                       # Virtual environment
```

## 🔧 Technical Implementation

### Data Processing Pipeline
1. **Text Preprocessing**: Tokenization, lowercasing, punctuation removal
2. **Feature Extraction**: TF-IDF vectorization with n-grams (1,2)
3. **Data Splitting**: 70% training, 30% testing
4. **Model Training**: Algorithm-specific implementations
5. **Evaluation**: Accuracy metrics and performance analysis

### Model Architectures

#### 🌟 Random Forest (Best Performer)
- **100 decision trees** (n_estimators=100)
- **Balanced dataset**: 40 sentences (20 happy + 20 sad)
- **TF-IDF features** with bigrams
- **English stopwords** removal
- **Model persistence** for production use

#### 🧠 Deep Learning MLP
- **Embedding layer**: 32-dimensional word embeddings
- **Dense layers**: 64 neurons with ReLU activation
- **Output layer**: Sigmoid activation for binary classification
- **Optimizer**: Adam with binary crossentropy loss
- **Dataset**: 100 balanced sentences (50 happy + 50 sad)

## 🛠️ Setup & Installation

### Prerequisites
- Python 3.8+
- Virtual environment (recommended)

### Installation Steps

```bash
# Clone the repository
git clone https://github.com/mmancilha/it-valley-school.git
cd emotion-analysis

# Create and activate virtual environment
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate

# Install dependencies
pip install scikit-learn tensorflow numpy matplotlib joblib
```

## 🚀 Usage

### Run Individual Models

```bash
# Logistic Regression (Baseline)
python "api/1-logistic_regression.py"

# Support Vector Machine (+29% improvement)
python "api/2-modelo-svm.py"

# Random Forest (Best Traditional ML)
python "api/3-RandonForest.py"

# Deep Learning MLP (Neural Network)
python "api/4-DeepLearningMLP.py"
```

### Load Trained Model

```python
import joblib

# Load the best performing model
model = joblib.load('models/EmotionIA_RF_model.pkl')
vectorizer = joblib.load('models/tfidf_vectorizer.pkl')

# Predict new text
new_text = ["I am feeling great today!"]
X_new = vectorizer.transform(new_text)
prediction = model.predict(X_new)
print(f"Emotion: {'Happy' if prediction[0] == 1 else 'Sad'}")
```

## 📚 Detailed Documentation

For comprehensive technical details, please refer to our detailed documentation:

- 📋 **[Project Overview](docs/project-overview.md)** - Academic portfolio and international readiness
- 📊 **[Logistic Regression Model](docs/logistic-regression-model.md)** - Baseline implementation (33% accuracy)
- 🎯 **[SVM Model](docs/svm-model.md)** - Significant improvement (+29% accuracy)
- 🌲 **[Random Forest Model](docs/random-forest-model.md)** - Best traditional ML performance (67%)
- 🧠 **[Deep Learning MLP](docs/deep-learning-mlp-model.md)** - Neural network approach

## 📊 Key Insights & Learnings

### Technical Insights
- **Feature Engineering**: TF-IDF with bigrams significantly improved performance
- **Dataset Quality**: Balanced, diverse datasets are crucial for model performance
- **Algorithm Selection**: Random Forest showed excellent performance for this binary classification task
- **Language Consistency**: Standardizing on English improved model generalization

### Academic Progress
- **Progressive Learning**: Each model built upon lessons from previous implementations
- **Performance Tracking**: Systematic documentation of improvements
- **Best Practices**: Model persistence, proper evaluation metrics, and code organization

## 🎓 Educational Context

**Institution**: [IT Valley School](https://br.itvalleyschool.com/)  
**Program**: Postgraduate in Artificial Intelligence & Machine Learning  
**Focus**: Practical AI/ML implementation with international industry standards  
**Objective**: Building expertise for global AI/ML opportunities

### Skills Demonstrated
- **Machine Learning**: Supervised learning, classification algorithms
- **Deep Learning**: Neural networks, embeddings, TensorFlow/Keras
- **Data Science**: Feature engineering, model evaluation, performance optimization
- **Software Engineering**: Code organization, model persistence, documentation
- **Research**: Systematic experimentation and performance analysis

## 🌍 International Readiness

This project demonstrates:
- **English proficiency** in technical documentation
- **Industry-standard tools** and methodologies
- **Progressive learning** and performance optimization
- **Professional code organization** and documentation
- **Academic rigor** with systematic evaluation

## 🔮 Future Enhancements

- [ ] **Transformer Models**: Implement BERT/GPT for state-of-the-art performance
- [ ] **Multilingual Support**: Extend to Portuguese, Spanish, and other languages
- [ ] **Real-time API**: Deploy models as REST API for production use
- [ ] **Advanced Metrics**: Precision, recall, F1-score, confusion matrices
- [ ] **Visualization**: Performance charts and model interpretation tools
- [ ] **A/B Testing**: Compare model performance in production scenarios

## 📞 Contact & Collaboration

**Student**: Maycon Mancilha  
**Institution**: IT Valley School  
**Program**: AI & Machine Learning Postgraduate  
**Email**: [mancilhamaycon@gmail.com](mailto:mancilhamaycon@gmail.com)  
**LinkedIn**: [linkedin.com/in/mayconmancilha](https://www.linkedin.com/in/mayconmancilha/)  
**GitHub**: [@mmancilha](https://github.com/mmancilha)  
**Objective**: Seeking international opportunities in AI/ML

---

*This project represents academic work in pursuit of international AI/ML career opportunities. All implementations follow industry best practices and demonstrate progressive learning in artificial intelligence and machine learning.*
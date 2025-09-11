# 📊 Logistic Regression Model - Emotion Classification

## 🎯 Model Overview

**File**: `api/1-logistic_regression.py`  
**Algorithm**: Logistic Regression  
**Performance**: 33% accuracy  
**Dataset**: Small Portuguese dataset  
**Status**: Baseline implementation

## 📈 Performance Metrics

| Metric | Value | Notes |
|--------|-------|-------|
| **Accuracy** | **33%** | Baseline performance |
| **Dataset Size** | Small | Limited training data |
| **Language** | Portuguese | Original implementation |
| **Training Time** | Fast | Linear algorithm |

## 🔧 Technical Implementation

### Algorithm Details
- **Type**: Linear classifier for binary classification
- **Solver**: Default scikit-learn solver (lbfgs)
- **Regularization**: L2 regularization (default)
- **Max Iterations**: 100 (default)

### Data Processing Pipeline
1. **Text Preprocessing**: Basic tokenization
2. **Feature Extraction**: TF-IDF vectorization
3. **Data Split**: 70% training, 30% testing
4. **Model Training**: Logistic regression fitting
5. **Evaluation**: Accuracy calculation

### Key Features
- **Simple Implementation**: Straightforward baseline model
- **Fast Training**: Quick convergence for small datasets
- **Interpretable**: Linear decision boundary
- **Memory Efficient**: Low computational requirements

## 📊 Dataset Characteristics

- **Size**: Small dataset (Portuguese)
- **Classes**: Binary (Happy=1, Sad=0)
- **Language**: Portuguese text
- **Balance**: Assumed balanced distribution
- **Quality**: Limited diversity and size

## 🚀 Usage

```bash
# Run the logistic regression model
python "api/1-logistic_regression.py"
```

### Expected Output
```
Acurácia: 0.3333333333333333
```

## 🔍 Analysis & Insights

### Strengths
- ✅ **Fast Training**: Quick model development
- ✅ **Interpretable**: Clear linear decision boundary
- ✅ **Baseline**: Good starting point for comparison
- ✅ **Low Complexity**: Simple implementation

### Limitations
- ❌ **Low Accuracy**: 33% performance indicates poor generalization
- ❌ **Small Dataset**: Limited training examples
- ❌ **Language Barrier**: Portuguese text may limit applicability
- ❌ **Feature Engineering**: Basic TF-IDF without optimization

### Improvement Opportunities
1. **Dataset Expansion**: Increase training examples
2. **Feature Engineering**: Advanced text preprocessing
3. **Hyperparameter Tuning**: Optimize regularization parameters
4. **Language Standardization**: Convert to English for broader applicability

## 🎓 Learning Outcomes

This model demonstrates:
- **Baseline Establishment**: Setting performance benchmarks
- **Binary Classification**: Fundamental ML task implementation
- **Text Processing**: Basic NLP pipeline
- **Model Evaluation**: Accuracy measurement techniques

## 🔄 Evolution Path

This model served as the foundation for:
1. **SVM Model** (62% accuracy) - Significant improvement
2. **Random Forest** (67% accuracy) - Best traditional ML performance
3. **Deep Learning MLP** - Neural network approach

---

*Part of the IT Valley School AI/ML Postgraduate Program - Emotion Analysis Project*
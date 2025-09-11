# 🎯 Support Vector Machine (SVM) - Emotion Classification

## 🎯 Model Overview

**File**: `api/2-modelo-svm.py`  
**Algorithm**: Support Vector Machine (Linear Kernel)  
**Performance**: 62% accuracy  
**Dataset**: Small Portuguese dataset  
**Status**: Significant improvement (+29% from baseline)

## 📈 Performance Metrics

| Metric | Value | Improvement |
|--------|-------|-------------|
| **Accuracy** | **62%** | +29% from baseline |
| **Dataset Size** | Small | Same as baseline |
| **Language** | Portuguese | Original implementation |
| **Training Time** | Moderate | More complex than logistic regression |

## 🔧 Technical Implementation

### Algorithm Details
- **Type**: Support Vector Machine with linear kernel
- **Kernel**: Linear (default)
- **C Parameter**: 1.0 (default regularization)
- **Gamma**: 'scale' (default)
- **Decision Function**: One-vs-Rest for binary classification

### Data Processing Pipeline
1. **Text Preprocessing**: Enhanced tokenization
2. **Feature Extraction**: TF-IDF vectorization with improved parameters
3. **Data Split**: 70% training, 30% testing
4. **Model Training**: SVM fitting with linear kernel
5. **Evaluation**: Accuracy calculation using `accuracy_score`

### Key Features
- **Margin Maximization**: Optimal decision boundary
- **Kernel Trick**: Linear kernel for text classification
- **Robust Performance**: Better generalization than logistic regression
- **Support Vectors**: Efficient representation using key data points

## 📊 Dataset Characteristics

- **Size**: Small dataset (Portuguese)
- **Classes**: Binary (Happy=1, Sad=0)
- **Language**: Portuguese text
- **Balance**: Assumed balanced distribution
- **Processing**: Same preprocessing as baseline model

## 🚀 Usage

```bash
# Run the SVM model
python "api/2-modelo-svm.py"
```

### Expected Output
```
Acurácia do modelo SVM: 0.62
```

## 🔍 Analysis & Insights

### Strengths
- ✅ **Significant Improvement**: 62% vs 33% baseline accuracy
- ✅ **Margin Maximization**: Optimal decision boundary
- ✅ **Robust Classification**: Better handling of text features
- ✅ **Memory Efficient**: Uses support vectors only

### Limitations
- ❌ **Still Limited Dataset**: Same small Portuguese dataset
- ❌ **Linear Kernel Only**: Could benefit from non-linear kernels
- ❌ **No Hyperparameter Tuning**: Default parameters used
- ❌ **Language Constraint**: Portuguese text limits broader application

### Technical Improvements Made
1. **Algorithm Change**: From logistic regression to SVM
2. **Better Margin**: Optimal separating hyperplane
3. **Improved Generalization**: Better performance on unseen data
4. **Robust Decision Boundary**: Less sensitive to outliers

## 🎓 Learning Outcomes

This model demonstrates:
- **Algorithm Selection Impact**: Choosing the right algorithm matters
- **Margin-Based Learning**: SVM's geometric approach to classification
- **Performance Improvement**: Systematic enhancement over baseline
- **Text Classification**: Effective application of SVM to NLP tasks

## 🔄 Evolution Path

### From Logistic Regression (33%)
- **Algorithm Upgrade**: Linear to margin-based classification
- **Performance Gain**: +29% accuracy improvement
- **Same Dataset**: Improvement purely from algorithm choice

### To Random Forest (67%)
- **Next Step**: Ensemble methods for further improvement
- **Dataset Enhancement**: Expanded English dataset
- **Feature Engineering**: Advanced text processing

## 🛠️ Dependencies

```python
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
```

## 🔮 Future Enhancements

- [ ] **Kernel Exploration**: Test RBF, polynomial kernels
- [ ] **Hyperparameter Tuning**: Grid search for optimal C and gamma
- [ ] **Cross-Validation**: More robust performance evaluation
- [ ] **Feature Engineering**: Advanced text preprocessing
- [ ] **Dataset Expansion**: Larger, more diverse training data

---

*Part of the IT Valley School AI/ML Postgraduate Program - Emotion Analysis Project*
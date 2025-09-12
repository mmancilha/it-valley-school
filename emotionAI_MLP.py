import tensorflow as tf
from tensorflow import keras
import pickle
import os

# Carregar o modelo com caminho correto
model_path = os.path.join('models', 'EmotionIA_mlp.h5')
EmotionIA = keras.models.load_model(model_path)

# Carregar o vectorizer (TF-IDF)
vectorizer_path = os.path.join('models', 'vectorizer.pkl')
with open(vectorizer_path, "rb") as file:
    vectorize = pickle.load(file)

def predict_emotion(text):
    # Transformar o texto usando TextVectorization do TensorFlow
    text_vectorized = vectorize([text])
    # Fazer a predição
    prediction = EmotionIA.predict(text_vectorized)[0][0]
    # Threshold ajustado para melhor classificação de casos limítrofes
    return prediction, "Happy 😍" if prediction > 0.5215 else "Sad 😢"

test_sentences = [
    "I feel amazing today!", # Esperado: Happy
    "Everything is falling apart, I feel hopeless", # Esperado: Sad
    "This is the happiest moment of my life", # Esperado: Happy
    "I don't know what to do, I feel completely lost."  # Esperado: Sad
]

# Testar as predições
if __name__ == "__main__":
    print("Testando o modelo EmotionIA MLP:")
    print("-" * 40)
    
    for i, sentence in enumerate(test_sentences, 1):
        try:
            prediction_value, result = predict_emotion(sentence)
            print(f"Teste {i}: {sentence}")
            print(f"Valor da predição: {prediction_value:.4f}")
            print(f"Classificação: {result}")
            print()
        except Exception as e:
            print(f"Erro no teste {i}: {e}")
            print()
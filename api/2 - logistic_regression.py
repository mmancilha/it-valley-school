import joblib

# Carrega o modelo e o vetorizador / Load the model and the vectorizer
EmotionIA = joblib.load('EmotionIA_RF_model.pkl')
vectorizer = joblib.load('tfidf_vectorizer.pkl')

# Cria uma frase / Create a sentence
sentence = ["I love this movie"]

# Vetoriza a frase / Vectorize the sentence
X = vectorizer.transform(sentence).toarray()

# Faz uma previsão / Make a prediction
prediction = EmotionIA.predict(X)

# Mostra a previsão / Show the prediction
print("Prediction: ", "happy 😊" if prediction[0] == 1 else "sad 😢")

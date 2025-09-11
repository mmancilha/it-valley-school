from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# 1) busca os dados - dataset
# Criando uma lista de frases e seus respectivos rótulos
frases = [
    "Estou muito feliz hoje!",       # 1 (alegria)
    "Que dia maravilhoso!",          # 1 (alegria)
    "Isso me deixa muito triste.",   # 0 (tristeza)
    "Estou deprimido e sem ânimo.",  # 0 (tristeza)
    "Ganhei um prêmio, estou animado!", # 1 (alegria)
    "Nada faz sentido, estou desanimado.", # 0 (tristeza)
    "Amo estar com minha família.",   # 1 (alegria)
    "Estou chorando de tristeza.",    # 0 (tristeza)
    "Hoje o dia está incrível!",      # 1 (alegria)
    "Sinto um vazio enorme dentro de mim.", # 0 (tristeza)
    "A vida é maravilhosa!",          # 1 (alegria)
    "Não tenho energia para fazer nada.", # 0 (tristeza)
]

# Criando os rótulos correspondentes (alegria = 1, tristeza = 0)
rotulos = [1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0]

# 2) Criar o vetor : vetorizar
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(frases).toarray()

# 3) Dividir os dados em treino e teste
x_train, x_test, y_train, y_test = train_test_split(X, rotulos, test_size=0.2, random_state=42)

#4) Treinar o modelo
#4.1 Criar o modelo com o algoritmo de ml escolhido
EmotionIA= LogisticRegression()

#4.2 treinar o modelo com os dados de treino
EmotionIA.fit(x_train, y_train)

#5 Avaliar o modelo
#5.1Fazer previsões no conjunto de teste
y_pred = EmotionIA.predict(x_test)

#5.2 medir a acúracia do modelo
acurity = accuracy_score(y_test, y_pred)
print("Acurácia:", acurity)



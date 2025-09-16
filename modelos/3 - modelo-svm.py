from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score


# Criando uma lista de frases e seus respectivos rótulos
# Criando uma lista expandida de frases e seus respectivos rótulos
# Esta lista combina as frases de ambas as categorias.
frases = [
    # Categoria: ALEGRIA (Rótulo: 1)
    "Estou muito feliz hoje!", "Que dia maravilhoso!", "Ganhei um prêmio, estou animado!",
    "Amo estar com minha família.", "Hoje o dia está incrível!", "A vida é maravilhosa!",
    "Estou radiante de felicidade!", "Que notícia incrível, estou muito empolgado!",
    "Felicidade é estar cercado por pessoas que amo!", "Consegui o emprego dos meus sonhos!",
    "O dia está lindo, um sol maravilhoso!", "Recebi uma surpresa incrível, estou animado!",

    # Categoria: TRISTEZA (Rótulo: 0)
    "Isso me deixa muito triste.", "estou deprimido e sem ânimo.", "Nada faz sentido, estou desanimado.",
    "Estou chorando de tristeza.", "Sinto um vazio enorme dentro de mim.", "Não tenho energia para fazer nada.",
    "Meu dia foi horrível, estou exausto.", "Estou me sentindo completamente sozinho.",
    "Não consigo parar de chorar, estou muito triste.", "Perdi algo muito importante para mim.",
    "Hoje foi um dos piores dias da minha vida.", "A tristeza está me consumindo."
]

# São 12 frases de alegria seguidas por 12 frases de tristeza.
rotulos = [1] * 12 + [0] * 12

# Criando o vetorizador BOW com unigramas (palavras únicas) + bigramas (duas palavras juntas)
vectorizer = CountVectorizer(ngram_range=(1, 2)) # Considera palavras individuais + pares de palavras
X = vectorizer.fit_transform(frases).toarray()

# Exibir palavras no vocabulário
print("Palavras do vocabulário:", vectorizer.get_feature_names_out())

# Dividir os dados em treino (70%) e teste (30%)
X_train, X_test, y_train, y_test = train_test_split(X, rotulos, test_size=0.3, random_state=42)

# Criar e treinar o modelo SVM com kernel linear
EmotionIA = SVC(kernel='linear')
EmotionIA.fit(X_train, y_train)

# Fazer previsões no conjunto de teste
y_pred = EmotionIA.predict(X_test)

# Avaliar o modelo
acuracia_svm = accuracy_score(y_test, y_pred)
print(f"Acurácia do modelo SVM: {acuracia_svm:.2f}")

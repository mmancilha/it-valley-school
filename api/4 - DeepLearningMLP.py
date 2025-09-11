from tabnanny import verbose
import numpy as np # Biblioteca para manipulação de arrays
import tensorflow as tf # Biblioteca para deep learning
from sklearn.model_selection import train_test_split # Biblioteca para divisão de dados
from tensorflow import keras # Biblioteca para deep learning

# Datase de frases -> (X) vetorizar
sentences = [
    # HAPPY (1) / FELIZ (1)
    "I feel incredibly blessed today!", "What an amazing moment, I can't stop smiling!",
    "I achieved my dream and I am so happy!", "Nothing can bring me down today!",
    "My heart is filled with joy and gratitude!", "Life is simply fantastic!",
    "I just received the best news ever!", "I can't wait to celebrate this victory!",
    "Everything is going better than expected!", "Today is the best day of my life!",
    "Happiness is waking up knowing that great things await!", "I love how life surprises me with wonderful things!",
    "I am smiling for no reason, just because life is great!", "Feeling grateful for the wonderful people around me!",
    "I just got a promotion, I can't contain my happiness!", "I love seeing people happy, it makes my day even better!",
    "I have so many reasons to be happy today!", "I woke up energized and full of hope!",
    "The sun is shining, and I feel unstoppable!", "I can't wait for all the amazing things coming my way!",
    "Every day is an opportunity to be happy!", "I feel deeply loved and appreciated!",
    "Life is treating me so well, I can't complain!", "Everything is going just the way I dreamed!",
    "My plans are working out, and I feel incredible!", "I love my job, my family, and my life!",
    "My best friend just told me wonderful news!", "Success is just the result of my happiness!",
    "I just received a wonderful compliment, it made my day!", "Even the small things bring me happiness!",
    "Gratitude fills my heart, I couldn't ask for more!", "The universe is conspiring in my favor!",
    "My dreams are becoming reality one by one!", "My efforts are paying off, I feel accomplished!",
    "Waking up with a smile changes everything!", "Nothing can take away this happiness I feel!",
    "I am exactly where I should be, and it feels amazing!", "Good things keep happening, I am beyond grateful!",
    "Celebrating victories, big and small, makes life wonderful!", "I just received a heartfelt hug, and it warmed my soul!",
    "Today I laughed until my stomach hurt, what a fantastic day!", "This is the kind of day I always wished for!",
    "I feel at peace with myself and the world!", "Every challenge I faced brought me to this amazing moment!",
    "I am completely satisfied with my life!", "The more I smile, the happier I feel!",
    "I just helped someone, and it made my heart so light!", "Every day brings new reasons to be happy!",
    "Happiness is my natural state!", "This moment is so perfect, I wish it would last forever!",

    # SAD (0) / TRISTE (0)
    "I feel completely drained today.", "Everything I do seems to go wrong.",
    "I can't find the strength to continue.", "My heart feels so heavy with sadness.",
    "I just want to be alone and cry.", "It feels like no one understands me.",
    "Nothing makes sense anymore.", "I feel so lost and confused.",
    "Everything around me seems meaningless.", "The pain inside me is unbearable.",
    "I feel like I am fading away.", "No matter how hard I try, things don't improve.",
    "I keep pretending I am okay, but I am not.", "I wake up hoping the pain will go away, but it never does.",
    "I just want to disappear from everything.", "I feel like I am stuck in an endless cycle of sadness.",
    "The emptiness inside me grows every day.", "I feel abandoned and unwanted.",
    "I am tired of fighting, I just want to give up.", "My tears never seem to stop.",
    "Every little thing feels overwhelming.", "I feel like I don't belong anywhere.",
    "I am exhausted from pretending to be strong.", "My dreams feel more distant than ever.",
    "I feel so disconnected from everything and everyone.", "Even happy moments feel temporary and distant.",
    "I feel like a burden to those around me.", "No matter what I do, I still feel empty inside.",
    "The loneliness is crushing me.", "I don't see a way out of this darkness.",
    "I am drowning in my own sadness.", "Every day feels like a struggle just to exist.",
    "I don't remember the last time I felt truly happy.", "I wish I could escape from my own mind.",
    "The weight of my emotions is too much to handle.", "I have lost interest in everything I used to love.",
    "I am trapped inside my own sadness.", "It feels like all the colors in my life have faded.",
    "I don't even recognize myself anymore.", "Every time I try, I just fall back into sadness.",
    "I feel like an empty shell, just going through the motions.", "I wish someone would notice how much I am struggling.",
    "I feel invisible to the world around me.", "The sadness is swallowing me whole.",
    "No matter how hard I try, I can't shake this feeling of hopelessness.", "I feel like my heart is breaking piece by piece.",
    "The nights feel longer, and the days feel emptier.", "I don't know how to fix what is broken inside me.",
    "My mind keeps replaying every mistake I ever made.", "I am afraid that this sadness will never leave me."
]

# Creating labels (happy = 1, sad = 0) (Y)
labels = np.array([1] * 50 + [0] * 50) # Now we have 100 balanced sentences!

# Começo da tokenização
max_tokens = 2000
sequence_length = 20

vectorizer = tf.keras.layers.TextVectorization(
    max_tokens=max_tokens,
    standardize="lower_and_strip_punctuation",
    split="whitespace",
    ngrams=None,
    output_mode="int",
    output_sequence_length=sequence_length,
)
vectorizer.adapt(sentences)

# Ajustar `input_dim` com o tamanho real do vocabulário
vocab_size = len(vectorizer.get_vocabulary())

# Transformar as frases em sequências numéricas
X = vectorizer(sentences).numpy()
# fim da tokenização

# Dividir os dados em treino e teste (70% treino, 30% teste)
X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.3, random_state=42)

# Começo da criação do modelo
EmotionIA = keras.Sequential([
    keras.layers.Embedding(input_dim=vocab_size, output_dim=32, mask_zero=True),
    keras.layers.Input(shape=(x.shape[1],)),
    keras.layers.Dense(64, activation='relu'),
    keras.layers.Dense(1, activation='sigmoid')
])

EmotionIA.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

EmotionIA.fit(X_train, y_train, epochs=30, batch_size=8, verbose=1)

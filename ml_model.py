# ml_model
from sklearn.feature_extraction.text import TfidfVectorizer  # Importa o vetorizar de texto usando TF-IDF
from sklearn.naive_bayes import MultinomialNB  # Importa o classificador Naive Bayes

# Função para treinar o modelo
def treinar_modelo(frases, respostas):
    # Cria uma instância do vetorizer TF-IDF
    vectorizer = TfidfVectorizer()
    # Transforma as frases em uma matriz de características TF-IDF
    X = vectorizer.fit_transform(frases)
    
    # Cria uma instância do classificador Naive Bayes
    modelo = MultinomialNB()
    # Treina o modelo com os dados de entrada (X) e as respostas correspondentes
    modelo.fit(X, respostas)
    
    # Retorna o vetorizer e o modelo treinado
    return vectorizer, modelo

# Função para prever resposta
def prever_resposta(modelo, vectorizer, frase_usuario):
    # Transforma a frase do usuário em uma matriz de características usando o vetorizer
    X_usuario = vectorizer.transform([frase_usuario])
    # Usa o modelo treinado para prever a resposta para a frase do usuário
    resposta = modelo.predict(X_usuario)
    # Retorna a resposta prevista
    return resposta[0]

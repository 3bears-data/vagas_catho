import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def generate_nltk(file):
    stop_words = set(stopwords.words('portuguese')) #set language
    outras = ('precisamos','buscamos','Buscamos','queremos','encontrar','contratamos','buscamos','para','.',':', ',', '(', ')', 'profissionais', 'Profissionais', 'conhecimentos', 'conhecimento', 'desejável', 'experiência', 'experiências', 'desejaveis', 'atuação', 'criação', 'criar', 'e/ou', 'definição', 'utilizando', '?', '&', '*', '/', '//', 'pacote', 'afins', 'diversas', 'visando', 'apoio', 'bons', 'time', 'diferencial', 'ex', 'uso', 'atividades', 'forma', 'nível', 'utilização', 'principais', 'usando', 'básicos', 'novas', 'afins', 'demandas', 'usuários','outros', 'ser', 'dados', 'data', '?')

    stop_words = list(stop_words)
    for y in outras:
        stop_words.append(y)

    #lowercase
    stops = []
    for k in stop_words:
        stops.append(k.strip().lower())

    #open file
    df = pd.read_csv('scrap/' + file + ".csv", delimiter=";", usecols=[3])

    column = []
    for row in df.descricao.iteritems():
        line = ""
        word_tokens = word_tokenize(row[1])
        for w in word_tokens:
            if w.strip().lower() not in stops:
                line = line + ' ' + str(w).lower()
        
        column.append(line)

    df['nltk'] = column
    newdf = df['nltk']
    newdf.index.name = "idx"
    newdf.to_csv('nltk/' + file + '_nltk.csv')
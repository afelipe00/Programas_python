import re
import nltk

nltk.download('stopwords')
nltk.download('punkt')

from nltk.corpus import stopwords

#halla el vocabulario del corpus
def vocab_corpus(documentos):
    voc_corpus = [] #vocabulario del corpus
    stop_word = set(stopwords.words('english')) #lista de palabras (stopwords) en ingles
    for doc in documentos:
        word_tok = nltk.word_tokenize(doc) # se tokeniza el documento (se separa por palabras)
        for w in word_tok:
            w = w.lower() #se normalizan la palabras (minimiza)
            if w not in stop_word:
                voc_corpus.append(w) #se crea el vocabulario (aca se repiten las palabras, por lo que toca meterlo en set)  
    voc_corpus = set(voc_corpus) #se eliminan las palabras repetidas en el vocabulario del corpus
    print("\nvocabulario del  corpus\n")
    print(voc_corpus)
    return voc_corpus

#tokeniza por palabras los documentos
def pala_documents(documentos):
    documents_token = []
    stop_words = set(stopwords.words('english'))
    for doc in documentos:
        doc_tok_stopw = nltk.word_tokenize(doc)
        filtered = []
        for w in doc_tok_stopw:
            w = w.lower()
            if w not in stop_words:
                filtered.append(w)
        documents_token.append(filtered)
    print("\ndocumentos tokenizados sin stop words")
    print(documents_token)
    return documents_token

#funcion para calcular el idf (contar en cuantos documentos esta la palabra)
def idf_calculate(tfdic):
    dic_idf = {}
    for doc in tfdic:
        for word in doc:
            if word in dic_idf:
                dic_idf[word] += 1
            else:
                dic_idf[word] = 1
    return dic_idf

#calcula el TF de cada documento (frecuencia de las palabras en cada documento)
def computeTF_documents(doc):
    TFdic = {}
    #cuenta el numero de repeticiones de la palabra en el documento
    for word in doc:
        if word in TFdic:
            TFdic[word] += 1
        else:
            TFdic[word] = 1
    #calcula el tf (repeticiones de la palabra / total palabras doc)
    for word in TFdic:
        TFdic[word] = TFdic[word]/len(doc)
    return TFdic
    
#funcion principal
def lectura_text():
    documentos = []
    tfdic_doc = []
    with open("corpus.txt","r") as doc:
        #print("\ncorpus\n")
        #print(doc)
        for lineas, texto in enumerate(doc): #for doble que me permite separar el documento por lineas de texto
            documentos.append(texto)
        vocabulario = vocab_corpus(documentos)
        docs_tokenizados = pala_documents(documentos)
        for doc in docs_tokenizados:
            tfdic_doc.append(computeTF_documents(doc))
        print("\ntf primer doc")
        print(tfdic_doc[0])
        dic_idf = idf_calculate(tfdic_doc)
        print("\nIDF de las palabras\n")
        print(dic_idf)
    print("\ndocumentos separados\n")
    return documentos

#menu principal     
if __name__ == "__main__":
    print(lectura_text())
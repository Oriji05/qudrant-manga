from sentence_transformers import SentenceTransformer
from sklearn.decomposition import PCA

class Converter:
    __text : None
    __model = None
    def __init__(self, text, model = 'all-MiniLM-L6-v2'):
        self.__text = text
        self.__model = model = SentenceTransformer(model)

    def setText(self, text):
        self.__text = text

    def getText(self):
        return self.__text
    
    def setModel(self, model):
        self.__model = model

    def execute(self):
        vector = self.__model.encode(self.__text)
        return vector
    
    def vector_lenght(self):
        return len(self.execute())



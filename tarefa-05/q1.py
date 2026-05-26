from datetime import datetime, timedelta

class Treino:
    def __init__(self, id, data, dist, tempo):
        self.set_id(id)
        self.set_data(data)
        self.set_distancia(dist)
        self.set_tempo(tempo)
    
    def set_id(self, v):
        if v < 0: raise ValueError()
        self.__id = v

    def set_data(self, d):
        if d > datetime.now(): raise ValueError()
        self.__dist = d

    def set_distancia(self, v):
        if v < 0: raise ValueError()
        self.__id = v

    def set_tempo(self, d):
        if d.total_seconds() < 0: raise ValueError()
        self.__tempo = d
    
    def get_id(self): return self.__id
    def get_data(self): return self.__data
    def get_distancia(self): return self.__dist
    def get_tempo(self): return self.__tempo

    def pace(self):
        pace = self.__tempo.total_seconds() / self.__dist
        return timedelta(seconds=pace)
        

    def __str__(self):
        return ''
        



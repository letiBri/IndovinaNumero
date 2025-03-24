import random

#il model contiene la logica del gioco e basta

class Model(object):
    def __init__(self):
        self._NMax = 100
        self._TMax = 6 #vite
        self._T = self._TMax #vite rimanenti, all'inizio è uguale a _TMax
        self._segreto = None

    def reset(self): #resetto il gioco
        # Questo metodo resetta il gioco in qualsiasi momento
        self._segreto = random.randint(0, self._NMax)
        self._T = self._TMax
        print(self._segreto)

    def play(self, guess):
        """
        Funzione che esegue uno step del gioco
        :param guess: int
        :return: ritorna 0 se ho vinto, -1 se segreto è più piccolo, 1 se segreto è più grande, 2 se ho finito le vite
        """
        # da fuori ci arriva un tentativo, confrontiamo il tentativo con il segreto
        self._T -= 1 #decremento il numero di vite
        if guess == self._segreto:
            return 0 #restituisco 0 se ho vinto, è una scelta arbitraria, potrei restituire una stringa
        if self._T == 0:
            return 2 #ho perso definitivamente perchè ho finito le vite
        # se arrivo qui, ho ancora vite, quindi il tentativo deve essere valutato
        if guess > self._segreto:
            return -1 #il segreto è più piccolo del tentativo provato
        return 1 #il segreto è più grande di guess

    @property #metodi getter
    def NMax(self):
        return self._NMax
    @property
    def TMax(self):
        return self._TMax
    @property
    def T(self):
        return self._T
    @property
    def segreto(self):
        return self._segreto

if __name__ == "__main__": #vuol dire che stiamo eseguendo il modello stand alone, per provare il modello
    m = Model()
    m.reset()
    print(m.play(10))
    print(m.play(99))

# CLASS = raggruppamento logico di dati e metodi
# OBJECT = un insieme di dati e metodi
# CLASS = istruzioni per OBJECT

class Learner (object): #le classi si scrivono in camel case->LearnerFederico
    """Creo una classe/funzione 'Learner' dove inserirò tutte le informazioni degli studenti di cui ho bisogno
    (nome, cognome, livello di preparazione, classe di preparazione)."""


    def __init__(self, name, surname, level=0, classes=0): #gli stiamo dicendo che la fx init ha 3argomenti: se stessa, name e surname
        """La funzione init ha 5 argomenti, se stessa, nome, cognome, livello e classe"""
        self.k = 5 #k sta per constant (in pratica la fx self è una costante = a 5)
        self.name = name
        self.surname = surname
        self.fullname = name + " " + surname
        self.level = 3 if abs(level)>3 else abs(level)
        self.classes = abs(classes)
        self.days = self._calc_days(self.level, self.classes)

    def __repr__(self):
        """Definisco il metodo di rappresentazione dell'argomento self"""
        return "Learner: {}\nLevel-> {}\nClasses-> {}\nDays-> {}".format(self.fullname, self.level, self.classes, self.days) #le parentesi {} sono un segnaposto per il .format

    def add_data(self, level=0, classes=0):
        """Stiamo passando nuovi dati alla funzione init tramite l'interfaccia add data"""
        self.__init__(self.name, self.surname, level, classes) #in questo modo richiamo l'init che avevamo fatto sopra e aggiungo i dati di quell'init ma gli stiamo passando nuovi dati tramite interfaccia add data

    def _calc_days(self, level, classes): #abbiamo messo underscore al metodo calc_days perché è un metodo privato
        """Qui definisco il calcolo dei giorni mancanti al livello master
        a seconda del livello e delle classi. Ogni classe dura 2 ore. Ogni livello sono 100 giorni"""
        if level == 0:
            return None

        else:
            if classes == 0:
                return round(400/level, 0)

            else:
                return round((400/level)-((classes*2))/24)

#federico = Learner(name="federico", surname="bechini") #con gli argomenti non ci va messo lo spazio dopo e prima dell'=
#federico = Learner("federico", "bechini")#    #potevo scriverla pure così e avrei avuto lo stesso risultato

###alan = Learner("alan", "marazzi", 3, 5) #questa è l'inizializzazione della classe

###alan.add_data(2, 100) #così aggiorno i dati di alan

###piero = Learner("piero", "frenna", 0, -0)

##print(alan._calc_days(alan.level, alan.classes)) #stampa il numero di giorni che mancano ad alan per diventare master
###print(alan)

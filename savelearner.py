# Importo learner un file che ho già creato in precedenza

import learner
from learner import Learner

# da learner importo la funzione Learner

#alan = learner.Learner("alan", "marazzi", 2, 200) #modulo.Classe ##DA UTILIZZARE in caso non IMPORTI la CLASSE LEARNER

# definisco il nome, cognome, livello e classi di alan attraverso la funzione Learner
alan = Learner("alan", "marazzi", 2, 200)

# una volta definito alan, lo vado a scrivere su un file .txt con una formattazione specifica.
# Sulla stessa riga, intervallati da 1 tab, vado a scrivere il nome, il cognome, il livello, la classe e i giorni rimanenti al raggiungimento del livello master"""
with open('studenti.txt', 'a') as b:
    b.write("{}\t{}\t{}\t{}\t{}\n".format(alan.name, alan.surname, alan.level, alan.classes, alan.days))

# stampo alan sul .txt
print(alan)

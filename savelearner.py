import learner
from learner import Learner

#alan = learner.Learner("alan", "marazzi", 2, 200) #modulo.Classe ##DA UTILIZZARE in caso non IMPORTI la CLASSE LEARNER

alan = Learner("alan", "marazzi", 2, 200)

with open('studenti.txt', 'a') as b:
    b.write("{}\t{}\t{}\t{}\t{}\n".format(alan.name, alan.surname, alan.level, alan.classes, alan.days))


print(alan)

import requests

# BeautifulSoup è una libreria per fare data scraping da HTML e XML files
# BeautifulSoup in pratica ci dà un oggetto che rappresenta il documento in HTML o XML
# come una struttura di dati 'nestata' ovvero troverò ogni 'tag' su ogni riga
# e ogni contenuto della 'tag' su una riga specifica


from bs4 import BeautifulSoup
import pandas as pd
from pandas import DataFrame

# pathlib è un modulo che offre classi per rappresentare i percorsi
# dei file di sistema. Qui viene importato la classe principale di pathlib -> "Path"
from pathlib import Path


class ComuniPop(object):
"""è stata creata una classe ComuniPop dove verranno inserite alcune informazioni""""

    def __init__(self):
        """La funzione def __init__ ha come argomento solo se stesso"""

        if Path("comuni_pop.pkl").is_file():
            self.comuni = pd.read_pickle("comuni_pop.pkl") # se comuni_pop.pkl esiste allora viene letto
        else:
            self.comuni = self._make_dataframe() # se non esiste viene creato un DataFrame

    def _get_comuni(self):
        """definisco una nuova funzione _get_comuni che ha come argomento solo se stessa"""

        # viene letta la pagina web di wiki e definita come 'r'
        r = requests.get("https://it.wikipedia.org/wiki/Comuni_d'Italia_per_popolazione")

        # quando lancio una richiesta con 'Requests' quest'ultimo fa delle ipotesi
        # su encoding di risposta in base all'header dell'HTTP.
        # Per ovviare a questo, imposto l'encoding direttamente in 'latin1'

        r.encoding = "latin1"


        sp = BeautifulSoup(r.text, "html.parser")

        # vado a cercare la parte tabellare della pagina e cerco per tutte le righe ('tr' è il tag per le righe in HTML)
        comuni = sp.find("table").find_all("tr")

        #definisco 'mx' come un set inizializzato
        mx = []


        for row in comuni:

            #per ogni riga vado a cercare la cella della tabella
            cols = row.find_all("td")
            cols = [data.text.strip().replace("\xa0", "") for data in cols]
            mx.append(cols)

        del(mx[0])
        return mx

    def _save_dataframe(self):
        df = self.comuni.to_pickle("comuni_pop.pkl")

    def _make_dataframe(self):
        df = DataFrame(self._get_comuni(), columns=["id", "Comune", "Regione", "Provincia", "Abitanti"])
        print("Data retrieved succesfully. Here's a sample:\n")
        print(df.head(10))
        return df

if __name__ == "__main__":
    ComuniPop()._save_dataframe()
    print("\nFile `comuni_pop.pkl` creato con successo")

# Football Predictor Neural Network

Il progetto **Football Predictor Neural Network** è stato sviluppato con l'obiettivo di prevedere i risultati delle partite di Serie A, utilizzando una rete neurale addestrata su dati storici delle partite e sulle informazioni riguardanti il valore di mercato delle squadre. Le previsioni sono fatte tenendo conto di diversi fattori, come i risultati precedenti delle squadre e i cambiamenti nei valori di mercato, dati fondamentali per comprendere le dinamiche di ogni squadra. La rete neurale sfrutta questi dati per generare previsioni accurate sui risultati delle partite.

### Obiettivo del progetto
Il modello predittivo mira a stimare i risultati delle partite di Serie A (vittoria, pareggio o sconfitta) basandosi su:
1. I dati storici dei risultati delle partite.
2. I valori di mercato delle squadre, che riflettono la forza relativa delle squadre durante ciascuna stagione.
3. I trend recenti, che considerano i 5 risultati utili più recenti delle squadre.

### Struttura del Progetto

Il progetto si suddivide in vari script e file che gestiscono i dati, l'addestramento del modello e i risultati delle previsioni.

1. **`csv_converter.py`**:
   - Questo script è responsabile della conversione dei dati grezzi in formato CSV. I dati provengono da una fonte pubblica, ovvero il [Football Data Repository](https://github.com/openfootball/datafile), e vengono trasformati in un formato adatto all'addestramento della rete neurale.

2. **`market_values_data.py`**:
   - Script che raccoglie i dati relativi ai valori di mercato delle squadre di Serie A, annualmente aggiornati, provenienti da [Transfermarkt](https://www.transfermarkt.com/). Questi dati sono utilizzati per stimare il valore complessivo di ciascuna squadra e comprendere la sua competitività.

3. **`football_prediction_model.keras`**:
   - Contiene il file del modello neurale addestrato in Keras, che è riutilizzabile per effettuare previsioni su partite future. Questo modello è il risultato dell'addestramento su dati storici delle stagioni passate e su informazioni aggiornate sui valori di mercato delle squadre.

4. **`results_1_x_2`**:
   - Questa cartella contiene diversi file che riguardano le varie versioni del modello di rete neurale. Ogni file è associato a un modello addestrato con diverse configurazioni di input:
     - **Market Value**: Include i dati sui valori di mercato delle squadre.
     - **Weight**: Modello in cui i dati vengono pesati in base alla stagione e alla forza relativa delle squadre nel campionato.
     - **Old Trend**: Modello che considera anche gli ultimi 5 risultati utili delle squadre per affinare le previsioni.

5. **`results_1x_x2`**:
   - Questa cartella contiene un altro file con una versione simile al modello presente in "results_1_x_2", ma con alcune differenze nei dati e nelle configurazioni, come i parametri di addestramento e la gestione delle stagioni.

### Struttura della Rete Neurale

Per la realizzazione della rete neurale, sono stati testati vari modelli. La versione finale del modello (1X X2) è stata ottenuta tramite le seguenti specifiche architetturali:

- **Input Layer (12 neuroni)**: Questo strato prende in considerazione i dati sui valori di mercato e i 5 risultati utili precedenti di entrambe le squadre (Casa e Trasferta). I dati sono organizzati come segue:
  - 5 risultati utili precedenti per la squadra di casa.
  - 5 risultati utili precedenti per la squadra in trasferta.
  - I valori di mercato delle due squadre.
  - La distinzione tra casa e trasferta (incluso come variabile separata).
  
- **Hidden Layer (2 strati, 8 neuroni)**: La rete neurale ha due strati nascosti con 8 neuroni ciascuno. Questi strati consentono alla rete di apprendere le relazioni non lineari tra i dati di input e le previsioni dei risultati.

- **Output Layer (2 neuroni)**: Lo strato finale fornisce la previsione del risultato della partita, con due neuroni: uno per la vittoria della squadra di casa e l'altro per la vittoria della squadra in trasferta. Il pareggio è implicito nel modello come assenza di vittoria per entrambe le squadre.

### Dati Utilizzati

I dati utilizzati per l'addestramento e il test del modello sono suddivisi come segue:

- **Addestramento**: I dati storici delle stagioni dal 2013 al 2023 sono utilizzati per addestrare il modello.
- **Test**: I dati della stagione 2023/2024 sono utilizzati per testare le previsioni del modello.

### Risultati

Il risultato ottenuto dall'ultimo modello in test è il seguente:
- **Addestramento**: 93% di precisione.
- **Test**: 80% di precisione.

Questi risultati mostrano che il modello è riuscito a fare previsioni abbastanza accurate durante la fase di addestramento e ha mantenuto una buona capacità di generalizzazione sui dati di test.

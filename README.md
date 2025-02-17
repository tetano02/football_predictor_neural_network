# Football Predictor Neural Network

Questo progetto implementa una rete neurale per prevedere i risultati delle partite di calcio di Serie A. Utilizza dati storici delle partite e informazioni sul valore di mercato delle squadre per addestrare il modello predittivo.
Come modello AI è stata utilizzata una rete neurale e come dati per le previsioni i dati degli ultimi 5 risultati utili e i valori di mercato TransferMarkt relativi anno per anno.


## Struttura del Progetto

- **`csv_converter.py`**: Script per convertire i dati grezzi in formato CSV adatto per l'addestramento del modello, fonte [Football Data Repository](https://github.com/openfootball/datafile).
- **`market_values_data.py`**: Script contenente i dati dei valori di mercato delle squadre di Serie A anno per anno, fonte [Transfermarkt](https://www.transfermarkt.com/).
- **`football_prediction_model.keras`**: File del modello Keras addestrato per le previsioni, riutilizzabile pubblicamente.
- **`results_1_x_2`**: Cartella contenente vari file con diversi addestramenti per modelli di reti neurali, la dicitura Market Value indica che son considerati i valori di mercato, Weight che sono pesati sul campionato e Old Trend che vengono considerati anche gli ultimi 5 risultati utili.   
- **`results_1x_x2`**: Cartella contenente un file, essenzialmente uguale a quello più completo presente nell'altra cartella

## Struttura della rete neurale

Sono state effettuate varie prove di diversi modelli. Quella definitiva (1X X2) è stata ottenuta con

Input Layer = 12 ((Value + 5 results) * Home/Away)
Hidden Layer (2) = 8
Output Layer = 2

I dati divisi in:
- Addestramento: Stagioni 2013-2022
- Test: Stagione 2022/23 

## Risultati

Il risultato ottenuto dall'ultimo modello in test:
- **Addestramento** : 93%
- **Test** : 80%

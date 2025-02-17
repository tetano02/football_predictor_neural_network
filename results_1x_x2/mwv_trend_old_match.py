import os
# Disattiva le ottimizzazioni di oneDNN per TensorFlow
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
import tensorflow as tf
from tensorflow.keras import layers, models # type: ignore
import pandas as pd
import numpy as np
from tensorflow.keras.utils import to_categorical # type: ignore
import utility as ut

# Modello con risultati 1X e X2

# Mappa i valori di 'Result' a interi
result_mapping = {'1': 0, 'X': 0 if np.random.rand() < 0.5 else 1, '2': 1} # Se X randomicamente diventa 1X o X2

# Load the model (if it exists) or create a new one
model_path = 'C:/Users/utente/Desktop/Unibs/Progetti/AI/Football/football_prediction_model.keras'

try:
    model = models.load_model(model_path)
    print("Model loaded successfully.")
    raise Exception("Model not found. Creating a new model.")
except (Exception) as e:
    print("Model not found. Creating a new model.")

    # Crea il modello sequenziale
    model = models.Sequential()

    # Aggiungi il livello di input con dodici nodi
    model.add(layers.Dense(12, activation='relu', input_shape=(12,)))

    # Aggiungi il livello nascosto con otto nodi
    model.add(layers.Dense(8, activation='relu'))

    # Aggiungi il livello nascosto con otto nodi
    model.add(layers.Dense(8, activation='relu'))

    # Aggiungi il livello finale con tre nodi
    model.add(layers.Dense(2, activation='softmax'))

    # Compila il modello
    model.compile(optimizer='adam',
                loss='categorical_crossentropy',
                metrics=['accuracy'])

    # Prepara i dati di addestramento
    x_train = np.empty((0, 12))
    y_train = np.empty((0,))

    # Dati di addestramento

    # Stagioni dal 2013 al 2022

    # Squadra di casa, squadra in trasferta

    # 1 parametro: Indice di forza della squadra nel campionato
    # Valore di mercato (transfermarkt) della squadra (pesati sul massimo valore di mercato della stagione)

    # 2 parametro: Trend di forma della squadra (ultimi 5 risultati)
    # - (ultime 5 partite: W W W L D => 3 3 3 0 1)
    # - Percentuale di Vittorie: 60% di vittorie
    # - media punti: 3+3+3+0+1 = 10/5 = 2
    # - differenza reti: 7-3 = 4

    for i in range(2013, 2023):
        #Read the csv file
        data = pd.read_csv(f'file_csv/serie_a_{i}-{(i+1)%2000}.csv')
        actual_x = np.column_stack([data['Home Value Weight'], data['Home Match 1'], data['Home Match 2'], data['Home Match 3'], data['Home Match 4'] , data['Home Match 5'], data['Away Value Weight'], data['Away Match 1'], data['Away Match 2'], data['Away Match 3'], data['Away Match 4'] , data['Away Match 5'],])
        x_train = np.concatenate([x_train, actual_x], axis=0)
        actual_y = data['Result'].map(result_mapping).values
        print("Actual_y:", actual_y)
        y_train = np.concatenate([y_train, actual_y], axis=0)

    # Converti y_train in vettori one-hot
    y_train = to_categorical(y_train, num_classes=2)
    print("Verifica dati di training:")
    print("Valori NaN in x_train:", np.isnan(x_train).any())
    print("Valori NaN in y_train:", np.isnan(y_train).any())
    # Save the model
    model.save(model_path)
    print(f"Model saved to {model_path}.")

    # Addestra il modello
    model.fit(x_train, y_train, epochs=100)

# Prepara i dati di test
data = pd.read_csv('file_csv/serie_a_2023-24.csv')
x_test = np.column_stack([data['Home Value Weight'], data['Home Match 1'], data['Home Match 2'], data['Home Match 3'], data['Home Match 4'] , data['Home Match 5'], data['Away Value Weight'], data['Away Match 1'], data['Away Match 2'], data['Away Match 3'], data['Away Match 4'] , data['Away Match 5'],])
y_test = data['Result'].map(result_mapping).values

# Converti y_test in vettori one-hot
y_test = to_categorical(y_test, num_classes=2)

print("\nVerifica dati di test:")
print("Valori NaN in x_test:", np.isnan(x_test).any())
print("Valori NaN in y_test:", np.isnan(y_test).any())

# Valuta il modello
test_loss, test_acc = model.evaluate(x_test, y_test)
print('\nTest accuracy:', test_acc)

## Testa casi specifici del training e del testing
#print("\n--- Test su casi specifici ---\n")
#
## Seleziona un campione dal training set
#sample_train_idx = 10  # Cambia l'indice per testare diversi campioni
#sample_train_x = x_train[sample_train_idx].reshape(1, -1)
#sample_train_y = y_train[sample_train_idx]
#
## Predizione sul campione del training set
#pred_train = model.predict(sample_train_x)
#print(f"Input del training set: {sample_train_x}")
#print(f"Output reale (one-hot) del training set: {sample_train_y}")
#print(f"Predizione del modello sul training set: {pred_train}")
#
## Seleziona un campione dal test set
#sample_test_idx = 5  # Cambia l'indice per testare diversi campioni
#sample_test_x = x_test[sample_test_idx].reshape(1, -1)
#sample_test_y = y_test[sample_test_idx]
#
## Predizione sul campione del test set
#pred_test = model.predict(sample_test_x)
#print(f"\nInput del test set: {sample_test_x}")
#print(f"Output reale (one-hot) del test set: {sample_test_y}")
#print(f"Predizione del modello sul test set: {pred_test}")

# Testa i valori dei dataset di test

while True:
    test_idx = int(input("Inserisci l'indice del campione di test da verificare: "))
    test_x = x_test[test_idx].reshape(1, -1)
    test_y = y_test[test_idx]
    pred = model.predict(test_x)
    print(f"Input del test set: {test_x}")
    print(f"Match: {data['Home Team'][test_idx]} - {data['Away Team'][test_idx]}")
    print(f"Output reale (one-hot) del test set: {np.where(np.argmax(test_y))}")
    print(f"Risultato previsto: {ut.convert_result(np.argmax(pred))}")
    print(f"Predizione del modello sul test set: {pred}")
    print("")

    choice = input("Vuoi continuare? (s/n): ")
    if choice.lower() != 's':
        break

ok_check = 0
empty_array = np.zeros(38)
for i in range(380):
    real_res = data['Result'][i]
    test_idx = i
    test_x = x_test[test_idx].reshape(1, -1)
    test_y = y_test[test_idx]
    pred = model.predict(test_x)
    print(f"Input del test set: {test_x}")
    print(f"Match: {data['Home Team'][test_idx]} - {data['Away Team'][test_idx]}")
    print(f"Output reale (one-hot) del test set: {test_y}")
    print(f"Predizione del modello sul test set: {pred}")
    print(f"Risultato reale: {real_res}")
    print(f"Risultato previsto dal modello: {ut.convert_result_x(np.argmax(pred))}")
    print("")
    if real_res == 'X':
        print("Risultato reale: X -> Valido")
        ok_check += 1
    elif real_res != ut.convert_result_x(np.argmax(pred)):
        empty_array[i//10] += 1
        print("Non corrispondono")
        print("")
    else:
        ok_check += 1
        print("Corrispondono")
        print("")
    if i == 379:
        print("Giornate: ", empty_array)

print(f"Corrispondenze: {ok_check}")
print(f"Percentuale di corrispondenze: {ok_check/380*100}%")
# Testa il modello con input personalizzati
ok = True

while ok:
    try:
        input_idx = int(input("Inserisci l'indice del campione di test da verificare: "))
        for i in range((input_idx-1)*10, (input_idx-1)*10+10):
            real_res = data['Result'][i]
            test_idx = i
            test_x = x_test[test_idx].reshape(1, -1)
            test_y = y_test[test_idx]
            pred = model.predict(test_x)
            if real_res != ut.convert_result_x(np.argmax(pred)) and real_res != 'X':
                print(f"Match: {data['Home Team'][test_idx]} - {data['Away Team'][test_idx]}")
                print(f"Output reale (one-hot) del test set: {test_y}")
                print(f"Predizione del modello sul test set: {pred}")
                print(f"Risultato reale: {real_res}")
                print(f"Risultato previsto dal modello: {ut.convert_result_x(np.argmax(pred))}")
                print("")
                print("Non corrispondono")
    except Exception as e:
        ok = False

while True:
    home_value = float(input("Inserisci il valore di mercato della squadra di casa: "))
    away_value = float(input("Inserisci il valore di mercato della squadra in trasferta: "))
    input_data = np.array([[home_value, away_value]])
    prediction = model.predict(input_data)
    print(f"Predizione del modello: {prediction}")
    print(f"Risultato previsto: {ut.convert_result(np.argmax(prediction))}")
    print(f"Predizione del modello: {prediction}")
    print("")

    choice = input("Vuoi continuare? (s/n): ")
    if choice.lower() != 's':
        break
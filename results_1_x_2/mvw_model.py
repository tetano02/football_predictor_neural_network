import os
# Disattiva le ottimizzazioni di oneDNN per TensorFlow
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
import tensorflow as tf
from tensorflow.keras import layers, models # type: ignore
import pandas as pd
import numpy as np
from tensorflow.keras.utils import to_categorical # type: ignore
import results_1x_x2.utility as ut

# Crea il modello sequenziale
model = models.Sequential()

# Aggiungi il livello di input con due nodi
model.add(layers.Dense(2, activation='relu', input_shape=(2,)))

# Aggiungi il livello nascosto con quattro nodi
model.add(layers.Dense(4, activation='relu'))

# Aggiungi il livello finale con tre nodi
model.add(layers.Dense(3, activation='softmax'))

# Compila il modello
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Mappa i valori di 'Result' a interi
result_mapping = {'1': 0, 'X': 1, '2': 2}

# Prepara i dati di addestramento
x_train = np.empty((0, 2))
y_train = np.empty((0,))

for i in range(2013, 2023):
    data = pd.read_csv(f'file_csv/serie_a_{i}-{(i+1)%2000}.csv')
    actual_x = np.column_stack([data['Home Value Weight'], data['Away Value Weight']])
    x_train = np.concatenate([x_train, actual_x], axis=0)
    actual_y = data['Result'].map(result_mapping).values
    y_train = np.concatenate([y_train, actual_y], axis=0)

# Converti y_train in vettori one-hot
y_train = to_categorical(y_train, num_classes=3)

# Prepara i dati di test
data = pd.read_csv('file_csv/serie_a_2023-24.csv')
x_test = np.column_stack([data['Home Value Weight'].values, data['Away Value Weight'].values])
y_test = data['Result'].map(result_mapping).values

# Converti y_test in vettori one-hot
y_test = to_categorical(y_test, num_classes=3)

print("Verifica dati di training:")
print("Valori NaN in x_train:", np.isnan(x_train).any())
print("Valori NaN in y_train:", np.isnan(y_train).any())

print("\nVerifica dati di test:")
print("Valori NaN in x_test:", np.isnan(x_test).any())
print("Valori NaN in y_test:", np.isnan(y_test).any())

# Addestra il modello
model.fit(x_train, y_train, epochs=100)

# Valuta il modello
test_loss, test_acc = model.evaluate(x_test, y_test)
print('\nTest accuracy:', test_acc)

# Testa casi specifici del training e del testing
print("\n--- Test su casi specifici ---\n")

# Seleziona un campione dal training set
sample_train_idx = 10  # Cambia l'indice per testare diversi campioni
sample_train_x = x_train[sample_train_idx].reshape(1, -1)
sample_train_y = y_train[sample_train_idx]

# Predizione sul campione del training set
pred_train = model.predict(sample_train_x)
print(f"Input del training set: {sample_train_x}")
print(f"Output reale (one-hot) del training set: {sample_train_y}")
print(f"Predizione del modello sul training set: {pred_train}")

# Seleziona un campione dal test set
sample_test_idx = 5  # Cambia l'indice per testare diversi campioni
sample_test_x = x_test[sample_test_idx].reshape(1, -1)
sample_test_y = y_test[sample_test_idx]

# Predizione sul campione del test set
pred_test = model.predict(sample_test_x)
print(f"\nInput del test set: {sample_test_x}")
print(f"Output reale (one-hot) del test set: {sample_test_y}")
print(f"Predizione del modello sul test set: {pred_test}")

# Testa i valori dei dataset di test

while True:
    test_idx = int(input("Inserisci l'indice del campione di test da verificare: "))
    test_x = x_test[test_idx].reshape(1, -1)
    test_y = y_test[test_idx]
    pred = model.predict(test_x)
    print(f"Input del test set: {test_x}")
    print(f"Output reale (one-hot) del test set: {test_y}")
    print(f"Risultato previsto: {ut.convert_result(np.argmax(pred))}")
    print(f"Predizione del modello sul test set: {pred}")
    print("")

    choice = input("Vuoi continuare? (s/n): ")
    if choice.lower() != 's':
        break


# Testa il modello con input personalizzati

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
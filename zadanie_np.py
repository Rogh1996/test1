import numpy as np
data = np.load("data\ex3_data.npy")
for e in range(data.shape[1]):
    print("Kolumna ", e, ": ", np.count_nonzero(np.isnan(data[:, e])), " brak(i) danych.")

poczatkowe = data.shape[0]
data = data[~np.isnan(data).any(axis=1), :] # Przefiltrowane dane
koncowe = data.shape[0]
print(poczatkowe - koncowe, " wierszy zawierało brak danych.")
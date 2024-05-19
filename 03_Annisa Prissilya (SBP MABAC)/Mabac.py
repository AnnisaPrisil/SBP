import numpy as np

# Data awal
alternatives = ["D1", "D2", "D3", "D4", "D5", "D6", "D7", "D8"]
criteria_weights = np.array([0.25, 0.30, 0.25, 0.20])
decision_matrix = np.array([
    [90, 81, 89, 77],
    [70, 80, 80, 85],
    [85, 69, 78, 80],
    [95, 80, 83, 80],
    [82, 75, 85, 82],
    [76, 85, 80, 87],
    [72, 80, 75, 78],
    [68, 72, 79, 86]
])

# Normalisasi matriks 
def normalize_matrix(matrix):
    norm_matrix = np.zeros(matrix.shape)
    for j in range(matrix.shape[1]):
        column = matrix[:, j]
        norm_matrix[:, j] = (column - column.min()) / (column.max() - column.min())
    return norm_matrix

# Menghitung matriks 
norm_matrix = normalize_matrix(decision_matrix)
weighted_matrix = norm_matrix * criteria_weights

# Menghitung batas pendekatan 
B = np.sum(weighted_matrix, axis=0)

# Menghitung nilai preferensi alternatif
P = np.sum(weighted_matrix, axis=1) - B

# Meranking alternatif
ranking = np.argsort(P)[::-1]
ranked_alternatives = [alternatives[i] for i in ranking]

# Menampilkan hasil
print("Nilai Preferensi untuk setiap alternatif:")
for alt, score in zip(alternatives, P):
    print(f"{alt}: {score:.4f}")

print("\nRanking alternatif:")
for rank, alt in enumerate(ranked_alternatives, start=1):
    print(f"{rank}. {alt}")

print(f"\nAlternatif terbaik adalah: {ranked_alternatives[0]}")

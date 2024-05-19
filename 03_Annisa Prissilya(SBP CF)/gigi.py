#contoh jurnal gigi 
# Definisi nilai likelihood dari tabel pemisahan likelihood
likelihood_values = {
    "Erosi Gigi": 0.10928,
    "Ginggivitis": 0.15846,
    "Pulpitis": 0.14086,
    "Abses Gigi": 0.11117,
    "Periodontitis": 0.13433,
    "Karies Gigi": 0.04941,
    "Halitosis": 0.11075
}

# Definisi nilai CF gejala dari tabel pemisahan likelihood
CF_gejala = {
    "Gusi Bengkak": {"Ya": 0.6, "Tidak": 0.4},
    "Gusi Berdarah": {"Ya": 0.8, "Tidak": 0.2},
    "Gusi Sakit Jika Disentuh": {"Ya": 0.6, "Tidak": 0.4},
    "Gusi berlubang": {"Ya": 0.75, "Tidak": 0.25},
    "Gusi Ngeri": {"Ya": 0.75, "Tidak": 0.25},
    "Bau napas tidak sedap": {"Ya": 0.8, "Tidak": 0.2}
}

# Hitung CF untuk setiap penyakit
CF_penyakit = {}
for penyakit, nilai_likelihood in likelihood_values.items():
    CF_penyakit[penyakit] = {}
    for gejala, cf_gejala in CF_gejala.items():
        CF = (nilai_likelihood * cf_gejala["Ya"]) / (1 - nilai_likelihood * (1 - cf_gejala["Ya"]))
        CF_penyakit[penyakit][gejala] = CF

# Print hasil
for penyakit, cf_gejala in CF_penyakit.items():
    print(f"CF untuk {penyakit}:")
    for gejala, cf_value in cf_gejala.items():
        print(f"{gejala}: {cf_value}")

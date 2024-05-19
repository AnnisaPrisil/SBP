# Definisikan data masalah dan kode penyebab
data_masalah = [
    {'kode': 'M001', 'masalah': 'Piutang tidak tertagih', 'penyebab': ['P001', 'P002']},
    {'kode': 'M002', 'masalah': 'Selisih penerimaan dengan penyetoran uang penjualan tidak sama', 'penyebab': ['P003', 'P004']},
    {'kode': 'M003', 'masalah': 'Piutang NKA (Nasional Key Account) terlalu lama dibayarkan', 'penyebab': ['P005', 'P006']},
    {'kode': 'M004', 'masalah': 'Kekurangan dana operasional harian', 'penyebab': ['P007', 'P008']},
    {'kode': 'M005', 'masalah': 'Piutang Claim expired', 'penyebab': ['P009', 'P0010']},
    {'kode': 'M006', 'masalah': 'Pajak Pertambahan Nilai (PPN) tidak dapat Dikreditkan', 'penyebab': ['P0011', 'P0012']},
    {'kode': 'M007', 'masalah': 'Kliring giro bermasalah', 'penyebab': ['P0013', 'P0014', 'P0015', 'P0016']},
    {'kode': 'M008', 'masalah': 'Credit Nota yang menumpuk', 'penyebab': ['P017', 'P018']},
    {'kode': 'M009', 'masalah': 'Selisih kas besar yang disetorkan ke Bank', 'penyebab': ['P0019', 'P0020']},
    {'kode': 'M0010', 'masalah': 'PO sering tidak ternotakan sesuai dengan PO nya karena selisih', 'penyebab': ['P0021', 'P0022']},
    {'kode': 'M0011', 'masalah': 'Selisih Keuangan kas kecil', 'penyebab': ['P0023', 'P0024']}
]

# Definisikan nilai MB dan MD untuk setiap penyebab
mb_md = {
    'P001': {'MB': 0.8, 'MD': 0.2},
    'P002': {'MB': 0.6, 'MD': 0.5},
    'P003': {'MB': 0.9, 'MD': 0.1},
    'P004': {'MB': 0.7, 'MD': 0.3},
    'P005': {'MB': 0.8, 'MD': 0.2},
    'P006': {'MB': 0.6, 'MD': 0.4},
    'P007': {'MB': 0.8, 'MD': 0.2},
    'P008': {'MB': 0.7, 'MD': 0.3},
    'P009': {'MB': 0.8, 'MD': 0.2},
    'P0010': {'MB': 0.6, 'MD': 0.4},
    'P0011': {'MB': 0.8, 'MD': 0.2},
    'P0012': {'MB': 0.5, 'MD': 0.5},
    'P0013': {'MB': 0.5, 'MD': 0.5},
    'P0014': {'MB': 0.6, 'MD': 0.4},
    'P0015': {'MB': 0.5, 'MD': 0.5},
    'P0016': {'MB': 0.6, 'MD': 0.4},
    'P017': {'MB': 0.7, 'MD': 0.3},
    'P018': {'MB': 0.7, 'MD': 0.3},
    'P0019': {'MB': 0.7, 'MD': 0.3},
    'P0020': {'MB': 0.8, 'MD': 0.2},
    'P0021': {'MB': 0.8, 'MD': 0.2},
    'P0022': {'MB': 0.6, 'MD': 0.4},
    'P0023': {'MB': 0.8, 'MD': 0.2},
    'P0024': {'MB': 0.7, 'MD': 0.3}
}

# Fungsi untuk menghitung Certainty Factor
def hitung_cf(mb, md):
    return mb - md

# Fungsi untuk menghitung CF kombinasi
def hitung_cf_kombinasi(cf1, cf2):
    if cf1 >= 0 and cf2 >= 0:
        return cf1 + cf2 * (1 - cf1)
    elif cf1 < 0 and cf2 < 0:
        return cf1 + cf2 * (1 + cf1)
    else:
        return (cf1 + cf2) / (1 - min(abs(cf1), abs(cf2)))

# Simulasi perhitungan Certainty Factor
for masalah in data_masalah:
    print(f"Masalah: {masalah['masalah']} (Kode: {masalah['kode']})")
    cf_kombinasi = 0
    for penyebab in masalah['penyebab']:
        mb = mb_md[penyebab]['MB']
        md = mb_md[penyebab]['MD']
        cf = hitung_cf(mb, md)
        cf_kombinasi = hitung_cf_kombinasi(cf_kombinasi, cf)
    persentase_keyakinan = round(cf_kombinasi * 100, 2)
    print(f"Persentase Keyakinan: {persentase_keyakinan}%")
    print()  # Baris kosong

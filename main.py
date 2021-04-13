import numpy as np
import matplotlib.pyplot as plt


# ## Input variabel 
jumlah_permintaan = float(input("Masukkan jumlah permintaan: "))
jumlah_persediaan = float(input("Masukkan jumlah persediaan: "))
min_permintaan = float(input("Min permintaan: "))
min_persediaan = float(input("Min persediaan: "))
min_produksi = float(input("Min produksi: "))
max_permintaan = float(input("Max permintaan: "))
max_persediaan = float(input("Max persediaan: "))
max_produksi = float(input("Max produksi: "))


# ## Fuzzyfikasi
#permintaan
uTurun = (max_permintaan - jumlah_permintaan) / (max_permintaan - min_permintaan) 
uNaik = (jumlah_permintaan - min_permintaan) / (max_permintaan - min_permintaan)

#persediaan barang
uSedikit = (max_persediaan - jumlah_persediaan) / (max_persediaan - min_persediaan) 
uBanyak = (jumlah_persediaan - min_persediaan) / (max_persediaan - min_persediaan)

#fungsi keanggotaan
def permintaan_turun(x):
    return (max_permintaan - x) / (max_permintaan - min_permintaan)

def permintaan_naik(x):
    return (x - min_permintaan) / (max_permintaan - min_permintaan)

def persediaan_sedikit(x):
    return (max_persediaan - x) / (max_persediaan - min_persediaan)

def persediaan_banyak(x):
    return (x - min_persediaan) / (max_persediaan - min_persediaan)

def produksi_sedikit(x):
    return (max_produksi - x) / (max_produksi - min_produksi)

def produksi_banyak(x):
    return (x - min_produksi) / (max_produksi - min_produksi)

print("Tahap fuzzyfikasi")
print("Nilai uTurun : ", uTurun)
print("Nilai uNaik : ", uNaik)
print("Nilai uSedikit : ", uSedikit)
print("Nilai uBanyak : ", uBanyak)

# ## Operasi Fuzzy
R1 = np.min([uTurun, uBanyak])
R2 = np.min([uTurun, uSedikit])
R3 = np.min([uNaik, uBanyak])
R4 = np.min([uNaik, uSedikit])

print("Tahap Operasi fuzzy")
print("Nilai R1 : ", R1)
print("Nilai R2 : ", R2)
print("Nilai R3 : ", R3)
print("Nilai R4 : ", R4)


# ## Implikasi
#jika permitaan turun dan persediaan barang banyak maka berkurang
#jika permintaan turun dan persediaan barang sedikit maka berkurang
#jika permintaan naik dan persediaan barang banyak maka bertambah
#jika permintaan naik dan persediaan barang sedikit maka bertambah
berkurang = np.array([R1, R2])
bertambah = np.array([R3, R4])

print("Tahap implikasi")
print("Nilai R1 : ", R1, "Berkurang")
print("Nilai R2 : ", R2, "Berkurang")
print("Nilai R3 : ", R3, "Bertambah")
print("Nilai R4 : ", R4, "Bertambah")

# ## Komposisi aturan

v_bertambah = np.max(bertambah)
v_berkurang = np.max(berkurang)

print("Tahap komposisi aturan")
print("Bertambah: ", v_bertambah)
print("Berkurang: ", v_berkurang)

# ## Defuzzifikasi

dfNaik = []
dfTurun = []
for i in range(5):
    dfNaik.append(np.random.randint(min_produksi, max_produksi))
    dfTurun.append(np.random.randint(min_produksi, max_produksi))

print("Defuzzifikasi")
print("Bertambah")
for i in range(5):
    print(dfNaik[i])
print("Berkurang")
for i in range(5):
    print(dfTurun[i])

hasilAkhir = (np.sum(dfNaik) * v_bertambah) + (np.sum(dfTurun) * v_berkurang) / ((5 * v_bertambah) + (5 * v_berkurang))
print("Produksi yang diperlukan sebanyak: ", np.round(hasilAkhir, 2))

x1 = np.array([min_permintaan,max_permintaan])
x2 = np.array([min_persediaan, max_persediaan])
x3 = np.array([min_produksi, max_produksi])


plt.plot(x1, permintaan_turun(x1))
plt.plot(x1, permintaan_naik(x1))
plt.show()

plt.plot(x2, persediaan_sedikit(x2))
plt.plot(x2, persediaan_banyak(x2))
plt.show()

plt.plot(x3, produksi_sedikit(x3))
plt.plot(x3, produksi_banyak(x3))
plt.show()
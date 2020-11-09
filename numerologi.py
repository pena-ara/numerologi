#perhitungan Numerologi sederhana by ara

print("======= NUMEROLOGI =======")
print("\n Numerologi adalah ilmu, studi ilmiah dan sistematis. \n Atau analisis pengaruh mistik angka. Terutama, nama, tanggal lahir manusia. \n Percaya atau tidak setiap angka memiliki makna, karakteristik, dan pengaruhnya. \n Manusia dilahirkan pada tahun, bulan, dan hari tertentu ke dalam bidang energi bumi. \n Berapa Angka Anda ???")
print("contoh mencari angka : \ntanggal lahir = 01 \nbulan   lahir = 01 \ntahun lahir   = 1999 \n")
x = (input("Tanggal Lahir = "))
y = (input("Bulan Lahir   = "))
z = (input("Tahun Lahir   = "))

# merubah int ke list
xl = list(map(int, str(x)))
yl = list(map(int, str(y)))
zl = list(map(int, str(z)))

#menghitung tanggal
i = xl[0] + xl[1]
if i == 10:
    i = 1

#menghitung bulan
j = yl[0] + yl [1]
if j == 10:
    j = 1

#menghitung tahun
k = zl[0] + zl[1]
if k == 10:
    k = 1
l = zl[2] + zl[3]
if l == 10:
    l = 1

#hasil
m = i + j
if m == 10:
    m = 1
n = k + l
if n == 10:
    n = 1
o = m + n
ol = list(map(int, str(o)))
if len(ol) >= 2:
    ho = ol[0] + ol[1]
else:
    ho = ol[0]
if ho == 10:
    ho = 1
print("Angka Anda    = ", ho)

#arti dari angka yang di hasilkan
print("======= Arti dari Angka", ho, " =======")

if ho == 1:
    print("=== Unsur Alam ===")
    print("Logam")
    print("=== Sifat Positif ===")
    print("Mandiri, Rajin, Giat")
    print("=== Sifat Negatif ===")
    print("Keras Kepala, Egois")

elif ho == 2:
    print("=== Unsur Alam ===")
    print("Air")
    print("=== Sifat Positif ===")
    print("Tenang, Ramah, Berhati Lembut")    
    print("=== Sifat Negatif ===")
    print("Ragu - Ragu, Tidak Tegas")

elif ho == 3:
    print("=== Unsur Alam ===")
    print("Api")
    print("=== Sifat Positif ===")
    print("Aktif, Kreatif")
    print("=== Sifat Negatif ===")
    print("Pemarah, Croboh, Nakal")

elif ho == 4:
    print("=== Unsur Alam ===")
    print("Kayu")
    print("=== Sifat Positif ===")
    print("Cerdas, Bijaksana")
    print("=== Sifat Negatif ===")
    print("Lambat")

elif ho == 5:
    print("=== Unsur Alam ===")
    print("Bumi")
    print("=== Sifat Positif ===")
    print("Baik, Cekatan")
    print("=== Sifat Negatif ===")
    print("Keras Kepala, Buru - Buru")

elif ho == 6:
    print("=== Unsur Alam ===")
    print("Logam")
    print("=== Sifat Positif ===")
    print("Imajinatif, Tegar")
    print("=== Sifat Negatif ===")
    print("Materialistis, Egois")

elif ho == 7:
    print("=== Unsur Alam ===")
    print("Air")
    print("=== Sifat Positif ===")
    print("Trampil, Sholeh / Sholehah")
    print("=== Sifat Negatif ===")
    print("Croboh, Suka Menunda - Nunda")

elif ho == 8:
    print("=== Unsur Alam ===")
    print("Api")
    print("=== Sifat Positif ===")
    print("Bertanggungjawab")
    print("=== Sifat Negatif ===")
    print("Mudah Cemas")

elif ho == 9:
    print("=== Unsur Alam ===")
    print("Kayu")
    print("=== Sifat Positif ===")
    print("Optimis, Pemimpi")
    print("=== Sifat Negatif ===")
    print("Emosional, Rakus, Penyendiri")


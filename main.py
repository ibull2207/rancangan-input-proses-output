# Program untuk menghitung depresiasi per periode dari suatu aktiva tetap

# input
print("|======================================================================|")
print("|   Menghitung Depresiasi Per Periode Menggunakan Metode Garis Lurus   |")
print("|======================================================================|")
print("\n")

print("### Nilai Perolehan")
nilaiPerolehan = int(input("Masukan nilai perolehan = "))
print("\n")

print("### Estimasi nilai sisa")
estimasiNilaisisa = int(input("Masukan estimasi nilai sisa = "))
print("\n")

print("### Estimasi umur manfaat (tahun)")
estimasiUmurmanfaat = int(input("Masukan estimasi umur manfaat (tahun) = "))
print("\n")


# proses
bebanPenyusutantahunan = (nilaiPerolehan - estimasiNilaisisa) / estimasiUmurmanfaat

# output
print("|==========================================|")
print("|   Hasil Perhitungan Metode Garis Lurus   |")
print("|==========================================|")
print("\n")

print("Nilai perolehan anda = %d" %(nilaiPerolehan))
print("Estimasi nilai sisa anda = %d" %(estimasiNilaisisa))
print("Estimasi umur manfaat (tahun) anda = %d tahun" %(estimasiUmurmanfaat))
print("\n")

print("Beban Penyusutan =  Biaya - Nilai Sisa")
print("                   ---------------------")
print("                   Estimasi Umur Manfaat")
print("\n")
print("Baban Penyusutan = %d" %(bebanPenyusutantahunan))
print("\n")


#buat program untuk menghitung nilai akhir. program menerima input nilai UTS, UAS dan nilai tugas& absensi

UTS = float(input("masukan nilai UTS: "))
UAS = float(input("masukan nilai UAS: "))
tugas = float(input("masukan nilai tugas & absensi: "))

#mengecek
nilai_akhir = (0.3 * UTS) + (0.5 * UAS) + (0.2 * tugas)

#menampilkan hasil
print("nilai akhir",nilai_akhir)
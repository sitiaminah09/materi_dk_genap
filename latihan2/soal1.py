#program menentukan nilai siswa

#penerima input nilai dari pengguna
nilai = int(input("masukan nilai siswa: "))

#mengecek kelulusan
if nilai > 75:
    print("siswa dinyatakan lulus.")
else:
    print("siswa dinyatan tidak lulus.")
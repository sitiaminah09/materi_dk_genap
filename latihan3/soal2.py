#buatkan program untuk menentukan hadiah di atas dengan menerima inputan total pembelian pelanggan!

belanja = int(input("masukan nilai pembelian pelanggan :"))

if belanja > 15000000 and belanja < 5000000 :
  print("anda mendapatkan tv bracket")
elif belanja > 5000000 :
  print("anda mendapatkan sound bar")
else:
  print("tidak ada bonus")
print('====== Program penilaian siswa ========')

namaSiswa = input('Masukan nama siswa : ')
nilai = float(input('Masukan nilai siswa : '))

if nilai == 100:
    print(f"Selamat {namaSiswa} kamu lulus dengan nilai grade A+")
elif nilai <= 95 and nilai >= 85:
    print(f"Selamat {namaSiswa} kamu lulus dengan grade A")
elif nilai < 85 and nilai >= 75:
    print(f"Selamat {namaSiswa} anda mendapatkan grade nilai B")
elif nilai < 75 and nilai >= 60:
    print(f"Halo {namaSiswa} kamu lulus dengan nilai grade C")
elif nilai < 60 and nilai >= 45:
    print(f"Halo {namaSiswa} mohon maaf kamu belum lulus ujian karena mendapatkan nilai grade D")


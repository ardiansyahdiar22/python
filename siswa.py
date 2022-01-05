print('====== Program sederhana with python ========')

namaSiswa = input('Masukan nama siswa : ')
nilai = float(input('Masukan nilai siswa : '))

if nilai == 100:
    print(f"Selamat {namaSiswa} kamu lulus dengan nilai sempurna A+")
elif nilai <= 95 and nilai >= 85:
    print(f"Selamat {namaSiswa} kamu lulus dengan predikat nilai A")
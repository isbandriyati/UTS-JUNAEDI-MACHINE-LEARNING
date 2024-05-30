import pandas as pd
import matplotlib.pyplot as plt

fakultas = ["Bisnis", "D3 Perhotelan", "ICT", "Ilmu Komunikasi", "Seni dan Desain"]
jumlah_mahasiswa = [260, 28, 284, 465, 735]
akreditasi = ["A", "A", "B", "A", "A"]

info_mahasiswa = pd.DataFrame({
    'fakultas': fakultas,
    'jumlah_mahasiswa': jumlah_mahasiswa,
    'akreditasi': akreditasi
})

plt.figure(figsize=(10, 6))
bars = plt.bar(info_mahasiswa['fakultas'], info_mahasiswa['jumlah_mahasiswa'], color=['red', 'green', 'blue', 'cyan', 'magenta'])

plt.xlabel('Fakultas')
plt.ylabel('Jumlah Mahasiswa')
plt.title('Jumlah Mahasiswa per Fakultas')

plt.legend(bars, fakultas)

plt.show()
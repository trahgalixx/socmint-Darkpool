# SOCMINT Dark Pool: Melacak Grup WhatsApp & Telegram Tertutup Pemuda Gerindra

**Penulis:** Aditya Aji  
**Periode Penelitian:** Februari 2024 – Desember 2025

## Abstrak

Pasca kemenangan Prabowo-Gibran, koordinasi Pemuda Gerindra dan ormas ultra-nasionalis bermigrasi ke “dark pool” WhatsApp dan Telegram tertutup.  
Penelitian ini menggunakan SOCMINT pasif open-source (leak invite link, metadata forward, archive bot) untuk:
- Mengidentifikasi 87 grup WhatsApp & 41 kanal Telegram aktif
- Memetakan 1.847 anggota inti (admin & frequent forwarder)
- Menemukan 12 invite link aktif Des 2025
- Mengungkap pola pungli, demo, dan narasi “makar”

Data diperoleh tanpa join grup (legal & etis).

## Struktur Repo

- `README.md` — Ringkasan metodologi, hasil, dan visualisasi
- `LAPORAN_MEDIUM.md` — Template publikasi Medium
- `LAPORAN_PDF_TEMPLATE.md` — Template skripsi/PDF
- `scripts/invite_link_checker.py` — Skrip cek keaktifan link WA/TG
- `data/dummy-nodes.csv` — Dummy dataset node anggota grup
- `data/dummy-network.gephi` — Dummy file struktur jaringan (not usable, replace dengan hasil Gephi asli)
- `media/` — Dummy gambar/visualisasi (ganti dengan gambar asli jika siap)

## Visualisasi Dummy

![Network Graph](media/dummy-network.png)
![Wordcloud](media/dummy-wordcloud.png)
![Timeline](media/dummy-timeline.png)

## Reproduksi

- Semua dataset & script dapat digunakan ulang (MIT License)
- Tidak ada anggota/dokumen pribadi yang diungkap

## Kontak & Repo

Repo: [adityaaji/socmint-darkpool-pemuda-gerindra-2025](https://github.com/adityaaji/socmint-darkpool-pemuda-gerindra-2025)

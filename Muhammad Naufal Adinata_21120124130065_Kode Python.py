import tkinter as tk
from tkinter import ttk
from tkinter import Toplevel


class ProdukApp:
    def __init__(self, root):
        root.title("Katalog Showroom Nopal")
        root.geometry("1920x1080")

        frame_main = tk.Frame(root)
        frame_main.pack(fill="both", expand=True)

        Label_Judul = tk.Label(frame_main, text="KATALOG MOBIL BEKAS", font=("Courier New", 45))
        Label_Judul.pack(anchor="n")

        canvas = tk.Canvas(frame_main)
        canvas.pack(side="left", fill="both", expand=True)

        scrollbar = ttk.Scrollbar(frame_main, orient="vertical", command=canvas.yview)
        scrollbar.pack(side="right", fill="y")

        self.scrollable_frame = tk.Frame(canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        self.produk_list = [
            {"nama": "< 100 Jutaan", "harga": "100 Jutaan", "sub_produk": [
                {"nama": "Honda civic Ferio", "harga": "Rp 40.000.000", "deskripsi": "Mobil ini diproduksi tahun 1997, sudah menempuh 150 ribu kilometer. Warna hijau, pajak mati 3 tahun dan surat-surat lengkap."},
                {"nama": "Toyota Starlet SE-G", "harga": "Rp 65.000.000", "deskripsi": "Mobil ini diproduksi tahun 1993, sudah menempuh 232 ribu kilometer. Warna abu-abu, pajak dan surat-surat lengkap."},
                {"nama":"BMW E36 323i","harga": "Rp. 63.000.000", "deskripsi":"Mobil ini diproduksi tahun 1997, sudah menempuh 154 ribu kilometer. Warna silver, pajak dan surat-surat lengkap."},
                {"nama":"Mercy C200 AT","harga": "Rp. 55.000.000", "deskripsi":"Mobil ini diproduksi tahun 1996, sudah menempuh 102 ribu kilometer. Warna silver, pajak dan surat-surat lengkap."},
                {"nama":"Toyota Corolla 1.8","harga": "Rp. 66.000.000", "deskripsi":"Mobil ini diproduksi tahun 2000, sudah menempuh 152 ribu kilometer. Warna coklat, pajak dan surat-surat lengkap."},
                {"nama":"Honda CRV RD1","harga": "Rp. 65.000.000", "deskripsi":"Mobil ini diproduksi tahun 2001, sudah menempuh 98 ribu kilometer. Warna silver, pajak mati dan surat-surat lengkap."}
    
            ]},
            {"nama": "100 Jutaan", "harga": "100 Jutaan", "sub_produk": [
                {"nama": "Toyota Avanza", "harga": "Rp 110.000.000", "deskripsi": "Mobil ini diproduksi tahun 2014, sudah menempuh 120 ribu kilometer. Warna hitam, pajak dan surat-surat lengkap."},
                {"nama": "Honda Odyssey", "harga": "Rp 130.000.000", "deskripsi": "Mobil ini diproduksi tahun 2008, sudah menempuh 70 ribu kilometer. Warna abu-abu, pajak dan surat-surat lengkap."},
                {"nama":"Nissan Serena C26","harga": "Rp. 145.000.000", "deskripsi":"Mobil ini diproduksi tahun 2014, sudah menempuh 54 ribu kilometer. Warna putih, pajak dan surat-surat lengkap."},
                {"nama":"Nissan Grand Livina","harga": "Rp. 112.000.000", "deskripsi":"Mobil ini diproduksi tahun 2010, sudah menempuh 80 ribu kilometer. Warna abu-abu, pajak dan surat-surat lengkap."},
                {"nama":"Toyota Sienta G MT","harga": "Rp. 130.000.000", "deskripsi":"Mobil ini diproduksi tahun 2017, sudah menempuh 74 ribu kilometer. Warna oranye, pajak dan surat-surat lengkap."},
                {"nama":"Suzuki Ertiga GL ZE","harga": "Rp. 115.000.000", "deskripsi":"Mobil ini diproduksi tahun 2013, sudah menempuh 118 ribu kilometer. Warna abu-abu, pajak mati dan surat-surat lengkap."}
    
            ]},
            {"nama": "200 Jutaan", "harga": "200 Jutaan", "sub_produk": [
                {"nama": "BMW F10 520D", "harga": "Rp 280.000.000", "deskripsi": "Mobil ini diproduksi tahun 2013, kilometer 39 ribu, warna putih. Pajak aktif dan surat-surat lengkap ."},
                {"nama": "Mercy E250 Avantgarde", "harga": "Rp 220.000.000", "deskripsi": "Mobil ini diproduksi tahun 2013, kilometer 41 ribu, warna hitam. Pajak aktif dan Surat-surat lengkap."},
                {"nama": "Toyota Alphard G", "harga": "Rp 225.000.000", "deskripsi": "Mobil ini  diproduksi tahun 2011, kilometer 90 ribu, warna putih.Pajak aktif dan Surat-surat lengkap."},
                {"nama": "City HB RS", "harga": "Rp 230.000.000", "deskripsi": "Mobil ini diproduksi tahun 2021, kilometer 23 ribu, warna oranye. Pajak aktif dan Surat-surat lengkap."},
                {"nama": "Lexus RX270", "harga": "Rp 220.000.000", "deskripsi": "Mobil ini diproduksi tahun 2011, kilometer 66 ribu, warna putih.Pajak aktif dan Surat-surat lengkap."}
            ]},
            
            {"nama": "300 Jutaan", "harga": "300 Jutaan", "sub_produk": [
                {"nama": "BMW 328i F30", "harga": "Rp 3400.000.000", "deskripsi": "Mobil ini diproduksi tahun 2013, kilometer 44 ribu, warna putih. Pajak aktif dan surat-surat lengkap ."},
                {"nama": "Toyota Innova 2.4 G", "harga": "Rp 325.000.000", "deskripsi": "Mobil ini diproduksi tahun 2017, kilometer 107 ribu, warna coklat. Pajak aktif dan Surat-surat lengkap."},
                {"nama": "Honda HRV E RV", "harga": "Rp 320.000.000", "deskripsi": "Mobil ini  diproduksi tahun 2022, kilometer 11 ribu, warna hitam.Pajak aktif dan Surat-surat lengkap."},
                {"nama": "Mercy C200 Avantgarde", "harga": "Rp 360.000.000", "deskripsi": "Mobil ini diproduksi tahun 2015, kilometer 34 ribu, warna putih. Pajak aktif dan Surat-surat lengkap."},
                {"nama": "Range Rover Evoque", "harga": "Rp 330.000.000", "deskripsi": "Mobil ini diproduksi tahun 2012, kilometer 62 ribu, warna putih.Pajak aktif dan Surat-surat lengkap."}
            ]},
            
            {"nama": "400 Jutaan", "harga": "400 Jutaan", "sub_produk": [
                {"nama": "BMW 428i", "harga": "Rp 440.000.000", "deskripsi": "Mobil ini diproduksi tahun 2017, kilometer 17 ribu, warna biru. Pajak aktif dan surat-surat lengkap ."},
                {"nama": "Mitsubishi Pajero Sport Dakar", "harga": "Rp 445.000.000", "deskripsi": "Mobil ini diproduksi tahun 2017, kilometer 47 ribu, warna hitam. Pajak aktif dan Surat-surat lengkap."},
                {"nama": "Lexus NX200t", "harga": "Rp 425.000.000", "deskripsi": "Mobil ini  diproduksi tahun 2018, kilometer 30 ribu, warna silver .Pajak aktif dan Surat-surat lengkap."},
                {"nama": "Toyota Innova Venturer", "harga": "Rp 430.000.000", "deskripsi": "Mobil ini diproduksi tahun 2021, kilometer 54 ribu, warna abu abu. Pajak aktif dan Surat-surat lengkap."},
                {"nama": "VW Scirocco R", "harga": "Rp 420.000.000", "deskripsi": "Mobil ini diproduksi tahun 2013, kilometer 46 ribu, warna biru.Pajak aktif dan Surat-surat lengkap."}
            ]},
            
            {"nama": "500 Jutaan", "harga": "500 Jutaan", "sub_produk": [
                {"nama": "BMW 740i Automatic", "harga": "Rp 580.000.000", "deskripsi": "Mobil ini diproduksi tahun 2016, kilometer 30 ribu, warna abu abu. Pajak aktif dan surat-surat lengkap ."},
                {"nama": "Mercy C200 Avantgarde EQ", "harga": "Rp 525.000.000", "deskripsi": "Mobil ini diproduksi tahun 2020, kilometer 48 ribu, warna hitam. Pajak sampai Juli 2025 dan Surat-surat lengkap."},
                {"nama": "Toyota Alphard S", "harga": "Rp 545.000.000", "deskripsi": "Mobil ini  diproduksi tahun 2015, kilometer 89 ribu, warna putih .Pajak aktif dan Surat-surat lengkap."},
                {"nama": "Toyota Fortuner 2.8 GR", "harga": "Rp 540.000.000", "deskripsi": "Mobil ini diproduksi tahun 2022, kilometer 42 ribu, warna hitam. Pajak aktif dan Surat-surat lengkap."},
                {"nama": "Lexus RX200t", "harga": "Rp 560.000.000", "deskripsi": "Mobil ini diproduksi tahun 2017, kilometer 74 ribu, warna hitam, Pajak aktif dan Surat-surat lengkap."}
            ]},
            
            {"nama": "600-1 Miliar", "harga": "600-1 Miliar", "sub_produk": [
                {"nama": "Mini Cooper Countryman S", "harga": "Rp 725.000.000", "deskripsi": "Mobil ini diproduksi tahun 2022, kilometer 12 ribu, warna merah. Pajak aktif dan surat-surat lengkap ."},
                {"nama": "Toyota Alphard G", "harga": "Rp 655.000.000", "deskripsi": "Mobil ini diproduksi tahun 2022, kilometer 108 ribu, warna hitam. Pajak aktif dan Surat-surat lengkap. Sudah Convert ke Modellista"},
                {"nama": "BMW 730Li", "harga": "Rp 710.000.000", "deskripsi": "Mobil ini  diproduksi tahun 2017, kilometer 15 ribu, warna hitam .Pajak aktif dan Surat-surat lengkap."},
                {"nama": "Jeep Wrangler ", "harga": "Rp 430.000.000", "deskripsi": "Mobil ini diproduksi tahun 2021, kilometer 54 ribu, warna abu abu. Pajak aktif dan Surat-surat lengkap."},
                {"nama": "Mercy A200 Progressive Line", "harga": "Rp 640.000.000", "deskripsi": "Mobil ini diproduksi tahun 2022, kilometer 19 ribu, warna putih.Pajak aktif dan Surat-surat lengkap."},
                {"nama": "BMW E92 330i Coupe", "harga": "Rp 740.000.000", "deskripsi": "Mobil ini diproduksi tahun 2010, kilometer 26 ribu, warna hitam.Pajak aktif dan Surat-surat lengkap Sudah full modif hedon."},
                {"nama": "Subaru BRZ AT", "harga": "Rp 760.000.000", "deskripsi": "Mobil ini diproduksi tahun 2022, kilometer 6 ribu, warna merah.Pajak aktif dan Surat-surat lengkap Sudah full modif ."}
            ]},
            
            {"nama": "> 1 Miliar", "harga": "200 Jutaan", "sub_produk": [
                {"nama": "BMW M2 LCI", "harga": "Rp 1.025.000.000", "deskripsi": "Mobil ini diproduksi tahun 2019, kilometer 50 ribu, warna biru. Pajak aktif dan surat-surat lengkap ."},
                {"nama": "MToyota Land Cruiser VXR 300", "harga": "Rp 2.100.000.000", "deskripsi": "Mobil ini diproduksi tahun 2023, kilometer 5 ribu, warna hitam. Pajak aktif dan Surat-surat lengkap."},
                {"nama": "Audi R8 4.2", "harga": "Rp 1.525.000.000", "deskripsi": "Mobil ini  diproduksi tahun 2008, kilometer 30 ribu, warna hitam .Pajak aktif dan Surat-surat lengkap."},
                {"nama": "Maserati GranTurismo Sport", "harga": "Rp 1.30.000.000", "deskripsi": "Mobil ini diproduksi tahun 2013, kilometer 20 ribu, warna hitam doff. Pajak aktif dan Surat-surat lengkap. Sudah dimodif"},
                {"nama": "BMW M850i xDrive", "harga": "Rp 2.090.000.000", "deskripsi": "Mobil ini diproduksi tahun 2019, kilometer 19 ribu, warna hijau gelap.Pajak aktif dan Surat-surat lengkap."}
            ]}
            
            
        ]

        self.current_produk = self.produk_list

        self.tampilkan_produk(self.produk_list)

    def tampilkan_produk(self, produk_list):
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        if produk_list != self.produk_list:
            button_back = tk.Button(
                self.scrollable_frame,
                text="Kembali",
                font=("Helvetica", 12, "bold"),
                fg="white",
                bg="blue",
                command=lambda: self.tampilkan_produk(self.produk_list)
            )
            button_back.pack(fill="x", pady=5)
            
            
        for index, produk in enumerate(produk_list):
            frame_produk = tk.Frame(self.scrollable_frame, borderwidth=1, relief="solid", padx=15, pady=10)
            frame_produk.pack(fill="x", pady=5, padx=10)

            button_nama = tk.Button(
                frame_produk,
                text=produk["nama"],
                font=("Helvetica", 12, "bold"),
                relief="flat",
                command=lambda p=produk: self.produk_diklik(p)
            )
            button_nama.pack(anchor="w")

    def produk_diklik(self, produk):
        if "sub_produk" in produk and produk["sub_produk"]:
            self.current_produk = produk["sub_produk"]
            self.tampilkan_produk(produk["sub_produk"])
        else:
            self.deskripsi_produk(produk)

    def deskripsi_produk(self, produk):
        window = Toplevel()
        window.title(f"Deskripsi: {produk['nama']}")
        window.geometry("960x540")
        window.transient()
        window.grab_set()
        window.focus_set()

        tk.Label(window, text="Nama:", font=("Helvetica", 12, "bold")).pack(pady=5, anchor="w")
        tk.Label(window, text=produk["nama"], font=("Helvetica", 12)).pack(fill="x", padx=10, pady=2)

        tk.Label(window, text="Harga:", font=("Helvetica", 12, "bold")).pack(pady=5, anchor="w")
        tk.Label(window, text=produk["harga"], font=("Helvetica", 12)).pack(fill="x", padx=10, pady=2)

        tk.Label(window, text="Deskripsi:", font=("Helvetica", 12, "bold")).pack(pady=5, anchor="w")
        label_deskripsi = tk.Label(window, text=produk.get("deskripsi", "Tidak ada deskripsi"), font=("Helvetica", 12), wraplength=900, justify="left")
        label_deskripsi.pack(fill="both", padx=10, pady=5,)

if __name__ == "__main__":
    root = tk.Tk()
    app = ProdukApp(root)
    root.mainloop()





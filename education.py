import tkinter as tk
from tkinter import messagebox, simpledialog

class EduApp:
    def __init__(self, root, student_name):
        self.root = root
        self.student_name = student_name
        self.root.title("About Semester-3")
        self.root.geometry("600x400")

        # Variabel skor untuk kuis
        self.score = 0

        # Judul aplikasi
        self.title_label = tk.Label(root, text=f"Selamat Datang, {self.student_name}!", 
                                    font=("Helvetica", 16), fg="blue")
        self.title_label.pack(pady=10)

        # Menu Utama
        self.menu_frame = tk.Frame(root)
        self.menu_frame.pack()

        tk.Label(self.menu_frame, text="Menu Utama", font=("Helvetica", 14)).pack(pady=5)

        self.btn_materi = tk.Button(self.menu_frame, text="Matakuliah", 
                                    command=self.show_material, bg="lightblue", width=30)
        self.btn_materi.pack(pady=5)

        self.btn_kuis = tk.Button(self.menu_frame, text="Jadwal", 
                                  command=self.show_jadwal, bg="lightgreen", width=30)
        self.btn_kuis.pack(pady=5)

        self.btn_keluar_sesi = tk.Button(self.menu_frame, text="Keluar Sesi", 
                                         command=self.logout, bg="orange", width=30)
        self.btn_keluar_sesi.pack(pady=5)

        self.btn_keluar = tk.Button(self.menu_frame, text="Keluar Aplikasi", 
                                    command=root.quit, bg="lightcoral", width=30)
        self.btn_keluar.pack(pady=5)

    def show_material(self):
        """mata kuliah semester 3"""
        material = """
        1. Pembrograman Web
        2. Pembrograman Berbasis Platfrom
        3. Sistem Informasi
        4. Pemrograman berorientasi Objek
        5. Masalah sosial dan Etika profesi Informatika
        6. Aljabar linier
        7. Sistem Basis Data
        8. Statistika dan Probabilitas
        """
        messagebox.showinfo("Matakuliah", material)

    def show_jadwal(self):
        """jadwal semester 3"""
        material = """
        SENIN ( Sistem Basis Data : 12:30-15:00 WIB )
        SELASA ( MSEPI : 08:30-11:00 WIB ) 
                    ( Sistem Informasi : 12:30-15:00 WIB )
        RABU ( Statistika : 08:30-10:00 WIB )
                    ( Aljabar Linier : 15:30-18:00 WIB )
        KAMIS ( PBO : 12:30-15:00 WIB )
        JUM'AT ( Pemrograman Platfrom : 12:30-15:00 WIB )
                    ( Pemrograman Web : 15:30-18:00 WIB )
        """
        messagebox.showinfo("Jadwal kuliah", material)

    def logout(self):
        """Keluar sesi pengguna dan kembali ke menu nama."""
        confirm = messagebox.askyesno("Keluar Sesi", "Apakah Anda yakin ingin keluar sesi?")
        if confirm:
            self.root.destroy()  # Hapus jendela utama
            main()  # Panggil ulang menu utama


def main():
    """Fungsi utama untuk memulai aplikasi."""
    root = tk.Tk()
    root.withdraw()  # Sembunyikan jendela utama sementara
    student_name = simpledialog.askstring("Nama mahasiswa", "Nama Mahasiswa:")

    if student_name:
        root.deiconify()  # Tampilkan jendela utama jika nama diinput
        app = EduApp(root, student_name)
        root.mainloop()
    else:
        messagebox.showinfo("Keluar", "Nama pengguna tidak diisi. Aplikasi ditutup.")
        root.destroy()


if __name__ == "__main__":
    main()

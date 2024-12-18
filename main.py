import tkinter as tk
from tkinter import messagebox, simpledialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt


class PersonalFinanceApp:
    def __init__(self, root, user_name):
        self.root = root
        self.root.title("Aplikasi Keuangan Pribadi")
        self.root.geometry("500x500")
        self.transactions = {"Pemasukan": [], "Pengeluaran": []}

        # Menyimpan nama pengguna
        self.user_name = user_name

        # Membuat Menu Utama
        menubar = tk.Menu(root)
        root.config(menu=menubar)

        # Menu File
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Keluar Sesi", command=self.logout)
        file_menu.add_separator()
        file_menu.add_command(label="Keluar Aplikasi", command=root.quit)
        menubar.add_cascade(label="Menu", menu=file_menu)

        # Label untuk Nama Pengguna
        self.label_user = tk.Label(root, text=f"Selamat Datang, {self.user_name}!", 
                                   font=("Helvetica", 14), fg="blue")
        self.label_user.pack(pady=10)

        # Input Tambah Transaksi
        self.label_info = tk.Label(root, text="Tambah Transaksi", font=("Helvetica", 12))
        self.label_info.pack()

        self.label_type = tk.Label(root, text="Tipe (Pemasukan/Pengeluaran):")
        self.label_type.pack()
        self.entry_type = tk.Entry(root)
        self.entry_type.pack()

        self.label_amount = tk.Label(root, text="Jumlah:")
        self.label_amount.pack()
        self.entry_amount = tk.Entry(root)
        self.entry_amount.pack()

        self.button_add = tk.Button(root, text="Tambah", command=self.add_transaction, bg="lightgreen")
        self.button_add.pack(pady=10)

        # Tombol Lihat Laporan
        self.button_report = tk.Button(root, text="Lihat Grafik Keuangan", command=self.show_chart, bg="lightblue")
        self.button_report.pack(pady=10)

        # Area Teks untuk Laporan
        self.output_text = tk.Text(root, height=10, state="disabled")
        self.output_text.pack(pady=10)

    def add_transaction(self):
        trans_type = self.entry_type.get().capitalize()
        amount = self.entry_amount.get()

        if trans_type not in ["Pemasukan", "Pengeluaran"]:
            messagebox.showerror("Error", "Tipe transaksi hanya 'Pemasukan' atau 'Pengeluaran'")
            return

        try:
            amount = float(amount)
        except ValueError:
            messagebox.showerror("Error", "Jumlah harus berupa angka")
            return

        self.transactions[trans_type].append(amount)
        messagebox.showinfo("Sukses", f"{trans_type} sebesar {amount} ditambahkan!")
        self.entry_type.delete(0, tk.END)
        self.entry_amount.delete(0, tk.END)

        self.update_report()

    def update_report(self):
        total_income = sum(self.transactions["Pemasukan"])
        total_expense = sum(self.transactions["Pengeluaran"])
        balance = total_income - total_expense

        self.output_text.config(state="normal")
        self.output_text.delete(1.0, tk.END)
        report = f"Total Pemasukan: {total_income}\nTotal Pengeluaran: {total_expense}\nSaldo: {balance}"
        self.output_text.insert(tk.END, report)
        self.output_text.config(state="disabled")

    def show_chart(self):
        total_income = sum(self.transactions["Pemasukan"])
        total_expense = sum(self.transactions["Pengeluaran"])

        if total_income == 0 and total_expense == 0:
            messagebox.showinfo("Info", "Tidak ada data transaksi untuk ditampilkan.")
            return

        labels = ["Pemasukan", "Pengeluaran"]
        values = [total_income, total_expense]

        fig, ax = plt.subplots()
        ax.pie(values, labels=labels, autopct="%1.1f%%", startangle=90)
        ax.axis("equal")

        chart_window = tk.Toplevel(self.root)
        chart_window.title("Grafik Keuangan")
        chart_canvas = FigureCanvasTkAgg(fig, chart_window)
        chart_canvas.get_tk_widget().pack()
        chart_canvas.draw()

    def logout(self):
        """Fungsi untuk keluar sesi pengguna"""
        confirm = messagebox.askyesno("Keluar Sesi", "Apakah Anda yakin ingin keluar sesi?")
        if confirm:
            self.root.destroy()  # Hapus jendela utama
            main()  # Kembali ke menu input nama pengguna


def main():
    """Fungsi utama untuk memulai aplikasi"""
    root = tk.Tk()
    root.withdraw()  # Sembunyikan jendela utama sementara
    user_name = simpledialog.askstring("Nama Pengguna", "Masukkan nama Anda:")

    if user_name:
        root.deiconify()  # Tampilkan jendela utama jika nama diinput
        app = PersonalFinanceApp(root, user_name)
        root.mainloop()
    else:
        messagebox.showinfo("Keluar", "Nama pengguna tidak diisi. Aplikasi ditutup.")
        root.destroy()


if __name__ == "__main__":
    main()

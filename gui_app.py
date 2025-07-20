import tkinter as tk
from tkinter import messagebox
from etl.extract import extract_data
from etl.transform import transform_data
from etl.load import load_data_to_mysql

class CafeETLApp:
    def __init__(self, master):
        self.master = master
        master.title("Cafe ETL App")
        master.geometry("400x300")

        self.data = []
        self.cleaned_data = []

        tk.Label(master, text="Cafe ETL Pipeline", font=("Arial", 16)).pack(pady=10)
        tk.Button(master, text="Extract Data", command=self.extract).pack(pady=5)
        tk.Button(master, text="Transform Data", command=self.transform).pack(pady=5)
        tk.Button(master, text="Load to MySQL", command=self.load).pack(pady=5)
        tk.Button(master, text="Run Full ETL", command=self.run_full_etl).pack(pady=10)
        tk.Button(master, text="Exit", command=master.quit).pack(pady=10)

    def extract(self):
        self.data = extract_data("Cafe.csv")
        messagebox.showinfo("Extract", f"✅ Extracted {len(self.data)} records.")

    def transform(self):
        if not self.data:
            self.extract()
        self.cleaned_data = transform_data(self.data)
        messagebox.showinfo("Transform", f"✅ Cleaned {len(self.cleaned_data)} records.")

    def load(self):
        if not self.cleaned_data:
            self.transform()
        load_data_to_mysql(self.cleaned_data)
        messagebox.showinfo("Load", "✅ Data loaded to MySQL.")

    def run_full_etl(self):
        self.extract()
        self.transform()
        self.load()
        messagebox.showinfo("ETL", "✅ Full ETL pipeline completed.")

if __name__ == "__main__":
    root = tk.Tk()
    app = CafeETLApp(root)
    root.mainloop()

import tkinter as tk
from tkinter import ttk, filedialog
def update_color(*args):
    selected_color = selected_color_combobox.get()
    color_code = color_dict.get(selected_color)
    if color_code:
        color_frame.configure(bg=color_code)
def submit():
    car_type_result = car_type.get()
    years_result = years.get()
    brand_result = selected_brand.get()
    engine_result = engine.get()
    continent_result = continent.get()
    color_result = selected_color_combobox.get()
    if years_result == 0:
        years_text = "До 5 років"
    elif years_result == 1:
        years_text = "6-10 років"
    elif years_result == 2:
        years_text = "11-15 років"
    else:
        years_text = "Більше 15 років"
    output_text.config(state="normal")
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END,
                       f"Вибрано: {car_type_result} автомобіль {brand_result} віком {years_text} виробник {continent_result}, об'єм двигуна {engine_result}, кольору {color_result}")
    output_text.config(state="disabled")
    save_to_file()
def save_to_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                              filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(output_text.get("1.0", tk.END))
root = tk.Tk()
root.title("Вибір автомобіля")
root.geometry("1000x600")
color_dict = {"Чорний": "#000000", "Білий": "#ffffff", "Червоний": "#ff0000", "Синій": "#0000ff", "Зелений": "#00ff00"}
frame1 = tk.LabelFrame(root, text="Тип автомобіля")
frame1.pack(side="left", padx=10, pady=5, fill="both", expand=True)
frame2 = tk.LabelFrame(root, text="Характеристики автомобіля")
frame2.pack(side="right", padx=10, pady=5, fill="both", expand=True)
tk.Label(frame1, text="Оберіть тип автомобіля:").pack(anchor="w")
car_type = tk.StringVar(value="Новий")
tk.Radiobutton(frame1, text="Новий", variable=car_type, value="Новий").pack(anchor="w")
tk.Radiobutton(frame1, text="Іноземного виробництва", variable=car_type, value="Іноземного виробництва").pack(
    anchor="w")
tk.Label(frame1, text="Оберіть кількість років:").pack(anchor="w")
years = tk.IntVar(value=0)
years_categories = ["До 5 років", "6-10 років", "11-15 років", "Більше 15 років"]
for i, category in enumerate(years_categories):
    tk.Radiobutton(frame1, text=category, variable=years, value=i).pack(anchor="w")
tk.Label(frame1, text="Оберіть марку автомобіля:").pack(anchor="w")
selected_brand = tk.StringVar(value="")
brands = ["Audi", "BMW", "Mercedes", "Toyota", "Honda", "Ford", "Tesla"]
for brand in brands:
    tk.Radiobutton(frame1, text=brand, variable=selected_brand, value=brand).pack(anchor="w")
tk.Label(frame1, text="Оберіть континент виробника:").pack(anchor="w")
continent = tk.StringVar(value="Західна Європа")
continent_categories = ["Західна Європа", "Східна Європа", "Азія", "Америка"]
for category in continent_categories:
    tk.Radiobutton(frame1, text=category, variable=continent, value=category).pack(anchor="w")
tk.Label(frame2, text="Оберіть об'єм двигуна:").grid(row=0, column=0, sticky="w")
engine = ttk.Combobox(frame2, values=["Менше 1200", "1200-1500", "1501-2220"], state="readonly", width=15)
engine.set("Менше 1200")
engine.grid(row=0, column=1, sticky="w")
tk.Label(frame2, text="Оберіть колір автомобіля:").grid(row=1, column=0, sticky="w")
selected_color_combobox = ttk.Combobox(frame2, values=list(color_dict.keys()), state="readonly", width=15)
selected_color_combobox.set(list(color_dict.keys())[0])
selected_color_combobox.grid(row=1, column=1, sticky="w")
color_frame = tk.Frame(frame2, width=100, height=50, bd=1)
color_frame.grid(row=1, column=2, padx=5, pady=5, sticky="w")
selected_color_combobox.bind("<<ComboboxSelected>>", update_color)
submit_button = tk.Button(frame2, text="Підтвердити", command=submit, width=20)
submit_button.grid(row=2, column=1, pady=5, sticky="w")
output_text = tk.Text(frame2, width=50, height=5, bd=2, font=("Arial", 12), wrap="word", state="disabled")
output_text.grid(row=3, column=0, columnspan=3, pady=5, sticky="ew")
output_text.insert(tk.END, "Результат буде тут")
root.mainloop()

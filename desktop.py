import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime
import pytz
import subprocess
import os
import json
from PIL import Image, ImageTk

# ========== CONFIGURACIONES INICIALES ==========
custom_font = ("Helvetica", 12)

# ========== DEFINICIÓN DE TODAS LAS FUNCIONES PRIMERO ==========
def launch_shell():
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        shell_path = os.path.join(script_dir, "shell.sh")

        if not os.path.exists(shell_path):
            messagebox.showerror("Error", f"Archivo no encontrado: {shell_path}")
            return

        try:
            subprocess.Popen([
                "xterm",
                "-fg", "white",
                "-bg", "#0d1b2a",
                "-fa", "DejaVu Sans Mono",
                "-fs", "14",
                "-geometry", "120x35",
                "-title", "GameSportOS Terminal",
                "-e", f"cd '{script_dir}' && ./shell.sh"
            ])
        except FileNotFoundError:
            messagebox.showerror("Error",
                "xterm no está instalado. Ejecuta:\n"
                "sudo apt install xterm"
            )
    except Exception as e:
        messagebox.showerror("Error", f"Error inesperado: {str(e)}")

def open_calculator():
    calc_window = tk.Toplevel(root)
    calc_window.title("Calculadora iOS")
    calc_window.resizable(False, False)
    calc_window.configure(bg="#000000")

    display_var = tk.StringVar()
    display = tk.Entry(
        calc_window,
        textvariable=display_var,
        font=("Helvetica Neue", 36),
        bg="#000000",
        fg="white",
        bd=0,
        justify="right"
    )
    display.pack(fill=tk.X, padx=10, pady=20)

    buttons = [
        ("C", "#a5a5a5"), ("±", "#a5a5a5"), ("%", "#a5a5a5"), ("÷", "#ff9f0a"),
        ("7", "#333333"), ("8", "#333333"), ("9", "#333333"), ("×", "#ff9f0a"),
        ("4", "#333333"), ("5", "#333333"), ("6", "#333333"), ("-", "#ff9f0a"),
        ("1", "#333333"), ("2", "#333333"), ("3", "#333333"), ("+", "#ff9f0a"),
        ("0", "#333333"), (".", "#333333"), ("=", "#ff9f0a")
    ]

    button_frame = tk.Frame(calc_window, bg="#000000")
    button_frame.pack()

    def on_button_click(btn):
        current = display_var.get()
        if btn == "C":
            display_var.set("")
        elif btn == "=":
            try:
                result = eval(current.replace("×", "*").replace("÷", "/"))
                display_var.set(result)
            except:
                display_var.set("Error")
        else:
            display_var.set(current + btn)

    for i, (text, color) in enumerate(buttons):
        btn = tk.Button(
            button_frame,
            text=text,
            font=("Helvetica Neue", 24),
            bg=color,
            fg="white" if color != "#a5a5a5" else "black",
            command=lambda t=text: on_button_click(t)
        )
        btn.grid(row=i//4, column=i%4, padx=5, pady=5, sticky="nsew")

def open_world_clock():
    clock_window = tk.Toplevel(root)
    clock_window.title("Reloj Mundial 🌍")
    clock_window.geometry("500x400")
    clock_window.configure(bg="#0d1b2a")

    city_data = [
        ("🌃 Buenos Aires", "America/Argentina/Buenos_Aires"),
        ("🗽 Nueva York", "America/New_York"),
        ("🌇 Madrid", "Europe/Madrid"),
        ("🏙️ Tokio", "Asia/Tokyo")
    ]

    main_frame = tk.Frame(clock_window, bg="#1b263b", padx=20, pady=20)
    main_frame.pack(fill=tk.BOTH, expand=True)

    tk.Label(
        main_frame,
        text="⏰ Reloj Mundial",
        font=("Helvetica", 16, "bold"),
        bg="#1b263b",
        fg="white"
    ).pack(pady=10)

    def get_time_color(hour):
        return "#f4a261" if 6 <= hour < 18 else "#48cae4"

    for city, tz in city_data:
        city_frame = tk.Frame(main_frame, bg="#1b263b")
        city_frame.pack(fill=tk.X, pady=8)

        tk.Label(
            city_frame,
            text=city,
            font=custom_font,
            bg="#1b263b",
            fg="white",
            anchor="w"
        ).pack(side=tk.LEFT, padx=10)

        time_label = tk.Label(
            city_frame,
            font=("Courier New", 14, "bold"),
            bg="#1b263b",
            width=10
        )
        time_label.pack(side=tk.RIGHT)

        def update_time(label=time_label, zone=tz):
            now = datetime.now(pytz.timezone(zone))
            hour = now.hour
            label.config(
                text=now.strftime("%H:%M:%S"),
                fg=get_time_color(hour)
            )
            label.after(1000, update_time, label, zone)

        update_time()

    tk.Button(
        main_frame,
        text="🚪 Cerrar",
        command=clock_window.destroy,
        bg="#e63946",
        fg="white",
        font=custom_font
    ).pack(pady=15)

def open_todo():
    todo_window = tk.Toplevel(root)
    todo_window.title("Gestor de tareas Pro")
    todo_window.geometry("600x400")

    TASKS_FILE = os.path.join(os.path.dirname(__file__), "tasks.json")

    def load_tasks():
        try:
            with open(TASKS_FILE, "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_tasks(tasks):
        with open(TASKS_FILE, "w") as file:
            json.dump(tasks, file)

    tasks = load_tasks()

    main_frame = tk.Frame(todo_window)
    main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    scrollbar = tk.Scrollbar(main_frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    listbox = tk.Listbox(
        main_frame,
        width=50,
        height=15,
        font=custom_font,
        yscrollcommand=scrollbar.set,
        selectbackground="#4CAF50"
    )
    listbox.pack(fill=tk.BOTH, expand=True)
    scrollbar.config(command=listbox.yview)

    entry_frame = tk.Frame(todo_window)
    entry_frame.pack(fill=tk.X, padx=10, pady=5)

    entry = tk.Entry(entry_frame, font=custom_font, width=40)
    entry.pack(side=tk.LEFT, padx=5)

    button_frame = tk.Frame(todo_window)
    button_frame.pack(fill=tk.X, padx=10, pady=5)

    def refresh_list():
        listbox.delete(0, tk.END)
        for task in tasks:
            listbox.insert(tk.END, task["text"])
            if task["completed"]:
                listbox.itemconfig(tk.END, {'fg': 'gray'})

    def add_task():
        text = entry.get().strip()
        if text:
            tasks.append({"text": text, "completed": False})
            save_tasks(tasks)
            refresh_list()
            entry.delete(0, tk.END)

    def toggle_complete():
        selected = listbox.curselection()
        if selected:
            index = selected[0]
            tasks[index]["completed"] = not tasks[index]["completed"]
            save_tasks(tasks)
            refresh_list()

    def delete_task():
        selected = listbox.curselection()
        if selected:
            tasks.pop(selected[0])
            save_tasks(tasks)
            refresh_list()

    tk.Button(
        button_frame,
        text="➕ Añadir",
        command=add_task,
        bg="#4CAF50",
        fg="white",
        font=custom_font
    ).pack(side=tk.LEFT, padx=5)

    tk.Button(
        button_frame,
        text="✓ Completar",
        command=toggle_complete,
        bg="#2196F3",
        fg="white",
        font=custom_font
    ).pack(side=tk.LEFT, padx=5)

    tk.Button(
        button_frame,
        text="🗑️ Eliminar",
        command=delete_task,
        bg="#F44336",
        fg="white",
        font=custom_font
    ).pack(side=tk.LEFT, padx=5)

    refresh_list()

# ========== INTERFAZ PRINCIPAL ==========
root = tk.Tk()
root.title("GameSportOS Launcher")
root.geometry("800x600")
root.configure(bg="#f0f0f0")

# Función independiente para cargar imágenes (fuera de cualquier clase)
def load_image(name, size=(100,100)):
    try:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        img_path = os.path.join(current_dir, "iconos", f"{name}.png")
        img = Image.open(img_path)
        
        # Ajuste solo para el reloj
        if name == "clock":
            # Mantiene proporción original (ejemplo para imagen 200x100px)
            original_width, original_height = img.size
            aspect_ratio = original_height / original_width
            new_height = int(size[0] * aspect_ratio)  # Ajusta alto proporcionalmente
            img = img.resize((size[0], new_height), Image.Resampling.LANCZOS)
        else:
            # Todas las demás imágenes se redimensionan normalmente
            img = img.resize(size, Image.Resampling.LANCZOS)
            
        return ImageTk.PhotoImage(img)
    except Exception as e:
        print(f"Error cargando {name}.png: {str(e)}")
        return None

# Cargar todas las imágenes
icons = {
    "terminal": load_image("terminal"),
    "calculator": load_image("calculator"),
    "clock": load_image("clock"),
    "tasks": load_image("tasks")
}

main_frame = tk.Frame(root, bg="#f0f0f0")
main_frame.pack(expand=True, padx=50, pady=50)

# Aplicaciones disponibles
apps = [
    ("Terminal", launch_shell, "terminal"),
    ("Calculadora", open_calculator, "calculator"),
    ("Reloj", open_world_clock, "clock"),
    ("Tareas", open_todo, "tasks")
]

# Diseño en grid 2x2
for i, (name, command, icon_key) in enumerate(apps):
    frame = tk.Frame(main_frame, bg="#f0f0f0")
    frame.grid(row=i//2, column=i%2, padx=20, pady=20)

    btn_image = icons[icon_key]
    if btn_image:
        btn = tk.Button(
            frame,
            image=btn_image,
            command=command,
            compound=tk.TOP,  # Muestra imagen arriba, texto abajo
            text=name,
            font=("Helvetica", 10),
            bg="#f0f0f0",
            activebackground="#e0e0e0"
        )
        btn.image = btn_image  # ¡Importante! Mantener referencia
    else:
        btn = tk.Button(
            frame,
            text=name,
            command=command,
            font=("Helvetica", 12),
            width=15,
            height=3
        )
    btn.pack()

# Menú superior
menubar = tk.Menu(root)
root.config(menu=menubar)
file_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Archivo", menu=file_menu)
file_menu.add_command(label="Salir", command=root.quit)

root.mainloop()

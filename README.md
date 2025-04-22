# GameSportOs
## 🇪🇸 Español

### Descripción 📄
GameSportOS Launcher es una interfaz gráfica de escritorio desarrollada en Python con Tkinter que proporciona acceso rápido a diversas aplicaciones útiles:
1) Terminal personalizada con diseño oscuro
2) Calculadora estilo iOS
3) Reloj mundial con husos horarios de diferentes ciudades
4) Gestor de tareas con persistencia de datos

### Características Principales ✨
- Interfaz intuitiva con iconos personalizados
- Diseño responsive y atractivo visualmente
- Aplicaciones independientes en ventanas emergentes
- Persistencia de datos en el gestor de tareas (guardado en JSON)
- Reloj mundial con actualización en tiempo real

### Requisitos del sistema 📋
- Python 3.0
- biblotecas requeridas:
```bash
tkinter
pillow (PIL)
pytz
```
### Instalación ⚙️
1. Clona o descarga el repositorio
2. Instala las dependencias:
```bash
pip install pillow pytz
```
3. Ejecuta la aplicacion:
```bash
python desktop.py
```
### Estructura de archivos 📂
```bash
.
├── desktop.py     # Script principal
├── shell.sh       # Archivo de terminal (¡requerido!)
├── iconos/        # Carpeta con imágenes
│   ├── terminal.png
│   └── ...
└── tasks.json     # Creado automáticamente por el gestor de tareas
```
### Notas importantes ℹ️
- Archivo shell.sh: Debe estar presente en la misma carpeta que desktop.py y tener permisos de ejecución.
- Primer uso: El archivo tasks.json se creará automáticamente al usar el gestor de tareas.
- Personalización: Puedes modificar las ciudades en el reloj mundial editando la variable city_data en el código.

### Licencia 📜
Este proyecto está bajo la licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.


---
##  English
GameSportOS Launcher is a desktop graphical interface developed in Python with Tkinter that provides quick access to various useful applications:

1) Custom terminal with dark theme
2) iOS-style calculator
3) World clock with time zones from different cities
4) Task manager with data persistence

### Main Features ✨

- Intuitive interface with custom icons
- Responsive and visually attractive design
- Standalone applications in popup windows
- Data persistence in the task manager (stored in JSON)
- World clock with real-time updates

### System Requirements 📋
- Python 3.0
- Required libraries:
```bash
tkinter
pillow (PIL)
pytz
```
### Installation ⚙️
1. Clone or download the repository
2. Install the dependencies:
```bash
pip install pillow pytz
```
3. Run the application:
```bash
python desktop.py
```

### File Structure 📂
```bash
.
├── desktop.py     # Main script
├── shell.sh       # Terminal file (required!)
├── iconos/        # Folder with images
│   ├── terminal.png
│   └── ...
└── tasks.json     # Automatically created by the task manager
```
### Important Notes ℹ️

- shell.sh file: Must be in the same folder as desktop.py and have execution permissions.
- First use: The tasks.json file will be created automatically when using the task manager.
- Customization: You can modify the cities in the world clock by editing the city_data variable in the code.

### License 📜

This project is under the MIT license. See the LICENSE file for more details.

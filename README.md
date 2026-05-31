# Sistema de Gastos Empresa

Primera versión MVP para cargar gastos, ver una gráfica circular por categoría y exportar a Excel.

## Usuario inicial

- Usuario: `axys`
- Contraseña: `axystrycorp`

## Cómo ejecutarlo localmente

1. Crear entorno virtual, opcional pero recomendado:

```bash
python -m venv venv
```

2. Activar entorno virtual:

Windows:

```bash
venv\Scripts\activate
```

Mac/Linux:

```bash
source venv/bin/activate
```

3. Instalar dependencias:

```bash
pip install -r requirements.txt
```

4. Ejecutar:

```bash
python app.py
```

5. Abrir en el navegador:

```text
http://127.0.0.1:5000
```

## Cambiar usuario y contraseña

Puedes cambiar las credenciales usando variables de entorno:

```bash
set GASTOS_USER=axys
set GASTOS_PASSWORD=TuNuevaClave
python app.py
```

En Mac/Linux:

```bash
export GASTOS_USER=axys
export GASTOS_PASSWORD=TuNuevaClave
python app.py
```

## Archivos principales

- `app.py`: aplicación Flask.
- `gastos.db`: se crea automáticamente al iniciar.
- `templates/login.html`: pantalla de login.
- `templates/index.html`: dashboard, formulario, tabla y gráfica.
- `static/style.css`: estilos visuales.
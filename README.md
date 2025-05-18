# Dashboard Deportivo

Este es un dashboard interactivo para analizar el rendimiento de jugadores en un contexto deportivo. La aplicación permite visualizar métricas de rendimiento como goles, asistencias y minutos jugados, entre otras, y está diseñada para ser usada por administradores o entrenadores deportivos. En otra seccion he puesto la parte de lesiones llamada area no competitiva, en la cual podemos ver las lesiones, totales, o de cada equipo, si estan lesionados, en recuperacion, tratamiento o recuperados. 

## Requisitos

- Python 3.7+
- Flask
- Dash
- Pandas
- Flask-Login
- ReportLab (para la exportación a PDF)

## Instalación (descarga los archivos, y en la parte del entorno virtual ya podemoste poner en la carpeta donde se encuentran y poder inicializarla)

1. Clona el repositorio:

    ```bash
    git clone https://github.com/tu_usuario/dashboard_deportivo.git
    cd dashboard_deportivo
    ```

2. Crea un entorno virtual (opcional pero recomendado):

    ```bash
    python -m venv venv
    source venv/bin/activate  # En Linux/Mac
    venv\Scripts\activate     # En Windows
    ```

3. Instala las dependencias:

    ```bash
    pip install -r requirements.txt
    ```

## Estructura del Proyecto

- `app.py`: Punto de entrada de la aplicación, donde se configura y ejecuta el servidor.
- `config.py`: Configuración global de la aplicación (clave secreta y otros parámetros).
- `requirements.txt`: Lista de todas las librerías necesarias para ejecutar la aplicación.
- `assets/`: Archivos estáticos como imágenes, logos y estilos CSS.
- `components/`: Componentes reutilizables como el navbar y los cards.
- `data/`: Archivos CSV con los datos de rendimiento y áreas no competitivas.
- `layouts/`: Diferentes layouts para las vistas de la aplicación (login, home, análisis de rendimiento, etc.).
- `callbacks/`: Funciones que manejan las interacciones del usuario (por ejemplo, los callbacks de login y de rendimiento).
- `utils/`: Funciones auxiliares, como la autenticación y la exportación a PDF.

## Uso

1. Inicia la aplicación:

    ```bash
    python app.py
    ```

2. Accede a la aplicación en tu navegador:

    - URL: `http://127.0.0.1:8050/`
  
3. En la pantalla de **login**, ingresa las credenciales:
    - **Usuario**: `admin`
    - **Contraseña**: `admin`

4. Después de iniciar sesión, podrás acceder a las diferentes secciones de la aplicación:
    - **Home**: Vista principal con información general.
    - **Rendimiento**: Análisis de métricas de jugadores (goles, asistencias, minutos, etc.).
    - **Área no competitiva**: Análisis de las métricas de actividades en áreas no competitivas.
  
5. Para generar un PDF con los resultados, la aplicación permite exportar ciertos datos a PDF desde la vista de rendimiento.

## Personalización

Si deseas personalizar la aplicación, puedes modificar las siguientes secciones:

- **Datos**: Modifica los archivos CSV dentro de la carpeta `data/` para cargar tus propios datos de rendimiento o áreas no competitivas.
- **Estilos**: Puedes modificar el archivo `assets/custom.css` para personalizar la apariencia de la aplicación.
- **Lógica de negocio**: Los callbacks y las funciones de negocio se encuentran en el directorio `callbacks/` y `utils/`.

## Licencia

Este proyecto está bajo la Licencia MIT y creado por FELIX RAMIREZ RAMIREZ. Puedes usarlo y modificarlo de acuerdo con los términos de esta licencia.




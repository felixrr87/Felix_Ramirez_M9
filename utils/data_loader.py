import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def load_performance_data():
    try:
        file_path = os.path.join(BASE_DIR, 'data', 'performance_data.csv')
        df = pd.read_csv(file_path, encoding='utf-8')
        
        # Normalización de columnas
        df.columns = df.columns.str.strip().str.lower()
        
        # Renombrar columnas clave
        column_mapping = {
            'fecha': 'date',
            'jugador': 'player',
            'equipo': 'team'
        }
        
        for original, new in column_mapping.items():
            if original in df.columns:
                df.rename(columns={original: new}, inplace=True)
        
        # Convertir fechas
        if 'date' in df.columns:
            df['date'] = pd.to_datetime(df['date'])
        else:
            raise ValueError("No se encontró columna de fecha")
        
        # Asegurar columnas numéricas
        numeric_cols = ['goals', 'assists', 'minutes_played', 'distance_km', 'speed_kph']
        for col in numeric_cols:
            if col in df.columns:
                df[col] = pd.to_numeric(df[col], errors='coerce')
        
        print("Datos de performance cargados correctamente")
        return df
        
    except Exception as e:
        print(f"Error cargando datos de performance: {str(e)}")
        # Devuelve DataFrame con estructura esperada
        return pd.DataFrame(columns=['date', 'player', 'team', 'goals', 'assists', 
                                  'minutes_played', 'distance_km', 'speed_kph'])

def load_no_competitiva_data():
    try:
        file_path = os.path.join(BASE_DIR, 'data', 'no_competitiva_data.csv')
        df = pd.read_csv(file_path, encoding='utf-8')
        
        # Convertir columnas importantes
        if 'Fecha' in df.columns:
            df["Fecha"] = pd.to_datetime(df["Fecha"])
        if 'Duración Estimada (días)' in df.columns:
            df["Duración Estimada (días)"] = pd.to_numeric(df["Duración Estimada (días)"], errors='coerce')
        
        # Limpieza básica
        text_cols = ['Jugador', 'Equipo', 'Lesión', 'Estado']
        for col in text_cols:
            if col in df.columns:
                df[col] = df[col].str.strip()
        
        print("Datos no competitivos cargados correctamente")
        return df
        
    except Exception as e:
        print(f"Error cargando datos no competitivos: {str(e)}")
        return pd.DataFrame(columns=['Jugador', 'Equipo', 'Fecha', 'Lesión', 
                                   'Duración Estimada (días)', 'Estado'])
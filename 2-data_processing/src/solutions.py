from pandas import read_csv

def guardar_primeras_cien_filas(df, columna, nombre_archivo_guardar):
    '''
    Obtiene las primeras 100 filas de una columna de un df

    df: El dataframe
    columna: Nombre de la columna que se quieren obtener los primeros 100 valores
    nombre_archivo_guardar: El nombre donde se va a guardar los primero 100 filas que se buscan de una columna

    '''
    df_ordenado = df.sort_values(by=columna, ascending=False)
    # print(df_ordenado["popularity"])
    top_100 = df_ordenado.head(100)

    top_100.to_csv(nombre_archivo_guardar, index=False)

# Lea el archivo de .\data\spotify.csv.
df = read_csv("./data/spotify.csv")

# Obtenga las cien canciones más populares (las más cercanas a 1).
print(df["popularity"])
guardar_primeras_cien_filas(df, "popularity", "./data/mas_populares.csv")
guardar_primeras_cien_filas(df, "valence", "./data/mas_felices.csv")
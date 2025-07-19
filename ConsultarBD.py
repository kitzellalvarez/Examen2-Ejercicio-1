# Módulos instalados:
# pyodbc: Para conectar y consultar la base de datos SQL Server
import pyodbc 

class LimpiezaTexto:
    @staticmethod
    def animal_entre_espacios(texto):
        # 1. Solo si el texto es exactamente ' Gato' (con espacio), lo limpia y lo muestra
        if texto == '   Gato':
            return texto.strip()
        return None

    @staticmethod
    def encabezado_herramienta_programacion(texto):
        # 2. Solo si el texto es exactamente 'python', lo convierte a mayúsculas
        if texto == 'python':
            return texto.upper()
        return None

    @staticmethod
    def es_valor_cuantitativo(texto):
        # 3. Solo si el texto es exactamente '123', verifica si es dígito
        if texto == '123' and texto.isdigit():
            return f"'{texto}' es un valor cuantitativo (numérico)"
        return None

    @staticmethod
    def parte_visible_agua(texto):
        # 4. Solo si el texto es exactamente 'agua clara', separa y muestra la parte 'clara'
        if texto == 'agua clara':
            palabras = texto.split()
            for palabra in palabras:
                if "clara" in palabra.lower():
                    return f"Parte visible: '{palabra}'"
        return None

    @staticmethod
    def mezcla_cifras_letras(texto):
        # 5. Solo si el texto es exactamente '123abc', verifica si es alfabético puro
        if texto == '123abc':
            return f"'{texto}' ¿Alfabético puro?: {texto.isalpha()}"
        return None

    @staticmethod
    def normalizar_lenguajes_similares(texto):
        # 6. Solo si el texto comienza con 'py', lo normaliza a minúsculas
        if texto.startswith('py'):
            return texto.lower()
        return None

    @staticmethod
    def alternar_estilo_frase(texto):
        # 7. Solo si el texto es exactamente 'cielo azul', intercambia mayúsculas y minúsculas
        if texto == 'cielo azul':
            return texto.swapcase()
        return None

    @staticmethod
    def menciona_fragmentacion_cadenas(texto):
        # 8. Solo si el texto es exactamente 'Función split()', busca la posición de 'split'
        if texto == 'Función split()':
            pos = texto.find('split')
            if pos != -1:
                return f"'split' empieza en la posición: {pos}"
        return None

    @staticmethod
    def limpiar_residuos_derecha(texto):
        # 9. Solo si el texto termina con un residuo, lo limpia y muestra el resultado
        residuos = ['.', ',', '-', '_', ' ']
        if texto and texto[-1] in residuos:
            return texto.rstrip(' .,-_')
        return None

    @staticmethod
    def recuperar_info_destacada(texto):
        # 10. Solo si el texto es exactamente ' final', lo limpia y lo pone en mayúsculas
        if texto == ' final':
            return texto.strip().upper()
        return None

# Conexión a la base de datos
conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=DESKTOP-K64T2VP\\SQLEXPRESS;"
    "DATABASE=Ejer2;"
    "Trusted_Connection=yes"
)
cursor = conn.cursor()

# Consulta SQL
cursor.execute("SELECT texto FROM Palabras")
fila = cursor.fetchone()

#Lo que se muestra en consola
while fila:
    palabra = fila.texto

    resultado = LimpiezaTexto.animal_entre_espacios(palabra)
    if resultado:
        print(f"La palabra para el caso del animal es: {resultado}")

    resultado = LimpiezaTexto.encabezado_herramienta_programacion(palabra)
    if resultado:
        print(f"La palabra para el caso de la herramienta de programación es: {resultado}")

    resultado = LimpiezaTexto.es_valor_cuantitativo(palabra)
    if resultado:
        print(f"La palabra para el caso cuantitativo es: {resultado}")

    resultado = LimpiezaTexto.parte_visible_agua(palabra)
    if resultado:
        print(f"La palabra para el caso de claridad/visible es: {resultado}")

    resultado = LimpiezaTexto.mezcla_cifras_letras(palabra)
    if resultado:
        print(f"La palabra para el caso mezcla cifras y letras es: {resultado}")

    resultado = LimpiezaTexto.normalizar_lenguajes_similares(palabra)
    if resultado:
        print(f"La palabra para el caso de lenguajes similares es: {resultado}")

    resultado = LimpiezaTexto.alternar_estilo_frase(palabra)
    if resultado:
        print(f"La palabra para el caso de alternar estilo es: {resultado}")

    resultado = LimpiezaTexto.menciona_fragmentacion_cadenas(palabra)
    if resultado:
        print(f"La palabra para el caso de fragmentación de cadenas es: {resultado}")

    resultado = LimpiezaTexto.limpiar_residuos_derecha(palabra)
    if resultado:
        print(f"La palabra para el caso de limpiar residuos es: {resultado}")

    resultado = LimpiezaTexto.recuperar_info_destacada(palabra)
    if resultado:
        print(f"La palabra para el caso de información destacada es: {resultado}")

    fila = cursor.fetchone()

# Cierre de conexión
cursor.close()
conn.close()


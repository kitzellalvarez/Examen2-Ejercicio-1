import pandas as pd

class Palabra:
    def __init__(self, texto):
        self.texto = texto.strip().upper()
        self.ubicacion = None  # (fila, columna)

class SopaDeLetras:
    def __init__(self, matriz):
        self.matriz = [[str(cell).strip().upper() for cell in row] for row in matriz]
        self.filas = len(self.matriz)
        self.columnas = len(self.matriz[0]) if self.filas > 0 else 0

    def buscar_palabra(self, palabra):
        # Buscar en todas las direcciones
        for i in range(self.filas):
            for j in range(self.columnas):
                if self._buscar_desde(i, j, palabra.texto):
                    palabra.ubicacion = (i+1, j+1)  # +1 para que sea 1-indexado como Excel
                    return True
        return False

    def _buscar_desde(self, fila, col, palabra):
        # Todas las direcciones posibles: horizontal, vertical, diagonal y sus inversas
        direcciones = [
            (0, 1),   # derecha
            (0, -1),  # izquierda
            (1, 0),   # abajo
            (-1, 0),  # arriba
            (1, 1),   # diagonal abajo-derecha
            (1, -1),  # diagonal abajo-izquierda
            (-1, 1),  # diagonal arriba-derecha
            (-1, -1)  # diagonal arriba-izquierda
        ]
        
        for df, dc in direcciones:
            encontrado = True
            for k in range(len(palabra)):
                nf, nc = fila + df*k, col + dc*k
                if nf < 0 or nf >= self.filas or nc < 0 or nc >= self.columnas or self.matriz[nf][nc] != palabra[k]:
                    encontrado = False
                    break
            if encontrado:
                return True
        return False

def main():
    # Leer el archivo Excel
    archivo = "archivoExcel/Examen2Excel.xlsx"
    sopa_df = pd.read_excel(archivo, sheet_name="Sopa", header=None)
    palabras_df = pd.read_excel(archivo, sheet_name="Palabras", header=None)

    # Convertir la sopa a matriz y las palabras a lista
    matriz = sopa_df.fillna('').values.tolist()
    palabras_lista = palabras_df.iloc[0,0].split()  # Todas las palabras están en la primera celda

    # Crear objetos
    sopa = SopaDeLetras(matriz)
    palabras = [Palabra(p) for p in palabras_lista]

    # Buscar palabras
    for palabra in palabras:
        if sopa.buscar_palabra(palabra):
            print(f"{palabra.texto}: encontrada en FILA {palabra.ubicacion[0]}, COLUMNA {palabra.ubicacion[1]}")
        else:
            print(f"{palabra.texto}: NO encontrada")

if __name__ == "__main__":
    main()
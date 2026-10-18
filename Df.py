import pandas as pd

# Tengo problemas con el dataset, por que cada columna debe de contener el mismo numero de filas.
datos = {
    "producto": [
        "Cuaderno", "lapicera", "mochila", "Regla", "Cartuchera",
        "Calculadora", "Auriculares", "Resaltadores", "Goma",
        "Lapiz"
    ],
    "categoria": [
        "Libreria", "libreria", "Accesorios", " Libreria",
        "accesorios",
        "Tecnologia", "tecnologia", "Libreria ", "Indumentaria", " libreria "
    ],
    "precio": [1500, 800, 4500, 600, 2800, 12000, 15000, 3200, 400, 500],
    "cantidad_vendida": [2, 4, 7-12, 15, 25, 5, 30, 12, 4, 22],
    "sucursal": [
        "Centro", "Centro", "Norte", "Sur", "Norte",
        "Centro", "Sur", "Centro", "Sur", "Centro"
    ],
    "forma_pago": [
        "Efectivo", "debito", "Credito", "Efectivo", "Debito",
        "credito", "Credito", "Debito", "Efectivo", "debito"
    ],
    "fecha": [
        "2024-03-01", "2024-03-01", "2024-03-02", "2024-03-02",
        "2024-03-03",
        "2024-03-03", "2024-03-04", "2024-03-04", "2024-03-05",
        "2024-03-05"
    ]
}

df = pd.DataFrame(datos)
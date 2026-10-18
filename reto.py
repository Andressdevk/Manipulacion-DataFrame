import pandas as pd
from Df import df

reemplazos_categoria = {
    'libreria': 'Libreria',
    'accesorios': 'Accesorios',
    'tecnologia': 'Tecnologia',
    'indumentaria': 'Indumentaria'
}

df['categoria_limpia'] = (
    df['categoria'].str.strip().str.lower().replace(reemplazos_categoria)
)


# Normalización
df['forma_pago'] = df['forma_pago'].str.strip().str.lower()

print(df)

# filtrado compuesto
condicion = (
    (df['categoria_limpia'] == 'Libreria') &
    (df['forma_pago'] == 'debito') &
    (df['cantidad_vendida'] >= 20)
)

df_filtrado = df[condicion]

# Proyeccion tabular
resultado_final = df_filtrado[['producto', 'precio', 'sucursal']]


# Auditoria de Dimensiones

print("RESULTADO FINAL")
print(resultado_final)

print(f"Tipo de objeto: {type(resultado_final)}")
print(f"Dimensiones : {resultado_final.shape}")





import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("ventas_productos.csv")
df.head()

df['Precio_total'] = df['Cantidad'] * df['Precio']
df.head()
plt.bar (df ['Producto' ], df ['Precio_total'])
plt.xlabel ('Producto')
plt.ylabel ('Precio total')
plt. title ('Precio Total por Producto')
plt.savefig ('grafico precios.png') # Guardar el gráfico como PNG
plt.show ()


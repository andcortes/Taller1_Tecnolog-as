import json

with open('data.json', 'r') as file:
    data = json.load(file)

print(data)

import csv

import csv
import json

IVA = 1.21

with open('data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# 1. Gasto total por usuario
gasto = {u: round(sum(c['precio'] for c in compras), 2) for u, compras in data.items()}

print("1. GASTO TOTAL POR USUARIO")
for usuario, total in gasto.items():
    print(f"   {usuario}: {total:.2f} €")

# 2. Cliente VIP
vip = max(gasto, key=gasto.get)
print(f"\n2. CLIENTE VIP: {vip} con {gasto[vip]:.2f} €")

# 3. Cliente con más artículos
articulos = {u: len(compras) for u, compras in data.items()}
mas_art = max(articulos, key=articulos.get)
print(f"\n3. MÁS ARTÍCULOS: {mas_art} con {articulos[mas_art]} productos")

# 4. Producto más caro y más barato (con el usuario que lo compró)
todas = [(u, c) for u, compras in data.items() for c in compras]
u_caro, caro = max(todas, key=lambda x: x[1]['precio'])
u_barato, barato = min(todas, key=lambda x: x[1]['precio'])
print("\n4. PRODUCTO MÁS CARO Y MÁS BARATO")
print(f"   Más caro:   {caro['producto']} - {caro['precio']:.2f} € (comprado por {u_caro})")
print(f"   Más barato: {barato['producto']} - {barato['precio']:.2f} € (comprado por {u_barato})")

# 5. Resumen por categorías
categorias = {}
for _, c in todas:
    categorias[c['categoria']] = categorias.get(c['categoria'], 0) + c['precio']
categorias = {k: round(v, 2) for k, v in categorias.items()}
print("\n5. RESUMEN POR CATEGORÍAS")
print(f"   {categorias}")

# 6. Atributo precioIVA
for _, c in todas:
    c['precioIVA'] = round(c['precio'] * IVA, 2)
print("\n6. PRODUCTOS CON IVA")
for u, c in todas:
    print(f"   {u}: {c['producto']} -> {c['precio']:.2f} € / {c['precioIVA']:.2f} € con IVA")

# 7. CSV: producto, precioIVA
with open('contabilidad_a.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['producto', 'precioIVA'])
    for _, c in todas:
        writer.writerow([c['producto'], c['precioIVA']])
print("\n7. Fichero 'contabilidad_a.csv' creado.")

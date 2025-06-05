import tkinter as tk
from tkinter import messagebox, ttk
from operaciones import agregar_producto, calcular_total
from excepciones import manejar_error
from productos import productos, historial_ventas

# Lista de productos seleccionados 
productos_seleccionados = []

def actualizar_lista():
    for row in  treeview_seleccionados.get_children():
        treeview_seleccionados.delete(row)
    for producto in productos_seleccionados:
        treeview_seleccionados.insert("","end", values=(producto['nombre'], f"${producto['precio']:.2f}"))
    total = calcular_total(productos_seleccionados)
    etiqueta_total.config(text=f"Total: ${total:.2f}")
    
def finalizar_compra():
    total = calcular_total(productos_seleccionados)
    recibo_texto = "RECIBO DE COMPRA\n\n"
    recibo_texto = "-"*30 + "\n"
    for producto in productos_seleccionados:
        recibo_texto += f"{producto['nombre']} - ${producto['precio']:.2f}\n"
    
    # Agregar al historial de ventas
    for producto in productos_seleccionados:
        historial_ventas.append({
            "producto":producto['nombre'],
            "cantidad":1,
            "precio_total":producto['precio']
        }) 
        
    recibo_texto += "-"* 30 + "\n"
    recibo_texto += f"Total: ${total:.2f}"
    recibo_texto += "-"* 30
    messagebox.showinfo("Recibo de Compra", recibo_texto)
    
    # Limpiar lista de productos seleccionados 
    productos_seleccionados.clear()
    actualizar_lista()
    
def mostrar_historial():
    historial_ventas = tk.Toplevel(ventana)
    historial_ventas.title("Historial de Ventas")
    
    treeview_historial = ttk.Treeview(historial_ventas, columns=("Producto", "Cantidad", "Precio Total"), show="headings", height=10)
    treeview_historial.heading("Producto", text="Producto")
    treeview_historial.heading("Cantidad", text="Cantidad")
    treeview_historial.heading("Precio Total", text="Precio Total")
    treeview_historial.heading("Producto", width=200)
    treeview_historial.heading("Cantidad", width=100)
    treeview_historial.heading("Precio Total", width=150)
    
    # Insertar las ventas al Treeview
    for venta in historial_ventas:
        treeview_historial.insert("", "end", values=(venta["producto"], venta["cantidad"], f"${venta["precio_total"]:.2f}"))
    
    treeview_historial.pack(padx=20, pady=20)
    
    # Mostrar las ganancias totales
    ganancias_totales = sum(venta["precio_total"] for venta in historial_ventas)
    etiqueta_ganancias = tk.Label(historial_ventas, text=f"Ganancias Totales: ${ganancias_totales:2f}", font=("Arial", 14, "bold"))
    etiqueta_ganancias.pack(pady=10)
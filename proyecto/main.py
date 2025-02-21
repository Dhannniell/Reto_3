import  tkinter as tk
from tkinter import messagebox, ttk
from operaciones import agregar_producto, calcular_total
from excepciones import manejar_error
from productos import productos, historial_ventas 

#Lista de productos seleccionados 
productos_seleccionados = []

def agregar_desde_lista():
    try:
        selected_item = treeview_productos.selection()
        if not selected_item:
            raise ValueError("Debe seleccionar un producto de la lista")
        
        id_producto = selected_item[0]
        
        if not id_producto.isdigit() or int(id_producto) not in producto:
            raise ValueError("ID de producto no es valido.")
        
        cantidad = int(entry_cantidad.get())
        
        producto = productos[int(id_producto)]
        cantidad_diponible = 100
        if cantidad > cantidad_diponible:
            raise ValueError("No hay suficiente cantidad disponible")
        
        agregar_producto(int(id_producto), cantidad, productos_seleccionados)
        
        
    except

def actualizar_lista():
    for row in treeview_seleccionados.get_children():
        treeview_seleccionados.delete(row)
    for producto in productos_seleccionados:
        treeview_seleccionados.insert("", "end", values=(producto['nombre'], f"${producto['precio']:.2f}"))
    total = calcular_total(productos_seleccionados)
    etiqueta_total.config(text=f"Total: ${total:.2f}")
    
    
def finalizar_compra():
    total = calcular_total(productos_seleccionados)
    recibo_texto = "RECIBO DE COMPRA \n\n"
    recibo_texto += "-"*30 + "\n"
    for producto in productos_seleccionados:
        recibo_texto += f"{producto['nombre']} - ${producto['precio']:.2f}\n"
        
        
        # Agregar al historial de ventas 
        for producto in productos_seleccionados:
            historial_ventas.append({
                "producto": producto['nombre'],
                "cantidad": 1,
                "precio_total": producto['precio']
            })
    
    recibo_texto += "-"*30 + "\n"
    recibo_texto += f"Total: ${total:.2f}\n"
    recibo_texto += "-" * 30
    messagebox.showinfo("recibo de Compra", recibo_texto)
    
    #Limpiar lista de productos seleccionados 
    productos_seleccionados.clear()
    actualizar_lista()
    
def mostrar_historial():
    historial_ventas = tk.Toplevel(ventana)
    historial_ventas.title("Historial de Ventas.")
    
    treeview_historial = ttk.Treeview(historial_ventas, columns=("Producto", "Cantidad", "Precio Total"), show= "heading", height=10)
    treeview_historial.heading("Proyecto", text="Producto")
    treeview_historial.heading("Cantidad", text="Cantidad")
    treeview_historial.heading("Precio Total", text="Precio Total")
    treeview_historial.heading("Producto", width=200)
    treeview_historial.heading("Cantidad", width=100)
    treeview_historial.heading("Precio Total", width=150)
    
    #Insertar las ventas al Treeview
    for venta in historial_ventas:
        treeview_historial.insert("", "end", values=(venta["producto"], venta["cantidad"], f"${venta["precio_total"]:.2f}"))
        
    treeview_historial.pack(padx=20, pady=20)
    
    #Mostrar las ganancias totales
    ganancias_totales = sum(venta["precio_total"] for venta in historial_ventas)
    etiqueta_ganacias = tk.Label(historial_ventas, text=f"Ganacias Totales: ${ganancias_totales:.2f}", font=("Arial", 14, "bold"))
    etiqueta_ganacias.pack(pady=10)
    
    
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
        
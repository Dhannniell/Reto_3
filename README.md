README - Sistema de Caja Registradora para Tienda Fruver
Descripción General
Este proyecto es un sistema de caja registradora desarrollado en Python con interfaz gráfica (Tkinter) para una tienda de frutas y verduras (Fruver). Permite gestionar ventas, calcular totales y mantener un historial de transacciones.

Estructura del Proyecto
El sistema está organizado en módulos siguiendo el principio de separación de responsabilidades:

text
caja_registradora/
├── main/                 # Interfaz gráfica y lógica principal
│   └── main.py
├── excepciones/          # Manejo de errores
│   └── excepciones.py
├── operaciones/          # Lógica de negocio
│   └── operaciones.py
└── productos/           # Datos y operaciones de productos
    └── productos.py
Módulos Principales
1. main.py (Interfaz Gráfica)
Responsabilidad: Interfaz de usuario y coordinación general

Características:

Interfaz con Tkinter para selección de productos

Visualización de productos disponibles

Gestión de productos seleccionados

Finalización de compras y generación de recibos

Visualización de historial de ventas

2. productos.py (Modelo de Datos)
Responsabilidad: Almacenamiento y acceso a datos de productos

Características:

Diccionario con datos de productos (nombre, precio, stock)

Lista para historial de ventas

Funciones para obtener productos por ID

Funciones para agregar ventas al historial

3. operaciones.py (Lógica de Negocio)
Responsabilidad: Cálculos y operaciones clave

Funciones:

calcular_total(): Suma los precios de productos seleccionados

agregar_producto_historial_ventas(): Añade productos a la lista de compra

4. excepciones.py (Manejo de Errores)
Responsabilidad: Gestión centralizada de errores

Función:

manejar_error(): Muestra mensajes de error al usuario

Cómo Utilizar el Sistema
Requisitos
Python 3.6+

Tkinter (generalmente incluido con Python)

Instrucciones de Uso
Ejecutar el archivo main.py:

bash
python main/main.py
Interfaz principal:

Panel izquierdo: Lista de productos disponibles

Panel central: Campo para ingresar cantidad y botón "Agregar Producto"

Panel derecho: Lista de productos seleccionados y total

Panel inferior: Botones para finalizar compra y ver historial

Flujo de trabajo:

Seleccionar un producto de la lista

Ingresar la cantidad deseada

Hacer clic en "Agregar Producto"

Repetir para todos los productos deseados

Finalizar la compra con el botón correspondiente

Ver historial de ventas cuando sea necesario
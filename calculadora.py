import json
import os
import matplotlib.pyplot as plt
import numpy as np
import customtkinter as ctk
from tkinter import messagebox, StringVar
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
import random

# Diccionario global para almacenar las entradas de la interfaz
entradas = {}

def crearEstructura():
    """
    Crea la estructura de carpetas y archivos si no existen.

    Esta función crea las carpetas necesarias para almacenar los datos y los archivos de salida.
    Si no existe el archivo "output/reporte_empresa.pdf", también lo crea.
    """
    estructura = ["data", "output"]
    for carpeta in estructura:
        os.makedirs(carpeta, exist_ok=True)
    if not os.path.exists("output/reporte_empresa.pdf"):
        open("output/reporte_empresa.pdf", "w").close()

def calcularImpacto(datos):
    """
    Calcula la huella de carbono de una empresa con fórmulas más precisas.

    Args:
        datos (dict): Diccionario con los datos de la empresa, como consumo energético, agua, residuos, etc.

    Returns:
        dict: Diccionario con el impacto ambiental calculado para cada categoría y el total.
    """
    factores = {
        "energia": 0.4,
        "agua": 0.25,
        "residuos": 1.5,
        "combustibles": 2.8,
        "materiales": 1.6
    }

    factores_transporte = {
        "Carretera": 0.15,
        "Marítimo": 0.05,
        "Aéreo": 0.5
    }

    impacto = {k: datos[k] * factores.get(k, 1) for k in datos if
               k not in ["nombre_empresa", "tipo_transporte", "transporte"]}

    tipo_transporte = datos["tipo_transporte"].lower()
    if tipo_transporte in factores_transporte:
        impacto["transporte"] = datos["transporte"] * factores_transporte[tipo_transporte]
    else:
        impacto["transporte"] = 0  # Si el tipo de transporte no está definido

    impacto["total"] = sum(impacto.values())
    return impacto

def generarSugerencias(datos, impacto):
    """
    Genera sugerencias personalizadas basadas en los datos del usuario.

    Args:
        datos (dict): Datos ingresados por el usuario.
        impacto (dict): Resultados del impacto ambiental calculado.

    Returns:
        list: Lista con sugerencias para reducir el impacto ambiental.
    """
    sugerencias = []
    if datos["energia"] > 50000:
        sugerencias.append("Reducir el consumo de energía implementando eficiencia energética y fuentes renovables.")
    if datos["agua"] > 100000:
        sugerencias.append("Optimizar el uso del agua con reciclaje y recolección de aguas pluviales.")
    if datos["residuos"] > 15000:
        sugerencias.append("Implementar programas de reducción de residuos y reciclaje.")
    if datos["combustibles"] > 100000:
        sugerencias.append("Explorar alternativas a combustibles fósiles, como biocombustibles o hidrógeno.")
    if datos["materiales"] > 50000:
        sugerencias.append("Revisar la cadena de suministro para utilizar materiales reciclados o biodegradables.")
    if datos["transporte"] > 200000:
        sugerencias.append(f"Optimizar la logística y considerar transporte {datos['tipo_transporte']} con menor impacto.")
    if not sugerencias:
        sugerencias.append("Se recomienda una auditoría ambiental para identificar oportunidades de mejora.")
    return sugerencias

def generarGrafico(datos, impacto):
    """
    Genera un gráfico del impacto ambiental y lo guarda como imagen.

    Args:
        datos (dict): Datos de la empresa.
        impacto (dict): Resultados del impacto ambiental calculado.
    """
    categorias = list(impacto.keys())[:-1]
    valores = [impacto[c] for c in categorias]

    plt.figure(figsize=(8, 5))
    plt.barh(categorias, valores, color=["#4CAF50", "#03A9F4", "#FF9800", "#8BC34A", "#FF5722", "#9C27B0"])
    plt.xlabel("kg CO₂")
    plt.ylabel("Categoría")
    plt.title(f"Impacto Ambiental de {datos['nombre_empresa']}")
    plt.savefig("output/grafico_impacto.png")
    plt.close()

def generarReportePDF(datos, impacto, sugerencias):
    """
    Genera un reporte en PDF con los resultados, gráfico y recomendaciones.

    Args:
        datos (dict): Datos de la empresa.
        impacto (dict): Resultados del impacto ambiental calculado.
        sugerencias (list): Sugerencias para reducir el impacto ambiental.
    """
    ruta_pdf = "output/reporte_empresa.pdf"
    doc = SimpleDocTemplate(ruta_pdf, pagesize=letter)
    styles = getSampleStyleSheet()
    elementos = []

    elementos.append(Paragraph(f"<b>Reporte de Impacto Ambiental</b>", styles["Title"]))
    elementos.append(Spacer(1, 12))
    elementos.append(Paragraph(f"<b>Empresa:</b> {datos['nombre_empresa']}", styles["Normal"]))
    elementos.append(Spacer(1, 12))

    data = [["Categoría", "Impacto (kg CO2)"]]
    for key, value in impacto.items():
        data.append([key.capitalize(), f"{value:.2f}"])

    tabla = Table(data)
    tabla.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))

    elementos.append(tabla)
    elementos.append(Spacer(1, 12))

    elementos.append(Paragraph("<b>Sugerencias para Reducir el Impacto:</b>", styles["Heading2"]))
    for sugerencia in sugerencias:
        elementos.append(Paragraph(f"- {sugerencia}", styles["Normal"]))
    elementos.append(Spacer(1, 12))

    elementos.append(Image("output/grafico_impacto.png", width=400, height=300))
    doc.build(elementos)

def calcular():
    """
    Función que gestiona el cálculo del impacto ambiental al recibir los datos desde la interfaz gráfica.

    Toma los datos de la interfaz, calcula el impacto, genera sugerencias, grafica el impacto y crea el reporte PDF.
    """
    datos = {
        campo: float(entradas[campo].get()) if campo != "nombre_empresa" and campo != "tipo_transporte" else entradas[
            campo].get() for campo in entradas}
    impacto = calcularImpacto(datos)
    sugerencias = generarSugerencias(datos, impacto)
    generarGrafico(datos, impacto)
    generarReportePDF(datos, impacto, sugerencias)
    messagebox.showinfo("Éxito", "Cálculo completado y reporte generado en output/reporte_empresa.pdf")

def ejecutar_interfaz():
    """
    Inicia la interfaz gráfica del programa, permitiendo al usuario ingresar los datos y ver los resultados.

    Crea una ventana con campos de entrada para cada dato necesario y un botón para ejecutar el cálculo.
    """
    global entradas
    ventana = ctk.CTk()
    ventana.title("Calculadora de Impacto Ambiental")
    ventana.geometry("700x800")

    etiquetas = {
        "nombre_empresa": "Nombre de la empresa:",
        "energia": "Consumo energético (kWh):",
        "agua": "Consumo de agua (m³):",
        "residuos": "Residuos generados (toneladas):",
        "transporte": "Distancia logística (km):",
        "tipo_transporte": "Tipo de transporte:",
        "combustibles": "Combustibles utilizados (litros):",
        "materiales": "Materiales empleados (toneladas):"
    }

    for campo, texto in etiquetas.items():
        ctk.CTkLabel(ventana, text=texto).pack()
        if campo == "tipo_transporte":
            tipo_transporte_var = StringVar()
            entradas[campo] = ctk.CTkComboBox(ventana, values=["Carretera", "Marítimo", "Aéreo"],
                                              variable=tipo_transporte_var, state="readonly")
        else:
            entradas[campo] = ctk.CTkEntry(ventana)
        entradas[campo].pack()

    ctk.CTkButton(ventana, text="Calcular Impacto", command=calcular).pack(pady=10)
    ventana.mainloop()

crearEstructura()
ejecutar_interfaz()

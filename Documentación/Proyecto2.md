# Calculadora de Impacto Ambiental

## Objetivo

Crear un programa sencillo que permita a las empresas calcular y visualizar su impacto ambiental de manera eficaz. El software estará diseñado para medir la huella de carbono y el consumo energético de las actividades de la empresa, proporcionando sugerencias prácticas para reducir el impacto ambiental.

## Alcance

- **Usuarios**: Empresas pequeñas y medianas interesadas en mejorar su sostenibilidad.
- **Características principales**:
  - Cálculo de huella de carbono.
  - Registro del consumo energético.
  - Sugerencias para reducir el impacto.
  - Generación de reportes básicos.

---

## Etapas de Desarrollo

### 1. Planificación

1. **Identificar métricas relevantes**:
   - Huella de carbono (kg CO₂).
   - Consumo energético (kWh).
   - Uso de recursos (agua, papel, etc.) en versiones futuras.
2. **Definir estructura de datos**:
   - Inputs necesarios (ej. cantidad de energía consumida, tipo de transporte utilizado, etc.).
   - Salidas esperadas (ej. gráfico de impacto, lista de sugerencias).

---

### 2. Desarrollo

1. **Interfaz del Usuario (CLI)**:
   - Usar una interfaz por línea de comandos para la versión inicial.
   - Solicitar datos básicos:
     - Consumo energético en kWh.
     - Distancias recorridas en transporte y tipo (ej. avión, coche).
   - Proveer resultados claros y gráficos simples.

2. **Cálculo de Impacto Ambiental**:
   - Fórmulas para calcular huella de carbono:
     - Energía: `kg CO₂ = consumo (kWh) * factor de emisión (kg CO₂/kWh)`.
     - Transporte: `kg CO₂ = distancia (km) * factor de emisión por tipo de transporte`.

3. **Sugerencias Automatizadas**:
   - Generar recomendaciones basadas en los datos ingresados:
     - "Utilizar iluminación LED puede reducir un 20% del consumo energético."
     - "Optar por transporte público puede disminuir el impacto en un 50%."

4. **Generación de Reportes**:
   - Crear un archivo en formato PDF o texto con:
     - Resumen del impacto ambiental.
     - Gráficos de consumo.
     - Lista de recomendaciones.

---

### 3. Pruebas

1. **Pruebas Unitarias**:
   - Validar que los cálculos sean precisos.
   - Verificar que los datos de entrada incorrectos generen errores manejables.
2. **Pruebas de Usuario**:
   - Probar con usuarios reales de empresas pequeñas para garantizar la facilidad de uso.

---

## Tecnologías

1. **Lenguaje de programación**: Python.
2. **Bibliotecas principales**:
   - `pandas`: Para manejar y analizar los datos.
   - `matplotlib`: Para la visualización de gráficos.
   - `fpdf` o `reportlab`: Para la generación de reportes en PDF.

---

## Estructura del Programa

1. **Archivo principal**: `main.py`
   - Controlará el flujo del programa.

2. **Módulos auxiliares**:
   - `calculadora.py`: Para los cálculos de impacto.
   - `sugerencias.py`: Para generar recomendaciones basadas en los datos.
   - `reportes.py`: Para crear los reportes en PDF o texto.

3. **Estructura de carpetas**:
   ```plaintext
   /calculadora_impacto_ambiental
   ├── main.py
   ├── calculadora.py
   ├── sugerencias.py
   ├── reportes.py
   ├── /data
   │   └── factores_emision.json
   └── /output
       └── reportes_generados

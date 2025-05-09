# Devlog: Calculadora de Impacto Ambiental

## Línea Temporal del Desarrollo del Proyecto

### 1. Desarrollo de la lógica de cálculo
En la primera fase, me centré en construir la **lógica de cálculo** de la huella de carbono. Esto incluyó establecer las fórmulas para calcular el impacto ambiental basándome en el consumo de energía, agua, residuos y el tipo de transporte. Se definieron los factores de emisión para cada categoría y se ajustaron según la naturaleza de los datos ingresados por el usuario.

### 2. Generación del PDF e informes
Una vez la lógica estuvo lista, implementé la capacidad para **generar reportes en PDF**. Utilicé **reportlab** para crear un documento que incluyera los resultados del cálculo del impacto ambiental. Además, se añadió un gráfico con **matplotlib** para mostrar visualmente el impacto, lo que mejoró la comprensión del resultado por parte del usuario.

### 3. Interfaz gráfica de usuario
Finalmente, me enfoqué en la **interfaz gráfica** utilizando **customtkinter**. Desarrollé una interfaz amigable donde los usuarios podían ingresar los datos necesarios de forma intuitiva, ver los resultados de los cálculos y generar los informes con un solo clic. La interfaz también incluía un sistema de validación para asegurar que los datos ingresados fueran correctos.

# Preguntas de evaluación

## ¿Cómo se gestionan los datos desde su generación hasta su eliminación en tu proyecto?

**En nuestro proyecto, la gestión de datos sigue un flujo bien definido, desde su generación hasta su almacenamiento y eliminación. Este proceso garantiza la integridad y consistencia de la información en todas las etapas.**

1. Generación y Captura de Datos

Los datos son ingresados por el usuario a través de una interfaz gráfica basada en CustomTkinter. Se recopilan valores clave 
como el consumo de energía, agua, residuos, combustibles y materiales, así como el tipo de transporte utilizado. 
La información se almacena temporalmente en un diccionario en memoria (entradas), lo que permite su procesamiento inmediato.

2. Procesamiento y Cálculo del Impacto Ambiental

Una vez capturados, los datos son utilizados para calcular la huella de carbono de la empresa a través de la función calcularImpacto(). 
Para ello, se aplican factores de conversión predefinidos, diferenciando categorías como energía, transporte y residuos. 
En el caso del transporte, se adapta el cálculo según el medio utilizado (terrestre, marítimo o aéreo), asegurando una conversión adecuada.

3. Visualización y Reporte de Datos

Los resultados obtenidos se presentan de dos maneras:

- Gráfico de barras: generado con matplotlib, el cual muestra el impacto ambiental por categoría.
- Reporte en PDF: estructurado mediante reportlab, incluyendo los datos de entrada, el cálculo del impacto y recomendaciones personalizadas.
Ambos elementos se guardan en la carpeta output/, asegurando su disponibilidad para consulta posterior.

4. Almacenamiento y Mantenimiento de Datos

Para garantizar la persistencia de los resultados:

- Se crea un directorio output/ si no existe, utilizando la función crearEstructura().
- El archivo PDF (reporte_empresa.pdf) es sobreescrito en cada ejecución, evitando la acumulación de archivos innecesarios.

## ¿Qué estrategia sigues para garantizar la consistencia e integridad de los datos?

1. Estrategias para Garantizar la Consistencia e Integridad de los Datos

Para mantener la fiabilidad de los datos, se aplican las siguientes estrategias:

- Validación de entradas: Se filtran valores inválidos y se convierte el formato adecuado para cada campo.
- Gestión de archivos: Se verifica la existencia de directorios antes de generar archivos nuevos.
- Consistencia en los cálculos: Se aplican factores de conversión estándar para evitar discrepancias en los resultados.
- Estructura organizada: Se diferencian claramente los datos de entrada, los cálculos y los resultados generados.

## ¿Qué alternativas consideraste para almacenar datos y por qué elegiste tu solución actual?

En el proyecto, se optó por almacenar los datos en archivos PDF e imágenes generadas con reportlab y matplotlib, en lugar de utilizar bases de datos o archivos JSON.

Razón por la que es una buena opción:

1. Presentación clara y estructurada → Permite generar un reporte final con toda la información calculada, gráficos y sugerencias en un formato profesional.
2. Fácil de compartir → Los reportes en PDF pueden enviarse o imprimirse sin necesidad de herramientas adicionales.
3. No requiere almacenamiento permanente → Como el propósito del sistema es generar análisis en tiempo real, no se necesita una base de datos compleja para guardar registros históricos.
4. Automatización y eficiencia → La generación automática de reportes facilita el acceso inmediato a los resultados sin requerir una estructura de almacenamiento adicional.

## Si no usas la nube, ¿cómo podrías integrarla en futuras versiones?

Se podría integrar la nube en futuras versiones subiendo los reportes a Google Drive, OneDrive o Amazon S3 mediante sus APIs. 
También se podría usar Firebase o una base de datos en la nube como PostgreSQL en AWS para almacenar los datos y permitir consultas históricas. 
Esto facilitaría el acceso desde cualquier dispositivo y mejoraría la gestión de la información.

## Si no implementaste medidas de seguridad, ¿qué riesgos potenciales identificas y cómo los abordarías en el futuro?

Al no contar con medidas de seguridad avanzadas, se identifican los siguientes riesgos potenciales y formas de abordarlos en futuras versiones:

🔴 Ingreso de datos inválidos → Actualmente, no se validan valores negativos o vacíos. Se podría agregar validación estricta y manejo de errores con try-except.

🔴 Pérdida o sobrescritura de archivos → Los reportes se generan en la misma ubicación, sobrescribiendo archivos previos. Se podría implementar versionado de reportes o una confirmación antes de sobrescribir.

🔴 Acceso no autorizado en la nube (si se integra en el futuro) → Se podrían usar credenciales seguras y cifrado para proteger los datos al almacenarlos en servicios en la nube.

Implementando estas mejoras, se garantizaría mayor seguridad en la manipulación y almacenamiento de datos.

## ¿Qué impacto tendría tu software en un entorno de negocio o en una planta industrial?

El software ayudaría a empresas y plantas industriales a evaluar su impacto ambiental de manera rápida y visual, permitiendo tomar decisiones para reducir su huella de carbono.

✅ Optimización de recursos → Facilita la identificación de áreas con alto consumo de energía, agua o materiales, mejorando la eficiencia.

✅ Cumplimiento normativo → Ayuda a documentar el impacto ambiental para cumplir con regulaciones y auditorías ambientales.

✅ Toma de decisiones estratégicas → Permite a gerentes y responsables ambientales implementar medidas sostenibles basadas en datos concretos.

## ¿Cómo crees que tu solución podría mejorar procesos operativos o la toma de decisiones?

Mi solución podría mejorar los procesos operativos y la toma de decisiones en una empresa o planta industrial al proporcionar datos precisos sobre el impacto ambiental.

✅ Optimización del uso de recursos → Identifica áreas con alto consumo de energía, agua o materiales, permitiendo reducir costos y desperdicios.

✅ Decisiones basadas en datos → Ofrece reportes detallados con gráficos y sugerencias, facilitando la implementación de estrategias sostenibles.

✅ Cumplimiento de normativas ambientales → Ayuda a documentar el impacto ambiental para auditorías y certificaciones.

Esto permitiría a las empresas mejorar su eficiencia, reducir costos y fortalecer su compromiso con la sostenibilidad.

## ¿Cómo puede tu software facilitar la integración entre entornos IT y OT?

Mi software puede facilitar la integración entre entornos IT (Tecnología de la Información) y OT (Tecnología Operativa) al permitir que los datos ambientales de la planta industrial sean procesados y visualizados en reportes accesibles desde el ámbito IT.

✅ Recopilación y procesamiento de datos → Puede recibir datos de sensores o sistemas OT sobre consumo de energía, agua y emisiones, y analizarlos en tiempo real.

✅ Generación de reportes automatizados → Transforma los datos operativos en informes claros y gráficos que pueden ser utilizados por gerentes y equipos de IT para la toma de decisiones.

✅ Accesibilidad y compatibilidad → Puede integrarse con bases de datos industriales o plataformas en la nube para que la información fluya entre OT e IT sin fricciones.

Esta integración permitiría a las empresas mejorar su eficiencia operativa y tomar decisiones basadas en datos en tiempo real.

## ¿Qué procesos específicos podrían beneficiarse de tu solución en términos de automatización o eficiencia?

Mi solución puede mejorar varios procesos específicos en términos de automatización y eficiencia, especialmente en empresas y plantas industriales:

✅ Monitoreo del consumo de recursos → Automatiza el cálculo del impacto ambiental a partir de datos de energía, agua y materiales, reduciendo el tiempo y errores en análisis manuales.

✅ Generación de reportes ambientales → Crea informes en PDF con gráficos y sugerencias automáticamente, eliminando la necesidad de realizar cálculos y reportes manuales.

✅ Optimización de logística y transporte → Evalúa el impacto del transporte según su tipo y distancia, ayudando a mejorar rutas y reducir emisiones.

✅ Gestión de cumplimiento normativo → Facilita la documentación de huella de carbono para auditorías y certificaciones ambientales sin intervención manual constante.

Estos procesos se benefician al reducir el esfuerzo humano, minimizar errores y mejorar la toma de decisiones basada en datos confiables.

## Si no has utilizado THD, ¿cómo podrías implementarlas para enriquecer tu solución?

Para enriquecer mi solución con Tecnologías Habilitadoras Digitales (THD), se podrían implementar las siguientes mejoras:

🔹 IoT (Internet de las Cosas) → Integrar sensores que midan en tiempo real el consumo de energía, agua y emisiones, automatizando la captura de datos.

🔹 Cloud Computing → Almacenar reportes en la nube (Google Drive, AWS o Firebase) para permitir el acceso remoto y el análisis centralizado de la información.

🔹 Big Data y Analítica → Guardar registros históricos y aplicar análisis predictivo para identificar patrones de consumo y proponer mejoras operativas.

🔹 Inteligencia Artificial → Implementar modelos que generen recomendaciones optimizadas basadas en el impacto ambiental detectado.

Estas tecnologías mejorarían la precisión, escalabilidad y automatización del software, facilitando su integración en entornos industriales avanzados.








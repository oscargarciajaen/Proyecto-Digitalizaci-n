# Environmental Impact Calculator

## Features
- **Carbon Footprint Calculation**: Calculates CO₂ emissions based on energy consumption, water usage, waste production, and transportation.
- **Sustainability Suggestions**: Provides tailored suggestions for reducing environmental impact.
- **PDF Report Generation**: Automatically generates a detailed report in PDF format, including calculated impact and suggestions for improvement.
- **Graphical Visualization**: Displays a bar chart visualizing the environmental impact across different categories.

## Technologies Used
- **Python 3.8**
- **CustomTkinter** for GUI
- **Matplotlib** for graph generation
- **ReportLab** for PDF report generation

## Setup Instructions

### Requirements
Before running the program, make sure you have the following installed:
- **Python 3.8+** 
- The required Python libraries (you can install them using `pip`):
    ```bash
    pip install matplotlib numpy customtkinter reportlab
    ```

### Download or Copy the Code

Save the code in a file called `calculadora.py`.

### Running the Program

1. **Open a terminal or command prompt** in the folder where you saved the file and run the following command:
    ```bash
    python calculadora.py
    ```

2. **Using the Graphical Interface**:
    - A window will open where you can input your company's data:
        - Energy consumption (kWh)
        - Water consumption (m³)
        - Waste generated (tons)
        - Transportation distance (km)
    - Select the type of transport used.
    - Click "Calculate Impact" to generate the results.
    - The program will create a PDF report and a graphical representation of the impact in the `output/` folder.

### Example Output
- A **PDF Report** with all the details of your company’s environmental impact.
    - [Example PDF Report](../output/reporte_empresa.pdf)
- A **Graph** of the environmental impact.
    - [Example Graph](../output/grafico_impacto.png)


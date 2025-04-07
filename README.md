# Procesamiento de Transacciones Bancarias (CLI)

## Introducción

Este proyecto es una aplicación de línea de comandos (CLI) que procesa un archivo CSV con transacciones bancarias y genera un reporte.

El propósito de esta aplicación es proporcionar una herramienta simple pero efectiva para analizar transacciones bancarias y obtener información útil como el balance final, la transacción de mayor monto y el conteo de transacciones por tipo.

## Características Principales

- **Cálculo de Balance**: Calcula el balance final considerando créditos y débitos.
- **Identificación de Transacción Mayor**: Encuentra la transacción con el monto más alto.
- **Conteo de Transacciones**: Cuenta el número de transacciones por tipo.
- **Manejo de Errores**: Proporciona mensajes de error claros para problemas comunes.
- **Interfaz CLI Amigable**: Interfaz de línea de comandos fácil de usar.

## Instrucciones de Ejecución

### Requisitos Previos

- Python 3.8 o superior
- Pip (gestor de paquetes de Python)

### Instalación de Dependencias

```bash
# Clonar el repositorio
git clone https://github.com/psaraviaq/interbank-academy-25.git
cd interbank-academy-25

# Crear un entorno virtual (opcional pero recomendado)
python -m venv .venv
source .venv/Scripts/activate  # En Linux: .venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt
```

### Ejecución de la Aplicación

```bash
# Ejecutar la aplicación con un archivo CSV
python main.py ruta/al/archivo.csv

# Ejemplo con el archivo de prueba incluido
python main.py data.csv
```

## Enfoque y Solución

### Arquitectura

La aplicación está diseñada siguiendo los principios de Clean Architecture, lo que permite una clara separación de responsabilidades y facilita el mantenimiento y la extensión del código.

1. **Capa de Dominio (Domain Layer)**: Contiene las entidades y reglas de negocio centrales.
   - Modelos: Representación de las transacciones bancarias.
   - Enumeraciones: Tipos de transacciones (Crédito, Débito).

2. **Capa de Aplicación (Application Layer)**: Contiene la lógica de aplicación y casos de uso.
   - Servicios: Procesamiento de transacciones y cálculos.

3. **Capa de Infraestructura (Infrastructure Layer)**: Maneja la interacción con recursos externos.
   - Lectura de archivos CSV: Carga de datos de transacciones.

4. **Capa de Presentación (Presentation Layer)**: Maneja la interacción con el usuario.
   - CLI: Interfaz de línea de comandos para recibir argumentos y mostrar resultados.
  
![structurizr-1-Diagram2](https://github.com/user-attachments/assets/6ecc3152-cb17-4e6c-ac83-3bf08b4e02d3)

### Decisiones de Diseño

- **Manejo de Errores**: Implementación de manejo de errores robusto para proporcionar mensajes claros al usuario.
- **Testabilidad**: Diseño que facilita la escritura de pruebas unitarias para cada componente.
- **Extensibilidad**: Arquitectura que permite agregar nuevas funcionalidades con cambios mínimos en el código existente.

## Estructura del Proyecto

```
interbank-academy-25/
│
├── domain/                           # Capa de dominio
│   ├── models/                       # Modelos de dominio
│   │   └── Transaction.py            # Clase Transaction
│   └── enums/                        # Enumeraciones
│       └── TransactionType.py        # Enum TransactionType
│
├── application/                      # Capa de aplicación
│   └── services/                     # Servicios de aplicación
│       └── TransactionService.py     # Servicio para procesar transacciones
│
├── infrastructure/                   # Capa de infraestructura
│   └── data/                         # Acceso a datos
│       └── csv_reader.py             # Lectura de archivos CSV
│
├── presentation/                     # Capa de presentación
│   └── cli/                          # Interfaz de línea de comandos
│       ├── cli_parser.py             # Parseo de argumentos de línea de comandos
│       └── cli_display.py            # Visualización de resultados
│
├── tests/                            # Pruebas
│   ├── domain/                       # Pruebas de la capa de dominio
│   ├── application/                  # Pruebas de la capa de aplicación
│   └── infrastructure/               # Pruebas de la capa de infraestructura
│
├── main.py                           # Punto de entrada de la aplicación
├── requirements.txt                  # Dependencias del proyecto
└── README.md                         # Documentación del proyecto
```

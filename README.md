# AI Lead Scoring for Startups

Prototipo educativo en Python que demuestra cómo entrenar un modelo Random Forest para ordenar clientes potenciales (*leads*) según su actividad.

## ¿Qué hace?

1. Genera un conjunto de datos **sintéticos** para la demostración.
2. Entrena un clasificador `RandomForestClassifier`.
3. Evalúa el modelo con un conjunto de prueba separado.
4. Calcula una probabilidad estimada de conversión para nuevos leads.
5. Asigna una prioridad demostrativa: Alto, Medio o Bajo.
6. Guarda los resultados en `scored_leads.csv`.

## Variables de entrada

| Variable | Descripción |
|---|---|
| `time_on_platform` | Tiempo en la plataforma, en minutos (según el ejemplo). |
| `clicks` | Número de clics. |
| `visits` | Número de visitas. |

Para entrenar el modelo de demostración se genera además `converted` (0 = no convirtió, 1 = convirtió).

## Requisitos

- Python 3.10 o superior recomendado.
- pandas
- numpy
- scikit-learn

## Instalación

```bash
python -m venv .venv
```

En Windows:

```bash
.venv\Scripts\activate
```

En macOS o Linux:

```bash
source .venv/bin/activate
```

Instala las dependencias:

```bash
pip install -r requirements.txt
```

## Ejecutar la demostración

```bash
python main.py
```

El programa muestra métricas de evaluación, puntúa tres leads de ejemplo y crea `scored_leads.csv`.

## Puntuar leads desde un CSV propio

Crea un archivo CSV con estas columnas:

```csv
lead,time_on_platform,clicks,visits
Lead_001,35,12,7
Lead_002,8,1,1
Lead_003,22,6,3
```

Ejecuta:

```bash
python main.py --csv mis_leads.csv --output resultados.csv
```

## Interpretación de prioridad

- Alto: probabilidad demostrativa igual o superior a 70 %.
- Medio: desde 40 % y menor de 70 %.
- Bajo: menor de 40 %.

Estos umbrales son ilustrativos y deben definirse con criterios de negocio y validación.

## Limitaciones importantes

**Este repositorio es un prototipo educativo.** El modelo se entrena con datos sintéticos generados por reglas simuladas. Por tanto:

- Las probabilidades no representan tasas reales de conversión.
- Las métricas solo evalúan el comportamiento sobre datos simulados.
- No debe utilizarse para decisiones comerciales reales.
- Para producción se necesitan datos históricos legítimos, representativos y suficientes; definición clara de conversión; validación temporal; análisis de sesgos; monitoreo y revisión humana.
- No incluyas datos personales o confidenciales en repositorios públicos.

## Tecnologías

Python · Pandas · NumPy · Scikit-learn · Random Forest

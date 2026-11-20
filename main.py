"""
AI Lead Scoring for Startups
Demo educativo: entrena un Random Forest con datos sintéticos y puntúa nuevos leads.

IMPORTANTE:
- Los datos de entrenamiento son simulados.
- Las probabilidades son demostrativas, no estimaciones comerciales validadas.
- Para uso real, reemplaza los datos sintéticos por datos históricos autorizados
  y valida el modelo antes de tomar decisiones comerciales.
"""

from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    roc_auc_score,
)
from sklearn.model_selection import train_test_split

FEATURES = ["time_on_platform", "clicks", "visits"]
TARGET = "converted"


def create_demo_data(n_rows: int = 1200, random_state: int = 42) -> pd.DataFrame:
    """Crea datos sintéticos reproducibles para demostrar el flujo."""
    rng = np.random.default_rng(random_state)

    time_on_platform = rng.integers(1, 61, size=n_rows)
    clicks = rng.poisson(lam=5, size=n_rows).clip(0, 30)
    visits = rng.poisson(lam=3, size=n_rows).clip(1, 20)

    # Regla simulada: más actividad suele asociarse con mayor probabilidad.
    raw_score = (
        -3.2
        + 0.035 * time_on_platform
        + 0.12 * clicks
        + 0.18 * visits
    )
    probability = 1 / (1 + np.exp(-raw_score))
    converted = rng.binomial(1, probability)

    return pd.DataFrame(
        {
            "time_on_platform": time_on_platform,
            "clicks": clicks,
            "visits": visits,
            "converted": converted,
        }
    )


def train_model(random_state: int = 42):
    """Entrena y evalúa el modelo con datos sintéticos."""
    data = create_demo_data(random_state=random_state)
    X = data[FEATURES]
    y = data[TARGET]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.25,
        random_state=random_state,
        stratify=y,
    )

    model = RandomForestClassifier(
        n_estimators=200,
        max_depth=6,
        min_samples_leaf=4,
        class_weight="balanced",
        random_state=random_state,
    )
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    probabilities = model.predict_proba(X_test)[:, 1]

    print("\n=== Evaluación del modelo (datos simulados) ===")
    print(f"Exactitud: {accuracy_score(y_test, predictions):.3f}")
    try:
        print(f"ROC-AUC:   {roc_auc_score(y_test, probabilities):.3f}")
    except ValueError:
        print("ROC-AUC: no disponible para esta distribución de clases.")
    print("\nInforme de clasificación:")
    print(classification_report(y_test, predictions, zero_division=0))

    return model


def classify_lead(probability: float) -> str:
    """Asigna una categoría demostrativa según la probabilidad estimada."""
    if probability >= 0.70:
        return "Alto"
    if probability >= 0.40:
        return "Medio"
    return "Bajo"


def score_leads(model, leads: pd.DataFrame) -> pd.DataFrame:
    """Valida y puntúa un conjunto de leads."""
    missing = [column for column in FEATURES if column not in leads.columns]
    if missing:
        raise ValueError(
            "Al CSV le faltan estas columnas: " + ", ".join(missing)
        )

    clean = leads[FEATURES].copy()
    for column in FEATURES:
        clean[column] = pd.to_numeric(clean[column], errors="coerce")

    if clean.isna().any().any():
        raise ValueError("Hay valores vacíos o no numéricos en las variables.")
    if (clean < 0).any().any():
        raise ValueError("Las variables no pueden tener valores negativos.")

    probabilities = model.predict_proba(clean)[:, 1]
    results = leads.copy()
    results["conversion_probability_demo"] = np.round(probabilities, 4)
    results["lead_score_demo"] = np.round(probabilities * 100, 1)
    results["priority_demo"] = [
        classify_lead(value) for value in probabilities
    ]
    return results.sort_values(
        "conversion_probability_demo", ascending=False
    ).reset_index(drop=True)


def main():
    parser = argparse.ArgumentParser(
        description="Demo de puntuación de leads con Random Forest."
    )
    parser.add_argument(
        "--csv",
        type=Path,
        help="CSV con time_on_platform, clicks y visits para puntuar leads.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("scored_leads.csv"),
        help="Archivo CSV donde guardar los resultados.",
    )
    args = parser.parse_args()

    model = train_model()

    if args.csv:
        leads = pd.read_csv(args.csv)
    else:
        leads = pd.DataFrame(
            {
                "lead": ["Lead_A", "Lead_B", "Lead_C"],
                "time_on_platform": [35, 8, 22],
                "clicks": [12, 1, 6],
                "visits": [7, 1, 3],
            }
        )

    results = score_leads(model, leads)
    results.to_csv(args.output, index=False)

    print("\n=== Leads puntuados (demostración) ===")
    print(results.to_string(index=False))
    print(f"\nResultados guardados en: {args.output.resolve()}")
    print(
        "\nAviso: este modelo usa datos sintéticos. "
        "No uses estas puntuaciones para decisiones reales."
    )


if __name__ == "__main__":
    main()

# SKILL.md — AI Lead Scoring (prototipo)

## Propósito
Ayudar a un equipo de ventas o crecimiento a organizar clientes potenciales (*leads*) según señales de actividad. Esta habilidad describe un flujo de análisis; no debe afirmar que predice conversiones reales si solo se dispone de datos de demostración.

## Datos de entrada
Para cada lead se esperan:
- `time_on_platform`: tiempo en la plataforma, expresado en minutos en el ejemplo.
- `clicks`: número de clics.
- `visits`: número de visitas.

Los valores deben ser numéricos y no negativos. No solicitar nombres, correos, teléfonos ni otros datos personales si no son necesarios.

## Flujo de trabajo
1. Verificar que estén presentes las tres variables requeridas.
2. Comprobar que los valores sean numéricos, no negativos y que no falten datos.
3. Si existe un modelo entrenado con datos históricos validados, usarlo para calcular puntuaciones.
4. Si solo se dispone del prototipo de este repositorio, explicar que utiliza datos sintéticos y que sus puntuaciones son únicamente demostrativas.
5. Ordenar los leads de mayor a menor puntuación.
6. Presentar la puntuación, la prioridad y una explicación breve de las limitaciones.
7. Recomendar revisión humana antes de cualquier contacto o decisión comercial.

## Categorías ilustrativas
- Alto: 70–100.
- Medio: 40–69.9.
- Bajo: 0–39.9.

Estas categorías son umbrales de ejemplo, no estándares universales.

## Formato de salida sugerido
Para cada lead:
- Identificador no personal.
- Puntuación (0–100).
- Prioridad (Alto, Medio o Bajo).
- Variables observadas.
- Nota de cautela sobre el origen y la validez del modelo.

## Límites y transparencia
- Nunca inventar datos ni resultados.
- No presentar una puntuación como certeza de compra.
- No afirmar que el sistema aumentó ventas o conversiones sin evidencia.
- No usar datos sensibles ni inferir atributos personales.
- No recomendar decisiones automatizadas definitivas.
- Informar si el modelo se entrenó con datos sintéticos o si faltan datos reales.

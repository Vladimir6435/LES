# Calculadora de Riesgo de APO Severo (PROMISSE Study)

Esta aplicación de Streamlit estima el riesgo de resultado adverso severo en el embarazo
(APO severo) en pacientes con lupus (SLE) y/o anticuerpos antifosfolípidos (APL),
basada en el artículo:

**Kim et al. (2016), American Journal of Obstetrics and Gynecology**

### Variables requeridas:
- sFlt-1 (pg/mL)
- PlGF (pg/mL)
- LAC positivo
- Historia de hipertensión
- Historia de trombosis
- Presión diastólica >80 mmHg
- IMC >30
- Uso de aspirina

Modelo implementado con regresión logística (coeficientes tomados del artículo).

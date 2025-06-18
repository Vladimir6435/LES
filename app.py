# app.py
import streamlit as st
import numpy as np

st.set_page_config(page_title="Calculadora de Riesgo APO Severo", layout="centered")
st.title("🧬 Calculadora de Riesgo de APO Severo (PROMISSE)")
st.markdown("Basado en: Kim et al. *AJOG* 2016 - Modelo de regresión logística")

st.header("🔢 Ingrese los valores clínicos:")

sflt1 = st.number_input("sFlt-1 (pg/mL)", min_value=0.0, value=1000.0, step=100.0)
plgf = st.number_input("PlGF (pg/mL)", min_value=0.0, value=100.0, step=10.0)

lac = st.checkbox("Lupus anticoagulante positivo (LAC)")
htn = st.checkbox("Antecedente de hipertensión")
thromb = st.checkbox("Antecedente de trombosis")
diastolic = st.checkbox("Presión diastólica > 80 mmHg")
bmi = st.checkbox("IMC > 30 kg/m²")
aspirin = st.checkbox("Uso de aspirina")

def riesgo_apo_severo(sflt1, plgf, lac_positive, hx_hypertension,
                      hx_thrombosis, diastolic_over_80,
                      bmi_over_30, aspirin_use):
    intercept = -4.98
    coef_lac = 2.05
    coef_htn = 1.30
    coef_thromb = 0.55
    coef_dias80 = 1.16
    coef_bmi = 1.49
    coef_aspirin = -0.88
    sflt1_high = int(sflt1 > 1872)
    plgf_low = int(plgf < 70.3)
    coef_comb = 3.44  # log(OR 31.14)
    log_odds = (
        intercept +
        coef_lac * lac_positive +
        coef_htn * hx_hypertension +
        coef_thromb * hx_thrombosis +
        coef_dias80 * diastolic_over_80 +
        coef_bmi * bmi_over_30 +
        coef_aspirin * aspirin_use +
        coef_comb * (sflt1_high * plgf_low)
    )
    prob = 1 / (1 + np.exp(-log_odds))
    return round(prob * 100, 2)

if st.button("Calcular riesgo"):
    riesgo = riesgo_apo_severo(
        sflt1, plgf,
        int(lac), int(htn), int(thromb),
        int(diastolic), int(bmi), int(aspirin)
    )
    st.success(f"🔴 Riesgo estimado de APO severo: **{riesgo}%**")

import streamlit as st
import pandas as pd

def analyze_market(data):
    """Функція аналізу ринку на основі введених параметрів"""
    phase = "Флет"
    recommendation = "Очікування пробою ключових рівнів"
    
    if data['MACD_1H'] == "Ріст" and data['RSI_1H'] > 50 and data['ATR_1H'] < 30 and data['ADX_1H'] > 25:
        phase = "Ріст"
        recommendation = "Лонг при закріпленні вище POC"
    elif data['MACD_1H'] == "Падіння" and data['RSI_1H'] < 50 and data['ATR_1H'] > 30 and data['ADX_1H'] > 25:
        phase = "Падіння"
        recommendation = "Шорт при пробої вниз"
    
    return phase, recommendation

# Інтерфейс Streamlit
st.title("Автоматизований Аналіз Ринку")

# Форма для введення даних
st.sidebar.header("Введіть дані ринку")
data = {
    "Ціна зараз": st.sidebar.number_input("Ціна зараз", value=2622),
    "MACD_1H": st.sidebar.selectbox("MACD (1H)", ["Ріст", "Флет", "Падіння"], index=0),
    "RSI_1H": st.sidebar.number_input("RSI (1H)", value=50.4),
    "ATR_1H": st.sidebar.number_input("ATR (1H)", value=28.61),
    "ADX_1H": st.sidebar.number_input("ADX (1H)", value=28.64),
    "CVD_1H": st.sidebar.selectbox("CVD (1H)", ["Ріст", "Падіння"], index=0),
    "OBV_1H": st.sidebar.number_input("OBV (1H)", value=-2.28),
    "POC_1H": st.sidebar.number_input("POC (1H)", value=2640),
}

# Виклик функції аналізу
phase, recommendation = analyze_market(data)

# Вивід результатів
st.subheader("Аналіз ринку")
st.write(f"**Фаза ринку:** {phase}")
st.write(f"**Рекомендація:** {recommendation}")

import streamlit as st

def calcular_imc(peso, altura):
    return peso / (altura ** 2)

# Título de la aplicación
st.title("Calculadora de IMC")

# Descripción
st.write("Calcula tu Índice de Masa Corporal (IMC) ingresando tu peso y altura.")

# Entrada de datos del usuario
peso = st.number_input("Ingresa tu peso (kg)", min_value=0.0, format="%.2f")
altura = st.number_input("Ingresa tu altura (m)", min_value=0.0, format="%.2f")

# Botón para calcular el IMC
if st.button("Calcular IMC"):
    if peso > 0 and altura > 0:
        imc = calcular_imc(peso, altura)
        st.write(f"Tu IMC es: {imc:.2f}")

        # Interpretación del resultado
        if imc < 18.5:
            st.write("Tienes un peso inferior al normal.")
        elif 18.5 <= imc < 24.9:
            st.write("Tienes un peso normal.")
        elif 25 <= imc < 29.9:
            st.write("Tienes sobrepeso.")
        else:
            st.write("Tienes obesidad.")
    else:
        st.write("Por favor, ingresa un peso y altura válidos.")

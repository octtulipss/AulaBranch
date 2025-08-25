import streamlit as st
from utils.calculator import add, subtract, multiply, divide

def main():
    st.title("Calculadora Simples")
    
    # Entrada do usuário para os números
    num1 = st.number_input("Digite o primeiro número", value=0.0)
    num2 = st.number_input("Digite o segundo número", value=0.0)
    
    # Entrada do usuário para a operação
    operation = st.selectbox("Selecione a operação", ["Somar", "Subtrair", "Multiplicar", "Dividir"])
    
    # Calcular e exibir o resultado
    if st.button("Calcular"):
        if operation == "Somar":
            result = add(num1, num2)
        elif operation == "Subtrair":
            result = subtract(num1, num2)
        elif operation == "Multiplicar":
            result = multiply(num1, num2)
        elif operation == "Dividir":
            if num2 != 0:
                result = divide(num1, num2)
            else:
                result = "Erro: Divisão por zero"
        
        st.write(f"Resultado: {result}")

if __name__ == "__main__":
    main()
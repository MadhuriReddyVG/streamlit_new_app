import streamlit as st

def main():
    st.title("Hello App")

    # User input field
    user_input = st.text_input("Enter your name:")

    # Append "Hello" to user input
    output = "Hello " + user_input

    # Display the output
    st.write("Output:", output)

if __name__ == "__main__":
    main()


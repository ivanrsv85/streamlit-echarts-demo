import streamlit as st

def main():
    st.title("Mi Web App: Grupo 6")
    
    st.markdown("""
        <iframe width="1200" height="1000" src="https://lookerstudio.google.com/embed/reporting/4d121c56-cc84-4ced-aa70-b4f09dc0709d/page/u91eD" frameborder="0" style="border:0" allowfullscreen></iframe>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()

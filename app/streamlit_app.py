import streamlit as st


def main() -> int:
    st.write("Hello world!!!?")
    st.caption("This version has been deployed by Azure Pipelines.")

    return 0


if __name__ == "__main__":
    main()

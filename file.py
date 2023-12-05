import polars as pl
import streamlit as st

st.title("Website Title")


st.header('This is the header')


st.markdown("[Source Code](https://github.com/blakedennett/LoanApprovalProject)")

code_block = """
def func():
    print('hi')
"""

st.code(code_block, language='python')


st.subheader("This is some nice data")

df = pl.read_csv(r'https://raw.githubusercontent.com/blakedennett/LoanApprovalProject/main/data/loan_approval_dataset.csv')

st.table(df.limit(3))


state = st.checkbox('Show Image', value=True)



if state:
    st.image('images/mountains.PNG', width=700)


choice = st.radio("Select the place", options=['Las Vegas', 'Orlando'])
st.write(choice)


select = st.selectbox("Select dog breed", options=('None Selected', 'Rotweiler', 'Border Collie'))


put = st.text_input('Enter the income')

st.write(put)
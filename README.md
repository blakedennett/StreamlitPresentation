# Streamlit Presentation


### Headers

st.header('This is the header')

### Link

st.markdown("[Source Code](https://github.com/blakedennett/LoanApprovalProject)")

### Code Block

code_block = """
def func():
    print('hi')
"""
st.code(code_block, language='python')

### Table

st.subheader("This is some nice data")

df = pl.read_csv(r'https://raw.githubusercontent.com/blakedennett/LoanApprovalProject/main/data/loan_approval_dataset.csv')

st.table(df.limit(3))


### Checkbox

state = st.checkbox('Show Image', value=True)

### Images

if state:
    st.image('images/mountains.PNG', width=700)


### CSS

st.markdown("""
<style>
.element-container.st-emotion-cache-e8g64f.e1f1d6gn3 
{
    color: red;
}
</style>""", unsafe_allow_html=True)

### Dropdown

choice = st.radio("Select the place", options=['Las Vegas', 'Orlando'])
st.write(choice)

### Button

def disp():
    st.write('Hello there')

but = st.button("Display Greeting", on_click=disp)

### Dropdown

select = st.selectbox("Select dog breed", options=('None Selected', 'Rotweiler', 'Border Collie'))

### Text input

put = st.text_input('Enter the income')

st.write(put)

### Line to run code in terminal

streamlit run file.py

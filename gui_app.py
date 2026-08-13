
import streamlit as st
import matplotlib.pyplot as plt
import time

st.set_page_config(layout='wide')

st.title('Cloud Debugging Studio GUI')

col1, col2 = st.columns(2)

with col1:
    st.write('**Application Information**')
    app_name = st.text_input('Application Name', placeholder='Enter application name')
    app_id = st.text_input('Application ID', placeholder='Enter application ID')
    st.button('Connect')

with col2:
    st.write('**Debugging Options**')
    debug_level = st.selectbox('Debug Level', ['INFO', 'DEBUG', 'WARNING', 'ERROR'])
    st.checkbox('Enable Live Updates')
    st.button('Start Debugging')

st.write('**Live Status Indicators**')
col3, col4, col5 = st.columns(3)
with col3:
    st.write('**CPU Usage**')
    fig, ax = plt.subplots()
    ax.plot([1, 2, 3], [10, 20, 30])
    st.pyplot(fig)
with col4:
    st.write('**Memory Usage**')
    fig, ax = plt.subplots()
    ax.plot([1, 2, 3], [40, 50, 60])
    st.pyplot(fig)
with col5:
    st.write('**Network Usage**')
    fig, ax = plt.subplots()
    ax.plot([1, 2, 3], [70, 80, 90])
    st.pyplot(fig)

st.write('**Graphical Chart/Progress Displays**')
fig, ax = plt.subplots()
ax.plot([1, 2, 3], [10, 20, 30])
st.pyplot(fig)

st.write('**Console Output**')
console_output = st.empty()
console_output.text('Waiting for debugging output...')

# Simulate debugging output
for i in range(10):
    console_output.text(f'Debugging output {i+1}')
    time.sleep(1)

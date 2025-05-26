# import streamlit as st from units import UNITS, convert_value

# Set page configuration
st.set_page_config(page_title="Advanced Unit Converter", layout="wide")

# Custom CSS for color tones and fade-in animation
st.markdown("""
<style>
body {
    background-color: #2b2b2b;
    color: #e0e0e0;
}
.stApp {
    background-color: #2b2b2b;
}
.result {
    animation: fadeIn 0.5s;
    background-color: #3a3a3a;
    padding: 10px;
    border-radius: 5px;
    color: #90ee90;
}
@keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
}
.sidebar .sidebar-content {
    background-color: #333333;
}
</style>
""", unsafe_allow_html=True)

# Title
st.title("Advanced Unit Converter")

# Sidebar for category selection with emojis
categories = [
    '📏 Length',
    '⚖ Weight',
    '🌡 Temperature',
    '💧 Volume',
    '🏞 Area',
    '🚀 Speed',
    '⏳ Time'
]
category_display = st.sidebar.selectbox("Select Category", categories, key='category')
category = category_display.split(' ', 1)[1]  # Remove emoji for internal use

# Determine units based on category
if category == 'Temperature':
    units = ['Celsius', 'Fahrenheit', 'Kelvin']
else:
    units = list(UNITS[category]['units'].keys())

# Unit selection and swap button
col1, col2, col3 = st.columns([2, 1, 2])
with col1:
    from_unit = st.selectbox("From", units, key='from_unit')
with col3:
    to_unit = st.selectbox("To", units, key='to_unit')
# with col2:
#     if st.button("🔄 Swap"):
#         st.session_state.from_unit, st.session_state.to_unit = to_unit, from_unit
#         st.experimental_rerun()

# Input value and precision
value = st.number_input("Enter Value", value=0.0, step=0.1)
precision = st.slider("Decimal Places", 0, 10, 6)

# Perform conversion
try:
    result = convert_value(value, from_unit, to_unit, category)
    result_text = f"{value} {from_unit} = {result:.{precision}f} {to_unit}"
    st.markdown(f'<div class="result">{result_text}</div>', unsafe_allow_html=True)
except Exception as e:
    st.error(f"Conversion error: {e}")

# Recent conversions (stored in session state)
if 'recent_conversions' not in st.session_state:
    st.session_state.recent_conversions = []
if 'result_text' in locals():
    st.session_state.recent_conversions.append(result_text)
    st.subheader("Recent Conversions")
    for conv in st.session_state.recent_conversions[-5:]:  # Show last 5
        st.write(conv)
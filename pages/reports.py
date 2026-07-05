import streamlit as st
import pandas as pd
from fpdf import FPDF

st.set_page_config(page_title="Report", page_icon="📄", layout="wide")

st.title("📄 AQI Report Generator")

df = pd.read_csv("data/final_dataset/daily_satellite_dataset.csv")

city = st.selectbox("Select City", sorted(df["City"].unique()))

latest = df[df["City"] == city].iloc[-1]

st.write(latest)

if st.button("Generate PDF Report"):

    pdf = FPDF()

    pdf.add_page()

    pdf.set_font("Arial", size=16)
    pdf.cell(200,10,"ISRO AI Surface AQI Report",ln=True)

    pdf.set_font("Arial", size=12)

    pdf.cell(200,10,f"City : {city}",ln=True)
    pdf.cell(200,10,f"AQI : {latest['AQI']}",ln=True)
    pdf.cell(200,10,f"NO2 : {latest['NO2']}",ln=True)
    pdf.cell(200,10,f"HCHO : {latest['HCHO']}",ln=True)
    pdf.cell(200,10,f"Temperature : {latest['Temperature']} C",ln=True)
    pdf.cell(200,10,f"Humidity : {latest['Humidity']} %",ln=True)
    pdf.cell(200,10,f"Wind Speed : {latest['WindSpeed']} m/s",ln=True)

    filename = f"reports/{city}_AQI_Report.pdf"

    pdf.output(filename)

    st.success("Report Generated Successfully!")

    with open(filename,"rb") as file:
        st.download_button(
            "⬇ Download Report",
            file,
            file_name=f"{city}_AQI_Report.pdf"
        )
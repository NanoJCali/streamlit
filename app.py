import streamlit as st
import pandas as pd

st.title('Hello Wilders, welcome to my application!')

st.write("I enjoy to discover stremalit possibilities")

link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
df = pd.read_csv(link)

# Here we use "magic commands":
df

import seaborn as sns
viz_correlation = sns.heatmap(df.corr(), 
								center=0,
								cmap = sns.color_palette("vlag", as_cmap=True))

st.pyplot(viz_correlation.figure)

Europe= st.button("Europe")
Europe
if Europe:
    st.pyplot(sns.heatmap(df[df.continent.str.contains("Europe")].corr(), 
								center=0,
								cmap = sns.color_palette("vlag", as_cmap=True)).figure)

US= st.button("US")
US
if US:
    st.pyplot(sns.heatmap(df[df.continent.str.contains("US")].corr(), 
								center=0,
								cmap = sns.color_palette("vlag", as_cmap=True)).figure)

Jap= st.button("Japan")
Jap
if Jap:
    st.pyplot(sns.heatmap(df[df.continent.str.contains("Japan")].corr(), 
								center=0,
								cmap = sns.color_palette("vlag", as_cmap=True)).figure)

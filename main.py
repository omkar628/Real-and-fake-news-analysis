import pandas as pd 
import streamlit as st
import datetime as dt 
from PIL import Image 
import plotly.express  as px
import plotly.graph_objects as go

df = pd.read_csv("C:/Users/omkar/Data science course/streamlit/streanli_projects/fake_news-dection/cleaned_file.csv")
st.set_page_config(layout="wide")
st.markdown('<style>div.block-container{padding-top:1rem;}</style>',unsafe_allow_html=True)
html_title="""
  <style>
  .title{
  font-weight:bold;
  padding:5px;
  border-radius:6px
  }
  </style>
  <center><h1 class=title>REAL AND FAKE NEWS ANALYSIS</h1></center>
"""
col1,col2=st.columns([0.1,0.9])
with col1:
  st.image("newspaper.png",width=100)
with col2:
  st.markdown(html_title,unsafe_allow_html=True)
st.divider()

col3,col4=st.columns([0.5,0.3])
with col3:
  data=df["label"].value_counts().reset_index()
  data.columns = ["label", "Count"]
  fig1=px.pie(data,values="Count",names="label",title="FAKE VS REAL")
  fig1.update_traces(hole=0.4)

  st.plotly_chart(fig1,use_container_width=True)
with col4:
  data1=df[["category","label"]].groupby(by="category")["label"].value_counts().reset_index()
  data1.columns=["category","label","count"]
  fig2=px.bar(data1,x="category",y="count",color="label",title="Category wise Real VS Fake ")
  


  st.plotly_chart(fig2,use_container_width=True)
_,view1,dwn1,view2,dwn2=st.columns([0.15,0.20,0.20,0.20,0.20])
with view1:
  expander=st.expander("FAKE VS REAL")
  result=data
  expander.write(result)
  
with dwn1:
  st.download_button("Downdload data",data=data.to_csv().encode("utf-8"),file_name="REAL_VS_FAKE.csv",mime="text/csv")

with view2:
  expander=st.expander("Category wise Real VS Fake")
  result1=data1
  expander.write(result1)

with dwn2:
  st.download_button("Downdload data",data=data.to_csv().encode("utf-8"),file_name="Category wise Real VS Fake.csv",mime="text/csv")

_,col5=st.columns([0.1,1])
with col5:
    
  df["date"] = pd.to_datetime(df["date"])


  last_30_days = pd.Timestamp.now() - pd.Timedelta(days=30)
  df_recent = df[df["date"] >= last_30_days]


  data3 = df_recent[["date", "label"]].groupby(by=["date", "label"]).size().reset_index()
  data3.columns = ["date", "label", "count"]


  fig3 = px.line(data3, x="date", y="count", color="label", title="Last 30 Days - Fake vs Real News")
  st.plotly_chart(fig3, use_container_width=True)

_,view3,dwn3=st.columns([0.15,0.40,0.40])
with view3:
  expander=st.expander("Last 30 Days - Fake vs Real News")
  result=data3
  expander.write(result)
with dwn3:
  st.download_button("Downdload data",data=data.to_csv().encode("utf-8"),file_name="Last 30 Days - Fake vs Real News",mime="text/csv")
_,col6=st.columns([0.15,0.8])
with col6:
  data4=df[["source","category"]].groupby(by=["source","category"]).size().reset_index()
  data4.columns=["source","category","count"]
  fig4=px.density_heatmap(data4,x="source",y="category",z="count",color_continuous_scale="Blues",title="No. of articles publishes by each Category")
  st.plotly_chart(fig4,use_container_width=True)
_,view4,dwn4=st.columns([0.15,0.40,0.40])
with view4:
  expander=st.expander("Full data")
  result=data4
  expander.write(result)
with dwn4:
  st.download_button("Downdload data",data=data.to_csv().encode("utf-8"),file_name="articlepublish.csv",mime="text/csv")

st.divider()

  
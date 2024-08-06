import streamlit as st
import plotly.express as px
import pandas as pd

st.set_page_config(
    page_title="Analytics",
    page_icon="📊"
)

st.title("Data Analytics Portal📊")
st.subheader("Explore Data With Ease")
st.markdown("---")
file=st.file_uploader("Upload CSV or EXCEL file only",type=['csv','xlsx'])
if file:
    if(file.name.endswith('csv')):
        data=pd.read_csv(file)
    else:
        data=pd.read_excel(file)
    st.dataframe(data)
    st.success("FILE UPLAODED SUCCESSFULLY:100:")

    st.subheader("Basic Information of dataset",divider='grey')
    tab1,tab2,tab3,tab4=st.tabs(['Summary','Top and Bottom rows','Data Types','Columns'])
    
    with tab1:
        st.write(f"Rows: {data.shape[0]}")
        st.write(f"Columns: {data.shape[1]}")
        

    with tab2:
        st.subheader("Top Rows")
        top_rows=st.slider("Top Rows",1,data.shape[0],key='topslider')
        st.dataframe(data.head(top_rows))
        st.markdown("---")
        st.subheader("Bottom Rows")
        bottom_rows=st.slider("Bottom Rows",1,data.shape[0],key='bottomslider')
        st.dataframe(data.tail(bottom_rows))
        

    with tab3:
        st.subheader("Data Types of Column")
        st.dataframe(data.dtypes)
        
    with tab4:
        st.subheader("Columns in Dataframe")
        st.write(list(data.columns))
        
    st.subheader("Columns Value to Count",divider='grey')
    with st.expander("Value Count"):
        column=st.selectbox("Select Column Name ",options=list(data.columns))
        count=st.button("Count")
        if count:
            result=data[column].value_counts().reset_index()
            st.dataframe(result)
            
            st.subheader("VIZ",divider="grey")
            viz=px.bar(data_frame=result,x=column, y='count',text='count')
            st.plotly_chart(viz)




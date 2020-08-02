import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from PIL import Image
from functools import reduce 


st.title("EDA APP")
st.sidebar.markdown("EDA App")

@st.cache(persist=True)
def explore_data(data):
    df = pd.read_csv(os.path.join(data))
    return df


datasets = os.listdir('dataset/')

data_list = st.sidebar.multiselect("Select dataset(s)", datasets)

for x in data_list:
    x = 'dataset/'+ x
    if st.sidebar.checkbox(f"Preview {x}"):
        data = explore_data(x)
        st.write(data)

dataset1 = 'dataset/train.csv'
dataset2 = 'dataset/test.csv'





col_option1 = st.sidebar.selectbox('select function', ("Select", "Merge","Head","Concat","Tail"))

if col_option1 == 'Merge':
    merge_df = []
    merge_list = st.sidebar.multiselect("Select dataset(s)", data_list)
    for x in merge_list:
        file = 'dataset/'+x
        x = explore_data(file)
        merge_df.append(x)

    if len(merge_df) > 0:
    # df = pd.merge(merge_df, right_index=True,left_index=True)
        df = reduce(lambda df1,df2: pd.merge(df1,df2, right_index=True,left_index=True), merge_df)
        st.write(df)
    else:
        pass

elif col_option1 == "":
    pass


    # data1 = explore_data(dataset1)
    # data2 = explore_data(dataset1)
    # df = pd.merge(data1, data2, right_index=True, left_index=True)
    # st.write(df)

col_option2 = st.sidebar.selectbox('Visualize DataFrame', ("Select", "Regplot","Pie Plot","Correlation","Bar Plot"))

if col_option2 == "Pie Plot":
    pie_df = st.sidebar.selectbox("Select Dataframe", data_list)
    col = st.sidebar.text_input("Enter column")
    file = "dataset/"+pie_df
    df = explore_data(file)
    if len(col) >0:
        try:
            st.write(df.plot.pie(y=col))
            st.pyplot()
        except Exception as e:
            st.write(e)
   

elif col_option2 == "Correlation":
    corr_df = st.sidebar.selectbox("Select Dataframe", data_list)
    file = 'dataset/'+corr_df
    df = explore_data(file)
    try:
        st.write(f"Correlation Plot of {corr_df}")
        sns.heatmap(df.corr(), annot=True)
        st.pyplot()
    except Exception:
        pass


# daf = pd.DataFrame({'mass': [0.330, 4.87 , 5.97], 'radius': [2439.7, 6051.8, 6378.1]},index=['Mercury', 'Venus', 'Earth'])
# plot = daf.plot.pie(y='mass')
# st.pyplot()
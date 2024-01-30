import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import pandas as pd

# Matplotlib의 전역 figure 경고 무시 설정
st.set_option('deprecation.showPyplotGlobalUse', False)

folder_path = "C:/Users/한대희/Desktop/mulcamp-240130/"
csv_files = ["sampled_order_products__prior.csv", "sampled_orders.csv", "sampled_products.csv"]

all_data = pd.DataFrame()

for file in csv_files:
    file_path = folder_path + file
    df = pd.read_csv(file_path)
    sampled_df = df.sample(frac=0.09, random_state=42)
    all_data = pd.concat([all_data, sampled_df]).reset_index(drop=True)

st.title("대시보드")
st.dataframe(all_data)

st.subheader("히스토그램")
selected_column = st.selectbox("히스토그램", all_data.columns)
fig, ax = plt.subplots(figsize=(8, 6))
sns.histplot(all_data[selected_column].drop_duplicates(), kde=True, ax=ax)
st.pyplot(fig)  # Matplotlib figure 객체를 전달

st.subheader("박스 플롯")
boxplot_column = st.selectbox("박스 플롯", all_data.columns)
fig, ax = plt.subplots(figsize=(8, 6))
sns.boxplot(x=all_data[boxplot_column], ax=ax)
st.pyplot(fig)  # Matplotlib figure 객체를 전달

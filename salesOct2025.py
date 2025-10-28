import pandas as pd
import streamlit as st
import plotly.express as px
df = pd.read_csv('all_df.csv')
st.set_page_config(page_title='My Salses Dashboard',page_icon=':bar_chart:',layout='wide')
st.sidebar.header('Please filter here')
pselect = st.sidebar.multiselect(
    "Select Product",
    options = df['Product'].unique(),
    default = df['Product'].unique()[:5]
)
cselect = st.sidebar.multiselect(
    "Select City",
    options = df['City'].unique(),
    default = df['City'].unique()[:5]
)
mselect = st.sidebar.multiselect(
    "Select Month",
    options = df['Month'].unique(),
    default = df['Month'].unique()[:5]
)

st.title(':bar_chart: Sales Dashborad for 2019')
st.markdown('#')
total = df['Total'].sum()
ptotal = df['Product'].nunique()
left_col, right_col = st.columns(2)
with left_col:
    st.subheader('Total Sales')
    st.subheader(f'US $ {total}')
with right_col:
    st.subheader('No. of Unique Product')
    st.subheader(f'US $ {ptotal}')
    
a_col, b_col, c_col = st.columns(3)

df_select = df.query('City==@cselect and Month == @mselect and Product == @pselect')
total_by_Product = df_select.groupby('Product')['Total'].sum().sort_values()

fig_by_product = px.bar(
    total_by_Product, 
    x=total_by_Product.values, 
    y=total_by_Product.index, 
    title="Sales by Product"
)
a_col.plotly_chart(fig_by_product,use_container_width=True)

fig_by_city = px.pie(
    df_select, 
    values='Total', 
    names='City', 
    title="Sales by City"
)
b_col.plotly_chart(fig_by_city,use_container_width=True)

total_by_Month = df_select.groupby('Month')['Total'].sum().sort_values()

fig_by_month = px.bar(
    total_by_Month, 
    x=total_by_Month.values, 
    y=total_by_Month.index, 
    title="Sales by Month"
)
c_col.plotly_chart(fig_by_month,use_container_width=True)

d_col, e_col = st.columns(2)
fig_month = px.line(
    total_by_Month, 
    x=total_by_Month.index,
    y=total_by_Month.values,
    title='Total Sales by Month with Line Chart'
)
d_col.plotly_chart(fig_month,use_container_width=True)   
 
fig_quantity = px.scatter(
    df, 
    x="Total", 
    y="QuantityOrdered",
    title = 'Sales Amount'
)
e_col.plotly_chart(fig_quantity,use_container_width=True)  


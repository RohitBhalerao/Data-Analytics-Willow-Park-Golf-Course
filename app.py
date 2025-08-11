# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import streamlit as st
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt 
DATA_URL = ("Data.xlsx")
data = pd.read_excel('Data.xlsx')
data = data[0:2000]

####
st.title("Data Analytics - Willow Park Golf Course - Restaurant Data - June 20 2020 to July 20 2020")
st.markdown("This is a streamlit dashboard used to analyze data and provide data-driven solutions to business optimization Problem. Analyzing the data from the first month of business post COVID-19 lockdown will help take actions that will result in improved business performance. 🗽💥")
if st.checkbox("Show Data", False):
    st.subheader('Data')
    st.write(data)
####
l1 = data[['Order_ID', 'DATE', 'DAY','TIME','TOTAL','WEEK NUMBER']]
l2 = data['Order_ID'].nunique()
groupl = l1.groupby('Order_ID')
l3 = groupl['TOTAL'].agg(['sum'])
groupl2 = l1.groupby('DATE')
l4 = groupl2['TOTAL'].agg(['sum'])
groupl3 = l1.groupby('WEEK NUMBER')
l5 = groupl3['TOTAL'].agg(['sum'])
groupl4 = l1.groupby('DAY')
l6 = groupl4['TOTAL'].agg(['sum'])
l6 = l6.loc[['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY'], :]
l6['Cumulative Revenue'] = l6['sum'].cumsum()
l6['Cumulative Percentage'] = 100*l6['Cumulative Revenue']/l6['sum'].sum()
l3['Cumulative Revenue'] = l3['sum'].cumsum()
l3['Cumulative Percentage'] = 100*l3['Cumulative Revenue']/l3['sum'].sum()
l4['Cumulative Revenue'] = l4['sum'].cumsum()
l4['Cumulative Percentage'] = 100*l4['Cumulative Revenue']/l4['sum'].sum()
l5['Cumulative Revenue'] = l5['sum'].cumsum()
l5['Cumulative Percentage'] = 100*l5['Cumulative Revenue']/l5['sum'].sum()
a4 = data['TOTAL'].sum()



fig1, ax = plt.subplots(figsize=(10, 10))

# Add x-axis and y-axis
ax.bar(l4.index.values,
        l4['sum'],
        color='purple')

# Set title and labels for axes
ax.set(xlabel="Date",
       ylabel="Revenue in Canadian Dollar's",
       title="Daily Total Revenue")

# Rotate tick marks on x-axis
plt.setp(ax.get_xticklabels(), rotation=45)


fig2, ax = plt.subplots(figsize=(10, 10))

# Add x-axis and y-axis
ax.bar(l5.index.values,
        l5['sum'],
        color='purple')
ax.plot(l5.index.values, l5['Cumulative Revenue'], color = 'red')
# Set title and labels for axes
ax.set(xlabel="Week of the month",
       ylabel="Revenue in Canadian Dollar's",
       title="Weekly Total Revenue")

# Rotate tick marks on x-axis
plt.setp(ax.get_xticklabels(), rotation=45)

fig3, ax = plt.subplots(figsize=(10, 10))

# Add x-axis and y-axis
ax.bar(l6.index.values,
        l6['sum'],
        color='purple')

# Set title and labels for axes
ax.set(xlabel="Day",
       ylabel="Revenue in Canadian Dollar's",
       title="Total Revenue by Days of the")

# Rotate tick marks on x-axis
plt.setp(ax.get_xticklabels(), rotation=45)

st.header("Performance for the first five weeks :")
st.markdown("The first 5 weeks have seen a total of %i customers visiting either for an in-house or a takeaway order. These have contributed to the total revenue of %i \\$. The average bill amount per customer comes out to be %i \\$." %(l2, a4 , a4/l2))
st.write(fig1)
st.markdown("The highest single day revenue was recorded on Tuesday, 7th July. New menu items were also introduced on this day. Though these new menu items were not the most ordered dishes, they had customers explore the previously less demanded items on the menu. Another day which saw above average performance was 21st July. The Men's and Ladies feature night menu introduced in the previous week (14th July) were in demand on the day, contributing to half of the revenue generated. These experiments clearly seem to be working for the restaurant. The average revenue per day of 784 \\$ saw an improvement of 461 \\$ as the average revenue on the three days on which the retaurant experimented with the menu was 1245 \\$. Introducing such changes every month will result in an increased business by 8%.")
st.write(fig2)
st.markdown("The revenue sees a steady and consistent growth through the five weeks")
st.write(fig3)
st.markdown("While the total revenues on Thursday is the lowest, it is important to note that the restaurant was closed on 3 of the 5 Thursdays.")





####
df2 = data[['Order_ID', 'SERVER','TOTAL']]
group = df2.groupby('Order_ID')
df3 = group['TOTAL'].agg(['sum'])
df4 = df2[['Order_ID','SERVER']]
df4 = df4.drop_duplicates()
group2 = df2.groupby('SERVER')
df5 = group2['TOTAL'].agg(['sum'])
df5['SERVER_NAME'] = df5.index
df6 = df4['SERVER'].value_counts()
df6.columns = ['server_name','num_of_bills']
df6 = df6.to_frame()
df6['SERVER_NAME']=df6.index
df7 = pd.merge(df5, df6, on='SERVER_NAME', how='outer')
df7['avg_bill'] = df7['sum']/df7['count']
df7 = df7.rename(columns={"sum": "Total revenue generated", "SERVER_NAME": "Server Name", "count" : "Customers served", "avg_bill" : "Average revenue per bill"})
df7.sort_values(by='Average revenue per bill', ascending=False)
q = df7.sort_values(by='Average revenue per bill', ascending=False)
w = df7.sort_values(by='Total revenue generated', ascending = False)

df9 = data[['DATE','TOTAL']]
a = df9.groupby('DATE')
df9 = a['TOTAL'].agg(['sum'])
df10 = data[['DATE','Order_ID']]
b = df10.groupby('DATE')
df10 = b['Order_ID'].nunique()
df11 = pd.merge(df9, df10, on='DATE', how='outer')
df11['avg'] = df11['sum']/df11['Order_ID']
df11.std()
a = (df11['avg'].std())
b = q['Customers served'][8:].sum()
c = df11['sum'].sum()
st.header("Server performances for the month :")
select = st.selectbox('Show the list of servers by:', ['Efficiency', 'Revenue generated', 'Customers attended'])

if select == 'Efficiency':
        st.write(q)
        st.markdown("Standard deviation for average revenue generated everyday is %i dollars" %(a))
        st.markdown("The standard deviation in the average revenue generated by the servers is %i. (Ignoring outlier server name Bailey T.) The total number of customers served by the server's with low average revenue generated is %i. (Contributing to negative standard deviation.) Replacing these servers with the server's with higher average revenue or awarding performance based incentives will see an improved business as follows : %i * %i = \\$ %i i.e. %i percent increase in revenue." %(a, b , a,  b , a * b , ((a * b)/c) * 100)) 
if select == 'Revenue generated':
        st.write(df7.sort_values(by='Total revenue generated', ascending=False))
        st.markdown("Deb, Jillian and Ashley have attended %i of the total %i customers in the month, contributing to more than half of the revenue generated. Jillian has a higher average revenue per bill" %(w['Customers served'][0:3].sum() , w['Customers served'].sum()))
elif select == 'Customers attended':
        st.write(df7.sort_values(by='Customers served', ascending=False))
        
        
###
d12 = data[[ 'DATE','DAY','TOTAL','WEEK NUMBER']]
def top(g):
    return g['DAY'].value_counts().idxmax()
topdf = d12.groupby('DATE').apply(top)
topdf = topdf.to_frame()
topdf.columns = ['DAY']
d13 = topdf['DAY'].value_counts()
d13 = d13.to_frame()
d13.index.names = ['DAY']
d13.columns = ['DAYS']
group4 = d12.groupby('DAY')
d14 = group4['TOTAL'].agg(['sum'])
e = pd.merge(d14, d13, on='DAY', how='outer')
e['Average day of week'] = e['sum']/e['DAYS']
e = e.loc[['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY'], :]
e.columns = ['Total revenue for this day', 'Number of working days', 'Average revenue']
a1 = (e['Average revenue'].iloc[1] + e['Average revenue'].iloc[3] + e['Average revenue'].iloc[4:].sum())/5
a2 = (e['Average revenue'].iloc[0] + e['Average revenue'].iloc[2])/2 
a3 = a1 - a2
a4 = data['TOTAL'].sum()
a5 = ((a3 * 4) / (data['TOTAL'].sum())) * 100

st.header("Best days to keep the restaurant closed for maintenance and sanitization :")
Day = e.index 
Average = e['Average revenue'] 
  
# Figure Size 
fig, ax = plt.subplots(figsize =(16, 9)) 
  
# Horizontal Bar Plot 
ax.barh(Day, Average) 
  
# Remove axes splines 
for s in ['top', 'bottom', 'left', 'right']: 
    ax.spines[s].set_visible(False) 
  
# Remove x, y Ticks 
ax.xaxis.set_ticks_position('none') 
ax.yaxis.set_ticks_position('none') 
  
# Add padding between axes and labels 
ax.xaxis.set_tick_params(pad = 5) 
ax.yaxis.set_tick_params(pad = 10) 
  
# Add x, y gridlines 
ax.grid(True, color ='grey', 
        linestyle ='-.', linewidth = 0.5, 
        alpha = 0.2) 
  
# Show top values  
ax.invert_yaxis() 
  
# Add annotation to bars 
for i in ax.patches: 
    plt.text(i.get_width()+0.2, i.get_y()+0.5,  
             str(round((i.get_width()), 2)), 
             fontsize = 10, fontweight ='bold', 
             color ='grey') 
  
# Add Plot Title 
ax.set_title('Average revenue by days of the week', 
             loc ='left', ) 
  
# Add Text watermark 
fig.text(0.9, 0.15, 'Rohit Bhalerao', fontsize = 12, 
         color ='grey', ha ='right', va ='bottom', 
         alpha = 0.7) 
  
# Show Plot 
st.write(fig)

st.write(e) 
st.markdown("Even though Tuesdays and Thursdays see a good business than other days of the week, the restaurant was closed on 2 Tuesdays and 3 Thursdays in the 5 weeks. So, it is suggested to change this, and to keep the restaurant closed on either Monday's or Wednesday's for Sanitization and Maintenance purpose. The average business of Tuesdays, Thursdays, Fridays and the weekends is %i \\$. The average business of Wednesdays and Mondays is %i \\$.This action will add up the revenue by around %i \\$ every week, i.e. , %i \\$ a month. Business performance will improve by around %i percent." %(a1, a2 , a3 , a3 * 4 , a5))

####
z = data[['DAY' , 'ITEM','FOOD TYPE', 'WEEK NUMBER']]
groupz = z.groupby('WEEK NUMBER')
z1 = groupz['ITEM'].value_counts()
z2 = z1['WEEK 1'][0:5]
z3 = z1['WEEK 2'][0:5]
z4 = z1['WEEK 3'][0:5]
z5 = z1['WEEK 4'][0:5]
z6 = z1['WEEK 5'][0:5]

z7 = data[['DAY' , 'ITEM','FOOD TYPE']]
groupz2 = z7.groupby('DAY')
z8 = groupz2['ITEM'].value_counts()
z9 = z8['MONDAY'][0:5]
z10 = z8['TUESDAY'][0:5]
z11 = z8['WEDNESDAY'][0:5]
z12 = z8['THURSDAY'][0:5]
z13 = z8['FRIDAY'][0:5]
z14 = z8['SATURDAY'][0:5]
z15 = z8['SUNDAY'][0:5]

df_final=pd.DataFrame(data["FOOD TYPE"])
df_final['ITEM']=data["ITEM"].values
countz = df_final.groupby(['FOOD TYPE','ITEM']).size().reset_index(name = 'Frequency')
countz = countz.sort_values(by = 'Frequency', ascending = False)
z17= countz.groupby(['FOOD TYPE'], sort=False)['Frequency'].max()
z = z17.to_frame()
z16 = df_final.groupby('FOOD TYPE')['ITEM'].apply(lambda x: x.value_counts().index[0]).reset_index(name='Most Frequent Item')
z18 = pd.merge(z16, z17, on = 'FOOD TYPE', how = 'outer')
z19 = countz.groupby(['FOOD TYPE'], sort=False)['Frequency'].min()
z19 = z19.to_frame()
z20 = df_final.groupby('FOOD TYPE')['ITEM'].apply(lambda x: x.value_counts().index[-1]).reset_index(name='Least Frequent Item')
z21 = pd.merge(z20, z19, on = 'FOOD TYPE', how = 'outer')



st.header("Most frequently ordered menu items: ")
select1 = st.selectbox('by:', ['Week', 'Days', 'Month'])

if select1 == 'Week':
            st.markdown("Week 1")
            st.write(z2)
            st.markdown("Week 2")
            st.write(z3)
            st.markdown("Week 3")
            st.write(z4)
            st.markdown("Week 4")
            st.write(z5)
            st.markdown("Week 5")
            st.write(z6)
    
if select1 == 'Days':
            st.markdown("Monday")
            st.write(z9)
            st.markdown("Tuesday")
            st.write(z10)
            st.markdown("Wednesday")
            st.write(z11)
            st.markdown("Thursday")
            st.write(z12)
            st.markdown("Friday")
            st.write(z13)
            st.markdown("Saturday")
            st.write(z14)
            st.markdown("Sunday")
            st.write(z15)
elif select1 == 'Month':
    select2 = st.selectbox('by:', ['Most Frequent', 'Least Frequent'])
    if select2 == 'Most Frequent':
            st.markdown("Most Frequently ordered items for the month :")
            st.write(z18)
    if select2 == 'Least Frequent':
            st.markdown("Least Frequently ordered items for the month :")
            st.write(z21)


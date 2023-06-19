#!/usr/bin/env python
# coding: utf-8

# In[79]:


import pandas as pd 


# In[81]:


import seaborn as sns


# In[46]:


df = pd.read_csv(r'..\Leanding causes of death in USA\Leading_causes_dataset.csv')
df


# In[ ]:





# In[47]:


#1) What are the total number of deaths in the dataset?
deaths_per_cause = df[(df['Cause Name'] != 'All causes')&(df['State'] != 'United States' )]
sum_deaths =sum(deaths_per_cause['Deaths'])
sum_deaths


# In[48]:


#2) How many deaths are attributed to each specific cause?
deaths_by_cause = deaths_per_cause.groupby('Cause Name')['Deaths'].sum()
deaths_by_cause


# In[57]:


#3) Which cause of death has the highest number of occurrences?
deaths_by_state = deaths_per_cause.groupby('State')['Deaths'].sum().reset_index()
deaths_by_state


# In[55]:


#4) How does the number of deaths vary across different states?
import matplotlib.pyplot as plt
deaths_by_state = deaths_by_state.sort_values('Deaths', ascending=False)

plt.figure(figsize=(10, 6))
plt.bar(deaths_by_state['State'], deaths_by_state['Deaths'])
plt.xlabel('State')
plt.ylabel('Number of Deaths')
plt.title('Number of Deaths by State')
plt.xticks(rotation=90)
plt.show()


# In[65]:


#5) Can you plot a bar chart or pie chart to visualize the distribution of causes of death?
deaths_by_cause=deaths_by_cause.reset_index()
deaths_by_cause = deaths_by_cause.sort_values('Deaths', ascending=False)
plt.figure(figsize=(12, 6))
plt.bar(deaths_by_cause['Cause Name'], deaths_by_cause['Deaths'])
plt.xlabel('Cause of Death')
plt.ylabel('Number of Deaths')
plt.title('Distribution of Causes of Death')
plt.xticks(rotation=90)
plt.show()


# In[70]:


# pie chart :
plt.figure(figsize=(8, 8))
plt.pie(deaths_by_cause['Deaths'], labels=deaths_by_cause['Cause Name'], autopct='%1.1f%%')
plt.title('Distribution of Causes of Death')
plt.show()


# In[67]:


#6) What is the average number of deaths per state?
deaths_by_state_avg = (deaths_per_cause.groupby('State')['Deaths']).mean()
deaths_by_state_avg


# In[84]:


#7) Is there any correlation between the number of deaths and other factors such as population size or demographic information?
selected_columns = ['Deaths', 'Age-adjusted Death Rate',]  
selected_data = df[selected_columns]
# Remove commas and convert numeric columns to float
cor_matrix = selected_data.replace(',', '', regex=True).astype(float).corr()
cor_matrix
#A correlation coefficient of 0.231 indicates a positive correlation between the two variables Deaths and Age-adjusted Death Rate



# In[93]:


#8) How does the number of deaths change over time? Are there any notable trends or patterns?
deaths_sorted_year = deaths_per_cause.sort_values('Year')
deaths_by_year = deaths_sorted_year.groupby('Year')['Deaths'].sum().reset_index()
plt.plot(deaths_by_year['Year'], deaths_by_year['Deaths'], marker='o')
plt.xlabel('Year')
plt.ylabel('Number of Deaths')
plt.title('Number of Deaths Over Time')
plt.show()


# In[96]:


#Are there any seasonal or yearly patterns in the number of deaths? Are certain years associated with higher or lower mortality rates?
# visualize each cause per Deaths rate
deaths_sorted_year = deaths_per_cause.sort_values('Year')
deaths_by_year = deaths_sorted_year.groupby('Cause Name')['Deaths'].sum().reset_index()
plt.plot(deaths_by_year['Cause Name'], deaths_by_year['Deaths'], marker='o')
plt.xlabel('Cause Name')
plt.ylabel('Number of Deaths')
plt.title('Number of Deaths Over Time')
plt.xticks(rotation='vertical')
plt.show()


# In[119]:


#visualize each cause's date rate over time 
years = df['Year']
cause1 = df[(df['Cause Name'] == 'Unintentional injuries')]
cause2 = df[(df['Cause Name'] == "Alzheimer's disease")]
cause3 = df[(df['Cause Name'] == 'Cancer')]
cause4 = df[(df['Cause Name'] == 'CLRD')]
cause5 = df[(df['Cause Name'] == 'Diabetes')]
cause6 = df[(df['Cause Name'] == 'Heart disease')]
cause7 = df[(df['Cause Name'] == 'Influenza and pneumonia')]
cause8 = df[(df['Cause Name'] == 'Kidney disease')]
cause9 = df[(df['Cause Name'] == 'Stroke')]
cause10 = df[(df['Cause Name'] == 'Suicide')]

cause1=cause1.groupby('Year')['Deaths'].sum().reset_index()
cause2=cause2.groupby('Year')['Deaths'].sum().reset_index()
cause3=cause3.groupby('Year')['Deaths'].sum().reset_index()
cause4=cause4.groupby('Year')['Deaths'].sum().reset_index()
cause5=cause5.groupby('Year')['Deaths'].sum().reset_index()
cause6=cause6.groupby('Year')['Deaths'].sum().reset_index()
cause7=cause7.groupby('Year')['Deaths'].sum().reset_index()
cause8=cause8.groupby('Year')['Deaths'].sum().reset_index()
cause9=cause9.groupby('Year')['Deaths'].sum().reset_index()
cause10=cause10.groupby('Year')['Deaths'].sum().reset_index()

plt.plot(cause1['Year'], cause1, label='Unintentional injuries')
plt.plot(cause2['Year'], cause2, label="Alzheimer's disease")
plt.plot(cause3['Year'], cause3, label='Cancer')
plt.plot(cause4['Year'], cause4, label='CLRD')
plt.plot(cause5['Year'], cause5, label='Diabetes')
plt.plot(cause6['Year'], cause6, label='Heart disease')
plt.plot(cause7['Year'], cause7, label='Influenza and pneumonia')
plt.plot(cause8['Year'], cause8, label='Kidney disease')
plt.plot(cause9['Year'], cause9, label='Stroke')
plt.plot(cause10['Year'], cause10, label='Suicide')

plt.xlabel('Year')
plt.ylabel('Number of Deaths')
plt.title('Number of Deaths by Cause Over Time')

# Display the legend
#plt.legend()

# Show the plot
plt.show()


# In[ ]:


cause1 = df[df['Cause Name'] == 'Unintentional injuries']
cause2 = df[df['Cause Name'] == "Alzheimer's disease"]
cause1=cause1.groupby('Year')['Deaths'].sum().reset_index()
cause2=cause2.groupby('Year')['Deaths'].sum().reset_index()

plt.plot(cause1['Year'], cause1['Deaths'], label='Unintentional injuries')
plt.plot(cause2['Year'], cause2['Deaths'], label="Alzheimer's disease")

plt.xlabel('Year')
plt.ylabel('Number of Deaths')
plt.title('Number of Deaths by Cause Over Time')

plt.legend()
plt.show()


# In[ ]:





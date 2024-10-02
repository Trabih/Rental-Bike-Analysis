import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Set the seaborn style
sns.set(style='dark')

# Streamlit dashboard header
st.header('Bike Rentals Dashboard')
# Load the datasets
summer_jam_2011 = pd.read_csv("streamlit/summer_jam_2011.csv")  
summer_jam_2012 = pd.read_csv("streamlit/summer_jam_2012.csv")  
summer_hari_2011 = pd.read_csv("streamlit/summer_hari_2011.csv")  
summer_hari_2012 = pd.read_csv("streamlit/summer_hari_2012.csv")

start_date = st.sidebar.date_input('Start Date', value=pd.to_datetime('2011-06-01'))
end_date = st.sidebar.date_input('End Date', value=pd.to_datetime('2012-09-30'))


summer_jam_2011_filtered = summer_jam_2011[(summer_jam_2011['dteday'] >= str(start_date)) & (summer_jam_2011['dteday'] <= str(end_date))]
summer_jam_2012_filtered = summer_jam_2012[(summer_jam_2012['dteday'] >= str(start_date)) & (summer_jam_2012['dteday'] <= str(end_date))]
summer_hari_2011_filtered = summer_hari_2011[(summer_hari_2011['dteday'] >= str(start_date)) & (summer_hari_2011['dteday'] <= str(end_date))]
summer_hari_2012_filtered = summer_hari_2012[(summer_hari_2012['dteday'] >= str(start_date)) & (summer_hari_2012['dteday'] <= str(end_date))]

# Question 1: Visualizations
st.subheader('Question 1: Average Bike Rentals per Hour in 2012')
avg_2012 = summer_jam_2012_filtered.groupby('hr')['cnt'].mean().reset_index()
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x=avg_2012['hr'], y=avg_2012['cnt'], ax=ax, palette='viridis')
ax.set_xlabel('Hour of the Day')
ax.set_ylabel('Average Bike Rentals')
ax.set_title('Average Bike Rentals per Hour in 2012')
st.pyplot(fig)

# Correlation Matrix for Question 1
st.subheader("Correlation Matrix of Weather Variables and Bike Rentals (Summer 2012)")
interesting = ['temp', 'atemp', 'hum', 'windspeed', 'cnt']
corr_summer_jam_2012 = summer_jam_2012_filtered[interesting].corr()
plt.figure(figsize=(10, 6))
sns.heatmap(corr_summer_jam_2012, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title("Correlation Matrix - Summer 2012")
st.pyplot(plt)


# Question 2: Total bike rentals
st.subheader('Question 2: Total Bike Rentals in Summer')
total_summer_jam_2011 = summer_jam_2011_filtered['cnt'].sum()
total_summer_jam_2012 = summer_jam_2012_filtered['cnt'].sum()
total_summer_hari_2011 = summer_hari_2011_filtered['cnt'].sum()
total_summer_hari_2012 = summer_hari_2012_filtered['cnt'].sum()
fig, axes = plt.subplots(1, 2, figsize=(12, 5))
axes[0].bar(['Summer Jam 2011', 'Summer Jam 2012'], [total_summer_jam_2011, total_summer_jam_2012], color=['blue', 'orange'])
axes[0].set_title('Total Bike Rentals (Jam) in Summer')
axes[0].set_ylabel('Total Rentals')
axes[1].bar(['Summer Hari 2011', 'Summer Hari 2012'], [total_summer_hari_2011, total_summer_hari_2012], color=['blue', 'orange'])
axes[1].set_title('Total Bike Rentals (Hari) in Summer')
axes[1].set_ylabel('Total Rentals')
plt.tight_layout()
st.pyplot(fig)

# Average bike rentals in summer
avg_summer_jam_2011 = total_summer_jam_2011 / len(summer_jam_2011_filtered)
avg_summer_jam_2012 = total_summer_jam_2012 / len(summer_jam_2012_filtered)
avg_summer_hari_2011 = total_summer_hari_2011 / len(summer_hari_2011_filtered)
avg_summer_hari_2012 = total_summer_hari_2012 / len(summer_hari_2012_filtered)
fig, axes = plt.subplots(1, 2, figsize=(12, 5))
axes[0].bar(['Summer Jam 2011', 'Summer Jam 2012'], [avg_summer_jam_2011, avg_summer_jam_2012], color=['blue', 'orange'])
axes[0].set_title('Average Bike Rentals Per Day (Jam) in Summer')
axes[0].set_ylabel('Average Rentals')
axes[1].bar(['Summer Hari 2011', 'Summer Hari 2012'], [avg_summer_hari_2011, avg_summer_hari_2012], color=['blue', 'orange'])
axes[1].set_title('Average Bike Rentals Per Day (Hari) in Summer')
axes[1].set_ylabel('Average Rentals')
plt.tight_layout()
st.pyplot(fig)

#Line graph
summer_hourly_jam_2011 = summer_jam_2011_filtered.groupby('hr')['cnt'].mean()
summer_hourly_jam_2012 = summer_jam_2012_filtered.groupby('hr')['cnt'].mean()
plt.figure(figsize=(10, 6))
plt.plot(summer_hourly_jam_2011.index, summer_hourly_jam_2011.values, label='Summer Jam 2011', color='blue', marker='o')
plt.plot(summer_hourly_jam_2012.index, summer_hourly_jam_2012.values, label='Summer Jam 2012', color='orange', marker='o')
plt.title('Average Hourly Bike Rentals in Summer 2011 vs. 2012 (Jam)')
plt.xlabel('Hour of the Day')
plt.ylabel('Average Number of Rentals')
plt.legend()
plt.grid(True)
st.pyplot(plt)

# Correlation Graph
corr_summer_jam_2011 = summer_jam_2011[interesting].corr()
corr_summer_jam_2012 = summer_jam_2012[interesting].corr()
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
sns.heatmap(corr_summer_jam_2011, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title("Weather and Bike Rentals Correlation (Summer Jam 2011)")
plt.subplot(1, 2, 2)
sns.heatmap(corr_summer_jam_2012, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title("Weather and Bike Rentals Correlation (Summer Jam 2012)")
plt.tight_layout()
st.pyplot(plt)


st.caption('Copyright (c) Tengku Rabih Razzan 2024')

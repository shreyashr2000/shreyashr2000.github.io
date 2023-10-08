import matplotlib.pyplot as plt
import pandas as pd

# Load the data
csv_file = 'CGHS_data.csv'
df = pd.read_csv(csv_file, header=None)

# Select the relevant data
selected_cities = ['PUNE', 'MUMBAI', 'CHENNAI', 'DELHI/NCR', 'BENGALURU', 'KOLKATA']
selected_rows = df[df[1].isin(selected_cities)]
new_df = selected_rows[[1, 5]]
new_df.columns = ['City', 'Num_Doctors']
new_df_copy = new_df.copy()
new_df_copy['Num_Doctors'] = pd.to_numeric(new_df_copy['Num_Doctors'], errors='coerce')

# Create a figure with multiple subplots
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 6))

# Plot the line plot
ax1.plot(years, budget_allocation, marker='o', label='Budget Allocation (in crore)')
ax1.plot(years, revised_estimates, marker='o', label='Revised Estimates (in crore)')
ax1.plot(years, actual_expenditure, marker='o', color='red', label='Actual Expenditure (in crore)')
ax1.set_title('Budget Details for Department of Sports Over the Years', fontsize=18)
ax1.set_xlabel('Year', fontsize=18)
ax1.set_ylabel('Amount in Crore', fontsize=18)
ax1.legend(fontsize=18)
ax1.grid(which='both', color='black')
ax1.minorticks_on()
ax1.grid(which='minor', linestyle=':', linewidth='0.5', color='grey')

# Plot the scatter plot
ax2.scatter(grants_received, num_events_conducted, c='blue', marker='o',s=80, label='Number of Events')
ax2.set_xlabel('Grants Received in Cr', fontsize=18)
ax2.set_ylabel('Number of Events', color='blue', fontsize=18)
ax2.tick_params(axis='both', which='both', labelsize=18, width=1.5)
ax2.minorticks_on()
ax2.grid(which='minor', linestyle=':', linewidth='0.5', color='grey')
ax2.grid(which='major', color='black')

# Add a legend to the scatter plot
ax2.legend(fontsize=16)

# Plot the box plot
ax3.boxplot([new_df_copy[new_df['City'] == city]['Num_Doctors'] for city in selected_cities], labels=selected_cities)
ax3.set_title('Doctors in Wellness Centres', fontsize=18)
ax3.set_xlabel('City', fontsize=18)
ax3.minorticks_on()
ax3.grid(which='minor', linestyle=':', linewidth='0.5',color='grey',axis='y')
ax3.grid(which='major', color='black',axis='y')
ax3.yticks( fontsize=18)
ax3.

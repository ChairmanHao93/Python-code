import folium
import pandas as pd

# Read data from the Excel file
excel_file_path = r'C:\Users\h.zhang.2\Desktop\Hao Restaurant coordinates-.xlsx'
df = pd.read_excel(excel_file_path)

# Print the columns to check their names
print("Columns in DataFrame:", df.columns)

# Create a base map centered at the mean coordinates of the data
map_center = [df['Coordinates (Latitude)'].mean(), df['Coordinates (Longitude)'].mean()]
my_map = folium.Map(location=map_center, zoom_start=10)

# Add markers for each data point
for index, row in df.iterrows():
    account_name = row['Account Name']
    latitude = row['Coordinates (Latitude)']
    longitude = row['Coordinates (Longitude)']

    # Check if the columns exist before accessing them
    monthly_gfv = int(row['Monthly GFV']) if 'Monthly GFV' in df.columns else 0
    
    # Fix the typo in the column name
    discount = row['Discount'] if 'Discount' in df.columns else ''
    ncr = row['NCR'] if 'NCR' in df.columns else ''

    # Create a popup message for the marker
    popup_message = (
        f"Account Name: {account_name}<br>"
        f"Monthly GFV: {monthly_gfv}<br>"
        f"Discount: {discount}<br>"
        f"NCR: {ncr}"
    )

    # Add marker to the map
    folium.Marker(
        location=[latitude, longitude],
        popup=popup_message,
        icon=folium.Icon(color='blue')
    ).add_to(my_map)

# Save the map as an HTML file
my_map.save('Hao vendors interactive_map.html')

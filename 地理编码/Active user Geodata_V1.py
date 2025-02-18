import pandas as pd
from geopy.geocoders import Nominatim
import folium

# Load the data
data = pd.read_excel(r'C:\Users\h.zhang.2\Desktop\finland_customers.xlsx')

# Initialize geolocator
geolocator = Nominatim(user_agent="geoapiExercises")

# Function to get latitude and longitude
def get_lat_lon(zip_code):
    location = geolocator.geocode(f"{zip_code}, Finland")
    if location:
        return location.latitude, location.longitude
    else:
        return None, None

# Apply function to get coordinates
data[['Latitude', 'Longitude']] = data['Zip Code'].apply(lambda x: pd.Series(get_lat_lon(x)))

# Drop rows where geocoding failed
data = data.dropna(subset=['Latitude', 'Longitude'])

# Print the data to check
print(data.head())

# Create a base map centered around Finland
map = folium.Map(location=[64.00, 26.00], zoom_start=5)

# Add points to the map
for idx, row in data.iterrows():
    folium.CircleMarker(
        location=[row['Latitude'], row['Longitude']],
        radius=row['Active Customers'] / 50,  # Adjust the radius as needed
        popup=f"Zip Code: {row['Zip Code']}<br>Active Customers: {row['Active Customers']}",
        color='blue',
        fill=True,
        fill_color='blue'
    ).add_to(map)

# Save the map to an HTML file
map.save('finland_customers_map.html')

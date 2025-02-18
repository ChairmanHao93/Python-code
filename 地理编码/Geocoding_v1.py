from geopy.geocoders import Nominatim
import pandas as pd

# Replace 'your_excel_file.xlsx' with your Excel file's path
input_excel_file = r"C:\Users\h.zhang.2\Desktop\address.xlsx"
output_excel_file = r"C:\Users\h.zhang.2\Desktop\geocoded_addresses.xlsx"


# Load your Excel sheet into a pandas DataFrame
df = pd.read_excel(input_excel_file)

# Initialize the Nominatim geocoder
geolocator = Nominatim(user_agent="myGeocoder")

# Create empty lists to store latitude and longitude
latitudes = []
longitudes = []

# Adjust 'AddressColumn' to the name of the column in your Excel file that contains addresses
for address in df['Column1']:
    location = geolocator.geocode(address)
    if location:
        latitudes.append(location.latitude)
        longitudes.append(location.longitude)
    else:
        # Handle cases where geocoding fails for an address
        latitudes.append(None)
        longitudes.append(None)

# Add the latitude and longitude columns to your DataFrame
df['Latitude'] = latitudes
df['Longitude'] = longitudes

# Save the DataFrame with latitude and longitude back to a new Excel file
df.to_excel(output_excel_file, index=False)

print(f"Geocoded data saved to {output_excel_file}")

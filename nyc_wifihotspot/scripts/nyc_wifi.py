import os
import pandas as pd

#Load CSV
nyc_wifihotspot = pd.read_csv('data/nyc_wifilocation.csv')

print(nyc_wifihotspot.columns.tolist())

print("Wifi Hotspots:")
print(nyc_wifihotspot.head(10))

# Drop rows with missing coordinates
nyc_wifihotspot.dropna(subset=['Longitude', 'Latitude'], inplace=True)

#Filter only free public Wi-Fi locations
nyc_wifihotspot = nyc_wifihotspot[nyc_wifihotspot['Type'] == "Free Public Wi-Fi"]

# Rename a few columns to snake_case (e.g. SSID, Borough, Location, etc.)
nyc_wifihotspot.rename(columns={
      'SSID': 'ssid',
    'Borough': 'borough',
    'Location': 'location'
}, inplace=True)

nyc_wifihotspot.to_csv('output/cln_nychotspot.csv', index=False)
print("Success!")




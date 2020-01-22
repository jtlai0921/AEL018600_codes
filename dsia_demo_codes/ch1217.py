import pandas as pd
import folium

pm25_url = "https://storage.googleapis.com/ds_data_import/2017_avg_pm25.csv"
pm25 = pd.read_csv(pm25_url)
# 調整臺為台
pm25["county"] = pm25["county"].str.replace("臺", "台")
# 調整桃園市為桃園縣
pm25["county"] = pm25["county"].str.replace("桃園市", "桃園縣")
geojson = "twCounty2010.geo.json"

m = folium.Map(location=[24, 121], zoom_start=7)

m.choropleth(
    geo_data=geojson,
    name='choropleth',
    data=pm25,
    columns=['county', 'avg_pm25'],
    key_on='feature.properties.COUNTYNAME',
    fill_color='RdYlGn_r',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='PM2.5'
)

folium.LayerControl().add_to(m)
m
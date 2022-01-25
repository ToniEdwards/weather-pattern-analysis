import pandas as pd

#load
data_file = "city_data.csv"

#create df
cityData_df = pd.read_csv(data_file)

#export to html
cityData_df.to_html("data_export.html",index=False)
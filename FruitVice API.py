import requests
import json
import pandas as pd

# We will obtain the fruitvice API data using requests.get("url") function.
# The data is in a json format.
data = requests.get("https://www.fruityvice.com/api/fruit/all")

# We will retrieve results using json.loads() function.
results = json.loads(data.text)

# We will convert our json data into pandas data frame.
pd.DataFrame(results)

# The result is in a nested json format.
# The 'nutrition' column contains multiple subcolumns, so the data needs to be 'flattened' or normalized.
df2 = pd.json_normalize(results)

cal_banana = df2.loc[df2["name"] == 'Banana']

cal_banana.iloc[0]['nutritions.calories']
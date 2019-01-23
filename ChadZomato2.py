#!/usr/bin/env python
# coding: utf-8

# In[178]:


# def get_results(start_index, cuisines):
import requests
import pandas as pd
import matplotlib as plt
import seaborn as sns
def get_results(start_index,cuisine):
    headers = {
        'Accept': 'application/json',
        'user-key': '4acc54ca3cf4e3c53521751bd0a2ca40',
    }

    params = (
        ('entity_id', '305'),
        ('entity_type', 'city'),
        ('start', start_index ),
        ('cuisines', [cuisine])
    )
    
    url = 'https://developers.zomato.com/api/v2.1/search'
    response = requests.get(url, headers=headers, params=params)
    return response.json()


#x = get_results(0)
num_rows=120
step=10
all_results = []
choice_cuisines=[168]
for x in range(0, num_rows, step):
    for cuisine in choice_cuisines:
        try:
            # get the data
            temp_result = get_results(x,cuisine)
            all_results.append(temp_result)

        except Exception as e:
            print(e, x)
# for i in all_results:
#     print(i)
#     print("\n\n\n")
# import requests

# headers = {
#     'Accept': 'application/json',
#     'user-key': '4acc54ca3cf4e3c53521751bd0a2ca40',
# }

# params = (
#     ('entity_id', '305'),
#     ('entity_type', 'city'),
# )

# response = requests.get('https://developers.zomato.com/api/v2.1/search?entity_id=305&entity_type=city&start=80&count=20', headers=headers)

# #NB. Original query string below. It seems impossible to parse and
# #reproduce query strings 100% accurately so the one below is given
# #in case the reproduced version is not "correct".
# # response = requests.get('https://developers.zomato.com/api/v2.1/location_details?entity_id=305&entity_type=city', headers=headers)

# response.json().get('restaurants')[].get('restaurant').get('name')


# In[179]:


for_df = []
num_loops=num_rows//step
for n in range(num_loops):
    t=all_results[n]['restaurants']
    for i in t:
        name=i['restaurant']['name']
        agg_rating=i['restaurant']['user_rating']['aggregate_rating']
        text_rating=i['restaurant']['user_rating']['rating_text']
        votes=i['restaurant']['user_rating']['votes']
        cuisines=i['restaurant']['cuisines']
        
#         print(i['restaurant'])
#         print("\n\n")
        to_append = (name,agg_rating,text_rating,votes,cuisines)
        for_df.append(to_append)
    #     print(i)

pd.DataFrame(for_df,columns=["Name","Rating","Text_Rating","Votes","Cuisines"])


# In[ ]:


start_index = 0

headers = {
    'Accept': 'application/json',
    'user-key': '4acc54ca3cf4e3c53521751bd0a2ca40'
    }

params = (
        ('entity_id', '305'),
        ('entity_type', 'city'),
        ('cuisines', 168),
        ('start', start_index)
    )
    
url = 'https://developers.zomato.com/api/v2.1/search'
response_test = requests.get(url, headers=headers, params=params)


# In[ ]:


for_df = []

for row in all_results:
    for restaurant in row.get('restaurants'):
        for_df.append(restaurant.get('restaurant'))
        
    
df = pd.DataFrame.from_records(for_df)

df['res_id'] = df['R'].map(lambda x: x.get('res_id'))
df['lat'] = df['location'].map(lambda x: x.get('latitude'))
df['lng'] = df['location'].map(lambda x: x.get('longitude'))
df['aggregate_rating'] = df['user_rating'].map(lambda x: x.get('aggregate_rating'))
df['rating_text'] = df['user_rating'].map(lambda x: x.get('rating_text'))
df['votes'] = df['user_rating'].map(lambda x: x.get('votes'))
# df['cuisines'] = df['location'].map(lambda x: x.get('zipcode'))

keep = ['res_id', 'name', 'lat','lng','cuisines','aggregate_rating','rating_text','votes']
newdf = df[keep].copy()

newdf.head()
newdf
# # all_burgers = ["American, Burger, Mexican"]
# burgerjoint = newdf[newdf['cuisines'] =='Burger']
# burgerjoint

# for cuisine in cuisines:
#     if "cuisines' = 'Burgers'
#     print(cuisines)

# burgerjoint

# loop with conditions
#     for x in newdf:
#     if burgerjoint == True:
#             print(burgerjoint)
        
# x = burgers()   
    # iloc: data.loc[<row selection>, <column selection>] .

# # Use `iloc[]` to select row `0`
# print(df.iloc[_])

# # Use `loc[]` to select column `'A'`
# print(df.loc[:,'_'])


# In[ ]:





# In[ ]:





# In[ ]:





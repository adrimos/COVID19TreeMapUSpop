# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
# Setting up the environment.
import numpy as np
import pandas as pd
from scipy import stats
import plotly as pl


# %%
# Load the data from the John Hopkins github repo
df = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/04-26-2020.csv')
dfpop = pd.read_csv('USpopCounties.csv')

# %%
# Dropping some columns and sorting

df1 = df[["Admin2", "Province_State", "Country_Region", "Confirmed", "Deaths", "Combined_Key"]] #getting the columns I want
df1 = df1[(df1["Country_Region"] == "US")] #dropping countries other than the US
df1 = df1.rename(columns={'Province_State': 'State'})
df1 = df1.rename(columns={'Admin2': 'County'})
df1 = df1.rename(columns={'Country_Region': 'Country'})
df1 = df1.rename(columns={'Combined_Key': 'County/State'})

# %%
# checking a match in column banes to merge by County/State
set(df1.columns).intersection(set(dfpop.columns))

# %%
# changes to make the columns equal to be able to merge
dfpop['County/State'] = dfpop['County/State'].str.replace(r' County', '')
dfpop['County/State'] = dfpop['County/State'] + ', US'

# %%
# Converting lower case to title case
#dfpop['County/State'] = dfpop['County/State'].str.upper().str.title()

# %%
# checking  how many cells are the same and how many are different
df1['County/State'].isin(dfpop['County/State']).value_counts()

# %%
# Merging dfpop into df1 to get the population count
dfpopmerged = pd.merge(left=df1, right=dfpop, how='left', left_on='County/State', right_on='County/State')

# %%
# there are some issues with the merge. Names of counties are different
dfpopmerged.isnull().sum()


# %%
#dfpopmerged = dfpopmerged.replace({'Population': {1: 62568}})
dfpopmerged.at[1,'Population']= 62568
dfpopmerged.at[32,'Population']= 156505
dfpopmerged.at[43,'Population']= 25661
dfpopmerged.at[52,'Population']= 296112
dfpopmerged.at[81,'Population']= 121176
dfpopmerged.at[88,'Population']= 22714
dfpopmerged.at[104,'Population']= 40882
dfpopmerged.at[113,'Population']= 614700
dfpopmerged.at[142,'Population']= 887
dfpopmerged.at[145,'Population']= 36769
dfpopmerged.at[180,'Population']= 18040
dfpopmerged.at[184,'Population']= 13668
dfpopmerged.at[215,'Population']= 126131
dfpopmerged.at[242,'Population']= 16843
dfpopmerged.at[268,'Population']= 6399
dfpopmerged.at[297,'Population']= 248361
dfpopmerged.at[300,'Population']= 200182
dfpopmerged.at[302,'Population']= 9996
dfpopmerged.at[325,'Population']= 6868
dfpopmerged.at[382,'Population']= 9893
dfpopmerged.at[392,'Population']= 613
dfpopmerged.at[408,'Population']= 47042
dfpopmerged.at[432,'Population']= 237820
dfpopmerged.at[462,'Population']= 16153
dfpopmerged.at[545,'Population']= 17593
dfpopmerged.at[563,'Population']= 20021
dfpopmerged.at[585,'Population']= 5582
dfpopmerged.at[647,'Population']= 41512
dfpopmerged.at[665,'Population']= 27463
dfpopmerged.at[717,'Population']= 218195
dfpopmerged.at[739,'Population']= 28656
dfpopmerged.at[751,'Population']= 444094
dfpopmerged.at[752,'Population']= 7225
dfpopmerged.at[753,'Population']= 19499
dfpopmerged.at[783,'Population']= 5381
dfpopmerged.at[797,'Population']= 33636
dfpopmerged.at[799,'Population']= 99653
dfpopmerged.at[801,'Population']= 23865
dfpopmerged.at[807,'Population']= 14067
dfpopmerged.at[825,'Population']= 1419
dfpopmerged.at[861,'Population']= 20322
dfpopmerged.at[876,'Population']= 8211
dfpopmerged.at[879,'Population']= 28469
dfpopmerged.at[899,'Population']= 6638
dfpopmerged.at[965,'Population']= 22348
dfpopmerged.at[1045,'Population']= 135583
dfpopmerged.at[1083,'Population']= 49973
dfpopmerged.at[1145,'Population']= 22529 #hopewell
dfpopmerged.at[1183,'Population']= 29099 #iberia
dfpopmerged.at[1184,'Population']= 32511 #iberville
dfpopmerged.at[1218,'Population']= 15902 #jackson
dfpopmerged.at[1253,'Population']= 432943 #jefferson
dfpopmerged.at[1268,'Population']= 31368  #jefferson davis
dfpopmerged.at[1300,'Population']= 31974 #juneau
dfpopmerged.at[1309,'Population']= 491918 #kansas city
dfpopmerged.at[1317,'Population']= 58708 #kenai peninsula
dfpopmerged.at[1331,'Population']= 13901 #ketchikan
dfpopmerged.at[1359,'Population']= 12998 #kodiak island
dfpopmerged.at[1371,'Population']= 14892 #lasalle
dfpopmerged.at[1377,'Population']= 244390 #lafayette
dfpopmerged.at[1382,'Population']= 96714 #lafourche
dfpopmerged.at[1467,'Population']= 7446 #lexington
dfpopmerged.at[1480,'Population']= 46742 #lincoln
dfpopmerged.at[1505,'Population']= 140789 #livingtson
dfpopmerged.at[1540,'Population']= 82168 #lynchburg
dfpopmerged.at[1566,'Population']= 10951 #madison
dfpopmerged.at[1582,'Population']= 41085 #manasas
dfpopmerged.at[1583,'Population']= 17478 #manasas park
dfpopmerged.at[1630,'Population']= 12554 #martinsville
dfpopmerged.at[1639,'Population']= 108317 #matanuska susitna
dfpopmerged.at[1707,'Population']= 42628 #michigan department of corrections
dfpopmerged.at[1790,'Population']= 24874 #marehouse
dfpopmerged.at[1831,'Population']= 38158 #natchitoches
dfpopmerged.at[1849,'Population']= 8398748 #mew york
dfpopmerged.at[1853,'Population']= 180994 #newport news
dfpopmerged.at[1872,'Population']= 10004 #nome
dfpopmerged.at[1874,'Population']= 242742 #norfolk
dfpopmerged.at[1881,'Population']= 3981 #norton
dfpopmerged.at[1930,'Population']= 391006 #orleans
dfpopmerged.at[1953,'Population']= 153279 #ouachita
dfpopmerged.at[1954,'Population']= 4952 #ouray
dfpopmerged.at[2018,'Population']= 3266 #petersburg
dfpopmerged.at[2019,'Population']= 31346 #petersburg
dfpopmerged.at[2058,'Population']= 23197 #plaquemines
dfpopmerged.at[2067,'Population']= 21730 #pointe coupee
dfpopmerged.at[2084,'Population']= 12271 #poquoson
dfpopmerged.at[2088,'Population']= 94398 #portsmouth
dfpopmerged.at[2110,'Population']= 6203 #prince of wales-hyder
dfpopmerged.at[2134,'Population']= 18249 #radford
dfpopmerged.at[2151,'Population']= 121648 #rapides
dfpopmerged.at[2156,'Population']= 8442 #red river
dfpopmerged.at[2170,'Population']= 20192 #richland
dfpopmerged.at[2179,'Population']= 228783 #richmond city
dfpopmerged.at[2190,'Population']= 94073 #roanoke
dfpopmerged.at[2227,'Population']= 23884 #sabine
dfpopmerged.at[2234,'Population']= 24836 #salem
dfpopmerged.at[2363,'Population']= 6893 #southeast fairbanks
dfpopmerged.at[2374,'Population']= 47244 #st. bernard
dfpopmerged.at[2375,'Population']= 53100 #st. charles
dfpopmerged.at[2384,'Population']= 10132 #st. helena
dfpopmerged.at[2385,'Population']= 21096 #st. james
dfpopmerged.at[2386,'Population']= 42837 #st. john the baptist
dfpopmerged.at[2390,'Population']= 82124 #st. landry
dfpopmerged.at[2394,'Population']= 300576 #st. louis city
dfpopmerged.at[2396,'Population']= 79210 #st. martin
dfpopmerged.at[2397,'Population']= 49348 #st. mary
dfpopmerged.at[2399,'Population']= 258111 #st. tammany
dfpopmerged.at[2412,'Population']= 24932 #staunton
dfpopmerged.at[2439,'Population']= 98108 #suffolk
dfpopmerged.at[2476,'Population']= 134758 #tangipahoa
dfpopmerged.at[2492,'Population']= 4334 #tensas
dfpopmerged.at[2493,'Population']= 110461 #terrebonne
dfpopmerged.at[2613,'Population']= 22330 #union
dfpopmerged.at[2643,'Population']= 59611 #vermilion
dfpopmerged.at[2645,'Population']= 47429 #vernon
dfpopmerged.at[2651,'Population']= 449974 #virginia beach
dfpopmerged.at[2707,'Population']= 46194 #washington, louisiana
dfpopmerged.at[2747,'Population']= 22628 #waynesboro
dfpopmerged.at[2750,'Population']= 260213 #weber
dfpopmerged.at[2754,'Population']= 38340 #webster, louisiana
dfpopmerged.at[2761,'Population']= 26465 #west baton rouge
dfpopmerged.at[2762,'Population']= 10830 #west carroll
dfpopmerged.at[2763,'Population']= 15568 #west feliciana
dfpopmerged.at[2800,'Population']= 13389 #williamsburg
dfpopmerged.at[2808,'Population']= 28078 #mwinchester
dfpopmerged.at[2813,'Population']= 13904 #winn
dfpopmerged.at[2869,'Population']= 5230 #yukon koyukuk
dfpopmerged.at[2876,'Population']= 165768 #guam
dfpopmerged.at[2877,'Population']= 56882 #northern mariana
dfpopmerged.at[2878,'Population']= 3193694 #puerto rico
dfpopmerged.at[2880,'Population']= 106977 #virgin islands


# %%
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd

levels = ['County/State', 'State'] # levels totaled for the hierarchical chart
color_columns = 'Deaths'
value_column = 'Population'

def build_hierarchical_dataframe(df, levels, value_column, color_columns=None):
    """
    Build a hierarchy of levels for Sunburst or Treemap charts.

    Levels are given starting from the bottom to the top of the hierarchy,
    ie the last level corresponds to the root.
    """
    df_all_trees = pd.DataFrame(columns=['id', 'parent', 'value', 'color'])
    for i, level in enumerate(levels):
        df_tree = pd.DataFrame(columns=['id', 'parent', 'value', 'color'])
        dfg = df.groupby(levels[i:]).sum()
        dfg = dfg.reset_index()
        df_tree['id'] = dfg[level].copy()
        if i < len(levels) - 1:
            df_tree['parent'] = dfg[levels[i+1]].copy()
        else:
            df_tree['parent'] = 'total'
        df_tree['value'] = dfg[value_column]
        df_tree['color'] = dfg[color_columns]
        df_all_trees = df_all_trees.append(df_tree, ignore_index=True)
    total = pd.Series(dict(id='total', parent='',
                              value=df[value_column].sum(),
                              color=df[color_columns].sum()
                              ))
    df_all_trees = df_all_trees.append(total, ignore_index=True)
    return df_all_trees


df_all_trees = build_hierarchical_dataframe(dfpopmerged, levels, value_column, color_columns)
avg = df1['Confirmed'].mean()

# %%
# Creating a categorical column to use in the treemap to use colors for each state
codes = pd.DataFrame(df_all_trees['parent'].astype('category'))
codes["parent"] = codes["parent"].cat.codes
df_all_trees['codes'] = codes['parent']

# %%
fig = make_subplots(1, 1, specs=[[{"type": "domain"}]])

fig.add_trace(go.Treemap(
    labels=df_all_trees['id'],
    parents=df_all_trees['parent'],
    values=df_all_trees['value'],
    branchvalues='total',
    marker=dict(
        colors=df_all_trees['codes'],
        colorscale='matter',
        #cmid=0.5
        ),
    hovertemplate='<b>%{label} </b> <br> Population: %{value:,.2s}<br> %{percentParent:,.2%} of total<extra></extra>',
    texttemplate='<b>%{label} </b> <br> Population %{value:,.2s} <br> %{percentParent:,.2%} of total<br>',
    maxdepth=3,
    meta=df_all_trees['codes']
    ), 1, 1)

fig.update_layout(
    title='Population per state and county as percentage of total in the US',
    title_x=0.5,
    hoverlabel=dict(
            bgcolor="white",
            font_size=16,
            font_color="#595959",
            font_family="Arial",
            bordercolor='#595959'
            ),
    )
fig.show()

import plotly.io as pio
pio.write_html(fig, file='Index.html', auto_open=True)

# %%

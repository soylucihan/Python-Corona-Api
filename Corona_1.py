import urllib.request
import json
import matplotlib.pyplot as plt
import numpy as np


veriler = json.load(urllib.request.urlopen("https://api.covid19api.com/countries"))
countries=dict()

for veri in veriler:
    countries[veri["Country"]]=veri["ISO2"]
    
print(countries)
country=input("Please Select Country and Press Enter: ")
veriler = json.load(urllib.request.urlopen("https://api.covid19api.com/total/dayone/country/"+country))
confirmed=[]
deaths=[]
recovered=[]
date=[]
daily=[]

for veri in veriler:
    confirmed.append(veri["Confirmed"])
    deaths.append(veri["Deaths"])
    recovered.append(veri["Recovered"])
    date.append(veri["Date"])


plt.plot(confirmed,color='mediumvioletred')
plt.ylabel('Total Case')

plt.show()

plt.plot(deaths,color='mediumvioletred')
plt.ylabel('Total Death')

plt.show()

plt.plot(recovered,color='mediumvioletred')
plt.ylabel('Recovered')

plt.show()

print ("Confirmed:",confirmed)
print ("Deaths:", deaths)
print ("Recovered:",recovered)

for i in range(len(confirmed)):
    if i==0:
        daily.append(1)
    else:
        daily.append(confirmed[i]-confirmed[i-1])

print("Daily Case:",daily)

index = np.arange(len(date))
plt.bar(index,daily,color='mediumvioletred')
plt.xlabel('Days', fontsize=15)
plt.ylabel('Cases', fontsize=15)
plt.xticks(index, index, fontsize=7, rotation=90)
plt.title('Daily Cases')
fig = plt.get_current_fig_manager()
fig.full_screen_toggle()
plt.show()



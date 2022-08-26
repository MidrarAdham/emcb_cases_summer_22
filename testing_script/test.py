import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import matplotlib.ticker as ticker

path='/home/parallels/Desktop/emcb_use_cases22/emcb_cases_summer_22/cold_load_pickup/Util10-6/aug_25/voltage_and_current/circuit-breaker-power-quality.csv'
df = pd.read_csv(path)

df['ti'] = (pd.to_datetime(df['time']).dt.strftime('%H:%M'))

fig, ax = plt.subplots(1,figsize=(12,8))
ax.plot(df['ti'],df['Voltage (A-B)'])
#ax.xaxis.set_major_locator(plt.Linear(15))
ax.xaxis.set_major_locator(ticker.LinearLocator(15))
ax.set_title('Voltage Variation, August 25')
plt.grid()
plt.show()

# plot_thingspeak.py
"""
A Python script that plots live data from Thingspeak.com using Matplotlib
inspiration from:
https://learn.sparkfun.com/tutorials/graph-sensor-data-with-python-and-matplotlib/update-a-graph-in-real-time
"""
import time
import datetime as dt
import requests
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#plt.style.use('fivethirtyeight')

url1 = "https://api.thingspeak.com/channels/9/fields/1.json?results=1"
url2 = "https://api.thingspeak.com/channels/9/fields/2.json?results=1"

# function to pull out a float from the requests response object
def pull_float(response, field_num='1'):
    jsonr = response.json()
    field_str = 'field'+field_num
    strr = jsonr['feeds'][0][field_str]
    fltr = round(float(strr),2)
    return fltr

# Create figure for plotting
fig, ax = plt.subplots()
xs = []
ys1 = []
ys2 = []

def animate(i, xs:list, ys1:list, ys2:list):
    # grab the data from thingspeak.com
    response1 = requests.get(url1)
    flt1 = pull_float(response1,'1')
    response2 = requests.get(url2)
    flt2 = pull_float(response2,'2')
    # Add x and y to lists
    xs.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
    ys1.append(flt1)
    ys2.append(flt2)
    # Limit x and y lists to 10 items
    xs = xs[-10:]
    ys1 = ys1[-10:]
    ys2 = ys2[-10:]
    # Draw x and y lists
    ax.clear()
    ax.plot(xs, ys1)
    # Format plot
    ax.set_ylim([175,225])
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('Light from ThingSpeak Channel 9')
    plt.ylabel('Light Reading')

# Set up plot to call animate() function periodically
ani = animation.FuncAnimation(fig, animate, fargs=(xs,ys1,ys2), interval=1000)
plt.show()

# -*- coding: utf-8 -*-
"""
Homework n3, made by Lumix888, for the Advanced Python course.
"""

import pandas as pd
import matplotlib
import cartopy
import cartopy.crs as ccrs
import matplotlib.pyplot as plt 

flights = pd.read_csv('flights_pre_COVID.csv',sep=';')
flights = flights.assign(Active=[False]*flights.shape[0])

active_flights = pd.read_csv('flights21.csv',sep=';').iloc[:,1:].values.flatten()
flights.loc[flights["IATA"].isin(active_flights), "Active"] = True
airports = pd.read_csv('airports.dat.txt')
flights = pd.merge(flights, airports[['IATA', 'Latitude', 'Longitude']], on="IATA")

plt.figure(figsize=(88, 88))
ax = plt.axes(projection=cartopy.crs.TransverseMercator(32))
ax.add_feature(cartopy.feature.BORDERS, linestyle='-', alpha=1)
ax.coastlines(resolution='110m')
ax.add_feature(cartopy.feature.OCEAN, facecolor=('lightblue'))
ax.gridlines()
ax.set_extent ((-7.5, 50, 34, 69), cartopy.crs.PlateCarree())


plt.title('Author: Luca Mizzi, RED: cancelled flights, GREEN: flights still active',
          font = {'family' : 'normal', 'weight' : 'bold', 'size' : 88})

i = 0

while i < 36:
    
    if flights.Active[i] == True: 
    
        plt.plot([flights.Longitude[0], flights.Longitude[i]], [flights.Latitude[0], flights.Latitude[i]],
             color='green', linewidth=5, marker='o',
             transform=ccrs.PlateCarree())
        
    else:
        
        plt.plot([flights.Longitude[0], flights.Longitude[i]], [flights.Latitude[0], flights.Latitude[i]],
             color='red', linewidth=5, marker='o',
             transform=ccrs.PlateCarree())
        

    plt.text(flights.Longitude[i] - 0.3, flights.Latitude[i] - 0.5, flights.IATA[i],
             horizontalalignment='right', 
             font = {'family' : 'normal', 'weight' : 'bold', 'size' : 88},           
             transform=ccrs.Geodetic())

    i += 1


if __name__ == "__main__":
    #flights.to_csv("flights.csv", index=False)
    #print(flights)
    #plt.show()
    plt.savefig("TallinFlights_lumizz.png")
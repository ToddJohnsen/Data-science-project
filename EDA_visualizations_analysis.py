# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 10:11:07 2015
@author: ToddJohnsen
"""


import pandas as pd
import csv
import matplotlib.pyplot as plt
import numpy as np
#
#
NHL_players= pd.read_csv("/Users/ToddJohnsen/Python/Data-science-project/Forecasting NHL All Star Teams/NHL_players.csv")
#
NHL_players_2015=  pd.read_csv("/Users/ToddJohnsen/Python/Data-science-project/Forecasting NHL All Star Teams/NHL_players_2015.csv")

corrMat =NHL_players.corr()

NHL_players.team= np.where(NHL_players.team != 'None',1,0)

NHL_players.team.value_counts().plot(kind = 'bar')

plt.title("Distribution of Honorees, (1 = Made Team)")  
#Only ??? players have made team


alpha_level = .35
NHL_players.pts[NHL_players.team ==0].plot(kind = 'hist',alpha=alpha_level)
NHL_players.pts[NHL_players.team ==1].plot(kind = 'hist')
plt.xlabel("Pts")
plt.ylabel("Points Distribution" )
plt.legend(('No team','NHL All Star Team', ),loc='best')




NHL_players.WS[NHL_players.team ==1].plot(kind = 'hist')
NHL_players.WS[NHL_players.team ==0].plot(kind = 'hist', alpha=alpha_level)
plt.legend(('NHL All Star Team', 'No team'),loc='best')
plt.xlabel("Win Shares")
plt.ylabel("Win Share Distribution" )



NHL_players.mp[NHL_players.team ==1].plot(kind = 'hist')
NHL_players.mp[NHL_players.team ==0].plot(kind = 'hist',alpha=alpha_level)
plt.legend(('NHL All Star Team', 'No team'),loc='best')
plt.xlabel("Minutes Played")
plt.ylabel("Minutes Played Distribution" )



NHL_players.PER[NHL_players.team ==1].plot(kind = 'kde')
NHL_players.PER[NHL_players.team ==0].plot(kind = 'kde',alpha=alpha_level)
plt.legend(('NHL All Star Team', 'No team'),loc='best')
plt.xlabel("Player Efficiency")
plt.ylabel("Player Efficiency Rating Distribution" )




# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 08:49 2015
The NHL All-Star team has been annual awarded bestowed to the best players in the league at the end of every season. 
Every year after the regular season the Professional Hockey Writers Association votes for the best performers over the season at each position. 
The top two players at each position are named to the First and Second All-Star Teams. 
The teams were first awarded at the end of the 1930-31 NHL Season. 
There are two-six man teams: First and Second.
It is suppsoed to be an assessment of the based players at their respective positions. 
Given that avaliable hockey data, can we predict which players will be voted into each team by the end of the 2014-15 season? 
Sourc: http://www.hockey-reference.com/
@author: ToddJohnsen
"""
import pandas as pd
import csv
import matplotlib.pyplot as plt
import numpy as np

#DATA
#BASIC ATTRIBUTES

#col_u = ["player","age","tm","pos","gp","cf","ca","cf_","cf_ rel","c/60","crel/60","ff","fa","ff_","ff_ rel","oish_","oisv_","pdo","ozs_","dzs_","toi/60","toi(ev)", "tk", "gv", "satt.", "thru_"]
#all_nba= pd.read_table("https://raw.githubusercontent.com/toddjohnsen/abresler.github.io/master/data/NHL/player_data/all_player_per_game/nhl_player_per_game_data_1930_2015.csv", header= 0,sep = ',',names = col_u)
all_nhl = pd.read_csv("/Users/ToddJohnsen/Python/Data-science-project/Forecasting NHL All Star Teams/all_nhl_abresler")

#all_nhl.to_csv('all_nba_abresler')

type(all_nnhl) #Data Frame
all_nhl.head(10) #Print first 10 rows
all_nhl.tail(10)#print last 10 rows
all_nhl.describe() # summarize all numeric  columns
all_nhl.dtypes #mixture of data types(integers, floats,string objects )
all_nhl.shape # There are currently 19030 rows and 32 columns
all_nhl.values #dataframe as array
all_nhl.info() #missing values in: pos, age


#Used Web Scraping to pull togehter more advanced statistics

nhl_advance = pd.read_csv("/Users/ToddJohnsen/Python/Data-science-project/Forecasting NHL All Star Teams/advanced_stats")
nhl_advance.head(10) #Print first 10 rows
nhl_advance.tail(10)#print last 10 rows
nhl_advance.describe() # summarize all numeric  columns
nhl_advance.dtypes #mixture of data types(integers, floats,string objects )
nhl_advance.shape # There are currently 18977 rows and 31 columns
nhl_advance.values #dataframe as array
nhl_advance.info() #missing values in: TS, ff% rel, oiSH%, TK, GV, G, A, PTS, +/-, PIM, EV, PP, SH, GW, S%, BLK, FOwin, FOloss, FO%

#Join on player name and season
#Create new variable in all_nhl

season_end = [int(sea[-4:]) for sea in all_nhl.season]
all_nhl['season_end'] = season_end

#Merge function, using inner join....?
all_stats = pd.merge(all_nhl, nba_advance,how = "inner", on = ['player', 'season_end'])

#Del variables
del all_stats['table_name']
del all_stats['season']
del all_stats['data_source']
del all_stats['scrape_time']
del all_stats['Unnamed: 0_x']
del all_stats['Rk']
del all_stats['Pos']
del all_stats['Age']
del all_stats['Tm']
del all_stats['G']
del all_stats['blnk']
del all_stats['blnk2']

all_stats[all_stats.sh_.isnull()] # players who did not have any shot attempts 
all_stats.sh_.fillna(value = 0, inplace = True)

all_stats[all_stats.g_.isnull()]   #players who did not have any goals
all_stats.g_.fillna(value = 0, inplace = True)

all_stats[all_stats.a_.isnull()] #players who did not have any assists
all_stats.a_.fillna(value = 0, inplace = True)

all_stats[all_stats.pts_.isnull()] #players who did not have any points
all_stats.pts_.fillna(value = 0, inplace = True)

#if missing used the median, because every playerwhere value was missing, played in games and had some form of contribution
#Were variables calculated consistently through out time. 
all_stats['+/-'].isnull().sum()
all_stats[all_stats.PIM.isnull()]
all_stats.+/-.fillna(value =all_stats.+/-.median(), inplace =True)

all_stats['S'].isnull().sum()
all_stats['S'].fillna(value =all_stats['S'].median(), inplace =True)

all_stats['S%'].isnull().sum()
all_stats[all_stats['S%'].isnull()]
all_stats['S%'].fillna(value =all_stats['S%'].median(), inplace =True)

all_stats['TOI'].isnull().sum()
all_stats[all_stats['TOI'].isnull()]
all_stats['TOI'].fillna(value =all_stats['TOI'].median(), inplace =True)
all_stats['ATOI'].isnull().sum()
all_stats[all_stats['ATOI'].isnull()]
all_stats['ATOI'].fillna(value =all_stats['ATOI'].median(), inplace =True)
all_stats['BLK'].isnull().sum()
all_stats[all_stats['BLK'].isnull()]
all_stats['BLK'].fillna(value =all_stats['WS'].median(), inplace =True)

all_stats['HIT'].isnull().sum()
all_stats[all_stats['HIT'].isnull()]
all_stats['HIT'].fillna(value =all_stats['HIT'].median(), inplace =True)

all_stats['FOwin'].isnull().sum()
all_stats[all_stats['FOwin'].isnull()]
all_stats['FOwin'].fillna(value =all_stats['OBPM'].median(), inplace =True)

all_stats['FOloss'].isnull().sum()
all_stats[all_stats['FOloss'].isnull()]
all_stats['FOloss'].fillna(value =all_stats['FOloss'].median(), inplace =True)

all_stats['FO%'].isnull().sum()
all_stats[all_stats['FO%'].isnull()]
all_stats['FO%'].fillna(value =all_stats['FO%'].median(), inplace =True)

all_stats['TOI/60'].isnull().sum()
all_stats[all_stats['TOI/60'].isnull()]
all_stats['TOI/60'].fillna(value =all_stats['TOI/60'].median(), inplace =True)


#Everything else kept 0 because these attributes were not used until later. 
all_stats['CF'].isnull().sum()
all_stats[all_stats['CF'].isnull()]
all_stats['CF'].fillna(value =0, inplace =True)

all_stats['CA'].isnull()
all_stats[all_stats['CA'].isnull()]
all_stats['CA'].fillna(value =0, inplace =True)

all_stats['CF%'].isnull().sum()
all_stats[all_stats['CF%'].isnull()]
all_stats['CF%'].fillna(value =0, inplace =True)


all_stats['CF% rel'].isnull().sum()
all_stats[all_stats['CF% rel'].isnull()]
all_stats['CF% rel'].fillna(value =0, inplace =True)

all_stats['C/60'].isnull().sum()
all_stats['C/60'].fillna(value =0, inplace =True)

all_stats['Crel/60'].isnull().sum()
all_stats[all_stats['Crel/60'].isnull()]
all_stats['Crel/60'].fillna(value =0, inplace =True)

all_stats['FF'].isnull().sum()
all_stats[all_stats['FF'].isnull()]
all_stats['FF'].fillna(value =0, inplace =True)


#Also need to get the 2015 data and process:

NHL_players_2015=  pd.read_csv("/Users/MindKontrol/Python/GADataScience/DAT4/Forecasting All NBA Teams/CurrentYearStats")
NHL_players_2015.info()
NHL_players_2015.sh_.fillna(value = 0, inplace = True)

NHL_players_2015.g_.fillna(value = 0, inplace = True)

NHL_players_2015.a_.fillna(value = 0, inplace = True)
NHL_players_2015.pts_.fillna(value = 0, inplace = True)
NHL_players_2015['CF%'].fillna(value =0, inplace =True)
NHL_players_2015['C/60'].fillna(value =0, inplace =True)
NHL_players_2015['FTr'].fillna(value =0, inplace =True)

NHL_players_2015['FF'].fillna(value =0, inplace =True)

del NHL_players_2015['Unnamed: 0']
del NHL_players_2015['Pos']
del NHL_players_2015['Age']
del NHL_players_2015['Tm']
del NHL_players_2015['blnk']
del NHL_players_2015['blnk2']
del NHL_players_2015['Rk_x']
del NHL_players_2015['Rk_y']
del NHL_players_2015['G']

NHL_players_2015.pos.value_counts()


NHL_players_2015.to_csv('/Users/ToddJohnsen/Python/Data-science-project/Forecasting NHL All Star Teams/NHL_players_2015.csv')

#Add ALL-NBA Team Data

NHL = pd.read_csv("/Users/ToddJohnsen/Python/Data-science-project/Forecasting NHL All Star Teams/All_Team_Data.csv")
NHL_players = pd.merge(all_stats, NHL, how = "left", on = ['player', 'season_end'])

#Where value in team varible is missing fill with none.
NHL_players.team.fillna(value = 'None', inplace = True)

#Void missing age values 
NHL_players  = NHL_players[NHL_players.age.notnull()]

#Selection teams consists of one left wing, one center, one right wing, two defensemen, and one goaltender
#So need to aggergate positions into LW, C, RW, D, G
NHL_players[NHL_players.pos.isnull()]
NHL_players.pos.fillna(value = 'F', inplace = True) 

#Exploratory Analysis
#Find most important features, parellel coordinates; coorealtion matrix

NHL_players.to_csv('NHL_players.csv')


corrMat =NHL_players.corr()
NHL_players.columns

from pandas.tools.plotting import parallel_coordinates
features = [["gp","g","a","pts","+/-","pim","ev","pp","sh","gw","ev","pp","sh","s","s_","toi","atoi","blk","hit","FOwin","FOloss","FO_"]]
#features = [["gp","g","a","pts","+/-","pim","ev","pp","sh","gw","ev","pp","sh","s","s_","toi","atoi","blk","hit","FOwin","FOloss","FO_"]]
NHL_df = pd.DataFrame(NHL_players, columns = features)
NHL_df['team']= NHL_players.team
parallel_coordinates(data=NHL_df,class_column = 'team')


                     


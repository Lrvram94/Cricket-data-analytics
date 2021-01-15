"""COSC 480 Cricket visualisation project

Done by: Venkatasubramanian Lalgudi Ramakrishnan
Date: 14/10/2020
Student ID: 82730861

This program visualises IPL Cricket statistics

"""

import pandas as pd
from tkinter import *
from tkinter.ttk import *
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


df = pd.read_csv("ipl_cleaned_data.csv")


def matches_played():
    """Displays data about number of matches played each season"""
    sns.countplot(x='season', data=df)
    plt.title("Number of Matches played every season")
    plt.xlabel("Season")
    plt.ylabel("Count of Matches(Played)")
    plt.show()


def team_wins():
    """Displays the data of count of matches won to determine the successfull team"""
    top_teams = df['winner'].value_counts()[:15]
    sns.barplot(x=top_teams, y=top_teams.index)
    plt.title("Top Teams")
    plt.xlabel("Team")
    plt.ylabel("Wins(Count)")
    plt.show()


def best_players():
    """Determines the Top 20 players by counting their man of the match awards"""
    top_players = df['player_of_match'].value_counts()[:20]
    sns.barplot(x=top_players, y=top_players.index)
    plt.title("Top Players")
    plt.xlabel("Man of the Match awards")
    plt.ylabel("Players")
    plt.show()

def overall_toss_impact():
    """Displays the details about the Impact of Toss in winning the match"""
    toss_comparison = (df['toss_winner'] == df['winner'])
    toss_comparison.groupby(toss_comparison).size()
    sns.countplot(x=toss_comparison)
    plt.title("Impact of toss in Match's result")
    plt.xlabel("Toss Impact")
    plt.ylabel("Wins(count)")
    plt.show()  

def toss_win_bat_first_impact():
    """Determines the team's performance when batting first after winning the Toss"""
    team_batting_first_won = df.loc[(df['toss_winner'] == df['winner']) & (df['toss_decision'] == 'bat')]
    toss_win_bat_first_won_count = team_batting_first_won['winner'].value_counts()
    toss_win_bat_first_won_count.plot(kind = 'bar', color = 'green')
    plt.title("Analysis of Winning team batting first after winning the Toss")
    plt.xlabel("Teams")
    plt.ylabel("Count of Matches(Won)")
    plt.show()


def toss_win_field_first_impact():
    """Determines the team's performance when fielding first after winning the Toss"""
    team_fielding_first_won = df.loc[(df['toss_winner'] == df['winner']) & (df['toss_decision'] == 'field')]
    team_fielding_first_won_count = team_fielding_first_won['winner'].value_counts()
    team_fielding_first_won_count.plot(kind = 'bar', color = 'blue')
    plt.title("Analysis of Winning team fielding first after winning the Toss")
    plt.xlabel("Teams")
    plt.ylabel("Count of Matches(Won)")
    plt.show()


def toss_impact():
    """Displays the details about the Impact of Toss in winning the match"""
    window = Tk()
    welcome_label = Label(window, text="Impact of Toss Decision in Match Result",  font=("Helvetica", 10))
    welcome_label.grid(row=1, column=1, padx=24, pady=5)
    overall_toss_impact_button = Button(window, text="Overall toss impact", command=overall_toss_impact)
    overall_toss_impact_button.grid(row=2, column=1, padx=24, pady=5, ipady=10, sticky=(E, W))
    toss_win_bat_first_impact_button =  Button(window, text="Batting first", command=toss_win_bat_first_impact)
    toss_win_bat_first_impact_button.grid(row=3, column=1, padx=24, pady=5, ipady=10, sticky=(E, W))
    toss_win_field_first_impact_button =  Button(window, text="Fielding first", command=toss_win_field_first_impact)
    toss_win_field_first_impact_button.grid(row=4, column=1, padx=24, pady=5, ipady=10, sticky=(E, W))
    exit_button = Button(window, text="Exit", command=window.destroy)
    exit_button.grid(row=5, column=1, padx=24, pady=5)
    window.geometry("300x300+10+10")
    window.title("COSC480")
    window.configure(background='light blue')    
    window.mainloop() 
    


def team_performance_by_runs():
    """Displays the details about the Team's performace in wins over years by runs"""
    df[df['win_by_runs']>0].groupby(['winner'])['win_by_runs'].apply(np.median).sort_values(ascending = False)
    sns.boxplot(y = 'winner', x = 'win_by_runs', data=df[df['win_by_runs']>0], orient = 'h')
    plt.xlabel("Win by runs")
    plt.ylabel("Teams")
    plt.title("Teams performance by Winning runs")
    plt.show()


def team_performance_by_wickets():
    """Displays the details about the Team's performace in wins over years by wickets"""
    df[df['win_by_wickets']>0].groupby(['winner'])['win_by_wickets'].apply(np.median).sort_values(ascending = False)
    sns.boxplot(y = 'winner', x = 'win_by_wickets', data=df[df['win_by_wickets']>0], orient = 'h')
    plt.xlabel("Win by wickets")
    plt.ylabel("Teams")
    plt.title("Teams performance by wickets")
    plt.show()
    


def head_to_head_csk_vs_mi():
    """Head to Head match win details between chennai and mumbai"""
    team_head_to_head = df[((df['team1']=='Chennai Super Kings')|(df['team2']=='Chennai Super Kings'))&((df['team1']=='Mumbai Indians')|(df['team2']=='Mumbai Indians'))]
    sns.countplot(x='season', hue='winner',data=team_head_to_head,palette='Set2')
    plt.show()


def head_to_head_rcb_vs_csk():
    """Head to Head match win details between chennai and mumbai"""
    team_head_to_head = df[((df['team1']=='Chennai Super Kings')|(df['team2']=='Chennai Super Kings'))&((df['team1']=='Royal Challengers Bangalore')|(df['team2']=='Royal Challengers Bangalore'))]
    sns.countplot(x='season', hue='winner',data=team_head_to_head,palette='Set1')
    plt.show()


def head_to_head_csk_vs_kkr():
    """Head to Head match win details between chennai and Kolkata"""
    team_head_to_head = df[((df['team1']=='Chennai Super Kings')|(df['team2']=='Chennai Super Kings'))&((df['team1']=='Kolkata Knight Riders')|(df['team2']=='Kolkata Knight Riders'))]
    sns.countplot(x='season', hue='winner',data=team_head_to_head,palette='Set3')
    plt.show()


def head_to_head_mi_vs_rcb():
    """Head to Head match win details between Mumbai and Banglore"""
    team_head_to_head = df[((df['team1']=='Mumbai Indians')|(df['team2']=='Mumbai Indians'))&((df['team1']=='Royal Challengers Bangalore')|(df['team2']=='Royal Challengers Bangalore'))]
    sns.countplot(x='season', hue='winner',data=team_head_to_head,palette='Set1')
    plt.show()


def head_to_head_mi_vs_kkr():
    """Head to Head match win details between Mumbai and Kolkata"""
    team_head_to_head = df[((df['team1']=='Mumbai Indians')|(df['team2']=='Mumbai Indians'))&((df['team1']=='Kolkata Knight Riders')|(df['team2']=='Kolkata Knight Riders'))]
    sns.countplot(x='season', hue='winner',data=team_head_to_head,palette='Set2')
    plt.show()


def head_to_head_rcb_vs_kkr():
    """Head to Head match win details between Banglore and Kolkata"""
    team_head_to_head = df[((df['team1']=='Royal Challengers Bangalore')|(df['team2']=='Royal Challengers Bangalore'))&((df['team1']=='Kolkata Knight Riders')|(df['team2']=='Kolkata Knight Riders'))]
    sns.countplot(x='season', hue='winner',data=team_head_to_head,palette='Set3')
    plt.show()


def head_to_head_top_teams():
    """Head to Head match statistics details about top 4 teams displayed in seperate windows"""
    window = Tk()
    welcome_label = Label(window, text="Top team's head to head Analysis",  font=("Helvetica", 10))
    welcome_label.grid(row=1, column=1, padx=24, pady=5)
    head_to_head_csk_vs_mi_button = Button(window, text="Chennai vs Mumbai", command=head_to_head_csk_vs_mi)
    head_to_head_csk_vs_mi_button.grid(row=2, column=1, padx=24, pady=5, ipady=10, sticky=(E, W))
    head_to_head_rcb_vs_csk_button = Button(window, text="Chennai vs Banglore", command=head_to_head_rcb_vs_csk)
    head_to_head_rcb_vs_csk_button.grid(row=3, column=1, padx=24, pady=5, ipady=10, sticky=(E, W))
    head_to_head_csk_vs_kkr_button = Button(window, text="Chennai vs Kolkata", command=head_to_head_csk_vs_kkr)
    head_to_head_csk_vs_kkr_button.grid(row=4, column=1, padx=24, pady=5, ipady=10, sticky=(E, W))
    head_to_head_mi_vs_rcb_button = Button(window, text="Mumbai vs Banglore", command=head_to_head_mi_vs_rcb)
    head_to_head_mi_vs_rcb_button.grid(row=5, column=1, padx=24, pady=5, ipady=10, sticky=(E, W))
    head_to_head_mi_vs_kkr_button = Button(window, text= 'Mumbai vs Kolkata', command=head_to_head_mi_vs_kkr)
    head_to_head_mi_vs_kkr_button.grid(row=6, column=1, padx=24, pady=5, ipady=10, sticky=(E, W))
    head_to_head_rcb_vs_kkr_button = Button(window, text="Banglore vs Kolkata", command=head_to_head_rcb_vs_kkr)
    head_to_head_rcb_vs_kkr_button.grid(row=7, column=1, padx=24, pady=5, ipady=10, sticky=(E, W))
    exit_button = Button(window, text="Exit", command=window.destroy)
    exit_button.grid(row=8, column=1, padx=24, pady=5)
    window.geometry("400x450+10+10")
    window.title("COSC480")
    window.configure(background='light blue')    
    window.mainloop()   



def teams_performance():
    """Displays the details about team's performance in seperate window"""
    window = Tk()
    welcome_label = Label(window, text="Team's performance Analysis",  font=("Helvetica", 10))
    welcome_label.grid(row=1, column=1, padx=24, pady=5)
    performance_by_runs_button =  Button(window, text="Performance by Runs", command=team_performance_by_runs)
    performance_by_runs_button.grid(row=2, column=1, padx=24, pady=5, ipady=10, sticky=(E, W))
    performance_by_wickets_button =  Button(window, text="Performance by Wickets", command=team_performance_by_wickets)
    performance_by_wickets_button.grid(row=3, column=1, padx=24, pady=5, ipady=10, sticky=(E, W))
    head_to_head_top_teams_button = Button(window, text="Head to Head", command=head_to_head_top_teams)
    head_to_head_top_teams_button.grid(row=4, column=1, padx=24, pady=5, ipady=10, sticky=(E, W))
    exit_button = Button(window, text="Exit", command=window.destroy)
    exit_button.grid(row=5, column=1, padx=24, pady=5)
    window.geometry("350x350+10+10")
    window.title("COSC480")
    window.configure(background='light blue')    
    window.mainloop()  


def ipl_statistics():
    """Displays the Statistics of the Indian Premier League tournament in a seperate window"""
    window = Tk()
    welcome_label = Label(window, text="Indian Premier League Statitics",  font=("Helvetica", 10))
    welcome_label.grid(row=1, column=1, padx=24, pady=5)
    matches_played_button = Button(window, text="Matches Played", command=matches_played)
    matches_played_button.grid(row=2, column=1, padx=24, pady=5, ipady=10, sticky=(E, W))
    team_wins_button = Button(window, text="Team's Win count", command=team_wins)
    team_wins_button.grid(row=3, column=1, padx=24, pady=5, ipady=10, sticky=(E, W))
    best_players_button = Button(window, text="Best Players", command=best_players)
    best_players_button.grid(row=4, column=1, padx=24, pady=5, ipady=10, sticky=(E, W))
    exit_button = Button(window, text="Exit", command=window.destroy)
    exit_button.grid(row=5, column=1, padx=24, pady=5)
    window.geometry("250x250+10+10")
    window.title("COSC480")
    window.configure(background='light blue')    
    window.mainloop()   


def main():
    """The Main function"""
    window = Tk()
    label_1 = Label(window, text="COSC 480 Project",  font=("Helvetica", 12))
    label_1.grid(row=0, column=1,padx=24, pady=5)
    label_2 = Label(window, text="IPL Data Visualisation GUI Program",  font=("Helvetica", 10))
    label_2.grid(row=1, column=1,padx=24, pady=5)
    ipl_statistics_button = Button(window, text="IPL Statistics", command=ipl_statistics)
    ipl_statistics_button.grid(row=2, column=1, padx=24, pady=5, ipady=10, sticky=(E, W))
    toss_impact_button = Button(window, text="Toss Impact", command=toss_impact)
    toss_impact_button.grid(row=3, column=1, padx=24, pady=5, ipady=10, sticky=(E, W))
    teams_performance_button = Button(window, text="Team's Performance Analysis", command=teams_performance)
    teams_performance_button.grid(row=4, column=1, padx=24, pady=5, ipady=10, sticky=(E, W))
    exit_button = Button(window, text="Exit", command=window.destroy)
    exit_button.grid(row=7, column=1, padx=24, pady=5)
    window.geometry("300x300+10+10")
    window.title("COSC480 GUI Project")
    window.configure(background='light blue')    
    window.mainloop()
    
main()


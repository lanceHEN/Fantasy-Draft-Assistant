import tabula as tb
import pandas as pd

df = pd.read_csv('https://footballabsurdity.com/wp-content/plugins/BeerSheetRequests/sheets/12,1,2,2,1,1,0,0,0,6,6,6,0.025,0.067,0.067,0,0,-2,0,0,0,0,0.csv')

#print(df)

ranked = df.sort_values(by = ['Average'], ascending=False)

pd.set_option('display.max_rows', 25)

print(ranked)

teams = input('How many teams are in your league? ')
rounds = input('How many rounds are in your draft? ')

totalpicks = int(teams) * int(rounds)

for n in range(0, totalpicks):
    playertaken = input('Who was just drafted? ')

    try:
        ranked.drop(ranked.loc[ranked['Name']==playertaken].index, inplace=True)
        print(ranked)

    except: ranked.drop


    #print(df)
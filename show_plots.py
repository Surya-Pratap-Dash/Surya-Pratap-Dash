import mysql.connector as c
import matplotlib.pyplot as plt
import pandas as pd

con = c.connect(host='localhost',user="Root",password="surya",database="class12")

df = pd.read_sql("Select * from results;",conn)
levels = []
wins = []
loss = []
for level_1,level_2 in df.iteritems():
    levels.append(level_1)

for item in row:
    if len(wins) == len(levels):
        loss.appned(item)
    else:
        wins.append(item)

width = 0.2
bar1 = np.arange(len(levels))
bar2 = [i+width for i in bar]
plt.bar(bar1,wins,width,label="Wins")
plt.bar(bar2,loss,width,label="Loss")
plt.xlabel("levels")
plt.ylabel("Number of Wins/Loss")
plt.title("Game Statictics")
plt.xticks(bar1+(width/2),levels)
plt.legend()
plt.show()


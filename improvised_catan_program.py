
import math
import csv

#基本的なデータ構造
# class Player():
#     def __init__(self, name):
#         self.name = name
#         self.entry = 0
#         self.point = 0
#         self.wins = 0
#         self.win_rate = 0
#         self.score_sum = 0
#         self.score_average = 0
    
#     def __str__(self):
#         return "名前: " + self.name, "出場回数: " + self.entry, "ポイント獲得数: " + self.point, "勝利数: " + self.wins, "勝率: " + self.win_rate, "得点の合計: " + self.score_sum, "平均得点: " + self.score_average

class Game():
    def __init__(self, ls):
        self.players = self.pl_names(ls)
        self.result = self.organize(ls)

    #プレイヤー名のリストの生成
    def pl_names(self, x):
        pl_list = []
        for pl in x:
            a_pl = pl.split(", ")
            pl_list.append(a_pl[0])
        return pl_list
    
    #入力をよりきれいなリストにする
    def organize(self, y):
        big_list = []
        for i in y:
            a = i.split(", ")
            for b in a:
                big_list.append(b)
        return big_list

if __name__ == "__main__":
    all_games = []
    with open("catan_game_data.csv") as f:
        data = f.read()
        games = []
        a_game = data.split("\n\n")
        for i in a_game:
            a = i.split("\n")
            games.append(a)
        for game in games:
            this_game = Game(game)
            all_games.append(this_game)
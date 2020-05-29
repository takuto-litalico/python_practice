
import math
import csv

#基本的なデータ構造
class Player():
    def __init__(self, name, ls):
        self.name = name
        self.entry = self.cal_entry(ls)
        self.points = self.cal_point(ls)
        self.wins = self.cal_win(ls)
        self.win_rate = self.cal_win_rate()
        self.score_sum = self.cal_score_sum(ls)
        self.score_average = self.cal_score_average()

    def cal_entry(self, ls):
        entry_num = len(ls)
        return entry_num

    def cal_point(self, ls):
        points_gained = 0
        for game in ls:
            game_ls = game.result
            print(game_ls)
            ind = int(game_ls.index(self.name))
            score = int(game_ls[ind+1])
            if ind == 0:
                points_gained += 2
            if len(game_ls) > 8:
                if score == game_ls[4]:
                    points_gained += 1
            if score < 7:
                if score > 4:
                    points_gained -= 1
                if score < 5:
                    points_gained -= 2
        return points_gained
    
    def cal_win(self, ls):
        wins = 0
        for game in ls:
            game_ls = game.result
            ind = game_ls.index(self.name)
            if ind == 0:
                wins += 1
        return wins

    def cal_win_rate(self):
        win_rate = self.wins / self.entry * 100
        a = int(win_rate * 100)
        b = a / 100
        return b

    def cal_score_sum(self, ls):
        score_sum = 0
        for game in ls:
            game_ls = game.result
            ind = int(game_ls.index(self.name)) + 1
            score = int(game_ls[ind])
            score_sum += score
        return score_sum
    
    def cal_score_average(self):
        score_average = self.score_sum / self.entry
        a = int(score_average * 100)
        b = a / 100
        return b

    def __str__(self):
        a_str = "名前: " + self.name, "出場回数: " + str(self.entry), "ポイント獲得数: " + str(self.points), "勝利数: " + str(self.wins), "勝率: " + str(self.win_rate), "得点の合計: " + str(self.score_sum), "平均得点: " + str(self.score_average)
        this = str(a_str)
        return this

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
    
    #各プレイヤーの名前を取得
    names_set = set()
    for game in all_games:
        for name in game.players:
            names_set.add(name)
    players = list(names_set)
    print(names_set)

    #情報処理
    player_datas = []
    for player in players:
        games_played = []
        for game in all_games:
            if player in game.players:
                games_played.append(game)
        player_datas.append(Player(player, games_played))
    
    for player in player_datas:
        print(player)


#モジュールのインポート
import math

#各プレイヤーのポイント獲得数、勝利数、勝率、得点の合計、平均得点、出場回数を保存するデータベース（DictのList）
big_data = [{'名前': 'takumi', '出場回数': 55, 'ポイント獲得数': -14, '勝利数': 5, '勝率': 9.09, '得点の合計': 360, '平均得点': 6.54}, {'名前': 'yoshiwaki', '出場回数': 41, 'ポイント獲得数': 22, '勝利数': 16, '勝率': 39.02, '得点の合計': 319, '平均得点': 7.78}, {'名前': 'shin', '出場回数': 19, 'ポイント獲得数': 7, '勝利数': 5, '勝率': 26.31, '得点の合計': 149, '平均得点': 7.84}, {'名前': 'takuto', '出場回数': 70, 'ポイント獲得数': 36, '勝利数': 15, '勝率': 21.42, '得点の合計': 553, '平均得点': 7.9}, {'名前': 'tomoe', '出場回数': 3, 'ポイント獲得数': 3, '勝利数': 1, '勝率': 33.33, '得点の合計': 24, '平均得点': 8.0}, {'名前': 'yuki', '出場回数': 5, 'ポイント獲得数': -2, '勝利数': 0, '勝率': 0.0, '得点の合計': 30, '平均得点': 6.0}, {'名前': 'izaya', '出場回数': 47, 'ポイント獲得数': 20, '勝利数': 15, '勝率': 31.91, '得点の合計': 365, '平均得点': 7.76}, {'名前': 'hisaki', '出場回数': 50, 'ポイント獲得数': -4, '勝利数': 5, '勝率': 10.0, '得点の合計': 345, '平均得点': 6.9}, {'名前': 'ponchi', '出場回数': 6, 'ポイント獲得数': 3, '勝利数': 1, '勝率': 16.66, '得点の合計': 44, '平均得点': 7.33}, {'名前': 'ayane', '出場回数': 6, 'ポイント獲得数': -3, '勝利数': 0, '勝率': 0.0, '得点の合計': 31, '平均得点': 5.16}, {'名前': 'tomoki', '出場回数': 4, 'ポイント獲得数': -4, '勝利数': 0, '勝率': 0.0, '得点の合計': 22, '平均得点': 5.5}, {'名前': 'kazuki', '出場回数': 5, 'ポイント獲得数': -7, '勝利数': 0, '勝率': 0.0, '得点の合計': 21, '平均得点': 4.2}, {'名前': 'canon', '出場回数': 38, 'ポイント獲得数': 9, '勝利数': 7, '勝率': 18.42, '得点の合計': 286, '平均得点': 7.52}, {'名前': 'yutaka', '出場回数': 3, 'ポイント獲得数': -2, '勝利数': 1, '勝率': 33.33, '得点の合計': 18, '平均得点': 6.0}, {'名前': 'makito', '出場回数': 7, 'ポイント獲得数': 4, '勝利数': 2, '勝率': 28.57, '得点の合計': 56, '平均得点': 8.0}, {'名前': 'ayumu', '出場回数': 6, 'ポイント獲得数': 1, '勝利数': 1, '勝率': 16.66, '得点の合計': 46, '平均得点': 7.66}, {'名前': 'tomo', '出場回数': 2, 'ポイント獲得数': -3, '勝利数': 0, '勝率': 0.0, '得点の合計': 9, '平均得点': 4.5}, {'名前': 'yoshihiro', '出場回数': 5, 'ポイント獲得数': 0, '勝利数': 0, '勝率': 0.0, '得点の合計': 33, '平均得点': 6.6}, {'名前': 'kento', '出場回数': 14, 'ポイント獲得数': 0, '勝利数': 3, '勝率': 21.42, '得点の合計': 98, '平均得点': 7.0}, {'名前': 'koh', '出場回数': 1, 'ポイント獲得数': 1, '勝利数': 0, '勝率': 0, '得点の合計': 9, '平均得点': 9}, {'名前': 'nao', '出場回数': 1, 'ポイント獲得数': -1, '勝利数': 0, '勝率': 0, '得点の合計': 5, '平均得点': 5}, {'名前': 'daniel', '出場回数': 13, 'ポイント獲得数': -2, '勝利数': 2, '勝率': 15.38, '得点の合計': 84, '平均得点': 6.46}, {'名前': 'vincent', '出場回数': 3, 'ポイント獲得数': -3, '勝利数': 0, '勝率': 0.0, '得点の合計': 17, '平均得点': 5.66}, {'名前': 'joshua', '出場回数': 3, 'ポイント獲得数': -1, '勝利数': 0, '勝率': 0.0, '得点の合計': 20, '平均得点': 6.66}, {'名前': 'aki', '出場回数': 1, 'ポイント獲得数': -1, '勝利数': 0, '勝率': 0, '得点の合計': 6, '平均得点': 6}, {'名前': 'lihito', '出場回数': 1, 'ポイント獲得数': -1, '勝利数': 0, '勝率': 0, '得点の合計': 5, '平均得点': 5}, {'名前': 'june', '出場回数': 1, 'ポイント獲得数': -2, '勝利数': 0, '勝率': 0, '得点の合計': 2, '平均得点': 2}]
#各ゲームデータの情報を保存するDict
#次第何回目かを入力
game_num = 80
game_data_dict = {'第1回目': ['２０１９年３月５日', {'takumi': '10'}, {'yoshiwaki': '9'}, {'shin': '8'}, {'takuto': '8'}, {'tomoe': '6'}, {'yuki': '6'}], '第2回目': ['２０１９年３月１７日', {'izaya': '10'}, {'hisaki': '8'}, {'takuto': '6'}, {'takumi': '4'}], '第3回目': ['２０１９年３月１７日', {'izaya': '10'}, {'tomoe': '8'}, {'takumi': '8'}, {'hisaki': '8'}, {'takuto': '7'}, {'yoshiwaki': '6'}], '第4回目': ['２０１９年３月２４日', {'takuto': '10'}, {'hisaki': '9'}, {'izaya': '8'}, {'takumi': '6'}, {'ponchi': '5'}], '第5回目': ['２０１９年３月２４日', {'hisaki': '10'}, {'ponchi': '8'}, {'takumi': '7'}, {'izaya': '6'}, {'takuto': '6'}], '第6回目': ['２０１９年３月２４日', {'takuto': '10'}, {'izaya': '9'}, {'hisaki': '6'}, {'takumi': '5'}], '第7回目': ['２０１９年３月２４日', {'izaya': '10'}, {'shin': '9'}, {'takuto': '9'}, {'yuki': '6'}, {'ayane': '3'}], '第8回目': ['２０１９年３月３１日', {'takuto': '10'}, {'shin': '9'}, {'izaya': '8'}, {'yoshiwaki': '6'}, {'tomoki': '3'}, {'kazuki': '3'}], '第9回目': ['２０１９年３月３１日', {'izaya': '10'}, {'yoshiwaki': '9'}, {'takuto': '9'}, {'shin': '8'}, {'canon': '7'}], '第10回目': ['２０１９年４月７日', {'takuto': '10'}, {'ponchi': '7'}, {'takumi': '7'}, {'izaya': '6'}, {'hisaki': '4'}, {'tomoki': '4'}], '第11回目': ['２０１９年４月７日', {'yoshiwaki': '10'}, {'izaya': '9'}, {'takumi': '9'}, {'takuto': '9'}, {'ponchi': '8'}, {'hisaki': '6'}], '第12回目': ['２０１９年４月１３日', {'yoshiwaki': '10'}, {'hisaki': '7'}, {'izaya': '6'}, {'takuto': '6'}, {'takumi': '4'}], '第13回目': ['２０１９年４月１４日', {'shin': '10'}, {'takumi': '9'}, {'hisaki': '7'}, {'izaya': '6'}], '第14回目': ['２０１９年４月２１日', {'izaya': '10'}, {'yoshiwaki': '7'}, {'shin': '6'}, {'takuto': '6'}], '第15回目': ['２０１９年４月３０日', {'yutaka': '10'}, {'hisaki': '7'}, {'yoshiwaki': '6'}, {'takuto': '6'}], '第16回目': ['２０１９年５月１日', {'shin': '10'}, {'yoshiwaki': '8'}, {'izaya': '7'}, {'takuto': '6'}], '第17回目': ['２０１９年５月１日', {'makito': '10'}, {'ayumu': '8'}, {'tomo': '6'}, {'shin': '5'}], '第18回目': ['２０１９年５月１日', {'izaya': '10'}, {'takuto': '8'}, {'hisaki': '7'}, {'yoshihiro': '5'}, {'yutaka': '4'}, {'takumi': '2'}], '第19回目': ['２０１９年５月１日', {'izaya': '10'}, {'yoshiwaki': '8'}, {'canon': '8'}, {'takumi': '6'}, {'yutaka': '4'}, {'hisaki': '4'}], '第20回目': ['２０１９年５月２日', {'kento': '10'}, {'koh': '9'}, {'makito': '9'}, {'shin': '6'}, {'ayumu': '6'}, {'tomo': '3'}], '第21回目': ['２０１９年５月２日', {'canon': '10'}, {'kento': '7'}, {'yoshiwaki': '7'}, {'takuto': '6'}, {'nao': '5'}, {'takumi': '5'}], '第22回目': ['２０１９年５月５日', {'canon': '10'}, {'takuto': '9'}, {'yoshiwaki': '8'}, {'kento': '7'}], '第23回目': ['２０１９年５月１１日', {'kento': '11'}, {'yoshihiro': '9'}, {'takuto': '9'}, {'hisaki': '9'}, {'canon': '8'}, {'takumi': '7'}], '第24回目': ['２０１９年５月１１日', {'takuto': '10'}, {'yoshihiro': '8'}, {'ayane': '8'}, {'takumi': '7'}, {'hisaki': '5'}], '第25回目': ['２０１９年５月１２日', {'daniel': '10'}, {'canon': '9'}, {'takumi': '9'}, {'hisaki': '7'}, {'izaya': '7'}, {'yuki': '5'}], '第26回目': ['２０１９年５月１２日', {'izaya': '10'}, {'takuto': '7'}, {'yoshiwaki': '6'}, {'canon': '4'}, {'daniel': '3'}], '第27回目': ['２０１９年５月１９日', {'ponchi': '11'}, {'izaya': '8'}, {'takuto': '7'}, {'hisaki': '7'}, {'takumi': '5'}], '第28回目': ['２０１９年５月１９日', {'takuto': '11'}, {'canon': '6'}, {'yoshiwaki': '5'}, {'hisaki': '5'}, {'takumi': '4'}, {'izaya': '3'}], '第29回目': ['２０１９年５月１９日', {'canon': '10'}, {'yoshiwaki': '8'}, {'takuto': '8'}, {'hisaki': '4'}, {'ayane': '3'}], '第30回目': ['２０１９年５月１９日', {'takuto': '10'}, {'shin': '8'}, {'canon': '7'}, {'yoshiwaki': '6'}], '第31回目': ['２０１９年５月２６日', {'takuto': '10'}, {'takumi': '10'}, {'canon': '9'}, {'tomoki': '8'}, {'hisaki': '7'}, {'kazuki': '5'}], '第32回目': ['２０１９年５月２６日', {'yoshiwaki': '10'}, {'takuto': '8'}, {'hisaki': '8'}, {'takumi': '7'}, {'ayane': '6'}], '第33回目': ['２０１９年６月１日', {'izaya': '10'}, {'takuto': '7'}, {'makito': '5'}, {'canon': '5'}, {'yuki': '4'}], '第34回目': ['２０１９年６月２日', {'canon': '10'}, {'izaya': '8'}, {'takuto': '8'}, {'takumi': '7'}, {'hisaki': '6'}], '第35回目': ['２０１９年６月２日', {'canon': '11'}, {'hisaki': '6'}, {'izaya': '5'}, {'takumi': '5'}, {'takuto': '4'}], '第36回目': ['２０１９年６月９日', {'izaya': '10'}, {'takuto': '9'}, {'takumi': '8'}, {'hisaki': '7'}, {'tomoki': '7'}, {'kazuki': '7'}], '第37回目': ['２０１９年６月９日', {'takuto': '10'}, {'izaya': '7'}, {'takumi': '4'}, {'hisaki': '4'}], '第38回目': ['２０１９年６月１６日', {'yoshiwaki': '10'}, {'hisaki': '10'}, {'takuto': '9'}, {'izaya': '8'}, {'canon': '8'}, {'takumi': '7'}], '第39回目': ['２０１９年６月１６日', {'yoshiwaki': '10'}, {'takuto': '7'}, {'hisaki': '7'}, {'takumi': '6'}], '第40回目': ['２０１９年６月２３日', {'takuto': '10'}, {'hisaki': '8'}, {'izaya': '7'}, {'yoshiwaki': '7'}, {'takumi': '7'}, {'ponchi': '5'}], '第41回目': ['２０１９年６月２３日', {'yoshiwaki': '11'}, {'shin': '8'}, {'takuto': '8'}, {'izaya': '7'}], '第42回目': ['２０１９年６月３０日', {'takumi': '10'}, {'takuto': '8'}, {'izaya': '7'}, {'hisaki': '7'}, {'vincent': '7'}, {'kazuki': '3'}], '第43回目': ['２０１９年６月３０日', {'canon': '10'}, {'takuto': '9'}, {'izaya': '5'}, {'takumi': '5'}, {'hisaki': '4'}], '第44回目': ['２０１９年７月７日', {'yoshiwaki': '10'}, {'takumi': '9'}, {'takuto': '9'}, {'joshua': '9'}, {'hisaki': '6'}, {'vincent': '6'}], '第45回目': ['２０１９年７月１４日', {'hisaki': '10'}, {'canon': '9'}, {'takuto': '9'}, {'joshua': '8'}, {'takumi': '5'}, {'vincent': '4'}], '第46回目': ['２０１９年７月１４日', {'shin': '11'}, {'canon': '7'}, {'kento': '5'}, {'daniel': '5'}, {'yoshiwaki': '5'}, {'takuto': '4'}], '第47回目': ['２０１９年７月１４日', {'canon': '10'}, {'takuto': '8'}, {'shin': '7'}, {'yoshiwaki': '5'}], '第48回目': ['２０１９年７月２１日', {'shin': '10'}, {'yoshihiro': '8'}, {'daniel': '7'}, {'takumi': '5'}, {'takuto': '5'}], '第49回目': ['２０１９年８月２５日', {'daniel': '10'}, {'takuto': '8'}, {'hisaki': '7'}, {'izaya': '6'}, {'takumi': '6'}, {'yoshiwaki': '3'}], '第50回目': ['２０１９年８月２５日', {'yoshiwaki': '10'}, {'izaya': '8'}, {'takuto': '7'}, {'shin': '4'}], '第51回目': ['２０１９年９月１日', {'yoshiwaki': '10'}, {'ayumu': '9'}, {'takuto': '8'}, {'shin': '7'}, {'izaya': '7'}, {'daniel': '7'}], '第52回目': ['２０１９年９月８日', {'izaya': '10'}, {'takuto': '9'}, {'yoshiwaki': '7'}, {'canon': '7'}, {'aki': '6'}], '第53回目': ['２０１９年９月１５日', {'takumi': '10'}, {'takuto': '8'}, {'daniel': '7'}, {'hisaki': '6'}], '第54回目': ['２０１９年９月２９日', {'takuto': '10'}, {'yoshiwaki': '6'}, {'takumi': '4'}, {'izaya': '3'}], '第55回目': ['２０１９年９月２９日', {'yoshiwaki': '10'}, {'izaya': '9'}, {'takuto': '9'}, {'takumi': '6'}], '第56回目': ['２０１９年１０月６日', {'yoshiwaki': '10'}, {'izaya': '8'}, {'canon': '7'}, {'takuto': '5'}, {'takumi': '4'}, {'kazuki': '3'}], '第57回目': ['２０１９年１０月６日', {'izaya': '10'}, {'takuto': '6'}, {'yoshiwaki': '5'}, {'takumi': '5'}, {'joshua': '3'}], '第58回目': ['２０１９年１０月７日', {'yoshiwaki': '10'}, {'takuto': '6'}, {'izaya': '5'}, {'makito': '5'}, {'kento': '4'}], '第59回目': ['２０１９年１０月７日', {'makito': '10'}, {'izaya': '8'}, {'kento': '7'}, {'yoshiwaki': '7'}, {'takuto': '6'}], '第60回目': ['２０１９年１０月１４日', {'kento': '10'}, {'canon': '8'}, {'hisaki': '6'}, {'takuto': '5'}, {'takumi': '4'}], '第61回目': ['２０１９年１０月１４日', {'hisaki': '10'}, {'shin': '7'}, {'kento': '5'}, {'takuto': '5'}, {'canon': '4'}, {'takumi': '4'}], '第62回目': ['２０１９年１０月１４日', {'ayumu': '10'}, {'hisaki': '9'}, {'kento': '8'}, {'takuto': '8'}, {'takumi': '5'}], '第63回目': ['２０１９年１０月１９日', {'izaya': '10'}, {'makito': '8'}, {'canon': '8'}, {'takuto': '8'}], '第64回目': ['２０１９年１０月２０日', {'hisaki': '10'}, {'canon': '8'}, {'takumi': '7'}, {'izaya': '6'}, {'daniel': '5'}, {'yoshiwaki': '3'}], '第65回目': ['２０１９年１０月２０日', {'izaya': '11'}, {'takuto': '8'}, {'yoshiwaki': '5'}, {'hisaki': '5'}, {'daniel': '3'}, {'yoshihiro': '3'}], '第66回目': ['２０１９年１１月９日', {'takuto': '10'}, {'makito': '9'}, {'canon': '7'}, {'daniel': '5'}, {'izaya': '5'}], '第67回目': ['２０１９年１１月１７日', {'takuto': '10'}, {'daniel': '8'}, {'izaya': '6'}, {'canon': '6'}, {'takumi': '6'}], '第68回目': ['２０１９年１１月１７日', {'hisaki': '12'}, {'canon': '9'}, {'yuki': '9'}, {'takumi': '9'}, {'daniel': '6'}, {'ayane': '3'}], '第69回目': ['２０１９年１１月２４日', {'yoshiwaki': '10'}, {'takumi': '12'}, {'hisaki': '6'}, {'canon': '6'}, {'lihito': '5'}, {'june': '2'}], '第70回目': ['２０１９年１２月１日', {'yoshiwaki': '10'}, {'takuto': '9'}, {'canon': '8'}, {'hisaki': '7'}, {'takumi': '6'}], '第71回目': ['２０１９年１２月１日', {'yoshiwaki': '10'}, {'takumi': '8'}, {'hisaki': '8'}, {'ayane': '8'}, {'takuto': '7'}, {'canon': '5'}], '第72回目': ['２０１９年１２月１５日', {'shin': '10'}, {'daniel': '8'}, {'takumi': '6'}, {'takuto': '6'}, {'hisaki': '5'}], '第73回目': ['２０１９年１２月３０日', {'takumi': '10'}, {'hisaki': '9'}, {'kento': '8'}, {'canon': '8'}, {'takuto': '8'}], '第74回目': ['２０１９年１２月３０日', {'takuto': '10'}, {'kento': '8'}, {'canon': '5'}, {'takumi': '5'}, {'hisaki': '4'}], '第75回目': ['２０１９年１２月３０日', {'takumi': '10'}, {'takuto': '6'}, {'hisaki': '6'}, {'canon': '5'}, {'kento': '4'}], '第76回目': ['２０１９年１２月３１日', {'takuto': '10'}, {'takumi': '9'}, {'canon': '8'}, {'hisaki': '7'}, {'shin': '6'}, {'ayumu': '6'}], '第77回目': ['２０１９年１２月３１日', {'tomoe': '10'}, {'takuto': '9'}, {'canon': '8'}, {'ayumu': '7'}, {'hisaki': '6'}, {'takumi': '5'}], '第78回目': ['２０１９年１２月３１日', {'izaya': '10'}, {'hisaki': '6'}, {'yoshiwaki': '5'}, {'canon': '5'}, {'kento': '4'}, {'takumi': '3'}], '第79回目': ['２０１９年１２月３１日', {'yoshiwaki': '11'}, {'takumi': '7'}, {'takuto': '7'}, {'izaya': '6'}, {'canon': '6'}, {'hisaki': '6'}]}


#全体の大きなループ（KeyboardInterruptでbreakされる）
while True:
    try:
        #入力フォームは完了
        #各ゲームの日付、プレイヤー名＆成績の保存
        game_data_list = []
        
        #日時、プレイヤー名＆成績の入力フォーム
        date = input("プレイされた日付を入力（年、月、日）: ")
        game_data_list.append(date)
        
        #ゲームデータをgame_data_dictに保存
        key = "第" + str(game_num) + "回目"
        game_data_dict[key] = game_data_list
        game_num += 1      

        print("注：プレイヤー名はフルネームで漢字で入力。得点は数字のみで入力。各プレイヤーの情報入力は１位から順にすること。")
        print("入力が終ったら end をタイプイン。")
        while True:
            pl_name = input("プレイヤー名を入力: ")
            if pl_name == "end":
                break
            pl_score = input("得点を入力: ")
            game_data_list.append({pl_name: pl_score})
        
        #データの処理
        #使う道具
        #big_data内検索関数(正常に動作することを確認 2019/8/29)
        def search(name):
            found = False
            for player in big_data:
                if player["名前"] == name:
                    found = True
                    result = big_data.index(player)
            if found == True:
                return result
            else:
                return False
                    
        #少数第２位まで正確に求める関数
        def my_floor(f, n):
            return math.floor(f*(10**n)) / 10**n
            
        #新規プレイヤー追加関数（正常に動作することを確認 2019/9/13）
        def add_player(new_name):
        #直近のゲームのインデックス
            for pl in game_data_list:
                if type(pl) == dict:
                    if list(pl.keys())[0] == new_name:
                        gdl_ind = game_data_list.index(pl)
            #直近のゲームの得点
            p_recent_score = int(game_data_list[gdl_ind][new_name])
        
            #注: すでに決まっている数値（出場回数など）はdictにそのまま書き込む
                
            #出場回数は１回
        
            #ポイント獲得数の計算
            #１位の場合
            p_point_sum  = 0
            if gdl_ind == 1:
                p_point_sum += 2
            #拡張版２位の場合
            if len(game_data_list) > 5:
                if gdl_ind == 2 or p_recent_score == int(list(game_data_list[2].values())[0]):
                    p_point_sum += 1
            #マイナスポイントを食らう（第１回目から第７回目まではマイナス制度がない）
            #マイナス１ポイント
            if game_num > 8:
                if p_recent_score == 5 or p_recent_score == 6:
                    p_point_sum -= 1
            #マイナス２ポイントを食らう
            if game_num > 8:
                if p_recent_score <= 4:
                    p_point_sum -= 2
                        
            #勝利数の計算
            p_win_num = 0
            if gdl_ind == 1:
                p_win_num = 1
        
            #勝率の計算
            if p_win_num == 1:
                p_win_rate = 100
            else:
                p_win_rate = 0
        
            #得点の合計は直近のゲームの得点
                
            #平均得点は直近のゲームの得点
    
            p_new_dict = {"名前": new_name, "出場回数": 1, "ポイント獲得数": p_point_sum, "勝利数": p_win_num, "勝率": p_win_rate, "得点の合計": p_recent_score, "平均得点": p_recent_score}
        
            big_data.append(p_new_dict)
        
        #計算関数(正常に動作することを確認 2019/9/6)
        def update(name):
           #既存のデータを取得
           #直近のゲームにおけるインデックス（順位）の取得
            for pl in game_data_list:
                if type(pl) == dict:
                    if list(pl.keys())[0] == name:
                        gdl_ind = game_data_list.index(pl)
            #データベース内のプレイヤーの位置を取得
            bd_ind = search(name)

            ###################################################
            #扱う情報をすべて変数にする
            #プレイヤーの辞書
            p_dict = big_data[bd_ind]
            #出場回数
            p_entry_num = int(p_dict["出場回数"])
            #ポイント獲得数
            p_point_sum = int(p_dict["ポイント獲得数"])
            #勝利数
            p_win_num = int(p_dict["勝利数"])
            #勝率
            p_win_rate = float(p_dict["勝率"])
            #得点の合計
            p_score_sum = int(p_dict["得点の合計"])
            #平均得点
            p_score_average = float(p_dict["平均得点"])
            #直近のゲームにおける得点の取得
            p_recent_score = int(game_data_list[gdl_ind][name])
            ###################################################
     
            #計算過程##########################################
            #出場回数の計算(ok)
            p_entry_num += 1
        
            #ポイント獲得数の計算(ok)
            #１位の場合
            if gdl_ind == 1:
                p_point_sum += 2
            #拡張版２位の場合
            elif len(game_data_list) > 5: #日時の情報も考えて5にしてる
                    if gdl_ind == 2 or p_recent_score == int(list(game_data_list[2].values())[0]):
                        p_point_sum += 1
            #マイナスポイントを食らう (第１回目から第７回目まではマイナス制度がないことに注意)   
            #マイナス１ポイント
            if game_num > 8:
                if p_recent_score == 5 or p_recent_score == 6:
                    p_point_sum -= 1
            #マイナス２ポイントを食らう
            if game_num > 8:
                if p_recent_score <= 4:
                    p_point_sum -= 2
            
            #勝利数の計算(ok)
            #１位ならば勝ち
            if gdl_ind == 1:
                p_win_num += 1
        
            #勝率の計算（１００倍にしたものを少数第２位まで正確に求めたもの）(ok)
            p_win_rate = my_floor(p_win_num / p_entry_num * 100, 2)
            
            #得点の合計(ok)
            p_score_sum += p_recent_score
            
            #平均得点(ok)
            p_score_average = my_floor(p_score_sum / p_entry_num, 2)
        
            #プレイヤーに関する新しいdict
            new_p_dict = {"名前": name, "出場回数": p_entry_num, "ポイント獲得数": p_point_sum, "勝利数": p_win_num, "勝率": p_win_rate, "得点の合計": p_score_sum, "平均得点": p_score_average}
        
            #データベースにおいても更新
            big_data[bd_ind].update(new_p_dict)

        #各プレイヤーの情報を処理
        for pl in game_data_list:
            if type(pl) == dict:
                name = list(pl.keys())[0]
                if type(search(name)) == int:
                    update(name)
                else:
                    add_player(name)
        
    except KeyboardInterrupt:
        print(big_data)

        print(game_data_dict)
        break

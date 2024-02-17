
import streamlit as st
import random
dish1 = ["キムチ鍋","豆乳クリーム煮","おでん","ふんわり卵のあんかけうどん","ポトフ"]
dish2 = ["鶏の唐揚げ","麻婆豆腐","餃子","厚揚げの酢豚風","豚キムチ炒め","豚肉の生姜焼き"]
dish3 = ["トマトツナそうめん","バターチキンカレー","うなぎの錦糸丼","夏野菜のガスパチョ","トマトの冷製パスタ"]

st.title("今日の夕食をご提案します")
temp = st.number_input("今日の気温は何度ですか？",-20,45)

# 気温が15度以下の場合はdish1からランダムに1つ選んで表示する
if (temp <= 15):
  dinner = random.choice(dish1)
# 気温が28度以下の場合はdish2からランダムに1つ選んで表示する
elif (temp <= 28):
  dinner = random.choice(dish2)
# それ以外の場合はdish3からランダムに1つ選んで表示する
else:
  dinner = random.choice(dish3)
st.text(f"今日は{dinner}がおすすめです。")

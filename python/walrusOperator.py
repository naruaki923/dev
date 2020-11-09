import random

def lottery(goods):
  # itemsへの代入が行われる(セイウチ演算子)
  if item := random.choice(goods):
    return print(item)
  else:
     return print('MISS!!')

books = ['大吉', '吉', '末吉', '凶', '大凶', None]

# 実行ごとに結果は異なる
lottery(books)
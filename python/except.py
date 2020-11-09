def get_book(index):
  items = ['note', 'notebook', 'sketchbook']
  try:
    book = str(items[index])
    #print(items[index])
    #return items[index]
  except (IndexError) as e:
    print(f'IndexErrorが発生しました: {e}')
    return '範囲外です'
  except (TypeError) as e:
    print(f'TypeErrorが発生しました: {e}')
    return '範囲外です'
  else:
    #例外が発生しなかったときのみelseの中の処理が実行される。

    #upperすべての文字を大文字に変換
    print(book.upper())
    return book.upper()
  """
  except (IndexError, TypeError) as e:
    print(f'例外が発生しました: {e}')
    return '範囲外です'
  """

get_book(2)
#get_book(3)
#get_book('3')

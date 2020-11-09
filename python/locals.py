x = 'ruby'
y = [0, 1]

def f(x): #Python 実践入門 P.168
  # 現在のローカルスコープの内容を表示
  print(locals())
  value = 'book'
  # 変数valueの定義後ローカルスコープの内容を表示
  print(locals())

def g():
  global x # グローバル変数であることを宣言
  x = 'git'
  print(x)

def h():
  y[0] = 2

def i():
  x = 'x'
  def j():
    nonlocal x # xがローカル変数でないことを宣言
    x = 1
    print(x)
  j()
  print(x)



if __name__ == "__main__":
    f('python')
    g()
    print(x)
    print(y) #[0, 1]になる
    h()
    print(y) #[2, 1]になる
    print(globals())
    
    i()
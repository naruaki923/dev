class Page: #Python 実践入門 P.125
  def __init__(self, num, content, section=None):
    self.num = num
    self.content = content
    self.section = section
  def output(self):
    return f'{self.content}'


class SubPage(Page):
  title_page = Page(0, 'Python Practice Book')
  title_page.output()
  title_page.change = 923


class Klass: #Python 実践入門 P.130
  def __new__(cls, *args): #コンストラクタ
    print(f'{cls=}')
    print('new', args)
    # インスタンスを作成して返す
    return super().__new__(cls)
  def __init__(self, *args): #イニシャライザ
    # インスタンスの初期化はこちらで行う。
    print('init', args)



  def some_method(self):
    print('method')

def some_function(self):
    print('function')
    print(self)

if __name__ == '__main__':
  kls = Klass(1, 2, 3)
  kls.some_method() #なぜインスタンスからメソッドを呼ぶときは引数なしでいいのか。klsが渡されるから？
  some_function('123')
  #some_function()

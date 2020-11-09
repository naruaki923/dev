from operator import attrgetter #Python 実践入門 P.137
class Page:
  book_title = 'Python Practice Book'
  def __init__(self, num, content):
    self.num = num
    self.content = content
  @staticmethod #スタティックメソッドにする
  def check_blank(page):
    return bool(page.content)
  def output(self):
    return f'{self.content}'
  # クラスメソッドの第一引数はクラスオブジェクト
  @classmethod
  def print_pages(cls, *pages):
    # クラスオブジェクトの利用
    print(cls.book_title)
    pages = list(pages)
    # ページ順に並べ替えて出力
    for page in sorted(pages, key=attrgetter('num')):
      print(page.output())

if __name__ == '__main__':
  first = Page(1, 'first page')
  second = Page(2, 'second page')
  third = Page(3, 'third page')

  # クラスメソッドの呼び出し
  Page.print_pages(first, third, second)

  # インスタンスからも呼び出せる
  first.print_pages(first, third, second)
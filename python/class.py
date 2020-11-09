class Page: #Python 実践入門 P.136
  book_title = 'Python Practice Book'

if __name__ == '__main__':
  print(Page.book_title)
  Page.book_title = 'No Title'
  print(Page.book_title)
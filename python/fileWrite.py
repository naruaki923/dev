with open('test.txt', 'w') as f:
  for i in range(100):
    f.write('some text' + str(i) + '\n')
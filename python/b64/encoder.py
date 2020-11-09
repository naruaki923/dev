import base64 #Python 実践入門 P.147
import sys

def str_to_base64(x):
  """文字列をbase64表現に変換する

  b64encode()はbyte-like objectを引数にとるため
  文字列はencode()でbyte型にして渡す
  """
  return base64.b64encode(x.encode('utf-8'))

def main():
  target = sys.argv[1]
  print(str_to_base64(target))

if __name__ == '__main__':
  main()

__all__ = ['str_to_base64']

#print(str_to_base64(sys.argv[1]))
#print(str_to_base64(sys.argv[2]))

#print(sys.argv[0])
#print(sys.argv[1])
#print(sys.argv[2])

#print(int(sys.argv[1])*(int(sys.argv[2])))

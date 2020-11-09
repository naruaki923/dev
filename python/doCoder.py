from b64 import encoder, decoder #Python 実践入門 P.154


# 文字列のbase64形式表現
print(encoder.str_to_base64('python'))

# base64形式表現のもとの文字列
# 引数はbyte型なので頭にbをつける
print(decoder.base64_to_str(b'cHl0aG9u'))
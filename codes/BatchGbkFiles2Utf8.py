import sys
import os
import chardet
import codecs

'''
批量修改编码为gbk的文件为utf8
'''
def convert(filename, in_enc="gbk", out_enc="utf8"): # gbk
  try:
    array = filename.split(".")
    if "txt" == array[-1]:
      print('Encode Converting (GBK to UTF-8) : ', filename)
      utfFile = open(filename,"r",encoding=in_enc) # ,'rb'
      tstr = utfFile.read()
      tstr = tstr.encode(out_enc) # .decode(in_enc)；,"ignore"
      utfFile.close()
      utfFile = open(filename, 'wb')
      utfFile.write(tstr)
      utfFile.close()
      print('Success.')
  except Exception as e:
    print(e)
    # 'gbk' codec can't decode byte 0xaa in position 198

def explore(dir):
  for root, dirs, files in os.walk(dir):
    for file in files:
      path = os.path.join(root, file)
      convert(path)

def main(target_path):
  for path in target_path:
    print(path)
    if os.path.isfile(path):
      convert(path)
    elif os.path.isdir(path):
      explore(path)

if __name__ == "__main__":
  main(["D:\\software\\BaiduPCS-Go-v3.5.6-windows-x64\\Downloads\\3445684368_lumir95\\books\\txt_books"])

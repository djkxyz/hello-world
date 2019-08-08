#!/usr/bin/python
import os

def  listFilesToTxt(dir, file, wildcard, recursion ):
    exts = wildcard.split(" ")
    files = os.listdir(dir)
    for name in files:
        fullname = os.path.join(dir, name)
        if(os.path.isdir(fullname) & recursion):
            listFilesToTxt(fullname, file, wildcard, recursion)
        else:
            for ext in exts:
                if(name.endswith(ext)):
                    file.write(name + "\n")
                    break

def Test():
  dir="F:/教学资料/2019年下半年/招生/照片/机电一体化照片0806" \
      "/"     #文件路径
  outfile="binaries.txt"                     #写入的txt文件名
  wildcard = ".jpg "      #要读取的文件类型；

  file = open(outfile, "w")
  if not file:
    print("cannot open the file %s for writing" % outfile)

  listFilesToTxt(dir, file, wildcard, 1)

  file.close()


Test()

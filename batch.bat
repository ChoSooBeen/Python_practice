@echo off
cd C:\Users\edu\AppData\Local\Programs\Python\Python310
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
echo @@@@@@@@@@ pip install success @@@@@@@@@@
cd C:\Users\edu\AppData\Local\Programs\Python\Python310\Scripts
pip install requests
pip install pillow
pip install pygame
pip install pyqt5
echo @@@@@@@@@@ pyqt5 install success @@@@@@@@@@
pip install pyside2
echo @@@@@@@@@@ pyside2 install success @@@@@@@@@@
start C:\Users\edu\AppData\Local\Programs\Python\Python310\Scripts\pyside2-designer.exe
echo @@@@@@@@@@ execute pyside2.py success @@@@@@@@@@
<h1>RFA</h1>
<br>
<br>
<a href="https://github.com/CatTheKocicak/RFA/rfa/rfa.py">View code</a>

# How to convert source code to .exe? 

<a>1) Open cmd and paste following command:</a>
  ```
  pip install pyinstaller
  ```
<br>
<a>2) Download</a> <a href="github.com/CatTheKocicak/RFA/src">source code</a><a>.</a>
<br>
<a>3) Unzip.</a>
<br>
<a>4) Rewrite adress to "powershell"</a>
<br>
<a>5) Paste following command in cmd</a>
```
pyinstaller 'rfa.py'
```
# If you want only 1 file, paste:
```
pyinstaller --onefile 'rfa.py'
```
# If you want it without console, paste:
```
pyinstaller -w 'rfa.py'
```
# If you want only 1 file without console, paste:
```
pyinstaller --onefile -w 'rfa.py'
```
<br>
<a>6) Go to "dist" folder and run rfa.exe</a>

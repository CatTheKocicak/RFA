
# How to convert source code to .exe? 

<a>1) Open cmd and paste following command:</a>

  ```
  pip install pyinstaller
  ```

<br>
<a>2) Download source code.</a>
<br>
<a>3) Unzip.</a>
<br>
<a>4) Rewrite adress to "powershell"</a>
<br>
<a>5) Paste following command in cmd</a>
<br>

```
pyinstaller 'rfa.py'
```

<br>
<h5> If you want only 1 file, paste: </h5>
<br>

```
pyinstaller --onefile 'rfa.py'
```

<br>
<h5> If you want it without console, paste:</h5>
<br>

```
pyinstaller -w 'rfa.py'
```

<br>
<h5> If you want only 1 file without console, paste:</h5>
<br>

```
pyinstaller --onefile -w 'rfa.py'
```

<br>
<a>6) Go to "dist" folder and run rfa.exe</a>

#sht

Simple HTML templating: a Python script that generates a simple HTML page whenever the template or data files are modified.

##Usage

Start `./watch.py` to start watching the `data.txt` and `template.html` files. This will create output in `index.html`.

Check out defaultGenerator.py and imageGenerator.py for two example generators. Create your own generator and run it with

	$ ./watch.py -g myOwnGenerator

##License

sht (C) 2014 Yrjö Kari-Koskinen <ykk@peruna.fi>

sht's source code is licensed with the MIT License, see 
[LICENSE.txt](https://github.com/ykarikos/sht/blob/master/LICENSE.txt)
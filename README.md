# osu! Reverse Accuracy Calculator
A small program giving number of 100s from a given accuracy and 'hit numbers'.
#### [Download the most recent release here.](https://github.com/RedstoneSRG/reverse-accuracy/releases)

### Instructions
Input the accuracy you'd wish to obtain, then the number of 300s, 100s, 50s, and misses of a score on the respective map.

The program will then output in the format of, for example, `402/5/0/0 for 99.1% if FC (99.18%)`. In order:

1. `402/5/0/0` represents the number of 300s, 100s, 50s, and misses respectively.

2. `99.1%` is the accuracy requested.

3. I realized `if FC` is not true - acc is same if you sliderbreak and get five 100s in the end. I'm too lazy to go back and fix this small thing, so whatever.

4. `99.18%` is the actual accuracy of 402/5/0/0. The program's accuracy is always higher than or equal to the requested accuracy.

### Notes
* This program is made for [osu!](http://osu.ppy.sh/), a free-to-play rhythm game. This program is third-party software and is not associated with osu! and its brand.

* This program uses the [PySimpleGUI library](https://pypi.org/project/PySimpleGUI/).

* This program is packaged with [PyInstaller](https://pypi.org/project/PyInstaller/).

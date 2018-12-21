Digole LCD Driver

Tested with Digole 160x128 Color LCD 1.8" DSDM/Serial

Raspberry Pi 3 B using the i2c bus

Examples at www.github.com/jethornton/digole

Installing ```pip3 install digole```

Upgrade ```pip3 install digole --upgrade```

Importing ```from digole import lcd```

Create a new instance and use the default i2c address of 0x27 ```s = lcd()```

Create a new instance and use a different i2c address ```s = lcd(0x29)```

clear the screen ```s.clearScreen()```

write a line of text ```s.writeLine('Text to write')```

change X start position from the left edge in columns```s.changePosition(x)```

change XY start position of the text from the top left corner in columns, rows
```s.changePosition(x,y)```

```s.changePosition(0,2) # start the text on column 0 row 2```

Change Foreground Color color value 0-255 ```s.changeForeColor(color)```
color can be an int 0-255, a hex 0x0-0x255 or a color name from the chart.

Black   =   0 = 0x0
Navy    =   2 = 0x2
Blue    =   3 = 0x3
Green   =  24 = 0x18
Teal    =  27 = 0x1B
Lime    =  28 = 0x1C
Aqua    =  31 = 0x1F
Maroon  = 192 = 0xC0
Purple  = 195 = 0xC3
Olive   = 219 = 0xDB
Red     = 224 = 0xE0
Magenta = 227 = 0xE3
Yellow  = 252 = 0xFC
White   = 255 = 0xFF




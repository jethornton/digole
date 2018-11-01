Digole LCD Driver

Tested with Digole 160x128 Color LCD 1.8" DSDM/Serial

Raspberry Pi 3 B using the i2c bus

Installing ``` pip3 install digole ```

Upgrade ``` pip3 install digole --upgrade ```

Importing ```from digole import lcd```

Create a new instance and use the default i2c address of 0x27 ``` s = lcd() ```

Create a new instance and use a different i2c address ``` s = lcd(0x29) ```

clear the screen ``` s.clearScreen() ```

write a line of text ``` s.writeLine('Text to write') ```

change X start position from the left edge in columns ``` s.changePosition(x) ```

change XY start position of the text from the top left corner in columns, rows
```s.changePosition(x,y)

s.changePosition(0,2) # start the text on column 0 row 2```

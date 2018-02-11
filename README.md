# Bitcoin Price Monitor
I might implement other cryptocurrencies and make them configurable in the future.


## Preview:
Indicator and dropdown menu:<br>
![](https://i.imgur.com/pLPlwpT.png?1)
![](https://i.imgur.com/m9sCl0k.png?1)

Notification:<br>
![](https://i.imgur.com/N6Xl1vt.png?1)

## Installation:
Install all the Python dependencies:
```
$ sudo apt update && sudo apt upgrade
$ git clone https://github.com/sirajuddin97/BTCMonitor
[List is not complete! I'll add more dependencies later.]
```

## Run:
```
$ cd BTCMonitor
$ make
```

## Configuration:
```
[settings]
refresh_rate = 60 **#delay in seconds between each price lookup)**
min_value = 8000 (minimum )
max_value = 10000
```

# TradeSignals
TradeSignals is a program written in Pyhton 3.7+ to check simples strategy and show the result in Plotly off-line HTML chart. Also, is part of a huge private project.
TradeSignal pretend scratch how to work with the Binance api, implement a strategy and see the results.

TradeSignals was made only with demonstrative purpose!

## Table of contents

* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Run](#run)
* [Strategy info](#strategy-info)

## General info
The purpose of this project is to evaluate the entry/out point of the market. The project is small for a while, but is helpful to back-test your profitable trade. 

Any question or suggestion please let me know!
  
## Technologies
Project is created using:
* Python
* Plotly
* Binance API
  
## Setup
You should to have install Python3+, Pandas and Plotly.
You just need to clone the github repo and entry to the directory.

```
$ git clone https://github.com/arrdguez/trade_signals.git
$ cd ./trade_signals
```
## Run

To run TradeSignals and run it passing the parameter -h to check if all is alright! 
```
$ cd ./trade_signals
$ ./main.py -h
```
By default TradeSignals check the strategy in the symbol "BTCUSDT" in the time frame "1h". You can pass parameter via which symbol and time-frame you wish:  

```
$ ./main.py -s ETHUSDT -t 5m
```
If either symbol and time-frame it is not in the exchange the program will abort.   

## Strategy info

The strategy used by default it is only with demonstrative purpose. Feel free and play with it.



## License

MIT

**Free Software!**

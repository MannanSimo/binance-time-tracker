# binance-time-tracker

Simple toolkit to measure latency of Binance Futures F and D API.
## Requirements
---
You need Python **3.6** or later to run this application.

In Ubuntu, Mint and Debian you can install required libraries like this:

    $ pip3 install -r requirements.txt

The Binance API SDK is not available as pip package yet.
The following steps are required:

    $ git clone https://github.com/Binance-docs/Binance_Futures_python
    $ cd Binance_Futures_python
    $ python3 setup.py install
## How to run
---
Provide **API_KEY** and **SECRET_KEY** in **CONFIG.INI** file.
Please visit this page for more details:
https://www.binance.com/en/support/faq/360002502072

Execute mentioned below commands after updating of **CONFIG.INI**:

    $ git clone https://github.com/MannanSimo/binance-time-tracker
    $ cd binance-time-tracker
    $ python3 main.py
![Скриншот софта](https://i.imgur.com/hqwFMrT.png)


# RU: Для корректной работы требуется Python версии 3.11. Вы можете скачать его [здесь](https://www.python.org/downloads/release/python-3110).

## Внимание  
1. В файл `Wallets.txt` вам нужно поместить кошельки. **НЕ ПРИВАТНИКИ, БУДЬТЕ ВНИМАТЕЛЬНЫ!**

2. Кошельки должны быть добавлены в вайтлист, можно сделать через мой [генератор кода](https://th0masi.github.io/gate-whitelist-add/).


Софт ожидает достижения определенного уровня комиссии в $MEME (указывается в конфигурации). Как только комиссия опускается до заданного уровня, софт выводит средства на кошельки, указанные в файле `wallets.txt`.

## Файл конфигурации `Config.py`
`API_KEY`          = "ваш API KEY"  
`API_SECRET`       = "ваш API SECRET"  
`PASSPHRASE`       = "ваш API пароль OKX"
`MAX_FEE_MEME_GAS` = "максимальная сумма комиссии в $MEME"  
`AMOUNT`           = "сумма вывода без учета комиссии"  
`DELAY`            = "задержка между аккаунтами"  



# ENG: For the software to work correctly, Python version 3.11 is required. You can download it [here](https://www.python.org/downloads/release/python-3110).

## Attention
1. In the `Wallets.txt` file, you should add wallet addresses, **NOT PRIVATE KEYS! PLEASE BE CAREFUL!**

2. Your wallets must be whitelisted. To add them, use the console and [my whitelist code generator](https://th0masi.github.io/gate-whitelist-add/).


The software waits for a certain commission level in $MEME (which can be set in the configuration) to be reached. Once the commission drops to the required amount, the software automatically processes withdrawals for all the wallets listed in `wallets.txt`.

## Configuration File `Config.py`
`API_KEY` = "your API KEY"  
`API_SECRET` = "your API SECRET"  
`PASSPHRASE`  = "your API password from OKX"
`MAX_FEE_MEME_GAS` = "maximum commission amount in $MEME"  
`AMOUNT` = "withdrawal amount excluding commission (minimum 69)"  
`DELAY` = "delay between accounts"  

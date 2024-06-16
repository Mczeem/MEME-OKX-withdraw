import ccxt
import random
import time
from sys import stderr

import config
from loguru import logger

logger.remove()
logger.add(stderr, format='<white>{time:HH:mm:ss}</white>'
                          ' | <level>{level: <8}</level>'
                          ' | <cyan>{line}</cyan>'
                          ' - <white>{message}</white>')
logger.add(
    "logfile.log",
    rotation="3 days",
    format="<green>{time}</green> | "
           "<level>{level}</level> | "
           "<cyan>{name}</cyan>:"
           "<cyan>{function}</cyan>:"
           "<cyan>{line}</cyan> - "
           "<level>{message}</level>"
)

token_code = 'MEME'
network = 'ERC20'

def control_fee():
    while True:
        try:
            logger.info("Fetching withdraw fees...")
            fees = exchange.fetch_deposit_withdraw_fees([token_code])
            
            if token_code in fees:
                fee_info = fees[token_code]
                max_fee = config.MAX_FEE_MEME_GAS

                network_fees = fee_info.get('networks', {}).get(network, {})
                fee = network_fees.get('withdraw', {}).get('fee', None)

                if fee is not None and float(fee) <= max_fee:
                    logger.success(f'Current fee: {fee} ${token_code}, go withdraw!')
                    return float(fee)
                else:
                    logger.info(f'Current fee: {fee} ${token_code}, wait for {max_fee} ${token_code}')
            else:
                logger.error(f'No fee info available for {token_code}')

        except Exception as e:
            logger.error(f'Cant get current fee, error: {e}')
            continue

        logger.info('Sleep 120 sec...')
        time.sleep(120)

if __name__ == '__main__':
    exchange = ccxt.okx({
        'apiKey': config.API_KEY,
        'secret': config.API_SECRET,
        'password': config.PASSPHRASE,  # OKX requires a passphrase
    })

    with open('wallets.txt', 'r') as file:
        wallet_addresses = [line.strip() for line in file]

    logger.info("Starting the withdrawal process...")

    for address in wallet_addresses:
        while True:
            logger.info(f"Processing wallet address: {address}")
            fee = control_fee()
            logger.info(f"Control fee returned: {fee}")

            # Ensure the net amount is within the defined range
            net_amount = random.uniform(*config.AMOUNT)

            try:
                logger.info(f" {address} | Try to withdraw {net_amount} ${token_code}...")
                response = exchange.withdraw(token_code, net_amount, address, params={
                    'network': network,
                })

                withdrawal_id = response.get('id', None)

                if withdrawal_id:
                    logger.success(f" {address} | Successfully withdrew {net_amount} ${token_code} [ID: {withdrawal_id}]")
                    break
                else:
                    logger.error(f" {address} | Withdrawal failed, no ID returned")

            except ccxt.BaseError as error:
                error_message = str(error)
                logger.error(f"Error occurred: {error_message}")

                if "INVALID_PARAM_VALUE" in error_message:
                    logger.error(f" {address} | Account not in whitelist: {error}")

                elif "Invalid key provided" in error_message:
                    logger.error(f" {address} | Invalid API key")
                    exit()

                elif "Signature mismatch" in error_message:
                    logger.error(f" {address} | Invalid API secret")
                    exit()

                elif "Insufficient balance" in error_message:
                    logger.error(f" {address} | Insufficient balance, retrying...")

                else:
                    logger.error(f" {address} | Unexpected error: {error}")
                    break

        delay = random.randint(*config.DELAY)
        logger.info(f"Waiting for {delay} seconds before processing the next address...")
        time.sleep(delay)

    logger.success("All tasks done!")

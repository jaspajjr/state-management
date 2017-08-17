import asyncio
from actions import update_command, update_prices, buy


if __name__ == '__main__':
    state = {
        'command': 'hold',
        'prices': [],
        'cash': 0,
        'btc': 0
            }
    event_loop = asyncio.get_event_loop()
    event_loop.set_debug(True)
    try:
        event_loop.run_until_complete(update_command(state))
        event_loop.run_until_complete(buy(state))
        event_loop.run_until_complete(update_prices(state))
    finally:
        event_loop.close()

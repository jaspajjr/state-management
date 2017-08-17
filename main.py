import asyncio
from reducers import get_prices, get_command


async def update_prices(state):
        '''
        Updates the state with new prices.
        '''
        coroutines = [get_prices(state)]
        completed, pending = await asyncio.wait(coroutines)


async def update_command(state):
        '''
        Updates the buy/sell command in state
        '''
        coroutines = [get_command(state)]
        completed, pending = await asyncio.wait(coroutines)


if __name__ == '__main__':
    state = {
        'command': 'hold'
            }

    event_loop = asyncio.get_event_loop()
    event_loop.set_debug(True)
    try:
        event_loop.run_until_complete(update_command(state))
        event_loop.run_until_complete(update_prices(state))
    finally:
        event_loop.close()
    print(state)

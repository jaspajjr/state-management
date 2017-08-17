import asyncio
from reducers import get_prices, get_command, update_after_buy


async def buy(state):
        '''
        Calculates the available orders and executes them.
        '''
        order = {
            "size": 0.01,
            "price": 0.1,
            "side": "buy",
            "product_id": "BTC-USD"
            }
        coroutines = [update_after_buy(state, order)]
        completed, pending = await asyncio.wait(coroutines)


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

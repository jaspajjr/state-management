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

import asyncio
from reducers import do_thing, get_command
from functools import partial


# async def main(args):
#         '''
#         Creates a group of coroutines and waits for them to finish.
#         '''
#         coroutines = [partial_do_thing(key, url) for (key, url) in [
#             ('hello', 'world'), ('foo', 'bar')]]
#         completed, pending = await asyncio.wait(coroutines)


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
    args = [(state, 'hello', 1),
            (state, 'world', 2),
            (state, 'foo', 3),
            (state, 'bar', 4)]

    # partial_do_thing = partial(do_thing, state)
    event_loop = asyncio.get_event_loop()
    event_loop.set_debug(True)
    try:
        # event_loop.run_until_complete(main(args))
        event_loop.run_until_complete(update_command(state))
    finally:
        event_loop.close()
    print(state)

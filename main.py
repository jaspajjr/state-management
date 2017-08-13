import asyncio


async def do_thing(state, key, url):
    state[key] = url
    print(state)


async def main(args):
        '''
        Creates a group of coroutines and waits for them to finish.
        '''
        coroutines = [do_thing(state, key, url) for (state, key, url) in args]
        completed, pending = await asyncio.wait(coroutines)


if __name__ == '__main__':
    state = {}
    args = [(state, 'hello', 1),
            (state, 'world', 2),
            (state, 'foo', 3),
            (state, 'bar', 4)]

    event_loop = asyncio.get_event_loop()
    try:
        event_loop.run_until_complete(main(args))
    finally:
        event_loop.close()

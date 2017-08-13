import asyncio


async def add_item(state, key, value):
    '''
    Add key, value to the state dictionary
    '''
    def do_thing():
        state[key] = value
    await do_thing()
    print(state)


if __name__ == '__main__':
    state = {}
    key_list = ['word'.join('_{}'.format(x)) for x in range(10)]
    value_list = [x for x in range(10)]
    tasks = [add_item(state, 1, 2)]

    event_loop = asyncio.get_event_loop()
    try:
        event_loop.run_until_complete(
                asyncio.async(add_item(state, 'hello', 2)))
    finally:
        event_loop.close()

async def do_thing(state, key, url):
    state[key] = url


async def get_command(state):
    command = 'buy'
    state['command'] = command

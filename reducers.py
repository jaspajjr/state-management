from prices import get_prices_gdax


async def get_command(state):
    command = 'buy'
    state['command'] = command


async def get_prices(state):
    prices = get_prices_gdax()
    state['prices'] = prices


async def update_after_buy(state, order):
    state['cash'] -= order['price']
    state['btc'] += order['size']
    print(order, state['cash'], state['btc'])

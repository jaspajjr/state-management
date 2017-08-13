import asyncio


async def do_thing(state, key, url):
    state[key] = url
    print(state)


async def main(state, key, urls):
        '''
        Creates a group of coroutines and waits for them to finish.
        '''
        coroutines = [do_thing(state, key, url) for url in urls]
        completed, pending = await asyncio.wait(coroutines)
        for item in completed:
            print(item.result())


if __name__ == '__main__':
    urls = ["http://www.irs.gov/pub/irs-pdf/f1040.pdf",
            "http://www.irs.gov/pub/irs-pdf/f1040a.pdf",
            "http://www.irs.gov/pub/irs-pdf/f1040ez.pdf",
            "http://www.irs.gov/pub/irs-pdf/f1040es.pdf",
            "http://www.irs.gov/pub/irs-pdf/f1040sb.pdf"]

    state = {}
    key = 'hello'
    event_loop = asyncio.get_event_loop()
    try:
        event_loop.run_until_complete(main(state, key, urls))
    finally:
        event_loop.close()

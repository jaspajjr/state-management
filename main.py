import asyncio
import os
import urllib.request


async def download_coroutine(url):
    '''
    A coroutine to dl the specified url.
    '''
    req = urllib.request.urlopen(url)
    file_name = os.path.basename(url)
    print(file_name)

    with open(file_name, 'wb') as file_handle:
        while True:
            chunk = req.read(1024)
            if not chunk:
                break
            file_handle.write(chunk)
        msg = 'Finished downloading {filename}'.format(filename=file_name)
    return msg


async def main(urls):
        '''
        Creates a group of coroutines and waits for them to finish.
        '''
        coroutines = [download_coroutine(url) for url in urls]
        completed, pending = await asyncio.wait(coroutines)
        for item in completed:
            print(item.result())


if __name__ == '__main__':
    urls = ["http://www.irs.gov/pub/irs-pdf/f1040.pdf",
            "http://www.irs.gov/pub/irs-pdf/f1040a.pdf",
            "http://www.irs.gov/pub/irs-pdf/f1040ez.pdf",
            "http://www.irs.gov/pub/irs-pdf/f1040es.pdf",
            "http://www.irs.gov/pub/irs-pdf/f1040sb.pdf"]

    event_loop = asyncio.get_event_loop()
    try:
        event_loop.run_until_complete(main(urls))
    finally:
        event_loop.close()

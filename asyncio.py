# import asyncio

# async def find_divisibles(inrange, div_by):
#     print("finding nums in range {} divisible by {}".format(inrange, div_by))
#     located = []
#     for i in range(inrange):
#         if i % div_by == 0:
#             located.append(i)
#         if i % 500000 == 0:
#             await asyncio.sleep(0.0001)
#     print("Done w/ nums in range {} divisible by {}".format(inrange, div_by))
#     return located

# async def main():
#     divs1 = loop.create_task(find_divisibles(508000, 34113))
#     divs2 = loop.create_task(find_divisibles(100052, 3210))
#     divs3 = loop.create_task(find_divisibles(500, 3))
#     await asyncio.wait([divs1, divs2, divs3])

# if __name__ == '__main__':
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(main())
#     loop.close()


import gevent.monkey
from urllib.request import urlopen
gevent.monkey.patch_all()
urls = ['http://www.google.com', 'http://www.yandex.ru', 'http://www.python.org']

def print_head(url):
    print('Starting {}'.format(url))
    data = urlopen(url).read()
    print('{}: {} bytes: {}'.format(url, len(data), data))

jobs = [gevent.spawn(print_head, _url) for _url in urls]

gevent.wait(jobs)
from time import sleep, time
import asyncio


async def get_pages(site_name):
    await asyncio.sleep(0.5)
    print(f'Get page for {site_name}')
    return range(1, 4)


async def get_pages_data(site_name, page):
    await asyncio.sleep(1)

    return f'Data from page {page} ({site_name})'


# Возвращает корутину или сопрограмму.
async def spider(site_name):
    all_data = []
    pages = await get_pages(site_name)
    for page in pages:
        data = await get_pages_data(site_name, page)
        all_data.append(data)
    return all_data

start = time()

spiders = [
    asyncio.ensure_future(spider("Blog")),
    asyncio.ensure_future(spider("News")),
    asyncio.ensure_future(spider('Forum'))
]

# Диспетчер событий.
event_loop = asyncio.get_event_loop()

# Сообщаем диспетчеру событий что он должен выполнятся до тех пока не завершатся все сопрограммы(корутины) из списка.
result = event_loop.run_until_complete(asyncio.gather(*spiders))
print(result)
# Завершаем цикл.
event_loop.close()

print(time() - start)

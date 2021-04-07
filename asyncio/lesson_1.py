from time import sleep, time
import asyncio


start = time()


# Возвращает корутину или сопрограмму.
async def spider(site_name):
    for page in range(1, 4):
        # await передаёт управление из функции обратно в event_loop что бы диспетчер мог запустить другие функции.
        await asyncio.sleep(1)
        print(site_name, page)


spiders = [
    asyncio.ensure_future(spider("Blog")),
    asyncio.ensure_future(spider("News")),
    asyncio.ensure_future(spider('Forum'))

]
# Диспетчер событий.
event_loop = asyncio.get_event_loop()

# Сообщаем диспетчеру событий что он должен выполнятся до тех пока не завершатся все сопрограммы(корутины) из списка.
event_loop.run_until_complete(asyncio.gather(*spiders))

# Завершаем цикл.
event_loop.close()

print(time() - start)

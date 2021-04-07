from time import sleep, time


start = time()


def spider(site_name):
    for page in range(1, 4):
        sleep(1)
        print(site_name, page)


spider("Blog")
spider("News")
spider("Forum")

print(time() - start)

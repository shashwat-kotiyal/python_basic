import asyncio
import time

# synchronus
# asynchronus
# main thread --> subrutine-> mainthread
# corutine in
# concurrency and parallism


def brew_coffee_old():
    print("starting async brew_coffe(): w/o async")
    time.sleep(3)
    print("End brew_coffe()")
    return "coffe ready "


def toastBagle_old():
    print("starting toastBagle(): w/o async")
    time.sleep(2)
    print("end toastBagle():")
    return "bagle toasted"


def main_old():
    start_time = time.time()
    result_coffe = brew_coffee_old()
    result_bagle = toastBagle_old()
    end_time = time.time()
    print(f" 🛑 total_time:{start_time - end_time}")


async def brew_coffee():  # to make corutine add async keyword
    print("starting async brew_coffe(): w/o async")
    await asyncio.sleep(3)  # need to add await infort of cmd which is awaitable ,
    # sleep is not awaitable we have asyncio.sleep function
    print("End brew_coffe()")
    return "coffe ready "


async def toastBagle():
    print("starting toastBagle(): w/o async")
    await asyncio.sleep(2)
    print("end toastBagle():")
    return "bagle toasted"


async def main():
    start_time = time.time()
    # result_coffe =brew_coffee_old()
    # result_bagle =toastBagle_old()
    # can call corutine in batch or indivisually
    print("*" * 10 + "Calling in batch" + "*" * 10)
    batch = asyncio.gather(
        brew_coffee(), toastBagle()
    )  # gather to gather modules for concurrent execution
    # calling is calling corutine object not corutine values
    result_coffe, result_bagle = await batch
    # anything which have await keyword need to put async keyword before manin function
    # need to awit in same order as passed in gather function
    end_time = time.time()
    print(f"🚀total_time :{start_time - end_time}")

    print("*" * 10 + "Calling in indivisual " + "*" * 10)

    start_time = time.time()
    coffe_task = asyncio.create_task(brew_coffee())
    bagle_task = asyncio.create_task(toastBagle())
    result_coffe = await coffe_task
    result_bagle = await bagle_task
    end_time = time.time()
    print(f"🚀total_time :{start_time - end_time}")


if __name__ == "__main__":
    main_old()
    # main() #cannot call async function like this RuntimeWarning: coroutine 'main' was never awaited
    asyncio.run(main())

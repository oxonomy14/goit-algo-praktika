from queue import Queue
import random
import time

request_queue = Queue()


def generate_request():
    request_id = random.randint(1000, 9999)
    request = f"Заявка №{request_id}"

    request_queue.put(request)
    print(f"Створено: {request}")


def process_request():
    if not request_queue.empty():
        request = request_queue.get()
        print(f"Обробляється: {request}")
        time.sleep(1)
        print(f"{request} оброблена")
    else:
        print("Черга порожня")


while True:
    # Генеруємо від 1 до 3 нових заявок
    for _ in range(random.randint(1, 3)):
        generate_request()

    # Обробляємо одну заявку
    process_request()

    # Показуємо кількість заявок у черзі
    print(f"Заявок у черзі: {request_queue.qsize()}")

    command = input("Натисніть Enter для продовження або 'q' для виходу: ")

    if command.lower() == "q":
        break

from concurrent.futures import ProcessPoolExecutor
import time

def calculate_square(n):
    time.sleep(2)
    return n * n

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]

    with ProcessPoolExecutor() as executor:
        results = executor.map(calculate_square, numbers)

    for result in results:
        print(result)

    print("All calculations done.")
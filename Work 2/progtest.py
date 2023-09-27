import random
import time

def generate_random_numbers():
    for _ in range(20):
        random_number = random.randint(35000, 98000)
        print(random_number)
        time.sleep(0.5)

if __name__ == "__main__":
    generate_random_numbers()

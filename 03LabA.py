import time

def compute():
    # Example task: Sum of numbers from 1 to 100 million
    total = 0
    for i in range(1, 100000001):
        total += i
    return total

def main():
    start_time = time.time()
    result = compute()
    end_time = time.time()
    
    print("Result:", result)
    print("Time taken (seconds):", end_time - start_time)

if __name__ == "__main__":
    main()
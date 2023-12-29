def recursive_sum(n, limit):
    # Base case: if n exceeds the limit, return 0
    if n > limit:
        return 0

    # Recursive case: add the current number to the sum of the rest
    if n % 2 == 0:  # even
        return n + recursive_sum(n + 2, limit)
    else:  # odd
        return n + recursive_sum(n + 2, limit)

def main():
    # Input integer
    n = int(input())

    # Determine the limit based on the parity of n
    limit = 100 if n % 2 == 0 else 99

    # Calculate the sum using the recursive function
    result = recursive_sum(n, limit)

    # Output the result
    if n % 2 == 0:
        print(result)
    else:
        print(result)

if __name__ == "__main__":
    main()
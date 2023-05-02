import os
import sys


def load_things(filename):
    with open(filename, "r") as file:
        return [line.strip() for line in file.readlines()]


def save_things(filename, things):
    with open(filename, "w") as file:
        for thing in things:
            file.write(thing + "\n")


def binary_search_insert(sorted_things, new_thing):
    left = 0
    right = len(sorted_things)

    while left < right:
        mid = (left + right) // 2
        print(f"Is '{new_thing}' better than '{sorted_things[mid]}'? (yes/no/stop)")
        answer = input().lower()

        if answer == "yes":
            right = mid
        elif answer == "no":
            left = mid + 1
        elif answer == "stop":
            return -1
        else:
            print("Invalid input. Please enter 'yes', 'no', or 'stop'.")

    sorted_things.insert(left, new_thing)
    return left


def main(input_file, output_file):
    things = load_things(input_file)

    if os.path.exists(output_file):
        sorted_things = load_things(output_file)
    else:
        sorted_things = []

    unsorted_things = [thing for thing in things if thing not in sorted_things]

    for thing in unsorted_things:
        position = binary_search_insert(sorted_things, thing)
        if position == -1:
            break

    save_things(output_file, sorted_things)
    print("Current sorted list saved to", output_file)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python comparer.py <input_file> <output_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    main(input_file, output_file)

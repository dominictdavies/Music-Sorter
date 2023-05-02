import os
import sys
import webbrowser
import urllib.parse


def load_things(filename):
    with open(filename, "r") as file:
        return [line.strip() for line in file.readlines()]


def save_things(filename, things):
    with open(filename, "w") as file:
        for thing in things:
            file.write(thing + "\n")


def search_thing(thing):
    category = "Toby Fox"
    query = urllib.parse.quote(thing + " " + category)
    url = f"https://www.youtube.com/results?search_query={query}"
    webbrowser.open_new_tab(url)


def binary_search_insert(sorted_things, new_thing):
    left = 0
    right = len(sorted_things)
    show_prompt = True

    while left < right:
        mid = (left + right) // 2

        if show_prompt:
            print(
                f"Is '{new_thing}' better than '{sorted_things[mid]}'? (yes/no/search/stop)"
            )
        answer = input().lower().split()
        show_prompt = False

        if answer[0] == "yes":
            right = mid
            show_prompt = True
        elif answer[0] == "no":
            left = mid + 1
            show_prompt = True
        elif answer[0] == "search":
            if len(answer) > 1:
                if answer[1] == "1":
                    search_thing(new_thing)
                elif answer[1] == "2":
                    search_thing(sorted_things[mid])
                else:
                    print("Invalid input. Please enter 'search 1' or 'search 2'.")
            else:
                search_thing(new_thing)
                search_thing(sorted_things[mid])
        elif answer[0] == "stop":
            return -1
        else:
            print("Invalid input. Please enter 'yes', 'no', 'search', or 'stop'.")

    sorted_things.insert(left, new_thing)
    print(
        new_thing,
        "was inserted into position",
        left + 1,
        "out of",
        len(sorted_things),
        "\n\n",
    )

    return left


def main(input_file, output_file):
    things = load_things(input_file)

    sorted_things = []
    if os.path.exists(output_file):
        sorted_things = load_things(output_file)

    unsorted_things = [thing for thing in things if thing not in sorted_things]

    for thing in unsorted_things:
        position = binary_search_insert(sorted_things, thing)
        if position == -1:
            break

    save_things(output_file, sorted_things)
    print("Current sorted list saved to", output_file)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python Comparer.py <input_file> <output_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    main(input_file, output_file)

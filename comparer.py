import os
import sys


def load_songs(filename):
    with open(filename, "r") as file:
        return [line.strip() for line in file.readlines()]


def save_songs(filename, songs):
    with open(filename, "w") as file:
        for song in songs:
            file.write(song + "\n")


def binary_search_insert(sorted_songs, new_song):
    left = 0
    right = len(sorted_songs)

    while left < right:
        mid = (left + right) // 2
        print(f"Is '{new_song}' better than '{sorted_songs[mid]}'? (yes/no/stop)")
        answer = input().lower()

        if answer == "yes":
            right = mid
        elif answer == "no":
            left = mid + 1
        elif answer == "stop":
            return -1
        else:
            print("Invalid input. Please enter 'yes', 'no', or 'stop'.")

    sorted_songs.insert(left, new_song)
    return left


def main(input_file, output_file):
    if os.path.exists(output_file):
        songs = load_songs(output_file)
    else:
        songs = load_songs(input_file)

    sorted_songs = []

    for song in songs:
        position = binary_search_insert(sorted_songs, song)
        if position == -1:
            break

    save_songs(output_file, sorted_songs)
    print("Current sorted list saved to", output_file)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python comparer.py <input_file> <output_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    main(input_file, output_file)

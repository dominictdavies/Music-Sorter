import os
import sys


def list_songs(music_path):
    return [
        song
        for song in os.listdir(music_path)
        if os.path.isfile(os.path.join(music_path, song))
    ]


def load_sorted(sorted_file):
    with open(sorted_file, "r") as file:
        return [line.strip() for line in file.readlines()]


def save_songs(filename, sorted_songs):
    with open(filename, "w") as file:
        for song in sorted_songs:
            file.write(song + "\n")


def binary_search_insert(sorted_songs, new_song):
    left = 0
    right = len(sorted_songs)

    while left < right:
        mid = (left + right) // 2
        old_song = sorted_songs[mid]
        print(f"Is '{new_song}' better than '{old_song}'? (yes/no/switch)")

        answer = "switch"
        while True:
            answer = input().lower()
            if answer[0] == "s":
                print(f"Now playing: {new_song}")
            elif answer[0] == "y" or answer[0] == "n":
                break
            else:
                print("Invalid response, please enter 'yes', 'no', or 'switch'.")

        if answer[0] == "y":
            right = mid
        elif answer[0] == "n":
            left = mid + 1

    sorted_songs.insert(left, new_song)
    print(f"{new_song} was inserted into position {left + 1} out of {len(sorted_songs)}.\n")

    return left


def main(music_path, sorted_file):
    songs = list_songs(music_path)

    sorted_songs = []
    if os.path.exists(sorted_file):
        sorted_songs = load_sorted(sorted_file)

    unsorted_songs = [song for song in songs if song not in sorted_songs]

    for song in unsorted_songs:
        position = binary_search_insert(sorted_songs, song)
        save_songs(sorted_file, sorted_songs)
        if position == -1:
            break

    print("Sorting complete!")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python music_sorter.py <music_path> <sorted_file>")
        sys.exit(1)

    music_path = sys.argv[1]
    sorted_file = sys.argv[2]
    main(music_path, sorted_file)

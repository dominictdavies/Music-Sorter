import os
import sys


def list_song_names(music_path):
    return [
        song_name
        for song_name in os.listdir(music_path)
        if os.path.isfile(os.path.join(music_path, song_name))
    ]


def save_songs(filename, songs):
    with open(filename, "w") as file:
        for song in songs:
            file.write(song + "\n")


def binary_search_insert(sorted_songs, new_song):
    left = 0
    right = len(sorted_songs)
    show_prompt = True

    while left < right:
        mid = (left + right) // 2

        if show_prompt:
            print(
                f"Is '{new_song}' better than '{sorted_songs[mid]}'? (yes/no/search/stop)"
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
                    print("No more online searching")
                elif answer[1] == "2":
                    print("No more online searching")
                else:
                    print("Invalid input. Please enter 'search 1' or 'search 2'.")
            else:
                print("No more online searching")
        elif answer[0] == "stop":
            return -1
        else:
            print("Invalid input. Please enter 'yes', 'no', 'search', or 'stop'.")

    sorted_songs.insert(left, new_song)
    print(
        new_song,
        "was inserted into position",
        left + 1,
        "out of",
        len(sorted_songs),
        "\n",
    )

    return left


def main(music_path, sorted_file):
    song_names = list_song_names(music_path)

    sorted_songs = []
    if os.path.exists(sorted_file):
        sorted_songs = list_song_names(sorted_file)

    unsorted_songs = [song for song in song_names if song not in sorted_songs]

    for song in unsorted_songs:
        position = binary_search_insert(sorted_songs, song)
        if position == -1:
            break

    save_songs(sorted_file, sorted_songs)
    print("Current sorted list saved to", sorted_file)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python music_sorter.py <music_path> <sorted_file>")
        sys.exit(1)

    music_path = sys.argv[1]
    sorted_file = sys.argv[2]
    main(music_path, sorted_file)

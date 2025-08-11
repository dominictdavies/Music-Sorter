import os
import sys
import pygame


def list_songs(music_path):
    audio_types = {".mp3", ".wav", ".ogg", ".flac", ".aac", ".m4a"}
    return [
        song
        for song in os.listdir(music_path)
        if os.path.isfile(os.path.join(music_path, song))
        and os.path.splitext(song)[1].lower() in audio_types
    ]


def load_sorted(sorted_file):
    with open(sorted_file, "r") as file:
        return [line.strip() for line in file.readlines()]


def play_song(music_path, song):
    song_path = os.path.join(music_path, song)
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.stop()
    pygame.mixer.music.load(song_path)
    pygame.mixer.music.play()


def save_songs(sorted_file, sorted_songs):
    with open(sorted_file, "w") as file:
        for song in sorted_songs:
            file.write(song + "\n")


def binary_search_insert(sorted_songs, new_song, music_path):
    left = 0
    right = len(sorted_songs)

    while left < right:
        mid = (left + right) // 2
        old_song = sorted_songs[mid]

        play_song(music_path, new_song)
        playing_new_song = True
        print(f"Is '{new_song}' better than '{old_song}'? (yes/no/switch)")

        while True:
            answer = input().lower()
            if answer[0] == "y" or answer[0] == "n":
                break
            elif answer[0] == "s":
                next_song = old_song if playing_new_song else new_song
                playing_new_song = not playing_new_song
                play_song(music_path, next_song)
                print(f"Now playing: {next_song}")
            else:
                print("Invalid response, please enter 'yes', 'no', or 'switch'.")

        if answer[0] == "y":
            right = mid
        elif answer[0] == "n":
            left = mid + 1

    sorted_songs.insert(left, new_song)
    print(
        f"{new_song} was inserted into position {left + 1} out of {len(sorted_songs)}.\n\n"
    )

    return left


def main(music_path, sorted_file):
    pygame.mixer.init()

    songs = list_songs(music_path)

    sorted_songs = []
    if os.path.exists(sorted_file):
        sorted_songs = load_sorted(sorted_file)

    unsorted_songs = [song for song in songs if song not in sorted_songs]

    for song in unsorted_songs:
        position = binary_search_insert(sorted_songs, song, music_path)
        save_songs(sorted_file, sorted_songs)
        if position == -1:
            break

    print("Sorting complete!")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python music_sorter.py <music_path> <sorted_file>")
        sys.exit(1)

    music_path = sys.argv[1]
    sorted_file = sys.argv[2] + ".txt"

    try:
        main(music_path, sorted_file)
    except KeyboardInterrupt:
        print("\nExiting...")
        sys.exit(0)

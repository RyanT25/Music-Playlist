
#! Music Playlist

#* Dictionary for Playlist
playlist = {
    "Mardy Bum" : {
        "Artist" : "Arctic Monkeys",
        "Genre" : "Indie Rock"
    },
    "All These Things That I've Done" : {
        "Artist" : "The Killers",
        "Genre" : "Alternative Rock"
    },
    "bellyache" : {
        "Artist" : "Billie Eilish",
        "Genre" : "Pop"
    },
    "How Can I Make It Ok?" : {
        "Artist" : "Wolf Alice",
        "Genre" : "Indie Rock"
    },
    "Acceptable in the 80's" : {
        "Artist" : "Calvin Harris",
        "Genre" : "Electronic Pop"
    },
    "The Runner" : {
        "Artist" : "Foals",
        "Genre" : "Indie Rock"
    },
    "Crying Lightning" : {
        "Artist" : "Arctic Monkeys",
        "Genre" : "Indie Rock"
    },
    "Hotel California" : {
        "Artist" : "The Eagles",
        "Genre" : "Country Rock"
    },
    "Seventeen Going Under" : {
        "Artist" : "Sam Fender",
        "Genre" : "Indie Rock"
    },
    "deja vu" : {
        "Artist" : "Olivia Rodrigo",
        "Genre" : "Pop"
    },
}

#* Add Song Function
def add_song(title, artist, genre):
    playlist[title]={"Artist": artist, "Genre": genre}
    print(f"'{title}' - Has Been Added")

#* View Playlist Function
def view_playlist():
    for songs in playlist:
        print("--------------------")
        print(songs)
        for artist, genre in playlist[songs].items():
            print(f"{artist}: {genre}")

#* Update Song Function
def update_song(title, new_artist, new_genre):
    if title in playlist:
        playlist[title]={"Artist": new_artist, "Genre": new_genre}
    else:
        print(f"{title} Cannot Be Found - Try Again")

#* Delete Song Function
def delete_song(title):
    if title in playlist:
        del playlist[title]
        print(f"'{title}' - Has Been Deleted")
    else:
        print(f"{title} Cannot Be Found - Try Again")

#* Add options for the user (Add, View, Update, Delete)
def options_menu():
    while True:
        print("\nMusic Playlist Options")
        print("--------------------\n")
        print("1. Add Song")
        print("2. View Playlist")
        print("3. Update Song")
        print("4. Delete Song")

        select=input("Select Option 1/2/3/4: ")

        #? Data Validation
        if select=="1":
            print("\n--- 1. Add Song ---")
            add_song(input("Enter Song Title: "), input("Enter Artist's Name: "), input("Enter Genre: "))
        elif select=="2":
            print("\n--- 2. View Playlist ---")
            view_playlist()
        elif select=="3":
            print("\n--- 3. Update Song ---")
            update_song(input("Enter Song Title: "), input("Update Artist's Name: "), input("Update Genre: "))
        elif select=="4":
            print("\n--- 4. Delete Song ---")
            delete_song(input("Enter Song Title: "))
            break
        else:
            print("Invalid Input - Please Select 1/2/3/4")
options_menu()

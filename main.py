
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

#* Add options for the user (Add, View, Update, Delete)


#* Add Song Function
def add_song(title, artist, genre):
    playlist[title]={"Artist": artist, "Genre": genre}
add_song(input("Enter Song Title: "), input("Enter Artist's Name: "), input("Enter Genre: "))

#* View Playlist Function
def view_playlist():
    for songs in playlist:
        print(songs)
        for artist, genre in playlist[songs].items():
            print(f"{artist}: {genre}")
view_playlist()

#* Update Song Function
def update_song(title, new_artist, new_genre):
    if title in playlist:
        playlist[title]={"Artist": new_artist, "Genre": new_genre}
update_song(input("Enter Song Title: "), input("Update Artist's Name: "), input("Update Genre: "))

#* Delete Song Function
def delete_song(title):
    if title in playlist:
        del playlist[title]
        print(f"'{title}' - Has Been Deleted")
delete_song(input("Enter Song Title: "))


class Music:
    def __init__(self, title, singer, genre):
        self.title = title
        self.singer = singer
        self.genre = genre

    def display(self):
        print(f"Title: {self.title}, Singer: {self.singer}, Genre: {self.genre}")

class ManageMusic:
    music_list = []

    @classmethod
    def add_music(cls, title, singer, genre):
        music = Music(title, singer, genre)
        cls.music_list.append(music)
        print(f"Music '{title}' by {singer} added successfully.")

    @classmethod
    def delete_music(cls, title):
        for music in cls.music_list:
            if music.title == title:
                cls.music_list.remove(music)
                print(f"Music '{title}' deleted successfully.")
                return
        print(f"Music '{title}' not found.")

    @classmethod
    def display_all(cls):
        if not cls.music_list:
            print("No music in the list.")
        else:
            for music in cls.music_list:
                music.display()

class SortMusic(ManageMusic):
    @classmethod
    def sort_music(cls):
        if not cls.music_list:
            print("No music to sort.")
        else:
            sorted_list = sorted(cls.music_list, key=lambda x: x.title)
            print("\nMusic list sorted by title (A-Z):")
            for music in sorted_list:
                music.display()

class SearchMusic(ManageMusic):
    @classmethod
    def search_by_singer(cls, singer):
        found = False
        for music in cls.music_list:
            if music.singer.lower() == singer.lower():
                music.display()
                found = True
        if not found:
            print(f"No music found for singer: {singer}")
while True:
    print("\n--- menu utama ---")
    print("1. Tambah Musik")
    print("2. Hapus Musik")
    print("3. Tampilkan semua Musik")
    print("4. Cari Musik Berdasarkan penyanyi")
    print("5. keluar Program")
    pilihan = input("Pilih menu: ")
    if pilihan == '1':
        title = input("masukan judull lagu: ")
        singer = input("masukan penyanyi lagu: ")
        genre = input("masukan genre lagu: ")
        ManageMusic.add_music(title, singer, genre)
    elif pilihan == "2":
        singer = input("masukan nama penyanyi yang akan di hapus: ")
        ManageMusic.delete_music(singer)
    elif pilihan == "3":
        print("\nAll music:")
        ManageMusic.display_all()
    elif pilihan == "4":
        singer = input("Enter singer to search: ")
        SearchMusic.search_by_singer(singer)
    elif pilihan == "5":
        print("Program selesai.")
        break  
    else:
        print("Pilihan tidak valid, coba lagi.")
import pygame
import sys

# Inisialisasi Pygame
pygame.init()

# Tentukan ukuran layar
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Tebak Nama Hewan")

# Warna
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (100, 149, 237)
GREEN = (34, 139, 34)
RED = (255, 0, 0)

# Memuat gambar dan suara dengan error handling
try:
    assets = {
        "kucing": {
            "image": pygame.image.load("./assets/kucing.jpeg"),
            "sound": pygame.mixer.Sound("./assets/kucing.wav"),
        },
        "anjing": {
            "image": pygame.image.load("./assets/anjing.jpeg"),
            "sound": pygame.mixer.Sound("./assets/anjing.wav"),
        },
        "monyet": {
            "image": pygame.image.load("./assets/monyet.jpeg"),
            "sound": pygame.mixer.Sound("./assets/monyet.wav"),
        },
        "burung": {
            "image": pygame.image.load("./assets/burung.jpeg"),
            "sound": pygame.mixer.Sound("./assets/burung.wav"),
        },
        "singa": {
            "image": pygame.image.load("./assets/singa.jpeg"),
            "sound": pygame.mixer.Sound("./assets/singa.wav"),
        }
    }
except pygame.error as e:
    print(f"Error loading asset: {e}")
    pygame.quit()
    sys.exit()

# Variabel untuk menyimpan hewan yang dipilih dan input tebakan
current_animal = None
user_guess = ""
feedback = ""

# Fungsi untuk menghentikan semua suara
def stop_all_sounds():
    for asset in assets.values():
        asset["sound"].stop()

# Fungsi untuk menampilkan gambar dan memainkan suara
def display_animal(animal):
    global current_animal, feedback, user_guess
    stop_all_sounds()
    current_animal = animal
    user_guess = ""
    feedback = ""
    assets[animal]["sound"].play()

# Fungsi untuk menampilkan teks di layar
def display_text(text, position, font_size=36, color=BLACK):
    font = pygame.font.Font(None, font_size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=position)
    screen.blit(text_surface, text_rect)

# Daftar posisi angka pilihan
option_positions = [(120, 550), (220, 550), (320, 550), (420, 550), (520, 550)]

# Game loop
while True:
    screen.fill(BLUE)  # Background berwarna biru

    # Instruksi input
    display_text("Tebak Nama Hewan yang Ditampilkan:", (screen.get_width() // 2, 50), font_size=40, color=WHITE)

    # Menampilkan gambar hewan jika ada yang dipilih
    if current_animal:
        image = assets[current_animal]["image"]
        image_rect = image.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 - 50))
        screen.blit(image, image_rect)

    # Menampilkan hasil tebakan
    display_text("Tebakanmu: " + user_guess, (screen.get_width() // 2, 450), font_size=30, color=WHITE)
    display_text(feedback, (screen.get_width() // 2, 500), font_size=30, color=GREEN if feedback == "Tebakan benar!" else RED)

    # Menampilkan pilihan angka tanpa nama hewan
    for i, pos in enumerate(option_positions):
        display_text(f"{i + 1}", pos, font_size=30, color=WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                display_animal("kucing")
            elif event.key == pygame.K_2:
                display_animal("anjing")
            elif event.key == pygame.K_3:
                display_animal("monyet")
            elif event.key == pygame.K_4:
                display_animal("burung")
            elif event.key == pygame.K_5:
                display_animal("singa")
            elif event.key == pygame.K_RETURN:
                if user_guess.lower() == current_animal:
                    feedback = "Tebakan benar!"
                else:
                    feedback = "Tebakan salah, coba lagi!"
            elif event.key == pygame.K_BACKSPACE:
                user_guess = user_guess[:-1]  # Menghapus karakter terakhir
            else:
                # Menambahkan karakter ke input tebakan
                user_guess += event.unicode

    pygame.display.update()

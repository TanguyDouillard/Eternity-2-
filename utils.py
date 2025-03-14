import pygame

son_check = pygame.mixer.Sound("Son/Check.MP3")
son_faux = pygame.mixer.Sound("Son/Faux.MP3")
son_victoire = pygame.mixer.Sound("Son/Victoire.MP3")


def load_image(path, size):
    image = pygame.image.load(path)
    return pygame.transform.scale(image, size)

def load_sound(path):
    return pygame.mixer.Sound(path)

def play_sound(sound):
    pygame.mixer.Sound.play(sound)
    pygame.mixer.music.stop()

def sons(son,son_jouable):

    if son_jouable == True:

        if son == "son_check":
            pygame.mixer.Sound.play(son_check)
            pygame.mixer.music.stop()

        elif son == "son_faux":
            pygame.mixer.Sound.play(son_faux)
            pygame.mixer.music.stop()

        elif son == "son_victoire":
            pygame.mixer.Sound.play(son_victoire)
            pygame.mixer.music.stop()
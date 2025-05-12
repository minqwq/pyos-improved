import pygame
import pymod

def play_module(fname):
    modplay = pymod.Player()
    modplay.load(fname)
    modplay.play()
    while modplay.playing():
        pass

def play_stdfile(fname):
    try:
        pygame.mixer.init()
        pygame.mixer.stop()
    except Exception:
        pass
    pygame.mixer.music.load(fname)
    pygame.mixer.music.play()

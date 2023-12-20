from PIL import Image
import pygame


def putinwin():
    putinwin = pygame.mixer.Sound("./assets/putinwin.ogg")
    putinwin.play()
    image = Image.open("./assets/putin.jpg")
    image.show()

def sigmawin():
    sigmawin = pygame.mixer.Sound("./assets/sigmawin.ogg")
    sigmawin.play()
    image = Image.open("./assets/sigmawin.jpg")
    image.show()

def fnafwin():
    fnafwin = pygame.mixer.Sound("./assets/fnafwin.ogg")
    fnafwin.play()
    image = Image.open("./assets/fnafwin.jpg")
    image.show()

def pobedawin():
    pobedawin = pygame.mixer.Sound("./assets/pobedawin.ogg")
    pobedawin.play()
    image = Image.open("./assets/pobedawin.jpg")
    image.show()
def dsdeath():
    dsdeath = pygame.mixer.Sound("./assets/dsdeath.ogg")
    dsdeath.play()
    image = Image.open("./assets/dsdeath.png")
    image.show()

def skaladeath():
    skaladeath = pygame.mixer.Sound("./assets/skaladeath.ogg")
    skaladeath.play()
    image = Image.open("./assets/skaladeath.jpg")
    image.show()

def fnafdeath():
    fnafdeath = pygame.mixer.Sound("./assets/fnafdeath.ogg")
    fnafdeath.play()
    image = Image.open("./assets/fnafdeath.jpg")
    image.show()

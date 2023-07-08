import pygame
from sys import exit

from constantes import *
from animaciones import *

from gui_button import Button

global is_paused
global return_to_play

class Menu:
    def __init__(self):
        self.buttons = []
        self.background = None
        self.coordenadas = (0,0)
        self.fill = True

    def update(self):
      return self.handle_events()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                return self.handle_button_click()

    def draw(self, screen):
      MENU_MOUSE_POS = pygame.mouse.get_pos()
      if self.fill:
        screen.fill("black")
      if self.background != None:
        screen.blit(self.background, self.coordenadas)
      for button in self.buttons:
        button.changeColor(MENU_MOUSE_POS)
        button.update(screen)


class MainMenu(Menu):
    def __init__(self):
        super().__init__()
        self.background = background_menu
        self.fill = True

        self.buttons = [
            Button(image=pygame.image.load("./images/play-rect2.png"), x=1060, y=320,
                   text_input="PLAY", base_color="white", hovering_color="yellow"),
            Button(image=pygame.image.load("./images/play-rect2.png"), x=1060, y=400,
                   text_input="LEVELS", base_color="white", hovering_color="yellow"),
            Button(image=pygame.image.load("./images/play-rect2.png"), x=1060, y=480,
                   text_input="QUIT", base_color="white", hovering_color="yellow")
        ]

    def handle_button_click(self):
        mouse_pos = pygame.mouse.get_pos()
        click_magic.play()
        if self.buttons[0].checkForInput(mouse_pos):
            return "play"
        if self.buttons[1].checkForInput(mouse_pos):
            return "levels_menu"
        if self.buttons[2].checkForInput(mouse_pos):
            pygame.quit()
            exit()
        else:
            click_magic.stop()


class LevelsMenu(Menu):
    def __init__(self):
        super().__init__()
        self.fill = True
        self.buttons = [
            Button(image=pygame.image.load("./images/play-rect2.png"), x=WIDTH_PANTALLA / 2, y=320,
                   text_input="LEVEL 1", base_color="white", hovering_color="yellow"),
            Button(image=pygame.image.load("./images/play-rect2.png"), x=WIDTH_PANTALLA / 2, y=400,
                   text_input="LEVEL 2", base_color="white", hovering_color="yellow"),
            Button(image=pygame.image.load("./images/play-rect2.png"), x=WIDTH_PANTALLA / 2, y=480,
                   text_input="LEVEL 3", base_color="white", hovering_color="yellow")
        ]

    def handle_button_click(self):
        mouse_pos = pygame.mouse.get_pos()
        alice_intro.stop()
        click_magic.play()
        if self.buttons[0].checkForInput(mouse_pos):
            return "play_1"
        if self.buttons[1].checkForInput(mouse_pos):
            return "play_2"
        if self.buttons[2].checkForInput(mouse_pos):
            return "play_3"

class PauseMenu(Menu):
    def __init__(self):
        super().__init__()
        self.background = background_pause
        self.coordenadas = ((WIDTH_PANTALLA - background_pause.get_width()
                            ) // 2, (HEIGHT_PANTALLA - background_pause.get_height()) // 2)
        self.fill = False
        self.buttons = [
            Button(image=pygame.image.load("./images/play-rect2.png"), x=WIDTH_PANTALLA / 2, y=250,
                   text_input="CONTINUE", base_color="white", hovering_color="yellow"),
            Button(image=pygame.image.load("./images/play-rect2.png"), x=WIDTH_PANTALLA / 2, y=310,
                   text_input="RESTART", base_color="white", hovering_color="yellow"),
            Button(image=pygame.image.load("./images/play-rect2.png"), x=WIDTH_PANTALLA / 2, y=370,
                   text_input="MAIN MENU", base_color="white", hovering_color="yellow"),
            Button(image=pygame.image.load("./images/play-rect2.png"), x=WIDTH_PANTALLA / 2, y=430,
                   text_input="QUIT", base_color="white", hovering_color="yellow")
        ]

    def handle_events(self):
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              pygame.quit()
              exit()
          if event.type == pygame.MOUSEBUTTONDOWN:
              return self.handle_button_click()
      return False

    def handle_button_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.buttons[0].checkForInput(mouse_pos):
            return "continue"
        if self.buttons[1].checkForInput(mouse_pos):
            return "restart"
        if self.buttons[2].checkForInput(mouse_pos):
            return "main_menu"
        if self.buttons[3].checkForInput(mouse_pos):
            pygame.quit()
            exit()
        return False
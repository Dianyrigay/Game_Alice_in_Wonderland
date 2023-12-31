import pygame
from sys import exit

from constantes import *
from animations import *

from gui_button import Button
from gui_form import TextInput
from sql import *

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

        self.buttons = [
            Button(image=pygame.image.load("./images/play-rect2.png"), x=1120, y=320,
                   text_input="PLAY", base_color="white", hovering_color="yellow"),
            Button(image=pygame.image.load("./images/play-rect2.png"), x=1120, y=400,
                   text_input="LEVELS", base_color="white", hovering_color="yellow"),
            Button(image=pygame.image.load("./images/play-rect2.png"), x=1120, y=480,
                   text_input="RECORDS", base_color="white", hovering_color="yellow"),
            Button(image=pygame.image.load("./images/play-rect2.png"), x=1120, y=560,
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
            return "records"
        if self.buttons[3].checkForInput(mouse_pos):
            pygame.quit()
            exit()
        else:
            click_magic.stop()


class LevelsMenu(Menu):
    def __init__(self):
        super().__init__()
        self.background = levels_image
        self.level_blocked = level_blocked
        self.level_active = level_active
        self.rect_level = level_blocked.get_rect(midbottom = (0, 500))
        self.buttons = [
            Button(image=pygame.image.load("./images/play-rect2.png"), x=200, y=510,
                   text_input="LEVEL 1", base_color="white", hovering_color="yellow"),
            Button(image=pygame.image.load("./images/play-rect2.png"), x=WIDTH_PANTALLA / 2, y=510,
                   text_input="LEVEL 2", base_color="white", hovering_color="yellow"),
            Button(image=pygame.image.load("./images/play-rect2.png"), x=1300, y=510,
                   text_input="LEVEL 3", base_color="white", hovering_color="yellow"),
            Button(image=pygame.image.load("./images/play-rect2.png"), x=WIDTH_PANTALLA / 2, y=750,
                   text_input="BACK", base_color="white", hovering_color="yellow")]
        self.level_status = [True] + [False] * (len(self.buttons) - 1)

    def draw(self, screen):
        super().draw(screen)
        x = self.rect_level.right
        for i, button in enumerate(self.buttons):
            if self.level_status[i]:
                image = self.level_active
            else:
                image = self.level_blocked
            screen.blit(image, (x, self.rect_level.y))
            x += self.rect_level.width + 350

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
        if self.buttons[3].checkForInput(mouse_pos):
            return "main_menu"

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

class FinalMenu(Menu):
    def __init__(self, game_over, game_win, score, level):
        super().__init__()
        self.game_over = game_over
        self.game_win = game_win

        if self.game_over:
            self.background = game_over_image
            self.buttons = [
                Button(image=pygame.image.load("./images/play-rect2.png"), x=WIDTH_PANTALLA / 2, y=300,
                    text_input="RETRY", base_color="white", hovering_color="yellow"),
                Button(image=pygame.image.load("./images/play-rect2.png"), x=WIDTH_PANTALLA / 2, y=380,
                    text_input="MAIN MENU", base_color="white", hovering_color="yellow")
            ]
        if self.game_win:
            ambient_horror.stop()
            self.score = score
            self.level = level
            self.background = you_win
            self.text_input = TextInput(980, 280, 300, 40, 20)
            self.buttons = [
                Button(image=pygame.image.load("./images/play-rect2.png"), x=1120, y=480,
                    text_input="GUARDAR", base_color="white", hovering_color="yellow")
            ]

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if self.game_win:
                self.text_input.handle_event(event)

            if event.type == pygame.MOUSEBUTTONDOWN:
                return self.handle_button_click()
        return False

    def handle_button_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.game_over:
            if self.buttons[0].checkForInput(mouse_pos):
                return "retry"
            if self.buttons[1].checkForInput(mouse_pos):
                return "main_menu"
        if self.game_win:
            nombre = self.text_input.text
            if self.buttons[0].checkForInput(mouse_pos):
                create_table()
                save_score(nombre, self.score, self.level)
                get_score()
                return "guardar"
        return False

    def draw(self, screen):
        super().draw(screen)
        if self.game_win:
            self.text_input.draw(screen)

class High_Scores(Menu):
    def __init__(self):
        super().__init__()
        self.background = high_scores_image
        self.buttons = [
            Button(image=pygame.image.load("./images/play-rect2.png"), x=WIDTH_PANTALLA/2, y=750,
                text_input="BACK", base_color="white", hovering_color="yellow"),
        ]

    def handle_button_click(self):
        mouse_pos = pygame.mouse.get_pos()
        click_magic.play()
        if self.buttons[0].checkForInput(mouse_pos):
            return "main_menu"

    def draw(self, screen):
        super().draw(screen)
        write_screen(screen, "PLAYER", "yellow", "", (300, 300))
        write_screen(screen, "SCORE", "yellow", "", (1050, 300))
        rows = get_score()
        y = 380
        for row in rows:
            write_screen(screen, "", "white", str(row[1]), (300, y))
            write_screen(screen, "", "white", str(row[2]), (1050, y))
            y += 60




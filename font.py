import pygame, sys

class Font:
    _id = "0"
    _fonts = []
    _screen = None

    def __init__(self, SCREEN):
        self._screen = SCREEN
        pygame.font.init()
    
    def __del__(self):
        print("[CLASS] Font class destroyed")

    def register_text(self, size = 100, text = False, color = (255, 255, 255)):
        tmp = {}
        if not text:
            print("[FONT] [FATAL ERROR] No font text where given, exiting")
            pygame.quit()
            sys.exit()
        tmp["text"] = text
        tmp["object"] = pygame.font.Font("./fonts/PUSAB.otf", size)
        tmp["color"] = color
        self._fonts.append(tmp)

    def draw_everything(self):
        for _, font in enumerate(self._fonts):
            renderObj = font["object"].render(font["text"], True, font["color"])
            self._screen.blit(renderObj, (self._screen.get_width()/2 - renderObj.get_width()/2, self._screen.get_height()/2 - renderObj.get_height()/2))
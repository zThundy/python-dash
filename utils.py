from pygame import mouse

class Utils:
    _old_state = None
    def __init__(self):
        self._old_state = (0, 0, 0)
        print("[CLASS] Utils module initialized successfully")

    def mouseClickEvent(self):
        if mouse.get_pressed() == (1, 0, 0):
            if self._old_state != mouse.get_pressed():
                self._old_state = mouse.get_pressed()
                return True
        if self._old_state == (1, 0, 0) and mouse.get_pressed() == (0, 0, 0):
            self._old_state = mouse.get_pressed()
        return False
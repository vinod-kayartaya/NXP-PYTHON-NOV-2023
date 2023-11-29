"""
Example of using Multiple inheritance in Python
"""
from my_utils import dir2


class MobilePhone:
    def __init__(self):
        print('MobilePhone.__init__() called')

    def make_call(self):
        pass


class MusicPlayer:
    def __init__(self):
        print('MusicPlayer.__init__() called')

    def play_music(self):
        pass

    def pause_music(self):
        pass







class Camera:
    def __init__(self):
        print('Camera.__init__() called')

    def take_picture(self):
        pass

    def delete_picture(self):
        pass


# subclass with multiple super classes
class SmartPhone(MobilePhone, MusicPlayer, Camera):
    def __init__(self):
        super().__init__()
        super(MobilePhone, self).__init__()
        super(MusicPlayer, self).__init__()  # MusicPlayer.__init__(self)
        super(Camera, self).__init__()  # Camera.__init__(self)
        print('SmartPhone.__init__() called')

    def message_in_whatsapp(self):
        pass


if __name__ == '__main__':
    sp = SmartPhone()  # new SmartPhone object
    print(dir2(sp))

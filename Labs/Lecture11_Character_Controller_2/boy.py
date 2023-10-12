# 이것은 각 상태들을 객체로 구현한 것임.

from pico2d import load_image
import math


class Idle:

    @staticmethod
    def enter(boy):
        boy.frame = 0
        print('Idle Enter')

    @staticmethod
    def exit(boy):
        print('Idle Exit')

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + 1) % 8
        print('Idle Do')

    @staticmethod
    def draw(boy):
        boy.image.clip_draw(boy.frame * 100, boy.action * 100, 100, 100,
                            boy.x, boy.y)

class Sleep:

    @staticmethod
    def enter(boy):
        boy.frame = 0
        print('고개 숙이기')

    @staticmethod
    def exit(boy):
        print('고개 들기')

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + 1) % 8
        print('드르렁')

    @staticmethod
    def draw(boy):
        boy.image.clip_composite_draw(boy.frame * 100, boy.action * 100, 100, 100,
                            math.pi/2, ' ',
                            boy.x, boy.y, 100, 100)
        pass



class StateMachine:
    def __init__(self, boy):
        self.boy = boy
        self.cur_state = Sleep

    def start(self):
        self.cur_state.enter(self.boy)

    def update(self):
        self.cur_state.do(self.boy)

    def draw(self):
        self.cur_state.draw(self.boy)





class Boy:
    def __init__(self):
        self.x, self.y = 400, 90
        self.frame = 0
        self.action = 3
        self.image = load_image('animation_sheet.png')
        self.state_machine = StateMachine(self)
        self.state_machine.start()

    def update(self):
        self.state_machine.update(self)

    def handle_event(self, event):
        pass

    def draw(self):
        self.state_machine.draw()

import pygame
import sys

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 640

white = (255, 255, 255)
black = (0, 0, 0)


class Player:
    def __init__(self, name):
        self.name = name
        self.imgs = {
            "stand": pygame.transform.scale(
                pygame.image.load(f"./img/{self.name}_stand.png"), (200, 200)
            ),
            "move_l": pygame.transform.scale(
                pygame.image.load(f"./img/{self.name}_move_l.png"), (200, 200)
            ),
            "move_r": pygame.transform.scale(
                pygame.image.load(f"./img/{self.name}_move_r.png"), (200, 200)
            ),
            "emo1": pygame.transform.scale(
                pygame.image.load(f"./img/{self.name}_emo1.png"), (200, 200)
            ),
            "emo2": pygame.transform.scale(
                pygame.image.load(f"./img/{self.name}_emo2.png"), (200, 200)
            ),
            "emo3": pygame.transform.scale(
                pygame.image.load(f"./img/{self.name}_emo3.png"), (200, 200)
            ),
        }
        self.pos = [200, 200]
        self.cur_status = "stand"
        self.exist_move = 0
        self.speed = 3

    def on_move(self, key_event):
        #* 좌, 우 이동
        if key_event[pygame.K_LEFT] and key_event[pygame.K_RIGHT]:
            # left, right 동시에 누르는 경우
            self.cur_status = "stand"
        elif key_event[pygame.K_LEFT]:
            # left, right 중에 left만 있는 경우
            self.cur_status = "move_l"
            self.set_pos((-3, 0))
            self.exist_move += 1
        elif key_event[pygame.K_RIGHT]:
            # left, right 중에 right만 있는 경우
            self.cur_status = "move_r"
            self.set_pos((3, 0))
            self.exist_move += 1
        else:
            # left, right 둘다 없는 경우
            self.cur_status = "move_l"

        #* 상, 하 이동
        if key_event[pygame.K_UP]:
            self.set_pos((0, -3))
            self.exist_move += 1
        if key_event[pygame.K_DOWN]:
            self.set_pos((0, 3))
            self.exist_move += 1
        
        #* 스크린 벗어날 경우 위치 조정
        if self.pos[0] < -100:
            self.pos[0] = -100
        elif self.pos[0] > SCREEN_WIDTH - 100:
            self.pos[0] = SCREEN_WIDTH - 100
        if self.pos[1] < -100:
            self.pos[1] = -100
        elif self.pos[1] > SCREEN_HEIGHT - 100:
            self.pos[1] = SCREEN_HEIGHT - 100


    def on_stand(self, key_event):
        self.cur_status = "stand"
        if key_event[pygame.K_1]:
            self.cur_status = "emo1"
        elif key_event[pygame.K_2]:
            self.cur_status = "emo2"
        elif key_event[pygame.K_3]:
            self.cur_status = "emo3"

    def set_pos(self, ch_pos):
        self.pos[0] += ch_pos[0]
        self.pos[1] += ch_pos[1]

    def get_pos(self):
        return self.pos

    def get_cur_img(self):
        return self.imgs[self.cur_status]


pygame.init()
pygame.display.set_caption("연습")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

p1 = Player("bong")
# p2 = Player("yuri")

clock = pygame.time.Clock()
while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    p1.exist_move = 0
    key_event = pygame.key.get_pressed()
    p1.on_move(key_event)

    if not p1.exist_move:
        p1.on_stand(key_event)

    screen.fill(white)

    screen.blit(p1.get_cur_img(), p1.get_pos())
    # screen.blit(p2.get_cur_img(), p2.get_pos())
    pygame.display.update()

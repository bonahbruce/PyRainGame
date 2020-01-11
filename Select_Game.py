import pygame
import PyRain
import time
# pygame초기화
pygame.init()

# 색상 RGB 설정변수
black = (0, 0, 0)
white = (255, 255, 255)
sky_blue = (153, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
gray = (153, 153, 153)
font = pygame.font.Font(None, 50)

background = pygame.image.load('bg1.png')

pygame.display.set_caption("Menu_Select")


def draw_button(button, screen):
    """사각형 버튼 및 텍스트표면 생성"""
    pygame.draw.rect(screen, button['color'], button['rect'])
    screen.blit(button['text'], button['text rect'])


def create_button(x, y, w, h, text, callback):
    """버튼과 관련된 데이터가 포함된 딕셔너리
    rect, text surface 및 text rect, color
    값 반환
    """
    # 문자 설정 변수
    text_surf = font.render(text, True, black)
    # 사각 버튼 설정 변수
    button_rect = pygame.Rect(x, y, w, h)
    # 텍스트 위치 설정 변수
    text_rect = text_surf.get_rect(center=button_rect.center)
    # 딕셔너리로 값 묶기
    button = {
        'rect': button_rect,
        'text': text_surf,
        'text rect': text_rect,
        'color': gray,
        'callback': callback,
        }
    return button


def main():
    # 출력 화면 크기 및 FPS 설정
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    done = False

    # 테스트로 버튼 클릭시 클릭 카운트 증가시켜 동작확인
    number = 0

    # 추후 이 부분은 PyRain을 불러오는 함수로 바꾸어야함
    def game1():
        for i in range(1,11):
            PyRain.game(i)
            time.sleep(1)
            if PyRain.z :
                break
        
    # 종료버튼으로 누르면 화면닫힘
    def quit_game():
        nonlocal done
        done = True

    # 버튼 설정
    button1 = create_button(250, 100, 250, 80, 'PyRain', game1)
    button2 = create_button(250, 400, 250, 80, 'Exit', quit_game)

    # 리스트를 이용하여 전체 버튼 받기
    button_list = [button1, button2]

    # pygame 동작 수행 부분
    while not done:

        # RGB = Red, Green, Blue
        screen.fill((0, 0, 0))
        # Background Image
        screen.blit(background, (0, 0))

        # 함수를 통해 게임 중간에 발생한 이벤트 감지하여 검사하기위한 인덱스
        for event in pygame.event.get():

            # 함수를 통해 가져온 이벤트가 만약 pygame.QUIT이라는 값과 일치하는지 검사
            if event.type == pygame.QUIT:
                done = True

            # 마우스 버튼에 대한 이벤트 처리 부분
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # 1 : 마우스 왼쪽버튼, 2: 마우스 가운데 버튼, 3: 마우스 오른쪽 버튼
                if event.button == 1:
                    for button in button_list:
                        # `event.pos` 마우스 위치
                        if button['rect'].collidepoint(event.pos):
                            # Increment the number by calling the callback
                            # function in the button list.
                            button['callback']()

            elif event.type == pygame.MOUSEMOTION:
                # 마우스가 움직였을 때의 변화
                # buttons if they collide with the mouse.
                for button in button_list:
                    # 버튼에 마우스 가져다가 놓을 경우
                    if button['rect'].collidepoint(event.pos):
                        button['color'] = gray
                    # 버튼에 마우스가 없을 경우
                    else:
                        button['color'] = white

        for button in button_list:
            draw_button(button, screen)

        # 지금까지 화면에 작성한 모든 행위를 업데이트하기 위한 함수
        # 반드시 pygame의 메인 루프 끝에는 해당 함수를 사용해야 한다.
        pygame.display.update()
        clock.tick(60)

main()
pygame.quit()

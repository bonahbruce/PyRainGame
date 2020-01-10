import pygame

# pygame초기화
pygame.init()

# 색상 RGB 설정변수
black = (0, 0, 0)
white = (255, 255, 255)
sky_blue = (153, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# 화면 크기 조절
size = [1000, 800] # [x축, y축]
screen = pygame.display.set_mode(size)

# 화면 제목 설정
pygame.display.set_caption('Game Select Menu')

# 화면을 초당 몇 번 출력하는지 설정하기 위한 변수
done = False
clock = pygame.time.Clock()

while not done:
    # 지정한 값 만큼 초당 화면을 출력
    clock.tick(60)

    for event in pygame.event.get(): # 함수를 통해 게임 중간에 발생한 이벤트 감지하여 검사하기위한 인덱스

        # 함수를 통해 가져온 이벤트가 만약 pygame.QUIT이라는 값과 일치하는지 검사
        if event.type == pygame.QUIT:
            done = True

    screen.fill(sky_blue) # fill()함수는 화면 전체를 특정 색깔로 모두 채워주는 함수

    # Surface = pygame을 실행할 때 전체적으로 화면을 선언한 변수 값
    # color = 도형의 색깔로 RGB 형태로 데이터의 값 삽입
    # Width = 사각형의 선 크기를 말하며, 기본적으로 0으로 설정된다.
    # 만약 Width의 값을 지정해주게 되면, 색깔채움 없는 빈 상자로 그려주는것을 의미한다.

    # 사각형
    # Rect = 사각형의 [x축, y축, 가로, 세로]의 형태로 삽입

    # 삼각형
    # PointList = 삼각형의 세 개의 점을 [[x축,y축], [x축, y축], [x축, y축]]의 형태로 삽입

    # 원
    # Pos = 원을 그릴 위치를 지정해주는 x,y 좌표 값
    # Radius = 원의 반지름의 길이 값

    # 타원
    # Rect = 타원의 [x축, y축, 가로, 세로]의 형태로 삽입

    # 자유원
    # Rect = 원의 [x축, y축, 가로, 세로]의 형태로 삽입
    # Start_angle = 원을 그릴 시작 위치(0 혹은 원주율인 pi를 기준으로 입력)
    # Stop_angle = 원을 그릴 끝 위치(0 혹은 원주율인 pi를 기준으로 입력)

    # 선
    # Start_pos = 선이 시작하는 점을 말하며 [x,y]형태로 값을 삽입
    # End_pos = 선이 끝나는 점을 말하며 [x,y]형태로 값을 삽입입

    # 여러선
    # Closed = 이어지는 여러 개의 선을 다 그리고 하나의 구역으로 설정할지 결정
    # PointList = 여러 개의 선을 그릴 위치들을 입력

    # 부드러운선
    # StartPos = 선이 시작하는 점을 말하며 [x,y]형태로 값을 삽입
    # EndPos = 선이 끝나는 점을 말하며 [x,y]형태로 값을 삽입
    # Blend = Anti-Aliasing(부드러움) 설정 여부로, True 혹은 False를 입력함

    # 부드러운여러선
    # Closed = 이어지는 여러 개의 선을 다 그리고 하나의 구역으로 설정할지 결정
    # PointList = 여러 개의 선을 그릴 위치들을 입력
    # Blend = Anti-Aliasing(부드러움) 설정 여부로, True 혹은 False를 입력함

    # 사각형 : pygame.draw.rect(Surface, color, Rect, Width=0)
    # 삼각형 : pygame.draw.polygon(Surface, color, PointList, Width=0)
    # 원 : pygame.draw.circle(Surface, color, Pos, Radius, Width=0)
    # 타원 : pygame.draw.ellipse(Surface, color, Rect, Width=0)
    # 자유원 : pygame.draw.arc(Surface, color, Rect, Start_angle, Stop_angle, Width=1)
    # 선 : pygame.draw.line(Surface, color, Start_pos, End_pos, Width=1)
    # 여러선 : pygame.draw.lines(Surface, color, Closed, PointList, width=1)
    # 부드러운선 : pygame.draw.aaline(Surface, color, StartPos, EndPos, Blend=1)
    # 부드러운여러선 : pygame.draw.aalines(Surface, color, Closed, PointList, Blend=1)

    pygame.draw.rect(screen, white, [450, 600, 100, 50],)

    # 지금까지 화면에 작성한 모든 행위를 업데이트하기 위한 함수
    # 반드시 pygame의 메인 루프 끝에는 해당 함수를 사용해야 한다.
    pygame.display.flip()

pygame.quit()
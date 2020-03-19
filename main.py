import pygame


pygame.init()
size = width, height = 501, 501
screen = pygame.display.set_mode(size)
running = True
coords = [50, 50]
positions = []
status = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pos()[0] in range(coords[0] - 50, coords[0] + 50) and \
                    pygame.mouse.get_pos()[1] in range(coords[1] - 50, coords[1] + 50):
                status = 1
        if event.type == pygame.MOUSEBUTTONUP:
            status = 0
            positions = []
    if status == 1:
        if len(positions) > 0:
            if positions[-1] != pygame.mouse.get_pos():
                positions.append(pygame.mouse.get_pos())
        else:
            positions.append(pygame.mouse.get_pos())
        if len(positions) >= 2:
            a = positions[-1][0] - positions[-2][0]
            b = positions[-1][1] - positions[-2][1]
            coords[0] += a
            coords[1] += b
            for i in range(2):
                del positions[0]
    screen.fill(pygame.Color('black'))
    pygame.draw.rect(screen, (0, 255, 0), (coords[0] - 50, coords[1] - 50, 100, 100))
    pygame.display.flip()
pygame.quit()
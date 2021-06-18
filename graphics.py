from pygame import draw
import pygame, math, random, schedule

screen = None
size = ()
dots = {}
simulate = False
simulateData = {"pos": 0, "dir": True, "last": 200}
def drawDefault():
    def scaledArc(scale, color):
        w = size[0]*scale
        h = size[1]*scale
        px = size[0]*0.5*(1-scale)
        py = size[1]*(1-scale)+2
        draw.arc(screen, color, (px, py, w, h*2), math.radians(-1), math.radians(180), 1)
    scaledArc(0.25, (0, 150, 0))
    scaledArc(0.50, (0, 150, 0))
    scaledArc(0.75, (0, 150, 0))
    scaledArc(1, (0, 255, 0))
    draw.line(screen, (0, 255, 0), (0, size[1]-1), (size[0], size[1]-1), 1)

def drawDots():
    global size, dots
    xOff = size[0] / 2
    yOff = size[1] - 1
    for k, v in dots.items():
        angle = k - 90
        distance = v
        if distance < 0: return
        x = xOff + (math.sin(math.radians(angle)) * distance)
        y = yOff - (math.cos(math.radians(angle)) * distance)
        draw.circle(screen, (0,0,255), (x, y), 2, 2)

def simulateTask():
    global simulateData, dots
    if simulateData["dir"]:
        simulateData["pos"] += 1
    else:
        simulateData["pos"] -= 1
    if simulateData["pos"] >= 180 or simulateData["pos"] <= 0:
        simulateData["dir"] = not simulateData["dir"]
    out = (random.random() * 10) - 4.9 + simulateData["last"]
    while out < 0 or out > 400:
        out = (random.random() * 10) - 4.9 + simulateData["last"]
    simulateData["last"] = out
    dots[simulateData["pos"]] = out
    
def main():
    global size, screen
    if (simulate):
        schedule.every(0.01).seconds.do(simulateTask)
    size = (800, 400)
    screen = pygame.display.set_mode(size)

    is_running = True
    clock = pygame.time.Clock()
    while is_running:
        schedule.run_pending()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
        screen.fill((0,0,0))
        drawDefault()
        drawDots()
        pygame.display.flip()
        clock.tick(60)
        

if __name__ == "__main__":
    main()
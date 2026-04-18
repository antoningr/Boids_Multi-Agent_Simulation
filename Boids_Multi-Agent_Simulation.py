import pygame
import random
import math

# ============================================================
# CONFIGURATION
# ============================================================

WIDTH, HEIGHT = 1200, 800
FPS = 60

NB_BOIDS = 150

MAX_SPEED = 4.5
MAX_FORCE = 0.09

# Rayons
SEPARATION_RADIUS = 22
ALIGNMENT_RADIUS = 60
COHESION_RADIUS = 110

# Poids comportements
W_SEPARATION = 1.9
W_ALIGNMENT = 1.0
W_COHESION = 0.85

# Affichage
BG = (10, 12, 20)
TRAIL_ALPHA = 25


# ============================================================
# OUTILS VECTEURS
# ============================================================

def limit(v, max_v):
    mag = math.hypot(v[0], v[1])
    if mag > max_v and mag != 0:
        return (v[0] / mag * max_v, v[1] / mag * max_v)
    return v


def normalize(v):
    mag = math.hypot(v[0], v[1])
    if mag == 0:
        return (0, 0)
    return (v[0] / mag, v[1] / mag)


def dist(a, b):
    return math.hypot(a[0] - b[0], a[1] - b[1])


def sub(a, b):
    return (a[0] - b[0], a[1] - b[1])


def add(a, b):
    return (a[0] + b[0], a[1] + b[1])


def mul(v, k):
    return (v[0] * k, v[1] * k)


# ============================================================
# BOID
# ============================================================

class Boid:
    def __init__(self):
        self.pos = (random.uniform(0, WIDTH), random.uniform(0, HEIGHT))

        angle = random.uniform(0, math.pi * 2)
        self.vel = (math.cos(angle) * 2, math.sin(angle) * 2)

        self.acc = (0, 0)

    # --------------------------------------------------------

    def apply(self, force):
        self.acc = add(self.acc, force)

    # --------------------------------------------------------

    def separation(self, boids):
        steer = (0, 0)
        total = 0

        for b in boids:
            if b is self:
                continue

            d = dist(self.pos, b.pos)
            if 0 < d < SEPARATION_RADIUS:
                diff = normalize(sub(self.pos, b.pos))
                diff = mul(diff, 1 / d)
                steer = add(steer, diff)
                total += 1

        if total > 0:
            steer = mul(steer, 1 / total)
            steer = normalize(steer)
            steer = mul(steer, MAX_SPEED)
            steer = sub(steer, self.vel)
            steer = limit(steer, MAX_FORCE)

        return steer

    # --------------------------------------------------------

    def alignment(self, boids):
        avg = (0, 0)
        total = 0

        for b in boids:
            if b is self:
                continue
            if dist(self.pos, b.pos) < ALIGNMENT_RADIUS:
                avg = add(avg, b.vel)
                total += 1

        if total > 0:
            avg = mul(avg, 1 / total)
            avg = normalize(avg)
            avg = mul(avg, MAX_SPEED)

            steer = sub(avg, self.vel)
            return limit(steer, MAX_FORCE)

        return (0, 0)

    # --------------------------------------------------------

    def cohesion(self, boids):
        center = (0, 0)
        total = 0

        for b in boids:
            if b is self:
                continue
            if dist(self.pos, b.pos) < COHESION_RADIUS:
                center = add(center, b.pos)
                total += 1

        if total > 0:
            center = mul(center, 1 / total)

            desired = normalize(sub(center, self.pos))
            desired = mul(desired, MAX_SPEED)

            steer = sub(desired, self.vel)
            return limit(steer, MAX_FORCE)

        return (0, 0)

    # --------------------------------------------------------

    def flock(self, boids):
        s = mul(self.separation(boids), W_SEPARATION)
        a = mul(self.alignment(boids), W_ALIGNMENT)
        c = mul(self.cohesion(boids), W_COHESION)

        self.apply(s)
        self.apply(a)
        self.apply(c)

    # --------------------------------------------------------

    def update(self):
        self.vel = add(self.vel, self.acc)
        self.vel = limit(self.vel, MAX_SPEED)

        self.pos = add(self.pos, self.vel)
        self.acc = (0, 0)

        # rebond murs
        x, y = self.pos
        vx, vy = self.vel

        if x < 0 or x > WIDTH:
            vx *= -1
        if y < 0 or y > HEIGHT:
            vy *= -1

        self.pos = (max(0, min(WIDTH, x)), max(0, min(HEIGHT, y)))
        self.vel = (vx, vy)

    # --------------------------------------------------------

    def draw(self, screen):
        x, y = self.pos
        vx, vy = self.vel

        angle = math.atan2(vy, vx)
        size = 8

        color_intensity = min(255, int(math.hypot(vx, vy) * 60))
        color = (120, 200, 255)

        p1 = (x + math.cos(angle) * size,
              y + math.sin(angle) * size)

        p2 = (x + math.cos(angle + 2.5) * size,
              y + math.sin(angle + 2.5) * size)

        p3 = (x + math.cos(angle - 2.5) * size,
              y + math.sin(angle - 2.5) * size)

        pygame.draw.polygon(screen, color, [p1, p2, p3])


# ============================================================
# MAIN
# ============================================================

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Boids - Simulation multi-agent (Reynolds)")
    clock = pygame.time.Clock()

    flock = [Boid() for _ in range(NB_BOIDS)]

    # surface pour effet de traînée
    trail = pygame.Surface((WIDTH, HEIGHT))
    trail.set_alpha(TRAIL_ALPHA)

    running = True

    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # effet "trace"
        trail.fill(BG)
        screen.blit(trail, (0, 0))

        # update + draw
        for b in flock:
            b.flock(flock)
            b.update()
            b.draw(screen)

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
import pygame
import math
import requests
import time

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ultrasonic Polar Radar")

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Radar settings
MAX_DISTANCE = 200  # Max detectable distance (cm)
RADAR_CENTER = (WIDTH // 2, HEIGHT // 2)
RADAR_RADIUS = min(WIDTH, HEIGHT) // 2 - 20

# ESP8266 server URL
ESP_IP = "192.168.43.7"  # Replace with your ESP's IP
URL = f"http://{ESP_IP}/distance"

def get_distance():
    try:
        response = requests.get(URL, timeout=1)
        if response.status_code == 200:
            return int(response.text)
    except:
        return None
    return None

def draw_radar(distance):
    screen.fill(BLACK)
    
    # Draw concentric circles (distance markers)
    for r in range(50, MAX_DISTANCE + 1, 50):
        radius = int(r * RADAR_RADIUS / MAX_DISTANCE)
        pygame.draw.circle(screen, GREEN, RADAR_CENTER, radius, 1)
        
        # Add distance labels
        font = pygame.font.SysFont('Arial', 16)
        text = font.render(f"{r} cm", True, GREEN)
        text_rect = text.get_rect(center=(RADAR_CENTER[0] + radius + 15, RADAR_CENTER[1]))
        screen.blit(text, text_rect)
    
    # Draw radar angle lines (fixed at 0° since no servo is used)
    for angle in range(0, 360, 45):
        rad = math.radians(angle)
        end_x = RADAR_CENTER[0] + RADAR_RADIUS * math.sin(rad)
        end_y = RADAR_CENTER[1] - RADAR_RADIUS * math.cos(rad)
        pygame.draw.line(screen, GREEN, RADAR_CENTER, (end_x, end_y), 1)
    
    # Draw detection (if object is detected)
    if distance and 0 < distance <= MAX_DISTANCE:
        # Convert distance to polar coordinates
        scaled_radius = int(distance * RADAR_RADIUS / MAX_DISTANCE)
        
        # Draw a red dot at the detected distance (straight ahead)
        detection_x = RADAR_CENTER[0]
        detection_y = RADAR_CENTER[1] - scaled_radius
        pygame.draw.circle(screen, RED, (detection_x, detection_y), 8)
        
        # Draw a line from center to the detected object
        pygame.draw.line(screen, RED, RADAR_CENTER, (detection_x, detection_y), 2)
        
        # Display distance text
        font = pygame.font.SysFont('Arial', 24)
        text = font.render(f"Object: {distance} cm", True, WHITE)
        screen.blit(text, (20, 20))
    
    # Draw radar sweep effect (simulated)
    for angle in range(0, 360, 30):
        rad = math.radians(angle)
        end_x = RADAR_CENTER[0] + RADAR_RADIUS * math.sin(rad)
        end_y = RADAR_CENTER[1] - RADAR_RADIUS * math.cos(rad)
        pygame.draw.line(screen, BLUE, RADAR_CENTER, (end_x, end_y), 1)
    
    # Update display
    pygame.display.flip()

def main():
    clock = pygame.time.Clock()
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        distance = get_distance()
        draw_radar(distance)
        clock.tick(10)  # 10 FPS
    
    pygame.quit()

if __name__ == "__main__":
    main()
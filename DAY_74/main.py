import turtle
import math
import time

# Set up the screen
screen = turtle.Screen()
screen.setup(width=1000, height=800)
screen.bgcolor("black")
screen.title("Beautiful Moving Design with Turtle")

# Create the turtle
pen = turtle.Turtle()
pen.speed(0)  # Maximum speed
pen.hideturtle()  # Hide the turtle cursor

# Color palette for beautiful designs
colors = ["#FF6B9D", "#C44569", "#F8B195", "#F67280", "#355C7D", 
          "#6C5B7B", "#355C7D", "#2A9D8F", "#E9C46A", "#F4A261"]

def draw_spiral_flower():
    """Draw a beautiful spiral flower pattern"""
    pen.penup()
    pen.goto(0, 0)
    pen.pendown()
    
    for i in range(360):
        angle = i * 0.5
        radius = i * 0.5
        x = radius * math.cos(math.radians(angle))
        y = radius * math.sin(math.radians(angle))
        
        pen.pencolor(colors[i % len(colors)])
        pen.pensize(2)
        pen.goto(x, y)
        
    time.sleep(0.5)

def draw_rotating_squares():
    """Draw rotating squares pattern"""
    pen.penup()
    pen.goto(0, -200)
    pen.pendown()
    
    for i in range(8):
        pen.pencolor(colors[i % len(colors)])
        pen.pensize(3)
        
        for j in range(4):
            pen.forward(100)
            pen.right(90)
        
        pen.penup()
        pen.goto(0, -200)
        pen.right(45)
        pen.pendown()

def draw_circular_pattern():
    """Draw beautiful circular concentric pattern"""
    pen.penup()
    pen.goto(0, 0)
    
    for i in range(36):
        radius = 20 + i * 8
        pen.penup()
        pen.goto(0, -radius)
        pen.pendown()
        pen.pencolor(colors[i % len(colors)])
        pen.pensize(2)
        pen.circle(radius)

def draw_star_burst():
    """Draw a stunning star burst pattern"""
    pen.penup()
    pen.goto(0, 0)
    
    for i in range(24):
        pen.pencolor(colors[i % len(colors)])
        pen.pensize(3)
        pen.penup()
        pen.goto(0, 0)
        pen.pendown()
        
        angle = i * (360 / 24)
        pen.setheading(angle)
        
        for j in range(5):
            pen.forward(150)
            pen.backward(150)
            pen.right(36)

def draw_mandala():
    """Draw a beautiful mandala pattern"""
    pen.speed(0)
    pen.penup()
    pen.goto(0, 0)
    
    for i in range(36):
        pen.pencolor(colors[i % len(colors)])
        pen.pensize(2)
        pen.penup()
        pen.goto(0, 0)
        pen.setheading(i * 10)
        pen.pendown()
        
        for j in range(5):
            pen.forward(100)
            pen.backward(100)
            pen.right(72)

def draw_hypnotic_spiral():
    """Draw a hypnotic spinning spiral"""
    pen.penup()
    pen.goto(0, 0)
    
    for i in range(1000):
        angle = i * 2
        radius = i * 0.3
        x = radius * math.cos(math.radians(angle))
        y = radius * math.sin(math.radians(angle))
        
        pen.pencolor(colors[(i // 50) % len(colors)])
        pen.pensize(1)
        pen.penup()
        pen.goto(x, y)
        
        if i > 0:
            pen.pendown()
            pen.dot(3)

def draw_animated_waves():
    """Draw beautiful wave patterns"""
    pen.penup()
    pen.goto(-400, 0)
    pen.pendown()
    
    for wave in range(5):
        pen.pencolor(colors[wave % len(colors)])
        pen.pensize(3)
        
        for x in range(-400, 400, 5):
            y = 50 * math.sin(math.radians(x)) + (wave * 80)
            pen.goto(x, y)
        
        pen.penup()
        pen.goto(-400, 0)
        pen.pendown()

# Main animation loop
def main():
    try:
        while True:
            # Clear screen
            pen.clear()
            
            # Draw different patterns
            print("Drawing Spiral Flower...")
            draw_spiral_flower()
            time.sleep(2)
            
            pen.clear()
            print("Drawing Circular Pattern...")
            draw_circular_pattern()
            time.sleep(2)
            
            pen.clear()
            print("Drawing Star Burst...")
            draw_star_burst()
            time.sleep(2)
            
            pen.clear()
            print("Drawing Rotating Squares...")
            draw_rotating_squares()
            time.sleep(2)
            
            pen.clear()
            print("Drawing Mandala...")
            draw_mandala()
            time.sleep(2)
            
            pen.clear()
            print("Drawing Hypnotic Spiral...")
            draw_hypnotic_spiral()
            time.sleep(2)
            
            pen.clear()
            print("Drawing Animated Waves...")
            draw_animated_waves()
            time.sleep(2)
            
    except KeyboardInterrupt:
        print("Animation stopped!")
        screen.close()

# Run the program
if __name__ == "__main__":
    main()
    turtle.done()
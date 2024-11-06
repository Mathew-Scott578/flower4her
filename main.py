import turtle
import math

def setup_turtle():
    t = turtle.Turtle()
    t.speed(0)  # Fastest speed
    t.hideturtle()
    return t

def draw_petal_vein(t, size, angle):
    original_pos = t.pos()
    original_heading = t.heading()
    
    t.pensize(1)
    t.color("#FFD1DC")  # Light pink for veins
    t.setheading(original_heading + angle)
    
    # Draw curved vein
    t.pendown()
    t.circle(size * 2, 30)
    
    # Return to original position
    t.penup()
    t.goto(original_pos)
    t.setheading(original_heading)

def draw_detailed_petal(t, size):
    t.pendown()
    t.begin_fill()
    
    # Create more natural petal shape with curves
    t.circle(size * 1.2, 60)
    t.left(30)
    t.circle(size * 1.5, 30)
    t.left(10)
    t.circle(size, 40)
    
    # Create pointed tip
    t.left(140)
    t.circle(-size * 0.5, 40)
    t.circle(-size * 0.8, 30)
    
    # Complete other side of petal
    t.left(10)
    t.circle(-size, 40)
    t.circle(-size * 1.5, 30)
    t.left(30)
    t.circle(-size * 1.2, 60)
    
    t.end_fill()
    
    # Add petal details
    current_pos = t.pos()
    current_heading = t.heading()
    
    # Draw veins
    t.penup()
    t.goto(current_pos)
    t.setheading(current_heading)
    
    # Central vein
    t.pensize(1)
    t.color("#FFD1DC")
    t.forward(size * 0.2)
    t.pendown()
    t.forward(size * 1.5)
    
    # Side veins
    for angle in [-30, -15, 15, 30]:
        t.penup()
        t.goto(current_pos)
        t.setheading(current_heading)
        t.forward(size * 0.5)
        draw_petal_vein(t, size * 0.5, angle)
    
    # Add subtle shading
    t.penup()
    t.goto(current_pos)
    t.setheading(current_heading)

def draw_stamen(t, length):
    original_pos = t.pos()
    original_heading = t.heading()
    
    # Draw filament with gradient effect
    t.pensize(2)
    for i in range(length):
        shade = 255 - int(i * 2)
        t.color(f"#{shade:02x}D700")  # Gradient from yellow to darker yellow
        t.pendown()
        t.forward(1)
    
    # Draw detailed anther
    t.pensize(4)
    t.color("#FFD700")
    t.dot(8)
    
    # Add pollen details
    t.pensize(1)
    t.color("#FFA500")  # Orange pollen
    for _ in range(6):
        t.right(60)
        t.forward(4)
        t.dot(3)
        t.backward(4)
    
    # Return to original position
    t.penup()
    t.goto(original_pos)
    t.setheading(original_heading)

def draw_textured_leaf(t, size):
    t.color("forest green")
    t.begin_fill()
    
    # Create more natural leaf shape
    t.circle(size, 60)
    t.left(120)
    t.circle(size, 60)
    t.end_fill()
    
    # Add leaf veining
    start_pos = t.pos()
    start_heading = t.heading()
    
    # Main vein
    t.color("dark green")
    t.pensize(1)
    t.pendown()
    t.forward(size * 1.5)
    
    # Side veins
    for i in range(5):
        t.penup()
        t.goto(start_pos)
        t.setheading(start_heading)
        t.forward(size * 0.3 * i)
        t.pendown()
        t.left(45)
        t.forward(size * 0.5)
        t.penup()
        t.goto(start_pos)
        t.setheading(start_heading)
        t.forward(size * 0.3 * i)
        t.pendown()
        t.right(45)
        t.forward(size * 0.5)

def write_message(t):
    # Save current position and settings
    original_pos = t.pos()
    original_heading = t.heading()
    
    # Position text further below the flower
    t.penup()
    t.goto(0, -300)
    
    # Add decorative line above text
    t.color("#FF69B4")
    t.pensize(2)
    t.goto(-200, -280)
    t.pendown()
    t.goto(200, -280)
    
    # Configure enhanced text style
    t.penup()
    t.goto(0, -320)
    style = ("Times New Roman", 16, "italic bold")
    
    # Write main text with enhanced formatting
    t.color("#FF1493")
    t.write("Until the flower of our love has blossomed,", 
            align="center", font=style)
    
    # Second line
    t.goto(0, -350)
    t.color("#FF69B4")
    t.write("my heart won't be at peace meri ayushi", 
            align="center", font=style)
    
    # Signature
    # t.goto(0, -380)
    # style_signature = ("Courier", 14, "italic")
    # t.color("#FF69B4")
    # t.write("~ ayushi", align="center", font=style_signature)
    
    # Add decorative line below text
    t.color("#FF69B4")
    t.pensize(2)
    t.goto(-200, -400)
    t.pendown()
    t.goto(200, -400)
    
    # Restore original position and settings
    t.penup()
    t.goto(original_pos)
    t.setheading(original_heading)

def draw_lily():
    screen = turtle.Screen()
    screen.bgcolor("white")
    t = setup_turtle()
    
    # Adjust screen size to accommodate lower text
    screen.setup(800, 900)
    
    # Draw stem with gradient
    t.penup()
    t.goto(0, -200)
    t.setheading(90)
    
    # Gradient stem
    for i in range(200):
        shade = 100 + int(i * 0.3)
        t.color(f"#{0:02x}{shade:02x}{0:02x}")
        t.pensize(4 - i/80)
        t.pendown()
        t.forward(1)
    
    # Draw detailed leaves
    positions = [(-20, -100), (20, -150), (-30, -50), (25, -75)]
    angles = [40, 160, 45, 155]
    sizes = [40, 35, 30, 45]
    for pos, angle, size in zip(positions, angles, sizes):
        t.penup()
        t.goto(pos)
        t.setheading(angle)
        draw_textured_leaf(t, size)
    
    # Draw petals with gradient colors
    t.penup()
    t.goto(0, 0)
    petal_colors = ["#FFE4E1", "#FFF0F5", "#FFE4E1", "#FFDAB9", "#FFF0F5", "#FFE4E1"]
    
    # Outer petals
    for i in range(6):
        t.penup()
        t.goto(0, 0)
        t.setheading(i * 60)
        t.color(petal_colors[i])
        t.pensize(1)
        draw_detailed_petal(t, 50)
    
    # Inner petals
    for i in range(6):
        t.penup()
        t.goto(0, 0)
        t.setheading(30 + i * 60)
        t.color(petal_colors[(i + 1) % len(petal_colors)])
        draw_detailed_petal(t, 40)
    
    # Draw detailed stamens
    for i in range(6):
        t.penup()
        t.goto(0, 0)
        t.setheading(i * 60)
        draw_stamen(t, 30)
    
    # Add the enhanced romantic message
    write_message(t)
    
    screen.exitonclick()

if __name__ == "__main__":
    draw_lily()

from p5 import * 
# pip install skia-python
# pip install git+https://github.com/p5py/p5.git#egg=p5
from random import randint 

# Setup global variables
screen_size = 400
rocket_y = screen_size  # Start at the bottom
burn = 100  # How much fuel is burned in each frame
orbit_radius = 250
orbit_y = screen_size - orbit_radius

# The draw_rocket function goes here
def draw_rocket():
    global rocket_y, fuel, burn  # Use the global rocket_y variable

    if fuel >= burn and rocket_y > orbit_y:  # Still flying
        rocket_y -= 1
        fuel -= burn
        print('Fuel left: ', fuel)

        no_stroke()  # Turn off the stroke
    
        for i in range(25):
            fill(255, 255 - i*10, 0)
            ellipse(width/2, rocket_y + i, 8, 3)
    
        fill(200, 200, 200, 100)
        for i in range(20):
            ellipse(width/2 + randint(-5, 5), rocket_y + randint(20, 50), randint(5, 10), randint(5, 10))

    if fuel < burn and rocket_y > orbit_y:  # No more fuel and not in orbit
        tint(255, 0, 0)  # Failure (RED)
    elif fuel < 1000 and rocket_y <= orbit_y:
        tint(0, 255, 0)  # Success (GREEN)  
    elif fuel >= 1000 and rocket_y <= orbit_y:
        tint(255, 200, 0)  # Too much fuel (YELLOW)

    image(rocket, width/2, rocket_y, 64, 64)
    
    no_tint()  # So the planet isn't tinted red in the next frame!

    no_stroke()  # Turn off the stroke

    for i in range(25):  # Draw 25 burning exhaust ellipses
        fill(255, 255 - i * 10, 0)  # Reduce the amount of green
        #fill(255, 255, 0)  # Yellow
        ellipse(width/2, rocket_y + i, 8, 3)  # i increases each time the loop repeats

    fill(200, 200, 200, 100)  # Transparent grey
    for i in range(20):  # Draw 20 random smoke ellipses
        ellipse(width/2 + randint(-5, 5), rocket_y + randint(20, 50), randint(5, 10), randint(5, 10))

# The draw_background function goes here
def draw_background():
    background(0)  # Short for background(0, 0, 0) — black
    image(planet, width/2, height, 300, 300)  # Draw the image

    no_fill()  # Turn off any fill
    stroke(255)  # Set a white stroke
    stroke_weight(2)
    ellipse(width/2, height, orbit_radius * 2, orbit_radius * 2)

# The setup function goes here
def setup():
    # Setup your animation here
    size(screen_size, screen_size)
    image_mode(CENTER)  # Positions the image in the center
    global planet, rocket
    planet = load_image('planet.png')  # Your chosen planet  
    rocket = load_image('rocket.png')

# The draw function goes here
def draw():
    # Things to do in every frame
    draw_background()
    draw_rocket()

# Ask for an user input
fuel = int(input('How many kilograms of fuel do you want to use?'))

# Run the Sketch
run()

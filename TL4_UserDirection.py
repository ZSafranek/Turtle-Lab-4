import turtle

def move(direction, distance):
    if direction == "up":
        turtle.setheading(90)
    elif direction == "down":
        turtle.setheading(270)
    elif direction == "left":
        turtle.setheading(180)
    elif direction == "right":
        turtle.setheading(0)
    turtle.forward(distance)

def path(directions):
    for direction, distance in directions:
        move(direction, distance)

def main():
    directions = []
    while True:
        direction = input("Enter a direction (up, down, left, right or 'stop' to end)").lower()
        if direction == "stop":
            break
        distance = int(input("Enter the distance: "))
        directions.append((direction, distance))

    path(directions)
    turtle.exitonclick()

main()
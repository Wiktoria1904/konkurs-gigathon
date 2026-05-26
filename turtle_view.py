import turtle
import constants

class TurtleView:
    """Odpowiada za wizualizację świata i łazika przy użyciu modułu turtle."""

    def __init__(self):
        self.screen = turtle.Screen()
        self.rover_turtle = turtle.Turtle()
        self.bounds_turtle = turtle.Turtle()

    def setup_world(self, width, height):
        """Konfiguruje okno i rysuje granice świata."""
        self.screen.clear()
        self.screen.setup(width + constants.MARGIN * 2, height + constants.MARGIN * 2)
        self.screen.title("Symulator Łazika")
        self.screen.tracer(0)

        # Rysowanie granic
        self.bounds_turtle.hideturtle()
        self.bounds_turtle.penup()
        self.bounds_turtle.color(constants.COLOR_BOUNDS)
        self.bounds_turtle.pensize(constants.PEN_SIZE)

        hw, hh = width / 2, height / 2
        self.bounds_turtle.goto(-hw, -hh)
        self.bounds_turtle.pendown()
        for _ in range(2):
            self.bounds_turtle.forward(width)
            self.bounds_turtle.left(90)
            self.bounds_turtle.forward(height)
            self.bounds_turtle.left(90)
        self.bounds_turtle.penup()

        # Inicjalizacja łazika
        self.rover_turtle.shape("triangle")
        self.rover_turtle.color(constants.COLOR_VEHICLE)
        self.rover_turtle.speed(constants.TURTLE_SPEED)
        self.screen.update()

    def set_initial_position(self, position, angle):
        """Ustawia łazik w pozycji startowej."""
        self.rover_turtle.penup()
        self.rover_turtle.goto(position.x, position.y)
        self.rover_turtle.setheading(angle)
        self.rover_turtle.pendown()
        self.screen.update()

    def update_rover(self, position, angle):
        """Aktualizuje pozycję łazika na ekranie."""
        self.rover_turtle.goto(position.x, position.y)
        self.rover_turtle.setheading(angle)
        self.screen.update()

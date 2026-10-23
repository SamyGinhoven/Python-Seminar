"""Edit only the commands inside main(). Run run_world.py to see Karel move."""

from stanfordkarel import *  # noqa: F403


def turn_right():
    """Turn 90 degrees clockwise using Karel's built-in command."""
    turn_left()
    turn_left()
    turn_left()


def main():
    # Replace this starter move with your route to the green square.
    move()

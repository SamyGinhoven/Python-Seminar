# Challenge 1: Karel Finds Home

Guide Karel from the bottom left corner to the **green square** after picking up all **beepers**. You only need to edit `student.py`, and then run `run_world.py` which opens the world and runs your code.

## Start

1. Open `student.py`. Change only the commands inside `main()`.
2. From this folder, run `python run_world.py`.
3. In the Karel window, click **Run Program**. Change your code, then click **Reset World** and **Run Program** again.

If you use an editor with a Run button, run `run_world.py`, not `student.py`. Keep all files and folders together after extracting the ZIP.

## Your task

Karel starts at the bottom left, facing east. A wall blocks the direct route. Find a path to the green square without walking through a wall or off the edge. But wait, Karel first needs to pick up the beeper before reaching home on the green square. You should only use the following commands:

- `move()` — move one square forward.
- `turn_left()` — rotate 90 degrees to the left.
- `pick_beeper()` — pick up a beeper from the square where Karel is standing. 

Write one command per line inside `main()`. The window reports success only when Karel finishes on the green square.

Change the name of your program from `student.py` to `01_solution_[your name].py` **before your submit it**. Here replace `[your_name]` with your own name where you replace all spaces by `_`. For example my name is Sam van Ginhoven, so my file name is `01_solution_Sam_van_Ginhoven.py`.

## Example input and output

The starter `student.py` contains:

```python
def main():
    move()
    turn_left()
```

After clicking **Run Program**, Karel moves one square to the right and then turns left, so Karel is facing north. The status line says:

```text
Keep going: Karel has not reached the green square.
```

## Learning objectives

- Call Python functions.
- Plan a route as a sequence of commands.
- Use the Karel window to debug each move.
- Understand that a program's final position can be checked.

## Hints

1. You can make a drawing on which steps Karel needs to take.
2. To turn right, you can also turn left three times.
# Challenge 1: Karel Finds Home

Guide Karel from the bottom left corner to the **green square**. You only need to edit `student.py`; `run_world.py` opens the world and runs your code.

## Start

### In GitHub Codespaces

1. Follow the [browser setup in the project README](../README.md). No local installation is needed.
2. Open `student.py` and change only the commands inside `main()`.
3. Open the **Karel window** preview and click **Run Program**. Change your code, then click **Reset World** and **Run Program** again.

### On your own computer (optional)

1. Make sure Python 3 and `tkinter` are available. The `stanfordkarel` library is already included in this folder, so no `pip install` is needed.
2. Open `student.py`. Change only the commands inside `main()`.
3. From this folder, run `python run_world.py` (or `python3 run_world.py` on systems where Python uses that name).
4. In the Karel window, click **Run Program**. Change your code, then click **Reset World** and **Run Program** again.

If you use an editor with a Run button, run `run_world.py`, not `student.py`. Keep all files and folders together after extracting the ZIP.

## Your task

Karel starts at the bottom left, facing east. A wall blocks the direct route. Find a path to the green square without walking through a wall or off the edge. Begin with these commands:

- `move()` — move one square forward.
- `turn_left()` — rotate 90 degrees to the left.
- `turn_right()` — rotate 90 degrees to the right. This helper is already written for you in `student.py`.
- `pick_beeper()` — pick up a beeper from the square where Karel is standing. You need this only in worlds that contain beepers.

Write one command per line inside `main()`. The window reports success when Karel finishes on the green square. If the world contains beepers at the start, Karel must collect them before finishing there.

## Example input and output

The starter `student.py` contains:

```python
def main():
    move()
```

After clicking **Run Program**, Karel moves one square to the right. The status line says:

```text
Keep going: Karel has not reached the green square.
```

## Learning objectives

- Call Python functions with parentheses.
- Plan a route as a sequence of commands.
- Use the Karel window to debug each move.
- Understand that a program's final position and the remaining beepers can be checked.

## Hints

1. Make one move east before turning north.
2. Move north until you are above the wall.
3. Use `turn_right()` to travel east again.
4. The green square is one row above the long eastbound route.

## Bonus challenges

1. Define a `turn_around()` helper using two left turns, then use it in a new route.
2. Use a `for` loop to replace repeated `move()` calls.
3. Try a different valid route and compare how many commands it takes.
4. Edit a copy of `worlds/find_home.w` to add a wall, then solve the new world.
5. Add a beeper with `Beeper: (3, 1); 1`. Plan a route through that square and call `pick_beeper()` before reaching the green square.

## If your world has a beeper

A beeper drawn in the world is part of the challenge, not just decoration. Stand on its square and call `pick_beeper()`. Reaching the green square while leaving a starting beeper behind gives this message:

```text
Keep going: collect the beeper before reaching home.
```

The runner checks every beeper that was present when the world loaded. If you add more than one, collect all of them before finishing. Press **Reset World** to return Karel and the beepers to their starting positions between attempts.

## For teachers

The full teacher project includes `solution.py` with a reference route. Run `python run_world.py --solution` there to show it. The student ZIP omits that file. The project includes the source of [StanfordKarel](https://github.com/TylerYep/stanfordkarel) under its MIT license; see `STANFORDKAREL-LICENSE`. The [Karel Reader](https://compedu.stanford.edu/karel-reader/docs/python/en/chapter2.html) explains the robot commands. Both links are optional reading. The local version runs without a website or webserver.

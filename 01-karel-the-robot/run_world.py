"""Launch the local Karel window using student.py"""

import sys
import tkinter as tk
from pathlib import Path

from stanfordkarel.karel_application import KarelApplication
from stanfordkarel.karel_program import KarelProgram


HERE = Path(__file__).resolve().parent
GOAL = (6, 4)


class ChallengeApplication(KarelApplication):
    def run_program(self):
        super().run_program()
        if self.status_label.cget("text") != "Finished running.":
            return
        required_beepers = {
            location for location, count in self.world.init_beepers.items() if count > 0
        }
        if (self.karel.avenue, self.karel.street) != GOAL:
            self.status_label.configure(text="Keep going: Karel has not reached the green square.", fg="dark orange")
        elif any(self.world.beepers.get(location, 0) > 0 for location in required_beepers):
            self.status_label.configure(text="Keep going: collect the beeper before reaching home.", fg="dark orange")
        else:
            message = "Success! Karel reached the green square."
            if required_beepers:
                message = "Success! Karel reached the green square and collected the beeper."
            self.status_label.configure(text=message, fg="green")

if __name__ == "__main__":
    code = HERE / "student.py"
    world = HERE / "worlds" / "find_home.w"
    root = tk.Tk()
    app = ChallengeApplication(KarelProgram(str(world)), code, master=root)
    app.mainloop()

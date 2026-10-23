# Included StanfordKarel source

This folder includes the `stanfordkarel/` Python package from
[TylerYep/stanfordkarel](https://github.com/TylerYep/stanfordkarel), commit
`3eaf0b3e1d8e03df3791a307f913c4002aa84a5f`.

The package is distributed under the MIT license in `STANFORDKAREL-LICENSE`.
One local fix in `stanfordkarel/karel_world.py` preserves the original corner
colors when the world is reset; upstream currently clears all corner colors.
`run_world.py`, `student.py`, `solution.py`, and `worlds/find_home.w` were
created for this seminar.

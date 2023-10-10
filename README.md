# dnd-roller-tutorial
Simple python app to roll dice for D&amp;D (Dungeons&amp;Dragons), from US RSE tutorial

See https://hackmd.io/@conda-us-rse-2023/tutorial.

The `dnd_roller_tutorial` provides three main functions: `roll`, `dice_roll`, and `sequence_rolls` to generate a single die roll, multiple rolls of the same die, or multiple rolls of multiple dice.

The former (i.e. `roll()`) could generate a simple output in the terminal, whilst the latter (i.e. `sequence_rolls()`) generate a tabular report for the outcome of each roll in the sequence.

Please have a look at the examples below for additional details.

### Examples

Rolling a single game die:

```python
>>> from dnd_roller_tutorial import roll
>>> roll(d=4)
4
>>> roll(d=20, verbose=true)
You rolled  17
17
```
Rolling multiple times the same game die:

```python 

>>> from dnd_roller_tutorial import dice_roll
>>> dice_roll(throws=3, sides=4)
[3, 2, 4]
```

Rolling a sequence of dice rolls:

```python
>>> from dnd_roller_tutorial import sequence_rolls
>>> sequence_rolls(sequence="12d20, 4d4, 2d10, 1d100", verbose=True)

╒════════╤════════════════════════════════════════════════╤═══════╕
│ dice   │ rolls                                          │   sum │
╞════════╪════════════════════════════════════════════════╪═══════╡
│ 12d20  │ [15, 9, 13, 2, 14, 13, 18, 15, 13, 10, 17, 18] │   157 │
├────────┼────────────────────────────────────────────────┼───────┤
│ 4d4    │ [2, 3, 2, 1]                                   │     8 │
├────────┼────────────────────────────────────────────────┼───────┤
│ 2d10   │ [8, 5]                                         │    13 │
├────────┼────────────────────────────────────────────────┼───────┤
│ 1d100  │ [50]                                           │    50 │
╘════════╧════════════════════════════════════════════════╧═══════╛
{'12d20': [15, 9, 13, 2, 14, 13, 18, 15, 13, 10, 17, 18],
 '4d4': [2, 3, 2, 1],
 '2d10': [8, 5],
 '1d100': [50]}
```

# NAND 2 TETRIS 

## PROJECT 6 - ASSEMBLER

I really enjoyed the Nand 2 Tetris course: https://www.nand2tetris.org/ 

It's a free (well the first half that I did is free) course that really helps you understand computer architecture at a fundamental level. It starts you at basic logic and you build your way up from there. The full course takes you all the way through building a Tetris emulator. It is a very well done course and I highly recommend it. 

I wanted to share my work from Project 6 - building an Assembler. I chose to write it in the language I'm most familiar with, python. It translates programs written in the Hack assembly language into binary Hack code. 

## USAGE

Call the main function and provide a path to a .asm file, like so:

```python
python3 assembler/main.py add/Add.asm
```

This will create a file with .hack extension alongside the .asm file. 

Optionally, you can provide the debug flag (as either --debug or --d) to see the timing of each step: 

```python
python3 assembler/main.py add/Add.asm --debug
```

And in addition to producing the output file, it will print something like:

```
Converting add/Add.asm
Parsed file in 0.00018 secs
First pass in 0.00004 secs
Second pass in 0.00009 secs
Wrote add/Add.hack
Ran in 0.00065 secs
```

## REQUIREMENTS

There are no 3rd party libraries involved in this project - everything is in the python standard library!

## TODO

add unit tests?



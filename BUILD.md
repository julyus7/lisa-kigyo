# Building the native Lisa game

The release used **Lisa Pascal V3.26 (10-Jul-84)**, **MC68000 Code Generator
V3.16**, and **M68000 Object Code Linker 3.0**, in Workshop 3 running in LisaEm.
Python prepares files; the Pascal compiler runs on the emulated Lisa.

## Requirements

- Real Apple Lisa 2 (2/5 or 2/10), or LisaEm, your own ROM, Workshop 3 and LOS 3 environment.
- LOS interface objects referenced by the source, plus `IOSPASLIB.OBJ`,
  `SYS1LIB.OBJ` and `PRLIB.OBJ`.
- Python 3.10+ for the included tools, using the standard library only.

ROMs, OS images, SDK libraries and prepared developer disks are not included.
Use a separate copy of your development disk.

## Compile

Transfer `src/G.TEXT`, `J.TEXT`, `D.TEXT`, `I.TEXT`, `M.TEXT` as Lisa TEXT files.
These files retain classic CR line endings. The receiver and serial transfer
utility in [LOS Minesweeper](https://github.com/alexthecat123/los_minesweeper)
provide one transfer method. Set your Workshop prefix to the source folder
and make the LOS interface objects available.

Compile G, J, D, I, then M: press P, enter each source name, and accept the
default listing and .OBJ output. The release reused the four verified support
objects and freshly compiled M. The code generator reported **5282 machine-code
bytes** and 11.591 seconds.

Press L and enter these inputs, one per prompt:

```text
M.OBJ
G.OBJ
J.OBJ
D.OBJ
I.OBJ
IOSPASLIB.OBJ
SYS1LIB.OBJ
PRLIB.OBJ
```

End the inputs with Return, accept the default listing and enter **K.OBJ** as
output. Require zero errors and an executable program file. The released
K.OBJ is 8192 bytes. `src/C.TEXT` and `src/L.TEXT` contain Workshop EXEC answers.

Quit Workshop with Q, confirm with Y, then use P (Power_off) in the resulting
text menu. Wait for the Lisa to shut down before reading the developer disk.

## Package

The packager replaces the executable in the released floppy template while
preserving tool ID 243, icons, phrase resources and native Sony sector tags:

```sh
python tools/package.py /path/to/closed-workshop.dc42 Kigyo-new.dc42
python tools/inspect_image.py Kigyo-new.dc42
```

The replacement must fit the existing allocation. This utility does not
allocate a larger file or change resource files.

Optional source regeneration and host rule checks:

```sh
python tools/generate_source.py
python tests/test_rules.py
```

The generator uses the included Raktaros shell template. The checked-in
src/M.TEXT is the exact source used for the release. LisaEm ran locally in an
Alpine Linux VM under Windows QEMU; that particular VM is not required.

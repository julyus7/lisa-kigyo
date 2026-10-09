# Kigyo (Snake) for Apple Lisa

Hungarian Snake for Lisa Office System 3, running in a window.
Collect food, grow the snake and avoid your own body. Includes three speeds,
solid or wrapping edges, and automatic pause when switching to another window.
Hungarian captions use unaccented characters for the Lisa font.

![Native LOS gameplay](screenshots/gameplay.png)

## Download and run

Download **[Kigyo.dc42](https://github.com/julyus7/lisa-kigyo/releases/latest/download/Kigyo.dc42)**
from Releases, or [dist/Kigyo.dc42](dist/Kigyo.dc42) using Download raw.
This is a tagged 400 KB Lisa floppy in Disk Copy 4.2 format, **419284 bytes**.
It is an application floppy; boot your own LOS installation first.

1. Boot Lisa Office System 3 in LisaEm.
2. Insert `Kigyo.dc42`, open its disk and the Kigyo tool icon.
3. Press Space to start.
4. To install on a hard disk, select LOS **Duplicate** and drag the duplicate
   into your Games folder. Allow LOS to shut down the running tool if requested.
   Keep the floppy inserted until copying finishes.

The game has its own snake icon, **tool ID 243**, and volume identity ending D604.
It was installed alongside eight existing games without altering their files.
LOS allows only one copy of the same tool per disk; replace an earlier Kigyo
version when updating.

## Controls

| Key | Action |
| --- | --- |
| W / A / S / D | Up / left / down / right |
| Space | Start, pause, resume |
| N | New game, preserving speed and edge mode |
| 1 / 2 / 3 | Slow / medium / fast |
| F | Toggle solid / wrapping edges; restart paused |

The game starts paused. Reverse turns and two direction changes before one
movement tick are rejected. Food gives 10 points and adds one body segment.
Filling the 20 by 14 board wins. Returning from another window leaves it paused;
press Space to resume.

## Source and validation

- [src/M.TEXT](src/M.TEXT): exact released Lisa Pascal source.
- `src/G.TEXT`, `J.TEXT`, `D.TEXT`, `I.TEXT`: supporting LOS units.
- [BUILD.md](BUILD.md): native compilation and packaging instructions.
- [VALIDATION.md](VALIDATION.md): completed checks and their scope.
- [README-HU.md](README-HU.md): magyar leírás és kezelés.
- [CREDITS.md](CREDITS.md): inherited framework and source provenance.

Release checks: 10 host rule checks, 10 native LOS checks, 16 rendering samples,
focus pause, native hard-disk installation and launch after ejecting the floppy.
The installed launch used the same emulator session, not a cold reboot.

Image SHA-256: `618ffb171bcbf230cd0c8fb5e27a10c40edc4405779d6404cfe7ce64b92ad510`.

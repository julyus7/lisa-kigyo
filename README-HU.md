# Kígyó (Snake) – Apple Lisa 2

**Natív játék valódi Apple Lisa 2 számítógéphez (Lisa 2/5 és Lisa 2/10),
Lisa Office System 3 alatt.** Ugyanez a kiadás LisaEm-ben is használható.

## Indítás valódi Lisa 2 gépen

1. Indítsd el a Lisa Office System 3 rendszert a Lisa 2 gépen.
2. A `Kigyo.dc42` lemezképet írd ki Lisa-formátumú, 400 KB-os, 3,5 hüvelykes
   floppyra megfelelő lemezképíró programmal és meghajtóval. A DC42-ben lévő
   natív Lisa szektorcímkéket is meg kell őrizni. Lisa-lemezképeket támogató
   floppyhelyettesítő is használható.
3. Helyezd be a lemezt, nyisd meg a lemez ablakát, jelöld ki a játék ikonját,
   és válaszd a File/Print → Open műveletet.
4. Merevlemezre telepítéshez használd a LOS Duplikálás műveletét, majd húzd a
   másolatot a Games mappába. A másolás végéig maradjon bent a floppy.

A DC42 fájl teljes lemezkép; lemezképként kell kiírni, a fájl egyszerű
floppyra másolása nem készít Lisa-játéklemezt. LisaEm-ben közvetlenül
behelyezhető a letöltött DC42.

Az eddigi kiadási tesztek LisaEm-ben történtek; fizikai Lisa 2 gépen végzett
próba még nincs dokumentálva. Részletek: [VALIDATION.md](VALIDATION.md).

Magyar, ablakban futó játék Lisa Office System 3 rendszerhez.
Gyűjtsd az ételt: minden falat 10 pontot ér, és egy mezővel hosszabbítja
a kígyót. A saját testeddel történő ütközés véget vet a játéknak.
Ha az egész pályát betöltöd, nyertél.

## Kezelés

- W/A/S/D: fel/balra/le/jobbra. Visszafordulni nem lehet.
- Szóköz: indítás, szünet és folytatás.
- N: új játék, a választott sebesség és pályaszél megtartásával.
- 1/2/3: lassú/közepes/gyors sebesség.
- F: váltás falas és átjárható pályaszél között; új játék indul szünetben.

A játék először szünetben indul. Másik ablakra váltáskor automatikusan
megáll; visszatérve szóközzel folytatható. A képernyőn lévő magyar
feliratok a Lisa betűkészlete miatt ékezet nélküliek.

## Lemezkép és forrás

A kiadási fájl neve `Kigyo.dc42`. A valódi Lisa 2 gépeden vagy LisaEm-ben a LOS 3
indítása után helyezd be a floppyt, és nyisd meg a Kigyo ikont.
Merevlemezre telepítéshez használd a LOS Duplikálás műveletét, majd húzd
a másolatot a Games mappába. A másolás végéig maradjon bent a floppy.

Saját eszközazonosító: **243**. Saját lemez-UID vége: **D604**.
A játék saját kígyóikonja különbözik a többi alkalmazásétól.

A teljes fő forrás: `src/M.TEXT`. A LOS-keret egységei: `G.TEXT`,
`J.TEXT`, `D.TEXT`, `I.TEXT`. Újrafordítás: `BUILD.md`.
A végleges teszteredményeket a validációs JSON állományok rögzítik.

A LOS-keret eredete Alex LOS Minesweeper projektje:
https://github.com/alexthecat123/los_minesweeper . A játéklogika és ikon
ennek a projektnek az új fejlesztése. A korábbi játékokhoz hasonlóan
ROM, operációs rendszer és fejlesztői SDK nem része a játékfloppynak.

Letöltés: https://github.com/julyus7/lisa-kigyo/releases/latest .

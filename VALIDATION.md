# Kígyó – tesztelési jegyzőkönyv

## Hardware target and test scope

The program is a native Motorola 68000 application for Apple Lisa 2 hardware
(Lisa 2/5 and Lisa 2/10) running Lisa Office System 3. The released tagged
DC42 image can be written to a native Lisa floppy for use on those machines.
The checks below were performed in LisaEm. No physical Lisa 2 hardware test
is recorded in this release; emulator results are not a physical-hardware
test result.


A játékot ezen a gépen futó helyi Linux virtuális gépben, valódi Lisa
Pascal 3.26 és MC68000 Code Generator 3.16 segítségével fordítottam.
A Linker 3.0 nyolc bemeneti állományból, nulla hibával készítette el a
K.OBJ futtatható programot. A fordító által készített gépi kód 5282 bájt.
Bizonyíték: screenshots/native-compiler.png és screenshots/native-linker.png.

## Elvégzett ellenőrzések

- 10 szabályteszt: növekedés, pontozás, fordulás, falak, átjárható szélek,
  saját test, felszabaduló farokmező és megtelt pálya.
- 10 natív LisaEm-próba LOS 3 alatt: indítás, szünet, billentyűk,
  önálló mozgás, ütközés, új játék és mindhárom sebesség.
- 16 mintavételezett képkockán a keret, cím és utasítások változatlanok,
  miközben a kígyó mind a 16 mintán eltérő helyzetben látható.
  Ez képkockák vizsgálata, nem folyamatos videóelemzés.
- Másik ablakra váltás automatikusan megállítja a játékot; visszatéréskor
  szünetben marad.
- DC42 adat- és címkeellenőrző összegek, mind a 800 Sony szektorcímke,
  a lemez egyedi azonosítója és a 243-as alkalmazásazonosító ellenőrizve.
- A floppy futtatható állománya bájtonként megegyezik a fordító által
  készített K.OBJ állománnyal; a lefordított forrás egyezik az M.TEXT-tel.

A részletes eredmények: host-validation.json, native-validation.json,
render-validation.json, focus-validation.json és floppy-validation.json.
A natív bemeneteket a LisaEm COPS billentyűzet- és egérkezelésén keresztül
küldtem; a teszt a játék memóriáját kizárólag olvasta.

Kiadási lemezkép: Kigyo.dc42, 419284 bájt.
SHA-256: 618ffb171bcbf230cd0c8fb5e27a10c40edc4405779d6404cfe7ce64b92ad510.

## Natív merevlemezre másolás

A LOS fájlkezelő Duplikálás műveletével másoltam a játékot egy külön
Games tesztlemezre. A másoláskor a LOS rendesen leállította a Kígyó
alkalmazást. A tesztlemezen mind a 18 korábbi alkalmazás és az új,
243-as játék megtalálható; 72 program-, nyelvi és ikonállomány
bájtonkénti összehasonlítása sikeres, a nyolc korábbi játék változatlan.
A részletes ellenőrzés: installed-validation.json.
A meglévő backup LOS3 Games lemezt ez a próba nem módosította.

A floppy LOS-ból történő kivétele után a Games mappából újranyitottam
a Kígyót. A teljes pálya és az összes magyar kezelési felirat megjelent:
screenshots/gameplay.png. A másolás előtti alkalmazást a LOS leállította.

A merevlemezes indítás ugyanabban az emulátormenetben történt; hideg újraindítás nem volt része ennek a próbának. A LOS szabályos leállítása után megismételt állományellenőrzés is sikeres. A jelentések a validation/ mappában vannak.

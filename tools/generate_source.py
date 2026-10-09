"""Create Hungarian native Lisa Snake using the tested Raktaros LOS shell."""
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parent
source = (ROOT/'templates/RaktarosM.TEXT').read_text().replace('program Raktaros;', 'program Kigyo;')
start = source.index('   sgWidth =')
end = source.index('   nextClkPoll :')
source = source[:start]+'''   snWidth = 20;
   snHeight = 14;
   snCells = 280;
   snLeft = 16;
   snTop = 40;
   snCellW = 14;
   snCellH = 12;
type BOVideoPtr = ^integer;
var
   snBody, snOcc, snShown : array[1..snCells] of integer;
   snHead, snTail, snLen, snPos, snFood, snScore : integer;
   snDir, snNextD, snSpeed, snSeed, snSteps : integer;
   snNext : longint;
   snReady, snPaint, snHud, snPause, snDone, snWon,
   snWalls, snTurn : boolean;
''' + source[end:]
start = source.index('function SGInside')
end = source.index('procedure doUpdateEvent', start)
body = '''function SNDelay : integer;
begin
   case snSpeed of
      1: SNDelay := 25;
      2: SNDelay := 15;
      3: SNDelay := 9
   end
end;
procedure SNFood;
var i, cell : integer;
begin
   snFood := 0;
   snSeed := (snSeed+73) mod snCells;
   cell := snSeed+1;
   for i := 1 to snCells do begin
      if snOcc[cell] = 0 then begin
         snFood := cell;
         exit(SNFood)
      end;
      cell := (cell mod snCells)+1
   end;
   snWon := true; snDone := true; snPause := true
end;
procedure SNNew;
var i : integer;
begin
   for i := 1 to snCells do begin
      snOcc[i] := 0; snBody[i] := 0; snShown[i] := -1
   end;
   snBody[1] := 147; snBody[2] := 148; snBody[3] := 149;
   snOcc[147] := 1; snOcc[148] := 1; snOcc[149] := 1;
   snHead := 3; snTail := 1; snLen := 3; snPos := 149;
   snFood := 154; snSeed := 17; snScore := 0; snSteps := 0;
   snDir := 2; snNextD := 2; snTurn := false;
   snDone := false; snWon := false; snPause := true;
   snPaint := false; snHud := true; snReady := true;
   snNext := Time+SNDelay
end;
procedure SNDraw;
var i, x, y, value : integer;
    box : Rect;
    text : Str255;
begin
   if myWindow = nil then exit(SNDraw);
   SetPort(myWindow); ClipRect(myWindow^.portRect); PenSize(1,1);
   if not snPaint then begin
      EraseRect(myWindow^.portRect);
      MoveTo(16,18); DrawString('KIGYO - SNAKE');
      SetRect(box,14,38,298,210); FrameRect(box);
      MoveTo(316,105); DrawString('W A S D: MOZGAS');
      MoveTo(316,126); DrawString('SZOKOZ: INDUL/SZUNET');
      MoveTo(316,147); DrawString('N: UJ JATEK');
      MoveTo(316,168); DrawString('1 2 3: SEBESSEG');
      MoveTo(316,189); DrawString('F: FAL MOD, UJ JATEK');
      MoveTo(16,233); DrawString('GYUJTSD AZ ETELT! NE UTKOZZ MAGADBA!');
      snHud := true
   end;
   for i := 1 to snCells do begin
      value := snOcc[i];
      if i = snPos then value := 2;
      if i = snFood then value := 3;
      if (not snPaint) or (value <> snShown[i]) then begin
         x := snLeft+((i-1) mod snWidth)*snCellW;
         y := snTop+((i-1) div snWidth)*snCellH;
         SetRect(box,x,y,x+snCellW,y+snCellH); EraseRect(box);
         if (value = 1) or (value = 2) then begin
            SetRect(box,x+1,y+1,x+snCellW-1,y+snCellH-1);
            PaintRect(box);
            if value = 2 then begin
               SetRect(box,x+4,y+3,x+10,y+9); EraseRect(box)
            end
         end;
         if value = 3 then begin
            SetRect(box,x+3,y+2,x+11,y+10); FrameOval(box);
            MoveTo(x+7,y+3); LineTo(x+7,y+9);
            MoveTo(x+4,y+6); LineTo(x+10,y+6)
         end;
         snShown[i] := value
      end
   end;
   if snHud then begin
      SetRect(box,312,28,498,92); EraseRect(box);
      MoveTo(316,42); NumToStr(snScore,text); DrawString(concat('PONT: ',text));
      MoveTo(316,62); NumToStr(snSpeed,text); DrawString(concat('SEBESSEG: ',text));
      MoveTo(316,82);
      if snWalls then DrawString('SZEL: FAL') else DrawString('SZEL: ATJARHATO');
      SetRect(box,312,198,498,245); EraseRect(box); MoveTo(316,214);
      if snDone then begin
         if snWon then DrawString('NYERTEL!') else DrawString('VEGE!');
         MoveTo(316,235); DrawString('N: UJ JATEK')
      end
      else if snPause then DrawString('SZUNET - SZOKOZ')
      else DrawString('JATEK');
      snHud := false
   end;
   snPaint := true
end;
procedure SNDir(dir : integer);
begin
   if snDone or snTurn then exit(SNDir);
   if abs(dir-snDir) = 2 then exit(SNDir);
   if dir = snDir then exit(SNDir);
   snNextD := dir; snTurn := true
end;
procedure SNMove;
var row, col, target, tailpos : integer;
    grow, outside : boolean;
begin
   if snDone or snPause then exit(SNMove);
   snDir := snNextD; snTurn := false;
   row := (snPos-1) div snWidth; col := (snPos-1) mod snWidth;
   case snDir of
      1: row := row-1;
      2: col := col+1;
      3: row := row+1;
      4: col := col-1
   end;
   outside := (row < 0) or (row >= snHeight) or (col < 0) or (col >= snWidth);
   if outside and snWalls then begin
      snDone := true; snPause := true; snHud := true; SNDraw; exit(SNMove)
   end;
   if row < 0 then row := snHeight-1;
   if row >= snHeight then row := 0;
   if col < 0 then col := snWidth-1;
   if col >= snWidth then col := 0;
   target := row*snWidth+col+1;
   grow := target = snFood;
   tailpos := snBody[snTail];
   if (snOcc[target] <> 0) and (grow or (target <> tailpos)) then begin
      snDone := true; snPause := true; snHud := true; SNDraw; exit(SNMove)
   end;
   if not grow then begin
      snOcc[tailpos] := 0;
      snTail := (snTail mod snCells)+1
   end
   else begin
      snLen := snLen+1; snScore := snScore+10; snHud := true
   end;
   snHead := (snHead mod snCells)+1;
   snBody[snHead] := target; snOcc[target] := 1; snPos := target;
   if snSteps < 30000 then snSteps := snSteps+1;
   if grow then SNFood;
   SNDraw
end;
procedure SNTick;
begin
   if (myWindow = nil) or (activeFolder <> myWindow) then exit(SNTick);
   if snPause or snDone then exit(SNTick);
   if Time < snNext then exit(SNTick);
   snNext := Time+SNDelay;
   SNMove
end;
procedure SNKey(key : char);
begin
   case key of
      'w','W': SNDir(1);
      'd','D': SNDir(2);
      's','S': SNDir(3);
      'a','A': SNDir(4);
      ' ': if not snDone then begin
         snPause := not snPause; snNext := Time+SNDelay; snHud := true
      end;
      'n','N': SNNew;
      '1','2','3': begin
         snSpeed := ord(key)-ord('0'); snNext := Time+SNDelay; snHud := true
      end;
      'f','F': begin snWalls := not snWalls; SNNew end
   end;
   SNDraw
end;
'''
body = body.replace('SNFood', 'SNPlace').replace('SNDir', 'SNSetDir')
source = source[:start]+body+source[end:]
source = source.replace('sgPainted', 'snPaint').replace('SGDraw', 'SNDraw')
source = source.replace('if not sgReady then SGLoad(1);', 'if not snReady then SNNew;')
source = source.replace('SGClick;', ';')
start = source.index('case theEvent.ascii of')
end = source.index('folderActivate :', start)
source = source[:start]+"SNKey(theEvent.ascii);\n"+source[end:]
source = source.replace('folderDeactivate :\nGiveControl(theEvent);', '''folderDeactivate :
begin
   snPause := true; snHud := true; SNDraw;
   GiveControl(theEvent)
end;''')
source = source.replace('sgReady := false;', 'snReady := false; snSpeed := 1; snWalls := true;')
source = source.replace('if myWindow <> nil then BlockPresent;', 'SNTick;\nif myWindow <> nil then BlockPresent;')
assert 'sgReady' not in source and 'SGLoad' not in source and 'SGMove' not in source
(ROOT.parent/'src/M.TEXT').write_bytes(source.replace('\n','\r').encode('ascii'))
print('Supporting units are already in src/.')

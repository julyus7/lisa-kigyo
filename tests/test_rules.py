"""Independent Snake rule fixtures and deterministic replay checks."""
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent
D={1:(0,-1),2:(1,0),3:(0,1),4:(-1,0)}

class Snake:
    def __init__(self, walls=True):
        self.walls=walls; self.body=[147,148,149]; self.food=154
        self.direction=2; self.pending=2; self.turned=False
        self.seed=17; self.score=0; self.steps=0; self.done=False; self.won=False
    def turn(self, direction):
        if self.done or self.turned or abs(direction-self.direction)==2 or direction==self.direction:
            return
        self.pending=direction; self.turned=True
    def step(self):
        if self.done:return
        self.direction=self.pending;self.turned=False
        x=(self.body[-1]-1)%20;y=(self.body[-1]-1)//20
        dx,dy=D[self.direction];x+=dx;y+=dy
        if self.walls and not (0<=x<20 and 0<=y<14):
            self.done=True;return
        target=(y%14)*20+x%20+1
        grow=target==self.food
        if target in self.body and (grow or target!=self.body[0]):
            self.done=True;return
        if not grow:self.body.pop(0)
        else:self.score+=10
        self.body.append(target);self.steps+=1
        if grow:
            self.seed=(self.seed+73)%280
            self.food=next((1+(self.seed+i)%280 for i in range(280)
                            if 1+(self.seed+i)%280 not in self.body),0)
            if not self.food:self.won=True;self.done=True

records=[]
def passed(label):
    records.append(label);print('PASS',label)

s=Snake();s.turn(4);assert s.pending==2
s.turn(1);s.turn(4);assert s.pending==1
s.step();assert s.body[-1]==129 and s.direction==1
passed('opposite direction and two turns in one tick rejected')
s=Snake()
for _ in range(5):s.step()
assert len(s.body)==4 and s.score==10 and s.body[-1]==154 and s.food==91
passed('food increases length and score; deterministic new food on empty cell')
for _ in range(7):s.step()
assert s.done and s.body[-1]==160 and s.steps==11
passed('right wall stops game without corrupting body')
for direction, head in [(1,9),(2,160),(3,269),(4,141)]:
    s=Snake();s.body=[head];s.direction=s.pending=direction;s.step();assert s.done
passed('all four wall boundaries')
for direction, head, dest in [(1,9,269),(2,160,141),(3,269,9),(4,141,160)]:
    s=Snake(False);s.body=[head];s.direction=s.pending=direction;s.step()
    assert not s.done and s.body[-1]==dest
passed('all four wrap boundaries')
s=Snake(False)
for _ in range(1000):
    s.step();assert len(s.body)==len(set(s.body)) and not s.done
assert s.steps==1000
passed('1000 automatic straight movements with wrapping and valid body')
s=Snake();s.body=[147,148,168,167];s.direction=s.pending=1;s.food=200;s.step()
assert not s.done and s.body==[148,168,167,147]
passed('moving into vacated tail is legal')
s=Snake();s.body=[146,147,148,168,167];s.direction=s.pending=1;s.step();assert s.done
passed('collision with body ends game')
s=Snake();s.body=list(range(1,280));s.direction=s.pending=2;s.food=280;s.step()
assert s.won and s.done and len(s.body)==280 and s.food==0
passed('filling the board wins without food placement loop')
source=(ROOT.parent/'src/M.TEXT').read_text()
assert 'SNTick;\nif myWindow <> nil then BlockPresent;' in source
assert 'snNext := Time+SNDelay' in source
for caption in ('KIGYO - SNAKE','SZUNET - SZOKOZ','SZEL: ATJARHATO','VEGE!','NYERTEL!'):
    assert caption in source
passed('native source contains timed loop and Hungarian captions')
(ROOT/'host-validation.json').write_text(json.dumps({'passed':len(records),'checks':records},indent=2)+'\n')

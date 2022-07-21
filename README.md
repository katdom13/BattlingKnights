# Challenge: Battling Knights
## How to read the solution

### Prerequisites
#### 1. Moves are indicated in the `moves.txt` file
#### 2. You can edit the `moves.txt` file

##### Example `moves.txt` file content
```
GAME-START
R:S
R:S
B:E
G:N
Y:N
GAME-END
```

### Run `main.py`
#### The output is shown in `final_state.json` in the following format:

```
{
    "red": [<R position>,<R status>,<R item (null if no item)>,R Attack,<R Defence>],
    "blue": [<B position>,<B status>,<B item (null if no item)>,B Attack,<B Defence>],
    "green": [<G position>,<G status>,<G item (null if no item)>,G Attack,<G Defence>],
    "yellow": [<Y position>,<Y status>,<Y item (null if no item)>,Y Attack,<Y Defence>],
    "magic_staff": [<M position>,<M equipped>],
    "helmet": [<H position>,<H equipped>],
    "dagger": [<D position>,<D equipped>],
    "axe": [<A position>,<A equipped>],
}
```

##### Example `final_state.json` file content based on the moves above.
```
{
    "red": [[2,0],"LIVE",null,1,1],
    "blue": [[7,1],"LIVE",null,1,1],
    "green": [[6,7],"LIVE",null,1,1],
    "yellow": [null,"DROWNED",null,0,0],
    "magic_staff": [[5,2],false],
    "helmet": [[5,5],false],
    "dagger": [[2,5],false],
    "axe": [[2,2],false]
}

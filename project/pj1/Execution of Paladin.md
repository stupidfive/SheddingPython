# The Execution of Paladin

Murloc is a powerful race in Hearthstone. In the set League of Explorer, a new Paladin ability card called **Anyfin Can Happen** is released with the ability to summon 7 Murlocs that died this game.

If there aren't enough dead Murlocs, it may summon less than 7 Murlocs.

![Anyfin Can Happen](http://wow.zamimg.com/images/hearthstone/cards/enus/original/LOE_026.png)

There are many different minions in Murloc race, here are four of them:

Coldlight Oracle: 3 **MANA**, 2 **ATTACK**, 2 **HP**. **Battlecry**: Each player draws 2 cards.

Muloc Warleader: 3 **MANA**, 3 **ATTACK**, 3 **HP**. All other Murlocs have +2/+1.

Bluegill Warrior: 2 **MANA**, 2 **ATTACK**, 3 **HP**. **Charge**.

Old Murk-Eye: 4 **MANA**, 2 **ATTACK**, 3 **HP**. **Charge**. Has +1 Attack for each other Murloc on the **Battlefield**.

![Coldlight Oracle](http://wow.zamimg.com/images/hearthstone/cards/enus/original/EX1_050.png)
![Muloc Warleader](http://wow.zamimg.com/images/hearthstone/cards/enus/original/EX1_507.png)
![Bluegill Warrior](http://wow.zamimg.com/images/hearthstone/cards/enus/original/CS2_173.png)
![Old Murk-Eye](http://wow.zamimg.com/images/hearthstone/cards/enus/original/EX1_062.png)

Here are some explanations:

**MANA**: The cost of summon the minion. Minions summoned by ability cards cost no mana besides the cost of the ability cards. Every player has 10 **MANAs** at most.

**ATTACK**: How many damage can the minion make once.

**HP**: How many attacks can the minions or heroes take.

**Battlecry**: An ability where a particular effect activates when the card with the Battlecry is dealt to the **Battlefield**. Minions summoned by skills don't trigger **Battlecry**.

**Charge**: Normally, minion can't attack the round it's being summoned. But with **Charge** it can.

**Battlefield**: The board where any gaming events happen.

+2/+1: +2 **ATTACK** and +1 **HP**.

Now, it's your turn of the game. You have 10 **MANAs** and only one card: **Anyfin Can Happen**. There are nothing on the **Battlefield**, which means your minions can directly attack enemy hero. You can remember the list of dead Murlocs. You know how many HP the enemy hero remains. Will you win this game through this only card you have?

## Input

Multiple test cases. The first line contains an integer T (T <= 22000), indicating the number of test case.

The first line of each test contains two integers, n (the number of dead Murlocs, 0 <= n <= 7) and h (the HP of enemy hero, 0 < h <= 30).

The n lines follows, each line contains a string, indicates the name of dead Murloc. The string will only be "**Coldlight Oracle**", "**Muloc Warleader**", "**Bluegill Warrior**" or "**Old Murk-Eye**".

## Output

One line per case. If you can win the game in this turn, output "Mrghllghghllghg!" (without quotes), Otherwise, output "Tell you a joke, the execution of Paladin." You will win the game if you attack enemy hero with your minions and make his/her HP less or equal than 0.

## Sample

| Input            |                   Output                   |
|------------------|:-------------------------------------------|
| 3                | Tell you a joke, the execution of Paladin. |
| 3 1              | Mrghllghghllghg                            |
| Coldlight Oracle | Tell you a joke, the execution of Paladin. |
| Coldlight Oracle |                                            |
| Muloc Warleader  |                                            |
| 3 8              |                                            |
| Old Murk-Eye     |                                            |
| Old Murk-Eye     |                                            |
| Coldlight Oracle |                                            |
| 7 30             |                                            |
| Old Murk-Eye     |                                            |
| Bluegill Warrior |                                            |
| Bluegill Warrior |                                            |
| Muloc Warleader  |                                            |
| Muloc Warleader  |                                            |
| Coldlight Oracle |                                            |
| Coldlight Oracle |                                            |

## Hint

In the first test case, none of the Murlocs can attack.

In the second test case, each **Old Murk-Eye** has +2 **ATTACK** because of the other **Old Murk-Eye** and a **Coldlight Oracle**. This makes the execution 8.

In the last test case, **Old Murk-Eye** has 12 **ATTACK** (2 basic, 6 from other Murlocs, 2 **Muloc Warleader**s), **Bluegill Warrior** has 6 **ATTACK** (2 basic, 2 **Muloc Warleader**s). This makes the execution 24.

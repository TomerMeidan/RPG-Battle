# RPG Battle Simulator
This is a text-based RPG battle simulator where the player faces off against an enemy. The player has the option to attack, use magic, or use items during their turn, and the enemy will attack during their turn. The game continues until either the player or the enemy has been defeated.

## Getting Started
To run the game, simply run the main.py file. The game requires Python 3 to be installed on your machine.

## Game Mechanics
### Player
The player has the following stats:

#### HP (Health Points): represents the amount of damage the player can take before being defeated.
MP (Magic Points): represents the amount of magic the player can use during battle.
Attack Power: represents the amount of damage the player's physical attacks deal.
Magic Power: represents the amount of damage the player's magic attacks deal.
Magic Spells: a list of spells the player can use during battle.
Inventory: a list of items the player can use during battle.
During their turn, the player can:

Attack: deal damage to the enemy using physical attacks.
Use Magic: use a spell to deal damage or heal the player.
Use Item: use an item to heal the player, restore MP, or deal damage to the enemy.
Enemy
The enemy has the following stats:

HP (Health Points): represents the amount of damage the enemy can take before being defeated.
Attack Power: represents the amount of damage the enemy's attacks deal.
Magic Power: represents the amount of damage the enemy's magic attacks deal.
During their turn, the enemy will attack the player.

Built With
Python 3

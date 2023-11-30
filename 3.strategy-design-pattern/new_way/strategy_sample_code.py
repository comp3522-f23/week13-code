import abc


# Strategy functions
def sword_attack(enemy):
    damage = 5
    print(f"hit {enemy['name']} with a Sword for {damage} damage")
    enemy["health"] -= damage
    return damage


def spear_attack(enemy):
    damage = 10
    print(f"hit {enemy['name']} with a Spear for {damage} damage")
    enemy["health"] -= damage
    return damage


def bow_and_arrow_attack(enemy):
    damage = 15
    print(f"hit {enemy['name']} with a Bow and Arrow for {damage} damage")
    enemy["health"] -= damage
    return damage


def cannon_attack(enemy):
    damage = 75
    print(f"hit {enemy['name']} with a Cannon for {damage} damage")
    enemy["health"] -= damage
    return damage


# Character functions
def create_character(name, health, weapon):
    return {"name": name, "health": health, "weapon": weapon}


def set_weapon(character, weapon):
    character["weapon"] = weapon


def attack(attacker, enemy):
    print(f"{attacker['name']}", end=" ")
    damage = attacker["weapon"](enemy)
    return damage


def main():
    # create characters and strategies
    aragorn = create_character("Aragorn", 100, sword_attack)
    sauron = create_character("Sauron", 100, spear_attack)

    # aragorn attacks with the sword with which it was initialized
    attack(aragorn, sauron)

    # aragorn can dynamically change attack behavior by changing the weapon
    set_weapon(aragorn, spear_attack)
    attack(aragorn, sauron)

    set_weapon(aragorn, bow_and_arrow_attack)
    attack(aragorn, sauron)

    attack(sauron, aragorn)

    # sauron can dynamically change attack behavior by changing the weapon
    set_weapon(sauron, cannon_attack)
    attack(sauron, aragorn)

    # print character name and health
    print(f"{aragorn['name']} has {aragorn['health']} health")
    print(f"{sauron['name']} has {sauron['health']} health")


if __name__ == "__main__":
    main()

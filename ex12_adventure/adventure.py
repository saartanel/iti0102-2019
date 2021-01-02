"""Time to play DND."""


class Adventurer:
    """Information about the Adventurer class."""

    def __init__(self, name, class_type, power, experience=0):
        """Create variables for Adventurer class."""
        self.name = name
        if class_type in ["Fighter", "Druid", "Wizard", "Paladin"]:
            self.class_type = class_type
        else:
            self.class_type = "Fighter"
        self.power = power
        self.experience = experience

    def add_experience(self, exp):
        """
        Add experience to adventurer.

        :param exp:
        """
        self.experience += exp

    def add_power(self, power):
        """
        Add power to adventurer.

        :param power:
        """
        self.power += power

    def __repr__(self):
        """Return function for Adventurer."""
        return f"{self.name}, the {self.class_type}, Power: {self.power}, Experience: {self.experience}."


class Monster:
    """Information about the Monster class."""

    def __init__(self, name, mon_type, power=0):
        """Create variables for Monster class."""
        self.name = name
        if mon_type == "Zombie":
            self.name = f"Undead {name}"
        self.mon_type = mon_type
        self.power = power

    def __repr__(self):
        """Return function for Monster class."""
        return f"{self.name} of type {self.mon_type}, Power: {self.power}."


class World:
    """Information about the World class."""

    def __init__(self, PM):
        """Create variables for World class."""
        self.adventurerlist = []
        self.monsterlist = []
        self.graveyard = []
        self.PM = PM
        self.necromancer = False
        self.active_adventurerlist = []
        self.active_monsterlist = []

    def add_adventurer(self, adventurer: Adventurer):
        """Add adventurer to adventurerlist."""
        if isinstance(adventurer, Adventurer):
            self.adventurerlist.append(adventurer)

    def add_monster(self, monster: Monster):
        """Add monster to monsterlist."""
        if isinstance(monster, Monster):
            self.monsterlist.append(monster)

    def get_adventurerlist(self):
        """Return function for adventurerlist."""
        return self.adventurerlist

    def get_monsterlist(self):
        """Return function for monsterlist."""
        return self.monsterlist

    def get_graveyard(self):
        """Return function for graveyard."""
        return self.graveyard

    def get_python_master(self):
        """Return function for PM."""
        return self.PM

    def change_necromancer(self, bool):
        """Change necromancer status to True or False."""
        if bool:
            self.necromancer = True
        if not bool:
            self.necromancer = False

    def revive_graveyard(self):
        """Revive monsters if necromancer is True."""
        if self.necromancer:
            x = self.graveyard.copy()
            for dead_being in x:
                if isinstance(dead_being, Monster):
                    if dead_being.mon_type != "Zombie":
                        dead_being.name = f"Undead {dead_being.name}"
                    dead_being.mon_type = "Zombie"
                    self.add_monster(dead_being)
                    self.graveyard.remove(dead_being)
                if isinstance(dead_being, Adventurer):
                    monpower = dead_being.power
                    monname = f"Undead {dead_being.name}"
                    montype = f"Zombie {dead_being.class_type}"
                    self.add_monster(Monster(monname, montype, monpower))
                    self.graveyard.remove(dead_being)
                    self.necromancer = False

    def add_strongest(self, class_type):
        """
        Add strongest non-active adventurer to active duty list.

        :param class_type:
        """
        y = []
        for adventurer in self.adventurerlist:
            if adventurer.class_type == class_type:
                y.append(adventurer)
        if y:
            strongest = sorted(y, key=lambda a: a.power)[-1]
            self.adventurerlist.remove(strongest)
            self.active_adventurerlist.append(strongest)

    def add_weakest(self, class_type):
        """
        Add weakest non-active adventurer to active duty list.

        :param class_type:
        """
        y = []
        for adventurer in self.adventurerlist:
            if adventurer.class_type == class_type:
                y.append(adventurer)
        if y:
            strongest = sorted(y, key=lambda a: a.power)[0]
            self.adventurerlist.remove(strongest)
            self.active_adventurerlist.append(strongest)

    def add_most_experience(self, class_type):
        """
        Add a non-active adventurer with the most experience to active duty list.

        :param class_type:
        """
        y = []
        for adventurer in self.adventurerlist:
            if adventurer.class_type == class_type:
                y.append(adventurer)
        if y:
            strongest = sorted(y, key=lambda a: a.experience)[-1]
            self.adventurerlist.remove(strongest)
            self.active_adventurerlist.append(strongest)

    def add_least_experience(self, class_type):
        """
        Add a non-active adventurer with the most experience to active duty list.

        :param class_type:
        """
        y = []
        for adventurer in self.adventurerlist:
            if adventurer.class_type == class_type:
                y.append(adventurer)
        if y:
            strongest = sorted(y, key=lambda a: a.experience)[0]
            self.adventurerlist.remove(strongest)
            self.active_adventurerlist.append(strongest)

    def add_by_name(self, name):
        """
        If adventurer with given name exists, add to active duty list.

        :param name:
        """
        for adventurer in self.adventurerlist:
            if name == adventurer.name:
                self.active_adventurerlist.append(adventurer)
                self.adventurerlist.remove(adventurer)

    def add_all_of_class_type(self, class_type):
        """
        Add all adventurers with given class type to active duty.

        :param class_type:
        """
        x = self.adventurerlist.copy()
        for adventurer in x:
            if adventurer.class_type == class_type:
                self.active_adventurerlist.append(adventurer)
                self.adventurerlist.remove(adventurer)

    def add_all(self):
        """Add all non-active adventurers to active duty."""
        x = self.adventurerlist.copy()
        for adventurer in x:
            self.active_adventurerlist.append(adventurer)
            self.adventurerlist.remove(adventurer)

    def get_active_adventurers(self):
        """Return function for active_adventurers list."""
        return sorted(self.active_adventurerlist, key=lambda x: x.power, reverse=True)

    def add_monster_by_name(self, name):
        """
        If monster with given name exists, add to active monster list.

        :param name:
        """
        for monster in self.monsterlist:
            if monster.name == name:
                self.active_monsterlist.append(monster)
                self.monsterlist.remove(monster)

    def add_strongest_monster(self):
        """Add strongest monster to active monster list."""
        if self.monsterlist:
            y = sorted(self.monsterlist, key=lambda a: a.power)[-1]
            self.active_monsterlist.append(y)
            self.monsterlist.remove(y)

    def add_weakest_monster(self):
        """Add weakest monster to active monster list."""
        if self.monsterlist:
            y = sorted(self.monsterlist, key=lambda a: a.power)[0]
            self.active_monsterlist.append(y)
            self.monsterlist.remove(y)

    def add_all_of_type(self, mon_type):
        """Add all monsters with given mon_type to active monster list."""
        y = self.monsterlist.copy()
        if self.monsterlist:
            for monster in y:
                if monster.mon_type == mon_type:
                    self.active_monsterlist.append(monster)
                    self.monsterlist.remove(monster)

    def add_all_monsters(self):
        """Add all monsters to active monster list."""
        y = self.monsterlist.copy()
        if self.monsterlist:
            for monster in y:
                self.active_monsterlist.append(monster)
                self.monsterlist.remove(monster)

    def get_active_monsters(self):
        """Return function for active monsters list."""
        return sorted(self.active_monsterlist, key=lambda x: x.power, reverse=True)

    def remove_character(self, name):
        """Remove monster/adventurer from World."""
        x = self.adventurerlist.copy()
        y = self.monsterlist.copy()
        z = self.graveyard.copy()
        for adventurer in x:
            if adventurer.name == name:
                self.adventurerlist.remove(adventurer)
                return
        for monster in y:
            if monster.name == name:
                self.monsterlist.remove(monster)
                return
        for being in z:
            if being.name == name:
                self.graveyard.remove(being)
                return

    def paladin_power(self):
        """Check active monster list for Zombies, Zombie Fighters, Zombie Druids, Zombie Paladins or Zombie Wizards."""
        monster_check = False
        total_power = 0
        for monster in self.active_monsterlist:
            if monster.mon_type in ["Zombie", "Zombie Fighter", "Zombie Druid", "Zombie Paladin", "Zombie Wizard"]:
                monster_check = True
                break
        if monster_check:
            for adventurer in self.active_adventurerlist:
                total_power += adventurer.power
                if adventurer.class_type == "Paladin":
                    total_power += adventurer.power
            return total_power
        total_power = sum([adventurer.power for adventurer in self.active_adventurerlist])
        return total_power

    def druid_play(self, druid_check=False, animal_ent_check=False):
        """Check active monster list for Animal or Ent and adventurer list for druids."""
        for adventurer in self.active_adventurerlist:
            if adventurer.class_type == "Druid":
                druid_check = True
        for monster in self.active_monsterlist:
            if monster.mon_type in ["Ent", "Animal"]:
                animal_ent_check = True
        if druid_check and animal_ent_check:
            x = self.active_monsterlist.copy()
            for monster in x:
                if monster.mon_type in ["Ent", "Animal"]:
                    self.monsterlist.append(monster)
                    self.active_monsterlist.remove(monster)

    def not_deadly(self):
        """Remove monsters from active list and move to old list."""
        x = self.active_adventurerlist.copy()
        y = self.active_monsterlist.copy()
        for adventurer in x:
            self.adventurerlist.append(adventurer)
            self.active_adventurerlist.remove(adventurer)
        for monster in y:
            self.monsterlist.append(monster)
            self.active_monsterlist.remove(monster)

    def deadly(self, winner):
        """Move losers to graveyard."""
        if winner == "adv":
            x = self.active_adventurerlist.copy()
            y = self.active_monsterlist.copy()
            for adventurer in x:
                self.adventurerlist.append(adventurer)
                self.active_adventurerlist.remove(adventurer)
            for monster in y:
                self.graveyard.append(monster)
                self.active_monsterlist.remove(monster)
        elif winner == "mon":
            x = self.active_adventurerlist.copy()
            y = self.active_monsterlist.copy()
            for adventurer in x:
                self.graveyard.append(adventurer)
                self.active_adventurerlist.remove(adventurer)
            for monster in y:
                self.monsterlist.append(monster)
                self.active_monsterlist.remove(monster)
        elif winner == "tie":
            self.not_deadly()

    def add_xp(self, add_xp, winner, deadly, mon_sum_power):
        """Since the game was a tie or the adventurers won, they get some xp."""
        adventure_len = len(self.active_adventurerlist)
        if add_xp and mon_sum_power and adventure_len:
            xp_per_adv = mon_sum_power // adventure_len
            if xp_per_adv:
                if deadly and winner == "adv":
                    xp_per_adv = xp_per_adv * 2
                if not deadly and winner == "tie":
                    xp_per_adv = xp_per_adv // 2
                for adventurer in self.active_adventurerlist:
                    adventurer.experience += xp_per_adv

    def go_adventure(self, deadly=False):
        """
        Start game.

        :param deadly:
        """
        winner = ""
        add_xp = False
        self.druid_play()
        adv_sum_power = self.paladin_power()
        mon_sum_power = sum([monster.power for monster in self.active_monsterlist])
        if adv_sum_power > mon_sum_power:
            winner = "adv"
            add_xp = True
        elif adv_sum_power < mon_sum_power:
            winner = "mon"
        elif adv_sum_power == mon_sum_power:
            winner = "tie"
            add_xp = True
        self.add_xp(add_xp, winner, deadly, mon_sum_power)
        if not deadly:
            self.not_deadly()
        elif deadly:
            self.deadly(winner)


if __name__ == "__main__":
    print("Kord oli maailm.")
    Maailm = World("Sõber")
    print(Maailm.get_python_master())  # -> "Sõber"
    print(Maailm.get_graveyard())  # -> []
    print()
    print("Tutvustame tegelasi.")
    Kangelane = Adventurer("Sander", "Paladin", 50)
    Tüütu_Sõber = Adventurer("XxX_Eepiline_Sõdalane_XxX", "Tulevikurändaja ja ninja", 999999)
    Lahe_Sõber = Adventurer("Peep", "Druid", 25)
    Teine_Sõber = Adventurer("Toots", "Wizard", 40)

    print(Kangelane)  # -> "Sander, the Paladin, Power: 50, Experience: 0."
    # Ei, tüütu sõber, sa ei saa olla tulevikurändaja ja ninja, nüüd sa pead fighter olema.
    print(Tüütu_Sõber)  # -> "XxX_Eepiline_Sõdalane_XxX, the Fighter, Power: 999999, Experience: 0."

    print("Sa ei tohiks kohe alguses ka nii tugev olla.")
    Tüütu_Sõber.add_power(-999959)
    print(Tüütu_Sõber)  # -> XxX_Eepiline_Sõdalane_XxX, the Fighter, Power: 40, Experience: 0.
    print()
    print(Lahe_Sõber)  # -> "Peep, the Druid, Power: 25, Experience: 0."
    print(Teine_Sõber)  # -> "Toots, the Wizard, Power: 40, Experience: 0."
    print()
    Lahe_Sõber.add_power(20)
    print("Sa tundud kuidagi nõrk, ma lisasin sulle natukene tugevust.")
    print(Lahe_Sõber)  # -> "Peep, the Druid, Power: 45, Experience: 0."

    Maailm.add_adventurer(Kangelane)
    Maailm.add_adventurer(Lahe_Sõber)
    Maailm.add_adventurer(Teine_Sõber)
    print(Maailm.get_adventurerlist())  # -> Sander, Peep ja Toots

    Maailm.add_monster(Tüütu_Sõber)
    # Ei, tüütu sõber, sa ei saa olla vaenlane.
    print(Maailm.get_monsterlist())  # -> []
    Maailm.add_adventurer(Tüütu_Sõber)

    print()
    print()
    print("Oodake veidikene, ma tekitan natukene kolle.")
    Zombie = Monster("Rat", "Zombie", 10)
    GoblinSpear = Monster("Goblin Spearman", "Goblin", 10)
    GoblinArc = Monster("Goblin Archer", "Goblin", 5)
    BigOgre = Monster("Big Ogre", "Ogre", 120)
    GargantuanBadger = Monster("Massive Badger", "Animal", 1590)

    print(BigOgre)  # -> "Big Ogre of type Ogre, Power: 120."
    print(Zombie)  # -> "Undead Rat of type Zombie, Power: 10."

    Maailm.add_monster(GoblinSpear)

    print()
    print()
    print("Mängime esimese kakluse läbi!")
    Maailm.add_strongest("Druid")
    Maailm.add_strongest_monster()
    print(Maailm.get_active_adventurers())  # -> Peep
    print(Maailm.get_active_monsters())  # -> [Goblin Spearman of type Goblin, Power: 10.]

    Maailm.go_adventure(True)

    Maailm.add_strongest("Druid")
    print(Maailm.get_active_adventurers())  # -> [Peep, the Druid, Power: 45, Experience: 20.]
    print("Surnuaias peaks üks goblin olema.")
    print(Maailm.get_graveyard())  # ->[Goblin Spearman of type Goblin, Power: 10.]

    Maailm.add_monster(GargantuanBadger)
    Maailm.add_strongest_monster()

    Maailm.go_adventure(True)
    # Druid on loomade sõber, ja ajab massiivse mägra ära.
    print(Maailm.get_adventurerlist())  # -> Kõik 4 mängijat.
    print(Maailm.get_active_adventurers())
    print(Maailm.get_monsterlist())  # -> [Massive Badger of type Animal, Power: 1590.]

    Maailm.remove_character("Massive Badger")
    print(Maailm.get_monsterlist())  # -> []

    print("Su sõber ütleb: \"Kui kõik need testid andsid sinu koodiga sama tulemuse mille ma siin ette kirjutasin,"
          " peaks kõik okei olema, proovi testerisse pushida! \" ")

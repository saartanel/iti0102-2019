"""Chefs creating tasty pizza."""
import math


class Chef:
    """Chef class."""

    def __init__(self, name: str, experience_level: int):
        """Create variables for Chef class."""
        self.name = name
        self.experience_level = experience_level
        self.money = 0

    def __repr__(self):
        """Creating return str for Chef class."""
        return f"Pizza chef {self.name.capitalize()} with {self.experience_level} XP"


class Pizza:
    """Pizza class."""

    def __init__(self, name: str, diameter: int, toppings: list):
        """Create variables for Pizza class."""
        self.name = name
        self.diameter = diameter
        self.toppings = toppings

    def calculate_complexity(self) -> int:
        """Calculate pizza topping complexity using self.toppings variable."""
        cplx = 0
        cplx = sum([cplx + len(i) // 3 for i in self.toppings])
        return cplx

    def calculate_price(self) -> int:
        """Calculate pizza price using math.pi and Pizza class variables."""
        area = math.pi * (self.diameter / 2) ** 2
        price = area / 40 + len(self.toppings) // 2
        price = math.floor(price * 100)
        return price

    def __repr__(self):
        """Creating return str for Pizza class."""
        price = '{:,.2f}'.format(self.calculate_price() / 100)
        return f"{self.name.capitalize()} pizza with a price of {price}"


class Pizzeria:
    """Pizzeria class."""

    def __init__(self, name: str, is_fancy: bool, budget: int):
        """Create variables for Pizzeria class."""
        self.name = name
        self.is_fancy = is_fancy
        self.budget = budget
        self.chefs = []
        self.menu = []
        self.baked_pizzas = {}

    def add_chef(self, chef: Chef) -> Chef or None:
        """
        If chef isnt in chefs list, add him/her.

        :param chef:
        """
        if chef not in self.chefs:
            if self.is_fancy:
                if chef.experience_level >= 25:
                    self.chefs.append(chef)
                    self.sort_chefs_by_xp()
                    return chef
                return None
            self.chefs.append(chef)
            return chef
        return None

    def sort_chefs_by_xp(self):
        """Sort the chefs list by chef XP."""
        self.chefs = sorted(self.chefs, key=lambda chef: chef.experience_level)

    def remove_chef(self, chef: Chef):
        """
        If chef is in chefs list, remove him/her.

        :param chef:
        """
        if chef in self.chefs:
            self.chefs.remove(chef)

    def add_pizza_to_menu(self, pizza: Pizza):
        """
        If pizza isnt in the menu, add it.

        :param pizza:
        """
        if (self.budget - pizza.calculate_price()) > 0:
            if len(self.chefs) > 0:
                if pizza not in self.menu:
                    self.budget -= pizza.calculate_price()
                    self.menu.append(pizza)

    def remove_pizza_from_menu(self, pizza: Pizza):
        """
        If pizza is in menu, remove it.

        :param pizza:
        """
        if pizza in self.menu:
            self.menu.remove(pizza)

    def bake_pizza(self, pizza: Pizza) -> Pizza or None:
        """
        Put pizza to the oven.

        :param pizza:
        """
        if pizza in self.menu:
            for chef in self.chefs:
                if chef.experience_level >= pizza.calculate_complexity():
                    chef.experience_level += len(pizza.name) // 2
                    self.sort_chefs_by_xp()
                    earnings = pizza.calculate_price() * 4 + len(pizza.name)
                    if pizza not in self.baked_pizzas:
                        self.baked_pizzas[pizza] = 0
                    self.baked_pizzas[pizza] += 1
                    if earnings % 2 == 1:
                        earnings -= 1
                    chef.money += earnings / 2
                    self.budget += earnings / 2
                    return pizza
        return None

    def get_pizza_menu(self) -> list:
        """Give customer the menu."""
        self.menu = sorted(self.menu, key=lambda pizza: pizza.calculate_price(), reverse=True)
        """return_list = []
        for pizza in self.menu:
            price = '{:,.2f}'.format(pizza.calculate_price() / 100)
            return_list.append(f"{pizza.name.capitalize()} with a price of {price}")
        return return_list"""
        return self.menu

    def get_baked_pizzas(self) -> dict:
        """Return dict of baked pizzas."""
        return self.baked_pizzas

    def get_chefs(self) -> list:
        """Return a list of chefs sorted by XP levels."""
        self.sort_chefs_by_xp()
        return self.chefs

    def __repr__(self):
        """Creating return str for Pizzeria class."""
        return f"{self.name.capitalize()} with {len(self.chefs)} pizza chef(s)."


if __name__ == '__main__':
    pizzeria1 = Pizzeria("Mama's Pizza", True, 10000)
    print(pizzeria1)  # Mama's pizza with 0 pizza chef(s).

    pizzeria1.add_chef(Chef("Clara", 24))
    print(pizzeria1)
    # Mama's pizza with 0 pizza chef(s). -> Clara was not added because of low XP (24) since it's a fancy pizzeria.

    pizza1 = Pizza("basic", 20, ["Cheese", "Ham"])
    print(pizzeria1.bake_pizza(pizza1))  # None -> No such pizza on the menu nor a chef in the pizzeria.

    ##########################################################
    sebastian = Chef("Sebastian", 58)
    charles = Chef("Charles", 35)
    kimi = Chef("Kimi", 83)

    pizzeria1.add_chef(sebastian)
    pizzeria1.add_chef(charles)
    pizzeria1.add_chef(kimi)

    # Trying to order a pizza which is not on the menu.

    print(pizzeria1.bake_pizza(pizza1))  # None

    pizzeria1.add_pizza_to_menu(pizza1)  # Price is 8.85

    print(pizzeria1.budget)  # 9115
    print(pizzeria1.get_pizza_menu())  # [Basic pizza with a price of 8.85]

    print(pizzeria1.bake_pizza(pizza1))  # Basic pizza with a price of 8.85

    print(pizzeria1.get_chefs())
    # Charles was chosen to bake the pizza, because Charles' XP was the closest to pizza's complexity

    print(pizzeria1.budget)  # 10887
    print(charles.money)  # 1772

    print(pizzeria1.get_baked_pizzas())  # {Basic pizza with a price of 8.85: 1}

    ##########################################################
    pizzeria2 = Pizzeria("Maranello", False, 10000)

    fernando = Chef("Fernando", 9)
    felipe = Chef("Felipe", 6)
    michael = Chef("Michael", 17)
    rubens = Chef("Rubens", 4)
    eddie = Chef("Eddie", 5)

    pizzeria2.add_chef(fernando)
    pizzeria2.add_chef(felipe)
    pizzeria2.add_chef(michael)
    pizzeria2.add_chef(rubens)
    pizzeria2.add_chef(eddie)

    margherita = Pizza("Margherita", 20, ["Sauce", "Mozzarella", "Basil"])
    smoke = Pizza("Big Smoke", 30, ["nine", "NINE", "six w/dip", "seven", "45", "45 w/cheese", "SODA"])

    pizzeria2.add_pizza_to_menu(margherita)
    pizzeria2.add_pizza_to_menu(smoke)

    print(pizzeria2.get_pizza_menu())  # [Big smoke pizza with a price of 20.67, Margherita pizza with a price of 8.85]
    print(pizzeria2.get_chefs())
    # [Pizza chef Rubens with 4 XP, Pizza chef Eddie with 5 XP, Pizza chef Felipe with 6 XP,
    # Pizza chef Fernando with 9 XP, Pizza chef Michael with 17 XP]

    pizzeria2.bake_pizza(margherita)
    print(pizzeria2.get_chefs())
    # [Pizza chef Rubens with 4 XP, Pizza chef Felipe with 6 XP, Pizza chef Fernando with 9 XP,
    # Pizza chef Eddie with 10 XP, Pizza chef Michael with 17 XP]

    pizzeria2.bake_pizza(smoke)
    print(pizzeria2.get_chefs())
    # [Pizza chef Rubens with 4 XP, Pizza chef Felipe with 6 XP, Pizza chef Fernando with 9 XP,
    # Pizza chef Eddie with 14 XP, Pizza chef Michael with 17 XP]
    print(smoke)

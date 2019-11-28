from World import *

class Simulator:
    """
    Game of Life simulator. Handles the evolution of a Game of Life ``World``.
    Read https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life for an introduction to Conway's Game of Life.
    """

    def __init__(self, world = None, age = 1, survival = [2,3], birth = [3, 6]):
        """
        Constructor for Game of Life simulator.

        :param world: (optional) environment used to simulate Game of Life.
        :param age: (optional) Max age of cell.
        """
        self.generation = 0
        self.age = age
        self.birth = birth
        self.survival = survival

        if world == None:
            self.world = World(20)
        else:
            self.world = world

    def update(self) -> World:
        """
        Updates the state of the world to the next generation. Uses rules for evolution.

        :return: New state of the world.
        """

        self.generation += 1

        #Build next generation
        next_generation = World(self.world.width, self.world.height)
        birth_condition = set(range(2, self.age - 1))
        # Leftside is B3/S23 rule right side is custom rule system
        birth = [3] if self.age == 1 else self.birth # Amount of neighbours for birth
        survival = [2,3] if self.age == 1 else self.survival # Amount of neighbours for survival of a cell

        #TODO: Do something to evolve the generation
        for y in range(0, self.world.height):
            for x in range(0, self.world.width):
                cell_age = self.world.get(x, y)
                neighbours = self.world.get_neighbours(x, y)
                neighbours_count = len([n for n in neighbours if n > 0])

                # Rules for decreasing the age of a cell or preserving a cell
                if (cell_age != 0 and not neighbours_count in survival):
                    next_generation.set(x, y, cell_age - 1)
                else:
                    next_generation.set(x, y, cell_age)

                correct_birth_condition = list(set(neighbours) & birth_condition)

                # Rules for creating a cell
                if (not cell_age and neighbours_count in birth):
                    if (self.age > 1 and len(correct_birth_condition) > 0):
                        # Playing on custom rules
                        next_generation.set(x, y, self.age)
                    else:
                        # Playing on B3/S23 rules
                        next_generation.set(x, y, 1)


        self.set_world(next_generation)

        return self.world

    def get_generation(self):
        """
        Returns the value of the current generation of the simulated Game of Life.

        :return: generation of simulated Game of Life.
        """
        return self.generation

    def get_world(self):
        """
        Returns the current version of the ``World``.

        :return: current state of the world.
        """
        return self.world

    def set_world(self, world: World) -> None:
        """
        Changes the current world to the given value.

        :param world: new version of the world.

        """
        self.world = world
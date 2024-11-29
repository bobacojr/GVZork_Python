"""
This project is creating the game Zork, but with different rules.
Author: Kaleb Maulding
Date: 2/12/2023
Version: 3.10
"""
#used to go to a random location
import random
#used to print date and time
import datetime
#used to stagger print statements
from time import sleep
#used to import color
from colorama import Fore

class Item:
    """Represents objects the player may encounter during the game.

    Attributes
    ----------
    _name: str
        creates the item's name.
    _description: str
        creates the item's description.
    _calories: int
        creates the amount of calories an item has.
    _weight: int
        creates the amount of weight an item has.
    """

    def __init__(self, name, description, calories, weight):
        """
        parameters:
        ----------
        name:
            name of the item
        description:
            description of the item
        calories:
            calories of the item
        weight:
            weight of the item
        """
        self._name = name
        self._description = description
        self._calories = calories
        self._weight = weight

    def get_name(self):
        """gets and returns an items name

        returns:
        -------
        self._name:
            an instance of _name
        """
        return self._name

    def set_name(self, name):
        """sets the name of an item, raises a ValueError if blank

        parameters:
        ----------
        name:
            the name of the item
        """
        if name == '':
            raise ValueError('Name cannot be blank.')
        self._name = name

    def get_description(self):
        """gets and returns an instance of _description

        returns:
        -------
        self._description:
            an instance of _description

        error:
        -----
        ValueError:
            name cannot be blank
        """
        return self._description

    def set_description(self, description):
        """sets the description of an item, raises a ValueError if blank

        parameters:
        ----------
        description:
            the items description

        error:
        -----
        ValueError:
            description cannot be blank
        """
        if description == '':
            raise ValueError('Description cannot be blank.')
        self._description = description

    def get_calories(self):
        """gets and returns an instance of _calories

        returns:
        -------
        self._calories:
            an instance of _calories
        """
        return self._calories

    def set_calories(self, calories):
        """sets the calories an item has, raises ValueError if
        calories < 0 or calories > 1000

        parameters:
        ----------
        calories:
            amount of calories an item has

        error:
        -----
        ValueError:
            calories must be a number 0-1000
        """
        if calories < 0 or calories > 1000 or not isinstance(calories, int):
            raise ValueError('Calories must be a number 0-1000.')
        self._calories = calories

    def get_weight(self):
        """gets and returns an instance of _weight

        returns:
        -------
        self._weight:
            an instance of _weight
        """
        return self._weight

    def set_weight(self, weight):
        """sets the weight an item has, raises a ValueError if
        0 > weight or weight > 500

        parameters:
        ----------
        weight:
            the amount of weight an item has

        error:
        -----
        ValueError:
            weight must be a number 0-500 inclusive
        """
        if 0 > weight or weight > 500 or not isinstance(weight, int):
            raise ValueError('Weight must be a number 0-500 inclusive.')
        self._weight = weight

    def __str__(self):
        """returns a string defining the item

        returns:
        -------
        str:
            consists of the items nam, weight, calories, and weight
        """
        return f"{self._name} - {self._weight} lb - {self._calories} - {self._description}"

class NPC:
    """Represents people the player may encounter during the game.

    Attributes
    ----------
    _name: str
        creates the npc name.
    _description: str
        creates the npc description.
    _message_number: int
        keeps track of which message a npc is saying.
    _message_list: []
        list of messages a npc has.
    """

    def __init__(self, name, description):
        self._name = name
        self._description = description
        self._message_number = 0
        self._message_list = []

    def get_name(self):
        """gets and returns the npcs name

        returns:
        -------
        self._name:
            an instance of _name
        """
        return self._name

    def set_name(self, name):
        """sets the name of a npc, raises a ValueError if blank

        parameters:
        ----------
        name:
            the name of a npc

        error:
        -----
        ValueError:
            name cannot be blank
        """
        if name == '':
            raise ValueError('Name cannot be blank.')
        self._name = name

    def get_description(self):
        """gets and returns the description of a npc

        returns:
        -------
        self._description:
            an instance of _description
        """
        return self._description

    def set_description(self, description):
        """sets the description of a npc, raises a ValueError if blank

        parameters:
        ----------
        description:
            the description of a npc

        error:
        -----
        ValueError:
            description cannot be blank
        """
        if description == '':
            raise ValueError('Description cannot be blank.')
        self._description = description

    def get_message_number(self):
        """returns the current message(indicated by message number)
        and changes the message number appropriately.

        returns:
        -------
        message:
            the mpcs message indicated by the message number
        """
        message = self._message_list[self._message_number]
        self._message_number = (self._message_number + 1) % len(self._message_list)
        return message

    def get_message_list(self):
        """gets and returns the npcs message list

        returns:
        -------
        self._message_list:
            an instance of _message_list
        """
        return self._message_list

    def npc_message_list(self, message_list):
        """sets the list of messages a npc has,
        raises a ValueError if blank or not a str

        parameters:
        ----------
        message_list:
            the npcs list of messages

        error:
        -----
        ValueError:
            cannot be blank and must be a str
        """
        for message in message_list:
            if not isinstance(message, str):
                raise ValueError('Message cannot be blank and must be a string.')
            self._message_list = message_list

    def __str__(self):
        """returns a str stating the npcs name

        returns:
        -------
        self._name
            an instance of _name
        """
        return self._name

class Location:
    """Represents places the player may encounter during the game.

    Attributes
    ----------
    _name: str
        creates the locations name.
    _description: str
        creates the locations' description.
    _visited: bool
        indicates whether the location has been visited yet.
    _neighbors: dict
        creates a dictionary of neighboring locations.
    _npc_list: []
        creates a list of all npcs in the location.
    _item_list: []
        creates a list of all items in the location.
    """

    def __init__(self, name, description):
        """
        parameters:
        ----------
        name:
            the locations name
        description:
            the locations description
        """
        self._name = name
        self._description = description
        self._visited = False
        self._neighbors = {}
        self._npc_list = []
        self._item_list = []

    def get_name(self):
        """gets and returns the locations name

        returns:
        -------
        self._name:
            an instance of _name
        """
        return self._name

    def set_name(self, name):
        """sets the name of a location, raises a ValueError if blank

        parameters:
        ----------
        name:
            the name of a location

        error:
        -----
        ValueError:
            name cannot be blank
        """
        if name == '':
            raise ValueError('Name cannot be blank.')
        self._name = name

    def get_description(self):
        """gets and returns the description of a location

        returns:
        -------
        self._description:
            an instance of _description
        """
        return self._description

    def set_description(self, description):
        """sets the description of a location, raises a ValueError if blank

        parameters:
        ----------
        description:
            the description of a location

        error:
        -----
        ValueError:
            description cannot be blank
        """
        if description == '':
            raise ValueError('Description cannot be blank.')
        self._description = description

    def get_locations(self):
        """gets and returns a locations list of npcs

        returns:
        -------
        self._neighbors:
            an instance of _neighbors
        """
        return self._neighbors

    def add_location(self, direction: str, location: 'Location') -> None:
        """ adds the location into the dictionary with the provided direction string.
        If the string is blank a ValueError is raised, and a KeyError is raised if
        the Location is already in the dictionary.

        parameters:
        ----------
        direction: str:
            a direction ('north', 'south', 'east', 'west')
        location: 'Location':
            the location in the game

        error:
        -----
        ValueError:
            Direction cannot be blank
        KeyError:
            Location is already in the dictionary
        """
        if not direction:
            raise ValueError('Direction cannot be blank.')
        if direction in self._neighbors:
            raise KeyError('Location already exists in the dictionary.')
        self._neighbors[direction] = location

    def add_npc(self, npc: NPC):
        """adds a npc to the locations list

         parameters:
         ----------
         npc: NPC:
            the npc in the game
        """
        self._npc_list.append(npc)

    def del_npc(self, npc: NPC):
        """deletes a npc from a locations list

        parameters:
        ----------
        npc: NPC:
            the npc in the game
        """
        self._npc_list.remove(npc)

    def get_npcs(self) -> list[NPC]:
        """return the list of npcs

        returns:
        -------
        self._npc_list:
            a list of the locations npcs
        """
        return self._npc_list

    def item_list(self, item: Item):
        """adds an item to the locations npc list

        parameters:
        ----------
        item: Item:
            the item in the game
        """
        self._item_list.append(item)

    def get_items(self) -> list[Item]:
        """returns the items in the locations npc list

        returns:
        -------
        self._item_list:
            returns the items
        """
        return self._item_list

    def set_visited(self) -> None:
        """When a location is visited, the variable is changed to True
        """
        self._visited = True

    def get_visited(self) -> bool:
        """checks if the location has been visited

        returns:
        -------
        self._visited:
            an instance of _visited
        """
        return self._visited

    def __str__(self):
        """returns a str describing a location

        returns:
        -------
        str:
            a locations name, and description
        """
        return f"{self._name} - {self._description}"


# noinspection PyProtectedMember
class Game:
    """The game takes place in a world of connected locations. The purpose of the game is to collect
    edible items and then bring them to the elf in the woods behind campus. The elf needs
    500 calories of edible food before it will save GVSU. Each item can have 0 or more calories.
    If a player gives the elf something inedible, the elf will be displeased and
    will teleport the player to a random location in the world.
    The player can only carry 30 pounds at a time, so multiple trips to the elf may be needed. Once
    the elf has enough calories, it will save campus and the game will end.

    Attributes
    ----------
    _create_world():
        creates the world
    _commands: dict
        creates a dictionary that holds the games commands.
        is set equal to the return call from setup_commands.
    _Item_list: lst
        creates a list of all the items the player is holding.
    _weight: int
        creates a variable that keeps track of the current weight
        the player is holding.
    _Location_list: lst
        creates a list of the locations that exist in the game.
    _current_location: str
        keeps track of which location the player is in. is set
        to a random location with random_location.
    _cals_needed: int
        keeps track of how many calories are needed to beat the game.
    _game_progress: bool
        keeps track of whether the game is continuing or ending.
    """

    def __init__(self):
        self._commands = self.setup_commands()
        self._Item_list = []
        self._weight = int(0)
        self._Location_list = []
        self.create_world()
        self._current_location = self.random_location()
        self._cals_needed = int(500)
        self._game_progress = True

    def create_world(self) -> None:
        """creates all the Locations, Items, and NPCs in the game.
        """
        #Creating all locations in the game
        limgrave = Location('Limgrave', 'Limgrave is a lush, expansive section of the '
                            'Tenebrae Demesne. Golden trees and tall grass and bushes' + '\n'
                            'provide plenty of sustenance for the local wildlife, '
                            'that features boars, sheep, goat and rodents in' + '\n'
                            'addition to flying creatures such as eagles and owls. '
                            'More sinister and aggressive wildlife also exists,' + '\n'
                            'and those venturing forth should be '
                            'prepared to combat them.' + '\n')
        weeping_penninsula = Location('Weeping Penninsula', 'The peninsula, to Limgraves '
                                      'south, is named for its '
                                      'unceasing rainfall, redolent of lament.' + '\n')
        liurnia = Location('Liurnia', 'With its shallow waters and vast wetlands, '
                           'the region of Liurnia is beset with the '
                           'gradual sinking of most of its landmass.' + '\n'
                           'With its forests perpetually blanketed in fog, '
                           'eerie sounds of bells can''be heard in '
                           'the distance.' + '\n')
        caelid = Location('Caelid', 'Caelid, known as the locale of the last '
                          'battle between General Radahn and Malenia, Blade' + '\n'
                          'of Miquella, is a vast land consummately marred '
                          'by scarlet rot.' + '\n')
        dragonbarrow = Location('Dragonbarrow', 'The dragons that escaped the scarlet rot '
                                'made nest of the plateau to Caelids north. '
                                'Thus it was named "Dragonbarrow," '
                                'and none dare to enter.' + '\n')
        atlus_plateau = Location('Atlus Plateau', 'Atlus Plateau, a large area filled with '
                                 'tall golden trees, '
                                 'lush golden grass, and many useful materials.' + '\n')
        mt_gelmir = Location('Mt. Gelmir', 'Mt. Gelmir is a volcanic region west '
                             'of the Altus Plateau, ruled over by the '
                             'enigmatic Volcano Manor and their lord, Praetor Rykard.' + '\n'
                             'This region has been'
                             'ravaged, and is home to many grotesque creatures.' + '\n')
        leyndell = Location('Leyndell', 'The Capital City, located at the foot '
                            'of the Erdtree. Despite being partially '
                            'destroyed by the dragon Gransax, it still' + '\n'
                            'holds strong to this day. It houses '
                            'many strong foes, along with the mysterious '
                            'Veiled Monarch, Morgott.' + '\n')
        mountaintops_of_the_giants = Location('Mountaintops of the Giants',
                                              'The fabled domain of the Giants, now in ruins. '
                                              'Devastated after their war against '
                                              'the Erdtree, their corpses lay frozen at the peak, '
                                              'with only the Fire Monks residing close by.' + '\n')

        #Adding locations into the _Location_list
        self._Location_list.append(limgrave)
        self._Location_list.append(weeping_penninsula)
        self._Location_list.append(liurnia)
        self._Location_list.append(caelid)
        self._Location_list.append(dragonbarrow)
        self._Location_list.append(atlus_plateau)
        self._Location_list.append(mt_gelmir)
        self._Location_list.append(leyndell)
        self._Location_list.append(mountaintops_of_the_giants)

        #Adding the neighboring locations for each location
        #Limgrave
        limgrave.add_location('north', liurnia)
        limgrave.add_location('east', caelid)
        limgrave.add_location('south', weeping_penninsula)
        #Caelid
        caelid.add_location('north', dragonbarrow)
        caelid.add_location('west', limgrave)
        #Liurnia
        liurnia.add_location('north', atlus_plateau)
        liurnia.add_location('south', limgrave)
        #Weeping Penninsula
        weeping_penninsula.add_location('north', limgrave)
        #Dragonbarrow
        dragonbarrow.add_location('south', caelid)
        #Atlus Plateau
        atlus_plateau.add_location('north', mt_gelmir)
        atlus_plateau.add_location('east', leyndell)
        atlus_plateau.add_location('south', liurnia)
        #Leyndell
        leyndell.add_location('east', mountaintops_of_the_giants)
        leyndell.add_location('west', atlus_plateau)
        #Mt. Gelmir
        mt_gelmir.add_location('south', atlus_plateau)
        #Mountaintops of the Giants
        mountaintops_of_the_giants.add_location('west', leyndell)

        #Creating items
        boiled_prawn = Item('Boiled Prawn', 'It looks a little green...', calories=62.5, weight=4)
        boiled_crab = Item('Boiled Crab', 'Better than Red Lobster!', calories=62.5, weight=4)
        white_cured_meat = Item('White Cured Meat', 'Mm-mmmm... meat!', calories=62.5, weight=3)
        cooked_meat = Item('Cooked Meat', 'Its a little too rare for me...',
                           calories=62.5, weight=4)
        flask_of_crimson_tears = Item('Flask of Crimson Tears', 'It glows... and tastes good!',
                                      calories=62.5 ,weight=6)
        flask_of_cerulean_tears = Item('Flask of Cerulean Tears', 'The first one was way better.',
                                       calories=62.5, weight=6)
        broken_sword = Item('Broken Sword', 'Belonged to the knights of Miquella... '
                                            'I wonder where they are...',
                            calories=0, weight=6)
        damaged_armor = Item('Damaged Armor', 'This armor belonged to one of Miquellas soldiers '
                                              'as well ...I wonder if ill need it...',
                             calories=0, weight=15)
        boiled_fish = Item('Boiled Fish', 'Did anybody even season this thing?',
                           calories=62.5, weight=4)
        silver_pickled_foul_foot = Item('Silver Pickled Foul Foot', 'W-who would even EAT this?',
                                        calories=62.5, weight=2)
        oil_pot = Item('Oil Pot', 'If only I had a match...',
                       calories=0,weight=7)
        dark_elf_sword = Item('Dark Elf Sword', 'I wonder if there is another way to '
                                                'save the land...',
                              calories=0, weight=30)

        #Adding items to respected locations
        limgrave.item_list(boiled_prawn)
        limgrave.item_list(boiled_crab)
        weeping_penninsula.item_list(white_cured_meat)
        liurnia.item_list(cooked_meat)
        caelid.item_list(flask_of_cerulean_tears)
        caelid.item_list(flask_of_crimson_tears)
        dragonbarrow.item_list(broken_sword)
        dragonbarrow.item_list(damaged_armor)
        atlus_plateau.item_list(boiled_fish)
        atlus_plateau.item_list(dark_elf_sword)
        mt_gelmir.item_list(silver_pickled_foul_foot)
        leyndell.item_list(oil_pot)

        #Creating npcs and setting their message list
        merchant_kale = NPC('Merchant Kale', 'A lonely merchant')
        merchant_kale.npc_message_list(['You are a Tarnished, I can see it. And I can also see... '
                                        'that youre not after my throat.' + '\n'
                                        'Then why not purchase '
                                        'a little something? I am Kale, Purveyor of fine goods.',
                                        'What is it? Still going to purchase something?',
                                        'Good-bye, for now.'])
        witch_hunter_jerren = NPC('Witch Hunter Jerren', 'Known as Catellan Jerren, '
                                  'a harold at the Radahn Festival.' + '\n'
                                  'It is said that Jerren helped the tarnished one defeat Radahn.')
        witch_hunter_jerren.npc_message_list(['Oh, Tarnished, are you? How did you slip inside, '
                                              'with the gate closed?' + '\n'
                                              'Hmph. No matter. If you can fell '
                                              'one of them, you are a champion, in my book. '
                                              'I am Jerren. Foolish old warrior, and witness.' + '\n'
                                              'Incidentally, do you like a good '
                                              'festival, from time to time? Well, '
                                              'its true, this fortress houses only the' + '\n'
                                              'vanquished. But when the stars align, '
                                              'we celebrate. A war festival honoring the '
                                              'last battle and death of General Radahn, '
                                              'the mightiest demigod of the Shattering,' + '\n'
                                              'and bearer of a Great Rune.',
                                              'Well, you are not much fun, are '
                                              'you, chum? No matter.' + '\n'
                                              'One day you will see. That true '
                                              'warriors bask in glory at the festival.',
                                              'Go on, now. This old geezer has not '
                                              'any use for you just yet.'])
        miriel = NPC('Miriel', 'The Church of Vows steward, a huge silver turtle wearing a mitre.')
        miriel.npc_message_list(
            ['Youre Tarnished, arent you? I Welcome you,'
             'to the Church of Vows. I am Miriel, steward of' + '\n'
             'this sacred chamber. My apologies, '
             'for the unseemly state of affairs. '
             'Do you know the origin of this place?',
             'Is there something else?', 'Bye now, '
             'come again.'])
        blaidd = NPC('Blaidd', 'Half man, half wolf, and trusted '
                     'companion and guardian of Ranni the Witch.')
        blaidd.npc_message_list(
            ['Ahh, long time, friend. Blaidd, if you’ve forgotten. '
             'Glad to have you in the service of mistress Ranni',
             'Do you need any assistance?', 'Thats enough '
             'chit-chat for now. Its time we parted ways.'])
        alexander_warrior_jar = NPC('Alexander Warrior Jar',
                                    'Know as Iron Fist Alexander, a large living'
                                    'jar who set out from' + '\n'
                                    'his home one day ins search'
                                    'of adventure, seeking to become'
                                    'a mighty warrior.')
        alexander_warrior_jar.npc_message_list(
            ['Oh my stars Im so happy to see you! I am Alexander, '
             'also known as the Iron Fist.',
             'I left my home in search of adventure, '
             'and it has brought me to you! Please, traveler,' + '\n'
             'duel me! Let us fight until the sun sets!',
             'Hmmm.. thats what I thought. Well, '
             'you know where to find me when you are '
             'looking for a good fight!'])
        elf = NPC('Elf', 'The proclaimed Elf Lord of the Mountains, '
                         'yet to be touched by the Scarlet Rot.' + '\n'
                         'Legend has it, if he is fed enough goods, '
                         'the Lands Between might be saved from the darkness.')
        elf.npc_message_list(['Mmmmmm...hungry...',
                              'Hmph....*stomach gurgles*',
                              'Feed...me...'])

        #Adding npcs to their respected locations
        limgrave.add_npc(merchant_kale)
        weeping_penninsula.add_npc(witch_hunter_jerren)
        liurnia.add_npc(miriel)
        caelid.add_npc(blaidd)
        mt_gelmir.add_npc(alexander_warrior_jar)
        mountaintops_of_the_giants.add_npc(elf)

    def setup_commands(self) -> dict[str, callable]:
        """creates a new dictionary for commands.

        returns:
        -------
        commands:
            a dictionary containing a str(direction) and a callable(location)
        """
        commands = {'talk': self.talk,
                    'help': self.show_help,
                    'meet': self.meet,
                    'take': self.take,
                    'give': self.give,
                    'go': self.go,
                    'items': self.show_items,
                    'look': self.look,
                    'quit': self.quit,
                    'teleport': self.teleport,
                    'inspect': self.inspect,
                    'fight': self.fight}
        return commands

    def random_location(self) -> Location:
        """selects a random location from the locations list and
        returns that location.

        returns:
        -------
        a random location chosen from the list of gae locations
        """
        return random.choice(self._Location_list)

    def play(self) -> None:
        """Core game loop. Prints beginning message, then calls method to list commands.
        Then checks if elf has been fed enough or not fed enough.
        """
        print(Fore.GREEN + 'Welcome to the Lands Between, '
              'a vast domain ruled by Queen Marika the Eternal.' + '\n'
              'In order to successfully save the land, you, '
              'the player, has to scavenge '
              'food from around the world to feed the elf.' + '\n'
              'After the elf has ingested 500 calories '
              'worth of food, he will lift the curse '
              'that was placed upon this domain, saving all '
              'who reside within it.' + '\n')
        self.show_help()

        while self._game_progress:
            if self._cals_needed <= 0:
                print()
                print(Fore.GREEN + 'The elf was fed 500 calories. '
                      'The Lands Between '
                      'have finally been saved. '
                      'Thank you, kind traveler.')
                self._game_progress = False
                break

            if 'Dark Elf Sword' in [item._name for item in self._Item_list]:
                if self._current_location._name == 'Mountaintops of the Giants':
                    print()
                    print(Fore.YELLOW + 'You approach the Elf while he sits '
                          'on his throne. Everything was a lie. '
                          'Feeding the him would only'
                          'destroy the Lands Between, not save it. ' + '\n'
                          'You slowly draw your sword from its holster, '
                          'black flames emerging'
                          'from the blade.' + '\n')
                    print()
                    sleep(2)
                    print(Fore.CYAN + 'Elf:', Fore.RED + 'Ahhhh... so you have '
                          'finally figured me out. This land was always doomed.' + '\n'
                          'I only brought the Scarlet Rot upon its inhabitants '
                          'to save them from the worlds wrath.' + '\n')
                    print()
                    sleep(2)
                    print(Fore.YELLOW + 'You let out a horrifying roar as you'
                          'rush towards the throne, sword in hand. '
                          'The Elf tries to move,'
                          'but your sword reaches him first. The '
                          'moment the blade cuts through his neck, '
                          'the swords black flames seem to become enraged.' + '\n'
                          'You follow through, and his head is gone. '
                          'The flames engulf his body, slowing turning it'
                          'into a dark pile of ash. The Elf is dead.')
                    print()
                    sleep(2)
                    print(Fore.YELLOW + 'You have done it, traveler. '
                          'The Lands Between are finally saved.')
                    self._game_progress = False
                    quit()

            print()
            user_response = input(Fore.RED + 'Input command here: ')
            print()
            tokens = user_response.split()
            if tokens:
                command = tokens[0]
                del(tokens[0])
                target = ' '.join(tokens)

                if command in self._commands:
                    self._commands[command](target)
                else:
                    print(Fore.RED + 'Please choose a valid command.')
            else:
                print(Fore.RED + 'Please enter a command.')

        if self._cals_needed > 0:
            print(Fore.RED + 'The elf has not been fed enough. For the sake of the land,'
                             'find more food.')

        quit()

    def show_help(self, target=None):
        """prints a help message along with all commands from dictionary.
        """
        now = datetime.datetime.now()
        print(Fore.YELLOW + 'Current time:', now.strftime(Fore.YELLOW + "%Y-%m-%d %H:%M:%S"))
        print(Fore.YELLOW + 'List of available commands:', ', '.join(self._commands.keys()))

    def inspect(self, target):
        """if the target item is in your inventory,
        it prints out its name,
        description, weight, and calories.
        prints a statement if the item is not in your inventory.

        parameters:
        ----------
        target:
            the item you wish to look at
        """
        item = None
        for i in self._Item_list:
            if i._name == target:
                item = i
                break
        if item:
            print(Fore.CYAN + f'{item._name}: {Fore.YELLOW + item._description}')
            print(Fore.CYAN + f'Item weight: {Fore.YELLOW + str(item._weight)}')
            print(Fore.CYAN + f'Item calories: {Fore.YELLOW + str(item._calories)}')
        else:
            print(f'{Fore.YELLOW + target}', Fore.RED + 'not in inventory.')

    def fight(self, target):
        """if the target is in the location,
        you can fight them. If you have the Dark Elf Sword,
        you can kill npcs and finish the game by killing the elf

        parameters:
        ----------
        target:
            the target npc
        """
        loc_npc = None
        for npc in self._current_location.get_npcs():
            if npc._name == target:
                loc_npc = npc
                break
        if loc_npc and 'Dark Elf Sword' in [item._name for item in self._Item_list]:
            print(f'{Fore.BLUE + target}', '' + Fore.RED + 'I challenge you to a fight '
                                                           'to the death.')
            print()
            sleep(2)
            print(f'{Fore.BLUE + target}:', Fore.MAGENTA + 'You dare wish to fight me? '
                                                           'I will kill you!')
            print()
            sleep(2)
            print(f'{Fore.BLUE + target}', Fore.RED + 'has been slain.')
            self._current_location.del_npc(loc_npc)
            return

        if loc_npc and 'Dark Elf Sword' not in [item._name for item in self._Item_list]:
            print(f'{Fore.BLUE + target}', '' + Fore.RED + 'I challenge you to a '
                                                           'fight to the death.')
            print()
            sleep(2)
            print(f'{Fore.BLUE + target}:', Fore.MAGENTA + '*Pulls a small knife out of'
                  'their boot*...never bring only your fists to a knife fight.')
            print()
            sleep(2)
            print(f'{Fore.BLUE + target}', Fore.RED + 'has killed you in battle. '
                  'You were sent to a random location.')
            self._current_location = self.random_location()
        else:
            print(f'{Fore.BLUE + target}', Fore.RED + 'is not in this location.')

    def teleport(self, target):
        """if a location has been discovered, the player can teleport to said
        location from any other discovered location

        parameters:
        ----------
        target:
            the location we are trying to teleport to
        """
        target_location = None
        for loc in self._Location_list:
            if loc._name == target:
                target_location = loc
                break
        if target_location:
            if target_location == self._current_location:
                print(Fore.RED + 'You are already in this location.')
            elif target in [loc._name for loc in self._Location_list]:
                if target_location._visited is True:
                    self._current_location._neighbors['teleport'] = target_location
                    self._current_location = target_location
                    print(Fore.GREEN + f'You have teleported to '
                          f'{Fore.YELLOW + target_location._name}')
            else:
                print(Fore.RED + 'this location has not been discovered.')
        else:
            print(Fore.RED + 'That is not a valid location to teleport to.')

    def talk(self, target) -> None:
        """checks if NPC is in the room, if so it calls the NPC's get_message.

        parameters:
        ----------
        target:
            the npc we are trying to talk to
        """
        loc_npc = None
        for npc in self._current_location.get_npcs():
            if npc._name == target:
                loc_npc = npc
                break
        if loc_npc:
            message = loc_npc.get_message_number()
            print(f'{Fore.BLUE + target}: {Fore.MAGENTA + message}')
        else:
            print(f'{Fore.BLUE + target}', Fore.RED + 'is not in this location.')

    def meet(self, target) -> None:
        """checks if NPC is in the room, if so asks for NPC description.

        parameters:
        ----------
        target:
            the npc we are trying to meet
        """
        meet_npc = None
        for npc in self._current_location.get_npcs():
            if npc._name == target:
                meet_npc = npc
                break
        if meet_npc:
            description = meet_npc.get_description()
            print(f'{Fore.BLUE + target}: {Fore.MAGENTA + description}')
        else:
            print(f'{Fore.BLUE + target}', Fore.RED + 'is not in this location.')

    def take(self, target) -> None:
        """if target is in the room, removes it from the rooms inventory and adds
        it to the users inventory, along with the weight.

        parameters:
        ----------
        target:
            the item we are trying to take
        """
        loc_item = None
        for item in self._current_location.get_items():
            if item._name == target:
                loc_item = item
                break
        if loc_item:
            if self._current_location._name == 'Mountaintops of the Giants':
                if loc_item._calories > 0:
                    print(f'{Fore.YELLOW + target}', Fore.RED + 'has already been eaten '
                          'by the elf...what a shame...')
                    return
            print(f'{Fore.YELLOW + target}', Fore.GREEN + 'is now in your inventory.')
            self._Item_list.append(loc_item)
            self._current_location.get_items().remove(loc_item)
            if isinstance(loc_item._weight,int):
                self._weight += loc_item._weight
        else:
            print(f'{Fore.YELLOW + target}', Fore.RED + 'not found in this location.')

    def give(self, target) -> None:
        """removes target item from users inventory and adds it to the current locations
        inventory and decreases players weight. If the current location is in the woods,
        it checks if the item is edible. If it is, reduce the amount of calories needed.
        If it was not edible, transport the player to a new location by setting the
        current location to the return from random_location.

        parameters:
        ----------
        target:
            the item we are trying to give
        """
        for item in self._Item_list:
            if item._name == target:
                print(Fore.GREEN + f'You have dropped {Fore.YELLOW + target}')
                self._current_location._item_list.append(item)
                self._Item_list.remove(item)
                self._weight -= item._weight

                if self._current_location._name == 'Mountaintops of the Giants':
                    if item._calories > 0 and item._name == target:
                        self._cals_needed -= item._calories
                        print(Fore.GREEN + f'Elf calories needed: '
                              f'{Fore.YELLOW + str(self._cals_needed)}')
                    else:
                        print()
                        print(Fore.RED + 'The air grows thin and the sky turns dark...'
                              'everything goes black.' + '\n'
                              'You wake up in a pile of ash...where are you?')
                        self._current_location = self.random_location()
                return
        print(f'{Fore.YELLOW + target}', Fore.RED + 'is not in your inventory.')

    def go(self, target) -> None:
        """Sets current location's visited status to True. Checks if players weight is over 30;
        prints a message and returns if so. Otherwise, checks if provided direction exists
        in current locations neighbor dictionary. If so, sets current location equal to
        the value from the dictionary.

        parameters:
        ----------
        target:
            the location we are trying to go to
        """
        self._current_location.visited = True
        if self._weight > 30:
            print(Fore.RED + 'You are carrying too much. You must drop something.')
            return
        if target in self._current_location._neighbors:
            self._current_location = self._current_location._neighbors[target]
            print(Fore.GREEN + f'You have arrived in {Fore.YELLOW + self._current_location._name}')
            print()
            self.look()
        else:
            print(f'{Fore.YELLOW + target}', Fore.RED + 'is not a valid location.')

    def show_items(self, args: str = None) -> None:
        """prints out all the items the player is carrying,
        along with the cumulative weight carried

        parameters:
        ----------
        args: str = None:
            used to make it callable with the same syntax as other commands
        """
        items = [item._name for item in self._Item_list]
        print(Fore.CYAN + "You are carrying:" if items else Fore.RED +
              "You are not carrying any items.")
        for item in items:
            print(Fore.YELLOW + "-", Fore.YELLOW + item)
        print(Fore.CYAN + "Current weight:", Fore.YELLOW +
              str(sum(item._weight for item in self._Item_list)),
              Fore.YELLOW + "lb")
        print(Fore.CYAN + "Current Calories Held:",
              Fore.YELLOW + str(sum(item._calories for item in self._Item_list)))

    def look(self, args: str = None) -> None:
        """prints the current location, a list of items in the location or a message
        indicating that there are no items, a list of NPCs in the room or the message
        "You are alone.", and a list of directions in which the player can go. If a
        location has been visited previously, print the direction and location. Otherwise,
        simply print the direction.

        parameters:
        ----------
        args: str = None:
            used to make it callable with the same syntax as other commands
        """
        self._current_location.set_visited()
        print(Fore.CYAN + f'{self._current_location._name}: '
              f'{Fore.GREEN + self._current_location._description}')
        print(Fore.CYAN + 'Location items:')
        if len(self._current_location._item_list) > 0:
            for item in self._current_location._item_list:
                print(Fore.YELLOW + f'- {Fore.YELLOW + item._name}')
        else:
            print(Fore.RED + 'The location currently has no items.')
        print(Fore.CYAN + 'Location npc(s):')
        if len(self._current_location._npc_list) > 0:
            for npc in self._current_location._npc_list:
                print(Fore.YELLOW + f'- {Fore.YELLOW + npc._name}')
        else:
            print(Fore.RED + 'You are alone.')

        print(Fore.CYAN + 'You can travel in the following directions:')
        for direction in self._current_location._neighbors:
            neighbor = self._current_location._neighbors[direction]
            if neighbor._visited:
                print(Fore.YELLOW + f'- {Fore.YELLOW + direction} '
                      f'to {Fore.YELLOW + neighbor._name}')
            else:
                print(Fore.YELLOW + f'- {Fore.YELLOW + direction}')

        print(Fore.CYAN + 'Locations you can teleport to:')
        teleport_loc = [loc for loc in self._Location_list
                        if loc != self._current_location
                        and loc.get_visited()]
        if teleport_loc:
            for loc in teleport_loc:
                print(Fore.YELLOW + f'- {Fore.YELLOW + loc._name}')
        else:
            print(Fore.RED + 'There is no location to teleport to.')

    def quit(self, args: str = None) -> None:
        """prints a failure message and quits the game

        parameters:
        ----------
        args: str = None:
            used to make it callable with the same syntax as other commands
        """
        print(Fore.RED + 'Game over.')
        exit(0)

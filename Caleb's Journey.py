from textwrap import dedent
from sys import exit


# Game title
print('\n' + '-' * 15, 'Caleb And The Dark Forest', '-' * 15 + '\n')
# Game intro
print(dedent('''
    Caleb is a farmer. He has a cow, Freddy, and a dog, Heko.
    One day, a typhoon destroyed his village; where he lived.
    So he started to move on to a new place. He passed the 
    plain and walked into the forest; The "Hermon" forest with
    the strangest creatures, only to find himself surrounded
    by tall trees and frightening sounds. Actually, a sound 
    made Freddy, his cow, scared; so he started "Mowing" and
    made "Gethara" awake. 
    He started roaring and here the story began...\n
'''))

# Main flow of the game
class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        scene = self.scene_map.opening_scene()
        end_game = self.scene_map.next_scene('win')

        while scene != end_game:
            scene = self.scene_map.next_scene('forest').enter_scene()
            



# Changing scenes
class Scene(object):

    def enter_scene(self):
        print("Used for other scenes.")
        exit(1)

# Win scenarios
class WinScenario(Scene):
    
    def enter_scene(self):
        print("That was something! Congratulations!\n")
        return True
    

class DeathScenario(Scene):
    
    def enter_scene(self):
        print("That was a horrible death. Didn't know you were this bad!\n")
        exit(1)
    


# Powers to defeat or increase health
class Powers(object):
    caleb_properties = {
            'milk': 2000,
            'butter': 1000,
            'wheat': 3000,
        }

    healths = {'caleb': 1000, 'gethara': 1000}
    caleb_money = {'current_money': 500}
    weapons = {'sickle': 0, 'poisoned_leaves': 0, 'hard_stones': 0}
    
    def sell(self):
        print('So you want to get some money, cool!\n')

        print(dedent('''
            1. Milk (made by Freddy)
            2. Butter (Freddy dancing!)
            3. Wheat (you are a farmer)\n
        '''))
        to_sell = int(input('>>> '))
        
        if to_sell == 1 and Powers.caleb_properties['milk'] > 260:
            Powers.caleb_properties['milk'] -= 250
            Powers.caleb_money['current_money'] += 250
                    
        elif to_sell == 2 and Powers.caleb_properties['butter'] > 310:
            Powers.caleb_properties['butter'] -= 300
            Powers.caleb_money['current_money'] += 300

        
        elif to_sell == 3 and Powers.caleb_properties['wheat'] > 210:
            Powers.caleb_properties['wheat'] -= 200
            Powers.caleb_money['current_money'] += 200

        else:
            "No such properties were found. Try again."
            sell()
        print(dedent(
            '''Milk: {}
               Butter: {}
               Wheat: {} 
            \n''').format(Powers.caleb_properties['milk'], Powers.caleb_properties['butter'], Powers.caleb_properties['wheat']))
        
        print(dedent('''
            Caleb's Health: {}
            Gethara's Health: {}
        \n''').format(Powers.healths['caleb'], Powers.healths['gethara']))
        
        print(dedent('''
            Caleb's Money: {} 
        \n''').format(Powers.caleb_money['current_money']))

        print(dedent('''
            Weapons:
              Sickle: {}
              Poisoned Leaves: {}
              Hard Stones: {}
        \n''').format(Powers.weapons['sickle'], Powers.weapons['poisoned_leaves'], Powers.weapons['hard_stones']))


    def buy(self):
        print('So you want to level up your power against Gethara!\n')

        print(dedent('''
            1. Sickle (sharpness!)
            2. Poisoned leaves (well, it's Hermon!)
            3. Hard stones (to throw!)
        '''))
        to_buy = int(input('>>> '))

        if to_buy == 1 and caleb_money['current_money'] > 0:
            caleb_money['current_money'] -= 800
            weapons['sickle'] += 100
        
        elif to_buy == 2 and caleb_money['current_money'] > 0:
            caleb_money['current_money'] -= 1000
            weapons['sickle'] += 200


        elif to_buy == 2 and caleb_money['current_money'] > 0:
            caleb_money['current_money'] -= 1200
            weapons['sickle'] += 300
        
        else:
            print("No such thing to buy...")
            buy()

    def attack(self):
        print(dedent(''' 
            Which weapon do you want to use?
            1. Sickle
            2. Poisoned leaves
            3. Hard stones
        '''))

        weapon_to_use = int(input('>>> '))

        if weapon_to_use == 1 and weapons['sickle'] > 100:
            weapons['sickle'] -= 100
            healths['gethara'] -= 50

        elif weapon_to_use == 2 and weapons['poisoned_leaves'] > 100:
            weapons['poisoned_leaves'] -= 200
            healths['gethara'] -= 70

        elif weapon_to_use == 3 and weapons['hard_stone'] > 100:
            weapons['poisoned_leaves'] -= 300
            healths['gethara'] -= 120

        else:
            print('Hmm...CHOOSE a damn weapon!')
            attack()
    
# Forest scene
class Forest(Scene):
    
    def enter_scene(self):
        print(dedent('''
                Ha! what are YOU doing in here...filthy little animals? (wandering, running, enjoying)\n
            '''))
        caleb_answer = input('>>> ')
        if caleb_answer == "wandering":
            print(dedent('''
                Hmmmm...This is MY territory...None of you are
                allowed to wander here. So...I am going to
                kill you all. Yaha...here the battle begins!\n
            '''))
            print('-' * 15, 'Choose what to do', '-' * 15 + '\n')
            exit_flag = False
            while exit_flag != True:
                print(dedent(''' 
                    1. Sell
                    2. Buy
                    3. Attack
                '''))
                choice = int(input('>>> '))
                char_power = Powers()

                if choice == 1:
                    char_power.sell()
                
                elif choice == 2:
                    char_power.buy()
                
                elif choice == 3:
                    char_power.attack()
                
                else:
                    print("Wrong choice...Open your eyes!")
                    exit_flag = False




        elif caleb_answer == "running":
            ...
        elif caleb_answer == "enjoyiong":
            ...
        else:
            print("Gara weyta urada opina?! (in simple: what the hell are you talking about?\n)")
            enter_scene()    
        


# Village scene
class Village(Scene):
    
    def enter_scene(self):
        ...

# What each character is able to do
class Character(Powers):

    def sell(self):
        return super().sell()

    def buy(self):
        return super().buy()    

    def attack(self):
        return super().attack()


# Define scenes
class GameMap(object):

    game_scenes = {'forest': Forest(), 'village': Village(), 'win': WinScenario(), 'death': DeathScenario()}

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        scene = GameMap.game_scenes.get(scene_name)
        return scene

    def opening_scene(self):
        return self.next_scene(self.start_scene)

scene_play = GameMap('Forest')
game_play = Engine(scene_play)
game_play.play()
from textwrap import dedent
from sys import exit
import random

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
        next_map = GameMap(self)
        next_map.next_scene('village').enter_scene()
        exit(0)
    

class DeathScenario(Scene):
    
    def enter_scene(self):
        print("That was a horrible death. Didn't know you were this bad!\n")
        exit(1)
    

# Powers to defeat or increase health
class Powers(object):
    
    caleb_properties = {
            'milk': 2500,
            'butter': 1800,
            'wheat': 3000,
        }

    healths = {'caleb': 1000, 'gethara': 1000}
    caleb_money = {'current_money': 500}
    weapons = {'sickle': 0, 'poisoned_leaves': 0, 'hard_stones': 0}
    heko_freddy_energy = {'heko': 250, 'freddy': 350}
    enemy_weapons = ['magic_punch', 'air_kick', 'poisoned_blow']
    
    def enemy_attack(self, weapon):
        if Powers.healths['caleb'] < 110:
            Powers.healths['caleb'] = 0
            return 'win'

        if weapon == 'magic_punch':
            Powers.healths['caleb'] -= 90

        elif weapon == 'air_kick':
            Powers.healths['caleb'] -= 100
        
        elif weapon == 'poisoned_blow':
            Powers.healths['caleb'] -= 120

        print(dedent(f"Gethara attacked using {weapon}!\n"))


    def enemy_random_attack(self):
        weapon = random.choice(Powers.enemy_weapons)
        return weapon
    

    def progress_bar(self, val, label, max_size):
        bar_size = 20
        j = val / max_size
        bar = '█' * int(bar_size * j)
        bar = bar + '-' * int(bar_size * (1 - j))
        print(f"{label.ljust(10)} | [{bar:{bar_size}s}] {int(100 * j)}%")


    def show_status(self):
        print(dedent('Properties:\n'))     
        self.progress_bar(Powers.caleb_properties['milk'], 'Milk', 2500)
        self.progress_bar(Powers.caleb_properties['butter'], 'Butter', 1800)
        self.progress_bar(Powers.caleb_properties['wheat'], 'Wheat', 3000)
        
        print(dedent('\n\nHealth:\n'))
        self.progress_bar(Powers.healths['caleb'], 'Caleb', 1000)
        self.progress_bar(Powers.healths['gethara'], 'Gethara', 1000)
        
        print(dedent('''\n
            Money:\n
            Caleb: {} 
         \n''').format(Powers.caleb_money['current_money']))   

        print(dedent('''
            Weapons:\n
            Sickle: {}
            Poisoned Leaves: {}
            Hard Stones: {}
         \n''').format(Powers.weapons['sickle'], Powers.weapons['poisoned_leaves'], Powers.weapons['hard_stones']))

        print(dedent('Friend\'s Energy Level:\n'))
        if Powers.heko_freddy_energy['heko'] == 'dead':
            print(dedent(f"Heko: {Powers.heko_freddy_energy['heko']}"))
        
        else:
            self.progress_bar(Powers.heko_freddy_energy['heko'], 'Heko', 250)
        
        if Powers.heko_freddy_energy['freddy'] == 'dead':
            print(dedent(f"Freddy: {Powers.heko_freddy_energy['freddy']}"))
        
        else:
            self.progress_bar(Powers.heko_freddy_energy['freddy'], 'Freddy', 350)

    
    def sell(self):
        print(dedent('So you want to get some money, cool!\n'))

        print(dedent('''
            1. Milk (made by Freddy)
            2. Butter (Freddy dancing!)
            3. Wheat (you are a farmer)
            4. Back\n
        '''))
        to_sell = input('>>> ')
        
        if to_sell == "1" and Powers.caleb_properties['milk'] >= 250:
            Powers.caleb_properties['milk'] -= 250
            Powers.caleb_money['current_money'] += 250
                    
        elif to_sell == "2" and Powers.caleb_properties['butter'] >= 300:
            Powers.caleb_properties['butter'] -= 300
            Powers.caleb_money['current_money'] += 300

        
        elif to_sell == "3" and Powers.caleb_properties['wheat'] >= 200:
            Powers.caleb_properties['wheat'] -= 200
            Powers.caleb_money['current_money'] += 200

        elif to_sell == "4":
            return

        else:
            print(dedent('No such properties were found. Try again.\n'))
            self.sell()


    def buy(self):
        print('So you want to level up your power against Gethara!\n')

        print(dedent('''
            1. Sickle (sharpness!)
            2. Poisoned leaves (well, it's Hermon!)
            3. Hard stones (to throw!)
            4. Back\n
        '''))
        to_buy = input('>>> ')

        if to_buy == "1" and Powers.caleb_money['current_money'] >= 800:
            Powers.caleb_money['current_money'] -= 800
            Powers.weapons['sickle'] += 100
        
        elif to_buy == "2" and Powers.caleb_money['current_money'] >= 1000:
            Powers.caleb_money['current_money'] -= 1000
            Powers.weapons['poisoned_leaves'] += 200


        elif to_buy == "3" and Powers.caleb_money['current_money'] >= 1200:
            Powers.caleb_money['current_money'] -= 1200
            Powers.weapons['hard_stones'] += 300
        
        elif to_buy == "4":
            return

        else:
            print(dedent("Not enough money to buy...\n"))
            self.buy()


    def attack(self):

        # enemy = Powers()
        # enemy.enemy_attack(enemy.enemy_random_attack())

        print(dedent(''' 
            Which weapon do you want to use?
            1. Sickle
            2. Poisoned leaves
            3. Hard stones
            4. Freddy's kick
            5. Heko's bark
            6. Back
        '''))

        weapon_to_use = input('>>> ')
        
        if Powers.healths['gethara'] == 0:
            return 'win'

        if weapon_to_use == "1" and Powers.weapons['sickle'] >= 100:
            Powers.weapons['sickle'] -= 100
            
            if Powers.healths['gethara'] >= 70:
                Powers.healths['gethara'] -= 70

            else:
                Powers.healths['gethara'] = 0
            

        elif weapon_to_use == "2" and Powers.weapons['poisoned_leaves'] >= 200:
            Powers.weapons['poisoned_leaves'] -= 200
            
            if Powers.healths['gethara'] >= 100:
                Powers.healths['gethara'] -= 100

            else:
                Powers.healths['gethara'] = 0
            


        elif weapon_to_use == "3" and Powers.weapons['hard_stones'] >= 300:
            Powers.weapons['hard_stones'] -= 300
            
            if Powers.healths['gethara'] >= 150: 
                Powers.healths['gethara'] -= 150

            else:
                Powers.healths['gethara'] = 0

        elif weapon_to_use == "4":
            if Powers.heko_freddy_energy['freddy'] == 'dead':
                print('He already sacrificed himself!\n')
                return
            
            elif Powers.heko_freddy_energy['freddy'] >= 90:
                Powers.heko_freddy_energy['freddy'] -= 100
            
            else:
                print('Freddy could not resist. He died.\n')
                Powers.heko_freddy_energy['freddy'] = 'dead'

            if Powers.healths['gethara'] >= 90: 
                Powers.healths['gethara'] -= 90

            else:
                Powers.healths['gethara'] = 0

        elif weapon_to_use == "5":
            if Powers.heko_freddy_energy['heko'] == 'dead':
                print('He already sacrificed himself!\n')
                return

            elif Powers.heko_freddy_energy['heko'] >= 100:
                Powers.heko_freddy_energy['heko'] -= 90

            else:
                print('Heko could not resist anymore. He\'s dead now.')
                Powers.heko_freddy_energy['heko'] = 'dead'

            if Powers.healths['gethara'] >= 60:
                Powers.healths['gethara'] -= 60

            else:
                Powers.healths['gethara'] = 0
       
        elif weapon_to_use == "6":
            return

        else:
            print('Hmm...CHOOSE the right weapon or he\'s gonna kill you!')
            self.attack()
        
        if Powers.healths['gethara'] == 0:
            return 'win'

        elif Powers.healths['caleb'] == 0:
             return 'death'

    

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
            print('-' * 15, 'Initial Resources', '-' * 15 + '\n')
            exit_flag = False
            
            while exit_flag != True:
                char_power = Powers()
                result = ""
                char_power.show_status()
                print('\n' + '-' * 15, 'Choose what to do', '-' * 15 + '\n')    
                
                print(dedent(''' 
                    1. Sell
                    2. Buy
                    3. Attack
                '''))
                choice = int(input('>>> '))
                

                if choice == 1:
                    char_power.sell()
                
                elif choice == 2:
                    char_power.buy()
                
                elif choice == 3:
                    enemy = Powers()
                    enemy.enemy_attack(enemy.enemy_random_attack())
                    result = char_power.attack()

                else:
                    print("Wrong choice...Open your eyes!")
                    exit_flag = False

                if result == 'win':
                    WinScenario().enter_scene()

                elif result == 'death':
                    DeathScenario.enter_scene()

        elif caleb_answer == "running":
            ...
        
        elif caleb_answer == "enjoyiong":
            ...
        
        else:
            print("Gara weyta urada opina?! (in simple: what the hell are you talking about?)\n")
            self.enter_scene()    
        


# Village scene
class Village(Scene):
    
    def enter_scene(self):
        print(dedent('''
            Well, caleb won. You halped him a lot!
            All "Hermon's" creatures will listen to
            him now. With their super powers, he
            is able to rebuild his village, and he
            does so. He is not a farmer anymore. He
            has even chosen a name for himself, Gethara.  
        \n'''))


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
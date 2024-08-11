from flask import Flask, render_template_string, redirect, url_for
from dataclasses import dataclass
import operator
import random
import colorama
from colorama import Fore, Back, Style


# Define the players


def game():
    @dataclass
    class Player:
        name: str
        skill: int
        random: int
        gender: str
        chart: list
        placement: int
        era: int
        eliminatedFirst: bool
        pic: str
        elimPic: str
    player_1 = Player('Derrick', 80, 0, 'M', [], 0, 1, False, 
                  '<img src="https://live.staticflickr.com/65535/53914826951_132f681c41_m.jpg" alt="Game Image" width="120" height="120" />', 
                  '<img src="https://live.staticflickr.com/65535/53914826951_132f681c41_m.jpg" alt="Game Image" width="120" height="120" style="filter: grayscale(100%);" />')
    player_2 = Player('Mark', 60, 0, 'M', [], 0, 1, False, 
                 '<img src="https://live.staticflickr.com/65535/53913941667_3d2660ee6d_m.jpg" alt="Game Image" width="120" height="120" />', 
                 '<img src="https://live.staticflickr.com/65535/53913941667_3d2660ee6d_m.jpg" alt="Game Image" width="120" height="120" style="filter: grayscale(100%);" />')
    player_3 = Player('CT', 90, 0, 'M', [], 0, 1, False, 
                 '<img src="https://live.staticflickr.com/65535/53913941762_26db92626d_m.jpg" alt="Game Image" width="120" height="120" />', 
                 '<img src="https://live.staticflickr.com/65535/53913941762_26db92626d_m.jpg" alt="Game Image" width="120" height="120" style="filter: grayscale(100%);" />')
    player_4 = Player('Brad', 80, 0, 'M', [], 0, 1, False, 
                 '<img src="https://live.staticflickr.com/65535/53915074283_0700298b2d_m.jpg" alt="Game Image" width="120" height="120" />', 
                 '<img src="https://live.staticflickr.com/65535/53915074283_0700298b2d_m.jpg" alt="Game Image" width="120" height="120" style="filter: grayscale(100%);" />')
    player_5 = Player('Darrell', 80, 0, 'M', [], 0, 1, False, 
                 '<img src="https://live.staticflickr.com/65535/53915177519_8b1f00300a_m.jpg" alt="Game Image" width="120" height="120" />', 
                 '<img src="https://live.staticflickr.com/65535/53915177519_8b1f00300a_m.jpg" alt="Game Image" width="120" height="120" style="filter: grayscale(100%);" />')
    player_6 = Player('Brandon', 60, 0, 'M', [], 0, 2, False, 
                 '<img src="https://live.staticflickr.com/65535/53915276930_6b866566d2_m.jpg" alt="Game Image" width="120" height="120" />', 
                 '<img src="https://live.staticflickr.com/65535/53915276930_6b866566d2_m.jpg" alt="Game Image" width="120" height="120" style="filter: grayscale(100%);" />')
    player_7 = Player('Nehemiah', 60, 0, 'M', [], 0, 2, False, 
                 '<img src="https://live.staticflickr.com/65535/53915177454_4281b8f90d_m.jpg" alt="Game Image" width="120" height="120" />', 
                 '<img src="https://live.staticflickr.com/65535/53915177454_4281b8f90d_m.jpg" alt="Game Image" width="120" height="120" style="filter: grayscale(100%);" />')
    player_8 = Player('Bananas', 90, 0, 'M', [], 0, 2, False, 
                 '<img src="https://live.staticflickr.com/65535/53914826971_a80f63b477_m.jpg" alt="Game Image" width="120" height="120" />', 
                 '<img src="https://live.staticflickr.com/65535/53914826971_a80f63b477_m.jpg" alt="Game Image" width="120" height="120" style="filter: grayscale(100%);" />')
    player_9 = Player('Derek', 70, 0, 'M', [], 0, 2, False, 
                 '<img src="https://live.staticflickr.com/65535/53915276905_06df120bf1_m.jpg" alt="Game Image" width="120" height="120" />', 
                 '<img src="https://live.staticflickr.com/65535/53915276905_06df120bf1_m.jpg" alt="Game Image" width="120" height="120" style="filter: grayscale(100%);" />')
    player_10 = Player('Ryan', 50, 0, 'M', [], 0, 2, False, 
                  '<img src="https://live.staticflickr.com/65535/53915177424_0e2ba6f595_m.jpg" alt="Game Image" width="120" height="120" />', 
                  '<img src="https://live.staticflickr.com/65535/53915177424_0e2ba6f595_m.jpg" alt="Game Image" width="120" height="120" style="filter: grayscale(100%);" />')
    player_11 = Player('Cory', 70, 0, 'M', [], 0, 3, False, 
                  '<img src="https://live.staticflickr.com/65535/53914826961_d0e9522513_m.jpg" alt="Game Image" width="120" height="120" />', 
                  '<img src="https://live.staticflickr.com/65535/53914826961_d0e9522513_m.jpg" alt="Game Image" width="120" height="120" style="filter: grayscale(100%);" />')
    player_12 = Player('Devin', 80, 0, 'M', [], 0, 3, False, 
                  '<img src="https://live.staticflickr.com/65535/53913941747_65f0d9931a_m.jpg" alt="Game Image" width="120" height="120" />', 
                  '<img src="https://live.staticflickr.com/65535/53913941747_65f0d9931a_m.jpg" alt="Game Image" width="120" height="120" style="filter: grayscale(100%);" />')
    player_13 = Player('Jordan', 90, 0, 'M', [], 0, 3, False, 
                  '<img src="https://live.staticflickr.com/65535/53914826926_f5254b2911_m.jpg" alt="Game Image" width="120" height="120" />', 
                  '<img src="https://live.staticflickr.com/65535/53914826926_f5254b2911_m.jpg" alt="Game Image" width="120" height="120" style="filter: grayscale(100%);" />')
    player_14 = Player('Leroy', 80, 0, 'M', [], 0, 3, False, 
                  '<img src="https://live.staticflickr.com/65535/53915177479_70a18e73ea_m.jpg" alt="Game Image" width="120" height="120" />', 
                  '<img src="https://live.staticflickr.com/65535/53915177479_70a18e73ea_m.jpg" alt="Game Image" width="120" height="120" style="filter: grayscale(100%);" />')
    player_15 = Player('Tony', 60, 0, 'M', [], 0, 3, False, 
                  '<img src="https://live.staticflickr.com/65535/53915276820_7f6199bab6_m.jpg" alt="Game Image" width="120" height="120" />', 
                  '<img src="https://live.staticflickr.com/65535/53915276820_7f6199bab6_m.jpg" alt="Game Image" width="120" height="120" style="filter: grayscale(100%);" />')
    player_16 = Player('Horacio', 70, 0, 'M', [], 0, 4, False, 
                  '<img src="https://live.staticflickr.com/65535/53915074268_742747cb23_m.jpg" alt="Game Image" width="120" height="120" />', 
                  '<img src="https://live.staticflickr.com/65535/53915074268_742747cb23_m.jpg" alt="Game Image" width="120" height="120" style="filter: grayscale(100%);" />')
    player_17 = Player('Josh', 50, 0, 'M', [], 0, 4, False, 
                  '<img src="https://live.staticflickr.com/65535/53915276880_7432ffa775_m.jpg" alt="Game Image" width="120" height="120" />', 
                  '<img src="https://live.staticflickr.com/65535/53915276880_7432ffa775_m.jpg" alt="Game Image" width="120" height="120" style="filter: grayscale(100%);" />')
    player_18 = Player('Kyland', 70, 0, 'M', [], 0, 4, False, 
                  '<img src="https://live.staticflickr.com/65535/53915074223_92ab9e7f4d_m.jpg" alt="Game Image" width="120" height="120" />', 
                  '<img src="https://live.staticflickr.com/65535/53915074223_92ab9e7f4d_m.jpg" alt="Game Image" width="120" height="120" style="filter: grayscale(100%);" />')
    player_19 = Player('Paulie', 70, 0, 'M', [], 0, 4, False, 
                  '<img src="https://live.staticflickr.com/65535/53915177449_35fec241a3_m.jpg" alt="Game Image" width="120" height="120" />', 
                  '<img src="https://live.staticflickr.com/65535/53915177449_35fec241a3_m.jpg" alt="Game Image" width="120" height="120" style="filter: grayscale(100%);" />')
    player_20 = Player('Theo', 70, 0, 'M', [], 0, 4, False, 
                  '<img src="https://live.staticflickr.com/65535/53915276815_b85c5216d7_m.jpg" alt="Game Image" width="120" height="120" />', 
                  '<img src="https://live.staticflickr.com/65535/53915276815_b85c5216d7_m.jpg" alt="Game Image" width="120" height="120" style="filter: grayscale(100%);" />')
    player_21 = Player('Rachel', 90, 0, 'F', [], 0, 1, False, 
                  '<img src="https://live.staticflickr.com/65535/53915177444_1557dbc24c_m.jpg" alt="Game Image" width="120" height="120" />', 
                  '<img src="https://live.staticflickr.com/65535/53915177444_1557dbc24c_m.jpg" alt="Game Image" width="120" height="120" style="filter: grayscale(100%);" />')
    player_22 = Player('Jodi', 70, 0, 'F', [], 0, 1, False, 
                  '<img src="https://live.staticflickr.com/65535/53914826946_611e719439_m.jpg" alt="Game Image" width="120" height="120" />', 
                  '<img src="https://live.staticflickr.com/65535/53914826946_611e719439_m.jpg" alt="Game Image" width="120" height="120" style="filter: grayscale(100%);" />')
    player_23 = Player('Katie', 50, 0, 'F', [], 0, 1, False, 
                  '<img src="https://live.staticflickr.com/65535/53913941707_6fc59b419a_m.jpg" alt="Game Image" width="120" height="120" />', 
                  '<img src="https://live.staticflickr.com/65535/53913941707_6fc59b419a_m.jpg" alt="Game Image" width="120" height="120" style="filter: grayscale(100%);" />')
    player_24 = Player('Aneesa', 60, 0, 'F', [], 0, 1, False, 
                  '<img src="https://live.staticflickr.com/65535/53913941792_91062239ed_m.jpg" alt="Game Image" width="120" height="120" />', 
                  '<img src="https://live.staticflickr.com/65535/53913941792_91062239ed_m.jpg" alt="Game Image" width="120" height="120" style="filter: grayscale(100%);" />')
    player_25 = Player('Tina', 60, 0, 'F', [], 0, 1, False, 
                  '<img src="https://live.staticflickr.com/65535/53915177409_4b765c2d35_m.jpg" alt="Game Image" width="120" height="120" />', 
                  '<img src="https://live.staticflickr.com/65535/53915177409_4b765c2d35_m.jpg" alt="Game Image" width="120" height="120" style="filter: grayscale(100%);" />')
    player_26 = Player('Kellyanne', 70, 0, 'F', [], 0, 2, False, 
                  '<img src="https://live.staticflickr.com/65535/53913941692_eac36dcfe8_m.jpg" alt="Game Image" width="120" height="120" />', 
                  '<img src="https://live.staticflickr.com/65535/53913941692_eac36dcfe8_m.jpg" alt="Game Image" width="120" height="120" style="filter: grayscale(100%);" />')
    player_27 = Player('Emily', 80, 0, 'F', [], 0, 2, False, 
                  '<img src="https://live.staticflickr.com/65535/53915074263_ab79c4b40e_m.jpg" alt="Game Image" width="120" height="120" />', 
                  '<img src="https://live.staticflickr.com/65535/53915074263_ab79c4b40e_m.jpg" alt="Game Image" width="120" height="120" style="filter: grayscale(100%);" />')
    player_28 = Player('Cara Maria', 80, 0, 'F', [], 0, 2, False, 
                  '<img src="https://live.staticflickr.com/65535/53915276935_75703ef236_m.jpg" alt="Game Image" width="120" height="120" />', 
                  '<img src="https://live.staticflickr.com/65535/53915276935_75703ef236_m.jpg" alt="Game Image" width="120" height="120" style="filter: grayscale(100%);" />')
    player_29 = Player('Aviv', 60, 0, 'F', [], 0, 2, False, 
                  '<img src="https://live.staticflickr.com/65535/53914826981_16e856e3a0_m.jpg" alt="Game Image" width="120" height="120" />', 
                  '<img src="https://live.staticflickr.com/65535/53914826981_16e856e3a0_m.jpg" alt="Game Image" width="120" height="120" style="filter: grayscale(100%);" />')
    player_30 = Player('Laurel', 80, 0, 'F', [], 0, 2, False, 
                  '<img src="https://live.staticflickr.com/65535/53915177484_6d8ca27f5d_m.jpg" alt="Game Image" width="120" height="120" />', 
                  '<img src="https://live.staticflickr.com/65535/53915177484_6d8ca27f5d_m.jpg" alt="Game Image" width="120" height="120" style="filter: grayscale(100%);" />')
    player_31 = Player('Amanda', 50, 0, 'F', [], 0, 3, False, 
                  '<img src="https://live.staticflickr.com/65535/53915074293_52530116a4_m.jpg" alt="Game Image" width="120" height="120" />', 
                  '<img src="https://live.staticflickr.com/65535/53915074293_52530116a4_m.jpg" alt="Game Image" width="120" height="120" style="filter: grayscale(100%);" />')
    player_32 = Player('Averey', 60, 0, 'F', [], 0, 3, False, 
                  '<img src="https://live.staticflickr.com/65535/53913941792_91062239ed_m.jpg" alt="Game Image" width="120" height="120" />', 
                  '<img src="https://live.staticflickr.com/65535/53913941792_91062239ed_m.jpg" alt="Game Image" width="120" height="120" style="filter: grayscale(100%);" />')
    player_33 = Player('Jonna', 70, 0, 'F', [], 0, 3, False, 
                  '<img src="https://live.staticflickr.com/65535/53913941722_255d7eccdf_m.jpg" alt="Game Image" width="120" height="120" />', 
                  '<img src="https://live.staticflickr.com/65535/53913941722_255d7eccdf_m.jpg" alt="Game Image" width="120" height="120" style="filter: grayscale(100%);" />')
    player_34 = Player('Nia', 60, 0, 'F', [], 0, 3, False, 
                  '<img src="https://live.staticflickr.com/65535/53915074188_ee54662032_m.jpg" alt="Game Image" width="120" height="120" />', 
                  '<img src="https://live.staticflickr.com/65535/53915074188_ee54662032_m.jpg" alt="Game Image" width="120" height="120" style="filter: grayscale(100%);" />')
    player_35 = Player('Tori', 70, 0, 'F', [], 0, 3, False, 
                  '<img src="https://live.staticflickr.com/65535/53915276805_1987e3b741_m.jpg" alt="Game Image" width="120" height="120" />', 
                  '<img src="https://live.staticflickr.com/65535/53915276805_1987e3b741_m.jpg" alt="Game Image" width="120" height="120" style="filter: grayscale(100%);" />')
    player_36 = Player('Jenny', 80, 0, 'F', [], 0, 4, False, 
                  '<img src="https://live.staticflickr.com/65535/53915177509_d499d052f6_m.jpg" alt="Game Image" width="120" height="120" />', 
                  '<img src="https://live.staticflickr.com/65535/53915177509_d499d052f6_m.jpg" alt="Game Image" width="120" height="120" style="filter: grayscale(100%);" />')
    player_37 = Player('Kaycee', 80, 0, 'F', [], 0, 4, False, 
                  '<img src="https://live.staticflickr.com/65535/53913941697_e1272a6617_m.jpg" alt="Game Image" width="120" height="120" />', 
                  '<img src="https://live.staticflickr.com/65535/53913941697_e1272a6617_m.jpg" alt="Game Image" width="120" height="120" style="filter: grayscale(100%);" />')
    player_38 = Player('Michele', 70, 0, 'F', [], 0, 4, False, 
                  '<img src="https://live.staticflickr.com/65535/53914826891_3e4cef76a5_m.jpg" alt="Game Image" width="120" height="120" />', 
                  '<img src="https://live.staticflickr.com/65535/53914826891_3e4cef76a5_m.jpg" alt="Game Image" width="120" height="120" style="filter: grayscale(100%);" />')
    player_39 = Player('Nurys', 70, 0, 'F', [], 0, 4, False, 
                  '<img src="https://live.staticflickr.com/65535/53915074193_60ca2dd741_m.jpg" alt="Game Image" width="120" height="120" />', 
                  '<img src="https://live.staticflickr.com/65535/53915074193_60ca2dd741_m.jpg" alt="Game Image" width="120" height="120" style="filter: grayscale(100%);" />')
    player_40 = Player('Olivia', 70, 0, 'F', [], 0, 4, False, 
                  '<img src="https://live.staticflickr.com/65535/53915074178_90a5ef302f_m.jpg" alt="Game Image" width="120" height="120" />', 
                  '<img src="https://live.staticflickr.com/65535/53915074178_90a5ef302f_m.jpg" alt="Game Image" width="120" height="120" style="filter: grayscale(100%);" />')
    males = [player_1, player_2, player_3, player_4, player_5, player_6, player_7, player_8, player_9, player_10,
         player_11, player_12, player_13, player_14, player_15, player_16, player_17, player_18, player_19, player_20]
    females = [player_21, player_22, player_23, player_24, player_25, player_26, player_27, player_28, player_29, player_30,
           player_31, player_32, player_33, player_34, player_35, player_36, player_37, player_38, player_39, player_40]
    for male in females:
        male.chart = []
        male.eliminatedFirst = False
        male.placement = 0
    for male in males:
        male.chart = []
        male.eliminatedFirst = False
        male.placement = 0
    count = len(females)
    count2 = count
    index3 = 0
    eliminated = []
    game_output = []  # Store game events to display on the website
    game_results = []
    era1men = []
    era2men = []
    era3men = []
    era4men = []
    era1women = []
    era2women = []
    era3women = []
    era4women = []

    week = 1
    game_output.append("<h2>")
    while count2 > 4:
        game_output.append(f"</h2><br><h2>Week {week}</h2><br><div1>")
        if week == 1:  
            for i in range(count2):
                males[i].random = random.randint(1, males[i].skill) + random.randint(1, males[i].skill)
                females[i].random = random.randint(1, females[i].skill) + random.randint(1, females[i].skill)
            males = sorted(males, key=operator.attrgetter('random'), reverse=True)
            females = sorted(females, key=operator.attrgetter('random'), reverse=True)
            for male in males:
                if male.era == 1:
                    era1men.append(male)
                if male.era == 2:
                    era2men.append(male)
                if male.era == 3:
                    era3men.append(male)
                if male.era == 4:
                    era4men.append(male)
            for male in females:
                if male.era == 1:
                    era1women.append(male)
                if male.era == 2:
                    era2women.append(male)
                if male.era == 3:
                    era3women.append(male)
                if male.era == 4:
                    era4women.append(male)
            game_output.append(era1men[0].name+ " " + era2men[0].name+ " " + era3men[0].name+ " " + era4men[0].name+ " " + " won the opening daily<br>" + era1men[0].pic + era2men[0].pic + era3men[0].pic + era4men[0].pic + "<br>")
            game_output.append(era1women[0].name+ " " + era2women[0].name+ " " + era3women[0].name+ " " + era4women[0].name+ " " + " won the opening daily<br>" + era1women[0].pic + era2women[0].pic + era3women[0].pic + era4women[0].pic + "<br><br><br>")
            game_output.append(era1men[4].name+ " " + era2men[4].name+ " " + era3men[4].name+ " " + era4men[4].name+ " " + " got last in the opening daily<br>"+ era1men[4].pic + era2men[4].pic + era3men[4].pic + era4men[4].pic + "<br>")
            game_output.append(era1women[4].name+ " " + era2women[4].name+ " " + era3women[4].name+ " " + era4women[4].name+ " " + " got last in the opening daily<br>"+ era1women[4].pic + era2women[4].pic + era3women[4].pic + era4women[4].pic + "<br><br><br>")
            era1men[0].chart.append("WIN")
            era2men[0].chart.append("WIN")
            era3men[0].chart.append("WIN")
            era4men[0].chart.append("WIN")
            era1women[0].chart.append("WIN")
            era2women[0].chart.append("WIN")
            era3women[0].chart.append("WIN")
            era4women[0].chart.append("WIN")
            era1men[4].chart.append("ELIM")
            era2men[4].chart.append("ELIM")
            era3men[4].chart.append("ELIM")
            era4men[4].chart.append("ELIM")
            era1women[4].chart.append("ELIM")
            era2women[4].chart.append("ELIM")
            era3women[4].chart.append("ELIM")
            era4women[4].chart.append("ELIM")
            era1women[1].chart.append("SAFE")
            era1women[2].chart.append("SAFE")
            era1women[3].chart.append("SAFE")
            era2women[1].chart.append("SAFE")
            era2women[2].chart.append("SAFE")
            era2women[3].chart.append("SAFE")
            era3women[1].chart.append("SAFE")
            era3women[2].chart.append("SAFE")
            era3women[3].chart.append("SAFE")
            era4women[1].chart.append("SAFE")
            era4women[2].chart.append("SAFE")
            era4women[3].chart.append("SAFE")
            era1men[1].chart.append("SAFE")
            era1men[2].chart.append("SAFE")
            era1men[3].chart.append("SAFE")
            era2men[1].chart.append("SAFE")
            era2men[2].chart.append("SAFE")
            era2men[3].chart.append("SAFE")
            era3men[1].chart.append("SAFE")
            era3men[2].chart.append("SAFE")
            era3men[3].chart.append("SAFE")
            era4men[1].chart.append("SAFE")
            era4men[2].chart.append("SAFE")
            era4men[3].chart.append("SAFE")
            oneRandom = random.randint(1, 3)
            twoRandom = random.randint(1, 3)
            threeRandom = random.randint(1, 3)
            fourRandom = random.randint(1, 3)
            era1women[oneRandom].chart[0] = ("ELIM")
            era2women[twoRandom].chart[0] = ("ELIM")
            era3women[threeRandom].chart[0] = ("ELIM")
            era4women[fourRandom].chart[0] = ("ELIM")
            era1men[oneRandom].chart[0] = ("ELIM")
            era2men[twoRandom].chart[0] = ("ELIM")
            era3men[threeRandom].chart[0] = ("ELIM")
            era4men[fourRandom].chart[0] = ("ELIM")
            game_output.append(era1men[oneRandom].name+ " " + era2men[twoRandom].name+ " " + era3men[threeRandom].name+ " " + era4men[fourRandom].name+ " " + " were sent in by the winners<br>" + era1men[oneRandom].pic + era2men[twoRandom].pic + era3men[threeRandom].pic + era4men[fourRandom].pic + "<br>")
            game_output.append(era1women[oneRandom].name+ " " + era2women[twoRandom].name+ " " + era3women[threeRandom].name+ " " + era4women[fourRandom].name+ " " + " were sent in by the winners<br>" + era1women[oneRandom].pic + era2women[twoRandom].pic + era3women[threeRandom].pic + era4women[fourRandom].pic + "<br><br><br>")
            for i in range(count2):
                males[i].random = random.randint(1, males[i].skill) + random.randint(1, males[i].skill)
                females[i].random = random.randint(1, females[i].skill) + random.randint(1, females[i].skill)
            if era1men[4].random > era1men[oneRandom].random:
                game_output.append(era1men[4].name + " has beat " + era1men[oneRandom].name + " in elimination<br>" + era1men[4].pic + era1men[oneRandom].elimPic + "<br>")
                era1men[oneRandom].chart[0] = "OUT"
                era1men[oneRandom].placement = 20
                era1men[oneRandom].eliminatedFirst = True
                eliminated.append(era1men[oneRandom])
            else:
                game_output.append(era1men[oneRandom].name + " has beat " + era1men[4].name + " in elimination<br>" + era1men[oneRandom].pic + era1men[4].elimPic + "<br>")
                era1men[4].chart[0] = "OUT"
                era1men[4].placement = 20
                era1men[4].eliminatedFirst = True
                eliminated.append(era1men[4])

                
            if era1women[4].random > era1women[oneRandom].random:
                game_output.append(era1women[4].name + " has beat " + era1women[oneRandom].name + " in elimination<br>" + era1women[4].pic + era1women[oneRandom].elimPic + "<br>")
                era1women[oneRandom].chart[0] = "OUT"
                era1women[oneRandom].placement = 20
                era1women[oneRandom].eliminatedFirst = True
                eliminated.append(era1women[oneRandom])
            else:
                game_output.append(era1women[oneRandom].name + " has beat " + era1women[4].name + " in elimination<br>" + era1women[oneRandom].pic + era1women[4].elimPic + "<br>")
                era1women[4].chart[0] = "OUT"
                era1women[4].placement = 20
                era1women[4].eliminatedFirst = True
                eliminated.append(era1women[4])


            if era2men[4].random > era2men[twoRandom].random:
                game_output.append(era2men[4].name + " has beat " + era2men[twoRandom].name + " in elimination<br>" + era2men[4].pic + era2men[twoRandom].elimPic + "<br>")
                era2men[twoRandom].chart[0] = "OUT"
                era2men[twoRandom].placement = 20
                era2men[twoRandom].eliminatedFirst = True
                eliminated.append(era2men[twoRandom])
            else:
                game_output.append(era2men[twoRandom].name + " has beat " + era2men[4].name + " in elimination<br>" + era2men[twoRandom].pic + era2men[4].elimPic + "<br>")
                era2men[4].chart[0] = "OUT"
                era2men[4].placement = 20
                era2men[4].eliminatedFirst = True
                eliminated.append(era2men[4])
            if era2women[4].random > era2women[twoRandom].random:
                game_output.append(era2women[4].name + " has beat " + era2women[twoRandom].name + " in elimination<br>" + era2women[4].pic + era2women[twoRandom].elimPic + "<br>")
                era2women[twoRandom].chart[0] = "OUT"
                era2women[twoRandom].placement = 20
                era2women[twoRandom].eliminatedFirst = True
                eliminated.append(era2women[twoRandom])
            else:
                game_output.append(era2women[twoRandom].name + " has beat " + era2women[4].name + " in elimination<br>" + era2women[twoRandom].pic + era2women[4].elimPic + "<br>")
                era2women[4].chart[0] = "OUT"
                era2women[4].placement = 20
                era2women[4].eliminatedFirst = True
                eliminated.append(era2women[4])
            if era3men[4].random > era3men[threeRandom].random:
                game_output.append(era3men[4].name + " has beat " + era3men[threeRandom].name + " in elimination<br>" + era3men[4].pic + era3men[threeRandom].elimPic + "<br>")
                era3men[threeRandom].chart[0] = "OUT"
                era3men[threeRandom].placement = 20
                era3men[threeRandom].eliminatedFirst = True
                eliminated.append(era3men[threeRandom])
            else:
                game_output.append(era3men[threeRandom].name + " has beat " + era3men[4].name + " in elimination<br>" + era3men[threeRandom].pic + era3men[4].elimPic + "<br>")
                era3men[4].chart[0] = "OUT"
                era3men[4].placement = 20
                era3men[4].eliminatedFirst = True
                eliminated.append(era3men[4])
            if era3women[4].random > era3women[threeRandom].random:
                game_output.append(era3women[4].name + " has beat " + era3women[threeRandom].name + " in elimination<br>" + era3women[4].pic + era3women[threeRandom].elimPic + "<br>")
                era3women[threeRandom].chart[0] = "OUT"
                era3women[threeRandom].placement = 20
                era3women[threeRandom].eliminatedFirst = True
                eliminated.append(era3women[threeRandom])
            else:
                game_output.append(era3women[threeRandom].name + " has beat " + era3women[4].name + " in elimination<br>" + era3women[threeRandom].pic + era3women[4].elimPic + "<br>")
                era3women[4].chart[0] = "OUT"
                era3women[4].placement = 20
                era3women[4].eliminatedFirst = True
                eliminated.append(era3women[4])
            if era4men[4].random > era4men[fourRandom].random:
                game_output.append(era4men[4].name + " has beat " + era4men[fourRandom].name + " in elimination<br>" + era4men[4].pic + era4men[fourRandom].elimPic + "<br>")
                era4men[fourRandom].chart[0] = "OUT"
                era4men[fourRandom].placement = 20
                era4men[fourRandom].eliminatedFirst = True
                eliminated.append(era4men[fourRandom])
            else:
                game_output.append(era4men[fourRandom].name + " has beat " + era4men[4].name + " in elimination<br>" + era4men[fourRandom].pic + era4men[4].elimPic + "<br>")
                era4men[4].chart[0] = "OUT"
                era4men[4].placement = 20
                era4men[4].eliminatedFirst = True
                eliminated.append(era4men[4])
            if era4women[4].random > era4women[fourRandom].random:
                game_output.append(era4women[4].name + " has beat " + era4women[fourRandom].name + " in elimination<br>" + era4women[4].pic + era4women[fourRandom].elimPic + "<br>")
                era4women[fourRandom].chart[0] = "OUT"
                era4women[fourRandom].placement = 20
                era4women[fourRandom].eliminatedFirst = True
                eliminated.append(era4women[fourRandom])
            else:
                game_output.append(era4women[fourRandom].name + " has beat " + era4women[4].name + " in elimination<br>" + era4women[fourRandom].pic + era4women[4].elimPic + "<br>")
                era4women[4].chart[0] = "OUT"
                era4women[4].placement = 20
                era4women[4].eliminatedFirst = True
                eliminated.append(era4women[4])
            
                

            # Update game results for the round
            round_results = []
            for player in males + females:
                round_results.append((player, player.chart[index3]))
            game_results.append(round_results)
            index4 = 0
            for male in males:
                if male.eliminatedFirst == True:
                    del males[index4]
                index4 += 1
            index4 = 0
            for male in females:
                if male.eliminatedFirst == True:
                    del females[index4]
                index4 += 1
            index4 = 0
            for male in males:
                if male.eliminatedFirst == True:
                    del males[index4]
                index4 += 1
            index4 = 0
            for male in females:
                if male.eliminatedFirst == True:
                    del females[index4]
                index4 += 1
            index4 = 0
            for male in males:
                if male.eliminatedFirst == True:
                    del males[index4]
                index4 += 1
            index4 = 0
            for male in females:
                if male.eliminatedFirst == True:
                    del females[index4]
                index4 += 1
            week += 1
            count2 -= 4
            index3 += 1
        else:
            for i in range(count2):
                males[i].random = random.randint(1, males[i].skill) + random.randint(1, males[i].skill)
                females[i].random = random.randint(1, females[i].skill) + random.randint(1, females[i].skill)
        
            males = sorted(males, key=operator.attrgetter('random'), reverse=True)
            females = sorted(females, key=operator.attrgetter('random'), reverse=True)

            game_output.append(f"{males[0].name} and {females[0].name} Won The Daily<br>" + males[0].pic + females[0].pic + "<br><br>")

            males[0].chart.append("WIN")
            females[0].chart.append("WIN")

            for x in range(1, count2-4):
                males[x].chart.append("SAFE")
                females[x].chart.append("SAFE")

            for x in range(4):
                if count2-x-1 < len(males):
                    males[count2-x-1].chart.append("SAFE")
                if count2-x-1 < len(females):
                    females[count2-x-1].chart.append("SAFE")

            if count2-4 >= 0:
                game_output.append(f"{males[count2-4].name}, {males[count2-3].name}, {males[count2-2].name}, {males[count2-1].name} Placed Bottom 4 In The Daily<br> {females[count2-4].name}, {females[count2-3].name}, {females[count2-2].name}, {females[count2-1].name} Placed Bottom 4 In The Daily<br>" + males[count2-4].pic
                                    + males[count2-3].pic+ males[count2-2].pic+ males[count2-1].pic + " " + females[count2-4].pic
                                    + females[count2-3].pic+ females[count2-2].pic+ females[count2-1].pic + "<br><br>")

            maleint = random.randint(1, 4)
            maleint2 = random.randint(1, 4)
            while maleint == maleint2:
                maleint2 = random.randint(1, 4)
        
            femaleint = random.randint(1, 4)
            femaleint2 = random.randint(1, 4)
            while femaleint == femaleint2:
                femaleint2 = random.randint(1, 4)

            game_output.append(f"{males[count2-maleint].name}, {males[count2-maleint2].name}, {females[count2-femaleint].name}, {females[count2-femaleint2].name} were sent into elimination<br>" + males[count2-maleint].pic + males[count2-maleint2].pic + " "+ females[count2-femaleint].pic + females[count2-femaleint2].pic + "<br><br>")

            males[count2-maleint].random = random.randint(1, males[count2-maleint].skill)
            males[count2-maleint2].random = random.randint(1, males[count2-maleint2].skill)

            if males[count2-maleint].random > males[count2-maleint2].random:
                game_output.append(f"{males[count2-maleint].name} has beat {males[count2-maleint2].name} in the elimination<br>" + males[count2-maleint].pic + males[count2-maleint2].elimPic + "<br>")
                males[count2-maleint2].chart[index3] = "OUT"
                males[count2-maleint].chart[index3] = "ELIM"
                males[count2-maleint2].placement = count2
                eliminated.append(males[count2-maleint2])
            else:
                game_output.append(f"{males[count2-maleint2].name} has beat {males[count2-maleint].name} in the elimination<br>" + males[count2-maleint2].pic + males[count2-maleint].elimPic + "<br>")
                males[count2-maleint].chart[index3] = "OUT"
                males[count2-maleint2].chart[index3] = "ELIM"
                males[count2-maleint].placement = count2
                eliminated.append(males[count2-maleint])

            females[count2-femaleint].random = random.randint(1, females[count2-femaleint].skill)
            females[count2-femaleint2].random = random.randint(1, females[count2-femaleint2].skill)

            if females[count2-femaleint].random > females[count2-femaleint2].random:
                game_output.append(f"{females[count2-femaleint].name} has beat {females[count2-femaleint2].name} in the elimination<br>" + females[count2-femaleint].pic + females[count2-femaleint2].elimPic + "<br>")
                females[count2-femaleint2].chart[index3] = "OUT"
                females[count2-femaleint].chart[index3] = "ELIM"
                females[count2-femaleint2].placement = count2
                eliminated.append(females[count2-femaleint2])
            else:
                game_output.append(f"{females[count2-femaleint2].name} has beat {females[count2-femaleint].name} in the elimination<br>" + females[count2-femaleint2].pic + females[count2-femaleint].elimPic + "<br>")
                females[count2-femaleint].chart[index3] = "OUT"
                females[count2-femaleint2].chart[index3] = "ELIM"
                females[count2-femaleint].placement = count2
                eliminated.append(females[count2-femaleint])

            # Update game results for the round
            round_results = []
            for player in males + females:
                round_results.append((player, player.chart[index3]))
            game_results.append(round_results)
            if males[count2-maleint].random > males[count2-maleint2].random:
                del males[count2-maleint2]
            else:
                del males[count2-maleint]
            if females[count2-femaleint].random > females[count2-femaleint2].random:
                del females[count2-femaleint2]
            else:
                del females[count2-femaleint]

            count2 -= 1
            index3 += 1
            week += 1
        males = sorted(males, key=operator.attrgetter('era'), reverse=True)
        females = sorted(females, key=operator.attrgetter('era'), reverse=True)
        males.reverse()
        females.reverse()
        remainingMales = ""
        remainingFemales = ""
        for male in males:
            remainingMales += " " + male.name + " (" + str(male.era) + ") "
        for male in females:
            remainingFemales += " " + male.name + " (" + str(male.era) + ") "
        
        game_output.append("Males Remaining: " + remainingMales + "<br>")
        for male in males:
            game_output.append(male.pic)
        game_output.append("<br>")
        game_output.append("Females Remaining: " + remainingFemales + "<br>")
        for male in females:
            game_output.append(male.pic)
        game_output.append("<br>")
    index = 0
    while index < 4:
        females[index].random = random.randint(1,females[index].skill) + random.randint(1,females[index].skill)
        males[index].random = random.randint(1,males[index].skill) + random.randint(1,males[index].skill)
        index += 1
    males = sorted(males, key=operator.attrgetter('random'))
    males.reverse()
    females = sorted(females, key=operator.attrgetter('random'))
    females.reverse()
    game_output.append(f"<br><h1>Finale</h1><br>")
    game_output.append("Fourth Place<br>")
    game_output.append(males[3].name + " & " + females[3].name + "<br>" + males[3].elimPic+ females[3].elimPic)
    game_output.append("<br><br><br><br>Third Place<br>")
    game_output.append(males[2].name + " & " + females[2].name + "<br>" + males[2].elimPic+ females[2].elimPic)
    game_output.append("<br><br><br><br>Second Place<br>")
    game_output.append(males[1].name + " & " + females[1].name + "<br>" + males[1].elimPic+ females[1].elimPic)
    game_output.append("<br><br><br><br>First Place<br>")
    game_output.append(males[0].name + " & " + females[0].name + "<br>" + males[0].pic+ females[0].pic)
    females[3].chart.append("FOURTH")
    males[3].chart.append("FOURTH")
    eliminated.append(females[3])
    eliminated.append(males[3])
    females[3].placement = 4
    males[3].placement = 4
    eliminated.append(females[2])
    eliminated.append(males[2])
    females[2].chart.append("THIRD")
    males[2].chart.append("THIRD")
    females[2].placement = 3
    males[2].placement = 3
    eliminated.append(females[1])
    eliminated.append(males[1])
    females[1].placement = 2
    males[1].placement = 2
    females[1].chart.append("SECOND")
    males[1].chart.append("SECOND")
    eliminated.append(females[0])
    eliminated.append(males[0])
    females[0].placement = 1
    males[0].placement = 1
    females[0].chart.append("WINNER")
    males[0].chart.append("WINNER")
    round_results = []
    for player in males + females:
            round_results.append((player, player.chart[index3]))
    game_results.append(round_results)
    males = [player_1, player_2, player_3, player_4, player_5, player_6, player_7, player_8, player_9, player_10,
         player_11, player_12, player_13, player_14, player_15, player_16, player_17, player_18, player_19, player_20]
    females = [player_21, player_22, player_23, player_24, player_25, player_26, player_27, player_28, player_29, player_30,
           player_31, player_32, player_33, player_34, player_35, player_36, player_37, player_38, player_39, player_40]
    eliminated = sorted(eliminated, key=operator.attrgetter('placement'))

    return game_output, eliminated, game_results,males, females
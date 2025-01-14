from flask import Flask, render_template_string, redirect, url_for
from dataclasses import dataclass
import random
import operator

app = Flask(__name__)
def traitors1Cast():
    @dataclass
    class Player:
        name: str
        skill: int
        random: int
        chart: list
        placement: int
        suspicion: int
        pic: str
        elimPic: str
        isTraitor: bool
        isImmune: bool
        def to_dict(self):
            return {
                'name': self.name,
                'skill': self.skill,
                'random': self.random,
                'chart': self.chart,
                'placement': self.placement,
                'suspicion': self.suspicion,
                'pic': self.pic,
                'elimPic': self.elimPic,
                'isTraitor': self.isTraitor,
                'isImmune': self.isImmune
            }

        @staticmethod
        def from_dict(data):
            return Player(
                name=data['name'],
                skill=data['skill'],
                random=data['random'],
                chart=data['chart'],
                placement=data['placement'],
                suspicion=data['suspicion'],
                pic=data['pic'],
                elimPic=data['elimPic'],
                isTraitor=data['isTraitor'],
                isImmune=data['isImmune']
            )
    player_1 = Player('Cirie', 80, 0, [], 0, 0,
        '<img src="https://live.staticflickr.com/65535/53914011432_403b3ffdfe_m.jpg" alt="Game Image" width="120" height="120" />',
        '<img src="https://live.staticflickr.com/65535/53914011432_403b3ffdfe_m.jpg" alt="BW Image" width="120" height="120" style="filter: grayscale(100%);" />',
        False,False)

    player_2 = Player('Andie', 80, 0, [], 0, 0,
        '<img src="https://live.staticflickr.com/65535/53914011472_17c251d42e_m.jpg" alt="Game Image" width="120" height="120" />',
        '<img src="https://live.staticflickr.com/65535/53914011472_17c251d42e_m.jpg" alt="BW Image" width="120" height="120" style="filter: grayscale(100%);" />',
        False,False)

    player_3 = Player('Quentin', 80, 0, [], 0, 0,
        '<img src="https://live.staticflickr.com/65535/53915346890_56cba9248f_m.jpg" alt="Game Image" width="120" height="120" />',
        '<img src="https://live.staticflickr.com/65535/53915346890_56cba9248f_m.jpg" alt="BW Image" width="120" height="120" style="filter: grayscale(100%);" />',
        False,False)

    player_4 = Player('Arie', 80, 0, [], 0, 0,
        '<img src="https://live.staticflickr.com/65535/53915144383_506816e65b_m.jpg" alt="Game Image" width="120" height="120" />',
        '<img src="https://live.staticflickr.com/65535/53915144383_506816e65b_m.jpg" alt="BW Image" width="120" height="120" style="filter: grayscale(100%);" />',
        False,False)

    player_5 = Player('Kate', 80, 0, [], 0, 0,
        '<img src="https://live.staticflickr.com/65535/53915246989_412a1d7332_m.jpg" alt="Game Image" width="120" height="120" />',
        '<img src="https://live.staticflickr.com/65535/53915246989_412a1d7332_m.jpg" alt="BW Image" width="120" height="120" style="filter: grayscale(100%);" />',
        False,False)

    player_6 = Player('Christian', 80, 0, [], 0, 0,
        '<img src="https://live.staticflickr.com/65535/53915247009_9c974a3c3e_m.jpg" alt="Game Image" width="120" height="120" />',
        '<img src="https://live.staticflickr.com/65535/53915247009_9c974a3c3e_m.jpg" alt="BW Image" width="120" height="120" style="filter: grayscale(100%);" />',
        False,False)

    player_7 = Player('Stephenie', 80, 0, [], 0, 0,
        '<img src="https://live.staticflickr.com/65535/53915144328_a12bc34cf6_m.jpg" alt="Game Image" width="120" height="120" />',
        '<img src="https://live.staticflickr.com/65535/53915144328_a12bc34cf6_m.jpg" alt="BW Image" width="120" height="120" style="filter: grayscale(100%);" />',
        False,False)

    player_8 = Player('Rachel', 80, 0, [], 0, 0,
        '<img src="https://live.staticflickr.com/65535/53915346900_010032df5f_m.jpg" alt="Game Image" width="120" height="120" />',
        '<img src="https://live.staticflickr.com/65535/53915346900_010032df5f_m.jpg" alt="BW Image" width="120" height="120" style="filter: grayscale(100%);" />',
        False,False)

    player_9 = Player('Shelbe', 80, 0, [], 0, 0,
        '<img src="https://live.staticflickr.com/65535/53914826856_00c6c30ebb_m.jpg" alt="Game Image" width="120" height="120" />',
        '<img src="https://live.staticflickr.com/65535/53914826856_00c6c30ebb_m.jpg" alt="BW Image" width="120" height="120" style="filter: grayscale(100%);" />',
        False,False)

    player_10 = Player('Anjelica', 80, 0, [], 0, 0,
        '<img src="https://live.staticflickr.com/65535/53915247044_6bb5cbe3ee_m.jpg" alt="Game Image" width="120" height="120" />',
        '<img src="https://live.staticflickr.com/65535/53915247044_6bb5cbe3ee_m.jpg" alt="BW Image" width="120" height="120" style="filter: grayscale(100%);" />',
        False,False)

    player_11 = Player('Cody', 80, 0, [], 0, 0,
        '<img src="https://live.staticflickr.com/65535/53915246999_339a598b8f_m.jpg" alt="Game Image" width="120" height="120" />',
        '<img src="https://live.staticflickr.com/65535/53915246999_339a598b8f_m.jpg" alt="BW Image" width="120" height="120" style="filter: grayscale(100%);" />',
        False,False)

    player_12 = Player('Amanda', 80, 0, [], 0, 0,
        '<img src="https://live.staticflickr.com/65535/53915247049_588dd6d1d1_m.jpg" alt="Game Image" width="120" height="120" />',
        '<img src="https://live.staticflickr.com/65535/53915247049_588dd6d1d1_m.jpg" alt="BW Image" width="120" height="120" style="filter: grayscale(100%);" />',
        False,False)

    player_13 = Player('Kyle', 80, 0, [], 0, 0,
        '<img src="https://live.staticflickr.com/65535/53915346910_b4b0270fe0_m.jpg" alt="Game Image" width="120" height="120" />',
        '<img src="https://live.staticflickr.com/65535/53915346910_b4b0270fe0_m.jpg" alt="BW Image" width="120" height="120" style="filter: grayscale(100%);" />',
        False,False)

    player_14 = Player('Ryan', 80, 0, [], 0, 0,
        '<img src="https://live.staticflickr.com/65535/53915177429_8f997cc0c6_m.jpg" alt="Game Image" width="120" height="120" />',
        '<img src="https://live.staticflickr.com/65535/53915177429_8f997cc0c6_m.jpg" alt="BW Image" width="120" height="120" style="filter: grayscale(100%);" />',
        False,False)

    player_15 = Player('Michael', 80, 0, [], 0, 0,
        '<img src="https://live.staticflickr.com/65535/53915346895_c617ae8711_m.jpg" alt="Game Image" width="120" height="120" />',
        '<img src="https://live.staticflickr.com/65535/53915346895_c617ae8711_m.jpg" alt="BW Image" width="120" height="120" style="filter: grayscale(100%);" />',
        False,False)

    player_16 = Player('Azra', 80, 0, [], 0, 0,
        '<img src="https://live.staticflickr.com/65535/53914011452_5629a02c62_m.jpg" alt="Game Image" width="120" height="120" />',
        '<img src="https://live.staticflickr.com/65535/53914011452_5629a02c62_m.jpg" alt="BW Image" width="120" height="120" style="filter: grayscale(100%);" />',
        False,False)

    player_17 = Player('Brandi', 80, 0, [], 0, 0,
        '<img src="https://live.staticflickr.com/65535/53915247014_174ba51d18_m.jpg" alt="Game Image" width="120" height="120" />',
        '<img src="https://live.staticflickr.com/65535/53915247014_174ba51d18_m.jpg" alt="BW Image" width="120" height="120" style="filter: grayscale(100%);" />',
        False,False)

    player_18 = Player('Bam', 80, 0, [], 0, 0,
        '<img src="https://live.staticflickr.com/65535/53913941787_f7ebd34aff_m.jpg" alt="Game Image" width="120" height="120" />',
        '<img src="https://live.staticflickr.com/65535/53913941787_f7ebd34aff_m.jpg" alt="BW Image" width="120" height="120" style="filter: grayscale(100%);" />',
        False,False)

    player_19 = Player('Geraldine', 80, 0, [], 0, 0,
        '<img src="https://live.staticflickr.com/65535/53915144348_00e5b1c7ef_m.jpg" alt="Game Image" width="120" height="120" />',
        '<img src="https://live.staticflickr.com/65535/53915144348_00e5b1c7ef_m.jpg" alt="BW Image" width="120" height="120" style="filter: grayscale(100%);" />',
        False,False)

    player_20 = Player('Reza', 80, 0, [], 0, 0,
        '<img src="https://live.staticflickr.com/65535/53915074173_2a1220381e_m.jpg" alt="Game Image" width="120" height="120" />',
        '<img src="https://live.staticflickr.com/65535/53915074173_2a1220381e_m.jpg" alt="BW Image" width="120" height="120" style="filter: grayscale(100%);" />',
        False,False)
    cast = [player_1, player_2, player_3, player_4, player_5, player_6, player_7, player_8, player_9, player_10,
        player_11, player_12, player_13, player_14, player_15, player_16, player_17, player_18, player_19, player_20]
    for people in cast:
        people.isTraitor = False
    return cast
def traitors3Cast():
    @dataclass
    class Player:
        name: str
        skill: int
        random: int
        chart: list
        placement: int
        suspicion: int
        pic: str
        elimPic: str
        isTraitor: bool
        isImmune: bool
        def to_dict(self):
            return {
                'name': self.name,
                'skill': self.skill,
                'random': self.random,
                'chart': self.chart,
                'placement': self.placement,
                'suspicion': self.suspicion,
                'pic': self.pic,
                'elimPic': self.elimPic,
                'isTraitor': self.isTraitor,
                'isImmune': self.isImmune
            }

        @staticmethod
        def from_dict(data):
            return Player(
                name=data['name'],
                skill=data['skill'],
                random=data['random'],
                chart=data['chart'],
                placement=data['placement'],
                suspicion=data['suspicion'],
                pic=data['pic'],
                elimPic=data['elimPic'],
                isTraitor=data['isTraitor'],
                isImmune=data['isImmune']
            )
    player_1 = Player('Wes', 80, 0, [], 0, 0, '<img src="https://live.staticflickr.com/65535/54263710850_a82863550d_m.jpg" alt="Game Image" width="120" height="120" />',
                       '<img src="https://live.staticflickr.com/65535/54263710850_a82863550d_m.jpg" alt="BW Image" width="120" height="120" style="filter: grayscale(100%);" />', False, False)
    player_2 = Player('Wells', 80, 0, [], 0, 0, '<img src="https://live.staticflickr.com/65535/54263710855_41a34d1f0a_m.jpg" alt="Game Image" width="120" height="120" />',
                       '<img src="https://live.staticflickr.com/65535/54263710855_41a34d1f0a_m.jpg" alt="BW Image" width="120" height="120" style="filter: grayscale(100%);" />', False, False)
    player_3 = Player('Tony', 80, 0, [], 0, 0, '<img src="https://live.staticflickr.com/65535/54262404202_05a55f9bd8_m.jpg" alt="Game Image" width="120" height="120" />',
                       '<img src="https://live.staticflickr.com/65535/54262404202_05a55f9bd8_m.jpg" alt="BW Image" width="120" height="120" style="filter: grayscale(100%);" />', False, False)
    player_4 = Player('Tom', 80, 0, [], 0, 0, '<img src="https://live.staticflickr.com/65535/54263528969_ac01eed40f_m.jpg" alt="Game Image" width="120" height="120" />',
                       '<img src="https://live.staticflickr.com/65535/54263528969_ac01eed40f_m.jpg" alt="BW Image" width="120" height="120" style="filter: grayscale(100%);" />', False, False)
    player_5 = Player('Sam', 80, 0, [], 0, 0, '<img src="https://live.staticflickr.com/65535/54263291816_5eac7be7a9_m.jpg" alt="Game Image" width="120" height="120" />',
                       '<img src="https://live.staticflickr.com/65535/54263291816_5eac7be7a9_m.jpg" alt="BW Image" width="120" height="120" style="filter: grayscale(100%);" />', False, False)
    player_6 = Player('Robyn', 80, 0, [], 0, 0, '<img src="https://live.staticflickr.com/65535/54263710845_e3fdde2116_m.jpg" alt="Game Image" width="120" height="120" />',
                       '<img src="https://live.staticflickr.com/65535/54263710845_e3fdde2116_m.jpg" alt="BW Image" width="120" height="120" style="filter: grayscale(100%);" />', False, False)
    player_7 = Player('Rob', 80, 0, [], 0, 0, '<img src="https://live.staticflickr.com/65535/54262404217_5c2e437a8e_m.jpg" alt="Game Image" width="120" height="120" />',
                       '<img src="https://live.staticflickr.com/65535/54262404217_5c2e437a8e_m.jpg" alt="BW Image" width="120" height="120" style="filter: grayscale(100%);" />', False, False)
    player_8 = Player('Nikki', 80, 0, [], 0, 0, '<img src="https://live.staticflickr.com/65535/54263513323_d45c0587f4_m.jpg" alt="Game Image" width="120" height="120" />',
                       '<img src="https://live.staticflickr.com/65535/54263513323_d45c0587f4_m.jpg" alt="BW Image" width="120" height="120" style="filter: grayscale(100%);" />', False, False)
    player_9 = Player('Jeremy', 80, 0, [], 0, 0, '<img src="https://live.staticflickr.com/65535/54263291836_1a8838aa2c_m.jpg" alt="Game Image" width="120" height="120" />',
                       '<img src="https://live.staticflickr.com/65535/54263291836_1a8838aa2c_m.jpg" alt="BW Image" width="120" height="120" style="filter: grayscale(100%);" />', False, False)
    player_10 = Player('Ivar', 80, 0, [], 0, 0, '<img src="https://live.staticflickr.com/65535/54263291841_61b4ea33a5_m.jpg" alt="Game Image" width="120" height="120" />',
                        '<img src="https://live.staticflickr.com/65535/54263291841_61b4ea33a5_m.jpg" alt="BW Image" width="120" height="120" style="filter: grayscale(100%);" />', False, False)
    player_11 = Player('Gabby', 80, 0, [], 0, 0, '<img src="https://live.staticflickr.com/65535/54263528989_f15cff98d6_m.jpg" alt="Game Image" width="120" height="120" />',
                        '<img src="https://live.staticflickr.com/65535/54263528989_f15cff98d6_m.jpg" alt="BW Image" width="120" height="120" style="filter: grayscale(100%);" />', False, False)
    player_12 = Player('Dylan', 80, 0, [], 0, 0, '<img src="https://live.staticflickr.com/65535/54262404247_0d1ece66d0_m.jpg" alt="Game Image" width="120" height="120" />',
                        '<img src="https://live.staticflickr.com/65535/54262404247_0d1ece66d0_m.jpg" alt="BW Image" width="120" height="120" style="filter: grayscale(100%);" />', False, False)
    player_13 = Player('Dorinda', 80, 0, [], 0, 0, '<img src="https://live.staticflickr.com/65535/54263710870_9f512e6403_m.jpg" alt="Game Image" width="120" height="120" />',
                        '<img src="https://live.staticflickr.com/65535/54263710870_9f512e6403_m.jpg" alt="BW Image" width="120" height="120" style="filter: grayscale(100%);" />', False, False)
    player_14 = Player('Dolores', 80, 0, [], 0, 0, '<img src="https://live.staticflickr.com/65535/54263528994_0c75486b20_m.jpg" alt="Game Image" width="120" height="120" />',
                        '<img src="https://live.staticflickr.com/65535/54263528994_0c75486b20_m.jpg" alt="BW Image" width="120" height="120" style="filter: grayscale(100%);" />', False, False)
    player_15 = Player('Derrick', 80, 0, [], 0, 0, '<img src="https://live.staticflickr.com/65535/54263710900_509179af0d_m.jpg" alt="Game Image" width="120" height="120" />',
                        '<img src="https://live.staticflickr.com/65535/54263710900_509179af0d_m.jpg" alt="BW Image" width="120" height="120" style="filter: grayscale(100%);" />', False, False)
    player_16 = Player('Danielle', 80, 0, [], 0, 0, '<img src="https://live.staticflickr.com/65535/54263513343_bd6fe86963_m.jpg" alt="Game Image" width="120" height="120" />',
                        '<img src="https://live.staticflickr.com/65535/54263513343_bd6fe86963_m.jpg" alt="BW Image" width="120" height="120" style="filter: grayscale(100%);" />', False, False)
    player_17 = Player('Ciara', 80, 0, [], 0, 0, '<img src="https://live.staticflickr.com/65535/54262404277_4e9f84a8e8_m.jpg" alt="Game Image" width="120" height="120" />',
                        '<img src="https://live.staticflickr.com/65535/54262404277_4e9f84a8e8_m.jpg" alt="BW Image" width="120" height="120" style="filter: grayscale(100%);" />', False, False)
    player_18 = Player('Chriselle', 80, 0, [], 0, 0, '<img src="https://live.staticflickr.com/65535/54263529019_6a5d8d0c35_m.jpg" alt="Game Image" width="120" height="120" />',
                        '<img src="https://live.staticflickr.com/65535/54263529019_6a5d8d0c35_m.jpg" alt="BW Image" width="120" height="120" style="filter: grayscale(100%);" />', False, False)
    player_19 = Player('Carolyn', 80, 0, [], 0, 0, '<img src="https://live.staticflickr.com/65535/54263291861_81d92de8b5_m.jpg" alt="Game Image" width="120" height="120" />',
                        '<img src="https://live.staticflickr.com/65535/54263291861_81d92de8b5_m.jpg" alt="BW Image" width="120" height="120" style="filter: grayscale(100%);" />', False, False)
    player_20 = Player('Britney', 80, 0, [], 0, 0, '<img src="https://live.staticflickr.com/65535/54263710920_3007f3bc15_m.jpg" alt="Game Image" width="120" height="120" />',
                        '<img src="https://live.staticflickr.com/65535/54263710920_3007f3bc15_m.jpg" alt="BW Image" width="120" height="120" style="filter: grayscale(100%);" />', False, False)
    player_21 = Player('Bob TDQ', 80, 0, [], 0, 0, '<img src="https://live.staticflickr.com/65535/54262404287_e4dccde819_m.jpg" alt="Game Image" width="120" height="120" />',
                        '<img src="https://live.staticflickr.com/65535/54262404287_e4dccde819_m.jpg" alt="BW Image" width="120" height="120" style="filter: grayscale(100%);" />', False, False)
    player_22 = Player('Bob H', 80, 0, [], 0, 0, '<img src="https://live.staticflickr.com/65535/54263529039_0f94ab2db1_m.jpg" alt="Game Image" width="120" height="120" />',
                        '<img src="https://live.staticflickr.com/65535/54263529039_0f94ab2db1_m.jpg" alt="BW Image" width="120" height="120" style="filter: grayscale(100%);" />', False, False)
    player_23 = Player('Ayan', 80, 0, [], 0, 0, '<img src="https://live.staticflickr.com/65535/54263291886_1bd013c4f8_m.jpg" alt="Game Image" width="120" height="120" />',
                        '<img src="https://live.staticflickr.com/65535/54263291886_1bd013c4f8_m.jpg" alt="BW Image" width="120" height="120" style="filter: grayscale(100%);" />', False, False)
    cast = [player_1, player_2, player_3, player_4, player_5, player_6, player_7, player_8, player_9, player_10,
        player_11, player_12, player_13, player_14, player_15, player_16, player_17, player_18, player_19, player_20, player_21, player_22,player_23]
    for people in cast:
        people.isTraitor = False
    return cast
def traitors2Cast():
    @dataclass
    class Player:
        name: str
        skill: int
        random: int
        chart: list
        placement: int
        suspicion: int
        pic: str
        elimPic: str
        isTraitor: bool
        isImmune: bool
        def to_dict(self):
            return {
                'name': self.name,
                'skill': self.skill,
                'random': self.random,
                'chart': self.chart,
                'placement': self.placement,
                'suspicion': self.suspicion,
                'pic': self.pic,
                'elimPic': self.elimPic,
                'isTraitor': self.isTraitor,
                'isImmune': self.isImmune
            }

        @staticmethod
        def from_dict(data):
            return Player(
                name=data['name'],
                skill=data['skill'],
                random=data['random'],
                chart=data['chart'],
                placement=data['placement'],
                suspicion=data['suspicion'],
                pic=data['pic'],
                elimPic=data['elimPic'],
                isTraitor=data['isTraitor'],
                isImmune=data['isImmune']
            )
    player_1 = Player('CT', 80, 0, [], 0, 0, '<img src="https://live.staticflickr.com/65535/53914905541_737b455de8_m.jpg" alt="Game Image" width="120" height="120" />',
                       '<img src="https://live.staticflickr.com/65535/53914905541_737b455de8_m.jpg" alt="BW Image" width="120" height="120" style="filter: grayscale(100%);" />', False, False)
    player_2 = Player('Trishelle', 80, 0, [], 0, 0, '<img src="https://live.staticflickr.com/65535/53915355300_e0ab6d357e_m.jpg" alt="Game Image" width="120" height="120" />',
                       '<img src="https://live.staticflickr.com/65535/53915355300_e0ab6d357e_m.jpg" alt="BW Image" width="120" height="120" style="filter: grayscale(100%);" />', False, False)
    player_3 = Player('MJ', 80, 0, [], 0, 0, '<img src="https://live.staticflickr.com/65535/53915153248_5398be5ff8_m.jpg" alt="Game Image" width="120" height="120" />',
                       '<img src="https://live.staticflickr.com/65535/53915153248_5398be5ff8_m.jpg" alt="BW Image" width="120" height="120" style="filter: grayscale(100%);" />', False, False)
    player_4 = Player('Kate', 80, 0, [], 0, 0, '<img src="https://live.staticflickr.com/65535/53914020112_32065bdae3_m.jpg" alt="Game Image" width="120" height="120" />',
                       '<img src="https://live.staticflickr.com/65535/53914020112_32065bdae3_m.jpg" alt="BW Image" width="120" height="120" style="filter: grayscale(100%);" />', False, False)
    player_5 = Player('Sandra', 80, 0, [], 0, 0, '<img src="https://live.staticflickr.com/65535/53915255634_cb284f0eeb_m.jpg" alt="Game Image" width="120" height="120" />',
                       '<img src="https://live.staticflickr.com/65535/53915255634_cb284f0eeb_m.jpg" alt="BW Image" width="120" height="120" style="filter: grayscale(100%);" />', False, False)
    player_6 = Player('Shereé', 80, 0, [], 0, 0, '<img src="https://live.staticflickr.com/65535/53914905461_7f2832d852_m.jpg" alt="Game Image" width="120" height="120" />',
                       '<img src="https://live.staticflickr.com/65535/53914905461_7f2832d852_m.jpg" alt="BW Image" width="120" height="120" style="filter: grayscale(100%);" />', False, False)
    player_7 = Player('Phaedra', 80, 0, [], 0, 0, '<img src="https://live.staticflickr.com/65535/53914905471_4b0a733af5_m.jpg" alt="Game Image" width="120" height="120" />',
                       '<img src="https://live.staticflickr.com/65535/53914905471_4b0a733af5_m.jpg" alt="BW Image" width="120" height="120" style="filter: grayscale(100%);" />', False, False)
    player_8 = Player('John', 80, 0, [], 0, 0, '<img src="https://live.staticflickr.com/65535/53914020122_422c21631b_m.jpg" alt="Game Image" width="120" height="120" />',
                       '<img src="https://live.staticflickr.com/65535/53914020122_422c21631b_m.jpg" alt="BW Image" width="120" height="120" style="filter: grayscale(100%);" />', False, False)
    player_9 = Player('Peter', 80, 0, [], 0, 0, '<img src="https://live.staticflickr.com/65535/53914020077_aef08d1683_m.jpg" alt="Game Image" width="120" height="120" />',
                       '<img src="https://live.staticflickr.com/65535/53914020077_aef08d1683_m.jpg" alt="BW Image" width="120" height="120" style="filter: grayscale(100%);" />', False, False)
    player_10 = Player('Kevin', 80, 0, [], 0, 0, '<img src="https://live.staticflickr.com/65535/53915153258_91a7a87040_m.jpg" alt="Game Image" width="120" height="120" />',
                        '<img src="https://live.staticflickr.com/65535/53915153258_91a7a87040_m.jpg" alt="BW Image" width="120" height="120" style="filter: grayscale(100%);" />', False, False)
    player_11 = Player('Parvati', 80, 0, [], 0, 0, '<img src="https://live.staticflickr.com/65535/53915355320_670b9c5997_m.jpg" alt="Game Image" width="120" height="120" />',
                        '<img src="https://live.staticflickr.com/65535/53915355320_670b9c5997_m.jpg" alt="BW Image" width="120" height="120" style="filter: grayscale(100%);" />', False, False)
    player_12 = Player('Bergie', 80, 0, [], 0, 0, '<img src="https://live.staticflickr.com/65535/53915255734_8f2ed85195_m.jpg" alt="Game Image" width="120" height="120" />',
                        '<img src="https://live.staticflickr.com/65535/53915255734_8f2ed85195_m.jpg" alt="BW Image" width="120" height="120" style="filter: grayscale(100%);" />', False, False)
    player_13 = Player('Dan', 80, 0, [], 0, 0, '<img src="https://live.staticflickr.com/65535/53915255719_a3979c7c52_m.jpg" alt="Game Image" width="120" height="120" />',
                        '<img src="https://live.staticflickr.com/65535/53915255719_a3979c7c52_m.jpg" alt="BW Image" width="120" height="120" style="filter: grayscale(100%);" />', False, False)
    player_14 = Player('Janelle', 80, 0, [], 0, 0, '<img src="https://live.staticflickr.com/65535/53915355355_cdcc6c3d3f_m.jpg" alt="Game Image" width="120" height="120" />',
                        '<img src="https://live.staticflickr.com/65535/53915355355_cdcc6c3d3f_m.jpg" alt="BW Image" width="120" height="120" style="filter: grayscale(100%);" />', False, False)
    player_15 = Player('Tamra', 80, 0, [], 0, 0, '<img src="https://live.staticflickr.com/65535/53915355305_d83b4d29f7_m.jpg" alt="Game Image" width="120" height="120" />',
                        '<img src="https://live.staticflickr.com/65535/53915355305_d83b4d29f7_m.jpg" alt="BW Image" width="120" height="120" style="filter: grayscale(100%);" />', False, False)
    player_16 = Player('Larsa', 80, 0, [], 0, 0, '<img src="https://live.staticflickr.com/65535/53914905496_af592fe077_m.jpg" alt="Game Image" width="120" height="120" />',
                        '<img src="https://live.staticflickr.com/65535/53914905496_af592fe077_m.jpg" alt="BW Image" width="120" height="120" style="filter: grayscale(100%);" />', False, False)
    player_17 = Player('Ekin-Su', 80, 0, [], 0, 0, '<img src="https://live.staticflickr.com/65535/53915255709_5aaf967042_m.jpg" alt="Game Image" width="120" height="120" />',
                        '<img src="https://live.staticflickr.com/65535/53915255709_5aaf967042_m.jpg" alt="BW Image" width="120" height="120" style="filter: grayscale(100%);" />', False, False)
    player_18 = Player('Deontay', 80, 0, [], 0, 0, '<img src="https://live.staticflickr.com/65535/53915255714_e8e6b7b7f2_m.jpg" alt="Game Image" width="120" height="120" />',
                        '<img src="https://live.staticflickr.com/65535/53915255714_e8e6b7b7f2_m.jpg" alt="BW Image" width="120" height="120" style="filter: grayscale(100%);" />', False, False)
    player_19 = Player('Maks', 80, 0, [], 0, 0, '<img src="https://live.staticflickr.com/65535/53915355330_2a754eea33_m.jpg" alt="Game Image" width="120" height="120" />',
                        '<img src="https://live.staticflickr.com/65535/53915355330_2a754eea33_m.jpg" alt="BW Image" width="120" height="120" style="filter: grayscale(100%);" />', False, False)
    player_20 = Player('Marcus', 80, 0, [], 0, 0, '<img src="https://live.staticflickr.com/65535/53914020102_1f9046f57f_m.jpg" alt="Game Image" width="120" height="120" />',
                        '<img src="https://live.staticflickr.com/65535/53914020102_1f9046f57f_m.jpg" alt="BW Image" width="120" height="120" style="filter: grayscale(100%);" />', False, False)
    player_21 = Player('Peppermint', 80, 0, [], 0, 0, '<img src="https://live.staticflickr.com/65535/53915255644_aab5ca0ba6_m.jpg" alt="Game Image" width="120" height="120" />',
                        '<img src="https://live.staticflickr.com/65535/53915255644_aab5ca0ba6_m.jpg" alt="BW Image" width="120" height="120" style="filter: grayscale(100%);" />', False, False)
    player_22 = Player('Bananas', 80, 0, [], 0, 0, '<img src="https://live.staticflickr.com/65535/53914020127_0b3e13c61a_m.jpg" alt="Game Image" width="120" height="120" />',
                        '<img src="https://live.staticflickr.com/65535/53914020127_0b3e13c61a_m.jpg" alt="BW Image" width="120" height="120" style="filter: grayscale(100%);" />', False, False)
    cast = [player_1, player_2, player_3, player_4, player_5, player_6, player_7, player_8, player_9, player_10,
        player_11, player_12, player_13, player_14, player_15, player_16, player_17, player_18, player_19, player_20, player_21, player_22]
    for people in cast:
        people.isTraitor = False
    return cast
def traitors(game_output, eliminated, game_results, cast, week,money):
    
    amountOfTraitors = int(len(cast)/6)
    remainingPlace = len(cast)
    print(amountOfTraitors)
    
    game_output.append("<h2>")
    game_output.append(f"</h1><br><h2>Week {week}</h1><br><div1>")
    index3 = 0
    traitorsStillIn = False
    for player in cast:
        if player.isTraitor == True:
            traitorsStillIn = True
    
    randomInt = 0
    randomSus = 0
    count = len(cast) - 1
    suspicions = [" was caught telling a lie<br>", " said they were the traitor by accident<br>", " is disliked by the cast<br>",
                  " is too quiet<br>", " is too loud<br>", " gossips too much<br>", " looks suspicious<br>", " is telling too many lies<br>",
                  " is being framed as a traitor<br>", " is the person the group thinks is the best at lying<br>",
                  " is refusing to talk to anyone<br>", " won't talk strategy<br>", " is publicly accused of being the traitor<br>",
                  " didn't look nervous at breakfast and people thought it was suspicious<br>",
                  " was smiling when they found out the last person died<br>", " is being accused of being the traitor due to their votes<br>",
                  " is overplaying being a faithful<br>", " is too tricky<br>", " is the house target<br>", " is crying a lot<br>", 
                  " is awkwardly walking into rooms and leaving without saying anything<br>", " acted suspicious during the challenge<br>"]
    positives = [
    "is liked by the group<br>", 
    "is always helpful to others<br>", 
    "is good at the challenges<br>", 
    "is kind to everyone<br>", 
    "is good at leading discussions<br>", 
    "always supports their team<br>", 
    "is trustworthy<br>", 
    "is very friendly and approachable<br>", 
    "has a great sense of humor<br>", 
    "always encourages others<br>", 
    "is highly respected by the group<br>", 
    "has a lot of great ideas<br>", 
    "is very empathetic to the group<br>", 
    "is always in a good mood<br>", 
    "is an excellent communicator<br>", 
    "always volunteers to help<br>", 
    "is a calming presence in stressful situations<br>"
]
    duoInteractions = [
        "is friends with ",
        "is aligned with ",
        "is working with ",
        "wants to go far in the game with ",
        "is in a showmance with ",
        "hates ",
        "wants to banish ",
        "solidifies a final 2 with ",
        "gossips with ",
        "can not stand ",
        "has a crush on ",
        "shares a secret alliance with ",
        "supports ",
        "is plotting against ",
        "has a strong bond with ",
        "is manipulating ",
        "is strategizing with ",
        "trusts ",
        "is openly hostile towards ",
        "is secretly working with ",
        "tries to sabotage ",
        "feels betrayed by ",
        "has a mutual respect for ",
        "wants to work together in the future with ",
        "is trying to eliminate ",
        "is constantly debating with ",
        "has formed an alliance with ",
        "is secretly plotting behind the back of ",
        "has a rivalry with ",
        "feels threatened by ",
        "shares a common goal with ",
        "thinks they're a valuable ally in the game ",
        "is creating drama with ",
        "has a deep connection with ",
        "would betray ",
        "is suspicious of ",
        "is trying to manipulate ",
        "is fiercely loyal to ",
        "is trying to outwit ",
        "is trying to distance themselves from ",
        "is openly competing with ",
        "is going after ",
        "has a mutual understanding with ",
        "has teamed up with ",
        "is trying to keep their distance from ",
        "is keeping their options open with "
    ]
    duoCount = len(duoInteractions)
    suspicionCount = len(suspicions)
    positiveCount = len(positives)
    traitors = []
    round_results = []
    if week == 1:
        traitorsIndex = random.sample(range(0, remainingPlace), amountOfTraitors)
        for i in range(amountOfTraitors):
            traitors.append(cast[traitorsIndex[i]])
            traitors[i].isTraitor = True
        index3 = 0
        traitors_names = ", ".join([traitor.name for traitor in traitors[:-1]])  # All except the last traitor
        if len(traitors) > 1:
            traitors_names += ", and " + traitors[-1].name  # Add the last traitor with "and"

        traitors_pics = "".join([traitor.pic for traitor in traitors])  # Concatenate all traitor pictures

        game_output.append(f"{traitors_names} have been chosen as the traitors.<br>{traitors_pics}<br>")
    if week == 1:
        return game_output, eliminated, game_results, cast, money
    while count >= 5:

        if week != 1:
            randomInt = random.randint(0, count)
            while cast[randomInt].isTraitor or cast[randomInt].isImmune:
                randomInt = random.randint(0, count)
            for player in cast:
                player.isImmune = False
            index = 0
            game_output.append(cast[randomInt].name + " was murdered by the traitors<br>")
            game_output.append(cast[randomInt].elimPic+ "<br>")
            for people in cast:
                if people.name == cast[randomInt].name:
                    people.placement = remainingPlace
                    remainingPlace -= 1
                    eliminated.append(cast[index])
                    del cast[index]
                index += 1

            count -= 1
            remaining = "Remaining: "
            mostSuspicious = sorted(cast, key=operator.attrgetter('suspicion'), reverse=True)
            for people in mostSuspicious:
                if people.isTraitor == True:
                    remaining += '<span style="color: red; font-weight: bold;">' + people.name + '</span>' + ", "
                else:
                    remaining += people.name + ", "
            remaining = remaining[:-2]
            remaining += "<br>"
            game_output.append(remaining)
            for people in mostSuspicious:
                game_output.append(people.pic)
        game_output.append("<h3> Breakfast </h3>")
        randomInt = random.randint(0, count)
        randomSus = random.randint(0, suspicionCount - 1)
        game_output.append(cast[randomInt].name + suspicions[randomSus]  + cast[randomInt].pic + "<br>")
        cast[randomInt].suspicion += 5
        randomInt = random.randint(0, count)
        randomSus = random.randint(0, suspicionCount - 1)
        game_output.append(cast[randomInt].name + suspicions[randomSus] + cast[randomInt].pic + "<br>")
        cast[randomInt].suspicion += 5
        randomInt = random.randint(0, count)
        randomSus = random.randint(0, suspicionCount - 1)
        game_output.append(cast[randomInt].name + suspicions[randomSus] + cast[randomInt].pic + "<br>")
        cast[randomInt].suspicion += 5
        randomInt = random.randint(0, count)
        randomSus = random.randint(0, positiveCount - 1)
        game_output.append(cast[randomInt].name + " " + positives[randomSus] + cast[randomInt].pic + "<br>")
        cast[randomInt].suspicion = max(0, cast[randomInt].suspicion - 2)
        randomInts = random.sample(range(0, count), 2)
        randomSus = random.randint(0, duoCount - 1)
        game_output.append(cast[randomInts[0]].name + " " + duoInteractions[randomSus] + " " + cast[randomInts[1]].name + "<br>" + cast[randomInts[0]].pic + cast[randomInts[1]].pic + "<br>")
        for people in cast:
            people.suspicion += 1
        traitorsTotal = 0
        for people in cast:
            if people.isTraitor:
                traitorsTotal += 1
        if (random.randint(0,2) == 0):
            traitors_list = [person for person in cast if person.isTraitor]
            randomTraitor = random.choice(traitors_list)
            game_output.append("People are starting to catch on to " + randomTraitor.name + " being a traitor<br> " + randomTraitor.pic + "<br>")
            randomTraitor.suspicion += 3

        randomInt = random.randint(0, 6)

        money += randomInt*5000
        game_output.append("<h3> Challenge </h3>")
        game_output.append("The group earned $" + str(randomInt*5000) + " at the challenge ($" + str(money) + " Total)" + "<br><br>")
        randomInt = random.randint(0, count)
        random.shuffle(cast)
        game_output.append(cast[randomInt].name + " earned a shield during the challenge<br>" + cast[randomInt].pic + "<br>")
        cast[randomInt].isImmune = True
        mostSuspicious = sorted(cast, key=operator.attrgetter('suspicion'), reverse=True)
        if week != 1:
            game_output.append("<h3> Round Table </h3>")
            game_output.append("The three most suspicious by the group are: " + mostSuspicious[0].name + ", " + mostSuspicious[1].name + ", " + mostSuspicious[2].name + "<br>" + mostSuspicious[0].pic + mostSuspicious[1].pic +mostSuspicious[2].pic + "<br>")
            votable = []
            for x in range(mostSuspicious[0].suspicion):
                votable.append(mostSuspicious[0].name)
            for x in range(mostSuspicious[1].suspicion):
                votable.append(mostSuspicious[1].name)
            for x in range(mostSuspicious[2].suspicion):
                votable.append(mostSuspicious[2].name)
            voteList = len(votable)
            votes = []
            player1V = 0
            player2V = 0
            player3V = 0
            game_output.append("<br>")
            for person in cast:
                randomNum = random.randint(0, voteList - 1)
                while (person.name == votable[randomNum]):
                    randomNum = random.randint(0, voteList - 1)
                game_output.append(person.name + " has voted for " + votable[randomNum] + "<br>")
                person.chart.append(votable[randomNum])

                if votable[randomNum] == mostSuspicious[0].name:
                    player1V += 1
                if votable[randomNum] == mostSuspicious[1].name:
                    player2V += 1
                if votable[randomNum] == mostSuspicious[2].name:
                    player3V += 1
            game_output.append("<br>")
            round_results = []
            for player in cast:
                round_results.append((player, player.chart[index3]))

            game_results.append(round_results)
            index3 += 1
            if player1V >= player3V and player1V >= player2V:
                if player3V > player2V:
                    game_output.append("By a vote of " + str(player1V) + "-" + str(player3V) + "-" + str(player2V)+ "<br>")
                else:
                    game_output.append("By a vote of " + str(player1V) + "-" + str(player2V) + "-" + str(player3V) + "<br>")
                game_output.append(mostSuspicious[0].name + " has been voted out<br>" + mostSuspicious[0].elimPic)
                index = 0
                for people in cast:
                    if people.name == mostSuspicious[0].name:
                        eliminated.append(cast[index])
                        people.placement = remainingPlace
                        remainingPlace -= 1
                        if len(cast) == 5:
                            if people.isTraitor:
                                traitorsStillIn = False
                        del cast[index]
                    index += 1
            if player2V >= player3V and player2V > player1V:
                if player3V > player1V:
                    game_output.append("By a vote of " + str(player2V) + "-" + str(player3V) + "-" + str(player1V)+ "<br>")
                else:
                    game_output.append("By a vote of " + str(player2V) + "-" + str(player1V) + "-" + str(player3V)+ "<br>")
                game_output.append(mostSuspicious[1].name + " has been voted out" + "<br>"+ mostSuspicious[1].elimPic)
                index = 0
                for people in cast:
                    if people.name == mostSuspicious[1].name:
                        eliminated.append(cast[index])
                        people.placement = remainingPlace
                        remainingPlace -= 1
                        if len(cast) == 5:
                            if people.isTraitor:
                                traitorsStillIn = False
                        del cast[index]
                    index += 1
            if player3V > player2V and player3V > player1V:
                if player1V > player2V:
                    game_output.append("By a vote of " + str(player3V) + "-" + str(player1V) + "-" + str(player2V)+ "<br>")
                else:
                    game_output.append("By a vote of " + str(player3V) + "-" + str(player2V) + "-" + str(player1V)+ "<br>")
                game_output.append(mostSuspicious[2].name + " has been voted out"+ "<br>"+ mostSuspicious[2].elimPic)
                index = 0
                for people in cast:
                    if people.name == mostSuspicious[2].name:
                        eliminated.append(cast[index])
                        people.placement = remainingPlace
                        remainingPlace -= 1
                        if len(cast) == 5:
                            if people.isTraitor:
                                traitorsStillIn = False
                        del cast[index]
                    index += 1
            totalTraitors = 0
            for player in cast:
                if player.isTraitor:
                    totalTraitors += 1      
            if (totalTraitors == 1) and (len(cast) > 6):
                traitorsIndex = random.randint(0, remainingPlace - 1)
                if cast[traitorsIndex].isTraitor == True:
                    cast[(traitorsIndex +1 % (len(cast)))].isTraitor = True
                    game_output.append("<br>" + cast[((traitorsIndex +1) % (len(cast)))].name + " has been recruited as a traitor "+ "<br>"+ cast[(traitorsIndex +1 % (len(cast)))].pic + "<br>")
                else:
                    cast[traitorsIndex].isTraitor = True
                    game_output.append("<br>" + cast[traitorsIndex].name + " has been recruited as a traitor "+ "<br>"+ cast[traitorsIndex].pic + "<br>")
            if len(cast) != 4:
                traitorsStillIn = False
                for player in cast:
                    traitorsStillIn = (traitorsStillIn or player.isTraitor)
                if traitorsStillIn == False:
                    game_output.append("<h3> The Faithfuls Have Won </h3><br>")
                    for player in cast:
                        player.chart.append("WINNER")
                    round_results = []
                    for player in cast:
                        round_results.append((player, player.chart[index3]))

                    game_results.append(round_results)

                    return game_output, eliminated, game_results, cast, money
            return game_output, eliminated, game_results, cast, money






    continueGame = False
    game_output.append("<br>")
    game_output.append("<h3> Final Fire </h3><br>")
    traitorsTotal = 0
    for people in cast:
        if people.isTraitor == True:
            traitorsIn = True
            traitorsTotal += 1
    if traitorsStillIn == True:
        traitorsTotal = 4

    for people in cast:
        randomNum = random.randint(0, 4-traitorsTotal)
        if randomNum > 0:
            game_output.append(people.name + ' has voted to <span style="color: red; font-weight: bold;">end</span> the game<br>' + people.pic + '<br>')
            people.chart.append("END")
        else:
            game_output.append(people.name + ' has voted to <span style="color: green; font-weight: bold;">continue</span> the game<br>' + people.pic + '<br>')
            people.chart.append("BANISH")


            continueGame = True
    round_results = []
    for player in cast:
        round_results.append((player, player.chart[index3]))

    game_results.append(round_results)
    index3 += 1


    while continueGame == True:
        game_output.append("<h3> Final Fire </h3><br>")
        mostSuspicious = sorted(cast, key=operator.attrgetter('suspicion'), reverse=True)
        game_output.append("The three most suspicious by the group are: " + mostSuspicious[0].name + ", " + mostSuspicious[1].name + ", " + mostSuspicious[2].name + "<br>" + mostSuspicious[0].pic + mostSuspicious[1].pic +mostSuspicious[2].pic + "<br>")
        votable = []

        for x in range(mostSuspicious[0].suspicion):
            votable.append(mostSuspicious[0].name)
        for x in range(mostSuspicious[1].suspicion):
            votable.append(mostSuspicious[1].name)
        for x in range(mostSuspicious[2].suspicion):
            votable.append(mostSuspicious[2].name)
        voteList = len(votable)
        votes = []
        player1V = 0
        player2V = 0
        player3V = 0
        game_output.append("<br>")
        for person in cast:
            randomNum = random.randint(0, voteList - 1)
            while (person.name == votable[randomNum]):
                randomNum = random.randint(0, voteList - 1)
            game_output.append(person.name + " has voted for " + votable[randomNum] + "<br>")
            person.chart.append(votable[randomNum])

            if votable[randomNum] == mostSuspicious[0].name:
                player1V += 1
            if votable[randomNum] == mostSuspicious[1].name:
                player2V += 1
            if votable[randomNum] == mostSuspicious[2].name:
                player3V += 1

        game_output.append("<br>")
        round_results = []
        for player in cast:
            round_results.append((player, player.chart[index3]))

        game_results.append(round_results)
        index3 += 1
        if player1V >= player3V and player1V >= player2V:
            if player3V > player2V:
                game_output.append("By a vote of " + str(player1V) + "-" + str(player3V) + "-" + str(player2V)+ "<br>")
            else:
                game_output.append("By a vote of " + str(player1V) + "-" + str(player2V) + "-" + str(player3V) + "<br>")
            game_output.append(mostSuspicious[0].name + " has been voted out<br>" + mostSuspicious[0].elimPic + "<br>")
            index = 0
            if (mostSuspicious[0].isTraitor):
                traitorsStillIn = False
            for people in cast:
                if people.name == mostSuspicious[0].name:
                    eliminated.append(cast[index])
                    people.placement = remainingPlace
                    remainingPlace -= 1
                    del cast[index]
                index += 1
        if player2V >= player3V and player2V > player1V:
            if player3V > player1V:
                game_output.append("By a vote of " + str(player2V) + "-" + str(player3V) + "-" + str(player1V)+ "<br>")
            else:
                game_output.append("By a vote of " + str(player2V) + "-" + str(player1V) + "-" + str(player3V)+ "<br>")
            game_output.append(mostSuspicious[1].name + " has been voted out" + "<br>"+ mostSuspicious[1].elimPic+ "<br>")
            index = 0
            if (mostSuspicious[1].isTraitor):
                traitorsStillIn = False
            for people in cast:
                if people.name == mostSuspicious[1].name:
                    eliminated.append(cast[index])
                    people.placement = remainingPlace
                    remainingPlace -= 1
                    del cast[index]
                index += 1
        if player3V > player2V and player3V > player1V:
            if player1V > player2V:
                game_output.append("By a vote of " + str(player3V) + "-" + str(player1V) + "-" + str(player2V)+ "<br>")
            else:
                game_output.append("By a vote of " + str(player3V) + "-" + str(player2V) + "-" + str(player1V)+ "<br>")
            game_output.append(mostSuspicious[2].name + " has been voted out"+ "<br>"+ mostSuspicious[2].elimPic+ "<br>")
            index = 0
            if (mostSuspicious[2].isTraitor):
                traitorsStillIn = False
            for people in cast:
                if people.name == mostSuspicious[2].name:
                    eliminated.append(cast[index])
                    people.placement = remainingPlace
                    remainingPlace -= 1
                    del cast[index]
                index += 1
        count -= 1
        continueGame = False
        traitorsTotal = 0
        for people in cast:
            if people.isTraitor == True:
                traitorsIn = True
                traitorsTotal += 1
        if traitorsStillIn == True:
            traitorsTotal = 3
        for people in cast:
            randomNum = random.randint(0, 3-traitorsTotal)
            if len(cast) == 2:
                continueGame = False
            else:
                if randomNum > 0:
                    game_output.append(people.name + ' has voted to <span style="color: red; font-weight: bold;">end</span> the game<br>' + people.pic + '<br>')
                    people.chart.append("END")
                else:
                    game_output.append(people.name + ' has voted to <span style="color: green; font-weight: bold;">continue</span> the game<br>' + people.pic + '<br>')
                    people.chart.append("BANISH")
                    continueGame = True
        if len(cast) != 2:
            round_results = []
            for player in cast:
                round_results.append((player, player.chart[index3]))

            game_results.append(round_results)
            index3 += 1

    traitorsIn = False
    game_output.append("<br>")
    traitorsTotal = 0
    for people in cast:
        if people.isTraitor == True:
            traitorsIn = True
            traitorsTotal += 1

    if traitorsIn == True:
        game_output.append("The Traitors Have Won <br>")
        for people in cast:
            if people.isTraitor == True:
                game_output.append(people.name + " ($" + str(int(money/(traitorsTotal))) + ")<br>")
                people.chart.append("WINNER")
                people.placement = 1
            else:
                people.chart.append("RUNNER-UP")
                people.placement = 2
        for people in cast:
            if people.isTraitor == True:
                game_output.append(people.pic)

    else:
        game_output.append("The Faithfuls Have Won <br>")
        for people in cast:
            game_output.append(people.name + " ($" + str(int(money/(len(cast)))) + ")<br>")
            people.chart.append("WINNER")
            people.placement = 1
        for people in cast:
            game_output.append(people.pic)

    round_results = []
    for player in cast:
        round_results.append((player, player.chart[index3]))

    game_results.append(round_results)

    return game_output, eliminated, game_results, cast, money
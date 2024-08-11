from dataclasses import dataclass
import random
import colorama
from colorama import Fore, Back, Style

def mole2():
    @dataclass
    class Player:
        name: str
        isMole: bool
        betweenNum: int
        tempPoints: int
        guessList: list
        correctGuess: bool
        totalPoints: int
        playerGuess: str
        quizResult: str
        pic: str
        elimPic: str
        chart: list
        placement: int
    
    player_1 = Player("Michael", False, 0, 0, [], False, 0, "", "",
                      '<img src="https://live.staticflickr.com/65535/53915206730_6e536bd9cf_m.jpg" alt="Game Image" width="120" height="120" />', 
                      '<img src="https://live.staticflickr.com/65535/53915206730_6e536bd9cf_m.jpg" alt="Game Image" width="120" height="120" style="filter: grayscale(100%);" />',[],0)
    player_2 = Player("Sean", False, 0, 0, [], False, 0, "", "",
                      '<img src="https://live.staticflickr.com/65535/53915004193_4a57e4deac_m.jpg" alt="Game Image" width="120" height="120" />', 
                      '<img src="https://live.staticflickr.com/65535/53915004193_4a57e4deac_m.jpg" alt="Game Image" width="120" height="120" style="filter: grayscale(100%);" />',[],0)
    player_3 = Player("Muna", False, 0, 0, [], False, 0, "", "",
                      '<img src="https://live.staticflickr.com/65535/53913872447_207c7a908a_m.jpg" alt="Game Image" width="120" height="120" />', 
                      '<img src="https://live.staticflickr.com/65535/53913872447_207c7a908a_m.jpg" alt="Game Image" width="120" height="120" style="filter: grayscale(100%);" />',[],0)
    player_4 = Player("Hannah", False, 0, 0, [], False, 0, "", "",
                      '<img src="https://live.staticflickr.com/65535/53915106964_b4e8999c1a_m.jpg" alt="Game Image" width="120" height="120" />', 
                      '<img src="https://live.staticflickr.com/65535/53915106964_b4e8999c1a_m.jpg" alt="Game Image" width="120" height="120" style="filter: grayscale(100%);" />',[],0)
    player_5 = Player("Deena", False, 0, 0, [], False, 0, "", "",
                      '<img src="https://live.staticflickr.com/65535/53915106969_9b5916dca8_m.jpg" alt="Game Image" width="120" height="120" />', 
                      '<img src="https://live.staticflickr.com/65535/53915106969_9b5916dca8_m.jpg" alt="Game Image" width="120" height="120" style="filter: grayscale(100%);" />',[],0)
    player_6 = Player("Ryan", False, 0, 0, [], False, 0, "", "",
                      '<img src="https://live.staticflickr.com/65535/53914757856_e97a8f354e_m.jpg" alt="Game Image" width="120" height="120" />', 
                      '<img src="https://live.staticflickr.com/65535/53914757856_e97a8f354e_m.jpg" alt="Game Image" width="120" height="120" style="filter: grayscale(100%);" />',[],0)
    player_7 = Player("Neesh", False, 0, 0, [], False, 0, "", "",
                      '<img src="https://live.staticflickr.com/65535/53914757861_9532347121_m.jpg" alt="Game Image" width="120" height="120" />', 
                      '<img src="https://live.staticflickr.com/65535/53914757861_9532347121_m.jpg" alt="Game Image" width="120" height="120" style="filter: grayscale(100%);" />',[],0)
    player_8 = Player("Quaylyn", False, 0, 0, [], False, 0, "", "",
                      '<img src="https://live.staticflickr.com/65535/53915206720_fe3abb3251_m.jpg" alt="Game Image" width="120" height="120" />', 
                      '<img src="https://live.staticflickr.com/65535/53915206720_fe3abb3251_m.jpg" alt="Game Image" width="120" height="120" style="filter: grayscale(100%);" />',[],0)
    player_9 = Player("Tony", False, 0, 0, [], False, 0, "", "",  
                    '<img src="https://live.staticflickr.com/65535/53915004198_9512a7e1b9_m.jpg" alt="Game Image" width="120" height="120" />', 
                    '<img src="https://live.staticflickr.com/65535/53915004198_9512a7e1b9_m.jpg" alt="Game Image" width="120" height="120" style="filter: grayscale(100%);" />',[],0)
    player_10 = Player("Melissa", False, 0, 0, [], False, 0, "", "",
                       '<img src="https://live.staticflickr.com/65535/53915206735_829021ea82_m.jpg" alt="Game Image" width="120" height="120" />', 
                      '<img src="https://live.staticflickr.com/65535/53915206735_829021ea82_m.jpg" alt="Game Image" width="120" height="120" style="filter: grayscale(100%);" />',[],0)
    player_11 = Player("Andy", False, 0, 0, [], False, 0, "", "",
                       '<img src="https://live.staticflickr.com/65535/53913872472_0b82fba2f0_m.jpg" alt="Game Image" width="120" height="120" />', 
                      '<img src="https://live.staticflickr.com/65535/53913872472_0b82fba2f0_m.jpg" alt="Game Image" width="120" height="120" style="filter: grayscale(100%);" />',[],0)
    player_12 = Player("Jennifer", False, 0, 0, [], False, 0, "", "",
                       '<img src="https://live.staticflickr.com/65535/53913872467_ea1109e7d8_m.jpg" alt="Game Image" width="120" height="120" />', 
                      '<img src="https://live.staticflickr.com/65535/53913872467_ea1109e7d8_m.jpg" alt="Game Image" width="120" height="120" style="filter: grayscale(100%);" />',[],0)

    cast = [player_1, player_2, player_3, player_4, player_5, player_6, player_7, player_8, player_9, player_10, player_11, player_12]
    index3 = 0
    game_results = []
    castSize = len(cast)
    moleNumber = random.randint(0, castSize-1)
    moleName = cast[moleNumber].name
    molePic = cast[moleNumber].pic
    cast[moleNumber].isMole = True
    eliminated = []
    game_output = []
    remaining = len(cast)
    week = 1
    while len(cast) > 3:
        game_output.append("<h2> Week " + str(week) + "</h2>")
        week += 1
        castSize = len(cast)
        index = -1
        for player in cast:
            player.tempPoints = random.randint(1, 10000)
        cast = sorted(cast, key=lambda x: x.tempPoints, reverse=True)
        
        for player in cast:
            index += 1
            player.guessList = []
            player.betweenNum = random.randint(1, 3)
            if player.betweenNum == 1:
                playerGuess = random.randint(0, castSize-1)
                while playerGuess == index:
                    playerGuess = random.randint(0, castSize-1)
                player.playerGuess = (player.name + " went all in on " + cast[playerGuess].name)
                player.guessList.append(cast[playerGuess].name)
                player.tempPoints = 3
            if player.betweenNum == 2:
                playerGuess = random.randint(0, castSize-1)
                playerGuess2 = random.randint(0, castSize-1)
                while playerGuess == index:
                    playerGuess = random.randint(0, castSize-1)
                while playerGuess == playerGuess2:
                    playerGuess2 = random.randint(0, castSize-1)
                player.playerGuess = (player.name + " split between " + cast[playerGuess].name + ' and ' + cast[playerGuess2].name)
                player.guessList.append(cast[playerGuess].name)
                player.guessList.append(cast[playerGuess2].name)
                player.tempPoints = 2
            if player.betweenNum == 3:
                playerGuess = random.randint(0, castSize-1)
                playerGuess2 = random.randint(0, castSize-1)
                playerGuess3 = random.randint(0, castSize-1)
                while playerGuess == index:
                    playerGuess = random.randint(0, castSize-1)
                while playerGuess == playerGuess2 or playerGuess2 == index:
                    playerGuess2 = random.randint(0, castSize-1)
                while (playerGuess == playerGuess3) or (playerGuess3 == playerGuess2) or playerGuess3 == index:
                    playerGuess3 = random.randint(0, castSize-1)
                player.playerGuess = (player.name + " split between " + cast[playerGuess].name + ' and ' + cast[playerGuess2].name + ' and ' + cast[playerGuess3].name)
                player.guessList.append(cast[playerGuess].name)
                player.guessList.append(cast[playerGuess2].name)
                player.guessList.append(cast[playerGuess3].name)
                player.tempPoints = 1
        
        for player in cast:
            if moleName in player.guessList:
                player.correctGuess = True
                player.totalPoints += player.tempPoints
            else:
                player.correctGuess = False
        
        for people in cast:
            if people.name == moleName:
                people.correctGuess = True
                people.tempPoints = 0
        
        cast = sorted(cast, key=lambda x: x.totalPoints, reverse=True)
        cast = sorted(cast, key=lambda x: x.tempPoints, reverse=False)
        cast = sorted(cast, key=lambda x: x.correctGuess, reverse=True)
        
        everyoneCorrect = True
        for player in cast:
            everyoneCorrect = (everyoneCorrect and player.correctGuess)
        if everyoneCorrect:
            for player in cast:
                if player.name == moleName:
                    player.tempPoints = 50
            cast = sorted(cast, key=lambda x: x.tempPoints, reverse=True)
        
        stopNum = 0
        ranNum = 0
        index2 = 0
        for player in cast:
            if index2 == (castSize-1):
                player.quizResult = '<img src="https://live.staticflickr.com/65535/53913842302_0f2ae7e35e_m.jpg" alt="Red" width="120" height="120"/>'
            else:
                player.quizResult = '<img src="https://live.staticflickr.com/65535/53914714201_ddd93f19d7_m.jpg" alt="Green" width="120" height="120"/>'
            index2 += 1
        
        usedNums = []
        while stopNum == 0:
            ranNum = random.randint(0, castSize-1)
            while ranNum in usedNums:
                ranNum = random.randint(0, castSize-1)
            usedNums.append(ranNum)
            game_output.append(cast[ranNum].name + "<br>" + cast[ranNum].pic)
            game_output.append(cast[ranNum].quizResult + "<br>")
            if cast[ranNum].quizResult == '<img src="https://live.staticflickr.com/65535/53913842302_0f2ae7e35e_m.jpg" alt="Red" width="120" height="120"/>':
                stopNum = 1
        
        game_output.append(cast[castSize-1].name + " has been eliminated" +"<br>"+ cast[castSize-1].elimPic + "<br>")
        game_output.append(cast[castSize-1].playerGuess + "<br>")
        guessRevealNum = random.randint(1, castSize-2)
        guessRevealNum2 = random.randint(1, castSize-2)
        while guessRevealNum == guessRevealNum2:
            guessRevealNum2 = random.randint(1, castSize-2)
        game_output.append(cast[guessRevealNum].pic + "<br>"+ cast[guessRevealNum].playerGuess+ "<br>")
        game_output.append(cast[guessRevealNum2].pic + "<br>"+ cast[guessRevealNum2].playerGuess+ "<br>")
        index4 = 0
        while (index4 < castSize-1):
            cast[index4].chart.append("IN")
            index4 += 1
        cast[castSize-1].chart.append("ELIM")
        round_results = []
        for player in cast:
                round_results.append((player, player.chart[index3]))
        game_results.append(round_results)
        index3 += 1
        cast[castSize-1].placement = remaining
        remaining -= 1
        eliminated.append(cast[castSize-1])
        del cast[castSize-1]
        game_output.append("<br> <br> Remaining: ")
        playerString = ''
        for player in cast:
            playerString += player.name + ' '
        game_output.append(playerString + "<br>")
        playerString = ''
        for player in cast:
            playerString += player.pic + ' '
        game_output.append(playerString)
    
    game_output.append("<br><br><br><br>The Mole was...")
    game_output.append("<br><br><br><br>")
    game_output.append(moleName + "<br>" + molePic + "<br><br><br><br>")
    game_output.append("The winner of The Mole season 2...<br><br><br><br>")
    cast = sorted(cast, key=lambda x: x.totalPoints, reverse=True)
    cast[0].chart.append("WINNER")
    cast[0].placement = 1
    cast[1].chart.append("RUNNER-UP")
    cast[1].placement = 3
    cast[2].placement = 2
    cast[2].chart.append("MOLE")
    cast[0].tempPoints = 40
    cast[1].tempPoints = 10
    cast[2].tempPoints = 20
    cast = sorted(cast, key=lambda x: x.tempPoints, reverse=True)
    round_results = []
    for player in cast:
            round_results.append((player, player.chart[index3]))
    game_results.append(round_results)
    game_output.append(cast[0].name + "<br>" + cast[0].pic)
    cast = cast + eliminated
    return game_output, game_results, cast

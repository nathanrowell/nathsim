from dataclasses import dataclass
import random
import colorama
from colorama import Fore, Back, Style

def mole1():
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
    
    player_1 = Player("Will", False, 0, 0, [], False, 0, "", "",
                      '<img src="https://live.staticflickr.com/65535/53916717596_71cacb503b_m.jpg" alt="Game Image" width="120" height="120" />', 
                      '<img src="https://live.staticflickr.com/65535/53916717596_71cacb503b_m.jpg" alt="Game Image" width="120" height="120" style="filter: grayscale(100%);" />',[],0)
    player_2 = Player("Sandy", False, 0, 0, [], False, 0, "", "",
                      '<img src="https://live.staticflickr.com/65535/53917162550_5a4f8e6f9d_m.jpg" alt="Game Image" width="120" height="120" />', 
                      '<img src="https://live.staticflickr.com/65535/53917162550_5a4f8e6f9d_m.jpg" alt="Game Image" width="120" height="120" style="filter: grayscale(100%);" />',[],0)
    player_3 = Player("Samara", False, 0, 0, [], False, 0, "", "",
                      '<img src="https://live.staticflickr.com/65535/53917068694_06e32c4155_m.jpg" alt="Game Image" width="120" height="120" />', 
                      '<img src="https://live.staticflickr.com/65535/53917068694_06e32c4155_m.jpg" alt="Game Image" width="120" height="120" style="filter: grayscale(100%);" />',[],0)
    player_4 = Player("Pranav", False, 0, 0, [], False, 0, "", "",
                      '<img src="https://live.staticflickr.com/65535/53915828977_208633cbce_m.jpg" alt="Game Image" width="120" height="120" />', 
                      '<img src="https://live.staticflickr.com/65535/53915828977_208633cbce_m.jpg" alt="Game Image" width="120" height="120" style="filter: grayscale(100%);" />',[],0)
    player_5 = Player("Osei", False, 0, 0, [], False, 0, "", "",
                      '<img src="https://live.staticflickr.com/65535/53916717576_d85979d0da_m.jpg" alt="Game Image" width="120" height="120" />', 
                      '<img src="https://live.staticflickr.com/65535/53916717576_d85979d0da_m.jpg" alt="Game Image" width="120" height="120" style="filter: grayscale(100%);" />',[],0)
    player_6 = Player("Kesi", False, 0, 0, [], False, 0, "", "",
                      '<img src="https://live.staticflickr.com/65535/53917068724_9ced1f277a_m.jpg" alt="Game Image" width="120" height="120" />', 
                      '<img src="https://live.staticflickr.com/65535/53917068724_9ced1f277a_m.jpg" alt="Game Image" width="120" height="120" style="filter: grayscale(100%);" />',[],0)
    player_7 = Player("Joi", False, 0, 0, [], False, 0, "", "",
                      '<img src="https://live.staticflickr.com/65535/53916967448_54e8585378_m.jpg" alt="Game Image" width="120" height="120" />', 
                      '<img src="https://live.staticflickr.com/65535/53916967448_54e8585378_m.jpg" alt="Game Image" width="120" height="120" style="filter: grayscale(100%);" />',[],0)
    player_8 = Player("Jacob", False, 0, 0, [], False, 0, "", "",
                      '<img src="https://live.staticflickr.com/65535/53917162585_59e77325fe_m.jpg" alt="Game Image" width="120" height="120" />', 
                      '<img src="https://live.staticflickr.com/65535/53917162585_59e77325fe_m.jpg" alt="Game Image" width="120" height="120" style="filter: grayscale(100%);" />',[],0)
    player_9 = Player("Greg", False, 0, 0, [], False, 0, "", "",  
                    '<img src="https://live.staticflickr.com/65535/53917162580_a9cea704c6_m.jpg" alt="Game Image" width="120" height="120" />', 
                    '<img src="https://live.staticflickr.com/65535/53917162580_a9cea704c6_m.jpg" alt="Game Image" width="120" height="120" style="filter: grayscale(100%);" />',[],0)
    player_10 = Player("Dom", False, 0, 0, [], False, 0, "", "",
                       '<img src="https://live.staticflickr.com/65535/53916967473_521100f909_m.jpg" alt="Game Image" width="120" height="120" />', 
                      '<img src="https://live.staticflickr.com/65535/53916967473_521100f909_m.jpg" alt="Game Image" width="120" height="120" style="filter: grayscale(100%);" />',[],0)
    player_11 = Player("Casey", False, 0, 0, [], False, 0, "", "",
                       '<img src="https://live.staticflickr.com/65535/53917162590_3e6d5430ef_m.jpg" alt="Game Image" width="120" height="120" />', 
                      '<img src="https://live.staticflickr.com/65535/53917162590_3e6d5430ef_m.jpg" alt="Game Image" width="120" height="120" style="filter: grayscale(100%);" />',[],0)
    player_12 = Player("Avori", False, 0, 0, [], False, 0, "", "",
                       '<img src="https://live.staticflickr.com/65535/53917068734_7a89f2f920_m.jpg" alt="Game Image" width="120" height="120" />', 
                      '<img src="https://live.staticflickr.com/65535/53917068734_7a89f2f920_m.jpg" alt="Game Image" width="120" height="120" style="filter: grayscale(100%);" />',[],0)

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

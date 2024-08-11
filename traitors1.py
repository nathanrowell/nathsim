from flask import Flask, render_template_string, redirect, url_for
from dataclasses import dataclass
import random
import operator

app = Flask(__name__)



def traitors1sim():
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
    
    player_1 = Player('Cirie', 80, 0, [], 0, 0, 
        '<img src="https://live.staticflickr.com/65535/53914011432_403b3ffdfe_m.jpg" alt="Game Image" width="120" height="120" />', 
        '<img src="https://live.staticflickr.com/65535/53914011432_403b3ffdfe_m.jpg" alt="BW Image" width="120" height="120" style="filter: grayscale(100%);" />', 
        False)

    player_2 = Player('Andie', 80, 0, [], 0, 0, 
        '<img src="https://live.staticflickr.com/65535/53914011472_17c251d42e_m.jpg" alt="Game Image" width="120" height="120" />', 
        '<img src="https://live.staticflickr.com/65535/53914011472_17c251d42e_m.jpg" alt="BW Image" width="120" height="120" style="filter: grayscale(100%);" />', 
        False)

    player_3 = Player('Quentin', 80, 0, [], 0, 0, 
        '<img src="https://live.staticflickr.com/65535/53915346890_56cba9248f_m.jpg" alt="Game Image" width="120" height="120" />', 
        '<img src="https://live.staticflickr.com/65535/53915346890_56cba9248f_m.jpg" alt="BW Image" width="120" height="120" style="filter: grayscale(100%);" />', 
        False)

    player_4 = Player('Arie', 80, 0, [], 0, 0, 
        '<img src="https://live.staticflickr.com/65535/53915144383_506816e65b_m.jpg" alt="Game Image" width="120" height="120" />', 
        '<img src="https://live.staticflickr.com/65535/53915144383_506816e65b_m.jpg" alt="BW Image" width="120" height="120" style="filter: grayscale(100%);" />', 
        False)

    player_5 = Player('Kate', 80, 0, [], 0, 0, 
        '<img src="https://live.staticflickr.com/65535/53915246989_412a1d7332_m.jpg" alt="Game Image" width="120" height="120" />', 
        '<img src="https://live.staticflickr.com/65535/53915246989_412a1d7332_m.jpg" alt="BW Image" width="120" height="120" style="filter: grayscale(100%);" />', 
        False)

    player_6 = Player('Christian', 80, 0, [], 0, 0, 
        '<img src="https://live.staticflickr.com/65535/53915247009_9c974a3c3e_m.jpg" alt="Game Image" width="120" height="120" />', 
        '<img src="https://live.staticflickr.com/65535/53915247009_9c974a3c3e_m.jpg" alt="BW Image" width="120" height="120" style="filter: grayscale(100%);" />', 
        False)

    player_7 = Player('Stephenie', 80, 0, [], 0, 0, 
        '<img src="https://live.staticflickr.com/65535/53915144328_a12bc34cf6_m.jpg" alt="Game Image" width="120" height="120" />', 
        '<img src="https://live.staticflickr.com/65535/53915144328_a12bc34cf6_m.jpg" alt="BW Image" width="120" height="120" style="filter: grayscale(100%);" />', 
        False)

    player_8 = Player('Rachel', 80, 0, [], 0, 0, 
        '<img src="https://live.staticflickr.com/65535/53915346900_010032df5f_m.jpg" alt="Game Image" width="120" height="120" />', 
        '<img src="https://live.staticflickr.com/65535/53915346900_010032df5f_m.jpg" alt="BW Image" width="120" height="120" style="filter: grayscale(100%);" />', 
        False)

    player_9 = Player('Shelbe', 80, 0, [], 0, 0, 
        '<img src="https://live.staticflickr.com/65535/53914826856_00c6c30ebb_m.jpg" alt="Game Image" width="120" height="120" />', 
        '<img src="https://live.staticflickr.com/65535/53914826856_00c6c30ebb_m.jpg" alt="BW Image" width="120" height="120" style="filter: grayscale(100%);" />', 
        False)

    player_10 = Player('Anjelica', 80, 0, [], 0, 0, 
        '<img src="https://live.staticflickr.com/65535/53915247044_6bb5cbe3ee_m.jpg" alt="Game Image" width="120" height="120" />', 
        '<img src="https://live.staticflickr.com/65535/53915247044_6bb5cbe3ee_m.jpg" alt="BW Image" width="120" height="120" style="filter: grayscale(100%);" />', 
        False)

    player_11 = Player('Cody', 80, 0, [], 0, 0, 
        '<img src="https://live.staticflickr.com/65535/53915246999_339a598b8f_m.jpg" alt="Game Image" width="120" height="120" />', 
        '<img src="https://live.staticflickr.com/65535/53915246999_339a598b8f_m.jpg" alt="BW Image" width="120" height="120" style="filter: grayscale(100%);" />', 
        False)

    player_12 = Player('Amanda', 80, 0, [], 0, 0, 
        '<img src="https://live.staticflickr.com/65535/53915247049_588dd6d1d1_m.jpg" alt="Game Image" width="120" height="120" />', 
        '<img src="https://live.staticflickr.com/65535/53915247049_588dd6d1d1_m.jpg" alt="BW Image" width="120" height="120" style="filter: grayscale(100%);" />', 
        False)

    player_13 = Player('Kyle', 80, 0, [], 0, 0, 
        '<img src="https://live.staticflickr.com/65535/53915346910_b4b0270fe0_m.jpg" alt="Game Image" width="120" height="120" />', 
        '<img src="https://live.staticflickr.com/65535/53915346910_b4b0270fe0_m.jpg" alt="BW Image" width="120" height="120" style="filter: grayscale(100%);" />', 
        False)

    player_14 = Player('Ryan', 80, 0, [], 0, 0, 
        '<img src="https://live.staticflickr.com/65535/53915177429_8f997cc0c6_m.jpg" alt="Game Image" width="120" height="120" />', 
        '<img src="https://live.staticflickr.com/65535/53915177429_8f997cc0c6_m.jpg" alt="BW Image" width="120" height="120" style="filter: grayscale(100%);" />', 
        False)

    player_15 = Player('Michael', 80, 0, [], 0, 0, 
        '<img src="https://live.staticflickr.com/65535/53915346895_c617ae8711_m.jpg" alt="Game Image" width="120" height="120" />', 
        '<img src="https://live.staticflickr.com/65535/53915346895_c617ae8711_m.jpg" alt="BW Image" width="120" height="120" style="filter: grayscale(100%);" />', 
        False)

    player_16 = Player('Azra', 80, 0, [], 0, 0, 
        '<img src="https://live.staticflickr.com/65535/53914011452_5629a02c62_m.jpg" alt="Game Image" width="120" height="120" />', 
        '<img src="https://live.staticflickr.com/65535/53914011452_5629a02c62_m.jpg" alt="BW Image" width="120" height="120" style="filter: grayscale(100%);" />', 
        False)

    player_17 = Player('Brandi', 80, 0, [], 0, 0, 
        '<img src="https://live.staticflickr.com/65535/53915247014_174ba51d18_m.jpg" alt="Game Image" width="120" height="120" />', 
        '<img src="https://live.staticflickr.com/65535/53915247014_174ba51d18_m.jpg" alt="BW Image" width="120" height="120" style="filter: grayscale(100%);" />', 
        False)

    player_18 = Player('Bam', 80, 0, [], 0, 0, 
        '<img src="https://live.staticflickr.com/65535/53913941787_f7ebd34aff_m.jpg" alt="Game Image" width="120" height="120" />', 
        '<img src="https://live.staticflickr.com/65535/53913941787_f7ebd34aff_m.jpg" alt="BW Image" width="120" height="120" style="filter: grayscale(100%);" />', 
        False)

    player_19 = Player('Geraldine', 80, 0, [], 0, 0, 
        '<img src="https://live.staticflickr.com/65535/53915144348_00e5b1c7ef_m.jpg" alt="Game Image" width="120" height="120" />', 
        '<img src="https://live.staticflickr.com/65535/53915144348_00e5b1c7ef_m.jpg" alt="BW Image" width="120" height="120" style="filter: grayscale(100%);" />', 
        False)

    player_20 = Player('Reza', 80, 0, [], 0, 0, 
        '<img src="https://live.staticflickr.com/65535/53915074173_2a1220381e_m.jpg" alt="Game Image" width="120" height="120" />', 
        '<img src="https://live.staticflickr.com/65535/53915074173_2a1220381e_m.jpg" alt="BW Image" width="120" height="120" style="filter: grayscale(100%);" />', 
        False)
    remainingPlace = 20
    cast = [player_1, player_2, player_3, player_4, player_5, player_6, player_7, player_8, player_9, player_10,
        player_11, player_12, player_13, player_14, player_15, player_16, player_17, player_18, player_19, player_20]
    game_output = []
    for people in cast:
        people.isTraitor = False
    index3 = 0
    totalMoney = 0
    randomInt = 0
    randomSus = 0
    totalEarned = 0
    count = len(cast) - 1
    suspicions = [" was caught telling a lie<br>", " said they were the traitor by accident<br>", " is disliked by the cast<br>",
                  " is too quiet<br>", " is too loud<br>", " gossips too much<br>", " looks suspicious<br>", " is telling too many lies<br>",
                  " is being framed as a traitor<br>", " is the person the group thinks is the best at lying<br>",
                  " is refusing to talk to anyone<br>", " won't talk strategy<br>", " is publicly accused of being the traitor<br>",
                  " didn't look nervous at breakfast and people thought it was suspicious<br>",
                  " was smiling when they found out the last person died<br>", " is being accused of being the traitor due to their votes<br>",
                  " is overplaying being a faithful<br>", " is too tricky<br>", " is the house target<br>"]
    suspicionCount = len(suspicions)
    eliminated = []
    traitors = []
    traitorsStillIn = True
    game_results = []
    round_results = []
    traitorsIndex = random.sample(range(0, 19), 3)
    traitors.append(cast[traitorsIndex[0]])
    traitors.append(cast[traitorsIndex[1]])
    traitors.append(cast[traitorsIndex[2]])
    traitorsNames = [traitors[0].name, traitors[1].name, traitors[2].name]
    traitors[0].isTraitor = True
    traitors[1].isTraitor = True
    traitors[2].isTraitor = True
    week = 1
    index3 = 0
    game_output.append(traitors[0].name + ", " + traitors[1].name + ", and " + traitors[2].name + " have been chosen as the traitors.<br>" + traitors[0].pic + traitors[1].pic + traitors[2].pic + "<br>")
    while count >= 5:
        print("<week" + str(week) + ">")
        game_output.append("<week" + str(week) + ">")
        game_output.append("<h2> Week " + str(week) + "</h2>")
        if week != 1: 
            randomInt = random.randint(0, count)
            while cast[randomInt].name in traitorsNames or cast[randomInt] in immunity:
                randomInt = random.randint(0, count)
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
        game_output.append(cast[randomInt].name + suspicions[randomSus] + cast[randomInt].pic+ "<br>")
        cast[randomInt].suspicion += 5
        for people in cast:
            people.suspicion += 1
        
        immunity = []
        randomInt = random.randint(0, 6)

        totalEarned += randomInt*5000
        game_output.append("<h3> Challenge </h3>")
        game_output.append("The group earned $" + str(randomInt*5000) + " at the challenge ($" + str(totalEarned) + " Total)" + "<br><br>")
        randomInt = random.randint(0, count)
        random.shuffle(cast)
        game_output.append(cast[randomInt].name + " earned a shield during the challenge<br>" + cast[randomInt].pic + "<br>")
        immunity.append(cast[randomInt])
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
                    
                    cast = [player_1, player_2, player_3, player_4, player_5, player_6, player_7, player_8, player_9, player_10,
                        player_11, player_12, player_13, player_14, player_15, player_16, player_17, player_18, player_19, player_20]
                    return game_output,cast, game_results

        
            count -= 1
        print("</week" + str(week) + ">")
        game_output.append("</week" + str(week) + ">")
        week += 1
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
                game_output.append(people.name + " ($" + str(int(totalEarned/(traitorsTotal))) + ")<br>")
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
            game_output.append(people.name + " ($" + str(int(totalEarned/(len(cast)))) + ")<br>")
            people.chart.append("WINNER")
            people.placement = 1
        for people in cast:
            game_output.append(people.pic)
    
    round_results = []
    for player in cast:
        round_results.append((player, player.chart[index3]))
    
    game_results.append(round_results)
    
    cast = [player_1, player_2, player_3, player_4, player_5, player_6, player_7, player_8, player_9, player_10,
        player_11, player_12, player_13, player_14, player_15, player_16, player_17, player_18, player_19, player_20]
    return game_output,cast, game_results
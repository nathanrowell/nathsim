import json
import random
from flask import Flask, flash, render_template, render_template_string, redirect, session, url_for, request
from dataclasses import dataclass
from TC40 import TC40cast
from TC40 import TC40Simulation
from traitors import traitors
from traitors import traitors3Cast
from traitors import traitors2Cast
from traitors import traitors1Cast
from mole2sim import mole2
from mole1sim import mole1

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')  # This will render the external index.html file


@app.route('/TheChallenge40', methods=['POST'])
def TheChallenge40():
    # Declares the Player class for TheChalelnge40 Specifically
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

        def to_dict(self):
            return {
                'name': self.name,
                'skill': self.skill,
                'random': self.random,
                'gender': self.gender,
                'chart': self.chart,
                'placement': self.placement,
                'era': self.era,
                'eliminatedFirst': self.eliminatedFirst,
                'pic': self.pic,
                'elimPic': self.elimPic
            }

        @staticmethod
        def from_dict(data):
            return Player(
                name=data['name'],
                skill=data['skill'],
                random=data['random'],
                gender=data['gender'],
                chart=data['chart'],
                placement=data['placement'],
                era=data['era'],
                eliminatedFirst=data['eliminatedFirst'],
                pic=data['pic'],
                elimPic=data['elimPic']
            )
    def parse_json_list(key):
        json_str = request.form.get(key, '[]')
        try:
            return json.loads(json_str)
        except json.JSONDecodeError:
            return []

    # Access form data
    game_output = parse_json_list('game_output')
    eliminated = parse_json_list('eliminated')
    week = int(request.form.get('week', 1))
    males = parse_json_list('males')
    females = parse_json_list('females')
    game_results = []

    # Initialize males and females if week is 1
    if week == 1:
        males, females = TC40cast()
    else:
        males = [Player.from_dict(player_dict) for player_dict in males]
        females = [Player.from_dict(player_dict) for player_dict in females]
        eliminated = [Player.from_dict(player_dict) for player_dict in eliminated]
    results_output = []
    # Update game state
    game_output, eliminated_cur, game_results, males, females, results_output = TC40Simulation(game_output, eliminated, game_results, males, females, week)
    week += 1

    game_output_display = '\n'.join(game_output)
    # Generate player results
    males_json = json.dumps([p.to_dict() for p in males])
    females_json = json.dumps([p.to_dict() for p in females])
    eliminated_json = json.dumps([p.to_dict() for p in eliminated])
    results_json = json.dumps(results_output)



    return render_template('challenge40.html', game_output_display=game_output_display,males_json=males_json, females_json=females_json, week = week,eliminated_json=eliminated_json, results_json = results_json)

@app.route('/TheChallenge40Results', methods=['POST'])
def TheChallenge40Results():
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

        def to_dict(self):
            return {
                'name': self.name,
                'skill': self.skill,
                'random': self.random,
                'gender': self.gender,
                'chart': self.chart,
                'placement': self.placement,
                'era': self.era,
                'eliminatedFirst': self.eliminatedFirst,
                'pic': self.pic,
                'elimPic': self.elimPic
            }

        @staticmethod
        def from_dict(data):
            return Player(
                name=data['name'],
                skill=data['skill'],
                random=data['random'],
                gender=data['gender'],
                chart=data['chart'],
                placement=data['placement'],
                era=data['era'],
                eliminatedFirst=data['eliminatedFirst'],
                pic=data['pic'],
                elimPic=data['elimPic']
            )
    def parse_json_list(key):
        json_str = request.form.get(key, '[]')
        try:
            return json.loads(json_str)
        except json.JSONDecodeError:
            return []

    # Access form data
    eliminated = parse_json_list('eliminated')
    results = parse_json_list('results')
    week = int(request.form.get('week', 1))
    males = parse_json_list('males')
    females = parse_json_list('females')


    # Reconstruct the original format

    # Initialize males and females if week is 1
    if week == 1:
        males, females = TC40cast()
    else:
        males = [Player.from_dict(player_dict) for player_dict in males]
        females = [Player.from_dict(player_dict) for player_dict in females]
        eliminated = [Player.from_dict(player_dict) for player_dict in eliminated]

    # Update game state

    game_output_display = '\n'.join(results)
    # Generate player results
    num_rounds = week-1
    females = sorted(females, key=lambda player: player.name)
    males = sorted(males, key=lambda player: player.name)
    all_players = males + females + eliminated

        # Initialize player_results with empty results lists
    player_results = {player.name: [''] * num_rounds for player in all_players}

    # Update player_results with the chart field for each player
    for player in all_players:
        # Extend the chart list with empty strings if it's shorter than num_rounds
        player_results[player.name] = player.chart + [''] * (num_rounds - len(player.chart))

    # Sort player_results by player placement
    sorted_player_results = sorted(
        [(player, player_results[player.name]) for player in all_players],
        key=lambda x: x[0].placement
    )

    # Reconstruct player_results dictionary
    player_results = {player.name: results for player, results in sorted_player_results}

    males_json = json.dumps([p.to_dict() for p in males])
    females_json = json.dumps([p.to_dict() for p in females])
    eliminated_json = json.dumps([p.to_dict() for p in eliminated])




    return render_template_string('''
       <!DOCTYPE html>
        <html lang="en">
        <head>
            
        <!-- Google tag (gtag.js) -->
        <script async src="https://www.googletagmanager.com/gtag/js?id=G-RTYFB5MG1F"></script>
        <script>
        window.dataLayer = window.dataLayer || [];
        function gtag(){dataLayer.push(arguments);}
        gtag('js', new Date());

        gtag('config', 'G-RTYFB5MG1F');
        </script>

            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>The Challenge 40 Simulator Results</title>
            <link rel="stylesheet" href="{{ url_for('static', filename='challenge40ResultsStyles.css') }}">
            <script>
        // Function to check if results are empty and disable the buttons
        function toggleContinueButtons() {
            var results = {{ results | tojson }};
            var continueButtons = document.getElementsByClassName('continue-button');
            for (var i = 0; i < continueButtons.length; i++) {
                if (results.length === 0) {
                    continueButtons[i].disabled = true;
                    continueButtons[i].style.cursor = 'not-allowed'; // Optional: change cursor to indicate disabled state
                } else {
                    continueButtons[i].disabled = false;
                    continueButtons[i].style.cursor = 'pointer'; // Reset cursor style
                }
            }
        }

        // Call the function when the page loads
        window.onload = toggleContinueButtons;
    </script>
        </head>
        <body>

            <header>
                <div class="header-title">nathsim.com</div>
                <div class="center-title">The Challenge 40 Simulator</div>
                <div class="header-buttons">
                    <form id="challengeForm" action="{{ url_for('TheChallenge40') }}" method="post">
                    <input type="hidden" name="game_output" id="game_output" value="[]">
                    <input type="hidden" name="eliminated" id="eliminated" value="{{eliminated_json}}">
                    <input type="hidden" name="game_results" id="game_results" value="[]">
                    <input type="hidden" name="week" id="week" value="{{ week }}">
                    <input type="hidden" name="males" id="males" value="{{ males_json }}">
                    <input type="hidden" name="females" id="females" value="{{ females_json }}">
                    <button type="submit" class="continue-button">Continue</button>
                    </form>
                    <a href="{{ url_for('index') }}" style="text-decoration: none;">
                        <button class="back-button">Back to Home</button>
                    </a>
                    <form action="{{ url_for('TheChallenge40') }}" method="post" style="display: inline;">
                        <button class="resimulate-button" type="submit">Resimulate</button>
                    </form>
                </div>
            </header>
            <main>

                {% if results %}
        <div class="game-output-content">
            <p>{{ game_output_display | safe }}</p>
        </div>
    </div>
{% endif %}
                <h1 style="font-size: 2em; text-shadow: 1px 1px 3px #000000;">Results Chart</h1>

                                <table>
                <tr>
                    <th class="round-header">Round</th>
                    {% for round_num in range(1, num_rounds + 1) %}
                        <th class="round-header">{{ round_num }}</th>
                    {% endfor %}
                </tr>
                {% for player_name, results in player_results.items() %}
                    <tr>
                        <td class="name-column">{{ player_name }}</td>
                        {% for result in results %}
                            {% if result == '' %}
                                <td style="background-color: black;"></td>
                            {% else %}
                                <td class="result-cell" 
                                    style="background-color: 
                                        {% if result == 'WIN' %}#00ba37
                                        {% elif result == 'OUT' %}red
                                        {% elif result == 'ELIM' %}lightcoral
                                        {% elif result == 'BTM4' %}orange
                                        {% elif result == 'SAFE' %}white
                                        {% elif result == 'WINNER' %}forestgreen
                                        {% elif result == 'SECOND' %}ghostwhite
                                        {% elif result == 'THIRD' %}goldenrod
                                        {% elif result == 'FOURTH' %}darkseagreen
                                        {% endif %};
                                    ">
                                    {{ result }}
                                </td>
                            {% endif %}
                        {% endfor %}
                    </tr>
                {% endfor %}
            </table>

                </div>
                <form id="challengeForm" action="{{ url_for('TheChallenge40') }}" method="post">
                    <input type="hidden" name="game_output" id="game_output" value="[]">
                    <input type="hidden" name="eliminated" id="eliminated" value="{{eliminated_json}}">
                    <input type="hidden" name="game_results" id="game_results" value="[]">
                    <input type="hidden" name="week" id="week" value="{{ week }}">
                    <input type="hidden" name="males" id="males" value="{{ males_json }}">
                    <input type="hidden" name="females" id="females" value="{{ females_json }}">
                    <button type="submit" class="continue-button">Continue</button>
                </form>
            </main>
            <footer>
                <a href="{{ url_for('index') }}" style="text-decoration: none;">
                    <button class="back-button">Back to Home</button>
                </a>
                <form action="{{ url_for('TheChallenge40') }}" method="post" style="display: inline;">
                    <button class="resimulate-button" type="submit">Resimulate</button>
                </form>
            </footer>
        </body>
        </html>
    ''', player_results=player_results, num_rounds=num_rounds, game_output_display=game_output_display,males_json=males_json, females_json=females_json, week = week,eliminated_json=eliminated_json, results=results)


@app.route('/traitors2', methods=['POST'])
def traitors2():
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
    def parse_json_list(key):
        json_str = request.form.get(key, '[]')
        try:
            return json.loads(json_str)
        except json.JSONDecodeError:
            return []
    game_output = parse_json_list('game_output')
    eliminated = parse_json_list('eliminated')
    week = int(request.form.get('week', 1))
    money = int(request.form.get('money', 0))
    cast = parse_json_list('cast')
    game_results = []

    if week == 1:
        cast = traitors2Cast()
    else:
        cast = [Player.from_dict(player_dict) for player_dict in cast]
        eliminated = [Player.from_dict(player_dict) for player_dict in eliminated]

    game_output, eliminated_cur, game_results, cast,money = traitors(game_output, eliminated, game_results, cast, week,money)
    week += 1
    game_output_display = '\n'.join(game_output)
    cast_json = json.dumps([p.to_dict() for p in cast])
    eliminated_json = json.dumps([p.to_dict() for p in eliminated_cur])
    num_rounds = len(cast[0].chart)
    gameFinished = False
    all_players = cast + eliminated
    # Initialize player_results with player names and empty data
    player_results = {player.name: {'results': [''] * num_rounds, 'isTraitor': player.isTraitor} for player in all_players}
    
    # Update player_results with the chart field for each player
    for player in all_players:
        # Extend the chart list with empty strings if it's shorter than num_rounds
        player_results[player.name]['results'] = player.chart + [''] * (num_rounds - len(player.chart))

    # Sort player_results by player placement
    sorted_player_results = sorted(
        [(player, player_results[player.name]) for player in all_players],
        key=lambda x: x[0].placement
    )
    if week != 2:
        if cast[0].chart[-1] == "WINNER":
            gameFinished = True
        if cast[0].chart[-1] == "RUNNER-UP":
            gameFinished = True
    
    # Reconstruct player_results dictionary, preserving the isTraitor information
    player_results = {player.name: results for player, results in sorted_player_results}

    return render_template_string('''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>The Traitors 2 Simulator Results</title>
            <link rel="stylesheet" href="{{ url_for('static', filename='challenge40ResultsStyles.css') }}">
        </head>
            
        <script>
        
        function toggleContinueButtons() {
            var continueButtons = document.getElementsByClassName('continue-button');
            for (var i = 0; i < continueButtons.length; i++) {
                if ({{ gameFinished|tojson }}) {
                    continueButtons[i].disabled = true;
                    continueButtons[i].style.cursor = 'not-allowed'; // Optional: change cursor to indicate disabled state
                } else {
                    continueButtons[i].disabled = false;
                    continueButtons[i].style.cursor = 'pointer'; // Reset cursor style
                }
            }
        }

        // Call the function when the page loads
        window.onload = toggleContinueButtons;
    </script>

        <body>
            <header>
                <div class="header-title">nathsim.com</div>
                <div class="center-title"> The Traitors Season 2 Simulator </div>
                <div class="header-buttons">
                    <form id="challengeForm" action="{{ url_for('traitors2') }}" method="post">
                    <input type="hidden" name="game_output" id="game_output" value="[]">
                    <input type="hidden" name="eliminated" id="eliminated" value="{{eliminated_json}}">
                    <input type="hidden" name="game_results" id="game_results" value="[]">
                    <input type="hidden" name="week" id="week" value="{{ week }}">
                    <input type="hidden" name="money" id="money" value="{{ money }}">
                    <input type="hidden" name="cast" id="males" value="{{ cast_json }}">
                    <input type="hidden" name="results" id="results" value="{{ results_json }}">
                    <button type="submit" class="continue-button" >Continue</button>
                    </form>
                    <a href="{{ url_for('index') }}" style="text-decoration: none;">
                        <button class="back-button">Back to Home</button>
                    </a>
                    <form action="{{ url_for('traitors2') }}" method="post" style="display: inline;">
                        <button class="resimulate-button" type="submit">Resimulate</button>
                    
                    
                </form>
                <button class="recent-update-button" id="recentUpdateButton">Recent Update</button>
                </div>
                <!-- Space where updates will appear, placed below header (hidden by default) -->
<div id="recentUpdateSection" style="display: none; margin-top: 20px; padding: 10px;"></div>

<!-- Modal for displaying the updates (hidden initially) -->
<div id="recentUpdateModal" style="display:none; padding: 20px; background-color: #f0f0f0; border: 2px solid #ccc; margin-top: 10px;">
    <h3>Recent Updates (1/14/25) </h3>
    <ul>
        <li>Amount of traitors now proportional to the amount of people in cast.</li>
        <li>Upper limit of traitors cast now 50 instead of 26.</li>
        <li>Recruits added if only 1 traitor is left.</li>
        <li>Added third suspicious action during breakfast (increases suspicion).</li>
        <li>Added new suspicious actions.</li>
        <li>Added positive action during breakfast (reduces suspicion).</li>
        <li>Added duo interactions during breakfast (no effect on suspicion).</li>
        <li>1/3 chance for a traitor to get added suspicion during breakfast.</li>
    </ul>
    <button onclick="closeModal()" style="padding: 10px 20px; background-color: #007BFF; color: white; border: none;">Close</button>
</div>

<!-- Add a little styling for the button -->
<style>
    .recent-update-button {
        border: 1px solid #4a7b8c;
        background-color: #D7BFDC;
        color: black;
        border-radius: 5px;
        cursor: pointer;
        transition: background-color 0.3s;
        padding: 4px 8px; /* Reduced padding for smaller button */
        font-size: 14px; /* Smaller font size for button */
    }

    .recent-update-button:hover {
        background-color: #218838;
    }

    #recentUpdateModal {
        background-color: #f8f9fa;
        border-radius: 5px;
        width: 500px;
        margin: 0 auto;
        text-align: left;
    }

    #recentUpdateSection {
        padding: 20px;
        background-color: #f0f0f0;
        border: 1px solid #ccc;
        display: none;  /* Ensure it is hidden initially */
    }

    /* Styling for the text */
    #recentUpdateSection h3,
    #recentUpdateSection ul {
        color: #000; /* Black text for readability */
        font-family: Arial, sans-serif; /* Optional: better font for readability */
        font-size: 16px; /* Adjust font size for better readability */
    }

    #recentUpdateSection li {
        line-height: 1.6; /* Improve readability with some line spacing */
    }

    /* Ensure there's no shadow or unwanted effects on the text */
    #recentUpdateSection * {
        text-shadow: none !important; /* Remove any text shadow */
    }
</style>

<!-- JavaScript to show the modal and display the updates -->
<script>
    document.getElementById("recentUpdateButton").onclick = function() {
        var modal = document.getElementById("recentUpdateModal");
        var updateSection = document.getElementById("recentUpdateSection");

        // Move the modal's content into the update section
        updateSection.innerHTML = modal.innerHTML;

        // Show the section with updates
        updateSection.style.display = "block";
    };

    function closeModal() {
        document.getElementById("recentUpdateSection").style.display = "none";
    }
</script>
                </div>
                
            </header>
            <main>
                <div class="game-output-content" style="background-color: #C0AFE2;">
                <p>{{ game_output_display | safe }}</p>
                </div>
                <h1 style="font-size: 2em;">Voting Chart</h1>
                <table border-collapse: collapse; background-color: white;">
                    <tr>
                        <th class="round-header">Vote</th>
                        {% for round_num in range(1, num_rounds + 1) %}
                            <th class="round-header" style="text-shadow: none;">{{ round_num }}</th>
                        {% endfor %}
                    </tr>
                    {% for player_name, player_data in player_results.items() %}
                        <tr>
                            <!-- Set the background color to red if the player is a traitor -->
                            <td class="name-column" style="background-color: {% if player_data.isTraitor %} red {% else %} lightblue {% endif %};">
                                {{ player_name }}
                            </td>
                            {% for result in player_data.results %}
                                {% if result == '' %}
                                    <td style="background-color: black;"></td>
                                {% else %}
                                    <td style="background-color: 
    {% if result == 'WINNER' %}forestgreen
    {% elif result == 'RUNNER-UP' %}yellow
    {% elif result == 'BANISH' %}tomato
    {% elif result == 'END' %}darkseagreen
    {% else %}white
    {% endif %};
    text-align: center; font-size: 14px;
    color: {% if result == 'WINNER' or result == 'BANISH' or result == 'END' %}white{% else %}black{% endif %};
    text-shadow: {% if result == 'WINNER' or result == 'BANISH' or result == 'END' %}2px 2px 4px rgba(0, 0, 0, 0.5){% else %}none{% endif %};">
    {{ result }}
</td>
                                {% endif %}
                            {% endfor %}
                        </tr>
                    {% endfor %}
                </table>
                <form id="challengeForm" action="{{ url_for('traitors2') }}" method="post">
                    <input type="hidden" name="game_output" id="game_output" value="[]">
                    <input type="hidden" name="eliminated" id="eliminated" value="{{eliminated_json}}">
                    <input type="hidden" name="game_results" id="game_results" value="[]">
                    <input type="hidden" name="week" id="week" value="{{ week }}">
                    <input type="hidden" name="money" id="money" value="{{ money }}">
                    <input type="hidden" name="cast" id="males" value="{{ cast_json }}">
                    <input type="hidden" name="results" id="results" value="{{ results_json }}">
                    <button type="submit" class="continue-button" >Continue</button>
                </form>
                <div style="overflow-x: auto;">
                    
                </div>
            </main>
            <footer>
                <a href="{{ url_for('index') }}" style="text-decoration: none;">
                    <button class="back-button">Back to Home</button>
                </a>
                <form action="{{ url_for('traitors2') }}" method="post" style="display: inline;">
                    <button class="resimulate-button" type="submit">Resimulate</button>
                </form>
            </footer>
        </body>
        </html>
    ''',game_output_display=game_output_display, cast_json=cast_json, week = week,eliminated_json=eliminated_json,num_rounds=num_rounds,player_results=player_results,gameFinished=gameFinished,money=money)

@app.route('/traitors3', methods=['POST'])
def traitors3():
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
    def parse_json_list(key):
        json_str = request.form.get(key, '[]')
        try:
            return json.loads(json_str)
        except json.JSONDecodeError:
            return []
    game_output = parse_json_list('game_output')
    eliminated = parse_json_list('eliminated')
    week = int(request.form.get('week', 1))
    money = int(request.form.get('money', 0))
    cast = parse_json_list('cast')
    game_results = []

    if week == 1:
        cast = traitors3Cast()
    else:
        cast = [Player.from_dict(player_dict) for player_dict in cast]
        eliminated = [Player.from_dict(player_dict) for player_dict in eliminated]

    game_output, eliminated_cur, game_results, cast,money = traitors(game_output, eliminated, game_results, cast, week,money)
    week += 1
    game_output_display = '\n'.join(game_output)
    cast_json = json.dumps([p.to_dict() for p in cast])
    eliminated_json = json.dumps([p.to_dict() for p in eliminated_cur])
    num_rounds = len(cast[0].chart)
    gameFinished = False
    all_players = cast + eliminated
    # Initialize player_results with player names and empty data
    player_results = {player.name: {'results': [''] * num_rounds, 'isTraitor': player.isTraitor} for player in all_players}
    
    # Update player_results with the chart field for each player
    for player in all_players:
        # Extend the chart list with empty strings if it's shorter than num_rounds
        player_results[player.name]['results'] = player.chart + [''] * (num_rounds - len(player.chart))

    # Sort player_results by player placement
    sorted_player_results = sorted(
        [(player, player_results[player.name]) for player in all_players],
        key=lambda x: x[0].placement
    )
    if week != 2:
        if cast[0].chart[-1] == "WINNER":
            gameFinished = True
        if cast[0].chart[-1] == "RUNNER-UP":
            gameFinished = True
    
    # Reconstruct player_results dictionary, preserving the isTraitor information
    player_results = {player.name: results for player, results in sorted_player_results}

    return render_template_string('''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>The Traitors 3 Simulator Results</title>
            <link rel="stylesheet" href="{{ url_for('static', filename='challenge40ResultsStyles.css') }}">
        </head>
            
        <script>
        
        function toggleContinueButtons() {
            var continueButtons = document.getElementsByClassName('continue-button');
            for (var i = 0; i < continueButtons.length; i++) {
                if ({{ gameFinished|tojson }}) {
                    continueButtons[i].disabled = true;
                    continueButtons[i].style.cursor = 'not-allowed'; // Optional: change cursor to indicate disabled state
                } else {
                    continueButtons[i].disabled = false;
                    continueButtons[i].style.cursor = 'pointer'; // Reset cursor style
                }
            }
        }

        // Call the function when the page loads
        window.onload = toggleContinueButtons;
    </script>

        <body>
            <header>
                <div class="header-title">nathsim.com</div>
                <div class="center-title"> The Traitors Season 3 Simulator </div>
                <div class="header-buttons">
                    <form id="challengeForm" action="{{ url_for('traitors3') }}" method="post">
                    <input type="hidden" name="game_output" id="game_output" value="[]">
                    <input type="hidden" name="eliminated" id="eliminated" value="{{eliminated_json}}">
                    <input type="hidden" name="game_results" id="game_results" value="[]">
                    <input type="hidden" name="week" id="week" value="{{ week }}">
                    <input type="hidden" name="money" id="money" value="{{ money }}">
                    <input type="hidden" name="cast" id="males" value="{{ cast_json }}">
                    <input type="hidden" name="results" id="results" value="{{ results_json }}">
                    <button type="submit" class="continue-button" >Continue</button>
                    </form>
                    <a href="{{ url_for('index') }}" style="text-decoration: none;">
                        <button class="back-button">Back to Home</button>
                    </a>
                    <form action="{{ url_for('traitors3') }}" method="post" style="display: inline;">
                        <button class="resimulate-button" type="submit">Resimulate</button>
                    
                    
                </form>
                                  <button class="recent-update-button" id="recentUpdateButton">Recent Update</button>
                </div>
                <!-- Space where updates will appear, placed below header (hidden by default) -->
<div id="recentUpdateSection" style="display: none; margin-top: 20px; padding: 10px;"></div>

<!-- Modal for displaying the updates (hidden initially) -->
<div id="recentUpdateModal" style="display:none; padding: 20px; background-color: #f0f0f0; border: 2px solid #ccc; margin-top: 10px;">
    <h3>Recent Updates (1/14/25) </h3>
    <ul>
        <li>Amount of traitors now proportional to the amount of people in cast.</li>
        <li>Upper limit of traitors cast now 50 instead of 26.</li>
        <li>Recruits added if only 1 traitor is left.</li>
        <li>Added third suspicious action during breakfast (increases suspicion).</li>
        <li>Added new suspicious actions.</li>
        <li>Added positive action during breakfast (reduces suspicion).</li>
        <li>Added duo interactions during breakfast (no effect on suspicion).</li>
        <li>1/3 chance for a traitor to get added suspicion during breakfast.</li>
    </ul>
    <button onclick="closeModal()" style="padding: 10px 20px; background-color: #007BFF; color: white; border: none;">Close</button>
</div>

<!-- Add a little styling for the button -->
<style>
    .recent-update-button {
        border: 1px solid #4a7b8c;
        background-color: #D7BFDC;
        color: black;
        border-radius: 5px;
        cursor: pointer;
        transition: background-color 0.3s;
        padding: 4px 8px; /* Reduced padding for smaller button */
        font-size: 14px; /* Smaller font size for button */
    }

    .recent-update-button:hover {
        background-color: #218838;
    }

    #recentUpdateModal {
        background-color: #f8f9fa;
        border-radius: 5px;
        width: 500px;
        margin: 0 auto;
        text-align: left;
    }

    #recentUpdateSection {
        padding: 20px;
        background-color: #f0f0f0;
        border: 1px solid #ccc;
        display: none;  /* Ensure it is hidden initially */
    }

    /* Styling for the text */
    #recentUpdateSection h3,
    #recentUpdateSection ul {
        color: #000; /* Black text for readability */
        font-family: Arial, sans-serif; /* Optional: better font for readability */
        font-size: 16px; /* Adjust font size for better readability */
    }

    #recentUpdateSection li {
        line-height: 1.6; /* Improve readability with some line spacing */
    }

    /* Ensure there's no shadow or unwanted effects on the text */
    #recentUpdateSection * {
        text-shadow: none !important; /* Remove any text shadow */
    }
</style>

<!-- JavaScript to show the modal and display the updates -->
<script>
    document.getElementById("recentUpdateButton").onclick = function() {
        var modal = document.getElementById("recentUpdateModal");
        var updateSection = document.getElementById("recentUpdateSection");

        // Move the modal's content into the update section
        updateSection.innerHTML = modal.innerHTML;

        // Show the section with updates
        updateSection.style.display = "block";
    };

    function closeModal() {
        document.getElementById("recentUpdateSection").style.display = "none";
    }
</script>
                
            </header>
            <main>
                <div class="game-output-content" style="background-color: #C0AFE2;">
                <p>{{ game_output_display | safe }}</p>
                </div>
                <h1 style="font-size: 2em;">Voting Chart</h1>
                <table border-collapse: collapse; background-color: white;">
                    <tr>
                        <th class="round-header">Vote</th>
                        {% for round_num in range(1, num_rounds + 1) %}
                            <th class="round-header" style="text-shadow: none;">{{ round_num }}</th>
                        {% endfor %}
                    </tr>
                    {% for player_name, player_data in player_results.items() %}
                        <tr>
                            <!-- Set the background color to red if the player is a traitor -->
                            <td class="name-column" style="background-color: {% if player_data.isTraitor %} red {% else %} lightblue {% endif %};">
                                {{ player_name }}
                            </td>
                            {% for result in player_data.results %}
                                {% if result == '' %}
                                    <td style="background-color: black;"></td>
                                {% else %}
                                    <td style="background-color: 
    {% if result == 'WINNER' %}forestgreen
    {% elif result == 'RUNNER-UP' %}yellow
    {% elif result == 'BANISH' %}tomato
    {% elif result == 'END' %}darkseagreen
    {% else %}white
    {% endif %};
    text-align: center; font-size: 14px;
    color: {% if result == 'WINNER' or result == 'BANISH' or result == 'END' %}white{% else %}black{% endif %};
    text-shadow: {% if result == 'WINNER' or result == 'BANISH' or result == 'END' %}2px 2px 4px rgba(0, 0, 0, 0.5){% else %}none{% endif %};">
    {{ result }}
</td>
                                {% endif %}
                            {% endfor %}
                        </tr>
                    {% endfor %}
                </table>
                <form id="challengeForm" action="{{ url_for('traitors3') }}" method="post">
                    <input type="hidden" name="game_output" id="game_output" value="[]">
                    <input type="hidden" name="eliminated" id="eliminated" value="{{eliminated_json}}">
                    <input type="hidden" name="game_results" id="game_results" value="[]">
                    <input type="hidden" name="week" id="week" value="{{ week }}">
                    <input type="hidden" name="money" id="money" value="{{ money }}">
                    <input type="hidden" name="cast" id="males" value="{{ cast_json }}">
                    <input type="hidden" name="results" id="results" value="{{ results_json }}">
                    <button type="submit" class="continue-button" >Continue</button>
                </form>
                <div style="overflow-x: auto;">
                    
                </div>
            </main>
            <footer>
                <a href="{{ url_for('index') }}" style="text-decoration: none;">
                    <button class="back-button">Back to Home</button>
                </a>
                <form action="{{ url_for('traitors3') }}" method="post" style="display: inline;">
                    <button class="resimulate-button" type="submit">Resimulate</button>
                </form>
            </footer>
        </body>
        </html>
    ''',game_output_display=game_output_display, cast_json=cast_json, week = week,eliminated_json=eliminated_json,num_rounds=num_rounds,player_results=player_results,gameFinished=gameFinished,money=money)

@app.route('/traitors1', methods=['POST'])
def traitors1():
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
    def parse_json_list(key):
        json_str = request.form.get(key, '[]')
        try:
            return json.loads(json_str)
        except json.JSONDecodeError:
            return []
    game_output = parse_json_list('game_output')
    eliminated = parse_json_list('eliminated')
    week = int(request.form.get('week', 1))
    money = int(request.form.get('money', 0))
    cast = parse_json_list('cast')
    game_results = []

    if week == 1:
        cast = traitors1Cast()
    else:
        cast = [Player.from_dict(player_dict) for player_dict in cast]
        eliminated = [Player.from_dict(player_dict) for player_dict in eliminated]

    game_output, eliminated_cur, game_results, cast,money = traitors(game_output, eliminated, game_results, cast, week,money)
    week += 1
    game_output_display = '\n'.join(game_output)
    cast_json = json.dumps([p.to_dict() for p in cast])
    eliminated_json = json.dumps([p.to_dict() for p in eliminated_cur])
    num_rounds = len(cast[0].chart)
    gameFinished = False
    all_players = cast + eliminated
    # Initialize player_results with player names and empty data
    player_results = {player.name: {'results': [''] * num_rounds, 'isTraitor': player.isTraitor} for player in all_players}
    
    # Update player_results with the chart field for each player
    for player in all_players:
        # Extend the chart list with empty strings if it's shorter than num_rounds
        player_results[player.name]['results'] = player.chart + [''] * (num_rounds - len(player.chart))

    # Sort player_results by player placement
    sorted_player_results = sorted(
        [(player, player_results[player.name]) for player in all_players],
        key=lambda x: x[0].placement
    )
    if week != 2:
        if cast[0].chart[-1] == "WINNER":
            gameFinished = True
        if cast[0].chart[-1] == "RUNNER-UP":
            gameFinished = True
    
    # Reconstruct player_results dictionary, preserving the isTraitor information
    player_results = {player.name: results for player, results in sorted_player_results}

    return render_template_string('''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>The Traitors 2 Simulator Results</title>
            <link rel="stylesheet" href="{{ url_for('static', filename='challenge40ResultsStyles.css') }}">
        </head>
            
        <script>
        
        function toggleContinueButtons() {
            var continueButtons = document.getElementsByClassName('continue-button');
            for (var i = 0; i < continueButtons.length; i++) {
                if ({{ gameFinished|tojson }}) {
                    continueButtons[i].disabled = true;
                    continueButtons[i].style.cursor = 'not-allowed'; // Optional: change cursor to indicate disabled state
                } else {
                    continueButtons[i].disabled = false;
                    continueButtons[i].style.cursor = 'pointer'; // Reset cursor style
                }
            }
        }

        // Call the function when the page loads
        window.onload = toggleContinueButtons;
    </script>

        <body>
            <header>
                <div class="header-title">nathsim.com</div>
                <div class="center-title"> The Traitors Season 1 Simulator </div>
                <div class="header-buttons">
                    <form id="challengeForm" action="{{ url_for('traitors1') }}" method="post">
                    <input type="hidden" name="game_output" id="game_output" value="[]">
                    <input type="hidden" name="eliminated" id="eliminated" value="{{eliminated_json}}">
                    <input type="hidden" name="game_results" id="game_results" value="[]">
                    <input type="hidden" name="week" id="week" value="{{ week }}">
                    <input type="hidden" name="money" id="money" value="{{ money }}">
                    <input type="hidden" name="cast" id="males" value="{{ cast_json }}">
                    <input type="hidden" name="results" id="results" value="{{ results_json }}">
                    <button type="submit" class="continue-button" >Continue</button>
                    </form>
                    <a href="{{ url_for('index') }}" style="text-decoration: none;">
                        <button class="back-button">Back to Home</button>
                    </a>
                    <form action="{{ url_for('traitors1') }}" method="post" style="display: inline;">
                        <button class="resimulate-button" type="submit">Resimulate</button>
                    
                    
                </form>
                <button class="recent-update-button" id="recentUpdateButton">Recent Update</button>
                </div>
                <!-- Space where updates will appear, placed below header (hidden by default) -->
<div id="recentUpdateSection" style="display: none; margin-top: 20px; padding: 10px;"></div>

<!-- Modal for displaying the updates (hidden initially) -->
<div id="recentUpdateModal" style="display:none; padding: 20px; background-color: #f0f0f0; border: 2px solid #ccc; margin-top: 10px;">
    <h3>Recent Updates (1/14/25) </h3>
    <ul>
        <li>Amount of traitors now proportional to the amount of people in cast.</li>
        <li>Upper limit of traitors cast now 50 instead of 26.</li>
        <li>Recruits added if only 1 traitor is left.</li>
        <li>Added third suspicious action during breakfast (increases suspicion).</li>
        <li>Added new suspicious actions.</li>
        <li>Added positive action during breakfast (reduces suspicion).</li>
        <li>Added duo interactions during breakfast (no effect on suspicion).</li>
        <li>1/3 chance for a traitor to get added suspicion during breakfast.</li>
    </ul>
    <button onclick="closeModal()" style="padding: 10px 20px; background-color: #007BFF; color: white; border: none;">Close</button>
</div>

<!-- Add a little styling for the button -->
<style>
    .recent-update-button {
        border: 1px solid #4a7b8c;
        background-color: #D7BFDC;
        color: black;
        border-radius: 5px;
        cursor: pointer;
        transition: background-color 0.3s;
        padding: 4px 8px; /* Reduced padding for smaller button */
        font-size: 14px; /* Smaller font size for button */
    }

    .recent-update-button:hover {
        background-color: #218838;
    }

    #recentUpdateModal {
        background-color: #f8f9fa;
        border-radius: 5px;
        width: 500px;
        margin: 0 auto;
        text-align: left;
    }

    #recentUpdateSection {
        padding: 20px;
        background-color: #f0f0f0;
        border: 1px solid #ccc;
        display: none;  /* Ensure it is hidden initially */
    }

    /* Styling for the text */
    #recentUpdateSection h3,
    #recentUpdateSection ul {
        color: #000; /* Black text for readability */
        font-family: Arial, sans-serif; /* Optional: better font for readability */
        font-size: 16px; /* Adjust font size for better readability */
    }

    #recentUpdateSection li {
        line-height: 1.6; /* Improve readability with some line spacing */
    }

    /* Ensure there's no shadow or unwanted effects on the text */
    #recentUpdateSection * {
        text-shadow: none !important; /* Remove any text shadow */
    }
</style>

<!-- JavaScript to show the modal and display the updates -->
<script>
    document.getElementById("recentUpdateButton").onclick = function() {
        var modal = document.getElementById("recentUpdateModal");
        var updateSection = document.getElementById("recentUpdateSection");

        // Move the modal's content into the update section
        updateSection.innerHTML = modal.innerHTML;

        // Show the section with updates
        updateSection.style.display = "block";
    };

    function closeModal() {
        document.getElementById("recentUpdateSection").style.display = "none";
    }
</script>
                </div>
                
            </header>
            <main>
                <div class="game-output-content" style="background-color: #C0AFE2;">
                <p>{{ game_output_display | safe }}</p>
                </div>
                <h1 style="font-size: 2em;">Voting Chart</h1>
                <table border-collapse: collapse; background-color: white;">
                    <tr>
                        <th class="round-header">Vote</th>
                        {% for round_num in range(1, num_rounds + 1) %}
                            <th class="round-header" style="text-shadow: none;">{{ round_num }}</th>
                        {% endfor %}
                    </tr>
                    {% for player_name, player_data in player_results.items() %}
                        <tr>
                            <!-- Set the background color to red if the player is a traitor -->
                            <td class="name-column" style="background-color: {% if player_data.isTraitor %} red {% else %} lightblue {% endif %};">
                                {{ player_name }}
                            </td>
                            {% for result in player_data.results %}
                                {% if result == '' %}
                                    <td style="background-color: black;"></td>
                                {% else %}
                                    <td style="background-color: 
    {% if result == 'WINNER' %}forestgreen
    {% elif result == 'RUNNER-UP' %}yellow
    {% elif result == 'BANISH' %}tomato
    {% elif result == 'END' %}darkseagreen
    {% else %}white
    {% endif %};
    text-align: center; font-size: 14px;
    color: {% if result == 'WINNER' or result == 'BANISH' or result == 'END' %}white{% else %}black{% endif %};
    text-shadow: {% if result == 'WINNER' or result == 'BANISH' or result == 'END' %}2px 2px 4px rgba(0, 0, 0, 0.5){% else %}none{% endif %};">
    {{ result }}
</td>
                                {% endif %}
                            {% endfor %}
                        </tr>
                    {% endfor %}
                </table>
                <form id="challengeForm" action="{{ url_for('traitors1') }}" method="post">
                    <input type="hidden" name="game_output" id="game_output" value="[]">
                    <input type="hidden" name="eliminated" id="eliminated" value="{{eliminated_json}}">
                    <input type="hidden" name="game_results" id="game_results" value="[]">
                    <input type="hidden" name="week" id="week" value="{{ week }}">
                    <input type="hidden" name="money" id="money" value="{{ money }}">
                    <input type="hidden" name="cast" id="males" value="{{ cast_json }}">
                    <input type="hidden" name="results" id="results" value="{{ results_json }}">
                    <button type="submit" class="continue-button" >Continue</button>
                </form>
                <div style="overflow-x: auto;">
                    
                </div>
            </main>
            <footer>
                <a href="{{ url_for('index') }}" style="text-decoration: none;">
                    <button class="back-button">Back to Home</button>
                </a>
                <form action="{{ url_for('traitors1') }}" method="post" style="display: inline;">
                    <button class="resimulate-button" type="submit">Resimulate</button>
                </form>
            </footer>
        </body>
        </html>
    ''',game_output_display=game_output_display, cast_json=cast_json, week = week,eliminated_json=eliminated_json,num_rounds=num_rounds,player_results=player_results,gameFinished=gameFinished,money=money)
from flask import Flask, request, render_template_string


app.secret_key = 'your_secret_key_here'

@app.route('/enter_names', methods=['GET', 'POST'])
def enter_names():
    # Initialize the lists to store names and pictures from the session
    if 'names' not in session:
        session['names'] = []
    if 'pictures' not in session:
        session['pictures'] = []

    if request.method == 'POST':
        if 'reset' in request.form:
            # Reset the session data when the reset button is clicked
            session['names'] = []
            session['pictures'] = []
            session.modified = True  # Mark the session as modified
            return redirect(url_for('enter_names'))  # Refresh the page to clear the data
        
        if 'remove_previous' in request.form:
            # Remove the last name and picture if available
            if session['names']:
                session['names'].pop()
                session['pictures'].pop()
                session.modified = True  # Mark the session as modified

        else:
            # Get the entered name and picture URL from the form
            name = request.form.get('name')
            picture = request.form.get('picture')

            # If no picture is provided, set it as an empty string
            if picture == '':
                picture = ""

            # Check if the name already exists in the list
            if name in session['names']:
                flash(f"The name '{name}' already exists. Please choose a unique name.", "error")
            elif name and len(session['names']) < 50:
                # Only append if the name is unique and the list has space for 20 people
                session['names'].append(name)
                session['pictures'].append(picture)
                session.modified = True  # Mark the session as modified

    # Create a list of pairs (name, picture) to pass to the template
    cast = list(zip(session['names'], session['pictures']))

    # Render the form and the accumulated names and pictures
    return render_template_string('''
        <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>The Traitors 2 Simulator Results</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='challenge40ResultsStyles.css') }}">
</head>

<body>
    <header>
        <div class="header-title">nathsim.com</div>
        <div class="center-title"> The Traitors Custom Simulator </div>
        <div class="header-buttons">
            <!-- Back to Home Button -->
            <a href="{{ url_for('index') }}" style="text-decoration: none;">
                <button class="back-button">Back to Home</button>
            </a>

            <!-- Resimulate Button -->
            <form action="{{ url_for('traitors2') }}" method="post" style="display: inline;">
                <button class="resimulate-button" type="submit">Resimulate</button>
            </form>
        </div>
    </header>
<h1> Traitors Custom Simulator </h1>
                                  <h3> Note: If the image doesn't show up, it probably isn't a valid image. Remove the person and try again. </h3>
    <form method="POST">
        <label for="name">Enter Name:</label>
        <input name="name" placeholder="Enter name" id="nameInput" autofocus><br><br>
        
        <label for="picture">Enter Picture URL (optional):</label>
        <input name="picture" placeholder="Enter picture URL (optional)"><br><br>
        
        <!-- Reset button to clear the form -->
        <input type="submit" value="Add">
        <button type="submit" name="reset" value="1">Reset</button>
        <button type="submit" name="remove_previous" value="1">Remove Previous</button>
    </form>
    
    {% if cast %}
        <h2>Cast:</h2>
        <ul>
            {% for name, picture in cast %}
                <li><b>{{ name }}</b>: 
                    {% if picture %}
                        <img src="{{ picture }}" alt="{{ name }}" width="100">
                    {% else %}
                        No picture provided
                    {% endif %}
                </li>
            {% endfor %}
        </ul>

        <!-- Display the count of names in the list -->
        <h3>Total Players: {{ cast|length }}</h3>
    {% endif %}

    {% if names|length >= 50 %}
        <h3>Max number of players reached (50)</h3>
    {% endif %}

    {% if names|length >= 16 and names|length <= 50 %}
        <!-- Button to pass data to traitorsCustom, visible only if there are between 16 and 50 names -->
        <form method="POST" action="{{ url_for('traitorsCustom') }}">
            <!-- Pass names and pictures as hidden fields -->
            <input type="hidden" name="names" value="{{ names|join(',') }}">
            <input type="hidden" name="pictures" value="{{ pictures|join(',') }}">
            <button type="submit">Submit to Custom Simulator</button>
        </form>
    {% else %}
        <p>Please add between 16 and 50 players before submitting to the Custom Simulator.</p>
    {% endif %}

    <!-- Display Flash messages -->
    {% with messages = get_flashed_messages(with_categories=true) %}
        {% if messages %}
            <ul class="flashes">
            {% for category, message in messages %}
                <li class="{{ category }}">{{ message }}</li>
            {% endfor %}
            </ul>
        {% endif %}
    {% endwith %}

    <!-- Script to focus the input box on page load -->
    <script>
        document.getElementById('nameInput').focus();
    </script>
</body>
</html>
    ''', names=session['names'], pictures=session['pictures'], cast=cast)
    
@app.route('/traitorsCustom', methods=['POST'])
def traitorsCustom():
    names = request.form.get('names', '').split(',')
    pictures = request.form.get('pictures', '').split(',')

    # Create a list of pairs (name, picture)
    cast = list(zip(names, pictures))

    print(names)
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
    def parse_json_list(key):
        json_str = request.form.get(key, '[]')
        try:
            return json.loads(json_str)
        except json.JSONDecodeError:
            return []
    game_output = parse_json_list('game_output')
    eliminated = parse_json_list('eliminated')
    week = int(request.form.get('week', 1))
    money = int(request.form.get('money', 0))
    cast = parse_json_list('cast')
    game_results = []


    if week == 1:
        for i, name in enumerate(names):
            picture = pictures[i] if i < len(pictures) else ""

            # Set default values for other player attributes
            player = Player(
                name=name,
                skill=80,  # Example default value for skill
                random=0,  # Random value for 'random' attribute
                chart=[],  # Empty chart for now
                placement=0,  # Default placement
                suspicion=0,  # Default suspicion
                pic=f'<img src="{picture}" alt="Game Image" width="120" height="120" />' if picture else '',
                elimPic=f'<img src="{picture}" alt="BW Image" width="120" height="120" style="filter: grayscale(100%);" />' if picture else '',
                isTraitor=False,  # Default value for isTraitor
                isImmune=False   # Default value for isImmune
            )
            cast.append(player)
    
    else:
        cast = [Player.from_dict(player_dict) for player_dict in cast]
        eliminated = [Player.from_dict(player_dict) for player_dict in eliminated]
    print(cast)
    game_output, eliminated_cur, game_results, cast,money = traitors(game_output, eliminated, game_results, cast, week,money)
    week += 1
    game_output_display = '\n'.join(game_output)
    cast_json = json.dumps([p.to_dict() for p in cast])
    eliminated_json = json.dumps([p.to_dict() for p in eliminated_cur])
    num_rounds = len(cast[0].chart)
    gameFinished = False
    all_players = cast + eliminated
    # Initialize player_results with player names and empty data
    player_results = {player.name: {'results': [''] * num_rounds, 'isTraitor': player.isTraitor} for player in all_players}
    
    # Update player_results with the chart field for each player
    for player in all_players:
        # Extend the chart list with empty strings if it's shorter than num_rounds
        player_results[player.name]['results'] = player.chart + [''] * (num_rounds - len(player.chart))

    # Sort player_results by player placement
    sorted_player_results = sorted(
        [(player, player_results[player.name]) for player in all_players],
        key=lambda x: x[0].placement
    )
    if week != 2:
        if cast[0].chart[-1] == "WINNER":
            gameFinished = True
        if cast[0].chart[-1] == "RUNNER-UP":
            gameFinished = True
    
    # Reconstruct player_results dictionary, preserving the isTraitor information
    player_results = {player.name: results for player, results in sorted_player_results}

    return render_template_string('''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>The Traitors 2 Simulator Results</title>
            <link rel="stylesheet" href="{{ url_for('static', filename='challenge40ResultsStyles.css') }}">
        </head>
            
        <script>
        
        function toggleContinueButtons() {
            var continueButtons = document.getElementsByClassName('continue-button');
            for (var i = 0; i < continueButtons.length; i++) {
                if ({{ gameFinished|tojson }}) {
                    continueButtons[i].disabled = true;
                    continueButtons[i].style.cursor = 'not-allowed'; // Optional: change cursor to indicate disabled state
                } else {
                    continueButtons[i].disabled = false;
                    continueButtons[i].style.cursor = 'pointer'; // Reset cursor style
                }
            }
        }

        // Call the function when the page loads
        window.onload = toggleContinueButtons;
    </script>

        <body>
            <header>
                <div class="header-title">nathsim.com</div>
                <div class="center-title"> The Traitors Custom Simulator </div>
                <div class="header-buttons">
                    <form id="challengeForm" action="{{ url_for('traitorsCustom') }}" method="post">
                    <input type="hidden" name="game_output" id="game_output" value="[]">
                    <input type="hidden" name="eliminated" id="eliminated" value="{{eliminated_json}}">
                    <input type="hidden" name="game_results" id="game_results" value="[]">
                    <input type="hidden" name="week" id="week" value="{{ week }}">
                    <input type="hidden" name="money" id="money" value="{{ money }}">
                    <input type="hidden" name="cast" id="males" value="{{ cast_json }}">
                    <input type="hidden" name="results" id="results" value="{{ results_json }}">
                    <button type="submit" class="continue-button" >Continue</button>
                    </form>
                    <a href="{{ url_for('index') }}" style="text-decoration: none;">
                        <button class="back-button">Back to Home</button>
                    </a>
                    
                    
                    
                </form>
                <button class="recent-update-button" id="recentUpdateButton">Recent Update</button>
                </div>
                <!-- Space where updates will appear, placed below header (hidden by default) -->
<div id="recentUpdateSection" style="display: none; margin-top: 20px; padding: 10px;"></div>

<!-- Modal for displaying the updates (hidden initially) -->
<div id="recentUpdateModal" style="display:none; padding: 20px; background-color: #f0f0f0; border: 2px solid #ccc; margin-top: 10px;">
    <h3>Recent Updates (1/14/25) </h3>
    <ul>
        <li>Amount of traitors now proportional to the amount of people in cast.</li>
        <li>Upper limit of traitors cast now 50 instead of 26.</li>
        <li>Recruits added if only 1 traitor is left.</li>
        <li>Added third suspicious action during breakfast (increases suspicion).</li>
        <li>Added new suspicious actions.</li>
        <li>Added positive action during breakfast (reduces suspicion).</li>
        <li>Added duo interactions during breakfast (no effect on suspicion).</li>
        <li>1/3 chance for a traitor to get added suspicion during breakfast.</li>
    </ul>
    <button onclick="closeModal()" style="padding: 10px 20px; background-color: #007BFF; color: white; border: none;">Close</button>
</div>

<!-- Add a little styling for the button -->
<style>
    .recent-update-button {
        border: 1px solid #4a7b8c;
        background-color: #D7BFDC;
        color: black;
        border-radius: 5px;
        cursor: pointer;
        transition: background-color 0.3s;
        padding: 4px 8px; /* Reduced padding for smaller button */
        font-size: 14px; /* Smaller font size for button */
    }

    .recent-update-button:hover {
        background-color: #218838;
    }

    #recentUpdateModal {
        background-color: #f8f9fa;
        border-radius: 5px;
        width: 500px;
        margin: 0 auto;
        text-align: left;
    }

    #recentUpdateSection {
        padding: 20px;
        background-color: #f0f0f0;
        border: 1px solid #ccc;
        display: none;  /* Ensure it is hidden initially */
    }

    /* Styling for the text */
    #recentUpdateSection h3,
    #recentUpdateSection ul {
        color: #000; /* Black text for readability */
        font-family: Arial, sans-serif; /* Optional: better font for readability */
        font-size: 16px; /* Adjust font size for better readability */
    }

    #recentUpdateSection li {
        line-height: 1.6; /* Improve readability with some line spacing */
    }

    /* Ensure there's no shadow or unwanted effects on the text */
    #recentUpdateSection * {
        text-shadow: none !important; /* Remove any text shadow */
    }
</style>

<!-- JavaScript to show the modal and display the updates -->
<script>
    document.getElementById("recentUpdateButton").onclick = function() {
        var modal = document.getElementById("recentUpdateModal");
        var updateSection = document.getElementById("recentUpdateSection");

        // Move the modal's content into the update section
        updateSection.innerHTML = modal.innerHTML;

        // Show the section with updates
        updateSection.style.display = "block";
    };

    function closeModal() {
        document.getElementById("recentUpdateSection").style.display = "none";
    }
</script>
                </div>
                
            </header>
            <main>
                <div class="game-output-content" style="background-color: #0504AA;">
                <p>{{ game_output_display | safe }}</p>
                </div>
                <h1 style="font-size: 2em;">Voting Chart</h1>
                <table border-collapse: collapse; background-color: white;">
                    <tr>
                        <th class="round-header">Vote</th>
                        {% for round_num in range(1, num_rounds + 1) %}
                            <th class="round-header" style="text-shadow: none;">{{ round_num }}</th>
                        {% endfor %}
                    </tr>
                    {% for player_name, player_data in player_results.items() %}
                        <tr>
                            <!-- Set the background color to red if the player is a traitor -->
                            <td class="name-column" style="background-color: {% if player_data.isTraitor %} red {% else %} lightblue {% endif %};">
                                {{ player_name }}
                            </td>
                            {% for result in player_data.results %}
                                {% if result == '' %}
                                    <td style="background-color: black;"></td>
                                {% else %}
                                    <td style="background-color: 
    {% if result == 'WINNER' %}forestgreen
    {% elif result == 'RUNNER-UP' %}yellow
    {% elif result == 'BANISH' %}tomato
    {% elif result == 'END' %}darkseagreen
    {% else %}white
    {% endif %};
    text-align: center; font-size: 14px;
    color: {% if result == 'WINNER' or result == 'BANISH' or result == 'END' %}white{% else %}black{% endif %};
    text-shadow: {% if result == 'WINNER' or result == 'BANISH' or result == 'END' %}2px 2px 4px rgba(0, 0, 0, 0.5){% else %}none{% endif %};">
    {{ result }}
</td>
                                {% endif %}
                            {% endfor %}
                        </tr>
                    {% endfor %}
                </table>
                <form id="challengeForm" action="{{ url_for('traitorsCustom') }}" method="post">
                    <input type="hidden" name="game_output" id="game_output" value="[]">
                    <input type="hidden" name="eliminated" id="eliminated" value="{{eliminated_json}}">
                    <input type="hidden" name="game_results" id="game_results" value="[]">
                    <input type="hidden" name="week" id="week" value="{{ week }}">
                    <input type="hidden" name="money" id="money" value="{{ money }}">
                    <input type="hidden" name="cast" id="males" value="{{ cast_json }}">
                    <input type="hidden" name="results" id="results" value="{{ results_json }}">
                    <button type="submit" class="continue-button" >Continue</button>
                </form>
                <div style="overflow-x: auto;">
                    
                </div>
            </main>
            <footer>
                <a href="{{ url_for('index') }}" style="text-decoration: none;">
                    <button class="back-button">Back to Home</button>
                </a>
                
            </footer>
        </body>
        </html>
    ''',game_output_display=game_output_display, cast_json=cast_json, week = week,eliminated_json=eliminated_json,num_rounds=num_rounds,player_results=player_results,gameFinished=gameFinished,money=money)



@app.route('/mole2', methods=['POST'])
def mole2sim():
    # Simulate the game and get the results
    game_result, game_results, cast = mole2()

    # Join the game results for display
    game_result_display = '\n'.join(game_result)

    num_rounds = len(game_results)

    # Initialize player results
    player_results = {player.name: [''] * num_rounds for player in cast}

    # Populate player results
    for round_num, round_results in enumerate(game_results):
        for player, result in round_results:
            if player.name in player_results:
                player_results[player.name][round_num] = result

    # Sort player results by placement or any other criteria
    sorted_player_results = sorted(
        [(player, player_results[player.name]) for player in cast],
        key=lambda x: x[0].placement  # Adjust based on actual sorting criteria
    )

    player_results = {player.name: results for player, results in sorted_player_results}

    return render_template_string('''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>The Mole 2 Simulator Results</title>
            <style>
                body {
                    background-color: #2c3e50;
                    color: white;
                    margin: 0;
                    padding: 0;
                    font-family: 'Roboto', sans-serif;
                    text-shadow: 2px 2px 4px #000000;
                }
                header {
                    background: linear-gradient(135deg, #1fd655, #16c43c);
                    display: flex;
                    justify-content: space-between;
                    align-items: center;
                    padding: 10px 20px;
                    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
                    position: fixed;
                    top: 0;
                    left: 0;
                    width: calc(100% - 1px);
                    z-index: 1000;
                    box-sizing: border-box;
                    font-weight: bold;
                }
                .header-title {
                    font-family: 'Montserrat', sans-serif;
                    font-weight: bold;
                    font-size: 20px;
                    margin: 0;
                }
                .center-title {
                    text-align: center;
                    flex-grow: 1;
                    font-size: 25px;
                    margin: 0;
                    padding-left: 90px;
                }
                .header-buttons {
                    display: flex;
                    gap: 10px;
                }
                main {
                    margin-top: 80px;
                    text-align: center;
                }
                table {
                    margin: 20px auto;
                    border-collapse: collapse;
                    width: 80%;
                    text-align: center;
                    font-size: 18px;
                }
                th, td {
                    border: 1px solid #dddddd;
                    padding: 10px;
                }
                th {
                    background-color: #72aee6;
                    color: white;
                    font-size: 20px;
                }
                td.name-column {
                    text-align: left;
                    background-color: ghostwhite;
                }
                td {
                    background-color: #f5f5f5; /* Very light gray */
                }
                .result-cell {
                    text-align: center;
                    font-size: 18px;
                    text-shadow: 1px 1px 3px #000000; /* Added text shadow */
                }
                .back-button {
                    background-color: darkgreen;
                    color: white;
                    border: orange;
                    border-radius: 5px;
                    cursor: pointer;
                    transition: background-color 0.3s;
                    padding: 5px 10px;
                }
                .resimulate-button {
                    background-color: white;
                    color: black;
                    border: orange;
                    border-radius: 5px;
                    cursor: pointer;
                    transition: background-color 0.3s;
                    padding: 5px 10px;
                }
                button:hover {
                    opacity: 0.9;
                }
                footer {
                    text-align: center;
                    margin: 20px;
                }
            </style>
        </head>
        <body>
            <header>
                <div class="header-title">nathsim.com</div>
                <div class="center-title">The Mole Season 2 Simulator</div>
                <div class="header-buttons">
                    <a href="{{ url_for('index') }}" style="text-decoration: none;">
                        <button class="back-button">Back to Home</button>
                    </a>
                    <form action="{{ url_for('mole2sim') }}" method="post" style="display: inline;">
                        <button class="resimulate-button" type="submit">Resimulate</button>
                    </form>
                </div>
            </header>
            <main>
                <p>{{ game_result_display | safe }}</p>
                <h1 style="font-size: 2em; text-shadow: 1px 1px 3px #000000;">Results Chart</h1>
                <div style="overflow-x: auto;">
                    <table>
                        <tr>
                            <th class="round-header">Round</th>
                            {% for round_num in range(1, num_rounds + 1) %}
                                <th class="round-header">{{ round_num }}</th>
                            {% endfor %}
                        </tr>
                        {% for player_name, results in player_results.items() %}
                            <tr>
                                <td class="name-column">{{ player_name }}</td>
                                {% for result in results %}
                                    {% if result == '' %}
                                        <td style="background-color: black;"></td>
                                    {% else %}
                                        <td class="result-cell" style="background-color:
                                            {% if result == 'WIN' %}#00ba37
                                            {% elif result == 'ELIM' %}red
                                            {% elif result == 'WINNER' %}blue
                                            {% elif result == 'IN' %}white
                                            {% elif result == 'MOLE' %}yellow
                                            {% endif %};">
                                            {{ result }}
                                        </td>
                                    {% endif %}
                                {% endfor %}
                            </tr>
                        {% endfor %}
                    </table>
                </div>
            </main>
            <footer>
                <a href="{{ url_for('index') }}" style="text-decoration: none;">
                    <button class="back-button">Back to Home</button>
                </a>
                <form action="{{ url_for('mole2sim') }}" method="post" style="display: inline;">
                    <button class="resimulate-button" type="submit">Resimulate</button>
                </form>
            </footer>
        </body>
        </html>
    ''', player_results=player_results, num_rounds=num_rounds, game_result_display=game_result_display)

@app.route('/mole1', methods=['POST'])
def mole1sim():
    # Simulate the game and get the results
    game_result, game_results, cast = mole1()

    # Join the game results for display
    game_result_display = '\n'.join(game_result)

    num_rounds = len(game_results)

    # Initialize player results
    player_results = {player.name: [''] * num_rounds for player in cast}

    # Populate player results
    for round_num, round_results in enumerate(game_results):
        for player, result in round_results:
            if player.name in player_results:
                player_results[player.name][round_num] = result

    # Sort player results by placement or any other criteria
    sorted_player_results = sorted(
        [(player, player_results[player.name]) for player in cast],
        key=lambda x: x[0].placement  # Adjust based on actual sorting criteria
    )

    player_results = {player.name: results for player, results in sorted_player_results}

    return render_template_string('''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>The Mole 2 Simulator Results</title>
            <style>
                body {
                    background-color: #2c3e50;
                    color: white;
                    margin: 0;
                    padding: 0;
                    font-family: 'Roboto', sans-serif;
                    text-shadow: 2px 2px 4px #000000;
                }
                header {
                    background: linear-gradient(135deg, #1fd655, #16c43c);
                    display: flex;
                    justify-content: space-between;
                    align-items: center;
                    padding: 10px 20px;
                    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
                    position: fixed;
                    top: 0;
                    left: 0;
                    width: calc(100% - 1px);
                    z-index: 1000;
                    box-sizing: border-box;
                    font-weight: bold;
                }
                .header-title {
                    font-family: 'Montserrat', sans-serif;
                    font-weight: bold;
                    font-size: 20px;
                    margin: 0;
                }
                .center-title {
                    text-align: center;
                    flex-grow: 1;
                    font-size: 25px;
                    margin: 0;
                    padding-left: 90px;
                }
                .header-buttons {
                    display: flex;
                    gap: 10px;
                }
                main {
                    margin-top: 80px;
                    text-align: center;
                }
                table {
                    margin: 20px auto;
                    border-collapse: collapse;
                    width: 80%;
                    text-align: center;
                    font-size: 18px;
                }
                th, td {
                    border: 1px solid #dddddd;
                    padding: 10px;
                }
                th {
                    background-color: #72aee6;
                    color: white;
                    font-size: 20px;
                }
                td.name-column {
                    text-align: left;
                    background-color: ghostwhite;
                }
                td {
                    background-color: #f5f5f5; /* Very light gray */
                }
                .result-cell {
                    text-align: center;
                    font-size: 18px;
                    text-shadow: 1px 1px 3px #000000; /* Added text shadow */
                }
                .back-button {
                    background-color: darkgreen;
                    color: white;
                    border: orange;
                    border-radius: 5px;
                    cursor: pointer;
                    transition: background-color 0.3s;
                    padding: 5px 10px;
                }
                .resimulate-button {
                    background-color: white;
                    color: black;
                    border: orange;
                    border-radius: 5px;
                    cursor: pointer;
                    transition: background-color 0.3s;
                    padding: 5px 10px;
                }
                button:hover {
                    opacity: 0.9;
                }
                footer {
                    text-align: center;
                    margin: 20px;
                }
            </style>
        </head>
        <body>
            <header>
                <div class="header-title">nathsim.com</div>
                <div class="center-title">The Mole Season 1 Simulator</div>
                <div class="header-buttons">
                    <a href="{{ url_for('index') }}" style="text-decoration: none;">
                        <button class="back-button">Back to Home</button>
                    </a>
                    <form action="{{ url_for('mole1sim') }}" method="post" style="display: inline;">
                        <button class="resimulate-button" type="submit">Resimulate</button>
                    </form>
                </div>
            </header>
            <main>
                <p>{{ game_result_display | safe }}</p>
                <h1 style="font-size: 2em; text-shadow: 1px 1px 3px #000000;">Results Chart</h1>
                <div style="overflow-x: auto;">
                    <table>
                        <tr>
                            <th class="round-header">Round</th>
                            {% for round_num in range(1, num_rounds + 1) %}
                                <th class="round-header">{{ round_num }}</th>
                            {% endfor %}
                        </tr>
                        {% for player_name, results in player_results.items() %}
                            <tr>
                                <td class="name-column">{{ player_name }}</td>
                                {% for result in results %}
                                    {% if result == '' %}
                                        <td style="background-color: black;"></td>
                                    {% else %}
                                        <td class="result-cell" style="background-color:
                                            {% if result == 'WIN' %}#00ba37
                                            {% elif result == 'ELIM' %}red
                                            {% elif result == 'WINNER' %}blue
                                            {% elif result == 'IN' %}white
                                            {% elif result == 'MOLE' %}yellow
                                            {% endif %};">
                                            {{ result }}
                                        </td>
                                    {% endif %}
                                {% endfor %}
                            </tr>
                        {% endfor %}
                    </table>
                </div>
            </main>
            <footer>
                <a href="{{ url_for('index') }}" style="text-decoration: none;">
                    <button class="back-button">Back to Home</button>
                </a>
                <form action="{{ url_for('mole1sim') }}" method="post" style="display: inline;">
                    <button class="resimulate-button" type="submit">Resimulate</button>
                </form>
            </footer>
        </body>
        </html>
    ''', player_results=player_results, num_rounds=num_rounds, game_result_display=game_result_display)

if __name__ == '__main__':
    app.run(debug=True)
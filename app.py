import json
from flask import Flask, render_template_string, redirect, url_for, request, jsonify
from dataclasses import dataclass
import random
from TC40 import TC40cast
from TC40 import game
from TC40 import convert_players_to_dict
from traitors import traitors
from traitors1 import traitors1sim
from mole2sim import mole2
from mole1sim import mole1

app = Flask(__name__)
@app.route('/')
def index():
    return render_template_string('''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Reality TV Simulator</title>
            <link rel="icon" href="https://live.staticflickr.com/65535/53916787871_44fe3238e9_m.jpg" type="image/jpeg">
            <style>
                body {
                    background-color: #2c3e50;
                    background-size: cover;
                    background-position: center;
                    background-repeat: no-repeat;
                    height: 100vh;
                    margin: 0;
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    color: white;
                    text-shadow: 2px 2px 4px #000000;
                    font-family: 'Arial', sans-serif;
                }
                header {
                    width: 100%;
                    display: flex;
                    justify-content: space-between;
                    align-items: center;
                    padding: 1px 10px;
                    background-color: #1fd655;
                    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
                    position: fixed;
                    top: 0;
                    left: 0;
                    z-index: 1000;
                }
                header h4 {
                font-size: 1.5em;
                margin: 0;
                padding-left: 150px;
                text-align: center;
                font-family: 'Roboto', sans-serif; 
            }
                
                .content {
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100%;
                    width: 100%;
                    margin-top: 100px; /* Adjust for header height */
                }
                .container {
                    text-align: center;
                    background-color: rgba(0, 0, 0, 0.5);
                    padding: 20px;
                    border-radius: 10px;
                    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
                    margin: 10px;
                    height: 300px;
                    width: 300px;
                    display: flex;
                    flex-direction: column;
                    justify-content: center;
                }
                h2 {
                    margin-bottom: 20px;
                    font-size: 1.8em;
                }
                button {
                    padding: 15px 30px;
                    font-size: 20px;
                    border: none;
                    background-color: #007bff;
                    color: white;
                    cursor: pointer;
                    border-radius: 2px;
                    transition: background-color 0.3s, transform 0.3s, box-shadow 0.3s;
                    margin: 10px 0;
                    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
                    font-family: 'Arial', sans-serif;
                }
                button:hover {
                    background-color: #0056b3;
                    transform: translateY(-2px);
                    box-shadow: 0 6px 12px rgba(0, 0, 0, 0.3);
                }
                button:active {
                    transform: translateY(0);
                    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
                }
                header .header-buttons {
                    display: flex;
                    gap: 15px; /* Space between buttons */
                    padding-right: 30px; /* Additional padding to the right */
                }
                header .header-buttons button {
                    padding: 10px 15px;
                    font-size: 14px;
                    background-color: #343a40;
                    border: none;
                    border-radius: 5px;
                    cursor: pointer;
                    transition: background-color 0.3s, transform 0.3s;
                    color: white;
                    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
                }
                header .header-buttons button:hover {
                    background-color: #495057;
                    transform: scale(1.05);
                }
                .container button {
                    background-color: #28a745; /* Green */
                    border: none;
                }
                .container button:hover {
                    background-color: #218838; /* Darker green */
                }
            </style>
        </head>
        <body>
            <header style="display: flex; align-items: center; justify-content: space-between;">
                <a href="https://x.com/nathuin" target="_blank">
                    <img src="https://live.staticflickr.com/65535/53916787871_44fe3238e9_m.jpg" style="width: 50px; height: 50px;" alt="X logo">
                </a>
                <div style="flex-grow: 1; text-align: center;">
                    <h4> NATHSIM.COM </h4>
                </div>
                <div class="header-buttons">
                    <button type="submit">Suggestions</button>
                    <button type="submit">Report Bugs</button>
                </div>
            </header>
            <div class="content">
                <div class="container">
                    <div class="button-container">
                        <h2>Challenge Seasons</h2>
                        <form id="challengeForm" action="{{ url_for('TheChallenge40') }}" method="post">
                            <input type="hidden" name="game_output" id="game_output" value=[]>
                            <input type="hidden" name="eliminated" id="eliminated" value=[]>
                            <input type="hidden" name="game_results" id="game_results" value=[]>
                            <input type="hidden" name="week" id="week" value="1">
                            <input type="hidden" name="males" id="males" value=[]>
                            <input type="hidden" name="females" id="females" value=[]>
                            <button type="submit">The Challenge 40</button>
                        </form>
                    </div>
                </div>
                <div class="container">
                    <div class="button-container">
                        <h2>Traitors Seasons</h2>
                        <form action="{{ url_for('traitors1') }}" method="post">
                            <button type="submit">The Traitors 1</button>
                        </form>
                        <form action="{{ url_for('traitors2') }}" method="post">
                            <button type="submit">The Traitors 2</button>
                        </form>
                    </div>
                </div>
                <div class="container">
                    <div class="button-container">
                        <h2>The Mole Seasons</h2>
                        <form action="{{ url_for('mole1sim') }}" method="post">
                            <button type="submit">The Mole 1</button>
                        </form>
                        <form action="{{ url_for('mole2sim') }}" method="post">
                            <button type="submit">The Mole 2</button>
                        </form>
                        
                    </div>
                </div>
                
            </div>
                                  
        </body>
        <div style="display: flex; gap: 10px;"> 
    <a href="https://github.com/nathanrowell/nathsim" target="_blank">
        <img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" style="width: 30px; height: 30px;" alt="X logo">
    </a>

</div>
        </html>
    ''')


@app.route('/TheChallenge40', methods=['POST'])
def TheChallenge40():
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
    # Reconstruct the original format
    
    # Initialize males and females if week is 1
    if week == 1:
        males, females = TC40cast()
    else:
        males = [Player.from_dict(player_dict) for player_dict in males]
        females = [Player.from_dict(player_dict) for player_dict in females]
        eliminated = [Player.from_dict(player_dict) for player_dict in eliminated]
    results_output = []
    # Update game state
    game_output, eliminated_cur, game_results, males, females, results_output = game(game_output, eliminated, game_results, males, females, week)
    week += 1

    game_output_display = '\n'.join(game_output)
    # Generate player results

    males_json = json.dumps([p.to_dict() for p in males])
    females_json = json.dumps([p.to_dict() for p in females])
    eliminated_json = json.dumps([p.to_dict() for p in eliminated])
    results_json = json.dumps(results_output)

    

    return render_template_string('''
       <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>The Challenge 40 Simulator Results</title>
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

@media (max-width: 768px) {
    header {
        padding: 10px;
    }
    
    .header-title {
        font-size: 18px;
    }
}

@media (max-width: 480px) {
    header {
        padding: 5px 10px;
    }
    
    .header-title {
        font-size: 16px;
    }
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


                .continue-button {background-color: #93C4E0;
                    
                    color: black;
                    border: orange;
                    border-radius: 5px;
                    cursor: pointer;
                    transition: background-color 0.3s;
                                  padding: 5px 10px;
                }
                .continue-button:hover {
                    background-color: #7aa3b4; /* Slightly darker blue on hover */
                    transform: scale(1.05); /* Slightly increase size on hover */
                }

                .continue-button:active {
                    background-color: #5a8db7; /* Even darker blue when clicked */
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
                                  
                .resimulate-button {background-color: white;
                    
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
                .game-output-wrapper {
                    width: 80%; /* Limit the width to 80% of the page */
                    margin: 20px auto; /* Add margin around the container to create space outside */
                    background-color: #003366; /* Updated dark blue background */
                    border: 2px solid #002244; /* Darker blue border for contrast */
                    padding: 15px; /* Add padding inside the container */
                    box-sizing: border-box; /* Include padding and border in the element's total width */
                    border-radius: 12px; /* Curved corners */
                }

                .game-output-text {
                    color: white; /* Text color */
                    font-size: 16px; /* Adjust font size as needed */
                    margin: 0; /* Remove default margin */
                    line-height: 1.5; /* Improve readability */
                }
            </style>
        </head>
        <body>               
            <header>
                <div class="header-title">nathsim.com</div>
                <div class="center-title">The Challenge 40 Simulator</div>
                <div class="header-buttons">
                    <form id="challengeForm" action="{{ url_for('TheChallenge40Results') }}" method="post">
                        <input type="hidden" name="game_output" id="game_output" value="[]">
                        <input type="hidden" name="eliminated" id="eliminated" value="{{eliminated_json}}">
                        <input type="hidden" name="game_results" id="game_results" value="[]">
                        <input type="hidden" name="week" id="week" value="{{ week }}">
                        <input type="hidden" name="males" id="males" value="{{ males_json }}">
                        <input type="hidden" name="females" id="females" value="{{ females_json }}">
                        <input type="hidden" name="results" id="results" value="{{ results_json }}">
                        <button type="submit" class="continue-button" >Continue</button>
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
                
                <div class="game-output-wrapper">
                    <p class="game-output-text">{{ game_output_display | safe }}</p>
                </div>
                <div style="overflow-x: auto;">
                    
                    
                </div>
                <form id="challengeForm" action="{{ url_for('TheChallenge40Results') }}" method="post">
                    <input type="hidden" name="game_output" id="game_output" value="[]">
                    <input type="hidden" name="eliminated" id="eliminated" value="{{eliminated_json}}">
                    <input type="hidden" name="game_results" id="game_results" value="[]">
                    <input type="hidden" name="week" id="week" value="{{ week }}">
                    <input type="hidden" name="males" id="males" value="{{ males_json }}">
                    <input type="hidden" name="females" id="females" value="{{ females_json }}">
                    <input type="hidden" name="results" id="results" value="{{ results_json }}">
                    <button type="submit" class="continue-button" >Continue</button>
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
    ''', game_output_display=game_output_display,males_json=males_json, females_json=females_json, week = week,eliminated_json=eliminated_json, results_json = results_json)

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
    game_results = []
    results = parse_json_list('results')
    week = int(request.form.get('week', 1))
    males = parse_json_list('males')
    females = parse_json_list('females')
    def dict_to_player(data):
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
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>The Challenge 40 Simulator Results</title>
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
    text-align: center; /* Center the title */
}

.center-title {
    text-align: center;
    flex-grow: 1;
    font-size: 20px; /* Adjusted font size */
    margin: 0;
    padding-left: 20px; /* Reduced padding for smaller screens */
}

.header-buttons {
    display: flex;
    gap: 8px; /* Reduced gap */
}

@media (max-width: 768px) {
    header {
        padding: 8px 15px; /* Adjusted padding for tablets */
    }
    
    .header-title {
        font-size: 18px; /* Slightly smaller font size for tablets */
    }

    .center-title {
        font-size: 18px; /* Slightly smaller font size for tablets */
        padding-left: 15px; /* Reduced padding */
    }
}

@media (max-width: 480px) {
    header {
        padding: 5px 10px; /* Reduced padding for mobile devices */
    }
    
    .header-title {
        font-size: 16px; /* Smaller font size for mobile devices */
    }

    .center-title {
        font-size: 16px; /* Smaller font size for mobile devices */
        padding-left: 10px; /* Reduced padding */
    }
}
main {
    margin-top: 60px; /* Reduced top margin */
    text-align: center;
}

table {
    margin: 20px auto;
    border-collapse: collapse;
    text-align: center;
    font-size: 14px; /* Reduced font size for overall smaller table */
    max-width: 90%; /* Limits the width of the table to 90% of its container */
    overflow-x: auto; /* Adds horizontal scroll if needed */
}

th, td {
    border: 1px solid #dddddd;
    padding: 6px; /* Reduced padding for compactness */
}

th {
    background-color: #72aee6;
    color: white;
    font-size: 16px; /* Reduced font size for headers */
}

td.name-column {
    text-align: left;
    background-color: ghostwhite;
    width: 80px; /* Reduced width */
}

td {
    background-color: #f5f5f5; /* Very light gray */
}

.continue-button {
    border: 1px solid #4a7b8c;
    background-color: #93C4E0;
    color: black;
    border-radius: 5px;
    cursor: pointer;
    transition: background-color 0.3s;
    padding: 4px 8px; /* Reduced padding for smaller button */
    font-size: 14px; /* Smaller font size for button */
}

.continue-button:hover {
    background-color: #7aa3b4; /* Slightly darker blue on hover */
    transform: scale(1.05); /* Slightly increase size on hover */
}

.continue-button:active {
    background-color: #5a8db7; /* Even darker blue when clicked */
}

.result-cell {
    text-align: center;
    font-size: 14px; /* Reduced font size */
    text-shadow: 1px 1px 2px #000000; /* Reduced text shadow */
    line-height: 20px; /* Adjusted line-height for better text centering */
    overflow: hidden; /* Ensure text does not overflow */
}

.back-button {
    border: 1px solid #4a7b8c;
    background-color: darkgreen;
    color: white;
    border-radius: 5px;
    cursor: pointer;
    transition: background-color 0.3s;
    padding: 4px 8px; /* Reduced padding for smaller button */
    font-size: 14px; /* Smaller font size for button */
}

.resimulate-button {
    border: 1px solid #4a7b8c;
    background-color: white;
    color: black;
    border-radius: 5px;
    cursor: pointer;
    transition: background-color 0.3s;
    padding: 4px 8px; /* Reduced padding for smaller button */
    font-size: 14px; /* Smaller font size for button */
}

button:hover {
    opacity: 0.9;
}

footer {
    text-align: center;
    margin: 20px;
}
                                  .game-output-container {
                                    width: 90%; /* Set container width to 90% of the viewport */
                                    margin: 0 auto; /* Center the container */
                                    overflow-x: auto; /* Add horizontal scroll if content overflows */
                                    padding: 10px; /* Optional: Add padding */
                                }

                                .game-output-content {
    width: 80%; /* Limit the width to 80% of the page */
    margin: 20px auto; /* Add margin around the container to create space outside */
    background-color: #003366; /* Dark blue background */
    border: 2px solid #002244; /* Darker blue border for contrast */
    padding: 15px; /* Add padding inside the container */
    box-sizing: border-box; /* Include padding and border in the element's total width */
    border-radius: 12px; /* Curved corners */
    color: white; /* Text color */
    font-size: 16px; /* Adjust font size as needed */
    line-height: 1.5; /* Improve readability */
}
            </style>
            <script>
            // Function to check if results are empty and disable the button
            function toggleContinueButton() {
                var results = {{ results | tojson}};
                var continueButton = document.getElementById('continueButton');
                if (results.length === 0) {
                    continueButton.disabled = true;
                    continueButton.style.cursor = 'not-allowed'; // Optional: change cursor to indicate disabled state
                } else {
                    continueButton.disabled = false;
                    continueButton.style.cursor = 'pointer'; // Reset cursor style
                }
            }

            // Call the function when the page loads
            window.onload = toggleContinueButton;
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
                    <button type="submit" id="continueButton" class="continue-button">Continue</button>
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
                
                <div class="game-output-container">
                    <div class="game-output-content">
                        <p>{{ game_output_display | safe }}</p>
                    </div>
                </div>
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
                                        <td class="result-cell" style="background-color: 
                                            {% if result == 'WIN' %}#00ba37
                                            {% elif result == 'OUT' %}red
                                            {% elif result == 'ELIM' %}lightcoral
                                            {% elif result == 'BTM4' %}orange
                                            {% elif result == 'SAFE' %}white
                                            {% elif result == 'WINNER' %}forestgreen
                                            {% elif result == 'SECOND' %}ghostwhite
                                            {% elif result == 'THIRD' %}goldenrod
                                            {% elif result == 'FOURTH' %}darkseagreen
                                            {% endif %};">
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
                    <button type="submit" id="continueButton" class="continue-button">Continue</button>
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
    game_result, cast, game_results = traitors()

    # Flatten the game results for display
    game_result_flattened = []
    for item in game_result:
        if isinstance(item, list):
            game_result_flattened.extend(item)
        else:
            game_result_flattened.append(item)

    game_result_flattened = [str(item) for item in game_result_flattened]

    # Filter out specific lines
    filtered_game_result = [line for line in game_result_flattened if 'has voted to continue' not in line]
    game_result_display = '\n'.join(filtered_game_result)

    # Create a player results structure for columnar display
    num_rounds = len(game_results)

    # Sort the cast by their placement
    sorted_cast = sorted(cast, key=lambda player: player.placement)

    # Initialize player results for the sorted cast
    player_results = {player.name: [''] * num_rounds for player in sorted_cast}

    # Populate player results
    for round_num, round_results in enumerate(game_results):
        for player, result in round_results:
            if player.name in player_results:
                player_results[player.name][round_num] = result

    return render_template_string('''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>The Traitors 2 Simulator Results</title>
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
                    font-size: 20px;
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
                    background-color: #4CAF50;
                    color: white;
                    font-size: 20px;
                }
                td.name-column {
                    text-align: left;
                    background-color: lightblue;
                }
                td {
                    background-color: #f5f5f5;
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
                                  
                .resimulate-button {background-color: white;
                    
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
                <div class="center-title"> The Traitors Season 2 Simulator </div>
                <div class="header-buttons">
                    <a href="{{ url_for('index') }}" style="text-decoration: none;">
                        <button class="back-button">Back to Home</button>
                    </a>
                    <form action="{{ url_for('traitors2') }}" method="post" style="display: inline;">
                        <button class="resimulate-button" type="submit">Resimulate</button>
                    </form>
                </div>
            </header>
            <main>
                
                <p>{{ game_result_display | safe }}</p>
                <h1 style="font-size: 2em;">Voting Chart</h1>
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
                                <td class="name-column" style="background-color: {% if sorted_cast[loop.index0].isTraitor %} #f1948a {% endif %};">{{ player_name }}</td>
                                {% for result in results %}
                                    {% if result == '' %}
                                        <td style="background-color: black;"></td>
                                    {% else %}
                                        <td style="background-color: 
                                            {% if result == 'WIN' %}aquamarine
                                            {% elif result == 'OUT' %}red
                                            {% elif result == 'ELIM' %}lightcoral
                                            {% elif result == 'BTM4' %}orange
                                            {% elif result == 'SAFE' %}beige
                                            {% elif result == 'WINNER' %}forestgreen
                                            {% elif result == 'RUNNER-UP' %}yellow
                                            {% elif result == 'BANISH' %}tomato
                                            {% elif result == 'END' %}darkseagreen
                                            {% endif %};
                                            text-align: center; font-size: 18px;">{{ result }}</td>
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
                <form action="{{ url_for('traitors2') }}" method="post" style="display: inline;">
                    <button class="resimulate-button" type="submit">Resimulate</button>
                </form>
            </footer>
        </body>
        </html>
    ''', game_result_display=game_result_display, player_results=player_results, num_rounds=num_rounds, sorted_cast=sorted_cast)

@app.route('/traitors1', methods=['POST'])
def traitors1():
    game_result, cast, game_results = traitors1sim()

    # Flatten the game results for display
    game_result_flattened = []
    for item in game_result:
        if isinstance(item, list):
            game_result_flattened.extend(item)
        else:
            game_result_flattened.append(item)

    game_result_flattened = [str(item) for item in game_result_flattened]

    # Filter out specific lines
    filtered_game_result = [line for line in game_result_flattened if 'has voted to continue' not in line]
    game_result_display = '\n'.join(filtered_game_result)

    # Create a player results structure for columnar display
    num_rounds = len(game_results)

    # Sort the cast by their placement
    sorted_cast = sorted(cast, key=lambda player: player.placement)

    # Initialize player results for the sorted cast
    player_results = {player.name: [''] * num_rounds for player in sorted_cast}

    # Populate player results
    for round_num, round_results in enumerate(game_results):
        for player, result in round_results:
            if player.name in player_results:
                player_results[player.name][round_num] = result

    return render_template_string('''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>The Traitors 1 Simulator Results</title>
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
                    font-size: 20px;
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
                    background-color: #4CAF50;
                    color: white;
                    font-size: 20px;
                }
                td.name-column {
                    text-align: left;
                    background-color: lightblue;
                }
                td {
                    background-color: white;
                
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
                                  
                .resimulate-button {background-color: white;
                    
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
                <div class="center-title"> The Traitors Season 1 Simulator </div>
                <div class="header-buttons">
                    <a href="{{ url_for('index') }}" style="text-decoration: none;">
                        <button class="back-button">Back to Home</button>
                    </a>
                    <form action="{{ url_for('traitors1') }}" method="post" style="display: inline;">
                        <button class="resimulate-button" type="submit">Resimulate</button>
                    </form>
                </div>
            </header>
            <main>
                
                <p>{{ game_result_display | safe }}</p>
                <h1 style="font-size: 2em;">Voting Chart</h1>
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
                                <td class="name-column" style="background-color: {% if sorted_cast[loop.index0].isTraitor %} #f1948a {% endif %};">{{ player_name }}</td>
                                {% for result in results %}
                                    {% if result == '' %}
                                        <td style="background-color: black;"></td>
                                    {% else %}
                                        <td style="background-color: 
                                            {% if result == 'WIN' %}aquamarine
                                            {% elif result == 'OUT' %}red
                                            {% elif result == 'ELIM' %}lightcoral
                                            {% elif result == 'BTM4' %}orange
                                            {% elif result == 'SAFE' %}beige
                                            {% elif result == 'WINNER' %}forestgreen
                                            {% elif result == 'RUNNER-UP' %}yellow
                                            {% elif result == 'BANISH' %}tomato
                                            {% elif result == 'END' %}darkseagreen
                                            {% endif %};
                                            text-align: center; font-size: 18px;">{{ result }}</td>
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
                <form action="{{ url_for('traitors1') }}" method="post" style="display: inline;">
                    <button class="resimulate-button" type="submit">Resimulate</button>
                </form>
            </footer>
        </body>
        </html>
    ''', game_result_display=game_result_display, player_results=player_results, num_rounds=num_rounds, sorted_cast=sorted_cast)





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

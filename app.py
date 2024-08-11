from flask import Flask, render_template_string, redirect, url_for, request
from dataclasses import dataclass
import random
from TC40 import game
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
                    padding: 10px 20px;
                    background-color: #1fd655;
                    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
                    position: fixed;
                    top: 0;
                    left: 0;
                    z-index: 1000;
                }
                header img {
                    width: 100px;
                    height: auto;
                }
                header h4 {
                    font-size: 1.5em;
                    margin: 0;
                    flex-grow: 1;
                    text-align: center;
                }
                header .social-icons {
                    display: flex;
                    align-items: center;
                }
                header .social-icons img {
                    width: 20px;
                    height: 20px;
                    margin-left: 5px;
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
                    border-radius: 5px;
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
            <header>
                <img src="https://live.staticflickr.com/65535/53916787871_44fe3238e9_m.jpg" style="width: 50px; height: 50px;" alt="X logo">
                <h4>Created by @nathuin 
                    <img src="https://upload.wikimedia.org/wikipedia/commons/5/53/X_logo_2023_original.svg" style="width: 14px; height: 14px;" alt="X logo">
                    <img src="https://www.svgrepo.com/show/353655/discord-icon.svg" style="width: 16px; height: 16px;" alt="Discord Logo">
                </h4>
                <div class="header-buttons">
                    <button type="submit">Suggestions</button>
                    <button type="submit">Report Bugs</button>
                </div>
            </header>
            <div class="content">
                <div class="container">
                    <div class="button-container">
                        <h2>Challenge Seasons</h2>
                        <button type="submit">The Challenge 39 - Coming Soon</button>
                        <form action="{{ url_for('TheChallenge40') }}" method="post">
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
        </html>
    ''')


@app.route('/TheChallenge40', methods=['POST'])
def TheChallenge40():
    game_output, eliminated, game_results, males, females = game()
    
    game_output_display = '\n'.join(game_output)
    
    num_rounds = len(game_results)
    
    # Initialize player results
    player_results = {player.name: [''] * num_rounds for player in males + females}
    
    # Populate player results
    for round_num, round_results in enumerate(game_results):
        for player, result in round_results:
            if player.name in player_results:
                player_results[player.name][round_num] = result

    # Sort player results by placement
    sorted_player_results = sorted(
        [(player, player_results[player.name]) for player in males + females],
        key=lambda x: x[0].placement
    )
    
    player_results = {player.name: results for player, results in sorted_player_results}

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
                <div class="center-title">The Challenge 40 Simulator</div>
                <div class="header-buttons">
                    <a href="{{ url_for('index') }}" style="text-decoration: none;">
                        <button class="back-button">Back to Home</button>
                    </a>
                    <form action="{{ url_for('TheChallenge40') }}" method="post" style="display: inline;">
                        <button class="resimulate-button" type="submit">Resimulate</button>
                    </form>
                </div>
            </header>
            <main>
                <p>{{ game_output_display | safe }}</p>
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
    ''', player_results=player_results, num_rounds=num_rounds, game_output_display=game_output_display)

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

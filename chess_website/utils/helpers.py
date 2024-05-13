from datetime import datetime
from chessdotcom import *
import requests
import re

Client.request_config["headers"]["User-Agent"] = (
 'Web App to display chess.com statistics. Email is abhi.rachmanto@gmail.com and chess.com account is Abee101'
)

main_lines = ["Kings Pawn Opening", "Queens Pawn Opening", "Caro Kann Defense", "Vienna Game", "French Defense", "Italian Game", "Scandinavian Defense", "Center Game", "Petrovs Defense", "Pirc Defense", "Four Knights Game", "Giuoco Piano Game", "Barnes Opening", "Philidor Defense", "Sicilian Defense", "Ruy Lopez Opening", "Three Knights Opening", "Nimzowitsch Defense", "Scotch Game", "Bishops Opening", "Alekhines Defense", "Slav Defense", "Ponziani Opening", "Vant Kruijs Opening", "Modern Defense", "Queens Gambit Declined", "Closed Sicilian Defense", "Reti Opening", "Kings Fianchetto", "Kings Gambit", "Van Geet Opening", "Englund Gambit", "English Opening", "Englund Gambit Declined", "Alapin Sicilian", "Birds Opening", "Mieses Opening", "Dutch Defense", "Grob Opening", "Indian Game", "Kings Indian", "Kadas Opening", "Queens Gambit Accepted", "Saragossa Opening", "Ware Opening", "Colle System", "Dresden Opening", "London System", "English Defense", "Benko Gambit", "Benoni", "Bogo-Indian", "Catalan", "Danish Gambit", "Grunfeld Defense", "Budapest Gambit", "Kings Indian Defense", "Kings Indian Attack", "Nimzo Indian Defense", "Nimzowitsch Larsen Attack", "Old Indian Defense", "Owens Defense", "Polish Opening", "Queens Indian Defense", "Semi Slav Defense", "Tarrasch Defense", "Trompowsky Attack"]

headers = {'User-Agent': 'Web App to display chess.com statistics. Email is abhi.rachmanto@gmail.com and chess.com account is Abee101'}

# returns some information about a player's profile
def get_profile(name):
    info = {}

    # Get the profile from player
    try:
        data = get_player_profile(name).json
    except ChessDotComError as e:
        return None

    # Get country from profile
    try:
        tmp = get_country_details(data['player']['country'][34:]).json
        info['country'] = tmp['country']['name']
    except ChessDotComError as e:
        return None

    # Get year joined from profile
    info['year'] = datetime.fromtimestamp(data['player']['joined'])

    # Get the stats from player
    try:
        data = get_player_stats(name).json
    except ChessDotComError as e:
        return None
    

    controls = ['chess_blitz', 'chess_rapid', 'chess_bullet']
    ratings = {}

    # Get the Win loss draw for each time control
    for control in controls:
        record = data['stats'][control]['record']
        sum = record['win']+record['loss']+record['draw']

        # List -> [Current rating, percentage of wins for time control, then loss, then draw]
        ratings[control] = [data['stats'][control]['last']['rating'], [round(record['win']/sum*100, 2), round(record['loss']/sum*100, 2), round(record['draw']/sum*100, 2)]]

    controls_human = ['Blitz', 'Rapid', 'Bullet']
    for i in range(3):
        ratings[controls_human[i]] = ratings.pop(controls[i])

    info['ratings'] = ratings

    # Get the name
    info['name'] = name 
    
    return info

# Get the openings from the games
def get_openings(name):
    info = {}
    openings = {}
    
    try:
        # Get the months
        data = get_player_game_archives(name).json
        for month in data['archives']:
            monthly =  requests.get(month, headers=headers).json()
            # Get all games for every month
            for game in monthly['games']:
                if 'pgn'in game:    
                    opening = parse(game)  

                    # Loop through mainline and add to openings counter if the start matches,             
                    for i in main_lines:
                        if opening['mainLineOpening'].startswith(i):
                            if i not in openings:
                                openings[i] = 1
                                break
                            else:
                                openings[i] += 1
                                break
                    else:
                        # When it ends without a match, add to the 'Other' counter.
                        if 'Other' not in openings:
                            openings['Other'] = 1
                        else:
                            openings['Other'] += 1    
                
        # Get top 5 openings
        # https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
        info["top_5"] = sorted(openings.items(), key=lambda x:x[1], reverse=True)[0:5]

    except ChessDotComError as e:
        return None
    

    return info

def parse(game):
    main_line = {}

    # pgn parsing
    pgn = game["pgn"].split('\n')

    # Find opening url
    openingUrl = ""
    for line in pgn:
        if line.startswith("[ECOUrl"):
            openingUrl = line
            break

    # Get rid of the special characters
    tmp_opening = re.sub(r'\\|\[|\]|\"|ECOUrl|https:\/\/www.chess.com\/openings\/', '', openingUrl)
    # Replace - with spaces
    parsed_opening = tmp_opening.replace("-", " ").strip()

    # mainLineOpening
    main_line_match = re.match(r'^(\D*)(?=\d)', parsed_opening)
    if main_line_match:
        main_line["mainLineOpening"] = main_line_match.group(1)
    else:
        main_line["mainLineOpening"] = parsed_opening

    return main_line
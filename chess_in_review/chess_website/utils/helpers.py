from datetime import datetime
from chessdotcom import *
import requests
import re

pattern = re.compile(r"ECO (.*?)\]")

Client.request_config["headers"]["User-Agent"] = (
 'Web App to display chess.com statistics. Email is abhi.rachmanto@gmail.com and chess.com account is Abee101'
)


headers = {'User-Agent': 'Web App to display chess.com statistics. Email is abhi.rachmanto@gmail.com and chess.com account is Abee101'}

ecoConversion = {'A00': 'Irregular Openings (A00)', 'A01': 'Nimzobich-Larsen Attack', 'A02': 'Bird Opening', 'A03': 'Bird Opening', 'A04': 'Reti Opening', 'A05': 'Reti Opening', 'A06': 'Reti Opening', 'A07': 'Reti Opening', 'A08': 'Reti Opening', 'A09': 'Reti Opening', 'A10': 'English Opening', 'A11': 'English Opening', 'A12': 'English Opening', 'A13': 'English Opening', 'A14': 'English Opening', 'A15': 'English Opening', 'A16': 'English Opening', 'A17': 'English Opening', 'A18': 'English Opening', 'A19': 'English Opening', 'A20': 'English Opening', 'A21': 'English Opening', 'A22': 'English Opening', 'A23': 'English Opening', 'A24': 'English Opening', 'A25': 'English Opening', 'A26': 'English Opening', 'A27': 'English Opening', 'A28': 'English Opening', 'A29': 'English Opening', 'A30': 'English Opening', 'A31': 'English Opening', 'A32': 'English Opening', 'A33': 'English Opening', 'A34': 'English Opening', 'A35': 'English Opening', 'A36': 'English Opening', 'A37': 'English Opening', 'A38': 'English Opening', 'A39': 'English Opening', 'A40': "Queen's Pawn (A40)", 'A41': "Queen's Pawn (A41)", 'A42': 'Modern Defence', 'A43': 'Old Benoni Defence', 'A44': 'Old Benoni Defence', 'A45': "Trompowsky Attack", 'A46': "Torre Attack", 'A47': "Queen's Indian Defence", 'A48': "King's Indian", 'A49': "King's Indian", 'A50': "Black Knights' Tango", 'A51': 'Budapest Gambit', 'A52': 'Budapest Gambit', 'A53': 'Old Indian Defence', 'A54': 'Old Indian Defence', 'A55': 'Old Indian Defence', 'A56': 'Benoni Defence', 'A57': 'Benko Gambit', 'A58': 'Benko Gambit', 'A59': 'Benko Gambit', 'A60': 'Benoni Defence', 'A61': 'Benoni Defence', 'A62': 'Benoni Defence', 'A63': 'Benoni Defence', 'A64': 'Benoni Defence', 'A65': 'Benoni Defence', 'A66': 'Benoni Defence', 'A67': 'Benoni Defence', 'A68': 'Benoni Defence', 'A69': 'Benoni Defence', 'A70': 'Benoni Defence', 'A71': 'Benoni Defence', 'A72': 'Benoni Defence', 'A73': 'Benoni Defence', 'A74': 'Benoni Defence', 'A75': 'Benoni Defence', 'A76': 'Benoni Defence', 'A77': 'Benoni Defence', 'A78': 'Benoni Defence', 'A79': 'Benoni Defence', 'A80': 'Dutch Defence', 'A81': 'Dutch Defence', 'A82': 'Dutch Defence', 'A83': 'Dutch Defence', 'A84': 'Dutch Defence', 'A85': 'Dutch Defence', 'A86': 'Dutch Defence', 'A87': 'Dutch Defence', 'A88': 'Dutch Defence', 'A89': 'Dutch Defence', 'A90': 'Dutch Defence', 'A91': 'Dutch Defence', 'A92': 'Dutch Defence', 'A93': 'Dutch Defence', 'A94': 'Dutch Defence', 'A95': 'Dutch Defence', 'A96': 'Dutch Defence', 'A97': 'Dutch Defence', 'A98': 'Dutch Defence', 'A99': 'Dutch Defence', 'B00': "King's Pawn Opening", 'B01': 'Scandinavian Defence', 'B02': "Alekhine's Defence", 'B03': "Alekhine's Defence", 'B04': "Alekhine's Defence", 'B05': "Alekhine's Defence", 'B06': 'Robatsch (modern) Defence', 'B07': 'Pirc Defence', 'B08': 'Pirc Defence', 'B09': 'Pirc Defence', 'B10': 'Caro-Kann Defence', 'B11': 'Caro-Kann Defence', 'B12': 'Caro-Kann Defence', 'B13': 'Caro-Kann Defence', 'B14': 'Caro-Kann Defence', 'B15': 'Caro-Kann Defence', 'B16': 'Caro-Kann Defence', 'B17': 'Caro-Kann Defence', 'B18': 'Caro-Kann Defence', 'B19': 'Caro-Kann Defence', 'B20': 'Sicillian Defence', 'B21': 'Sicillian Defence', 'B22': 'Sicillian Defence', 'B23': 'Sicillian Defence', 'B24': 'Sicillian Defence', 'B25': 'Sicillian Defence', 'B26': 'Sicillian Defence', 'B27': 'Sicillian Defence', 'B28': 'Sicillian Defence', 'B29': 'Sicillian Defence', 'B30': 'Sicillian Defence', 'B31': 'Sicillian Defence', 'B32': 'Sicillian Defence', 'B33': 'Sicillian Defence', 'B34': 'Sicillian Defence', 'B35': 'Sicillian Defence', 'B36': 'Sicillian Defence', 'B37': 'Sicillian Defence', 'B38': 'Sicillian Defence', 'B39': 'Sicillian Defence', 'B40': 'Sicillian Defence', 'B41': 'Sicillian Defence', 'B42': 'Sicillian Defence', 'B43': 'Sicillian Defence', 'B44': 'Sicillian Defence', 'B45': 'Sicillian Defence', 'B46': 'Sicillian Defence', 'B47': 'Sicillian Defence', 'B48': 'Sicillian Defence', 'B49': 'Sicillian Defence', 'B50': 'Sicillian Defence', 'B51': 'Sicillian Defence', 'B52': 'Sicillian Defence', 'B53': 'Sicillian Defence', 'B54': 'Sicillian Defence', 'B55': 'Sicillian Defence', 'B56': 'Sicillian Defence', 'B57': 'Sicillian Defence', 'B58': 'Sicillian Defence', 'B59': 'Sicillian Defence', 'B60': 'Sicillian Defence', 'B61': 'Sicillian Defence', 'B62': 'Sicillian Defence', 'B63': 'Sicillian Defence', 'B64': 'Sicillian Defence', 'B65': 'Sicillian Defence', 'B66': 'Sicillian Defence', 'B67': 'Sicillian Defence', 'B68': 'Sicillian Defence', 'B69': 'Sicillian Defence', 'B70': 'Sicillian Defence', 'B71': 'Sicillian Defence', 'B72': 'Sicillian Defence', 'B73': 'Sicillian Defence', 'B74': 'Sicillian Defence', 'B75': 'Sicillian Defence', 'B76': 'Sicillian Defence', 'B77': 'Sicillian Defence', 'B78': 'Sicillian Defence', 'B79': 'Sicillian Defence', 'B80': 'Sicillian Defence', 'B81': 'Sicillian Defence', 'B82': 'Sicillian Defence', 'B83': 'Sicillian Defence', 'B84': 'Sicillian Defence', 'B85': 'Sicillian Defence', 'B86': 'Sicillian Defence', 'B87': 'Sicillian Defence', 'B88': 'Sicillian Defence', 'B89': 'Sicillian Defence', 'B90': 'Sicillian Defence', 'B91': 'Sicillian Defence', 'B92': 'Sicillian Defence', 'B93': 'Sicillian Defence', 'B94': 'Sicillian Defence', 'B95': 'Sicillian Defence', 'B96': 'Sicillian Defence', 'B97': 'Sicillian Defence', 'B98': 'Sicillian Defence', 'B99': 'Sicillian Defence', 'C00': 'French Defence', 'C01': 'French Defence', 'C02': 'French Defence', 'C03': 'French Defence', 'C04': 'French Defence', 'C05': 'French Defence', 'C06': 'French Defence', 'C07': 'French Defence', 'C08': 'French Defence', 'C09': 'French Defence', 'C10': 'French Defence', 'C11': 'French Defence', 'C12': 'French Defence', 'C13': 'French Defence', 'C14': 'French Defence', 'C15': 'French Defence', 'C16': 'French Defence', 'C17': 'French Defence', 'C18': 'French Defence', 'C19': 'French Defence', 'C20': "King's Pawn Game", 'C21': 'Centre Game', 'C22': 'Centre Game', 'C23': "Bishop's Opening", 'C24': "Bishop's Opening", 'C25': 'Vienna Game', 'C26': 'Vienna Game', 'C27': 'Vienna Game', 'C28': 'Vienna Game', 'C29': 'Vienna Game', 'C30': "King's Gambit", 'C31': "King's Gambit", 'C32': "King's Gambit", 'C33': "King's Gambit", 'C34': "King's Gambit", 'C35': "King's Gambit", 'C36': "King's Gambit", 'C37': "King's Gambit", 'C38': "King's Gambit", 'C39': "King's Gambit", 'C40': "King's Knight Opening", 'C41': "Philidor's Defence", 'C42': "Petrov's Defence", 'C43': "Petrov's Defence", 'C44': "King's Pawn Game", 'C45': 'Scotch Game', 'C46': 'Three Knights Game', 'C47': 'Four Knights Game', 'C48': 'Four Knights Game', 'C49': 'Four Knights Game', 'C50': 'Italian Game', 'C51': 'Evans Gambit', 'C52': 'Evans Gambit', 'C53': 'Giuoco Piano', 'C54': 'Giuoco Piano', 'C55': 'Two Knights Defence', 'C56': 'Two Knights Defence', 'C57': 'Two Knights Defence', 'C58': 'Two Knights Defence', 'C59': 'Two Knights Defence', 'C60': 'Ruy Lopez', 'C61': 'Ruy Lopez', 'C62': 'Ruy Lopez', 'C63': 'Ruy Lopez', 'C64': 'Ruy Lopez', 'C65': 'Ruy Lopez', 'C66': 'Ruy Lopez', 'C67': 'Ruy Lopez', 'C68': 'Ruy Lopez', 'C69': 'Ruy Lopez', 'C70': 'Ruy Lopez', 'C71': 'Ruy Lopez', 'C72': 'Ruy Lopez', 'C73': 'Ruy Lopez', 'C74': 'Ruy Lopez', 'C75': 'Ruy Lopez', 'C76': 'Ruy Lopez', 'C77': 'Ruy Lopez', 'C78': 'Ruy Lopez', 'C79': 'Ruy Lopez', 'C80': 'Ruy Lopez', 'C81': 'Ruy Lopez', 'C82': 'Ruy Lopez', 'C83': 'Ruy Lopez', 'C84': 'Ruy Lopez', 'C85': 'Ruy Lopez', 'C86': 'Ruy Lopez', 'C87': 'Ruy Lopez', 'C88': 'Ruy Lopez', 'C89': 'Ruy Lopez', 'C90': 'Ruy Lopez', 'C91': 'Ruy Lopez', 'C92': 'Ruy Lopez', 'C93': 'Ruy Lopez', 'C94': 'Ruy Lopez', 'C95': 'Ruy Lopez', 'C96': 'Ruy Lopez', 'C97': 'Ruy Lopez', 'C98': 'Ruy Lopez', 'C99': 'Ruy Lopez', 'D00': "Queen's Pawn Game (D00)", 'D01': 'Richter-Veresov Attack', 'D02': "The London System", 'D03': 'Torre Attack (Tartakower variation)', 'D04': "Queen's Pawn Game, Colle System", 'D05': "Queen's Pawn Game, Colle System", 'D06': "Queen's Gambit", 'D07': "Queen's Gambit Declined", 'D08': "Queen's Gambit Declined", 'D09': "Queen's Gambit Declined", 'D10': "Queen's Gambit Declined", 'D11': "Queen's Gambit Declined", 'D12': "Queen's Gambit Declined", 'D13': "Queen's Gambit Declined", 'D14': "Queen's Gambit Declined", 'D15': "Queen's Gambit Declined", 'D16': "Queen's Gambit Declined", 'D17': "Queen's Gambit Declined", 'D18': "Queen's Gambit Declined", 'D19': "Queen's Gambit Declined", 'D20': "Queen's Gambit Accepted", 'D21': "Queen's Gambit Accepted", 'D22': "Queen's Gambit Accepted", 'D23': "Queen's Gambit Accepted", 'D24': "Queen's Gambit Accepted", 'D25': "Queen's Gambit Accepted", 'D26': "Queen's Gambit Accepted", 'D27': "Queen's Gambit Accepted", 'D28': "Queen's Gambit Accepted", 'D29': "Queen's Gambit Accepted", 'D30': "Queen's Gambit Declined", 'D31': "Queen's Gambit Declined", 'D32': "Queen's Gambit Declined", 'D33': "Queen's Gambit Declined", 'D34': "Queen's Gambit Declined", 'D35': "Queen's Gambit Declined", 'D36': "Queen's Gambit Declined", 'D37': "Queen's Gambit Declined", 'D38': "Queen's Gambit Declined", 'D39': "Queen's Gambit Declined", 'D40': "Queen's Gambit Declined", 'D41': "Queen's Gambit Declined", 'D42': "Queen's Gambit Declined", 'D43': "Queen's Gambit Declined", 'D44': "Queen's Gambit Declined", 'D45': "Queen's Gambit Declined", 'D46': "Queen's Gambit Declined", 'D47': "Queen's Gambit Declined", 'D48': "Queen's Gambit Declined", 'D49': "Queen's Gambit Declined", 'D50': "Queen's Gambit Declined, 4.Bg5", 'D51': "Queen's Gambit Declined, 4.Bg5", 'D52': "Queen's Gambit Declined, 4.Bg5", 'D53': "Queen's Gambit Declined, 4.Bg5", 'D54': "Queen's Gambit Declined, 4.Bg5", 'D55': "Queen's Gambit Declined, 4.Bg5", 'D56': "Queen's Gambit Declined, 4.Bg5", 'D57': "Queen's Gambit Declined, 4.Bg5", 'D58': "Queen's Gambit Declined, 4.Bg5", 'D59': "Queen's Gambit Declined, 4.Bg5", 'D60': "Queen's Gambit Declined, 4.Bg5", 'D61': "Queen's Gambit Declined, 4.Bg5", 'D62': "Queen's Gambit Declined, 4.Bg5", 'D63': "Queen's Gambit Declined, 4.Bg5", 'D64': "Queen's Gambit Declined, 4.Bg5", 'D65': "Queen's Gambit Declined, 4.Bg5", 'D66': "Queen's Gambit Declined, 4.Bg5", 'D67': "Queen's Gambit Declined, 4.Bg5", 'D68': "Queen's Gambit Declined, 4.Bg5", 'D69': "Queen's Gambit Declined, 4.Bg5", 'D70': 'Neo-Gruenfeld defence', 'D71': 'Neo-Gruenfeld defence', 'D72': 'Neo-Gruenfeld defence', 'D73': 'Neo-Gruenfeld defence', 'D74': 'Neo-Gruenfeld defence', 'D75': 'Neo-Gruenfeld defence', 'D76': 'Neo-Gruenfeld defence', 'D77': 'Neo-Gruenfeld defence', 'D78': 'Neo-Gruenfeld defence', 'D79': 'Neo-Gruenfeld defence', 'D80': 'Gruenfeld defence', 'D81': 'Gruenfeld defence', 'D82': 'Gruenfeld defence', 'D83': 'Gruenfeld defence', 'D84': 'Gruenfeld defence', 'D85': 'Gruenfeld defence', 'D86': 'Gruenfeld defence', 'D87': 'Gruenfeld defence', 'D88': 'Gruenfeld defence', 'D89': 'Gruenfeld defence', 'D90': 'Gruenfeld defence', 'D91': 'Gruenfeld defence', 'D92': 'Gruenfeld defence', 'D93': 'Gruenfeld defence', 'D94': 'Gruenfeld defence', 'D95': 'Gruenfeld defence', 'D96': 'Gruenfeld defence', 'D97': 'Gruenfeld defence', 'D98': 'Gruenfeld defence', 'D99': 'Gruenfeld defence', 'E00': "Queen's Pawn Game (E00)", 'E01': 'Catalan, closed', 'E02': 'Catalan, closed', 'E03': 'Catalan, closed', 'E04': 'Catalan, closed', 'E05': 'Catalan, closed', 'E06': 'Catalan, closed', 'E07': 'Catalan, closed', 'E08': 'Catalan, closed', 'E09': 'Catalan, closed', 'E10': "Queen's Pawn Game 3.Nf3", 'E11': 'Bogo-Indian Defence', 'E12': "Queen's Indian Defence", 'E13': "Queen's Indian Defence", 'E14': "Queen's Indian Defence", 'E15': "Queen's Indian Defence", 'E16': "Queen's Indian Defence", 'E17': "Queen's Indian Defence", 'E18': "Queen's Indian Defence", 'E19': "Queen's Indian Defence", 'E20': 'Nimzo-Indian Defence', 'E21': 'Nimzo-Indian Defence', 'E22': 'Nimzo-Indian Defence', 'E23': 'Nimzo-Indian Defence', 'E24': 'Nimzo-Indian Defence', 'E25': 'Nimzo-Indian Defence', 'E26': 'Nimzo-Indian Defence', 'E27': 'Nimzo-Indian Defence', 'E28': 'Nimzo-Indian Defence', 'E29': 'Nimzo-Indian Defence', 'E30': 'Nimzo-Indian Defence', 'E31': 'Nimzo-Indian Defence', 'E32': 'Nimzo-Indian Defence', 'E33': 'Nimzo-Indian Defence', 'E34': 'Nimzo-Indian Defence', 'E35': 'Nimzo-Indian Defence', 'E36': 'Nimzo-Indian Defence', 'E37': 'Nimzo-Indian Defence', 'E38': 'Nimzo-Indian Defence', 'E39': 'Nimzo-Indian Defence', 'E40': 'Nimzo-Indian Defence', 'E41': 'Nimzo-Indian Defence', 'E42': 'Nimzo-Indian Defence', 'E43': 'Nimzo-Indian Defence', 'E44': 'Nimzo-Indian Defence', 'E45': 'Nimzo-Indian Defence', 'E46': 'Nimzo-Indian Defence', 'E47': 'Nimzo-Indian Defence', 'E48': 'Nimzo-Indian Defence', 'E49': 'Nimzo-Indian Defence', 'E50': 'Nimzo-Indian Defence', 'E51': 'Nimzo-Indian Defence', 'E52': 'Nimzo-Indian Defence', 'E53': 'Nimzo-Indian Defence', 'E54': 'Nimzo-Indian Defence', 'E55': 'Nimzo-Indian Defence', 'E56': 'Nimzo-Indian Defence', 'E57': 'Nimzo-Indian Defence', 'E58': 'Nimzo-Indian Defence', 'E59': 'Nimzo-Indian Defence', 'E60': "King's Indian Defence", 'E61': "King's Indian Defence", 'E62': "King's Indian Defence", 'E63': "King's Indian Defence", 'E64': "King's Indian Defence", 'E65': "King's Indian Defence", 'E66': "King's Indian Defence", 'E67': "King's Indian Defence", 'E68': "King's Indian Defence", 'E69': "King's Indian Defence", 'E70': "King's Indian Defence", 'E71': "King's Indian Defence", 'E72': "King's Indian Defence", 'E73': "King's Indian Defence", 'E74': "King's Indian Defence", 'E75': "King's Indian Defence", 'E76': "King's Indian Defence", 'E77': "King's Indian Defence", 'E78': "King's Indian Defence", 'E79': "King's Indian Defence", 'E80': "King's Indian Defence", 'E81': "King's Indian Defence", 'E82': "King's Indian Defence", 'E83': "King's Indian Defence", 'E84': "King's Indian Defence", 'E85': "King's Indian Defence", 'E86': "King's Indian Defence", 'E87': "King's Indian Defence", 'E88': "King's Indian Defence", 'E89': "King's Indian Defence", 'E90': "King's Indian Defence", 'E91': "King's Indian Defence", 'E92': "King's Indian Defence", 'E93': "King's Indian Defence", 'E94': "King's Indian Defence", 'E95': "King's Indian Defence", 'E96': "King's Indian Defence", 'E97': "King's Indian Defence", 'E98': "King's Indian Defence", 'E99': "King's Indian Defence"}

# returns some information about a player's profile
def getProfile(name):
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
        ratings[control] = [data['stats'][control]['last']['rating'], [round(record['win']/sum*100, 2), round(record['loss']/sum*100, 2), round(record['draw']/sum*100, 2)]]

    controls_human = ['Blitz', 'Rapid', 'Bullet']
    for i in range(3):
        ratings[controls_human[i]] = ratings.pop(controls[i])

    info['ratings'] = ratings
    
    return info

# Get the openings from the games
def getOpenings(name):
    info = {}
    
    try:
        data = get_player_game_archives(name).json
        opening = {}
        for month in data['archives']:
            monthly =  requests.get(month, headers=headers).json()
            
            for game in monthly['games']:
                if 'pgn'in game:                      
                    match = re.search(pattern, game['pgn'])
                    if match:
                        ecoCode = match.group(1)[1:4]
                        if ecoConversion[ecoCode] not in opening:
                            opening[ecoConversion[ecoCode]] = 1
                        else:
                            opening[ecoConversion[ecoCode]] += 1
                
        info["top_5"] = sorted(opening.items(), key=lambda x:x[1], reverse=True)[0:5]

    except ChessDotComError as e:
        return None
    return info

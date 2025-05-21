import easygui

favourite_games = {
    1 : {
        "Title" : "Fortnite",
        "Genre" : "Survival, battle royale, sandbox",
        "Platform(s)" : "PC, Xbox, PS, Nintendo Switch",
        "Release Year" : 2017,
        "Rating out of 10" : 9.6
    },
    2 : {
        "Title" : "GTA V",
        "Genre" : "Action Adventure",
        "Platform(s)" : "PC, Xbox, PS",
        "Release Year" : 2013,
        "Rating out of 10" : 9.5
    },
    3 : {
        "Title" : "Minecraft",
        "Genre" : "Survival, sandbox, adventure",
        "Platform(s)" : "PC, Xbox, PS, Nintendo Switch, Mobile",
        "Release Year" : 2009,
        "Rating out of 10" : 9.4
    },
    4 : {
        "Title" : "Rainbow Six Seige",
        "Genre" : "Shooter, Search and Destroy",
        "Platform(s)" : "PC, Xbox PS",
        "Release Year" : 2015,
        "Rating out of 10" : 9.3
    },
    5 : {
        "Title" : "Rocket League",
        "Genre" : "Sports",
        "Platform(s)" : "PC, Xbox, PC, Nintendo Switch",
        "Release Year" : 2015,
        "Rating out of 10" : 8.8 
    },
    6 : {
        "Title" : "Skylanders",
        "Genre" : "Adventure, puzzle",
        "Platform(s)" : "Xbox, PS, Nintendo Switch, Wii",
        "Release Year" : 2011,
        "Rating out of 10" : 8.6   
    },
    7 : {
        "Title" : "Fifa",
        "Genre" : "Sports",
        "Platform(s)" : "PC, Xbox, PS",
        "Release Year" : 1993,
        "Rating out of 10" : 8.5 
    },
    8 : {
        "Title" : "NBA 2K",
        "Genre" : "Sports",
        "Platform(s)" : "PC, Xbox, PS, Nintendo Switch",
        "Release Year" : 1999,
        "Rating out of 10" : 8.2
    },
    9 : {
        "Title" : "Roblox",
        "Genre" : "Simulation, multiplayer, action",
        "Platform(s)" : "PC, Xbox, PS, Nintendo Switch, Mobile",
        "Release Year" : 2006,
        "Rating out of 10" : 8.0
    },
    10 : {
        "Title" : "Clash Royale",
        "Genre" : "Tower defence, multiplayer, strategy",
        "Platform(s)" : "Mobile",
        "Release Year" : 2016,
        "Rating out of 10" : 7.8
    }
}

def print_favourite_games():
    for rank, game_info in favourite_games.items():
        msg = f"Rank: {rank}\n"
        msg += f"Title: {game_info['Title']}\n"
        msg += f"Genre: {game_info['Genre']}\n"
        msg += f"Platform: {game_info['Platform(s)']}\n"
        msg += f"Release Year: {game_info['Release Year']}\n"
        msg += f"Rating: {game_info['Rating out of 10']}/10"
        
        easygui.msgbox(msg, title=f"Favourite Game #{rank}")

def show_menu():
    """
    """
    options = {
        #"Add Game" : add_game,
        "Edit Game" : edit_game,
        "Quit Menu" : quit_menu
    }

    choice_list = []

    for key in options:
        choice_list.append(key)

    user_choice = easygui.buttonbox("What would you like to do sole?", \
    choices = choice_list)

    function = options[user_choice]()
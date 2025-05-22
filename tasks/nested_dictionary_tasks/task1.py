import easygui

favourite_games = {
    "Fortnite" : {
        "Title" : "Fortnite",
        "Genre" : "Survival, battle royale, sandbox",
        "Platform(s)" : "PC, Xbox, PS, Nintendo Switch",
        "Release Year" : 2017,
        "Rating out of 10" : 9.6
    },
    "GTA V" : {
        "Title" : "GTA V",
        "Genre" : "Action Adventure",
        "Platform(s)" : "PC, Xbox, PS",
        "Release Year" : 2013,
        "Rating out of 10" : 9.5
    },
    "Minecraft" : {
        "Title" : "Minecraft",
        "Genre" : "Survival, sandbox, adventure",
        "Platform(s)" : "PC, Xbox, PS, Nintendo Switch, Mobile",
        "Release Year" : 2009,
        "Rating out of 10" : 9.4
    },
    "Rainbow Six Seige" : {
        "Title" : "Rainbow Six Seige",
        "Genre" : "Shooter, Search and Destroy",
        "Platform(s)" : "PC, Xbox PS",
        "Release Year" : 2015,
        "Rating out of 10" : 9.3
    },
    "Rocket League" : {
        "Title" : "Rocket League",
        "Genre" : "Sports",
        "Platform(s)" : "PC, Xbox, PC, Nintendo Switch",
        "Release Year" : 2015,
        "Rating out of 10" : 8.8 
    },
    "Skylanders" : {
        "Title" : "Skylanders",
        "Genre" : "Adventure, puzzle",
        "Platform(s)" : "Xbox, PS, Nintendo Switch, Wii",
        "Release Year" : 2011,
        "Rating out of 10" : 8.6   
    },
    "Fifa" : {
        "Title" : "Fifa",
        "Genre" : "Sports",
        "Platform(s)" : "PC, Xbox, PS",
        "Release Year" : 1993,
        "Rating out of 10" : 8.5 
    },
    "NBA 2K" : {
        "Title" : "NBA 2K",
        "Genre" : "Sports",
        "Platform(s)" : "PC, Xbox, PS, Nintendo Switch",
        "Release Year" : 1999,
        "Rating out of 10" : 8.2
    },
    "Roblox" : {
        "Title" : "Roblox",
        "Genre" : "Simulation, multiplayer, action",
        "Platform(s)" : "PC, Xbox, PS, Nintendo Switch, Mobile",
        "Release Year" : 2006,
        "Rating out of 10" : 8.0
    },
    "Clash Royale" : {
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
        #"Quit Menu" : quit_menu
    }

    choice_list = []

    for key in options:
        choice_list.append(key)

    user_choice = easygui.buttonbox("What would you like to do sole?", \
    choices = choice_list)

    function = options[user_choice]()

def edit_game():
    """
    """
    game_titles = []

    for key, value in favourite_games.items():
        game_titles.append(value["Title"])

    user_choice = easygui.choicebox("What game would you like to edit?", \
    choices = game_titles)

    user_options = []

    for key in favourite_games.items():
        user_options.append(key)

    user_info = easygui.buttonbox("What would you like to edit?", \
    choices = user_options)

    





show_menu()
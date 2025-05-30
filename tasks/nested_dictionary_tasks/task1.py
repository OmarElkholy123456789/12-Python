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

def show_menu():
    """
    """
    options = {
        "Print Games" : print_favourite_games,
        "Add Game" : add_game,
        "Edit Game" : edit_game,
        "Search Game" : search_game,
        "Delete Game" : delete_game,
        "Quit Menu" : quit
    }

    choice_list = []

    for key in options:
        choice_list.append(key)

    user_choice = easygui.buttonbox("What would you like to do sole?", \
    choices = choice_list)

    function = options[user_choice]()

def print_favourite_games():
    for game, game_info in favourite_games.items():
        msg = f"Title: {game_info['Title']}\n"
        msg += f"Genre: {game_info['Genre']}\n"
        msg += f"Platform: {game_info['Platform(s)']}\n"
        msg += f"Release Year: {game_info['Release Year']}\n"
        msg += f"Rating: {game_info['Rating out of 10']}/10"
        
        easygui.msgbox(msg, title=f"Favourite Game #{game}")

def edit_game():
    """
    """
    game_titles = []

    for key, titles in favourite_games.items():
        game_titles.append(titles["Title"])

    msg = "What game would you like to edit the details of"
    title="GAME CHOICE"

    game_choice = easygui.buttonbox(msg, title, game_titles)

    game_info = []

    for game_information in favourite_games[game_choice]:
        game_info.append(game_information)

    msg = f"What detail of {game_choice} would you like to edit?"
    title = "EDIT CHOICE"

    edit_choice = easygui.buttonbox(msg, title, game_info)

    msg = f"Enter the new {edit_choice} for {game_choice}"
    title = "EDIT CHOICE"

    favourite_games[game_choice][edit_choice] = easygui.enterbox(msg, title)

    show_menu()

def add_game():
    game_name = easygui.enterbox(f"Please enter the name of the game")
    game_genre = easygui.enterbox(f"Please enter the genre for {game_name}")
    game_platform = easygui.enterbox(f"Please enter the platform(s) for {game_name}")
    game_release_year = easygui.enterbox(f"Please enter the release year of {game_name}")
    game_rating = easygui.enterbox(f"Please enter the rating for {game_name}")

    favourite_games[game_name] = {
        "Title" : game_name,
        "Genre" : game_genre,
        "Platform(s)" : game_platform,
        "Release Year" : game_release_year,
        "Rating out of 10" : game_rating
    }

    show_menu()

def search_game():
    game_titles = []

    for key, titles in favourite_games.items():
        game_titles.append(titles["Title"])

    searched_game = easygui.buttonbox("What game would you like to search \
    for?", choices = game_titles)

    for game, game_info in favourite_games(searched_game):
        msg = f"Title: {game_info['Title']}\n"
        msg += f"Genre: {game_info['Genre']}\n"
        msg += f"Platform: {game_info['Platform(s)']}\n"
        msg += f"Release Year: {game_info['Release Year']}\n"
        msg += f"Rating: {game_info['Rating out of 10']}/10"
        
        easygui.msgbox(msg, title=f"Favourite Game #{game}")

def delete_game():

    game_titles = []

    for key, titles in favourite_games.items():
        game_titles.append(titles["Title"])

    deleted_games = easygui.buttonbox("What game would you like to delete", \
     choices = game_titles)
    
    favourite_games.pop(deleted_games)

    show_menu()

def quit():
    quit

show_menu()
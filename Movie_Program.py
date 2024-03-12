from easygui import *

movies = {
    "The Shawshank Redemption": {
                                 "Genre": "Drama",
                                 "Duration": 142,
                                 "Showtime":2200,
                                 "Today's Ticket sold":143
                                },
    "The Godfather": {
                                 "Genre": "Drama",
                                 "Duration": 175,
                                 "Showtime":1530,
                                 "Today's Ticket sold":111
                                },
    "Back to the Future": {
                                 "Genre": "Comedy",
                                 "Duration": 116,
                                 "Showtime":1200,
                                 "Today's Ticket sold":102
                                },
    "Spirited Away": {
                                 "Genre": "Family",
                                 "Duration": 125,
                                 "Showtime":930,
                                 "Today's Ticket sold":98
                                },
    "The Lion King": {
                                 "Genre": "Family",
                                 "Duration": 88,
                                 "Showtime":700,
                                 "Today's Ticket sold":123
                                },
}

def movie_change(type):
    input_list = ["Name", "genre", "duration", "showtime","tickets sold"]
    message = ''
    if type == new:
        pass
    elif type == update_movie:
        movie_search = choicebox("What movie do you want to change?", choices = list(movies.keys()))
    else:
        pass
   
    output = multenterbox("movie details", "Add movie", input_list)
    print(output)
    movies.update({output[0]:{
            "Genre":output[1],
            "Duration":output[2],
            "Showtime":output[3],
            "Today's Ticket sold":output[4]


    }})

   

def search():
   
    movie_search = choicebox("What movie are you looking for?", choices = list(movies.keys()))

    display(movie_search)
    if not movie_search:
        return 1

    

    
     
def display(movie_name):
    message = ''
    for i in movies:
        if i == movie_name:
            message += (f"""{i} :  \nGenre: {movies[i]['Genre']} \
    \nDuration: {movies[i]['Duration']}min  \
    \nShowtime: {movies[i]['Showtime']} \
    \nToday's tickets sold: {movies[i]["Today's Ticket sold"]} \n\n""")

    msgbox(message)




def update():
   
    change_options = []
    
    for i in movies:
        if i == movie_search:
            message += (f"""{i} :  \nGenre: {movies[i]['Genre']} \
    \nDuration: {movies[i]['Duration']}min  \
    \nShowtime: {movies[i]['Showtime']} \
    \nToday's tickets sold: {movies[i]["Today's Ticket sold"]} \n\n""")

    for key, value in movies.items():
        print(f"{key} + {value}") 
    buttonbox(message)

def output_movies():
    message = ''
    for i in movies:
        message += (f"""{i} :  \nGenre: {movies[i]['Genre']} \n\
Duration: {movies[i]['Duration']}min  \n\
Showtime: {movies[i]['Showtime']} \n\
Today's tickets sold: {movies[i]["Today's Ticket sold"]} \n\n""")

    msgbox(message)


def leave():
    return None



def main():


    options = {
        "Add new movie":new_movie,
        "Find movie showing":search,
        "Update":update,
        "Output Movies":output_movies,
        "Exit":leave,
        
    }

    running = True
    while running:
        
        msg = "What would you like to do?"
        title = "movie theater"

        choices = (list(options.keys()))
        print(choices)

        selection = buttonbox(msg,title,choices)
        print(type(selection))
        print(options[selection])
        user_choice = options[selection]()


        if not user_choice:
            running = False


main()
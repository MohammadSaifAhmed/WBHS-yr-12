from easygui import *

movies = {
    "The Shawshank Redemption": {
                                 "Genre": "Drama",
                                 "Duration": 142,
                                 "Showtime":2200,
                                 "Today's Tickets sold":143
                                },
    "The Godfather": {
                                 "Genre": "Drama",
                                 "Duration": 175,
                                 "Showtime":1530,
                                 "Today's Tickets sold":111
                                },
    "Back to the Future": {
                                 "Genre": "Comedy",
                                 "Duration": 116,
                                 "Showtime":1200,
                                 "Today's Tickets sold":102
                                },
    "Spirited Away": {
                                 "Genre": "Family",
                                 "Duration": 125,
                                 "Showtime":930,
                                 "Today's Tickets sold":98
                                },
    "The Lion King": {
                                 "Genre": "Family",
                                 "Duration": 88,
                                 "Showtime":700,
                                 "Today's Tickets sold":123
                                },
}

def movie_change():
    input_list = ["Name", "genre", "duration", "showtime","tickets sold"]
    message = ''
  
        
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
    \nToday's tickets sold: {movies[i]["Today's Tickets sold"]} \n\n""")

    return message




def update():
   
    change_options = ["Name", "Genre", "Duration", "Showtime","Today's Tickets sold"]
    message = ''
    movie_name = choicebox("Which movie do you want to update? :" , choices = list(movies.keys()))
    selection = buttonbox("What do you want to change? :" , choices = change_options)

    new_value = enterbox(f"Current {selection}: {movies[movie_name][selection]}")
    movies[movie_name][selection] = new_value
    msgbox(display(movie_name))

    return 1



def output_movies():
    message = ''
    for i in movies:
        message += (display(i))

    for key, value in movies.items():
        print(f"{key} + {value}") 
    buttonbox(message)


def leave():
    return None



def main():


    options = {
        "Add new movie":movie_change,
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
        

        selection = buttonbox(msg,title,choices)
        
        if not options.get(selection):
            running = False
        else:
            user_choice = options[selection]()


            if not user_choice:
                running = False


main()
def main():

    # TODO: Step 2 - Create a complex data structure
    about_me = {
        "full_name": "Pramish Prasad Shrestha",
        "student_id": 10319935,
        "pizza_toppings": ["BACON","ONION","PEPPERS"],
        "movies": [
            {
                "title": "3-idiots",
                "genre": "comedy"
            },
            {
                "title": "intersteller",
                "genre": "sci-fi"
            },
        ]
    }

    # TODO: Step 3 - Add another movie to the data structure
    new_movie = {"title":"tumbbad", "genre": "thiller"}
    about_me["movies"].append(new_movie)

    print_student_name_and_id(about_me)
    add_pizza_toppings(about_me, ("CHEESE","OLIVE"))
    print_pizza_toppings(about_me)
    print_movie_genres(about_me)
    print_movie_titles(about_me)
    
# TODO: Step 4 - Function that prints student name and ID	
def print_student_name_and_id(about_me):
    full_name = about_me["full_name"]
    first_name = full_name.split()[0]
    student_id = about_me["student_id"]
    print(f"My name is {full_name}, but you can call me Mr {first_name}.\nMy student ID is {student_id}.")
    print()
     

# TODO: Step 5 - Function that adds pizza toppings to data structure
def add_pizza_toppings(about_me, toppings):
    about_me["pizza_toppings"].extend(toppings) 
    about_me["pizza_toppings"] = [topping.lower() for topping in about_me['pizza_toppings']]
    return about_me

# TODO: Step 6 - Function that prints bullet list of pizza toppings
def print_pizza_toppings(about_me):
    print(f"My favourite pizza toppings are:")
    for toppings in about_me["pizza_toppings"]:
        print(f"-{toppings}")
    print()
    return
    



# TODO: Step 7 - Function that prints comma-separated list of movie genres
def print_movie_genres(about_me):
    genres = [movie["genre"] for movie in about_me["movies"]]
    print(f"I like to watch {', '.join(genres)} movies.\n")
    print() 
    


# TODO: Step 8 - Function that prints comma-separated list of movie titles
def print_movie_titles(movie_list):
    titles = [movie["title"] for movie in movie_list["movies"]]
    print(f"Some of my favourite movies are {', '.join(titles)}!\n")
    print()
    
if __name__ == '__main__':
    main()
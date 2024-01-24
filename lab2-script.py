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
    
# TODO: Step 4 - Function that prints student name and ID	
def print_student_name_and_id(about_me):
    full_name = about_me["full_name"]
    first_name = full_name.split()[0]
    student_id = about_me["student_id"]
    print(f"My name is {full_name}, but you can call me Mr {first_name}.\nMy student ID is {student_id}.")
    return
    
# TODO: Step 5 - Function that adds pizza toppings to data structure
def add_pizza_toppings(about_me, toppings):
    return

# TODO: Step 6 - Function that prints bullet list of pizza toppings
def print_pizza_toppings(about_me):
    return

# TODO: Step 7 - Function that prints comma-separated list of movie genres
def print_movie_genres(about_me):
    return 

# TODO: Step 8 - Function that prints comma-separated list of movie titles
def print_movie_titles(movie_list):
    return
    
if __name__ == '__main__':
    main()
import math


movies_data = [
    ('Alice', 'Dangal', 'Drama', 'Good', '2016-12-23'),
    ('Alice', 'KGF: Chapter 2', 'Action', 'Average', '2022-04-14'),
    ('Bob', 'Baahubali 2: The Conclusion', 'Action', 'Good', '2017-04-28'),
    ('Charlie', 'RRR', 'Adventure', 'Good', '2022-03-25'),
    ('David', 'Jawan', 'Action', 'Good', '2023-09-07'),
    ('Eve', 'Kalki', 'Adventure', 'Poor', '2019-06-28'),
    ('Eve', 'Pathaan', 'Action', 'Good', '2023-01-25'),
    ('Eve', 'Bajrangi Bhaijaan', 'Drama', 'Good', '2015-07-17'),
    ('Alice', 'Pathaan', 'Action', 'Average', '2023-01-25'),
    ('Charlie', 'KGF: Chapter 2', 'Action', 'Poor', '2022-04-14')
]

books_data = [
    ('Alice', 'To Kill a Mockingbird', 'Fiction', 'Good', '1960-07-11'),
    ('Bob', '1984', 'Dystopian', 'Good', '1949-06-08'),
    ('Charlie', 'Moby Dick', 'Adventure', 'Average', '1851-11-14'),
    ('David', 'Pride and Prejudice', 'Romance', 'Good', '1813-01-28'),
    ('Eve', 'The Great Gatsby', 'Fiction', 'Good', '1925-04-10')
]

products_data = [
    ('Alice', 'Dyson V11 Vacuum Cleaner', 'Home Appliance', 'Good', '2019-03-27', 'Dyson'),
    ('Bob', 'Nikon D3500 DSLR Camera', 'Electronics', 'Good', '2018-08-30', 'Nikon'),
    ('Charlie', 'Apple Watch Series 6', 'Wearable', 'Good', '2020-09-18', 'Apple'),
    ('David', 'Bose QuietComfort 35', 'Audio', 'Good', '2016-05-01', 'Bose'),
    ('Eve', 'Instant Pot Duo 7-in-1', 'Kitchen Appliance', 'Good', '2014-09-01', 'Instant Pot')
]


rating_map = {'Good': 3, 'Average': 2, 'Poor': 1}


movie_details = {item: {'Category': category, 'Rating': rating, 'Release Date': release_date} for user, item, category, rating, release_date in movies_data}
book_details = {item: {'Category': category, 'Rating': rating, 'Release Date': release_date} for user, item, category, rating, release_date in books_data}
product_details = {item: {'Category': category, 'Rating': rating, 'Release Date': release_date, 'Company': company} for user, item, category, rating, release_date, company in products_data}

data = movies_data + books_data + products_data


user_item_ratings = {}
for user, item, category, rating, release_date in movies_data + books_data + [(user, item, category, rating, release_date) for user, item, category, rating, release_date, company in products_data]:
    user_item_ratings.setdefault(user, {})[item] = rating_map[rating]

def cosine_similarity_manual(user1_ratings, user2_ratings):
    dot_product = 0
    norm_user1 = 0
    norm_user2 = 0
    
    for item in set(user1_ratings.keys()).union(user2_ratings.keys()):
        rating1 = user1_ratings.get(item, 0)
        rating2 = user2_ratings.get(item, 0)
        
        dot_product += rating1 * rating2
        norm_user1 += rating1 ** 2
        norm_user2 += rating2 ** 2
    
    if norm_user1 == 0 or norm_user2 == 0:
        return 0

    return dot_product / (math.sqrt(norm_user1) * math.sqrt(norm_user2))


def recommend(user, category):
    if user not in user_item_ratings:
        return "User not found."


    similarity_scores = {}
    for other_user in user_item_ratings:
        if other_user != user:
            similarity = cosine_similarity_manual(user_item_ratings[user], user_item_ratings[other_user])
            similarity_scores[other_user] = similarity


    similar_users = sorted(similarity_scores.items(), key=lambda x: x[1], reverse=True)

    
    recommendations = {}
    
    for similar_user, score in similar_users:
        for item, rating in user_item_ratings[similar_user].items():
            if item not in user_item_ratings[user]: 
                if item in movie_details and category == 'movies':
                    recommendations[item] = recommendations.get(item, 0) + rating * score
                elif item in book_details and category == 'books':
                    recommendations[item] = recommendations.get(item, 0) + rating * score
                elif item in product_details and category == 'products':
                    recommendations[item] = recommendations.get(item, 0) + rating * score

    
    recommended_items = sorted(recommendations.items(), key=lambda x: x[1], reverse=True)

   
    return [item for item, _ in recommended_items]


def filter_movies(category=None, rating=None):
    filtered_movies = []
    for item, details in movie_details.items():
        if category and details['Category'].lower() != category.lower():
            continue
        if rating and details['Rating'].lower() != rating.lower():
            continue
        filtered_movies.append(item)
    return filtered_movies


def filter_books(category=None, rating=None):
    filtered_books = []
    for item, details in book_details.items():
        if category and details['Category'].lower() != category.lower():
            continue
        if rating and details['Rating'].lower() != rating.lower():
            continue
        filtered_books.append(item)
    return filtered_books


def filter_products(rating=None):
    filtered_products = []
    for item, details in product_details.items():
        if rating and details['Rating'].lower() != rating.lower():
            continue
        filtered_products.append(item)
    return filtered_products


while True:
    user_input = input("Enter a command ('recommend', 'filter', 'details', or 'exit'): ").strip().lower()

    if user_input == 'exit':
        print("Exiting the recommendation system. Goodbye!")
        break
    elif user_input == 'recommend':
        user = input("Enter the user name: ").strip().title()
        category = input("Do you want recommendations for 'movies', 'books', or 'products'? ").strip().lower()
        
        if category in ['movies', 'books', 'products']:
            recommendations = recommend(user, category)
            if recommendations:
                print(f"Recommended {category} for {user}:")
                for item in recommendations:
                    print(item)
            else:
                print(f"No recommendations available for {user} in {category}.")
        else:
            print("Invalid category. Please choose 'movies', 'books', or 'products'.")
    elif user_input == 'filter':
        item_type = input("Do you want to filter 'movies', 'books', or 'products'? ").strip().lower()
        
        if item_type == 'movies':
            category = input(f"Enter the movie category (e.g., 'Action', 'Drama', 'Adventure'): ").strip().lower()
            rating = input(f"Enter a rating (e.g., 'Good', 'Average', 'Poor'): ").strip().lower()
            matching_items = filter_movies(category, rating)
        elif item_type == 'books':
            category = input(f"Enter the book category (e.g., 'Fiction', 'Dystopian', 'Adventure', 'Romance'): ").strip().lower()
            rating = input(f"Enter a rating (e.g., 'Good', 'Average', 'Poor'): ").strip().lower()
            matching_items = filter_books(category, rating)
        elif item_type == 'products':
            rating = input(f"Enter a rating (e.g., 'Good', 'Average', 'Poor'): ").strip().lower()
            matching_items = filter_products(rating)
        else:
            print("Invalid item type. Please choose 'movies', 'books', or 'products'.")
            continue
        
        if matching_items:
            print(f"{item_type.capitalize()} that match your criteria:")
            for item in matching_items:
                print(item)
        else:
            print(f"No {item_type} found that match your criteria.")
    else:
        print("Invalid command. Please try again.")

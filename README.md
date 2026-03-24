# Movie Recommendation System

This project is a content-based movie recommendation system built using the MovieLens dataset. The goal is to suggest movies similar to a selected title by analyzing genres and user-generated tags.

The system uses a simple but effective approach that combines text processing and similarity matching to generate relevant recommendations in real time.

---

## Features

- Recommends movies based on similarity  
- Uses genres and tags for better context  
- Real-time recommendations through a Streamlit interface  
- Displays top recommended movies with ratings  
- Includes a “Top Rated Movies” section for basic insights  

---

## Dataset

The project is based on the MovieLens dataset, which includes:

- Movie titles and genres  
- User ratings (5-star scale)  
- User-generated tags  

This dataset is widely used for building and testing recommendation systems.

---

## How It Works

The recommendation system follows these steps:

1. Combines genres and tags into a single text feature  
2. Converts text into numerical form using TF-IDF  
3. Measures similarity between movies using cosine similarity  
4. Recommends the most similar movies to the selected input  

This approach allows the system to find meaningful relationships between movies without requiring complex models.

---

---

## How to Run the Project

1. Clone the repository
 git clone https://github.com/AranyakD/Recommendation-System
 cd DynamixNetworks_Recommendation_System

2. Install the required libraries

3. Run the application

---

## Important Note

The `.pkl` files are not included in this repository because they exceed GitHub’s file size limits.

To run the project locally, you will need to:
- Generate these files using the preprocessing code  
or  
- Place `movies.pkl` and `similarity.pkl` inside a `model/` folder  

---

## Technologies Used

- Python  
- Pandas  
- Scikit-learn  
- Streamlit  

---

## Author

Aranyak Dutta


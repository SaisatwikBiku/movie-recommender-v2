# 🎬 Movie Recommender System

Deployed at: https://movify-mrs-759911d1e181.herokuapp.com/

This project is a content-based movie recommender system built using Python, pandas, scikit-learn, and NLP techniques. It recommends movies similar to a given title based on genres, keywords, cast, crew, and overview.

## Features

- Cleans and preprocesses movie metadata from the TMDB 5000 dataset
- Extracts and combines relevant features (genres, keywords, cast, crew, overview)
- Uses NLP (stemming, vectorization) to process text data
- Computes cosine similarity between movies
- Recommends top 5 similar movies for a given title

## How It Works

1. **Data Loading:** Loads `tmdb_5000_movies.csv` and `tmdb_5000_credits.csv`.
2. **Preprocessing:** Merges datasets, extracts features, removes nulls/duplicates, and processes text.
3. **Feature Engineering:** Combines features into a single 'tags' column and applies stemming.
4. **Vectorization:** Converts text data into vectors using `CountVectorizer`.
5. **Similarity Calculation:** Computes cosine similarity between movie vectors.
6. **Recommendation:** Returns the top 5 most similar movies for a given input title.

## Usage

1. Clone this repository and place the TMDB 5000 dataset files in the project directory.
2. Open `movie-recommender-system.ipynb` in Jupyter Notebook or VS Code.
3. Run all cells.
4. Use the `recommend('Movie Title')` function to get recommendations.

Example:
```python
recommend('Batman Begins')
```
## Requirements

1. Python 3.x
2. Pandas
3. Numpy
4. scikit-learn
5. nltk

Install Dependencies:
```bash
pip install pandas numpy scikit-learn nltk
```

## app.py

For the app.py to work, you will have to first use tuple to extract .pkl files for movies_dict.pkl and similarity.pkl. To get those files, go to movie-recommender-system.ipynb then import tuple module. Then use the following code:

```python
pickle.dump(new_movies.to_dict(), open('movies_dict.pkl', 'wb'))
pickle.dump(similarity, open('similarity.pkl', 'wb'))
```

This Project is going through active development. This Readme gives basic idea only.

import streamlit as st
from PIL import Image

# Liste fictive de films
movies = [
    {"title": "Inception", "description": "A thief who steals corporate secrets through dream-sharing technology.", "genres": ["Action", "Adventure", "Sci-Fi"]},
    {"title": "The Dark Knight", "description": "Batman faces the Joker in a fight for Gotham City.", "genres": ["Action", "Crime", "Drama"]},
    {"title": "Interstellar", "description": "A team of explorers travel through a wormhole in space.", "genres": ["Adventure", "Drama", "Sci-Fi"]},
    {"title": "The Matrix", "description": "A computer hacker learns about the true nature of reality.", "genres": ["Action", "Sci-Fi"]},
    {"title": "Titanic", "description": "A romance unfolds aboard the ill-fated RMS Titanic.", "genres": ["Drama", "Romance"]},
]

# Fonction pour insérer du CSS personnalisé
def set_custom_css():
    st.markdown(
        """
        <style>
        /* Arrière-plan sombre */
        body {
            background-color: #141414;
            color: #ffffff;
            font-family: Arial, sans-serif;
        }

        /* Style principal de l'application */
        .stApp {
            background-color: #141414;
        }

        /* Titres */
        h1, h2, h3, h4 {
            color: #e50914;
            font-weight: bold;
        }

        /* Widgets (Barre de recherche, sélections, etc.) */
        .stTextInput > div > div > input, .stSelectbox > div > div > div > div > div {
            background-color: #333333;
            color: white;
            border: none;
            padding: 10px;
            border-radius: 5px;
        }

        /* Boutons */
        .stButton > button {
            background-color: #e50914;
            color: white;
            font-weight: bold;
            font-size: 16px;
            border: none;
            border-radius: 5px;
            padding: 10px 20px;
            box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.3);
        }
        .stButton > button:hover {
            background-color: #f40612;
            box-shadow: 0px 6px 12px rgba(0, 0, 0, 0.5);
        }

        /* Cartes des films */
        .movie-card {
            background-color: #1c1c1c;
            border-radius: 10px;
            padding: 20px;
            margin-bottom: 20px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.5);
            border: 1px solid #333333;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

# Appliquer le style
set_custom_css()

# Header avec design Netflix
st.markdown(
    """
    <h1 style="text-align: center;">🎬 Recommandation de Films</h1>
    <p style="text-align: center; font-size: 18px; color: #e50914;">Découvrez des films captivants inspirés de Netflix.</p>
    """,
    unsafe_allow_html=True,
)

# Barre de recherche
search_query = st.text_input("🔍 Rechercher un film par titre ou description :")

# Filtrage par genre
genres = sorted(set(genre for movie in movies for genre in movie["genres"]))
selected_genre = st.selectbox("🎯 Filtrer par genre :", ["Tous"] + genres)

# Résultats
filtered_movies = movies

# Appliquer la recherche
if search_query:
    filtered_movies = [
        movie for movie in filtered_movies
        if search_query.lower() in movie["title"].lower() or search_query.lower() in movie["description"].lower()
    ]

# Appliquer le filtre de genre
if selected_genre != "Tous":
    filtered_movies = [
        movie for movie in filtered_movies if selected_genre in movie["genres"]
    ]

# Afficher les résultats
st.markdown("### 🎞️ Résultats :")
if filtered_movies:
    for movie in filtered_movies:
        st.markdown(
            f"""
            <div class="movie-card">
                <h2>{movie['title']}</h2>
                <p><strong>Description :</strong> {movie['description']}</p>
                <p><strong>Genres :</strong> {', '.join(movie['genres'])}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
else:
    st.markdown("🎬 Aucun film ne correspond à votre recherche. Essayez une autre requête.")

# Bouton interactif
if st.button("🎲 Surprise Me!"):
    import random
    random_movie = random.choice(movies)
    st.success(f"Vous devriez regarder : **{random_movie['title']}** - {', '.join(random_movie['genres'])}")

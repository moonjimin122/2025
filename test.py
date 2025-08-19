import streamlit as st
import requests
import random

# 🔑 API 키 입력
TMDB_API_KEY = "여기에_TMDB_API_KEY_입력"
GOOGLE_BOOKS_API_KEY = "여기에_GOOGLE_BOOKS_API_KEY_입력"

# 장르 매핑
book_genre_map = {
    "로맨스": "romance",
    "판타지": "fantasy",
    "스릴러": "thriller",
    "SF": "science fiction"
}

movie_genre_map = {
    "로맨스": 10749,
    "판타지": 14,
    "스릴러": 53,
    "SF": 878
}

genres = list(book_genre_map.keys())

# 🎨 Streamlit UI
st.title("📚🎬 장르 기반 책 & 영화 추천기")

genre = st.selectbox("관심 있는 장르를 선택하세요:", genres)
content_type = st.radio("추천 받고 싶은 콘텐츠를 선택하세요:", ["책", "영화"])


# ✅ Google Books API (책 추천)
def get_books(genre, n=3):
    subject = book_genre_map[genre]
    url = f"https://www.googleapis.com/books/v1/volumes?q=subject:{subject}&maxResults=20&langRestrict=ko&key={GOOGLE_BOOKS_API_KEY}"
    res = requests.get(url)
    data = res.json()
    books = []
    if "items" in data:
        items = random.sample(data["items"], min(n, len(data["items"])))
        for item in items:
            info = item.get("volumeInfo", {})
            books.append({
                "제목": info.get("title", "제목 없음"),
                "줄거리": info.get("description", "줄거리 정보 없음"),
                "이미지": info.get("imageLinks", {}).get("thumbnail", "https://cdn-icons-png.flaticon.com/512/29/29302.png")
            })
    return books


# ✅ TMDB API (영화 추천)
def get_movies(genre, n=3):
    url = f"https://api.themoviedb.org/3/discover/movie?api_key={TMDB_API_KEY}&with_genres={movie_genre_map[genre]}&language=ko-KR"
    res = requests.get(url)
    data = res.json()
    movies = []
    if "results" in data:
        items = random.sample(data["results"], min(n, len(data["results"])))
        for item in items:
            movies.append({
                "제목": item.get("title", "제목 없음"),
                "줄거리": item.get("overview", "줄거리 정보 없음"),
                "이미지": f"https://image.tmdb.org/t/p/w500{item['poster_path']}" if item.get("poster_path") else "https://cdn-icons-png.flaticon.com/512/74/74472.png"
            })
    return movies


# ✅ 결과 출력
if genre and content_type:
    st.subheader(f"👉 {genre} 장르의 {content_type} 추천 (3개)")

    recs = get_books(genre, 3) if content_type == "책" else get_movies(genre, 3)

    if recs:
        for idx, choice in enumerate(recs, 1):
            st.markdown(f"### {idx}. {choice['제목']}")
            st.image(choice["이미지"], width=200)
            st.write(f"**줄거리**: {choice['줄거리']}")
            st.markdown("---")
    else:
        st.warning("추천 결과를 불러오지 못했습니다. 😢")

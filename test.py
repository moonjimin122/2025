import streamlit as st
import requests
import random
import os

# 🔑 API 키 (여기에 직접 입력하거나, 환경변수 사용)
TMDB_API_KEY = "여기에_TMDB_API_KEY"
GOOGLE_BOOKS_API_KEY = "여기에_GOOGLE_BOOKS_API_KEY"

# 장르 매핑 (간단 버전)
genres = ["로맨스", "판타지", "스릴러", "SF"]

# TMDB 장르 코드 매핑
tmdb_genres = {
    "로맨스": 10749,
    "판타지": 14,
    "스릴러": 53,
    "SF": 878
}

# Google Books 검색어 매핑
book_keywords = {
    "로맨스": "romance novel",
    "판타지": "fantasy novel",
    "스릴러": "thriller novel",
    "SF": "science fiction novel"
}

# 영화 추천 (TMDB API)
def get_movies(genre, n=3):
    url = f"https://api.themoviedb.org/3/discover/movie"
    params = {
        "api_key": TMDB_API_KEY,
        "with_genres": tmdb_genres[genre],
        "language": "ko-KR",
        "sort_by": "popularity.desc",
        "page": 1
    }
    response = requests.get(url, params=params).json()
    results = response.get("results", [])
    if not results:
        return []
    choices = random.sample(results, min(n, len(results)))
    movies = []
    for m in choices:
        poster = f"https://image.tmdb.org/t/p/w500{m['poster_path']}" if m.get("poster_path") else None
        movies.append({
            "제목": m["title"],
            "줄거리": m["overview"] if m["overview"] else "줄거리 없음",
            "이미지": poster
        })
    return movies

# 책 추천 (Google Books API)
def get_books(genre, n=3):
    keyword = book_keywords[genre]
    url = "https://www.googleapis.com/books/v1/volumes"
    params = {
        "q": keyword,
        "key": GOOGLE_BOOKS_API_KEY,
        "maxResults": 20,
        "printType": "books",
        "langRestrict": "ko"  # 한국어 우선
    }
    response = requests.get(url, params=params).json()
    items = response.get("items", [])
    if not items:
        return []
    choices = random.sample(items, min(n, len(items)))
    books = []
    for b in choices:
        info = b.get("volumeInfo", {})
        image = info.get("imageLinks", {}).get("thumbnail")
        books.append({
            "제목": info.get("title", "제목 없음"),
            "줄거리": info.get("description", "줄거리 없음"),
            "이미지": image
        })
    return books

# Streamlit UI
st.title("📚🎬 장르 기반 책 & 영화 추천기 (API 버전)")

genre = st.selectbox("관심 있는 장르를 선택하세요:", genres)
content_type = st.radio("추천 받고 싶은 콘텐츠를 선택하세요:", ["책", "영화"])

if genre and content_type:
    st.subheader(f"👉 {genre} 장르의 {content_type} 추천 (3개)")
    
    if content_type == "영화":
        results = get_movies(genre, n=3)
    else:
        results = get_books(genre, n=3)
    
    if results:
        for idx, item in enumerate(results, 1):
            st.markdown(f"### {idx}. {item['제목']}")
            if item["이미지"]:
                st.image(item["이미지"], width=200)
            st.write(f"**줄거리**: {item['줄거리']}")
            st.markdown("---")
    else:
        st.warning("추천 결과가 없습니다. 😢")

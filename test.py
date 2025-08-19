import streamlit as st

# 한국 영화 데이터 (포스터 URL 포함 예시)
MOVIES = {
    "로맨스": [
        {"title": "건축학개론", "desc": "첫사랑을 다시 마주한 청춘 멜로", 
         "poster": "https://upload.wikimedia.org/wikipedia/ko/3/3d/Architecture_101_poster.jpg"},
        {"title": "클래식", "desc": "세대를 아우르는 사랑 이야기", 
         "poster": "https://upload.wikimedia.org/wikipedia/ko/0/05/The_Classic_film_poster.jpg"},
        {"title": "너의 결혼식", "desc": "첫사랑과의 10년 인연", 
         "poster": "https://upload.wikimedia.org/wikipedia/ko/4/46/On_Your_Wedding_Day.jpg"},
        {"title": "더 테이블", "desc": "카페 테이블에서 오가는 네 가지 이야기", 
         "poster": "https://upload.wikimedia.org/wikipedia/ko/f/fc/The_Table_%28film%29.jpg"},
        {"title": "조제", "desc": "운명처럼 다가온 사랑", 
         "poster": "https://upload.wikimedia.org/wikipedia/ko/c/c2/Josee_2020.jpg"},
    ],
    "액션": [
        {"title": "아저씨", "desc": "과거를 숨긴 남자의 구출 액션", 
         "poster": "https://upload.wikimedia.org/wikipedia/ko/5/5c/The_Man_from_Nowhere_poster.jpg"},
        {"title": "부산행", "desc": "좀비로부터의 생존 열차", 
         "poster": "https://upload.wikimedia.org/wikipedia/ko/c/c7/Train_to_Busan_poster.jpg"},
        {"title": "베테랑", "desc": "강력반 형사의 통쾌한 수사극", 
         "poster": "https://upload.wikimedia.org/wikipedia/ko/d/d4/Veteran_%28film%29.jpg"},
        {"title": "범죄도시", "desc": "강력반 형사와 범죄조직의 대결", 
         "poster": "https://upload.wikimedia.org/wikipedia/ko/7/7d/The_Outlaws.jpg"},
        {"title": "신세계", "desc": "언더커버 형사의 조직 잠입", 
         "poster": "https://upload.wikimedia.org/wikipedia/ko/6/6b/New_World_poster.jpg"},
    ],
    # 다큐멘터리 / 코미디도 같은 구조로 추가 가능
}

# 앱 제목
st.title("🎬 한국 영화 추천 앱")

st.write("원하는 테마를 선택하면 해당 테마의 영화들을 포스터와 함께 추천해드립니다!")

# 테마 선택
themes = list(MOVIES.keys())
selected_theme = st.selectbox("테마 선택", themes)

# 선택한 테마의 영화만 출력
st.subheader(f"⭐ {selected_theme} 영화 추천")
for m in MOVIES[selected_theme]:
    st.image(m["poster"], width=200)
    st.write(f"🎥 **{m['title']}** - {m['desc']}")
    st.markdown("---")

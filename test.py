import streamlit as st
import random

# 한국 영화 데이터
MOVIES = [
    # Romance
    {"title": "건축학개론", "theme": "로맨스", "desc": "첫사랑을 다시 마주한 청춘 멜로"},
    {"title": "클래식", "theme": "로맨스", "desc": "세대를 아우르는 사랑 이야기"},
    {"title": "너의 결혼식", "theme": "로맨스", "desc": "첫사랑과의 10년 인연"},
    {"title": "더 테이블", "theme": "로맨스", "desc": "카페 테이블에서 오가는 네 가지 이야기"},
    {"title": "조제", "theme": "로맨스", "desc": "운명처럼 다가온 사랑"},

    # Action
    {"title": "아저씨", "theme": "액션", "desc": "과거를 숨긴 남자의 구출 액션"},
    {"title": "부산행", "theme": "액션", "desc": "좀비로부터의 생존 열차"},
    {"title": "베테랑", "theme": "액션", "desc": "강력반 형사의 통쾌한 수사극"},
    {"title": "범죄도시", "theme": "액션", "desc": "강력반 형사와 범죄조직의 대결"},
    {"title": "신세계", "theme": "액션", "desc": "언더커버 형사의 조직 잠입"},

    # Documentary
    {"title": "님아, 그 강을 건너지 마오", "theme": "다큐멘터리", "desc": "노부부의 사랑과 삶"},
    {"title": "워낭소리", "theme": "다큐멘터리", "desc": "노부부와 소의 정겨운 삶"},
    {"title": "김군", "theme": "다큐멘터리", "desc": "1980년 광주의 기억"},
    {"title": "또 다른 가족", "theme": "다큐멘터리", "desc": "삼성 백혈병 피해자 가족 이야기"},
    {"title": "북극의 눈물", "theme": "다큐멘터리", "desc": "북극의 환경 다큐멘터리"},

    # Comedy
    {"title": "극한직업", "theme": "코미디", "desc": "치킨 장사로 위장한 마약 수사반"},
    {"title": "수상한 그녀", "theme": "코미디", "desc": "청춘으로 돌아간 할머니의 이야기"},
    {"title": "해적: 바다로 간 산적", "theme": "코미디", "desc": "해적과 산적의 유쾌한 모험"},
    {"title": "스물", "theme": "코미디", "desc": "스무 살 청춘들의 성장담"},
    {"title": "타짜", "theme": "코미디", "desc": "화투판의 세계와 인간 욕망"},
]

# 앱 제목
st.title("🎬 한국 영화 추천 앱")

# 테마 선택
themes = ["전체", "로맨스", "액션", "다큐멘터리", "코미디"]
selected_theme = st.sidebar.selectbox("테마 선택", themes)

# 검색
query = st.sidebar.text_input("검색어 입력")

# 필터링
filtered = [
    m for m in MOVIES
    if (selected_theme == "전체" or m["theme"] == selected_theme)
    and (query.lower() in m["title"].lower() or query.lower() in m["desc"].lower())
]

st.subheader(f"추천 영화 목록 ({len(filtered)}편)")
for m in filtered:
    st.write(f"**{m['title']}** ({m['theme']}) - {m['desc']}")

# 랜덤 추천
if st.button("랜덤 추천 🎲"):
    if filtered:
        choice = random.choice(filtered)
        st.success(f"오늘의 추천: **{choice['title']}** - {choice['desc']}")
    else:
        st.warning("조건에 맞는 영화가 없습니다.")

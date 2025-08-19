import streamlit as st
import random

# 샘플 데이터 (장르별 책/영화 매핑)
recommendations = {
    "로맨스": {
        "책": ["콜레라 시대의 사랑 - 가브리엘 가르시아 마르케스", "노르웨이의 숲 - 무라카미 하루키"],
        "영화": ["노팅힐", "라라랜드", "이터널 선샤인"]
    },
    "판타지": {
        "책": ["해리 포터 - J.K. 롤링", "반지의 제왕 - J.R.R. 톨킨"],
        "영화": ["해리 포터 시리즈", "반지의 제왕 시리즈", "나니아 연대기"]
    },
    "스릴러": {
        "책": ["셜록 홈즈 - 아서 코난 도일", "용의자 X의 헌신 - 히가시노 게이고"],
        "영화": ["세븐", "메멘토", "살인의 추억"]
    },
    "SF": {
        "책": ["듄 - 프랭크 허버트", "안드로메다 성운 - 이반 예프레모프"],
        "영화": ["인터스텔라", "인셉션", "매트릭스"]
    }
}

# 특정 장르가 '책 중심'인지 '영화 중심'인지 매핑 (임의 지정)
focus = {
    "로맨스": "책",
    "판타지": "영화",
    "스릴러": "책",
    "SF": "영화"
}

# Streamlit UI
st.title("📚🎬 장르 기반 책 & 영화 추천기")

# 장르 선택
genre = st.selectbox("관심 있는 장르를 선택하세요:", list(recommendations.keys()))

if genre:
    st.subheader(f"👉 선택한 장르: {genre}")

    # 중심 콘텐츠 결정
    main_type = focus[genre]
    other_type = "책" if main_type == "영화" else "영화"

    # 랜덤 추천
    main_choice = random.choice(recommendations[genre][main_type])
    other_choice = random.choice(recommendations[genre][other_type])

    # 출력
    st.write(f"**{main_type} 추천:** {main_choice}")
    st.write(f"**{other_type} 추천:** {other_choice}")

    st.success(f"이 장르는 보통 **{main_type} 중심**으로 추천돼요!")

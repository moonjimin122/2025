import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="MBTI 궁합 매칭 💞",
    page_icon="💘",
    layout="centered",
)

# 스타일 추가 (CSS)
st.markdown("""
    <style>
    .match-box {
        background-color: #fff0f5;
        padding: 20px;
        border-radius: 12px;
        margin-bottom: 15px;
        box-shadow: 2px 2px 8px rgba(0,0,0,0.05);
        border-left: 5px solid #f06292;
    }
    .footer {
        text-align: center;
        font-size: 0.9em;
        color: #aaa;
        margin-top: 50px;
    }
    .mbti-title {
        font-size: 1.3em;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# MBTI 궁합 데이터
mbti_matches = {
    "INFP": ["ENFJ", "INFJ"],
    "ENFP": ["INFJ", "INTJ"],
    "INFJ": ["ENFP", "ENTP"],
    "ENFJ": ["INFP", "ISFP"],
    "INTP": ["ENTJ", "ENTP"],
    "ENTP": ["INFJ", "INFP"],
    "INTJ": ["ENFP", "ENTP"],
    "ENTJ": ["INTP", "INFP"],
    "ISFP": ["ESFJ", "ENFJ"],
    "ESFP": ["ISFJ", "ISTJ"],
    "ISTP": ["ESTJ", "ESFJ"],
    "ESTP": ["ISFJ", "ISTJ"],
    "ISFJ": ["ESFP", "ESTP"],
    "ESFJ": ["ISFP", "ISTP"],
    "ISTJ": ["ESFP", "ENFP"],
    "ESTJ": ["ISTP", "INTP"],
}

# MBTI 간단 설명
mbti_descriptions = {
    "INFP": "이상주의적인 중재자 🧚",
    "ENFP": "열정적인 활동가 🔥",
    "INFJ": "통찰력 있는 옹호자 🌌",
    "ENFJ": "카리스마 있는 지도자 🌟",
    "INTP": "논리적인 사색가 🧠",
    "ENTP": "토론을 즐기는 혁신가 🗣️",
    "INTJ": "전략적인 계획가 ♟️",
    "ENTJ": "리더십 강한 통솔자 🧭",
    "ISFP": "예술적인 평화주의자 🎨",
    "ESFP": "자유로운 연예인 🎤",
    "ISTP": "모험적인 장인 🔧",
    "ESTP": "활동적인 사업가 🚀",
    "ISFJ": "헌신적인 수호자 🛡️",
    "ESFJ": "사교적인 외교관 🥂",
    "ISTJ": "신중한 관리자 📋",
    "ESTJ": "체계적인 감독관 🏛️",
}

# 헤더
st.title("💞 MBTI 궁합 매칭 웹앱")
st.markdown("당신의 MBTI를 선택하면, 어울리는 MBTI 유형을 알려드릴게요! ✨")

# 선택 박스
mbti_list = list(mbti_matches.keys())
user_mbti = st.selectbox("👇 당신의 MBTI를 선택하세요", mbti_list)

# 결과 표시
if user_mbti:
    st.markdown("---")
    st.markdown(f"<div class='mbti-title'>🔍 당신은 <span style='color:#d81b60'>{user_mbti}</span> - {mbti_descriptions[user_mbti]}</div>", unsafe_allow_html=True)
    st.markdown("### 💘 어울리는 MBTI 유형:")

    matches = mbti_matches[user_mbti]
    for match in matches:
        description = mbti_descriptions.get(match, "설명 없음")
        st.markdown(f"""
        <div class="match-box">
            <strong>{match}</strong> - {description}
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    st.info("💡 MBTI 궁합은 재미로만 봐주세요! 성격과 관계는 다양하고 유동적이니까요 😊")

# 푸터
st.markdown("""
<div class="footer">
    Made with ❤️ by MBTI 궁합 도우미 | © 2025
</div>
""", unsafe_allow_html=True)

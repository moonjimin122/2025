import streamlit as st

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

st.title("💞 MBTI 궁합 매칭 웹앱")
st.write("당신의 MBTI를 선택하면 어울리는 MBTI 유형을 알려드릴게요!")

mbti_types = list(mbti_matches.keys())
selected_mbti = st.selectbox("당신의 MBTI를 선택하세요:", mbti_types)

if selected_mbti:
    matches = mbti_matches[selected_mbti]
    st.subheader(f"💘 {selected_mbti}와 잘 어울리는 MBTI 유형:")
    for match in matches:
        st.markdown(f"- **{match}**")

    # 선택적으로 설명 추가
    st.markdown("---")
    st.markdown("💡 *MBTI 궁합은 절대적인 것은 아니며, 성격은 개인마다 다릅니다. 재미로 봐주세요!*")


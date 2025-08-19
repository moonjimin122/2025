import streamlit as st
import random

# 샘플 데이터 (제목 + 줄거리 + 이미지 URL)
recommendations = {
    "로맨스": {
        "책": [
            {"제목": "콜레라 시대의 사랑",
             "줄거리": "평생에 걸친 사랑과 기다림을 그린 고전 로맨스 소설.",
             "이미지": "https://upload.wikimedia.org/wikipedia/en/4/4f/Love_in_the_Time_of_Cholera.jpg"},
            {"제목": "노르웨이의 숲",
             "줄거리": "청춘의 방황과 사랑, 상실을 담은 서정적인 이야기.",
             "이미지": "https://upload.wikimedia.org/wikipedia/en/8/8a/Norwegian_Wood_book_cover.jpg"},
            {"제목": "연애의 기술",
             "줄거리": "현대인의 사랑을 철학적으로 탐구한 작품.",
             "이미지": "https://upload.wikimedia.org/wikipedia/en/f/fd/Essays_in_Love.jpg"}
        ],
        "영화": [
            {"제목": "노팅힐",
             "줄거리": "평범한 서점 주인이 세계적인 배우와 사랑에 빠지는 이야기.",
             "이미지": "https://upload.wikimedia.org/wikipedia/en/3/38/NottingHillRobertsGrant.jpg"},
            {"제목": "라라랜드",
             "줄거리": "꿈을 좇는 두 남녀의 사랑과 현실 사이의 갈등을 담은 뮤지컬 영화.",
             "이미지": "https://upload.wikimedia.org/wikipedia/en/a/ab/La_La_Land_%28film%29.png"},
            {"제목": "이터널 선샤인",
             "줄거리": "사랑의 기억을 지우려는 남녀가 다시 서로를 찾아가는 독특한 로맨스.",
             "이미지": "https://upload.wikimedia.org/wikipedia/en/6/62/Eternal_Sunshine_of_the_Spotless_Mind.png"},
            {"제목": "비포 선라이즈",
             "줄거리": "기차에서 우연히 만난 두 사람이 하루 동안 사랑을 나누는 이야기.",
             "이미지": "https://upload.wikimedia.org/wikipedia/en/d/da/Before_Sunrise_poster.jpg"}
        ]
    },
    "판타지": {
        "책": [
            {"제목": "해리 포터와 마법사의 돌",
             "줄거리": "소년 마법사 해리 포터가 호그와트에 입학하면서 시작되는 모험.",
             "이미지": "https://upload.wikimedia.org/wikipedia/en/6/6b/HP1_cover.jpg"},
            {"제목": "반지의 제왕: 반지 원정대",
             "줄거리": "절대 반지를 파괴하기 위해 떠나는 모험과 우정의 이야기.",
             "이미지": "https://upload.wikimedia.org/wikipedia/en/8/8e/The_Fellowship_of_the_Ring_cover.gif"},
            {"제목": "나니아 연대기",
             "줄거리": "옷장 속 판타지 세계 나니아에서의 전투와 모험.",
             "이미지": "https://upload.wikimedia.org/wikipedia/en/c/cb/The_Chronicles_of_Narnia_box_set_cover.jpg"}
        ],
        "영화": [
            {"제목": "반지의 제왕: 반지 원정대",
             "줄거리": "절대 반지를 없애기 위한 원정이 시작된다.",
             "이미지": "https://upload.wikimedia.org/wikipedia/en/0/0c/The_Lord_of_the_Rings_The_Fellowship_of_the_Ring_%282001%29.jpg"},
            {"제목": "해리 포터와 마법사의 돌",
             "줄거리": "마법사의 세계에 입문한 해리의 첫 모험.",
             "이미지": "https://upload.wikimedia.org/wikipedia/en/6/6b/HP1_cover.jpg"},
            {"제목": "나니아 연대기: 사자, 마녀 그리고 옷장",
             "줄거리": "네 남매가 옷장 속 세계 나니아에서 대모험을 펼친다.",
             "이미지": "https://upload.wikimedia.org/wikipedia/en/c/cb/The_Chronicles_of_Narnia_The_Lion%2C_the_Witch_and_the_Wardrobe_poster.jpg"},
            {"제목": "판의 미로: 오필리아와 세 개의 열쇠",
             "줄거리": "스페인 내전 후 소녀가 환상 세계와 현실 사이를 넘나드는 이야기.",
             "이미지": "https://upload.wikimedia.org/wikipedia/en/6/6f/Pans_labyrinth.jpg"}
        ]
    },
    "스릴러": {
        "책": [
            {"제목": "다 빈치 코드",
             "줄거리": "암호와 미스터리를 풀어가는 종교적 스릴러.",
             "이미지": "https://upload.wikimedia.org/wikipedia/en/6/6b/DaVinciCode.jpg"},
            {"제목": "드래곤 타투를 한 소녀",
             "줄거리": "사라진 소녀의 비밀을 추적하는 범죄 스릴러.",
             "이미지": "https://upload.wikimedia.org/wikipedia/en/0/0c/The_Girl_with_the_Dragon_Tattoo_Poster.jpg"},
            {"제목": "셜록 홈즈의 모험",
             "줄거리": "명탐정 셜록 홈즈의 추리와 스릴 넘치는 사건들.",
             "이미지": "https://upload.wikimedia.org/wikipedia/commons/8/8d/Sherlock_Holmes_Adventures.jpg"}
        ],
        "영화": [
            {"제목": "세븐",
             "줄거리": "7대 죄악을 모티브로 한 연쇄 살인 사건 추적.",
             "이미지": "https://upload.wikimedia.org/wikipedia/en/6/68/Seven_%28movie%29_poster.jpg"},
            {"제목": "셔터 아일랜드",
             "줄거리": "고립된 정신병원에서 벌어지는 미스터리 스릴러.",
             "이미지": "https://upload.wikimedia.org/wikipedia/en/7/76/Shutterislandposter.jpg"},
            {"제목": "메멘토",
             "줄거리": "단기 기억 상실증 환자의 복수극을 그린 독특한 스릴러.",
             "이미지": "https://upload.wikimedia.org/wikipedia/en/c/c7/Memento_poster.jpg"},
            {"제목": "올드보이",
             "줄거리": "15년간 감금되었던 남자의 충격적 복수극.",
             "이미지": "https://upload.wikimedia.org/wikipedia/en/6/67/Oldboykoreanposter.jpg"}
        ]
    },
    "SF": {
        "책": [
            {"제목": "듄",
             "줄거리": "사막 행성 아라키스를 둘러싼 권력과 생존의 서사.",
             "이미지": "https://upload.wikimedia.org/wikipedia/en/a/a4/Dune-Frank_Herbert_%281965%29_First_edition.jpg"},
            {"제목": "안드로메다 성운",
             "줄거리": "이상적인 미래 사회와 우주 탐험을 그린 소련 SF 고전.",
             "이미지": "https://upload.wikimedia.org/wikipedia/commons/5/58/Andromeda_Nebula_cover.jpg"},
            {"제목": "1984",
             "줄거리": "감시와 통제가 지배하는 디스토피아 사회의 이야기.",
             "이미지": "https://upload.wikimedia.org/wikipedia/en/c/c3/1984first.jpg"}
        ],
        "영화": [
            {"제목": "인터스텔라",
             "줄거리": "지구를 떠나 새로운 행성을 찾아 떠나는 우주 탐험.",
             "이미지": "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg"},
            {"제목": "인셉션",
             "줄거리": "꿈속에서 벌어지는 스파이 액션과 현실을 넘나드는 이야기.",
             "이미지": "https://upload.wikimedia.org/wikipedia/en/7/7e/Inception_ver3.jpg"},
            {"제목": "매트릭스",
             "줄거리": "가상현실 세계와 인간의 자유를 위한 혁명적 싸움.",
             "이미지": "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg"},
            {"제목": "블레이드 러너 2049",
             "줄거리": "인간과 인조인간의 경계와 존재의 의미를 탐구하는 미래 도시 이야기.",
             "이미지": "https://upload.wikimedia.org/wikipedia/en/2/27/Blade_Runner_2049_logo.png"}
        ]
    }
}

# Streamlit UI
st.title("📚🎬 장르 기반 책 & 영화 추천기")

# 장르 선택
genre = st.selectbox("관심 있는 장르를 선택하세요:", list(recommendations.keys()))

# 콘텐츠 타입 선택
content_type = st.radio("추천 받고 싶은 콘텐츠를 선택하세요:", ["책", "영화"])

if genre and content_type:
    st.subheader(f"👉 {genre} 장르의 {content_type} 추천 (3개)")
    choices = random.sample(recommendations[genre][content_type], 3)  # 3개 랜덤 선택
    for idx, choice in enumerate(choices, 1):
        st.markdown(f"### {idx}. {choice['제목']}")
        st.image(choice["이미지"], width=200)
        st.write(f"**줄거리**: {choice['줄거리']}")
        st.markdown("---")

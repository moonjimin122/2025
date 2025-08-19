import streamlit as st
import random

# 샘플 데이터 (제목 + 줄거리 + 이미지 URL)
recommendations = {
    "로맨스 ❤️": {
        "책": [
            {"제목": "노멀 피플", 
             "줄거리": "두 청춘 남녀가 엇갈리며 성장하는 섬세한 로맨스.", 
             "이미지": "https://upload.wikimedia.org/wikipedia/en/2/2e/NormalPeople.png"},
            {"제목": "파친코", 
             "줄거리": "일본에 이주한 한국인 가족의 사랑과 생존 이야기.", 
             "이미지": "https://upload.wikimedia.org/wikipedia/en/e/e8/Pachinko_%28novel%29.png"},
            {"제목": "비포 위 워 스트레인저스", 
             "줄거리": "첫사랑과 재회의 기적 같은 순간을 그린 현대 로맨스.", 
             "이미지": "https://images-na.ssl-images-amazon.com/images/I/81OthjkJBuL.jpg"},
            {"제목": "브리짓 존스의 일기 (1996)", 
             "줄거리": "30대 싱글 여성의 연애와 일상을 유쾌하게 그린 베스트셀러.", 
             "이미지": "https://upload.wikimedia.org/wikipedia/en/1/1a/BridgetJonesDiaryBook.jpg"}
        ],
        "영화": [
            {"제목": "어바웃 타임", 
             "줄거리": "시간 여행 능력을 가진 남자가 사랑을 찾아가는 이야기.", 
             "이미지": "https://upload.wikimedia.org/wikipedia/en/7/7c/About_Time_%282013_film%29.png"},
            {"제목": "콜 미 바이 유어 네임", 
             "줄거리": "이탈리아 여름, 첫사랑의 찬란함을 담은 로맨스.", 
             "이미지": "https://upload.wikimedia.org/wikipedia/en/7/71/Call_Me_by_Your_Name_%28film%29.png"},
            {"제목": "비긴 어게인", 
             "줄거리": "우연한 만남으로 인생의 두 번째 기회를 찾는 이야기.", 
             "이미지": "https://upload.wikimedia.org/wikipedia/en/5/55/Begin_Again_film_poster_2014.png"},
            {"제목": "노팅힐 (1999)", 
             "줄거리": "평범한 남자와 세계적인 배우의 사랑 이야기.", 
             "이미지": "https://upload.wikimedia.org/wikipedia/en/3/38/NottingHillRobertsGrant.jpg"}
        ]
    },
    "판타지 🧙": {
        "책": [
            {"제목": "그리샤버스: 그림과 뼈", 
             "줄거리": "어둠의 힘을 넘어 빛을 찾아가는 소녀의 모험.", 
             "이미지": "https://upload.wikimedia.org/wikipedia/en/a/a6/Shadow_and_Bone.png"},
            {"제목": "왕좌의 게임 (1996)", 
             "줄거리": "철왕좌를 차지하기 위한 정치와 전쟁, 그리고 용의 이야기.", 
             "이미지": "https://upload.wikimedia.org/wikipedia/en/9/93/AGameOfThrones.jpg"},
            {"제목": "어둠의 마법사", 
             "줄거리": "어린 마법사의 성장과 판타지 세계의 전쟁.", 
             "이미지": "https://m.media-amazon.com/images/I/81bWc4HhU6L.jpg"},
            {"제목": "황금 나침반 (1995)", 
             "줄거리": "평행 세계의 모험과 마법, 운명을 찾는 소녀의 여정.", 
             "이미지": "https://upload.wikimedia.org/wikipedia/en/2/2e/Northern_Lights_%28novel%29.jpg"}
        ],
        "영화": [
            {"제목": "말레피센트", 
             "줄거리": "잠자는 숲속의 공주 이야기를 새롭게 해석한 판타지.", 
             "이미지": "https://upload.wikimedia.org/wikipedia/en/7/7e/Maleficent_poster.jpg"},
            {"제목": "신비한 동물사전", 
             "줄거리": "마법 동물들과의 모험을 그린 해리포터 세계관 영화.", 
             "이미지": "https://upload.wikimedia.org/wikipedia/en/3/3c/Fantastic_Beasts_and_Where_to_Find_Them_poster.png"},
            {"제목": "위대한 쇼맨", 
             "줄거리": "상상력으로 무대를 바꾼 남자의 뮤지컬 판타지.", 
             "이미지": "https://upload.wikimedia.org/wikipedia/en/1/10/The_Greatest_Showman_poster.png"},
            {"제목": "판의 미로: 오필리아와 세 개의 열쇠 (2006)", 
             "줄거리": "현실과 환상이 교차하는 소녀의 기묘한 여정.", 
             "이미지": "https://upload.wikimedia.org/wikipedia/en/6/6f/Pans_labyrinth.jpg"}
        ]
    },
    "스릴러 🔪": {
        "책": [
            {"제목": "더 체인", 
             "줄거리": "아이를 구하기 위해 또 다른 아이를 납치해야 하는 부모의 딜레마.", 
             "이미지": "https://images-na.ssl-images-amazon.com/images/I/81d7RkZyJCL.jpg"},
            {"제목": "뒤에 있는 여자", 
             "줄거리": "부부의 은밀한 비밀을 파헤치는 심리 스릴러.", 
             "이미지": "https://images-na.ssl-images-amazon.com/images/I/91zZKXQWv-L.jpg"},
            {"제목": "서브머전스", 
             "줄거리": "사랑과 첩보가 얽힌 긴장감 넘치는 스릴러.", 
             "이미지": "https://m.media-amazon.com/images/I/81OjF0Vv4+L.jpg"},
            {"제목": "아메리칸 사이코 (1991)", 
             "줄거리": "양면적인 삶을 사는 뉴욕 월스트리트 남자의 충격적 이야기.", 
             "이미지": "https://upload.wikimedia.org/wikipedia/en/5/56/American_Psycho.png"}
        ],
        "영화": [
            {"제목": "나를 찾아줘", 
             "줄거리": "실종된 아내, 그리고 드러나는 충격적 진실.", 
             "이미지": "https://upload.wikimedia.org/wikipedia/en/0/05/Gone_Girl_Poster.jpg"},
            {"제목": "룸", 
             "줄거리": "갇혀 있던 공간에서의 모자 탈출과 이후의 삶.", 
             "이미지": "https://upload.wikimedia.org/wikipedia/en/7/70/Room_2015_film_poster.png"},
            {"제목": "기생충", 
             "줄거리": "두 가족의 계급을 넘나드는 블랙코미디 스릴러.", 
             "이미지": "https://upload.wikimedia.org/wikipedia/en/0/0f/Parasite_%282019_film%29.png"},
            {"제목": "세븐 (1995)", 
             "줄거리": "7대 죄악을 모티브로 한 끔찍한 연쇄 살인 사건.", 
             "이미지": "https://upload.wikimedia.org/wikipedia/en/6/68/Seven_%28movie%29_poster.jpg"}
        ]
    },
    "SF 🚀": {
        "책": [
            {"제목": "프로젝트 헤일 메리", 
             "줄거리": "우주에서 인류의 운명을 짊어진 한 남자의 생존기.", 
             "이미지": "https://upload.wikimedia.org/wikipedia/en/7/74/ProjectHailMary.png"},
            {"제목": "세븐 이브스", 
             "줄거리": "지구 종말 이후 살아남기 위한 인류의 방대한 이야기.", 
             "이미지": "https://upload.wikimedia.org/wikipedia/en/1/1f/Seveneves.jpg"},
            {"제목": "아르테미스", 
             "줄거리": "달의 도시에서 벌어지는 범죄와 음모.", 
             "이미지": "https://upload.wikimedia.org/wikipedia/en/4/48/Artemis_book_cover.jpg"},
            {"제목": "스노 크래시 (1992)", 
             "줄거리": "사이버 세계와 현실이 교차하는 초기 메타버스 소설.", 
             "이미지": "https://upload.wikimedia.org/wikipedia/en/c/c5/Snowcrash.jpg"}
        ],
        "영화": [
            {"제목": "듄 (2021)", 
             "줄거리": "사막 행성을 둘러싼 권력과 생존의 이야기.", 
             "이미지": "https://upload.wikimedia.org/wikipedia/en/8/8e/Dune_%282021_film%29.jpg"},
            {"제목": "테넷 (2020)", 
             "줄거리": "시간을 거꾸로 흐르게 하는 비밀 작전.", 
             "이미지": "https://upload.wikimedia.org/wikipedia/en/1/14/Tenet_movie_poster.jpg"},
            {"제목": "에브리씽 에브리웨어 올 앳 원스 (2022)", 
             "줄거리": "멀티버스 속의 평범한 주인공이 펼치는 독창적 SF 모험.", 
             "이미지": "https://upload.wikimedia.org/wikipedia/en/1/1a/Everything_Everywhere_All_at_Once.jpg"},
            {"제목": "매트릭스 (1999)", 
             "줄거리": "가상현실 세계의 혁명적 이야기.", 
             "이미지": "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg"}
        ]
    }
}

# Streamlit UI
st.title("📚🎬 장르 기반 책 & 영화 추천기")

# 장르 선택
genre = st.selectbox("관심 있는 장르를 선택하세요:", list(recommendations.keys()))

# 콘텐츠 타입 선택 (크게 강조)
content_type = st.radio(
    "추천 받고 싶은 콘텐츠를 선택하세요:",
    ["책", "영화"],
    horizontal=True
)

if genre and content_type:
    st.subheader(f"👉 {genre} 장르의 {content_type} 추천 (3개 랜덤)")
    choices = random.sample(recommendations[genre][content_type], 3)
    for idx, choice in enumerate(choices, 1):
        st.markdown(f"### {idx}. {choice['제목']} ✨")
        st.image(choice["이미지"], width=200)
        st.write(f"**줄거리**: {choice['줄거리']}")
        st.markdown("---")


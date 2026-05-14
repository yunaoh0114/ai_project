import streamlit as st

st.set_page_config(
    page_title="✨ MBTI 진로 추천기",
    page_icon="💼",
    layout="centered"
)

# MBTI별 진로 데이터
mbti_jobs = {
    "INTJ": [
        {
            "job": "🧠 데이터 분석가",
            "major": "통계학과, 컴퓨터공학과",
            "personality": "논리적이고 계획적인 사람",
            "salary": "평균 연봉 약 4,500만원"
        },
        {
            "job": "🔬 연구원",
            "major": "생명과학과, 화학과",
            "personality": "탐구심이 많고 집중력이 좋은 사람",
            "salary": "평균 연봉 약 5,000만원"
        }
    ],

    "INTP": [
        {
            "job": "💻 프로그래머",
            "major": "소프트웨어학과, 컴퓨터공학과",
            "personality": "호기심 많고 창의적인 사람",
            "salary": "평균 연봉 약 4,800만원"
        },
        {
            "job": "📚 교수",
            "major": "교육학과, 전공 관련 학과",
            "personality": "분석적이고 지식을 좋아하는 사람",
            "salary": "평균 연봉 약 6,000만원"
        }
    ],

    "ENTJ": [
        {
            "job": "🏢 기업 CEO",
            "major": "경영학과",
            "personality": "리더십이 강하고 추진력 있는 사람",
            "salary": "평균 연봉 약 7,000만원 이상"
        },
        {
            "job": "📈 마케팅 기획자",
            "major": "광고홍보학과, 경영학과",
            "personality": "도전적이고 아이디어가 많은 사람",
            "salary": "평균 연봉 약 4,500만원"
        }
    ],

    "ENTP": [
        {
            "job": "🎤 콘텐츠 크리에이터",
            "major": "미디어학과, 영상학과",
            "personality": "말재주 좋고 아이디어가 풍부한 사람",
            "salary": "평균 연봉 편차 큼 (약 3,000~1억원 이상)"
        },
        {
            "job": "🚀 스타트업 창업가",
            "major": "경영학과",
            "personality": "도전을 즐기고 창의적인 사람",
            "salary": "수익 편차 큼"
        }
    ],

    "INFJ": [
        {
            "job": "💖 상담사",
            "major": "심리학과",
            "personality": "공감 능력이 뛰어난 사람",
            "salary": "평균 연봉 약 3,500만원"
        },
        {
            "job": "✍️ 작가",
            "major": "문예창작과",
            "personality": "감수성이 풍부한 사람",
            "salary": "수입 편차 큼"
        }
    ],

    "INFP": [
        {
            "job": "🎨 일러스트레이터",
            "major": "디자인학과",
            "personality": "상상력이 풍부한 사람",
            "salary": "평균 연봉 약 3,000만원"
        },
        {
            "job": "📖 웹소설 작가",
            "major": "문예창작과",
            "personality": "감성적이고 창의적인 사람",
            "salary": "수익 편차 큼"
        }
    ],

    "ENFJ": [
        {
            "job": "👩‍🏫 교사",
            "major": "교육학과",
            "personality": "사람들을 잘 이끄는 사람",
            "salary": "평균 연봉 약 5,000만원"
        },
        {
            "job": "🤝 인사담당자",
            "major": "경영학과",
            "personality": "소통 능력이 좋은 사람",
            "salary": "평균 연봉 약 4,200만원"
        }
    ],

    "ENFP": [
        {
            "job": "🎬 방송 PD",
            "major": "신문방송학과",
            "personality": "활발하고 창의적인 사람",
            "salary": "평균 연봉 약 5,000만원"
        },
        {
            "job": "📱 SNS 마케터",
            "major": "광고홍보학과",
            "personality": "트렌드에 민감한 사람",
            "salary": "평균 연봉 약 4,000만원"
        }
    ],

    "ISTJ": [
        {
            "job": "📊 회계사",
            "major": "회계학과",
            "personality": "꼼꼼하고 책임감 있는 사람",
            "salary": "평균 연봉 약 6,000만원"
        },
        {
            "job": "🏛️ 공무원",
            "major": "행정학과",
            "personality": "성실하고 체계적인 사람",
            "salary": "평균 연봉 약 4,000만원"
        }
    ],

    "ISFJ": [
        {
            "job": "🏥 간호사",
            "major": "간호학과",
            "personality": "배려심이 깊은 사람",
            "salary": "평균 연봉 약 4,500만원"
        },
        {
            "job": "👶 유치원 교사",
            "major": "유아교육과",
            "personality": "따뜻하고 인내심 있는 사람",
            "salary": "평균 연봉 약 3,500만원"
        }
    ],

    "ESTJ": [
        {
            "job": "⚖️ 경찰관",
            "major": "경찰행정학과",
            "personality": "책임감과 리더십이 강한 사람",
            "salary": "평균 연봉 약 5,000만원"
        },
        {
            "job": "🏢 관리자",
            "major": "경영학과",
            "personality": "체계적이고 추진력 있는 사람",
            "salary": "평균 연봉 약 5,500만원"
        }
    ],

    "ESFJ": [
        {
            "job": "🩺 의료 코디네이터",
            "major": "보건행정학과",
            "personality": "친절하고 소통을 잘하는 사람",
            "salary": "평균 연봉 약 3,800만원"
        },
        {
            "job": "🎉 이벤트 플래너",
            "major": "관광경영학과",
            "personality": "사교적이고 밝은 사람",
            "salary": "평균 연봉 약 4,000만원"
        }
    ],

    "ISTP": [
        {
            "job": "🔧 자동차 정비사",
            "major": "자동차공학과",
            "personality": "손재주가 좋고 현실적인 사람",
            "salary": "평균 연봉 약 4,000만원"
        },
        {
            "job": "✈️ 파일럿",
            "major": "항공운항학과",
            "personality": "침착하고 판단력이 좋은 사람",
            "salary": "평균 연봉 약 7,000만원"
        }
    ],

    "ISFP": [
        {
            "job": "💄 메이크업 아티스트",
            "major": "뷰티미용학과",
            "personality": "감각적이고 섬세한 사람",
            "salary": "평균 연봉 약 3,500만원"
        },
        {
            "job": "📷 사진작가",
            "major": "사진영상학과",
            "personality": "예술 감각이 뛰어난 사람",
            "salary": "수익 편차 큼"
        }
    ],

    "ESTP": [
        {
            "job": "💼 영업 전문가",
            "major": "경영학과",
            "personality": "활동적이고 자신감 있는 사람",
            "salary": "평균 연봉 약 5,000만원"
        },
        {
            "job": "🏋️ 스포츠 트레이너",
            "major": "체육학과",
            "personality": "에너지가 넘치는 사람",
            "salary": "평균 연봉 약 3,500만원"
        }
    ],

    "ESFP": [
        {
            "job": "🎵 가수",
            "major": "실용음악과",
            "personality": "끼가 많고 밝은 사람",
            "salary": "수익 편차 큼"
        },
        {
            "job": "🎥 배우",
            "major": "연극영화과",
            "personality": "표현력이 뛰어난 사람",
            "salary": "수익 편차 큼"
        }
    ]
}

# 제목
st.title("✨ MBTI 진로 추천기")
st.write("💖 나의 MBTI에 어울리는 직업을 알아보자!")

# MBTI 선택
selected_mbti = st.selectbox(
    "🧐 MBTI를 선택해줘!",
    list(mbti_jobs.keys())
)

# 결과 출력
if selected_mbti:
    st.success(f"🎉 {selected_mbti} 유형에게 추천하는 진로야!")

    jobs = mbti_jobs[selected_mbti]

    for idx, job in enumerate(jobs, start=1):
        st.markdown(f"---")
        st.subheader(f"{idx}. {job['job']}")

        st.write(f"📚 **추천 학과** : {job['major']}")
        st.write(f"💡 **잘 어울리는 성격** : {job['personality']}")
        st.write(f"💰 **평균 연봉** : {job['salary']}")

    st.markdown("---")
    st.info("🌟 진로는 참고용이야! 가장 중요한 건 네가 좋아하는 일을 찾는 거야 😎")

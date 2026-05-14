import streamlit as st

st.set_page_config(
    page_title="💘 MBTI 연애 궁합 추천기",
    page_icon="💕",
    layout="centered"
)

# MBTI 궁합 데이터
mbti_love = {
    "INTJ": [
        {
            "type": "ENFP 💖",
            "love_style": "서로 다른 매력에 끌리는 설레는 연애",
            "personality": "밝고 자유로운 사람",
            "breakup": "감정 표현 부족 때문에 서운함이 쌓일 수 있음 😢"
        },
        {
            "type": "ENTP ⚡",
            "love_style": "대화가 끊이지 않는 재밌는 연애",
            "personality": "아이디어 많고 유쾌한 사람",
            "breakup": "둘 다 고집 세서 자주 부딪힐 수 있음 💥"
        }
    ],

    "INTP": [
        {
            "type": "ENTJ 💼",
            "love_style": "서로 성장하게 만드는 연애",
            "personality": "목표가 뚜렷한 사람",
            "breakup": "감정 표현 차이로 거리감이 생길 수 있음 🥲"
        },
        {
            "type": "ENFJ 🌸",
            "love_style": "배려 가득한 따뜻한 연애",
            "personality": "공감 능력이 좋은 사람",
            "breakup": "한쪽이 너무 맞춰주다 지칠 수 있음 😭"
        }
    ],

    "ENTJ": [
        {
            "type": "INFP 🌙",
            "love_style": "서로 부족한 부분을 채워주는 연애",
            "personality": "감성적이고 따뜻한 사람",
            "breakup": "현실적 성향 차이로 갈등 가능 ⚡"
        },
        {
            "type": "INTP 🧠",
            "love_style": "서로 자극을 주는 똑똑한 연애",
            "personality": "논리적인 사람",
            "breakup": "감정 공감 부족으로 멀어질 수 있음 💔"
        }
    ],

    "ENTP": [
        {
            "type": "INFJ ✨",
            "love_style": "설렘과 안정감이 공존하는 연애",
            "personality": "차분하고 이해심 많은 사람",
            "breakup": "자유를 중요하게 생각해 충돌 가능 🌀"
        },
        {
            "type": "INTJ 🔥",
            "love_style": "티키타카 최고인 연애",
            "personality": "똑부러진 사람",
            "breakup": "서로 자기주장이 강할 수 있음 😵"
        }
    ],

    "INFJ": [
        {
            "type": "ENTP 🎉",
            "love_style": "새로운 자극이 가득한 연애",
            "personality": "재밌고 활발한 사람",
            "breakup": "생활 패턴 차이로 힘들 수 있음 🥹"
        },
        {
            "type": "ENFP 🌈",
            "love_style": "감정 교류가 깊은 연애",
            "personality": "감정 표현 잘하는 사람",
            "breakup": "생각이 많아 오해가 쌓일 수 있음 💭"
        }
    ],

    "INFP": [
        {
            "type": "ENFJ 💕",
            "love_style": "서로에게 힘이 되는 연애",
            "personality": "다정하고 배려심 있는 사람",
            "breakup": "현실 문제에서 부딪힐 수 있음 😥"
        },
        {
            "type": "ENTJ 🚀",
            "love_style": "서로 다른 매력이 끌리는 연애",
            "personality": "리더십 있는 사람",
            "breakup": "감정 이해 부족으로 서운할 수 있음 💔"
        }
    ],

    "ENFJ": [
        {
            "type": "INFP 🌷",
            "love_style": "로맨틱하고 감성적인 연애",
            "personality": "순수하고 따뜻한 사람",
            "breakup": "한쪽이 너무 희생할 수 있음 🥲"
        },
        {
            "type": "ISFP 🎨",
            "love_style": "편안하고 안정적인 연애",
            "personality": "부드럽고 감각적인 사람",
            "breakup": "표현 방식 차이로 오해 가능 😭"
        }
    ],

    "ENFP": [
        {
            "type": "INFJ 🌟",
            "love_style": "설렘 가득한 영화 같은 연애",
            "personality": "차분하지만 속 깊은 사람",
            "breakup": "감정 기복 때문에 힘들 수 있음 🌧️"
        },
        {
            "type": "INTJ 🖤",
            "love_style": "정반대라 더 끌리는 연애",
            "personality": "계획적이고 냉철한 사람",
            "breakup": "자유 vs 계획 차이로 갈등 가능 ⚔️"
        }
    ],

    "ISTJ": [
        {
            "type": "ESFP 🎵",
            "love_style": "안정감과 즐거움이 공존하는 연애",
            "personality": "밝고 긍정적인 사람",
            "breakup": "생활 방식 차이 가능 😵"
        },
        {
            "type": "ESTP ⚡",
            "love_style": "현실적이고 든든한 연애",
            "personality": "행동력 강한 사람",
            "breakup": "고집 때문에 싸울 수 있음 💥"
        }
    ],

    "ISFJ": [
        {
            "type": "ESFP 💃",
            "love_style": "웃음 많은 행복한 연애",
            "personality": "활발하고 사교적인 사람",
            "breakup": "관심 표현 차이로 서운할 수 있음 😢"
        },
        {
            "type": "ESTP 🏍️",
            "love_style": "설레고 액티브한 연애",
            "personality": "도전적인 사람",
            "breakup": "안정성 차이로 갈등 가능 🥲"
        }
    ],

    "ESTJ": [
        {
            "type": "ISFP 🎨",
            "love_style": "서로 부족한 부분을 채워주는 연애",
            "personality": "감성적이고 차분한 사람",
            "breakup": "감정 표현 방식 차이 😭"
        },
        {
            "type": "ISTP 🔧",
            "love_style": "쿨하고 현실적인 연애",
            "personality": "독립적인 사람",
            "breakup": "무뚝뚝함 때문에 거리감 가능 🧊"
        }
    ],

    "ESFJ": [
        {
            "type": "ISFP 🌸",
            "love_style": "다정하고 안정적인 연애",
            "personality": "배려심 깊은 사람",
            "breakup": "지나친 간섭으로 힘들 수 있음 😥"
        },
        {
            "type": "ISTP 🚗",
            "love_style": "서로 다른 매력에 끌리는 연애",
            "personality": "쿨하고 자유로운 사람",
            "breakup": "표현 부족으로 오해 가능 💔"
        }
    ],

    "ISTP": [
        {
            "type": "ESFJ ☀️",
            "love_style": "밝고 편안한 연애",
            "personality": "사람 챙기는 걸 좋아하는 사람",
            "breakup": "감정 표현 차이 🥹"
        },
        {
            "type": "ESTJ 📚",
            "love_style": "현실적이고 안정적인 연애",
            "personality": "계획적인 사람",
            "breakup": "자유를 원하는 성향 충돌 ⚡"
        }
    ],

    "ISFP": [
        {
            "type": "ENFJ 💞",
            "love_style": "따뜻하고 로맨틱한 연애",
            "personality": "배려심 넘치는 사람",
            "breakup": "감정 기복 차이 가능 🌧️"
        },
        {
            "type": "ESFJ 🌼",
            "love_style": "편안하고 행복한 연애",
            "personality": "다정한 사람",
            "breakup": "의존도가 높아질 수 있음 😭"
        }
    ],

    "ESTP": [
        {
            "type": "ISFJ 🫶",
            "love_style": "설렘과 안정감이 있는 연애",
            "personality": "따뜻하고 성실한 사람",
            "breakup": "자유로운 성향 차이 😵"
        },
        {
            "type": "ISTJ 📖",
            "love_style": "현실적이고 오래가는 연애",
            "personality": "믿음직한 사람",
            "breakup": "답답함을 느낄 수 있음 💭"
        }
    ],

    "ESFP": [
        {
            "type": "ISFJ 💗",
            "love_style": "행복 바이러스 같은 연애",
            "personality": "다정하고 배려심 있는 사람",
            "breakup": "생활 스타일 차이 🥲"
        },
        {
            "type": "ISTJ 🧩",
            "love_style": "서로 다른 매력이 재밌는 연애",
            "personality": "차분하고 성실한 사람",
            "breakup": "감정 표현 부족 가능 😢"
        }
    ]
}

# 제목
st.title("💘 MBTI 연애 궁합 추천기")
st.write("✨ 내 MBTI랑 잘 맞는 연애 상대를 알아보자!")

# MBTI 선택
selected_mbti = st.selectbox(
    "🧐 너의 MBTI를 골라줘!",
    list(mbti_love.keys())
)

# 결과 출력
if selected_mbti:
    st.success(f"💖 {selected_mbti} 유형과 잘 맞는 연애 상대야!")

    matches = mbti_love[selected_mbti]

    for idx, match in enumerate(matches, start=1):
        st.markdown("---")
        st.subheader(f"{idx}. {match['type']}")

        st.write(f"💕 **잘 맞는 연애 스타일** : {match['love_style']}")
        st.write(f"😎 **잘 어울리는 성격** : {match['personality']}")
        st.write(f"💔 **헤어질 수 있는 이유** : {match['breakup']}")

    st.markdown("---")
    st.info("🌈 MBTI는 재미로 보는 거야! 가장 중요한 건 서로를 존중하는 마음 💕")

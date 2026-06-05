import streamlit as st
import pandas as pd
import pydeck as pdk
import random

# --------------------------------------------------
# 페이지 설정
# --------------------------------------------------

st.set_page_config(
    page_title="🍜 오늘 뭐 먹지?",
    page_icon="🍔",
    layout="wide"
)

# --------------------------------------------------
# 제목
# --------------------------------------------------

st.title("🍜 오늘 뭐 먹지?")
st.caption("🚇 지하철역 기준 음식 & 맛집 추천 서비스")

# --------------------------------------------------
# 음식 50개
# --------------------------------------------------

foods = [
    "삼겹살","목살","갈비","불고기","제육볶음",
    "김치찌개","된장찌개","순두부찌개","부대찌개","감자탕",
    "설렁탕","갈비탕","육개장","국밥","해장국",
    "냉면","비빔냉면","막국수","칼국수","잔치국수",
    "쌀국수","우동","라멘","초밥","회덮밥",
    "돈까스","카레","오므라이스","함박스테이크","파스타",
    "리조또","피자","햄버거","샌드위치","브런치",
    "짜장면","짬뽕","탕수육","마라탕","마라샹궈",
    "양꼬치","훠궈","닭갈비","찜닭","족발",
    "보쌈","곱창","막창","떡볶이","순대"
]

# --------------------------------------------------
# 맛집 데이터
# --------------------------------------------------

restaurants = {
    "한식": [
        ("청춘국밥", "든든한 국밥 맛집"),
        ("서울밥상", "집밥 느낌 가득"),
        ("삼겹천국", "고기 좋아하면 필수"),
        ("김치명가", "김치찌개 전문"),
        ("할머니식당", "정겨운 백반집")
    ],

    "중식": [
        ("황금반점", "정통 중화요리"),
        ("홍콩짬뽕", "얼큰한 국물 맛집"),
        ("마라월드", "매운맛 성지"),
        ("용궁반점", "가성비 최고"),
        ("북경성", "탕수육 인기")
    ],

    "일식": [
        ("스시하루", "신선한 초밥"),
        ("라멘공방", "돈코츠 라멘 전문"),
        ("사쿠라", "일본 가정식"),
        ("우동팩토리", "수타 우동"),
        ("돈카츠클럽", "바삭한 돈까스")
    ],

    "양식": [
        ("파스타랩", "크림파스타 인기"),
        ("버거클럽", "수제버거 맛집"),
        ("브런치팩토리", "감성 브런치"),
        ("스테이크하우스", "프리미엄 스테이크"),
        ("피자스퀘어", "화덕피자 전문")
    ]
}

# --------------------------------------------------
# 예시 역
# --------------------------------------------------

popular_stations = [
    "강남역",
    "잠실역",
    "홍대입구역",
    "서울역",
    "신촌역",
    "건대입구역",
    "사당역",
    "왕십리역",
    "종로3가역",
    "을지로입구역"
]

# --------------------------------------------------
# 지하철역 입력
# --------------------------------------------------

station = st.text_input(
    "🚇 현재 가장 가까운 지하철역을 입력해줘!",
    placeholder="예: 강남역"
)

with st.expander("📍 예시 지하철역 보기"):
    st.write(", ".join(popular_stations))

# --------------------------------------------------
# 실행
# --------------------------------------------------

if station:

    st.success(f"🎉 {station} 주변 음식 추천!")

    cols = st.columns(5)

    for idx, food in enumerate(foods):
        cols[idx % 5].write(f"🍽️ {food}")

    st.divider()

    st.info("🤔 아직 못 고르겠다면 종류를 선택해보자!")

    category = st.radio(
        "🍴 어떤 종류가 땡겨?",
        ["한식", "중식", "일식", "양식"],
        horizontal=True
    )

    st.divider()

    st.subheader(f"⭐ {station} 주변 추천 {category} 맛집 TOP5")

    map_data = []

    # 현재 위치(역)
    station_lat = 37.4979
    station_lon = 127.0276

    map_data.append({
        "name": f"{station} (현재 위치)",
        "lat": station_lat,
        "lon": station_lon,
        "color": [255, 0, 0]
    })

    for rank, (name, desc) in enumerate(restaurants[category], start=1):

        distance = round(random.uniform(0.3, 2.5), 1)

        walk_time = max(3, int(distance * 12))

        transit_time = max(2, int(distance * 4))

        rating = round(random.uniform(4.1, 4.9), 1)

        st.markdown("---")

        st.markdown(f"### 🏆 {rank}위 | {name}")

        st.write(f"💬 {desc}")
        st.write(f"📏 예상 거리 : {distance} km")
        st.write(f"🚶 도보 약 {walk_time}분")
        st.write(f"🚌 대중교통 약 {transit_time}분")
        st.write(f"⭐ 만족도 : {rating}/5.0")

        lat_offset = random.uniform(-0.01, 0.01)
        lon_offset = random.uniform(-0.01, 0.01)

        map_data.append({
            "name": f"{rank}위 {name}",
            "lat": station_lat + lat_offset,
            "lon": station_lon + lon_offset,
            "color": [0, 0, 255]
        })

    st.divider()

    st.subheader("🗺️ 맛집 위치 지도")

    df = pd.DataFrame(map_data)

    layer = pdk.Layer(
        "ScatterplotLayer",
        data=df,
        get_position=["lon", "lat"],
        get_fill_color="color",
        get_radius=120,
        pickable=True
    )

    view_state = pdk.ViewState(
        latitude=station_lat,
        longitude=station_lon,
        zoom=14,
        pitch=0
    )

    deck = pdk.Deck(
        layers=[layer],
        initial_view_state=view_state,
        tooltip={
            "text": "{name}"
        }
    )

    st.pydeck_chart(deck)

# --------------------------------------------------
# 하단
# --------------------------------------------------

st.divider()

st.markdown("""
### 🎯 사용 방법

1. 🚇 현재 가까운 지하철역 입력
2. 🍜 음식 추천 확인
3. 🤔 음식 종류 선택
4. ⭐ 맛집 TOP5 확인
5. 🗺️ 지도 확인
6. 😋 맛있게 먹기

오늘도 행복한 식사 되세요! 🍔🍕🍜🍣
""")

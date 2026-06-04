import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
from pathlib import Path

# ------------------------------------------------
# 페이지 설정
# ------------------------------------------------

st.set_page_config(
    page_title="🍜 오늘 뭐 먹지?",
    page_icon="🍔",
    layout="wide"
)

# ------------------------------------------------
# 제목
# ------------------------------------------------

st.title("🍜 오늘 뭐 먹지?")
st.caption("🚇 지하철역 기준 서울 맛집 추천 서비스")

# ------------------------------------------------
# CSV 불러오기
# ------------------------------------------------

@st.cache_data
def load_data():

    current_dir = Path(__file__).parent
    root_dir = current_dir.parent

    csv_path = root_dir / "서울시 관광 음식(1).csv"

    if not csv_path.exists():
        st.error("❌ 서울시 관광 음식(1).csv 파일을 찾을 수 없습니다.")
        st.stop()

    encodings = [
        "cp949",
        "euc-kr",
        "utf-8",
        "utf-8-sig",
        "latin1"
    ]

    for enc in encodings:
        try:
            df = pd.read_csv(csv_path, encoding=enc)
            return df
        except Exception:
            continue

    st.error("❌ CSV 파일을 읽을 수 없습니다.")
    st.stop()

df = load_data()

# ------------------------------------------------
# 음식 추천 50가지
# ------------------------------------------------

foods = [
    "삼겹살","갈비","불고기","김치찌개","된장찌개",
    "순두부찌개","감자탕","냉면","비빔밥","국밥",
    "족발","보쌈","곱창","닭갈비","치킨",
    "파스타","스테이크","햄버거","피자","초밥",
    "라멘","우동","돈까스","짜장면","짬뽕",
    "탕수육","마라탕","훠궈","쌀국수","샤브샤브",
    "카레","오므라이스","김밥","떡볶이","순대",
    "설렁탕","갈비탕","육개장","아귀찜","낙곱새",
    "쭈꾸미볶음","오징어볶음","양꼬치","브런치",
    "샌드위치","닭한마리","한우구이","막창",
    "해장국","쌀국수"
]

# ------------------------------------------------
# 지하철역 입력
# ------------------------------------------------

station = st.text_input(
    "🚇 현재 가장 가까운 지하철역을 입력하세요",
    placeholder="예: 강남역"
)

if station:

    st.success(f"🎉 {station} 주변 맛집을 찾아봤어요!")

    # ------------------------------------------------
    # 음식 추천
    # ------------------------------------------------

    st.subheader("🍽️ 오늘의 음식 추천 50가지")

    cols = st.columns(5)

    for idx, food in enumerate(foods):
        cols[idx % 5].write(f"🍜 {food}")

    st.divider()

    # ------------------------------------------------
    # 데이터 확인
    # ------------------------------------------------

    if "교통정보" not in df.columns:
        st.error("❌ 교통정보 컬럼을 찾을 수 없습니다.")
        st.write(df.columns.tolist())
        st.stop()

    # ------------------------------------------------
    # 맛집 검색
    # ------------------------------------------------

    result = df[
        df["교통정보"]
        .astype(str)
        .str.contains(
            station,
            case=False,
            na=False
        )
    ]

    if len(result) == 0:

        st.warning(
            "😢 해당 역 주변 맛집 정보를 찾지 못했어요."
        )

    else:

        top5 = result.head(5)

        st.subheader(
            f"🏆 {station} 주변 추천 맛집 TOP5"
        )

        for rank, (_, row) in enumerate(
            top5.iterrows(),
            start=1
        ):

            st.markdown("---")

            st.markdown(
                f"## 🏆 {rank}위 {row['상호명']}"
            )

            st.write(
                f"🍽️ 대표메뉴 : {row['대표메뉴']}"
            )

            st.write(
                f"📍 주소 : {row['신주소']}"
            )

            st.write(
                f"☎️ 전화번호 : {row['전화번호']}"
            )

            st.write(
                f"🚇 교통정보 : {row['교통정보']}"
            )

            if "운영시간" in df.columns:
                st.write(
                    f"🕒 운영시간 : {row['운영시간']}"
                )

        # ------------------------------------------------
        # 지도
        # ------------------------------------------------

        st.divider()

        st.subheader("🗺️ 맛집 지도")

        # 강남역 기준 예시 좌표
        station_lat = 37.4979
        station_lon = 127.0276

        m = folium.Map(
            location=[
                station_lat,
                station_lon
            ],
            zoom_start=15
        )

        # 현재 위치
        folium.Marker(
            [station_lat, station_lon],
            popup=f"🚇 {station}",
            tooltip="현재 위치",
            icon=folium.Icon(color="red")
        ).add_to(m)

        # 추천 맛집 1~5 표시
        for i in range(min(5, len(top5))):

            lat = station_lat + (i * 0.002)
            lon = station_lon + (i * 0.002)

            folium.CircleMarker(
                location=[lat, lon],
                radius=6,
                popup=f"{i+1}위",
                tooltip=f"{i+1}위 맛집",
                color="blue",
                fill=True
            ).add_to(m)

        st_folium(
            m,
            height=600,
            width=None
        )

# ------------------------------------------------
# 하단 안내
# ------------------------------------------------

st.divider()

st.markdown("""
### 🎯 사용 방법

1️⃣ 지하철역 입력

2️⃣ 음식 추천 확인

3️⃣ 맛집 TOP5 확인

4️⃣ 지도 확인

5️⃣ 맛있게 먹기 😋

즐거운 식사 되세요! 🍜🍕🍔
""")

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
st.caption("🚇 지하철역 기준 맛집 추천 서비스")

# ------------------------------------------------
# CSV 확인
# ------------------------------------------------

st.subheader("📂 CSV 파일 확인")

current_dir = Path(__file__).parent
root_dir = current_dir.parent

st.write("현재 폴더:", current_dir)

st.write("현재 폴더 파일")

for f in current_dir.iterdir():
    st.write("📄", f.name)

st.write("---")

st.write("프로젝트 루트 파일")

for f in root_dir.iterdir():
    st.write("📄", f.name)

# ------------------------------------------------
# 음식 추천
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

station = st.text_input(
    "🚇 가까운 지하철역을 입력하세요",
    placeholder="예: 강남역"
)

if station:

    st.success(f"🎉 {station} 주변 추천!")

    st.subheader("🍽️ 추천 음식")

    cols = st.columns(5)

    for idx, food in enumerate(foods):
        cols[idx % 5].write(f"🍜 {food}")

    st.divider()

    st.subheader("🗺️ 예시 지도")

    station_lat = 37.4979
    station_lon = 127.0276

    m = folium.Map(
        location=[station_lat, station_lon],
        zoom_start=15
    )

    folium.Marker(
        [station_lat, station_lon],
        popup=station,
        tooltip="현재 위치",
        icon=folium.Icon(color="red")
    ).add_to(m)

    st_folium(
        m,
        height=500,
        width=None
    )

st.divider()

st.info(
    "CSV 파일 이름 확인 후 알려주세요."
)

# app.py
import streamlit as st
import folium
from streamlit_folium import st_folium

st.set_page_config(
    page_title="서울 인기 관광지 TOP 10",
    page_icon="🗺️",
    layout="wide"
)

st.title("🌏 외국인들이 좋아하는 서울 관광지 TOP 10")
st.markdown("폴리움(Folium) 지도로 서울의 인기 관광지를 확인해보세요!")

# 관광지 데이터
places = [
    {
        "name": "경복궁",
        "lat": 37.579617,
        "lon": 126.977041,
        "desc": "조선 시대의 대표 궁궐 👑"
    },
    {
        "name": "명동",
        "lat": 37.563757,
        "lon": 126.985302,
        "desc": "쇼핑과 길거리 음식의 천국 🛍️"
    },
    {
        "name": "남산서울타워",
        "lat": 37.551169,
        "lon": 126.988227,
        "desc": "서울 야경 명소 🌃"
    },
    {
        "name": "북촌한옥마을",
        "lat": 37.582604,
        "lon": 126.983998,
        "desc": "전통 한옥 감성 🏡"
    },
    {
        "name": "홍대거리",
        "lat": 37.556354,
        "lon": 126.922019,
        "desc": "젊음과 버스킹의 거리 🎵"
    },
    {
        "name": "롯데월드타워",
        "lat": 37.513068,
        "lon": 127.102676,
        "desc": "서울의 초고층 랜드마크 🏙️"
    },
    {
        "name": "동대문디자인플라자(DDP)",
        "lat": 37.566526,
        "lon": 127.009223,
        "desc": "미래적인 건축물 ✨"
    },
    {
        "name": "인사동",
        "lat": 37.574187,
        "lon": 126.984952,
        "desc": "전통 문화와 기념품 🎎"
    },
    {
        "name": "한강공원",
        "lat": 37.528316,
        "lon": 126.932598,
        "desc": "치킨과 라면의 성지 🍗"
    },
    {
        "name": "코엑스",
        "lat": 37.512524,
        "lon": 127.058819,
        "desc": "쇼핑과 별마당도서관 📚"
    }
]

# 서울 중심 지도 생성
m = folium.Map(
    location=[37.5665, 126.9780],
    zoom_start=11,
    tiles="CartoDB positron"
)

# 마커 추가
for place in places:
    folium.Marker(
        location=[place["lat"], place["lon"]],
        popup=f"""
        <b>{place['name']}</b><br>
        {place['desc']}
        """,
        tooltip=place["name"],
        icon=folium.Icon(color="red", icon="info-sign")
    ).add_to(m)

# 지도 출력
st_folium(m, width=1200, height=700)

# 관광지 목록 출력
st.subheader("📍 관광지 리스트")

for i, place in enumerate(places, start=1):
    st.markdown(f"""
    ### {i}. {place['name']}
    - {place['desc']}
    """)

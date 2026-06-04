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

@st.cache_data
def load_data():

    root_dir = Path(__file__).resolve().parent.parent

    csv_files = list(root_dir.glob("*.csv"))

    if len(csv_files) == 0:
        st.error("❌ 프로젝트 폴더에 CSV 파일이 없습니다.")
        st.write("현재 폴더:", root_dir)

        st.write("파일 목록")
        for f in root_dir.iterdir():
            st.write(f.name)

        st.stop()

    csv_path = csv_files[0]

    st.success(f"CSV 발견: {csv_path.name}")

    encodings = [
        "cp949",
        "euc-kr",
        "utf-8",
        "utf-8-sig"
    ]

    for enc in encodings:
        try:
            return pd.read_csv(csv_path, encoding=enc)
        except:
            pass

    st.error("CSV 읽기 실패")
    st.stop()

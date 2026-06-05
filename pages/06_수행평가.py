import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(
    page_title="🍜 오늘 뭐 먹지?",
    page_icon="🍔",
    layout="wide"
)

st.title("🍜 오늘 뭐 먹지?")
st.caption("🚇 지하철역 기준 맛집 추천")

@st.cache_data
def load_data():

    root_dir = Path(__file__).resolve().parent.parent

    st.write("현재 폴더:", root_dir)

    st.write("파일 목록")

    for f in root_dir.iterdir():
        st.write(f.name)

    csv_path = root_dir / "seoul_food.csv"

    st.write("찾는 파일:", csv_path)

    if not csv_path.exists():
        st.error("❌ seoul_food.csv 없음")
        st.stop()

    try:
        df = pd.read_csv(csv_path)
        return df

    except Exception as e:
        st.error(str(e))
        st.stop()

df = load_data()

st.success("CSV 로딩 성공!")

st.write("컬럼 목록")
st.write(df.columns.tolist())

station = st.text_input("🚇 역 이름 입력")

if station:
    st.write(f"입력한 역: {station}")

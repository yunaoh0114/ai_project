import streamlit as st
import pandas as pd
from pathlib import Path

# ------------------------------------------------
# 페이지 설정
# ------------------------------------------------

st.set_page_config(
    page_title="🍜 오늘 뭐 먹지?",
    page_icon="🍔",
    layout="wide"
)

st.title("🍜 오늘 뭐 먹지?")
st.caption("🚇 지하철역 기준 서울 맛집 추천 서비스")

# ------------------------------------------------
# CSV 불러오기
# ------------------------------------------------

@st.cache_data
def load_data():

    root_dir = Path(__file__).resolve().parent.parent

    csv_path = root_dir / "seoul_food.csv"

    if not csv_path.exists():
        st.error("❌ seoul_food.csv 파일을 찾을 수 없습니다.")
        st.stop()

    encodings = [
        "cp949",
        "euc-kr",
        "utf-8",
        "utf-8-sig"
    ]

    for enc in encodings:
        try:
            df = pd.read_csv(csv_path, encoding=enc)

            # 컬럼명 공백 제거
            df.columns = df.columns.str.strip()

            return df

        except Exception:
            pass

    st.error("❌ CSV 파일을 읽을 수 없습니다.")
    st.stop()

df = load_data()

# ------------------------------------------------
# 디버그용 컬럼 확인
# ------------------------------------------------

st.subheader("📋 CSV 컬럼 확인")

st.write(df.columns.tolist())

# ------------------------------------------------
# 역 입력
# ------------------------------------------------

station = st.text_input(
    "🚇 지하철역 입력",
    placeholder="예: 강남역"
)

if station:

    if "교통정보" not in df.columns:

        st.error("❌ CSV에 '교통정보' 컬럼이 없습니다.")

        st.write("현재 컬럼")
        st.write(df.columns.tolist())

        st.stop()

    result = df[
        df["교통정보"]
        .astype(str)
        .str.contains(
            station,
            case=False,
            na=False
        )
    ]

    st.success(
        f"검색 결과 {len(result)}개"
    )

    if len(result) > 0:

        show_cols = []

        for col in [
            "상호명",
            "대표메뉴",
            "신주소",
            "전화번호",
            "교통정보"
        ]:
            if col in result.columns:
                show_cols.append(col)

        st.dataframe(
            result[show_cols].head(10),
            use_container_width=True
        )

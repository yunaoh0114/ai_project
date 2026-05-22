import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import platform

# -----------------------------
# 한글 폰트 설정
# -----------------------------
system_name = platform.system()

if system_name == "Windows":
    plt.rc("font", family="Malgun Gothic")
elif system_name == "Darwin":
    plt.rc("font", family="AppleGothic")
else:
    # Streamlit Cloud(Linux)
    plt.rc("font", family="NanumGothic")

plt.rcParams["axes.unicode_minus"] = False

# -----------------------------
# 샘플 데이터
# -----------------------------
data = {
    "수원시": [12000, 15000, 22000, 28000, 31000, 29000, 25000, 18000],
    "성남시": [10000, 14000, 21000, 26000, 30000, 27000, 23000, 16000],
    "고양시": [9000, 13000, 20000, 24000, 28000, 25000, 21000, 15000],
    "용인시": [11000, 14500, 21500, 27000, 32000, 30000, 26000, 19000]
}

age_groups = [
    "0~9세",
    "10~19세",
    "20~29세",
    "30~39세",
    "40~49세",
    "50~59세",
    "60~69세",
    "70세 이상"
]

df = pd.DataFrame(data, index=age_groups)

# -----------------------------
# Streamlit UI
# -----------------------------
st.title("경기도 인구통계 대시보드")

district = st.selectbox(
    "행정구를 선택하세요",
    df.columns
)

# -----------------------------
# 그래프 생성
# -----------------------------
fig, ax = plt.subplots(figsize=(10, 5))

# 그래프 바탕색
fig.patch.set_facecolor("#FFF9DB")
ax.set_facecolor("#FFF9DB")

# 꺾은선 그래프
ax.plot(
    age_groups,
    df[district],
    color="#D35400",
    marker="o",
    linewidth=3
)

# 제목 및 라벨
ax.set_title(
    "경기도의 인구통계",
    fontsize=18,
    fontweight="bold"
)

ax.set_xlabel("연령대", fontsize=12)
ax.set_ylabel("인구수", fontsize=12)

# 격자
ax.grid(True, linestyle="--", alpha=0.5)

# Streamlit 출력
st.pyplot(fig)

# app.py

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# ---------------------------------------------------
# 페이지 설정
# ---------------------------------------------------
st.set_page_config(
    page_title="🌍 MBTI 국가 분석기",
    page_icon="🌎",
    layout="wide"
)

# ---------------------------------------------------
# 제목
# ---------------------------------------------------
st.title("🌍 MBTI 유형별 TOP 10 국가 분석")
st.markdown(
    "MBTI 유형을 선택하면 비율이 가장 높은 국가 TOP 10을 인터랙티브 그래프로 보여줘요 ✨"
)

# ---------------------------------------------------
# 데이터 불러오기
# ---------------------------------------------------
@st.cache_data
def load_data():
    return pd.read_csv("countriesMBTI_16types.csv")

df = load_data()

# ---------------------------------------------------
# MBTI 목록
# ---------------------------------------------------
mbti_types = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
]

# ---------------------------------------------------
# MBTI 선택
# ---------------------------------------------------
selected_mbti = st.selectbox(
    "🧠 MBTI 유형 선택",
    mbti_types
)

# ---------------------------------------------------
# TOP 10 국가 추출
# ---------------------------------------------------
top10 = (
    df[["Country", selected_mbti]]
    .sort_values(by=selected_mbti, ascending=False)
    .head(10)
)

# ---------------------------------------------------
# 색상 설정
# 1등 = 빨강
# 나머지 = 파란 그라데이션
# ---------------------------------------------------
blue_gradient = px.colors.sequential.Blues_r

colors = []

for i in range(len(top10)):
    if i == 0:
        colors.append("red")
    else:
        gradient_index = int(
            (i / len(top10)) * (len(blue_gradient) - 1)
        )
        colors.append(blue_gradient[gradient_index])

# ---------------------------------------------------
# Plotly 그래프
# ---------------------------------------------------
fig = go.Figure()

fig.add_trace(
    go.Bar(
        x=top10["Country"],
        y=top10[selected_mbti],
        marker_color=colors,
        text=[
            f"{v*100:.2f}%"
            for v in top10[selected_mbti]
        ],
        textposition="outside",
        hovertemplate=
        "<b>%{x}</b><br>" +
        f"{selected_mbti}: " +
        "%{y:.2%}<extra></extra>"
    )
)

# ---------------------------------------------------
# 그래프 디자인
# ---------------------------------------------------
fig.update_layout(
    title=f"🏆 {selected_mbti} 비율이 높은 국가 TOP 10",
    xaxis_title="국가",
    yaxis_title="비율",
    template="plotly_white",
    height=650,
    hovermode="x unified",
    font=dict(size=16)
)

fig.update_yaxes(
    tickformat=".0%"
)

# ---------------------------------------------------
# 그래프 출력
# ---------------------------------------------------
st.plotly_chart(
    fig,
    use_container_width=True
)

# ---------------------------------------------------
# 1위 국가 표시
# ---------------------------------------------------
first_country = top10.iloc[0]["Country"]
first_ratio = top10.iloc[0][selected_mbti]

st.success(
    f"🥇 {selected_mbti} 비율이 가장 높은 나라는 "
    f"{first_country} "
    f"({first_ratio*100:.2f}%) 입니다!"
)

# ---------------------------------------------------
# 데이터 보기
# ---------------------------------------------------
with st.expander("📋 TOP 10 데이터 보기"):
    st.dataframe(
        top10,
        use_container_width=True
    )

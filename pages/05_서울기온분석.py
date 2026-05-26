# app.py

import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# ---------------------------
# 페이지 설정
# ---------------------------
st.set_page_config(
    page_title="날짜별 기온분석",
    layout="wide"
)

st.title("🌡️ 날짜별 기온분석")

# ---------------------------
# 데이터 불러오기
# ---------------------------
@st.cache_data
def load_data():

    df = pd.read_csv("seoul.csv", encoding="euc-kr")

    # 날짜 변환 오류 방지
    df['날짜'] = pd.to_datetime(
        df['날짜'],
        errors='coerce'
    )

    # 날짜 없는 행 제거
    df = df.dropna(subset=['날짜'])

    # 연/월/일 생성
    df['연도'] = df['날짜'].dt.year
    df['월'] = df['날짜'].dt.month
    df['일'] = df['날짜'].dt.day

    return df

df = load_data()

# ---------------------------
# 월 / 일 선택
# ---------------------------
col1, col2 = st.columns(2)

with col1:
    month = st.selectbox(
        "월 선택",
        sorted(df['월'].unique())
    )

with col2:

    available_days = sorted(
        df[df['월'] == month]['일'].unique()
    )

    day = st.selectbox(
        "일 선택",
        available_days
    )

# ---------------------------
# 데이터 필터링
# ---------------------------
filtered = df[
    (df['월'] == month) &
    (df['일'] == day)
]

filtered = filtered.sort_values('연도')

# ---------------------------
# 그래프 생성
# ---------------------------
fig = go.Figure()

# 최고기온
fig.add_trace(
    go.Scatter(
        x=filtered['연도'],
        y=filtered['최고기온(℃)'],
        mode='lines+markers',
        name='최고기온',
        line=dict(
            color='#FFB6C1',  # 파스텔 핑크
            width=3
        ),
        marker=dict(size=7)
    )
)

# 최저기온
fig.add_trace(
    go.Scatter(
        x=filtered['연도'],
        y=filtered['최저기온(℃)'],
        mode='lines+markers',
        name='최저기온',
        line=dict(
            color='#A7C7E7',  # 파스텔 파랑
            width=3
        ),
        marker=dict(size=7)
    )
)

# ---------------------------
# 그래프 꾸미기
# ---------------------------
fig.update_layout(
    title="날짜별 기온분석",
    xaxis_title="연도",
    yaxis_title="온도(℃)",
    template="plotly_white",
    hovermode='x unified',
    legend_title='범례',
    height=650
)

# ---------------------------
# 그래프 출력
# ---------------------------
st.plotly_chart(
    fig,
    use_container_width=True
)

# ---------------------------
# 데이터 테이블
# ---------------------------
with st.expander("📄 데이터 보기"):
    st.dataframe(
        filtered[
            ['연도', '최고기온(℃)', '최저기온(℃)']
        ],
        use_container_width=True
    )

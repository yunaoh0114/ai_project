# app.py

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from sklearn.linear_model import LinearRegression

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

    df = pd.read_csv(
        "seoul.csv",
        encoding="euc-kr"
    )

    # 날짜 변환
    df['날짜'] = pd.to_datetime(
        df['날짜'],
        errors='coerce'
    )

    # 날짜 오류 제거
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
        "📅 월 선택",
        sorted(df['월'].unique())
    )

with col2:

    available_days = sorted(
        df[df['월'] == month]['일'].unique()
    )

    day = st.selectbox(
        "📅 일 선택",
        available_days
    )

# ---------------------------
# 데이터 필터링
# ---------------------------
filtered = df[
    (df['월'] == month) &
    (df['일'] == day)
]

# 결측치 제거
filtered = filtered.dropna(
    subset=[
        '최고기온(℃)',
        '최저기온(℃)'
    ]
)

filtered = filtered.sort_values('연도')

# ---------------------------
# 미래 연도 선택
# ---------------------------
st.subheader("🔮 미래 기온 예측")

future_year = st.number_input(
    "예측할 미래 연도 입력",
    min_value=int(filtered['연도'].max()) + 1,
    max_value=2100,
    value=2030
)

# ---------------------------
# 머신러닝 예측
# ---------------------------

# 학습 데이터
X = filtered[['연도']].values

# 최고기온
y_max = filtered['최고기온(℃)'].values

# 최저기온
y_min = filtered['최저기온(℃)'].values

# 모델 생성
model_max = LinearRegression()
model_min = LinearRegression()

# 학습
model_max.fit(X, y_max)
model_min.fit(X, y_min)

# 예측
predicted_max = model_max.predict(
    [[future_year]]
)[0]

predicted_min = model_min.predict(
    [[future_year]]
)[0]

# ---------------------------
# 예측 결과 출력
# ---------------------------
col3, col4 = st.columns(2)

with col3:

    st.metric(
        "🌸 예상 최고기온",
        f"{predicted_max:.1f}℃"
    )

with col4:

    st.metric(
        "🩵 예상 최저기온",
        f"{predicted_min:.1f}℃"
    )

# ---------------------------
# 예측 데이터 추가
# ---------------------------
future_df = pd.DataFrame({

    '연도': [future_year],
    '최고기온(℃)': [predicted_max],
    '최저기온(℃)': [predicted_min]

})

plot_df = pd.concat(
    [filtered, future_df],
    ignore_index=True
)

# ---------------------------
# 그래프 생성
# ---------------------------
fig = go.Figure()

# 최고기온 그래프
fig.add_trace(

    go.Scatter(

        x=plot_df['연도'],
        y=plot_df['최고기온(℃)'],

        mode='lines+markers',

        name='최고기온',

        line=dict(
            color='#FFB6C1',
            width=3
        ),

        marker=dict(
            size=8
        ),

        hovertemplate=
        '<b>연도:</b> %{x}<br>' +
        '<b>최고기온:</b> %{y:.1f}℃<extra></extra>'

    )

)

# 최저기온 그래프
fig.add_trace(

    go.Scatter(

        x=plot_df['연도'],
        y=plot_df['최저기온(℃)'],

        mode='lines+markers',

        name='최저기온',

        line=dict(
            color='#A7C7E7',
            width=3
        ),

        marker=dict(
            size=8
        ),

        hovertemplate=
        '<b>연도:</b> %{x}<br>' +
        '<b>최저기온:</b> %{y:.1f}℃<extra></extra>'

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

    height=700

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

        plot_df[
            ['연도', '최고기온(℃)', '최저기온(℃)']
        ],

        use_container_width=True

    )

import streamlit as st
import random

st.set_page_config(
    page_title="🍜 오늘 뭐 먹지?",
    page_icon="🍔",
    layout="wide"
)

st.title("🍜 오늘 뭐 먹지?")
st.subheader("📍 지역별 음식 & 맛집 추천 서비스")

# -------------------------
# 지역별 음식 데이터
# -------------------------

foods = {
    "서울": [
        "김치찌개","된장찌개","불고기","삼겹살","닭갈비",
        "냉면","비빔밥","제육볶음","순두부찌개","감자탕",
        "족발","보쌈","떡볶이","순대","오뎅",
        "곱창","막창","치킨","피자","햄버거",
        "파스타","스테이크","초밥","라멘","우동",
        "짜장면","짬뽕","탕수육","마라탕","훠궈",
        "쌀국수","샤브샤브","돈까스","카레","오므라이스",
        "김밥","국밥","설렁탕","갈비탕","육개장",
        "해장국","아귀찜","낙곱새","쭈꾸미볶음","오징어볶음",
        "닭한마리","한우구이","양꼬치","브런치","샌드위치"
    ]
}

# -------------------------
# 음식 종류별 맛집
# -------------------------

restaurants = {
    "한식": [
        ("할머니국밥", "진한 국물의 국밥 전문점"),
        ("서울밥상", "집밥 느낌 가득"),
        ("고기천국", "삼겹살 맛집"),
        ("김치명가", "김치찌개 전문"),
        ("청춘식당", "가성비 좋은 한식")
    ],
    "중식": [
        ("황금반점", "정통 짜장면"),
        ("용궁짬뽕", "얼큰한 짬뽕"),
        ("마라천국", "마라탕 인기"),
        ("홍콩반점", "가성비 중식"),
        ("북경성", "중화요리 전문")
    ],
    "일식": [
        ("도쿄초밥", "신선한 초밥"),
        ("라멘하우스", "진한 돈코츠 라멘"),
        ("사쿠라", "일본 가정식"),
        ("우동공방", "수타 우동"),
        ("돈까스명가", "두툼한 돈까스")
    ],
    "양식": [
        ("파스타랩", "수제 파스타"),
        ("스테이크하우스", "프리미엄 스테이크"),
        ("브런치팩토리", "감성 브런치"),
        ("피자스퀘어", "화덕피자 전문"),
        ("버거클럽", "수제버거 맛집")
    ]
}

# -------------------------
# 지역 입력
# -------------------------

region = st.text_input(
    "📍 현재 있는 시/도를 입력하세요",
    placeholder="예: 서울"
)

if region:

    st.success(f"🎉 {region} 지역 추천 음식 리스트")

    food_list = foods.get(region, foods["서울"])

    cols = st.columns(5)

    for idx, food in enumerate(food_list):
        cols[idx % 5].write(f"🍽️ {food}")

    st.divider()

    st.info("🤔 아직도 못 고르겠다면 음식 종류를 선택해보자!")

    category = st.radio(
        "🍴 어떤 음식이 땡겨?",
        ["한식", "중식", "일식", "양식"],
        horizontal=True
    )

    st.subheader(f"⭐ 추천 {category} 맛집 TOP 5")

    for shop, desc in restaurants[category]:

        distance = round(random.uniform(0.5, 8.0), 1)

        walk_time = int(distance * 12)

        transport_time = int(distance * 4)

        with st.container(border=True):

            st.markdown(f"## 🍜 {shop}")

            st.write(f"💬 {desc}")

            st.write(f"📏 예상 거리 : {distance} km")

            st.write(f"🚶 걸어서 약 {walk_time}분")

            st.write(f"🚌 대중교통 약 {transport_time}분")

            st.write("⭐ 친구들이 자주 찾는 인기 맛집!")

st.divider()

st.caption("🍔 맛있는 식사하고 좋은 하루 보내자!")

import streamlit as st
from faker import Faker
import pandas as pd

# Faker 인스턴스 생성
fake = Faker()

# 가상 사용자 데이터를 생성하는 함수
def generate_fake_users(num_users):
    data = []
    for _ in range(num_users):
        user = {
            "Name": fake.name(),
            "Address": fake.address(),
            "Email": fake.email(),
            "Phone Number": fake.phone_number(),
            "Job": fake.job(),
            "Company": fake.company(),
            "Birthdate": fake.date_of_birth(),
            "Country": fake.country(),
        }
        data.append(user)
    return pd.DataFrame(data)

# Streamlit UI
st.set_page_config(layout="wide")
st.title("Faker 기반 가상 사용자 생성기")

# 사용자 수 입력
num_users = st.slider("생성할 사용자 수 선택", min_value=1, max_value=100, value=10)

# 사용자 데이터 생성 버튼
if st.button("가상 사용자 생성"):
    # 사용자 데이터 생성
    users_df = generate_fake_users(num_users)
    
    # 데이터 표시
    st.write(f"생성된 {num_users}명의 가상 사용자 데이터:")
    st.dataframe(users_df)
    
    # CSV 다운로드 버튼
    csv = users_df.to_csv(index=False)
    st.download_button("CSV로 다운로드", data=csv, file_name="fake_users.csv", mime="text/csv")

# 앱 설명
st.markdown("""
### 사용 방법:
- 슬라이더를 통해 원하는 가상 사용자 수를 선택하세요.
- '가상 사용자 생성' 버튼을 눌러 데이터를 생성하세요.
- 생성된 데이터를 테이블 형식으로 확인할 수 있습니다.
- CSV 파일로 다운로드하여 데이터를 저장할 수 있습니다.
""")

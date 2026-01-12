import os
import requests
import streamlit as st

API_BASE_URL = os.getenv("API_BASE_URL", "http://localhost:8000")

st.set_page_config(page_title="Notes UI", page_icon="📝")
st.title("📝 Notes (Streamlit)")
st.caption(f"API: {API_BASE_URL}")

def fetch_notes():
    r = requests.get(f"{API_BASE_URL}/notes", timeout=5)
    r.raise_for_status()
    data = r.json()
    return data.get("items", [])

def create_note(content: str):
    r = requests.post(f"{API_BASE_URL}/notes", json={"content": content}, timeout=5)
    r.raise_for_status()
    return r.json()

# ---- UI ----
with st.form("create_form", clear_on_submit=True):
    content = st.text_input("내용", placeholder="메모를 입력하세요 (1~200자)")
    submitted = st.form_submit_button("등록")
    if submitted:
        if not content.strip():
            st.warning("내용을 입력해줘!")
        else:
            try:
                create_note(content.strip())
                st.success("등록 완료!")
            except Exception as e:
                st.error(f"등록 실패: {e}")

st.divider()

col1, col2 = st.columns([1, 1])
with col1:
    if st.button("🔄 새로고침"):
        st.rerun()
with col2:
    st.write("")

try:
    notes = fetch_notes()
    if not notes:
        st.info("아직 데이터가 없어. 위에서 하나 등록해봐!")
    else:
        st.subheader(f"목록 ({len(notes)})")
        for n in notes:
            # row가 {"id":..., "content":..., "created_at":...} 형태라고 가정
            st.write(f"**#{n.get('id')}**  {n.get('content')}")
            st.caption(str(n.get("created_at")))
            st.divider()
except Exception as e:
    st.error(f"목록 불러오기 실패: {e}")
    st.write("✅ 체크: FastAPI가 실행 중인지 / API_BASE 주소가 맞는지 확인!")

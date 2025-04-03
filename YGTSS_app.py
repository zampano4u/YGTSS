import streamlit as st
import re

questions = [
    {"id": 1, "ko": "운동 틱 개수", "en": "Number of Motor Tics"},
    {"id": 2, "ko": "운동 틱 빈도", "en": "Frequency of Motor Tics"},
    {"id": 3, "ko": "운동 틱 강도", "en": "Intensity of Motor Tics"},
    {"id": 4, "ko": "운동 틱 복잡성", "en": "Complexity of Motor Tics"},
    {"id": 5, "ko": "운동 틱으로 인한 방해 정도", "en": "Interference of Motor Tics"},
    {"id": 6, "ko": "음성 틱 개수", "en": "Number of Vocal Tics"},
    {"id": 7, "ko": "음성 틱 빈도", "en": "Frequency of Vocal Tics"},
    {"id": 8, "ko": "음성 틱 강도", "en": "Intensity of Vocal Tics"},
    {"id": 9, "ko": "음성 틱 복잡성", "en": "Complexity of Vocal Tics"},
    {"id": 10, "ko": "음성 틱으로 인한 방해 정도", "en": "Interference of Vocal Tics"},
    {"id": 11, "ko": "기능 손상 정도", "en": "Impairment"}
]

# 각 문항 공통 선택지 (1~10번은 0~5점)
common_options = [
    "없음 (0)", "최소 (1)", "경미 (2)", "중간 (3)", "심각 (4)", "극심 (5)"
]

# 11번 문항만 별도 (0~50점 단위)
impairment_options = [
    "없음 (0)", "최소 (10)", "경미 (20)", "중간 (30)", "심각 (40)", "극심 (50)"
]

# UI 구성
st.title("Yale Global Tic Severity Scale (YGTSS)")

user_inputs = []
all_answered = True

for q in questions:
    opts = impairment_options if q["id"] == 11 else common_options
    choice = st.selectbox(q["ko"], opts, key=q["id"])
    if not choice:
        all_answered = False
    user_inputs.append(f'{q["id"]}. {q["en"]} - {choice}')

if st.button("Show Result"):
    if not all_answered or len(user_inputs) != 11:
        st.warning("모든 항목에 응답해 주세요.")
    else:
        # 점수 추출
        scores = [int(re.search(r"\((\d+)\)", s).group(1)) for s in user_inputs]
        total_tic_score = sum(scores[:10])  # 1~10번
        global_score = total_tic_score + scores[10]  # + impairment

        # 출력
        output = ["**Yale Global Tic Severity Scale, YGTSS**", ""]
        output.extend(user_inputs)
        output.append("")
        output.append(f"총 틱 점수 (Total Tic Score): {total_tic_score}")
        output.append(f"전반적 심각도 점수 (Global Severity Score): {global_score}")

        st.code("\n".join(output), language="markdown")

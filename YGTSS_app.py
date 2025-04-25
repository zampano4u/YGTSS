# pip install streamlit

import streamlit as st
import streamlit.components.v1 as components

# YGTSS 평가 문항 및 선택지 리스트 (tic_severity_mapping)
tic_severity_mapping = [
    {
        "id": 1,
        "question_ko": "운동 틱 수",
        "question_en": "Motor Tic Number",
        "description_ko": "운동 틱의 수를 평가합니다.",
        "description_en": "Evaluates the number of motor tics present.",
        "choices": {
            0: {
                "ko": "없음 - 운동 틱이 존재하지 않습니다.",
                "en": "NONE - No motor tics present.",
                "response_text_ko": "예시: 없음 - 운동 틱이 존재하지 않습니다.",
                "response_text_en": "Example: NONE - No motor tics present."
            },
            1: {
                "ko": "단일 틱 - 단 하나의 운동 틱만 존재합니다.",
                "en": "Single tic - Only one motor tic present.",
                "response_text_ko": "예시: 단일 틱 - 단 하나의 운동 틱만 존재합니다.",
                "response_text_en": "Example: Single tic - Only one motor tic present."
            },
            2: {
                "ko": "이산적인 틱 여러 개 (2-5개) - 두 개에서 다섯 개 사이의 분리된 운동 틱이 존재합니다.",
                "en": "Multiple discrete tics (2-5) - Two to five discrete motor tics present.",
                "response_text_ko": "예시: 이산적인 틱 여러 개 (2-5개) - 두 개에서 다섯 개 사이의 분리된 운동 틱이 존재합니다.",
                "response_text_en": "Example: Multiple discrete tics (2-5) - Two to five discrete motor tics present."
            },
            3: {
                "ko": "이산적인 틱 여러 개 (>5개) - 다섯 개를 초과하는 분리된 운동 틱이 존재합니다.",
                "en": "Multiple discrete tics (>5) - More than five discrete motor tics present.",
                "response_text_ko": "예시: 이산적인 틱 여러 개 (>5개) - 다섯 개를 초과하는 분리된 운동 틱이 존재합니다.",
                "response_text_en": "Example: Multiple discrete tics (>5) - More than five discrete motor tics present."
            },
            4: {
                "ko": "이산적인 틱 여러 개에 더하여, 동시에 혹은 연속적으로 발생하는 복합적인 틱의 조직화된 양상이 하나 이상 존재하여, 개별 틱들을 구분하기 어려운 경우입니다.",
                "en": "Multiple discrete tics plus at least one orchestrated pattern of multiple simultaneous or sequential tics where it is difficult to distinguish discrete tics.",
                "response_text_ko": "예시: 이산적인 틱 여러 개에 더하여, 동시에 혹은 연속적으로 발생하는 복합적인 틱의 조직화된 양상이 하나 이상 존재하여, 개별 틱들을 구분하기 어려운 경우입니다.",
                "response_text_en": "Example: Multiple discrete tics plus at least one orchestrated pattern of multiple simultaneous or sequential tics where it is difficult to distinguish discrete tics."
            },
            5: {
                "ko": "이산적인 틱 여러 개에 더하여, 동시에 혹은 연속적으로 발생하는 복합적인 틱의 조직화된 발작(paroxysm)이 두 개를 초과하여 여러 번 나타나며, 개별 틱을 구분하기 어려운 경우입니다.",
                "en": "Multiple discrete tics plus several (>2) orchestrated paroxysms of multiple simultaneous or sequential tics that where it is difficult to distinguish discrete tics.",
                "response_text_ko": "예시: 이산적인 틱 여러 개에 더하여, 동시에 혹은 연속적으로 발생하는 복합적인 틱의 조직화된 발작(paroxysm)이 두 개를 초과하여 여러 번 나타나며, 개별 틱을 구분하기 어려운 경우입니다.",
                "response_text_en": "Example: Multiple discrete tics plus several (>2) orchestrated paroxysms of multiple simultaneous or sequential tics that where it is difficult to distinguish discrete tics."
            }
        }
    },
    {
        "id": 2,
        "question_ko": "음성 틱 수",
        "question_en": "Vocal Tic Number",
        "description_ko": "음성 틱의 수를 평가합니다.",
        "description_en": "Evaluates the number of vocal tics present.",
        "choices": {
            0: {
                "ko": "없음 - 음성 틱이 존재하지 않습니다.",
                "en": "NONE - No vocal tics present.",
                "response_text_ko": "예시: 없음 - 음성 틱이 존재하지 않습니다.",
                "response_text_en": "Example: NONE - No vocal tics present."
            },
            1: {
                "ko": "단일 틱 - 단 하나의 음성 틱만 존재합니다.",
                "en": "Single tic - Only one vocal tic present.",
                "response_text_ko": "예시: 단일 틱 - 단 하나의 음성 틱만 존재합니다.",
                "response_text_en": "Example: Single tic - Only one vocal tic present."
            },
            2: {
                "ko": "이산적인 틱 여러 개 (2-5개) - 두 개에서 다섯 개 사이의 분리된 음성 틱이 존재합니다.",
                "en": "Multiple discrete tics (2-5) - Two to five discrete vocal tics present.",
                "response_text_ko": "예시: 이산적인 틱 여러 개 (2-5개) - 두 개에서 다섯 개 사이의 분리된 음성 틱이 존재합니다.",
                "response_text_en": "Example: Multiple discrete tics (2-5) - Two to five discrete vocal tics present."
            },
            3: {
                "ko": "이산적인 틱 여러 개 (>5개) - 다섯 개를 초과하는 분리된 음성 틱이 존재합니다.",
                "en": "Multiple discrete tics (>5) - More than five discrete vocal tics present.",
                "response_text_ko": "예시: 이산적인 틱 여러 개 (>5개) - 다섯 개를 초과하는 분리된 음성 틱이 존재합니다.",
                "response_text_en": "Example: Multiple discrete tics (>5) - More than five discrete vocal tics present."
            },
            4: {
                "ko": "이산적인 틱 여러 개에 더하여, 동시에 혹은 연속적으로 발생하는 복합적인 틱의 조직화된 양상이 하나 이상 존재하여, 개별 틱들을 구분하기 어려운 경우입니다.",
                "en": "Multiple discrete tics plus at least one orchestrated pattern of multiple simultaneous or sequential tics where it is difficult to distinguish discrete tics.",
                "response_text_ko": "예시: 이산적인 틱 여러 개에 더하여, 동시에 혹은 연속적으로 발생하는 복합적인 틱의 조직화된 양상이 하나 이상 존재하여, 개별 틱들을 구분하기 어려운 경우입니다.",
                "response_text_en": "Example: Multiple discrete tics plus at least one orchestrated pattern of multiple simultaneous or sequential tics where it is difficult to distinguish discrete tics."
            },
            5: {
                "ko": "이산적인 틱 여러 개에 더하여, 동시에 혹은 연속적으로 발생하는 복합적인 틱의 조직화된 발작(paroxysm)이 두 개를 초과하여 여러 번 나타나며, 개별 틱을 구분하기 어려운 경우입니다.",
                "en": "Multiple discrete tics plus several (>2) orchestrated paroxysms of multiple simultaneous or sequential tics that where it is difficult to distinguish discrete tics.",
                "response_text_ko": "예시: 이산적인 틱 여러 개에 더하여, 동시에 혹은 연속적으로 발생하는 복합적인 틱의 조직화된 발작(paroxysm)이 두 개를 초과하여 여러 번 나타나며, 개별 틱을 구분하기 어려운 경우입니다.",
                "response_text_en": "Example: Multiple discrete tics plus several (>2) orchestrated paroxysms of multiple simultaneous or sequential tics that where it is difficult to distinguish discrete tics."
            }
        }
    },
    {
        "id": 3,
        "question_ko": "운동 틱 빈도",
        "question_en": "Motor Tic Frequency",
        "description_ko": "운동 틱 행동의 발생 빈도를 평가합니다.",
        "description_en": "Evaluates the frequency of motor tic behaviors.",
        "choices": {
            0: {
                "ko": "특정한 틱 행동의 증거가 없습니다.",
                "en": "No evidence of specific tic behaviors.",
                "response_text_ko": "예시: 특정한 틱 행동의 증거가 없습니다.",
                "response_text_en": "Example: No evidence of specific tic behaviors."
            },
            1: {
                "ko": "드묾 (RARELY) - 특정한 틱 행동이 지난 일주일 동안 존재하였으며, 이러한 행동은 드물게 발생하고, 일상적으로 나타나지는 않습니다. 틱의 일시적 발작이 발생하더라도, 짧고 비정상적으로 드뭅니다.",
                "en": "RARELY - Specific tic behaviors have been present during previous week. These behaviors occur infrequently, often not on a daily basis. If bouts of tics occur, they are brief and uncommon.",
                "response_text_ko": "예시: 드묾 (RARELY) - 특정한 틱 행동이 지난 일주일 동안 존재하였으며, 드물게 발생합니다.",
                "response_text_en": "Example: RARELY - Specific tic behaviors have been present during previous week and occur infrequently."
            },
            2: {
                "ko": "때때로 (OCCASIONALLY) - 특정한 틱 행동이 대개 매일 나타나지만, 하루 중 틱이 없는 긴 간격이 존재합니다. 틱 발작이 간헐적으로 발생할 수 있으나, 보통 몇 분 이상 지속되지 않습니다.",
                "en": "OCCASIONALLY - Specific tic behaviors are usually present on a daily basis, but there are long tic-free intervals during the day. Bouts of tics may occur on occasion and are not sustained for more than a few minutes at a time.",
                "response_text_ko": "예시: 때때로 (OCCASIONALLY) - 매일 나타나나 긴 틱 없음 간격이 있습니다.",
                "response_text_en": "Example: OCCASIONALLY - Present daily with long tic-free intervals."
            },
            3: {
                "ko": "정기적으로 (REGULARLY) - 특정한 틱 행동이 매일 나타납니다. 틱이 없는 간격이 3시간 정도 지속되는 경우도 드물지 않으며, 틱 발작은 정기적으로 발생하지만, 특정한 한 가지 상황에만 제한될 수 있습니다.",
                "en": "REGULARLY - Specific tic behaviors are present on a daily basis. Tic-free intervals as long as 3 hours are not uncommon. Bouts of tics occur regularly but may be limited to a single setting.",
                "response_text_ko": "예시: 정기적으로 (REGULARLY) - 매일 발생하며 3시간 정도 틱 없는 간격이 있습니다.",
                "response_text_en": "Example: REGULARLY - Present daily with tic-free intervals up to 3 hours."
            },
            4: {
                "ko": "자주 (FREQUENTLY) - 특정한 틱 행동이 사실상 매일의 모든 깨어 있는 시간에 존재하며, 지속적인 틱 행동의 기간이 규칙적으로 나타납니다. 틱 발작은 흔하며, 특정한 상황에만 국한되지 않습니다.",
                "en": "FREQUENTLY - Specific tic behaviors are present virtually every waking hour of every day, and periods of sustained tic behaviors occur regularly. Bouts of tics are common and are not limited to a single setting.",
                "response_text_ko": "예시: 자주 (FREQUENTLY) - 거의 매 시간 지속적으로 틱이 나타납니다.",
                "response_text_en": "Example: FREQUENTLY - Present nearly every waking hour with sustained bouts."
            },
            5: {
                "ko": "지속적임 (CONSTANTLY) - 특정한 틱 행동이 사실상 항상 존재합니다. 틱이 없는 간격은 식별하기 어려우며, 최대 5-10분을 넘기지 않습니다.",
                "en": "CONSTANTLY - Specific tic behaviors are present virtually all the time. Tic-free intervals are difficult to identify and do not last more than 5 to 10 minutes at most.",
                "response_text_ko": "예시: 지속적임 (CONSTANTLY) - 거의 항상 틱 행동이 관찰됩니다.",
                "response_text_en": "Example: CONSTANTLY - Tic behaviors are present nearly all the time."
            }
        }
    },
    {
        "id": 4,
        "question_ko": "음성 틱 빈도",
        "question_en": "Vocal Tic Frequency",
        "description_ko": "음성 틱 행동의 발생 빈도를 평가합니다.",
        "description_en": "Evaluates the frequency of vocal tic behaviors.",
        "choices": {
            0: {
                "ko": "특정한 틱 행동의 증거가 없습니다.",
                "en": "No evidence of specific tic behaviors.",
                "response_text_ko": "예시: 특정한 틱 행동의 증거가 없습니다.",
                "response_text_en": "Example: No evidence of specific tic behaviors."
            },
            1: {
                "ko": "드묾 (RARELY) - 특정한 틱 행동이 지난 일주일 동안 존재하였으며, 이러한 행동은 드물게 발생하고, 일상적으로 나타나지는 않습니다. 틱의 일시적 발작이 발생하더라도, 짧고 비정상적으로 드뭅니다.",
                "en": "RARELY - Specific tic behaviors have been present during previous week. These behaviors occur infrequently, often not on a daily basis. If bouts of tics occur, they are brief and uncommon.",
                "response_text_ko": "예시: 드묾 (RARELY) - 일주일 동안 드물게 틱 행동이 나타납니다.",
                "response_text_en": "Example: RARELY - Tic behaviors appear infrequently over the week."
            },
            2: {
                "ko": "때때로 (OCCASIONALLY) - 특정한 틱 행동이 대개 매일 나타나지만, 하루 중 틱이 없는 긴 간격이 존재합니다. 틱 발작이 간헐적으로 발생할 수 있으나, 보통 몇 분 이상 지속되지 않습니다.",
                "en": "OCCASIONALLY - Specific tic behaviors are usually present on a daily basis, but there are long tic-free intervals during the day. Bouts of tics may occur on occasion and are not sustained for more than a few minutes at a time.",
                "response_text_ko": "예시: 때때로 (OCCASIONALLY) - 매일 나타나나 틱 없는 긴 간격이 있습니다.",
                "response_text_en": "Example: OCCASIONALLY - Present daily with long tic-free periods."
            },
            3: {
                "ko": "정기적으로 (REGULARLY) - 특정한 틱 행동이 매일 나타납니다. 틱이 없는 간격이 3시간 정도 지속되는 경우도 드물지 않으며, 틱 발작은 정기적으로 발생하지만, 특정한 한 가지 상황에만 제한될 수 있습니다.",
                "en": "REGULARLY - Specific tic behaviors are present on a daily basis. Tic-free intervals as long as 3 hours are not uncommon. Bouts of tics occur regularly but may be limited to a single setting.",
                "response_text_ko": "예시: 정기적으로 (REGULARLY) - 매일 발생하며 3시간 정도 틱 없는 간격이 있습니다.",
                "response_text_en": "Example: REGULARLY - Occurring daily with tic-free periods of around 3 hours."
            },
            4: {
                "ko": "자주 (FREQUENTLY) - 특정한 틱 행동이 사실상 매일의 모든 깨어 있는 시간에 존재하며, 지속적인 틱 행동의 기간이 규칙적으로 나타납니다. 틱 발작은 흔하며, 특정한 상황에만 국한되지 않습니다.",
                "en": "FREQUENTLY - Specific tic behaviors are present virtually every waking hour of every day, and periods of sustained tic behaviors occur regularly. Bouts of tics are common and are not limited to a single setting.",
                "response_text_ko": "예시: 자주 (FREQUENTLY) - 거의 매 시간 틱 행동이 관찰됩니다.",
                "response_text_en": "Example: FREQUENTLY - Observed nearly every waking hour."
            },
            5: {
                "ko": "지속적임 (CONSTANTLY) - 특정한 틱 행동이 사실상 항상 존재합니다. 틱이 없는 간격은 식별하기 어려우며, 최대 5-10분을 넘기지 않습니다.",
                "en": "CONSTANTLY - Specific tic behaviors are present virtually all the time. Tic-free intervals are difficult to identify and do not last more than 5 to 10 minutes at most.",
                "response_text_ko": "예시: 지속적임 (CONSTANTLY) - 거의 항상 틱 행동이 관찰됩니다.",
                "response_text_en": "Example: CONSTANTLY - Tic behaviors are nearly continuous."
            }
        }
    },
    {
        "id": 5,
        "question_ko": "운동 틱 강도",
        "question_en": "Motor Tic Intensity",
        "description_ko": "운동 틱의 강도(표현의 강도 및 주목성)를 평가합니다.",
        "description_en": "Evaluates the intensity of motor tics (the force and conspicuousness of their expression).",
        "choices": {
            0: {
                "ko": "없음 - 관찰되거나 경험되는 틱이 없습니다.",
                "en": "ABSENT - No visible or experienced tics.",
                "response_text_ko": "예시: 없음 - 관찰되거나 경험되는 틱이 없습니다.",
                "response_text_en": "Example: ABSENT - No visible or experienced tics."
            },
            1: {
                "ko": "최소 수준 (MINIMAL) - 틱은 보이지 않거나 들리지 않으며(환자의 주관적인 경험에만 기반함), 유사한 자발적 행동보다 덜 강하고 일반적으로 그 강도 때문에 인지되지 않습니다.",
                "en": "MINIMAL - Tics not visible or audible (based solely on patient's private experience) or tics are less forceful than comparable voluntary actions and are typically not noticed because of their intensity.",
                "response_text_ko": "예시: 최소 수준 (MINIMAL) - 틱이 미미하여 인지되지 않습니다.",
                "response_text_en": "Example: MINIMAL - Tics are so minimal that they are not noticed."
            },
            2: {
                "ko": "경도 (MILD) - 틱은 유사한 자발적 행동이나 발화보다 더 강하지 않으며, 보통 그 강도 때문에 인지되지 않습니다.",
                "en": "MILD - Tics are not more forceful than comparable voluntary actions or utterances and are typically not noticed because of their intensity.",
                "response_text_ko": "예시: 경도 (MILD) - 틱이 보통 강도로 나타납니다.",
                "response_text_en": "Example: MILD - Tics are present but not markedly forceful."
            },
            3: {
                "ko": "중등도 (MODERATE) - 틱은 유사한 자발적 행동보다 더 강하지만 정상적인 표현 범위를 벗어나지는 않습니다. 그 강도 때문에 타인의 주의를 끌 수 있습니다.",
                "en": "MODERATE - Tics are more forceful than comparable voluntary actions but are not outside the range of normal expression. They may call attention to the individual.",
                "response_text_ko": "예시: 중등도 (MODERATE) - 틱이 타인의 주의를 끌 정도로 나타납니다.",
                "response_text_en": "Example: MODERATE - Tics are sufficiently strong to draw attention."
            },
            4: {
                "ko": "뚜렷함 (MARKED) - 틱은 유사한 자발적 행동보다 훨씬 강하고 전형적으로 '과장된' 특성을 가지며, 이러한 강도와 과장된 특성으로 인해 타인의 주목을 자주 끕니다.",
                "en": "MARKED - Tics are more forceful and typically have an 'exaggerated' character, frequently calling attention to the individual.",
                "response_text_ko": "예시: 뚜렷함 (MARKED) - 틱이 과장되어 타인의 주목을 받습니다.",
                "response_text_en": "Example: MARKED - Tics are exaggerated and noticeably draw attention."
            },
            5: {
                "ko": "심함 (SEVERE) - 틱은 극도로 강하고 과장되어 표현되며, 그 강력한 표현으로 인해 타인의 주목을 받을 뿐 아니라 신체적 손상(우발적, 유발적, 또는 자해적)의 위험을 초래할 수 있습니다.",
                "en": "SEVERE - Tics are extremely forceful and exaggerated in expression. These tics call attention to the individual and may result in risk of physical injury (accidental, provoked, or self-inflicted).",
                "response_text_ko": "예시: 심함 (SEVERE) - 틱의 강도가 매우 높아 신체적 위험까지 초래할 수 있습니다.",
                "response_text_en": "Example: SEVERE - Tics are extremely forceful with potential risk of injury."
            }
        }
    },
    {
        "id": 6,
        "question_ko": "음성 틱 강도",
        "question_en": "Vocal Tic Intensity",
        "description_ko": "음성 틱의 강도(발화의 강도 및 주목성)를 평가합니다.",
        "description_en": "Evaluates the intensity of vocal tics (the force and conspicuousness of their expression).",
        "choices": {
            0: {
                "ko": "없음 - 음성 틱이 존재하지 않습니다.",
                "en": "ABSENT - No vocal tics present.",
                "response_text_ko": "예시: 없음 - 음성 틱이 존재하지 않습니다.",
                "response_text_en": "Example: ABSENT - No vocal tics present."
            },
            1: {
                "ko": "최소 수준 (MINIMAL) - 틱은 들리지 않거나, 유사한 자발적 발화보다 덜 강하며, 일반적으로 그 강도 때문에 인지되지 않습니다.",
                "en": "MINIMAL - Tics not audible or are less forceful than comparable voluntary utterances and are typically not noticed because of their intensity.",
                "response_text_ko": "예시: 최소 수준 (MINIMAL) - 음성 틱이 미미하여 잘 들리지 않습니다.",
                "response_text_en": "Example: MINIMAL - Vocal tics are minimal and not easily noticed."
            },
            2: {
                "ko": "경도 (MILD) - 틱은 유사한 자발적 발화보다 더 강하지 않으며, 보통 그 강도 때문에 인지되지 않습니다.",
                "en": "MILD - Tics are not more forceful than comparable voluntary utterances and are typically not noticed because of their intensity.",
                "response_text_ko": "예시: 경도 (MILD) - 음성 틱이 보통의 강도로 나타납니다.",
                "response_text_en": "Example: MILD - Vocal tics are present but not notably forceful."
            },
            3: {
                "ko": "중등도 (MODERATE) - 틱은 유사한 자발적 발화보다 더 강하지만, 정상적인 표현의 범위를 벗어나지 않습니다. 그 강도 때문에 타인의 주의를 끌 수 있습니다.",
                "en": "MODERATE - Tics are more forceful than comparable voluntary utterances but are not outside the range of normal expression. They may call attention to the individual.",
                "response_text_ko": "예시: 중등도 (MODERATE) - 음성 틱이 타인의 주의를 끌 정도로 강합니다.",
                "response_text_en": "Example: MODERATE - Vocal tics are moderately strong and noticeable."
            },
            4: {
                "ko": "뚜렷함 (MARKED) - 틱은 유사한 자발적 발화보다 훨씬 강하며, 전형적으로 '과장된' 특성을 가지며, 이로 인해 타인의 주목을 자주 받습니다.",
                "en": "MARKED - Tics are more forceful and typically have an 'exaggerated' character. Such tics frequently call attention to the individual.",
                "response_text_ko": "예시: 뚜렷함 (MARKED) - 음성 틱이 과장되어 명확히 들립니다.",
                "response_text_en": "Example: MARKED - Vocal tics are exaggerated and clearly noticeable."
            },
            5: {
               "ko": "심함 (SEVERE) - 틱은 매우 강하고 과장된 방식으로 표현되며, 그로 인해 신체적 손상(우발적, 유발적, 자해적)의 위험을 초래할 수 있습니다.",
               "en": "SEVERE - Tics are extremely forceful and exaggerated in expression. These tics may result in risk of physical injury (accidental, provoked, or self-inflicted).",
               "response_text_ko": "예시: 심함 (SEVERE) - 음성 틱이 매우 강해 신체적 위험까지 있을 수 있습니다.",
               "response_text_en": "Example: SEVERE - Vocal tics are extremely forceful with potential injury risk."
           }
       }
   },
   {
       "id": 7,
       "question_ko": "운동 틱 복잡성",
       "question_en": "Motor Tic Complexity",
       "description_ko": "운동 틱의 복잡성(단순한 vs. 복잡한 특성)을 평가합니다.",
       "description_en": "Evaluates the complexity of motor tics (simple vs. complex characteristics).",
       "choices": {
           0: {
               "ko": "없음 - 존재하는 틱이 있다면 모두 명백히 '단순한'(갑작스럽고, 짧고, 목적 없는) 특성을 가집니다.",
               "en": "NONE - If present, all tics are clearly 'simple' (sudden, brief, purposeless) in character.",
               "response_text_ko": "예시: 없음 - 모든 운동 틱이 단순합니다.",
               "response_text_en": "Example: NONE - All motor tics are simple."
           },
           1: {
               "ko": "다소 복잡함 - 일부 틱은 명백하게 단순하다고 보기 어렵습니다.",
               "en": "SOMEWHAT COMPLEX - Some tics are not clearly 'simple' in character.",
               "response_text_ko": "예시: 다소 복잡함 - 일부 운동 틱은 단순하지 않습니다.",
               "response_text_en": "Example: SOMEWHAT COMPLEX - Some motor tics are not clearly simple."
           },
           2: {
               "ko": "약간 복잡함 - 일부 틱은 명확하게 '복잡한' 특성을 가지며, 짧고 자동적인 행동을 흉내 내는 것처럼 보입니다.",
               "en": "MILDLY COMPLEX - Some tics are clearly 'complex' (purposive in appearance) and mimic brief 'automatic' behaviors.",
               "response_text_ko": "예시: 약간 복잡함 - 일부 운동 틱은 복잡한 특성을 보입니다.",
               "response_text_en": "Example: MILDLY COMPLEX - Some motor tics exhibit complex features."
           },
           3: {
               "ko": "중등도로 복잡함 - 일부 틱은 더욱 복잡한 특성을 가지며, 위장하기 어려운 조직화된 틱 발작 형태로 나타날 수 있습니다.",
               "en": "MODERATELY COMPLEX - Some tics are more 'complex' and may occur in orchestrated bouts that would be difficult to camouflage.",
               "response_text_ko": "예시: 중등도로 복잡함 - 운동 틱이 조직화된 발작 형태로 나타납니다.",
               "response_text_en": "Example: MODERATELY COMPLEX - Motor tics may appear in complex, organized bouts."
           },
           4: {
               "ko": "뚜렷하게 복잡함 - 일부 틱은 매우 복잡하고, 부적절하거나 기이하며 외설적인 특성을 지닙니다.",
               "en": "MARKEDLY COMPLEX - Some tics are very 'complex' and inappropriate, bizarre or obscene in character.",
               "response_text_ko": "예시: 뚜렷하게 복잡함 - 운동 틱이 기이하고 외설적입니다.",
               "response_text_en": "Example: MARKEDLY COMPLEX - Motor tics are notably bizarre or obscene."
           },
           5: {
               "ko": "극도로 복잡함 - 일부 틱은 정상적인 행동으로 위장하거나 설명하는 것이 불가능한 장기적이고 외설적이며 기괴한 발작 형태를 포함합니다.",
               "en": "EXTREMELY COMPLEX - Some tics involve lengthy bouts that would be impossible to camouflage or rationalize as normal.",
               "response_text_ko": "예시: 극도로 복잡함 - 운동 틱이 장기간 기괴하게 나타납니다.",
               "response_text_en": "Example: EXTREMELY COMPLEX - Motor tics appear in prolonged, inexplicable bouts."
           }
       }
   },
   {
       "id": 8,
       "question_ko": "음성 틱 복잡성",
       "question_en": "Vocal Tic Complexity",
       "description_ko": "음성 틱의 복잡성(단순한 vs. 복잡한 특성)을 평가합니다.",
       "description_en": "Evaluates the complexity of vocal tics (simple vs. complex characteristics).",
       "choices": {
           0: {
               "ko": "없음 - 존재하는 틱이 있다면 모두 명백히 '단순한'(갑작스럽고, 짧고, 목적 없는) 특성을 가집니다.",
               "en": "NONE - If present, all tics are clearly 'simple' (sudden, brief, purposeless) in character.",
               "response_text_ko": "예시: 없음 - 모든 음성 틱이 단순합니다.",
               "response_text_en": "Example: NONE - All vocal tics are simple."
           },
           1: {
               "ko": "다소 복잡함 - 일부 틱은 명백하게 단순하다고 보기 어렵습니다.",
               "en": "SOMEWHAT COMPLEX - Some tics are not clearly 'simple' in character.",
               "response_text_ko": "예시: 다소 복잡함 - 일부 음성 틱은 단순하지 않습니다.",
               "response_text_en": "Example: SOMEWHAT COMPLEX - Some vocal tics are not clearly simple."
           },
           2: {
               "ko": "약간 복잡함 - 일부 틱은 명확하게 '복잡한' 특성을 가지며, 짧고 자동적인 발화를 흉내 냅니다.",
               "en": "MILDLY COMPLEX - Some tics are clearly 'complex' and mimic brief automatic utterances.",
               "response_text_ko": "예시: 약간 복잡함 - 일부 음성 틱은 복잡한 특성을 보입니다.",
               "response_text_en": "Example: MILDLY COMPLEX - Some vocal tics exhibit complex features."
           },
           3: {
               "ko": "중등도로 복잡함 - 일부 틱은 더 지속적이며, 위장하기 어렵습니다.",
               "en": "MODERATELY COMPLEX - Some tics are more sustained and difficult to camouflage.",
               "response_text_ko": "예시: 중등도로 복잡함 - 음성 틱이 지속적으로 나타납니다.",
               "response_text_en": "Example: MODERATELY COMPLEX - Vocal tics are sustained and hard to camouflage."
           },
           4: {
               "ko": "뚜렷하게 복잡함 - 일부 틱은 부적절하거나 기괴하며, 쉽게 정상적인 행동으로 설명될 수 없습니다.",
               "en": "MARKEDLY COMPLEX - Some tics are inappropriate or bizarre and cannot be easily rationalized.",
               "response_text_ko": "예시: 뚜렷하게 복잡함 - 음성 틱이 기괴하여 정상 설명이 어렵습니다.",
               "response_text_en": "Example: MARKEDLY COMPLEX - Vocal tics are notably bizarre."
           },
           5: {
               "ko": "극도로 복잡함 - 일부 틱은 장기적이고 기괴하거나 외설적인 발화를 포함하며, 이를 정상적인 것으로 설명하는 것은 불가능합니다.",
               "en": "EXTREMELY COMPLEX - Some tics involve lengthy, bizarre, or obscene utterances impossible to rationalize.",
               "response_text_ko": "예시: 극도로 복잡함 - 음성 틱이 장기간 기괴하게 나타납니다.",
               "response_text_en": "Example: EXTREMELY COMPLEX - Vocal tics appear in prolonged, inexplicable bouts."
           }
       }
   },
   {
       "id": 9,
       "question_ko": "운동 틱 방해 정도",
       "question_en": "Motor Tic Interference",
       "description_ko": "운동 틱이 행동에 미치는 방해 정도를 평가합니다.",
       "description_en": "Evaluates the degree of interference of motor tics in behavior.",
       "choices": {
           0: {
               "ko": "없음 - 행동에 방해가 없습니다.",
               "en": "NONE - No interference in behavior.",
               "response_text_ko": "예시: 없음 - 운동 틱이 행동에 방해되지 않습니다.",
               "response_text_en": "Example: NONE - Motor tics do not interfere with behavior."
           },
           1: {
               "ko": "최소 수준 - 틱이 행동의 흐름을 방해하지 않습니다.",
               "en": "MINIMAL - Tics do not interrupt the flow of behavior.",
               "response_text_ko": "예시: 최소 수준 - 운동 틱이 거의 방해되지 않습니다.",
               "response_text_en": "Example: MINIMAL - Motor tics barely interrupt behavior."
           },
           2: {
               "ko": "간헐적 방해 - 틱이 행동의 흐름을 간헐적으로 방해합니다.",
               "en": "OCCASIONAL - Tics occasionally interrupt the flow of behavior.",
               "response_text_ko": "예시: 간헐적 방해 - 운동 틱이 때때로 행동에 방해됩니다.",
               "response_text_en": "Example: OCCASIONAL - Motor tics sometimes interrupt behavior."
           },
           3: {
               "ko": "빈번한 방해 - 틱이 행동의 흐름을 자주 방해합니다.",
               "en": "FREQUENT - Tics frequently interrupt the flow of behavior.",
               "response_text_ko": "예시: 빈번한 방해 - 운동 틱이 자주 행동에 방해됩니다.",
               "response_text_en": "Example: FREQUENT - Motor tics frequently disrupt behavior."
           },
           4: {
               "ko": "뚜렷한 방해 - 틱이 행동의 흐름을 자주 방해하며, 때때로 의도한 행동이나 의사소통을 방해합니다.",
               "en": "MARKED - Tics frequently interrupt behavior and occasionally disrupt intended action or communication.",
               "response_text_ko": "예시: 뚜렷한 방해 - 운동 틱이 행동과 의사소통에 방해됩니다.",
               "response_text_en": "Example: MARKED - Motor tics clearly disrupt behavior and communication at times."
           },
           5: {
               "ko": "심각한 방해 - 틱이 의도된 행동이나 의사소통을 자주 방해합니다.",
               "en": "SEVERE - Tics frequently disrupt intended action or communication.",
               "response_text_ko": "예시: 심각한 방해 - 운동 틱이 행동 및 의사소통에 심각하게 방해됩니다.",
               "response_text_en": "Example: SEVERE - Motor tics severely disrupt intended actions or communication."
           }
       }
   },
   {
       "id": 10,
       "question_ko": "음성 틱 방해 정도",
       "question_en": "Vocal Tic Interference",
       "description_ko": "음성 틱이 말하기에 미치는 방해 정도를 평가합니다.",
       "description_en": "Evaluates the degree of interference of vocal tics in speech.",
       "choices": {
           0: {
               "ko": "없음 - 말하기에 방해가 없습니다.",
               "en": "NONE - No interference in speech.",
               "response_text_ko": "예시: 없음 - 음성 틱이 말하기에 방해되지 않습니다.",
               "response_text_en": "Example: NONE - Vocal tics do not interfere with speech."
           },
           1: {
               "ko": "최소 수준 - 틱이 발화의 흐름을 방해하지 않습니다.",
               "en": "MINIMAL - Tics do not interrupt the flow of speech.",
               "response_text_ko": "예시: 최소 수준 - 음성 틱이 거의 방해되지 않습니다.",
               "response_text_en": "Example: MINIMAL - Vocal tics barely interrupt speech."
           },
           2: {
               "ko": "간헐적 방해 - 틱이 발화의 흐름을 간헐적으로 방해합니다.",
               "en": "OCCASIONALLY - Tics occasionally interrupt the flow of speech.",
               "response_text_ko": "예시: 간헐적 방해 - 음성 틱이 때때로 발화에 방해됩니다.",
               "response_text_en": "Example: OCCASIONALLY - Vocal tics occasionally disrupt speech."
           },
           3: {
               "ko": "빈번한 방해 - 틱이 발화의 흐름을 자주 방해합니다.",
               "en": "FREQUENT - Tics frequently interrupt the flow of speech.",
               "response_text_ko": "예시: 빈번한 방해 - 음성 틱이 자주 발화에 방해됩니다.",
               "response_text_en": "Example: FREQUENT - Vocal tics frequently interrupt speech."
           },
           4: {
               "ko": "뚜렷한 방해 - 틱이 발화를 자주 방해하며, 때때로 의도한 의사소통을 방해합니다.",
               "en": "MARKED - Tics frequently interrupt speech and occasionally disrupt intended communication.",
               "response_text_ko": "예시: 뚜렷한 방해 - 음성 틱이 발화와 의사소통에 방해됩니다.",
               "response_text_en": "Example: MARKED - Vocal tics clearly disrupt speech and communication at times."
           },
           5: {
               "ko": "심각한 방해 - 틱이 의도된 의사소통을 자주 방해합니다.",
               "en": "SEVERE - Tics frequently disrupt intended communication.",
               "response_text_ko": "예시: 심각한 방해 - 음성 틱이 의사소통에 심각하게 방해됩니다.",
               "response_text_en": "Example: SEVERE - Vocal tics severely disrupt intended communication."
           }
       }
   },
   {
       "id": 11,
       "question_ko": "기능 손상",
       "question_en": "Impairment",
       "description_ko": "환자의 기능적 손상 정도를 평가합니다.",
       "description_en": "Evaluates the level of functional impairment.",
       "choices": {
           0: {
               "ko": "없음 - 기능 손상이 없습니다.",
               "en": "NONE - No impairment.",
               "response_text_ko": "예시: 없음 - 기능 손상이 없습니다.",
               "response_text_en": "Example: NONE - No impairment is observed."
           },
           10: {
               "ko": "최소 수준 - 자존감, 가족 생활, 사회적 수용, 또는 일상 기능에서 미묘한 어려움이 있습니다.",
               "en": "MINIMAL - Subtle difficulties in self-esteem, family life, social acceptance, or functioning.",
               "response_text_ko": "예시: 최소 수준 - 미묘한 기능적 어려움이 있습니다.",
               "response_text_en": "Example: MINIMAL - There are subtle difficulties in functioning."
           },
           20: {
               "ko": "경도 - 심리사회적 또는 기능적 영역에서 경미한 어려움이 있습니다.",
               "en": "MILD - Minor difficulties in psychosocial or functional domains.",
               "response_text_ko": "예시: 경도 - 심리사회적 기능에 경미한 어려움이 있습니다.",
               "response_text_en": "Example: MILD - Minor psychosocial or functional difficulties are present."
           },
           30: {
               "ko": "중등도 - 자존감 또는 기능에서 분명한 문제가 나타납니다.",
               "en": "MODERATE - Clear problems in self-esteem or functioning.",
               "response_text_ko": "예시: 중등도 - 자존감이나 기능에 분명한 문제가 있습니다.",
               "response_text_en": "Example: MODERATE - There are clear issues in self-esteem or functioning."
           },
           40: {
               "ko": "뚜렷함 - 심리사회적 또는 기능적 영역에서 주요한 어려움이 존재합니다.",
               "en": "MARKED - Major psychosocial or functional difficulties exist.",
               "response_text_ko": "예시: 뚜렷함 - 주요한 기능적 어려움이 나타납니다.",
               "response_text_en": "Example: MARKED - Major difficulties in functioning are observed."
           },
           50: {
               "ko": "심각함 - 자살 사고, 가족의 해체, 학업 또는 직업 상실 등을 포함한 극심한 어려움이 존재합니다.",
               "en": "SEVERE - Extreme difficulties including suicidal ideation, family disruption, or loss of school/work.",
               "response_text_ko": "예시: 심각함 - 극심한 기능 손상이 존재합니다.",
               "response_text_en": "Example: SEVERE - Extreme impairment is observed, including risk factors such as suicidal ideation."
           }
       }
   }
]

def main():
   st.title("YGTSS 평가 웹앱")
   
   st.markdown("### 아래 항목에서 각 문항의 한국어 설명에 따라 드롭다운 메뉴로 선택해 주세요.")
   
   # 각 문항에 대해 st.selectbox를 통해 드롭다운 생성 (st.session_state를 사용하여 상태 유지)
   for q in tic_severity_mapping:
       q_id = q["id"]
       st.selectbox(f"{q['question_ko']} - {q['description_ko']}",
                    options=sorted(q["choices"].keys()),
                    key=f"q_{q_id}",
                    format_func=lambda x, q=q: q["choices"][x]["ko"])
   
   # 결과 출력 버튼
   if st.button("결과 출력"):
       result_lines = []
       # 그룹별 매핑: [1] Number, [2] Frequency, [3] Intensity, [4] Complexity, [5] Interference
       group_mapping = {
           "[1] Number": [1, 2],
           "[2] Frequency": [3, 4],
           "[3] Intensity": [5, 6],
           "[4] Complexity": [7, 8],
           "[5] Interference": [9, 10]
       }
       
       # 각 그룹별 결과 구성
       for group_name, q_ids in group_mapping.items():
           result_lines.append(group_name)
           result_lines.append("")  # 빈 줄
           for qid in q_ids:
               # tic_severity_mapping에서 해당 id 문항 찾기
               question = next((item for item in tic_severity_mapping if item["id"] == qid), None)
               if question:
                   selected_score = st.session_state[f"q_{qid}"]
                   # 특수 대시를 일반 하이픈으로 변환
                   question_en = question['question_en'].replace('–', '-')
                   description_en = question['description_en'].replace('–', '-')
                   choice_en = question['choices'][selected_score]['en'].replace('–', '-')
                   response_text_en = question['choices'][selected_score]['response_text_en'].replace('–', '-')
                   
                   result_lines.append(f"{question_en} - {description_en}")
                   result_lines.append(f"({selected_score}) {choice_en} - {response_text_en}")
                   result_lines.append("")  # 문항 사이 빈 줄
       
       # 장애 점수(Impairment score) 처리 (id: 11)
       impairment_question = next((item for item in tic_severity_mapping if item["id"] == 11), None)
       if impairment_question:
           selected_impairment = st.session_state["q_11"]
           # 특수 대시를 일반 하이픈으로 변환
           imp_en = impairment_question['choices'][selected_impairment]['en'].replace('–', '-')
           imp_response_en = impairment_question['choices'][selected_impairment]['response_text_en'].replace('–', '-')
           
           result_lines.append("*** Impairment score ***")
           result_lines.append(f"({selected_impairment}) {imp_en} - {imp_response_en}")
           result_lines.append("")
       
       # 총 틱 점수: 운동 틱 5개 항목 (id: 1,3,5,7,9) + 음성 틱 5개 항목 (id: 2,4,6,8,10)
       motor_ids = [1, 3, 5, 7, 9]
       vocal_ids = [2, 4, 6, 8, 10]
       total_tic_score = sum(int(st.session_state[f"q_{qid}"]) for qid in (motor_ids + vocal_ids))
       
       # 전반적 심각도 점수 = 총 틱 점수 + 장애 점수(Impairment score)
       impairment_score = int(st.session_state["q_11"])
       global_severity_score = total_tic_score + impairment_score
       
       result_lines.append(f"Total Tic Score: {total_tic_score}")
       result_lines.append(f"Global Severity Score: {global_severity_score}")
       
       result_text = "\n".join(result_lines)
       
       # 결과를 st.code() 블록 내에 출력 (\n을 사용하여 줄바꿈)
       st.code(result_text, language="plaintext")
       
       # 사용자에게 복사 방법 안내
       st.info("결과를 복사하려면 코드 블록 오른쪽 상단의 복사 버튼을 클릭하세요.")

if __name__ == "__main__":
   main()

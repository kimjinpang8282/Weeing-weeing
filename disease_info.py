# 딸기 병 정보 및 약품 추천 데이터

DISEASE_INFO = {
    "Angular leaf spot": {
        "name_kr": "모무늬병",
        "name_en": "Angular Leaf Spot",
        "symptoms": "잎에 각진 모양의 갈색 반점이 생기며, 심하면 잎이 시들어 떨어집니다.",
        "cause": "Xanthomonas fragariae 세균에 의해 발생하며, 습도가 높을 때 전염이 빠릅니다.",
        "prevention": "통풍을 좋게 하고, 물을 잎에 직접 뿌리지 않으며, 감염된 잎은 즉시 제거합니다.",
        "medicines": [
            {
                "name": "코사이드 수화제",
                "company": "듀폰코리아",
                "usage": "물 20L에 20g을 희석하여 7일 간격 살포",
                "link": "https://search.shopping.naver.com/search/all?query=코사이드수화제"
            },
            {
                "name": "성보싸이클린 수화제",
                "company": "성보화학",
                "usage": "물 20L에 10g을 희석하여 살포",
                "link": "https://search.shopping.naver.com/search/all?query=싸이클린수화제"
            },
            {
                "name": "농용신 수화제",
                "company": "동방아그로",
                "usage": "물 20L에 20g을 희석하여 예방 살포",
                "link": "https://search.shopping.naver.com/search/all?query=농용신수화제"
            }
        ]
    },
    "Anthracnose": {
        "name_kr": "탄저병",
        "name_en": "Anthracnose",
        "symptoms": "잎과 과일에 갈색 또는 검은색 원형 반점이 생기며, 과실이 썩습니다.",
        "cause": "Colletotrichum 곰팡이에 의해 발생하며, 고온다습한 환경에서 급속히 확산됩니다.",
        "prevention": "배수를 잘하고, 밀식을 피하며, 이병 잔재물을 제거합니다.",
        "medicines": [
            {
                "name": "프로키온 유제",
                "company": "신젠타",
                "usage": "물 20L에 20ml를 희석하여 10일 간격 살포",
                "link": "https://search.shopping.naver.com/search/all?query=프로키온유제"
            },
            {
                "name": "살림꾼 액상수화제",
                "company": "경농",
                "usage": "물 20L에 10ml를 희석하여 살포",
                "link": "https://search.shopping.naver.com/search/all?query=살림꾼액상수화제"
            },
            {
                "name": "카브리오 유제",
                "company": "바스프",
                "usage": "물 20L에 10ml를 희석하여 예방 살포",
                "link": "https://search.shopping.naver.com/search/all?query=카브리오유제"
            }
        ]
    },
    "Fusarium wilt": {
        "name_kr": "시들음병",
        "name_en": "Fusarium Wilt",
        "symptoms": "아래쪽 잎부터 시들고 황색으로 변하며, 뿌리가 갈변하고 썩습니다.",
        "cause": "Fusarium oxysporum 토양 곰팡이에 의해 발생하며, 뿌리를 통해 감염됩니다.",
        "prevention": "건전한 묘를 사용하고, 토양 소독을 하며, 연작을 피합니다.",
        "medicines": [
            {
                "name": "타미나 수화제",
                "company": "경농",
                "usage": "관주 처리: 물 20L에 20g을 희석",
                "link": "https://search.shopping.naver.com/search/all?query=타미나수화제"
            },
            {
                "name": "포룸 수화제",
                "company": "바이엘",
                "usage": "토양 관주: 물 20L에 40g을 희석",
                "link": "https://search.shopping.naver.com/search/all?query=포룸수화제"
            },
            {
                "name": "리조렉스 수화제",
                "company": "경농",
                "usage": "정식 전 토양 혼화 처리",
                "link": "https://search.shopping.naver.com/search/all?query=리조렉스수화제"
            }
        ]
    },
    "Gray mold": {
        "name_kr": "잿빛곰팡이병",
        "name_en": "Gray Mold",
        "symptoms": "꽃과 열매에 잿빛 곰팡이가 피며, 빠르게 썩어 들어갑니다.",
        "cause": "Botrytis cinerea 곰팡이에 의해 발생하며, 저온 다습할 때 발병합니다.",
        "prevention": "통풍과 환기를 철저히 하고, 과습을 피하며, 병든 부위를 즉시 제거합니다.",
        "medicines": [
            {
                "name": "스위치 입상수화제",
                "company": "신젠타",
                "usage": "물 20L에 10g을 희석하여 7일 간격 살포",
                "link": "https://search.shopping.naver.com/search/all?query=스위치입상수화제"
            },
            {
                "name": "로브랄 수화제",
                "company": "바이엘",
                "usage": "물 20L에 20g을 희석하여 살포",
                "link": "https://search.shopping.naver.com/search/all?query=로브랄수화제"
            },
            {
                "name": "캔투스 입상수화제",
                "company": "바이엘",
                "usage": "물 20L에 5g을 희석하여 예방 살포",
                "link": "https://search.shopping.naver.com/search/all?query=캔투스입상수화제"
            }
        ]
    },
    "Leaf spot": {
        "name_kr": "점무늬병",
        "name_en": "Leaf Spot",
        "symptoms": "잎에 작은 자주색 또는 갈색 반점이 생기고, 점차 확대되어 잎이 누렇게 마릅니다.",
        "cause": "Mycosphaerella fragariae 곰팡이에 의해 발생하며, 잎에 물방울이 맺힐 때 감염됩니다.",
        "prevention": "이병 잎을 제거하고, 물이 잎에 튀지 않도록 점적관수를 합니다.",
        "medicines": [
            {
                "name": "다코닐 수화제",
                "company": "경농",
                "usage": "물 20L에 20g을 희석하여 10일 간격 살포",
                "link": "https://search.shopping.naver.com/search/all?query=다코닐수화제"
            },
            {
                "name": "벨리스플러스 입상수화제",
                "company": "바스프",
                "usage": "물 20L에 10g을 희석하여 살포",
                "link": "https://search.shopping.naver.com/search/all?query=벨리스플러스"
            },
            {
                "name": "미리카트 액상수화제",
                "company": "경농",
                "usage": "물 20L에 10ml를 희석하여 예방 살포",
                "link": "https://search.shopping.naver.com/search/all?query=미리카트액상수화제"
            }
        ]
    },
    "Powdery mildew": {
        "name_kr": "흰가루병",
        "name_en": "Powdery Mildew",
        "symptoms": "잎 표면에 흰색 가루 같은 곰팡이가 퍼지며, 잎이 오그라들고 생육이 저해됩니다.",
        "cause": "Sphaerotheca macularis 곰팡이에 의해 발생하며, 건조하고 온도가 높을 때 번집니다.",
        "prevention": "적절한 습도 유지, 질소 과다 시비 금지, 통풍 개선",
        "medicines": [
            {
                "name": "테라코 입상수화제",
                "company": "경농",
                "usage": "물 20L에 5g을 희석하여 7일 간격 살포",
                "link": "https://search.shopping.naver.com/search/all?query=테라코입상수화제"
            },
            {
                "name": "푸르겐 수화제",
                "company": "동방아그로",
                "usage": "물 20L에 10g을 희석하여 살포",
                "link": "https://search.shopping.naver.com/search/all?query=푸르겐수화제"
            },
            {
                "name": "칸투스 입상수화제",
                "company": "바이엘",
                "usage": "물 20L에 10g을 희석하여 예방 살포",
                "link": "https://search.shopping.naver.com/search/all?query=칸투스입상수화제"
            }
        ]
    },
    "0": {
        "name_kr": "정상 (검출 오류 가능)",
        "name_en": "Normal or Background",
        "symptoms": "병징이 보이지 않거나 배경으로 판단됩니다.",
        "cause": "해당 없음",
        "prevention": "정기적인 관찰 및 예방적 관리를 계속하세요.",
        "medicines": []
    },
    "stawberry": {
        "name_kr": "정상 딸기",
        "name_en": "Healthy Strawberry",
        "symptoms": "건강한 상태의 딸기입니다.",
        "cause": "해당 없음",
        "prevention": "현재 상태를 유지하며 정기적인 관리를 계속하세요.",
        "medicines": []
    },
    "stawberry_1": {
        "name_kr": "정상 딸기",
        "name_en": "Healthy Strawberry",
        "symptoms": "건강한 상태의 딸기입니다.",
        "cause": "해당 없음",
        "prevention": "현재 상태를 유지하며 정기적인 관리를 계속하세요.",
        "medicines": []
    }
}


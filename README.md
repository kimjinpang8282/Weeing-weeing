# 🍓 딸기 병 분류 플랫폼

Roboflow AI 모델을 활용한 딸기 질병 자동 진단 및 치료제 추천 웹 플랫폼

## 기능

- ✅ 이미지 업로드 및 자동 병 분류
- ✅ 6가지 딸기 질병 탐지
  - 모무늬병 (Angular leaf spot)
  - 탄저병 (Anthracnose)
  - 시들음병 (Fusarium wilt)
  - 잿빛곰팡이병 (Gray mold)
  - 점무늬병 (Leaf spot)
  - 흰가루병 (Powdery mildew)
- ✅ 병 정보 및 원인 설명
- ✅ 치료제 추천 및 구매 링크 제공
- ✅ 분석 히스토리 관리

## 설치 방법

### 1. 필수 패키지 설치

```bash
pip install -r requirements.txt
```

### 2. 실행

```bash
streamlit run app.py
```

### 3. 브라우저에서 접속

자동으로 브라우저가 열리며, `http://localhost:8501`에서 접근 가능합니다.

## 사용 방법

1. 왼쪽 사이드바에서 신뢰도 임계값 조정 (기본: 50%)
2. 딸기 이미지 업로드 (JPG, PNG)
3. "병 분석하기" 버튼 클릭
4. 분석 결과 확인
5. 추천 치료제 및 구매 링크 확인

## 프로젝트 구조

```
Weeing-weeing/
├── app.py              # Streamlit 메인 앱
├── disease_info.py     # 병 정보 및 약품 데이터
├── requirements.txt    # 필요 패키지
└── README.md          # 문서
```

## 기술 스택

- **Frontend**: Streamlit
- **AI Model**: Roboflow (YOLOv8)
- **Image Processing**: Pillow, OpenCV
- **Python**: 3.8+

## Roboflow 모델 정보

- **Workspace**: weeing-weeing
- **Project**: weeing-weeing
- **Version**: 1
- **Model**: YOLOv8

## 주의사항

⚠️ 본 플랫폼의 진단 결과는 참고용이며, 정확한 진단 및 처방은 농업 기술 센터나 전문가와 상담하시기 바랍니다.

## 향후 개발 계획

- [ ] 동영상 분석 기능 추가
- [ ] 실시간 웹캠 분석
- [ ] 사용자 계정 및 히스토리 DB 저장
- [ ] 모바일 앱 개발
- [ ] 통계 및 분석 대시보드

## 라이선스

MIT License

## 문의

문제가 발생하거나 문의사항이 있으시면 Issue를 생성해주세요.

import streamlit as st
from PIL import Image
import numpy as np
import cv2
import os
from disease_info import DISEASE_INFO

# 페이지 설정
st.set_page_config(
    page_title="딸기 병 분류 플랫폼",
    page_icon="🍓",
    layout="wide"
)

# 세션 상태 초기화
if 'model' not in st.session_state:
    st.session_state.model = None
if 'history' not in st.session_state:
    st.session_state.history = []

# YOLOv8 모델 로드 (로컬 파일)
@st.cache_resource
def load_model():
    try:
        from ultralytics import YOLO
        
        # 프로젝트 폴더의 모델 경로
        model_path = os.path.join(os.path.dirname(__file__), "weights", "best.pt")
        
        if not os.path.exists(model_path):
            # weights 폴더에 없으면 루트에서 찾기
            model_path = os.path.join(os.path.dirname(__file__), "best.pt")
        
        # YOLOv8 모델 로드
        model = YOLO(model_path)
        
        # 클래스 이름 (Roboflow 프로젝트에서 확인한 것)
        class_names = [
            "0",
            "Angular leaf spot",
            "Anthracnose",
            "Fusarium wilt",
            "Gray mold",
            "Leaf spot",
            "Powdery mildew",
            "stawberry",
            "stawberry_1"
        ]
        
        return model, class_names, model_path
    except Exception as e:
        st.error(f"모델 로드 실패: {e}")
        import traceback
        st.code(traceback.format_exc())
        return None, None, None

# 이미지 분석 함수
def analyze_image(image, model, class_names, confidence_threshold=50):
    """이미지를 분석하고 결과 반환"""
    # PIL 이미지를 numpy array로 변환
    img_array = np.array(image)
    
    # YOLOv8 추론
    results = model(img_array, conf=confidence_threshold/100.0)
    
    # 결과를 Roboflow 형식으로 변환
    predictions = []
    for result in results:
        boxes = result.boxes
        for box in boxes:
            x1, y1, x2, y2 = box.xyxy[0].cpu().numpy()
            conf = float(box.conf[0].cpu().numpy())
            cls = int(box.cls[0].cpu().numpy())
            
            # 중심점과 너비/높이 계산
            x_center = (x1 + x2) / 2
            y_center = (y1 + y2) / 2
            width = x2 - x1
            height = y2 - y1
            
            predictions.append({
                'x': float(x_center),
                'y': float(y_center),
                'width': float(width),
                'height': float(height),
                'confidence': conf * 100,
                'class': class_names[cls] if cls < len(class_names) else str(cls)
            })
    
    return {'predictions': predictions}

# 결과 시각화
def draw_predictions(image, predictions):
    """예측 결과를 이미지에 그리기"""
    img_array = np.array(image)
    img_bgr = cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR)
    
    for pred in predictions:
        x = int(pred['x'] - pred['width'] / 2)
        y = int(pred['y'] - pred['height'] / 2)
        w = int(pred['width'])
        h = int(pred['height'])
        
        # 바운딩 박스 그리기
        cv2.rectangle(img_bgr, (x, y), (x + w, y + h), (0, 255, 0), 3)
        
        # 라벨 텍스트
        label = f"{pred['class']} ({pred['confidence']:.1f}%)"
        cv2.putText(img_bgr, label, (x, y - 10), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
    
    return cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

# 메인 UI
st.title("🍓 딸기 병 분류 플랫폼")
st.markdown("### YOLOv8 AI로 딸기 질병을 자동 진단하고 치료제를 추천받으세요")

# 사이드바
with st.sidebar:
    st.header("⚙️ 설정")
    confidence = st.slider("신뢰도 임계값 (%)", 0, 100, 50, 5)
    st.markdown("---")
    st.markdown("### 📊 분석 가능한 병")
    st.markdown("""
    - ✅ 모무늬병 (Angular leaf spot)
    - ✅ 탄저병 (Anthracnose)
    - ✅ 시들음병 (Fusarium wilt)
    - ✅ 잿빛곰팡이병 (Gray mold)
    - ✅ 점무늬병 (Leaf spot)
    - ✅ 흰가루병 (Powdery mildew)
    """)

# 모델 로드
if st.session_state.model is None:
    with st.spinner("🔄 AI 모델을 불러오는 중..."):
        model, class_names, model_location = load_model()
        if model is not None:
            st.session_state.model = model
            st.session_state.class_names = class_names
            st.session_state.model_location = model_location

if st.session_state.model is None:
    st.error("❌ 모델을 불러올 수 없습니다. best.pt 파일이 있는지 확인해주세요.")
    st.stop()

st.success("✅ AI 모델 준비 완료!")
st.info(f"📁 모델 위치: {st.session_state.model_location}")

# 파일 업로드
st.markdown("### 📤 이미지 업로드")
uploaded_file = st.file_uploader(
    "딸기 이미지를 선택하세요 (JPG, PNG)",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:
    # 이미지 로드
    image = Image.open(uploaded_file)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 📷 원본 이미지")
        st.image(image, use_column_width=True)
    
    # 분석 버튼
    if st.button("🔍 병 분석하기", type="primary"):
        with st.spinner("🧠 AI가 이미지를 분석하는 중..."):
            try:
                # 분석 실행
                result = analyze_image(
                    image, 
                    st.session_state.model, 
                    st.session_state.class_names,
                    confidence
                )
                predictions = result.get('predictions', [])
                
                if len(predictions) == 0:
                    st.warning("⚠️ 검출된 병징이 없습니다. 신뢰도 임계값을 낮춰보세요.")
                else:
                    # 결과 이미지 생성
                    result_image = draw_predictions(image.copy(), predictions)
                    
                    with col2:
                        st.markdown("#### 🎯 분석 결과")
                        st.image(result_image, use_column_width=True)
                    
                    # 검출된 병 정보 표시
                    st.markdown("### 🏥 검출된 질병 정보")
                    
                    # 중복 제거를 위한 set
                    detected_diseases = set([pred['class'] for pred in predictions])
                    
                    for disease_class in detected_diseases:
                        # 해당 클래스의 예측들 필터링
                        class_predictions = [p for p in predictions if p['class'] == disease_class]
                        avg_confidence = sum([p['confidence'] for p in class_predictions]) / len(class_predictions)
                        
                        disease_data = DISEASE_INFO.get(disease_class, None)
                        
                        if disease_data:
                            with st.expander(f"🔴 {disease_data['name_kr']} ({disease_data['name_en']}) - 신뢰도: {avg_confidence:.1f}%", expanded=True):
                                st.markdown(f"**📋 증상:** {disease_data['symptoms']}")
                                st.markdown(f"**🔬 원인:** {disease_data['cause']}")
                                st.markdown(f"**🛡️ 예방법:** {disease_data['prevention']}")
                                
                                if disease_data['medicines']:
                                    st.markdown("### 💊 추천 치료제")
                                    
                                    for idx, medicine in enumerate(disease_data['medicines'], 1):
                                        st.markdown(f"**{idx}. {medicine['name']}** ({medicine['company']})")
                                        st.markdown(f"   - 사용법: {medicine['usage']}")
                                        st.markdown(f"   - [🛒 구매하기]({medicine['link']})")
                                        st.markdown("")
                                else:
                                    st.info("정상 상태입니다. 추가 조치가 필요하지 않습니다.")
                    
                    # 히스토리에 추가
                    st.session_state.history.insert(0, {
                        'image': image,
                        'predictions': predictions,
                        'diseases': list(detected_diseases)
                    })
                    
                    # 히스토리 최대 10개 유지
                    if len(st.session_state.history) > 10:
                        st.session_state.history = st.session_state.history[:10]
                
            except Exception as e:
                st.error(f"❌ 분석 중 오류 발생: {e}")
                import traceback
                st.code(traceback.format_exc())

# 히스토리 표시
if st.session_state.history:
    st.markdown("---")
    st.markdown("### 📜 최근 분석 히스토리")
    
    cols = st.columns(5)
    for idx, record in enumerate(st.session_state.history[:5]):
        with cols[idx]:
            st.image(record['image'], use_column_width=True)
            st.caption(f"검출: {', '.join([DISEASE_INFO[d]['name_kr'] for d in record['diseases']])}")

# 푸터
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: gray;'>
    <p>🍓 딸기 병 분류 플랫폼 v1.0 | Powered by YOLOv8 & Streamlit</p>
    <p>⚠️ 본 진단은 참고용이며, 정확한 진단은 전문가와 상담하세요.</p>
</div>
""", unsafe_allow_html=True)

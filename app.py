import streamlit as st
import random
from datetime import datetime, date

# ==========================================
# 1. 系統設定
# ==========================================
st.set_page_config(
    page_title="Awos 農場 🌿 導覽體驗與好物市集",
    page_icon="🚜",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ==========================================
# 2. CSS 美學 (大地生機風格 & 轉換率防禦架構)
# ==========================================
st.markdown("""
    <style>
    /* 1. 強制全站背景為米膚色，字體為深咖啡色 (營造有機農場溫潤感) */
    .stApp {
        background-color: #FDF5E6;
        font-family: "Microsoft JhengHei", sans-serif;
        color: #3E2723 !important;
    }
    
    p, div, span, h1, h2, h3, h4, h5, h6, label, .stMarkdown {
        color: #3E2723 !important;
    }

    /* === 3. 核心修復：強制輸入框與選單在深色模式下維持白底黑字 === */
    div[data-baseweb="select"] > div, 
    div[data-baseweb="input"] > div, 
    div[data-baseweb="base-input"] {
        background-color: #ffffff !important; 
        border: 1px solid #A1887F !important;
        color: #3E2723 !important; 
    }
    input { color: #3E2723 !important; }
    div[data-baseweb="select"] span { color: #3E2723 !important; }
    ul[data-baseweb="menu"] { background-color: #ffffff !important; }
    li[data-baseweb="option"] { color: #3E2723 !important; }
    svg { fill: #3E2723 !important; color: #3E2723 !important; }

    /* === 4. 特別加強：日期選單高亮 === */
    div[data-testid="stDateInput"] > label {
        color: #2E7D32 !important; /* 森林綠 */
        font-size: 20px !important;
        font-weight: 900 !important;
        margin-bottom: 10px !important;
        display: block;
    }
    div[data-testid="stDateInput"] div[data-baseweb="input"] {
        border: 2px solid #4CAF50 !important; 
        background-color: #E8F5E9 !important;
        border-radius: 10px !important;
    }

    /* 隱藏官方元件 */
    header {visibility: hidden;}
    footer {display: none !important;}
    
    /* 標題區 (農場風格漸層：大地棕 到 草綠) */
    .header-box {
        background: linear-gradient(135deg, #6D4C41 0%, #43A047 100%);
        padding: 30px 20px;
        border-radius: 0 0 30px 30px;
        color: white !important;
        text-align: center;
        margin-bottom: 25px;
        box-shadow: 0 4px 15px rgba(67, 160, 71, 0.4);
        margin-top: -60px;
    }
    .header-box h1, .header-box div, .header-box span { color: white !important; }
    .header-title { font-size: 28px; font-weight: bold; letter-spacing: 2px; }
    
    /* 卡片模組 */
    .section-card {
        background: rgba(255, 255, 255, 0.9);
        border-radius: 15px;
        padding: 20px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05);
        border-top: 4px solid #8D6E63;
        margin-bottom: 20px;
    }
    
    /* 按鈕 */
    .stButton>button {
        width: 100%;
        background-color: #E64A19; /* 溫暖的磚紅色，高轉換率 */
        color: white !important;
        border-radius: 50px;
        border: none;
        padding: 12px 0;
        font-weight: bold;
        transition: 0.3s;
        font-size: 18px;
    }
    
    /* 導覽時間軸 */
    .tour-item {
        border-left: 3px solid #66BB6A;
        padding-left: 15px;
        margin-bottom: 15px;
        position: relative;
    }
    .tour-item::before {
        content: '🌿';
        position: absolute;
        left: -14px;
        top: 0;
        background: #FDF5E6;
    }
    .tour-title { font-weight: bold; color: #2E7D32 !important; font-size: 18px; }
    .tour-tag { font-size: 12px; background: #E8F5E9; color: #2E7D32 !important; padding: 2px 8px; border-radius: 10px; margin-right: 5px; }
    
    /* 商品網格卡片 */
    .product-card {
        background: #FFFFFF;
        border: 1px solid #D7CCC8;
        padding: 15px;
        border-radius: 10px;
        margin-bottom: 15px;
        text-align: center;
        transition: 0.3s;
    }
    .product-card:hover { border-color: #FF7043; box-shadow: 0 4px 8px rgba(255,112,67,0.2); }
    .product-price { font-size: 18px; color: #D84315 !important; font-weight: bold; margin: 5px 0; }
    .product-tag { font-size: 11px; background: #FFCCBC; color: #D84315 !important; padding: 2px 6px; border-radius: 8px; }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 3. 核心資料庫 (導覽 與 衍生商品)
# ==========================================

# 導覽體驗資料庫
tours_db = [
    {"name": "Awos 漫步生態導覽", "type": "入門導覽", "duration": "1.5小時", "fee": "$300", "desc": "由在地嚮導帶領，走入友善農法田野，認識農場的共生生態系。"},
    {"name": "大地餐桌與香草採摘", "type": "深度體驗", "duration": "2.5小時", "fee": "$850", "desc": "親自採摘當季無毒香草，並在田野間享用從產地到餐桌的農莊風味餐。"},
    {"name": "職人農莊咖啡烘焙 DIY", "type": "手作活動", "duration": "2小時", "fee": "$600", "desc": "從挑豆、認識咖啡果實到親手烘焙，帶回一包專屬於你的 Awos 咖啡。"},
    {"name": "果物釀造工坊 (季節限定)", "type": "手作活動", "duration": "2小時", "fee": "$500", "desc": "將農場採摘的當季水果，手工熬煮成天然果醬或釀製果醋。"},
    {"name": "星空夜觀秘境探索", "type": "夜間限定", "duration": "2小時", "fee": "$400", "desc": "夜間走入農場，探索夜行性生物與無光害的滿天星斗。"}
]

# 衍生商品資料庫
products_db = [
    {"name": "Awos 有機冷壓初榨茶油", "category": "健康油品", "price": 880, "icon": "🫒", "desc": "傳承古法冷壓，保留最高營養價值，拌麵拌菜皆宜。"},
    {"name": "Awos 莊園級精品咖啡豆", "category": "手作飲品", "price": 550, "icon": "☕", "desc": "自家農場友善種植，淺焙帶有花果香氣，深焙濃郁回甘。"},
    {"name": "純天然香草精油皂禮盒", "category": "生活沐浴", "price": 600, "icon": "🧼", "desc": "萃取農場無毒香草精華，溫和清潔不傷肌膚，友善環境。"},
    {"name": "當季手工無添加果醬", "category": "天然手作", "price": 280, "icon": "🍓", "desc": "採用農場『醜小鴨水果』慢火熬煮，封存大地的甜美滋味。"},
    {"name": "Awos 原木手工食器組", "category": "文創工藝", "price": 450, "icon": "🥄", "desc": "利用農場修枝下來的木材手工打磨，實踐循環經濟與永續理念。"},
    {"name": "天然驅蚊艾草香椎", "category": "生活沐浴", "price": 250, "icon": "🌿", "desc": "純天然艾草與香草手作揉製，露營與居家天然驅蚊首選。"}
]

# ==========================================
# 4. 邏輯核心：推薦系統
# ==========================================
def recommend_tours(group):
    # 根據客群動態推薦不同導覽
    if group == "親子家庭 (帶小孩)":
        return [t for t in tours_db if t['type'] in ["入門導覽", "手作活動"]]
    elif group == "情侶/閨蜜出遊":
        return [t for t in tours_db if t['name'] in ["大地餐桌與香草採摘", "職人農莊咖啡烘焙 DIY", "星空夜觀秘境探索"]]
    else:
        return tours_db[:3] # 預設推薦前三個

# ==========================================
# 5. 頁面內容
# ==========================================
st.markdown("""
    <div class="header-box">
        <div class="header-title">🚜 Awos 農場</div>
        <div style="font-size: 16px; margin-top: 5px;">探索大地生態 • 品味永續農創</div>
    </div>
""", unsafe_allow_html=True)

# --- 區塊 1：導覽預約模組 ---
st.markdown("### 🗓️ 規劃您的農場體驗")
with st.container():
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        visit_date = st.date_input("📅 預計到訪日期", value=date.today())
    with col2:
        group = st.selectbox("👥 出遊型態", ["親友/三五好友", "親子家庭 (帶小孩)", "情侶/閨蜜出遊", "一人放空散心"])
    
    if st.button("🔍 尋找適合的導覽活動"):
        st.session_state['show_tours'] = True
    st.markdown('</div>', unsafe_allow_html=True)

if st.session_state.get('show_tours'):
    st.markdown(f"**為「{group}」推薦的專屬體驗：**")
    recs = recommend_tours(group)
    for tour in recs:
        st.markdown(f"""
        <div class="tour-item">
            <div class="tour-title">{tour['name']}</div>
            <div style="margin: 4px 0;">
                <span class="tour-tag">⏱️ {tour['duration']}</span>
                <span class="tour-tag">💵 {tour['fee']}/人</span>
            </div>
            <div style="font-size: 14px; color: #555;">{tour['desc']}</div>
        </div>
        """, unsafe_allow_html=True)

# --- 區塊 2：農創衍生商品市集 ---
st.markdown("---")
st.markdown("### 🛍️ Awos 衍生好物市集")
st.markdown("<p style='font-size:14px; color:#795548;'>將農場的純淨與美好，打包帶回日常生活中。</p>", unsafe_allow_html=True)

# 商品分類 Filter
category_filter = st.radio("商品分類", ["全部顯示", "健康油品/飲品", "生活沐浴/文創"], horizontal=True)

filtered_products = products_db
if category_filter == "健康油品/飲品":
    filtered_products = [p for p in products_db if p['category'] in ["健康油品", "手作飲品", "天然手作"]]
elif category_filter == "生活沐浴/文創":
    filtered_products = [p for p in products_db if p['category'] in ["生活沐浴", "文創工藝"]]

# 使用雙欄網格顯示商品 (優化視覺轉換)
cols = st.columns(2)
for i, product in enumerate(filtered_products):
    with cols[i % 2]:
        st.markdown(f"""
        <div class="product-card">
            <div style="font-size: 30px;">{product['icon']}</div>
            <div style="font-weight: bold; color: #4E342E; margin-top: 5px; font-size:15px;">{product['name']}</div>
            <div class="product-price">NT$ {product['price']}</div>
            <span class="product-tag">{product['category']}</span>
            <div style="font-size: 12px; color: #757575; margin-top: 8px; line-height:1.4;">{product['desc']}</div>
        </div>
        """, unsafe_allow_html=True)

# 頁尾：導引購買與聯絡
st.markdown("""
    <div style="text-align:center; margin-top:30px; padding:20px; background-color:#EFEBE9; border-radius:10px;">
        <h4 style="color:#5D4037 !important;">想預約導覽或購買商品嗎？</h4>
        <p style="font-size:14px; color:#5D4037;">請透過 Awos 農場官方 Line 或致電聯繫我們，將有專人為您服務。</p>
        <button style="background-color:#4CAF50; color:white; border:none; padding:10px 20px; border-radius:5px; font-weight:bold;">🟢 加入官方 LINE 預約</button>
    </div>
""", unsafe_allow_html=True)

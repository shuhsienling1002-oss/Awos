import streamlit as st
import random
from datetime import datetime, date

# ==========================================
# 1. 系統設定 (AWOS 白玉蝸牛專屬配置)
# ==========================================
st.set_page_config(
    page_title="AWOS 宏成蝸牛農場 | 台東長濱頂級白玉蝸牛",
    page_icon="🐌",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ==========================================
# 2. CSS 美學 (長濱海岸湛藍 x 白玉蝸牛溫潤白)
# ==========================================
st.markdown("""
    <style>
    /* 1. 全站背景：象徵白玉蝸牛殼的溫潤乳白色 */
    .stApp {
        background-color: #FDFBF7;
        font-family: "Microsoft JhengHei", sans-serif;
        color: #3E2723 !important;
    }
    
    p, div, span, h1, h2, h3, h4, h5, h6, label, .stMarkdown {
        color: #3E2723 !important;
    }

    /* === 3. 深色模式防禦：強制輸入框白底黑字 === */
    div[data-baseweb="select"] > div, 
    div[data-baseweb="input"] > div, 
    div[data-baseweb="base-input"] {
        background-color: #ffffff !important; 
        border: 1px solid #BCAAA4 !important;
        color: #3E2723 !important; 
    }
    input { color: #3E2723 !important; }
    div[data-baseweb="select"] span { color: #3E2723 !important; }
    ul[data-baseweb="menu"] { background-color: #ffffff !important; }
    li[data-baseweb="option"] { color: #3E2723 !important; }
    svg { fill: #3E2723 !important; color: #3E2723 !important; }

    /* === 4. 日期選單高亮 (太平洋深海藍) === */
    div[data-testid="stDateInput"] > label {
        color: #0277BD !important; 
        font-size: 20px !important;
        font-weight: 900 !important;
        margin-bottom: 10px !important;
        display: block;
    }
    div[data-testid="stDateInput"] div[data-baseweb="input"] {
        border: 2px solid #0288D1 !important; 
        background-color: #E1F5FE !important;
        border-radius: 10px !important;
    }

    /* 隱藏官方元件 */
    header {visibility: hidden;}
    footer {display: none !important;}
    
    /* 標題區：長濱海岸星空 到 大地土壤的漸層 */
    .header-box {
        background: linear-gradient(135deg, #01579B 0%, #4E342E 100%);
        padding: 35px 20px;
        border-radius: 0 0 30px 30px;
        color: white !important;
        text-align: center;
        margin-bottom: 25px;
        box-shadow: 0 4px 15px rgba(1, 87, 155, 0.4);
        margin-top: -60px;
    }
    .header-box h1, .header-box div, .header-box span { color: white !important; }
    .header-title { font-size: 32px; font-weight: bold; letter-spacing: 3px; margin-bottom: 5px;}
    .header-subtitle { font-size: 15px; color: #E0E0E0 !important; font-style: italic; }
    
    /* 卡片模組 */
    .section-card {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 15px;
        padding: 20px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.06);
        border-top: 4px solid #0288D1;
        margin-bottom: 20px;
    }
    
    /* 轉換率按鈕 (溫暖法式芥末黃，吸引食慾與點擊) */
    .stButton>button {
        width: 100%;
        background-color: #F57F17; 
        color: white !important;
        border-radius: 50px;
        border: none;
        padding: 12px 0;
        font-weight: bold;
        transition: 0.3s;
        font-size: 18px;
        box-shadow: 0 4px 6px rgba(245, 127, 23, 0.3);
    }
    .stButton>button:hover { background-color: #E65100; transform: translateY(-2px); }
    
    /* 導覽時間軸 */
    .tour-item {
        border-left: 4px solid #8D6E63;
        padding-left: 15px;
        margin-bottom: 18px;
        position: relative;
    }
    .tour-item::before {
        content: '🐌';
        position: absolute;
        left: -15px;
        top: 0;
        background: #FDFBF7;
    }
    .tour-title { font-weight: bold; color: #4E342E !important; font-size: 19px; }
    .tour-tag { font-size: 12px; background: #EFEBE9; color: #5D4037 !important; padding: 3px 10px; border-radius: 12px; margin-right: 6px; font-weight: bold;}
    
    /* 商品網格卡片 */
    .product-card {
        background: #FFFFFF;
        border: 1px solid #E0E0E0;
        padding: 18px;
        border-radius: 12px;
        margin-bottom: 15px;
        text-align: center;
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }
    .product-card:hover { border-color: #0288D1; box-shadow: 0 8px 15px rgba(2,136,209,0.15); transform: translateY(-3px);}
    .product-price { font-size: 20px; color: #C62828 !important; font-weight: 900; margin: 8px 0; }
    .product-tag { font-size: 11px; background: #E1F5FE; color: #0277BD !important; padding: 3px 8px; border-radius: 8px; font-weight: bold;}
    .badge { position: absolute; top: 10px; right: -25px; background: #D32F2F; color: white !important; font-size: 10px; font-weight: bold; padding: 3px 30px; transform: rotate(45deg); }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 3. 核心資料庫 (真實 AWOS 資源：導覽與農創)
# ==========================================

# 導覽體驗資料庫 (夜間生態與食農教育)
tours_db = [
    {"name": "白玉蝸牛夜間生態探索", "type": "生態尋寶", "duration": "1.5小時", "fee": "$350", "desc": "蝸牛是夜行性動物！戴上頭燈，跟著農場主人在長濱星空下尋找白玉蝸牛的蹤跡。"},
    {"name": "田間採集與餵食體驗", "type": "親子互動", "duration": "1小時", "fee": "$250", "desc": "親自採摘農場種植的無毒地瓜葉，體驗近距離餵食蝸牛的療癒時光，適合全家大小。"},
    {"name": "產地到餐桌：法式蝸牛品嚐", "type": "頂級食農", "duration": "2小時", "fee": "$880", "desc": "導覽後，由主廚現場料理頂級白玉蝸牛，品嚐舒肥玉螺沙拉與法式香蒜烤蝸牛。"},
    {"name": "蝸牛殼彩繪手作坊", "type": "文創 DIY", "duration": "1.5小時", "fee": "$300", "desc": "將廢棄的白玉蝸牛殼回收再利用，發揮創意彩繪，製作成獨一無二的長濱紀念品。"}
]

# 衍生商品資料庫 (頂級食材與生技面膜)
products_db = [
    {"name": "頂級白玉蝸牛冷凍肉", "category": "星級食材", "price": 680, "icon": "🥩", "desc": "米其林餐廳指定使用！已手工去殼處理，肉質Ｑ彈鮮甜，適合乾煎或法式烤製。", "hot": True},
    {"name": "法式香蒜奶油蝸牛組", "category": "即食料理", "price": 850, "icon": "🧄", "desc": "內含頂級蝸牛肉與特調法式香蒜奶油醬，在家用烤箱10分鐘即享星級美味。", "hot": False},
    {"name": "舒肥玉螺沙拉獨享包", "category": "輕食首選", "price": 280, "icon": "🥗", "desc": "低溫舒肥處理，保留最高蛋白質，解凍後搭配生菜即可上桌的健康輕食。", "hot": False},
    {"name": "AWOS 蝸牛潛艇堡套組", "category": "即食料理", "price": 350, "icon": "🥖", "desc": "長濱必吃特色美食！滿滿的玉螺肉搭配特製醬汁與軟法麵包。", "hot": True},
    {"name": "極致修護保濕蝸牛面膜", "category": "生技保養", "price": 499, "icon": "🧴", "desc": "萃取白玉蝸牛高濃度黏液精華，富含膠原蛋白與尿囊素，深層修護曬後肌膚。", "hot": True},
    {"name": "蝸牛原液修護精華露", "category": "生技保養", "price": 1280, "icon": "✨", "desc": "高純度原液，吸收迅速不黏膩，鎖水撫平細紋，大自然的頂級抗老秘密。", "hot": False}
]

# ==========================================
# 4. 邏輯核心：精準推薦系統
# ==========================================
def recommend_tours(group):
    if group == "親子家庭 (帶小孩)":
        return [t for t in tours_db if t['name'] in ["田間採集與餵食體驗", "蝸牛殼彩繪手作坊"]]
    elif group == "老饕/情侶約會":
        return [t for t in tours_db if t['name'] in ["產地到餐桌：法式蝸牛品嚐", "白玉蝸牛夜間生態探索"]]
    elif group == "深度體驗玩家":
        return [t for t in tours_db if t['type'] in ["生態尋寶", "頂級食農"]]
    else:
        return tours_db[:3]

# ==========================================
# 5. 頁面內容
# ==========================================
st.markdown("""
    <div class="header-box">
        <div class="header-title">🐌 宏成蝸牛 AWOS 農場</div>
        <div class="header-subtitle">長濱純淨水土培育 • 台灣米其林級白玉蝸牛</div>
    </div>
""", unsafe_allow_html=True)

# --- 區塊 1：導覽預約模組 ---
st.markdown("### 🌿 預約產地生態體驗")
with st.container():
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        visit_date = st.date_input("📅 預計到訪長濱日期", value=date.today())
    with col2:
        group = st.selectbox("👥 您的同行旅伴", ["老饕/情侶約會", "親子家庭 (帶小孩)", "深度體驗玩家", "一人慢遊"])
    
    if st.button("🔍 尋找適合的蝸牛體驗"):
        st.session_state['show_tours'] = True
    st.markdown('</div>', unsafe_allow_html=True)

if st.session_state.get('show_tours'):
    st.markdown(f"**為「{group}」推薦的專屬導覽：**")
    recs = recommend_tours(group)
    for tour in recs:
        st.markdown(f"""
        <div class="tour-item">
            <div class="tour-title">{tour['name']}</div>
            <div style="margin: 6px 0;">
                <span class="tour-tag">⏱️ {tour['duration']}</span>
                <span class="tour-tag">💰 {tour['fee']}/人</span>
                <span class="tour-tag" style="background:#E1F5FE; color:#0277BD!important;">{tour['type']}</span>
            </div>
            <div style="font-size: 14px; color: #555; line-height: 1.5;">{tour['desc']}</div>
        </div>
        """, unsafe_allow_html=True)

# --- 區塊 2：蝸牛生技與農創市集 ---
st.markdown("---")
st.markdown("### 🛍️ AWOS 頂級農創市集")
st.markdown("<p style='font-size:14px; color:#5D4037;'>從米其林級食材到極致修護保養，把長濱的精華帶回家。</p>", unsafe_allow_html=True)

# 商品分類 Filter
category_filter = st.radio("商品分類", ["全部", "🍽️ 星級食材/即食", "💧 生技保養品"], horizontal=True)

filtered_products = products_db
if category_filter == "🍽️ 星級食材/即食":
    filtered_products = [p for p in products_db if p['category'] in ["星級食材", "即食料理", "輕食首選"]]
elif category_filter == "💧 生技保養品":
    filtered_products = [p for p in products_db if p['category'] == "生技保養"]

# 雙欄網格顯示 (修復版：將 badge_html 與商品圖示放在同一行，防止 Markdown 解析中斷)
cols = st.columns(2)
for i, product in enumerate(filtered_products):
    with cols[i % 2]:
        badge_html = '<div class="badge">熱銷</div>' if product.get('hot') else ''
        st.markdown(f"""
        <div class="product-card">
            {badge_html}<div style="font-size: 35px; margin-bottom:10px;">{product['icon']}</div>
            <span class="product-tag">{product['category']}</span>
            <div style="font-weight: 900; color: #3E2723; margin-top: 10px; font-size:16px;">{product['name']}</div>
            <div class="product-price">NT$ {product['price']}</div>
            <div style="font-size: 13px; color: #757575; margin-top: 8px; line-height:1.4;">{product['desc']}</div>
        </div>
        """, unsafe_allow_html=True)

# --- 頁尾：導引購買與聯絡 ---
st.markdown("""
    <div style="text-align:center; margin-top:40px; padding:25px; background: linear-gradient(180deg, #FDFBF7 0%, #EFEBE9 100%); border-radius:15px; border: 1px solid #D7CCC8;">
        <h4 style="color:#4E342E !important; font-weight:bold;">訂購食材 / 預約導覽</h4>
        <p style="font-size:14px; color:#5D4037; margin-bottom: 20px;">產地直銷，新鮮低溫宅配到府。歡迎餐廳主廚與團體洽詢。</p>
        <button style="background-color:#00C300; color:white; border:none; padding:12px 30px; border-radius:50px; font-weight:900; font-size: 16px; box-shadow: 0 4px 10px rgba(0, 195, 0, 0.3); cursor:pointer;">
            💬 加入官方 LINE 洽詢
        </button>
    </div>
""", unsafe_allow_html=True)

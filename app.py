import streamlit as st
import time
from datetime import datetime, date

# ==========================================
# 1. 系統設定 & 全域變數 (為手機版優化，改回 centered 佈局)
# ==========================================
st.set_page_config(
    page_title="Mayaw的店 | 阿美族頂級風土料理",
    page_icon="🌿",
    layout="centered", 
    initial_sidebar_state="collapsed"
)

# ==========================================
# 2. CSS 高對比清晰美學 & 手機版優化
# ==========================================
st.markdown("""
    <style>
    /* 強制全站純白底色與深黑字體 */
    .stApp { background-color: #FFFFFF !important; }
    p, span, div, h1, h2, h3, h4, h5, h6, label { 
        color: #1A1A1A !important; 
        font-family: "Microsoft JhengHei", sans-serif;
    }
    
    /* 隱藏預設的側邊欄展開按鈕，實現真正的單頁面 */
    [data-testid="collapsedControl"] { display: none !important; }
    section[data-testid="stSidebar"] { display: none !important; }

    /* 標題區漸層 (手機版縮小 padding) */
    .header-box {
        background: linear-gradient(135deg, #004D40 0%, #1B5E20 100%);
        padding: 30px 15px;
        border-radius: 15px;
        text-align: center;
        margin-bottom: 20px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.15);
    }
    .header-box h1 { color: #FFFFFF !important; font-size: 28px; letter-spacing: 3px; margin-bottom: 5px;}
    .header-box p { color: #E0F2F1 !important; font-size: 14px; font-weight: bold;}
    
    /* 卡片模組 */
    .card { 
        background-color: #F8F9FA !important; 
        border-radius: 12px; 
        padding: 20px; 
        box-shadow: 0 4px 8px rgba(0,0,0,0.05); 
        border: 1px solid #DEE2E6 !important;
        border-top: 5px solid #00695C !important; 
        margin-bottom: 20px; 
    }
    .warning-card { 
        background-color: #FFF3E0 !important; 
        border: 1px solid #FFE0B2 !important;
        border-top: 5px solid #D84315 !important; 
    }
    
    /* 按鈕優化 (適合手機點擊的大按鈕) */
    .stButton>button { 
        width: 100%; 
        background-color: #00695C !important; 
        color: #FFFFFF !important; 
        border-radius: 8px; 
        border: none; 
        padding: 15px 0; 
        font-weight: bold; 
        font-size: 18px;
        transition: 0.3s; 
    }
    .stButton>button:hover { background-color: #004D40 !important; }
    
    /* Streamlit Tabs 標籤頁樣式覆寫 */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        margin-bottom: 20px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        white-space: pre-wrap;
        background-color: #F1F3F4;
        border-radius: 8px 8px 0 0;
        padding: 10px 15px;
        font-weight: bold;
    }
    .stTabs [aria-selected="true"] {
        background-color: #004D40;
        color: white !important;
    }
    .stTabs [aria-selected="true"] p { color: white !important; }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 3. 核心資料庫
# ==========================================
ten_hearts_db = [
    {"name": "黃藤心", "trait": "先苦後甘", "desc": "富含鋅與鉀，高濃度多酚帶來極致苦味，需利用動物油脂包覆單寧轉化為悠長回甘。"},
    {"name": "林投心", "trait": "防禦與極限", "desc": "海岸線防風林植物，採集困難。其葉用於編織阿里鳳鳳(情人便當)，心部富含獨特纖維。"},
    {"name": "月桃心", "trait": "抗炎精油", "desc": "富含揮發性抗炎精油，散發熱帶雨林與生薑的天然辛香，常用於低溫燜烤驅邪。"},
    {"name": "鐵樹心", "trait": "致命與重生", "desc": "【警語】含有致命神經毒素。本餐廳具備實驗室級SOP，透過物理搗碎與活水連續浸泡提取純淨澱粉。"},
    {"name": "甘蔗心", "trait": "天然單醣", "desc": "阿美族湯頭「無味精堅持」的靈魂，釋放天然單醣與海鮮游離核苷酸產生完美梅納反應。"}
]

# ==========================================
# 4. 頂部主視覺 (全局顯示)
# ==========================================
st.markdown("""
    <div class="header-box">
        <h1>🌿 Mayaw 的店</h1>
        <p>吃草民族的生態智慧 • 阿美族風土 Fine Dining</p>
    </div>
""", unsafe_allow_html=True)

# ==========================================
# 5. 單一版面結構：使用 Tabs 整合三大功能
# ==========================================
tab1, tab2, tab3 = st.tabs(["🏠 預約單點", "💎 VIP客製", "🌱 產地圖鑑"])

# ------------------------------------------
# 模組 1：預約與單點 (Tab 1)
# ------------------------------------------
with tab1:
    st.markdown('<div class="card"><h3 style="color:#004D40!important;">⛰️ 預約主題饗宴</h3>', unsafe_allow_html=True)
    date_sel = st.date_input("📅 預計用餐日期", value=date.today())
    pax = st.number_input("👥 用餐人數", min_value=1, max_value=20, value=2)
    tour = st.selectbox("🍽️ 選擇主題套餐", [
        "野菜餐 (十心微生態饗宴) - $1,280", 
        "海洋餐 (潮間帶零綠葉禁忌) - $1,680", 
        "獵人餐 (荒野能量與發酵) - $1,080", 
        "巴歌浪餐 (流水與療癒) - $980"
    ])
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("確認預約", key="btn_reserve"):
        st.success(f"✅ 已成功為您預約 {date_sel} 共 {pax} 位之 {tour.split(' ')[0]}！")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="card"><h3 style="color:#004D40!important;">🥢 經典單點美饌</h3>', unsafe_allow_html=True)
    items = ["🍲 黃藤心豚骨慢燉醇湯 $380", "🥩 熟成 Siraw 佐刺蔥舒肥雞 $420", "🔥 800度蛇紋石水煮活鮮 $680", "🍙 林投葉編阿里鳳鳳 $250"]
    for item in items:
        st.markdown(f"<div style='margin-bottom:12px; font-size:16px; font-weight:bold; border-bottom:1px solid #EEE; padding-bottom:8px;'>{item}</div>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ------------------------------------------
# 模組 2：VIP 客製無菜單 (Tab 2)
# ------------------------------------------
with tab2:
    st.markdown('<div class="card" style="border-top-color: #311B92 !important;">', unsafe_allow_html=True)
    st.markdown("<h3 style='color:#311B92!important; margin-bottom:15px;'>🧠 構建味覺參數</h3>", unsafe_allow_html=True)
    st.markdown("<p style='font-size:14px; color:#555!important;'>滑動設定您的偏好，AI主廚將重組阿美族飲食DNA。</p>", unsafe_allow_html=True)
    
    # 手機版改為全垂直排列
    bitter_level = st.slider("🌿 苦味耐受度 (0=抗拒, 10=熱愛)", 0, 10, 5)
    ferment_level = st.slider("🥩 發酵接受度 (0=熟食, 10=生醃)", 0, 10, 5)
    sea_level = st.slider("🌊 海洋野味偏好 (0=純山林, 10=純海洋)", 0, 10, 5)
    courage_level = st.slider("🔥 食材冒險精神 (挑戰毒性降解)", 0, 10, 0)
    
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("✨ 生成專屬 Omakase 菜單", key="btn_omakase"):
        with st.spinner("AI 解析中..."):
            time.sleep(1.2)
            st.markdown("---")
            st.markdown("<h3 style='color:#311B92!important;'>📜 您的專屬無菜單</h3>", unsafe_allow_html=True)
            
            amuse_bouche = "月桃心低溫燜烤雞胸" if bitter_level < 5 else "冷萃黃藤心嫩芽佐天然海鹽"
            soup = "甘蔗心鮮魚清湯" if sea_level > 5 else "黃藤心豚骨醇湯"
            main_course = "黑潮鬼頭刀厚切鹽烤" if sea_level > 7 else ("12% 完美發酵熟成 Siraw" if ferment_level > 7 else "馬告香料烤山豬肉")
            special = "【極限料理】降解鐵樹心手作麻糬" if courage_level >= 8 else "紅糯米提拉米蘇"

            st.info(f"**【前菜】** {amuse_bouche}\n\n"
                    f"**【湯品】** {soup}\n\n"
                    f"**【主餐】** {main_course}\n\n"
                    f"**【甜點】** {special}")
            st.success("總廚 Mayaw 已接收！定價：NT$ 2,580 / 人")
    st.markdown('</div>', unsafe_allow_html=True)

# ------------------------------------------
# 模組 3：產地與十心菜圖鑑 (Tab 3)
# ------------------------------------------
with tab3:
    st.markdown('<div class="card warning-card">', unsafe_allow_html=True)
    st.markdown("<h3 style='color:#D84315!important; margin-bottom:10px;'>⚠️ 醫療級別食安防禦</h3>", unsafe_allow_html=True)
    st.markdown("""
    <ul style='font-size:15px; line-height:1.6; padding-left:20px; color:#1A1A1A!important;'>
        <li><b>絕對剔除檳榔心</b>：醫學實證會引發口腔癌與心肌梗塞，本餐廳<b>永久禁用</b>。</li>
        <li><b>鐵樹心極端解毒</b>：必須經過「物理破壁 -> 活水浸泡 -> 高溫熬煮」完整降解程序。孕婦及心血管疾病患者禁止食用。</li>
    </ul>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("<h3 style='margin:20px 0;'>🌿 十心菜名錄</h3>", unsafe_allow_html=True)
    
    # 手機版改為全垂直堆疊卡片
    for heart in ten_hearts_db:
        st.markdown(f"""
        <div class="card" style="padding:15px; border-left: 5px solid #004D40 !important; border-top: 1px solid #DEE2E6 !important;">
            <div style="display:flex; justify-content:space-between; align-items:center;">
                <h4 style="color:#004D40!important; margin:0;">{heart['name']}</h4>
                <span style="background:#E0F2F1; color:#00695C!important; padding:4px 8px; border-radius:8px; font-size:12px; font-weight:bold;">{heart['trait']}</span>
            </div>
            <p style="font-size:14px; margin-top:10px; color:#333333!important; line-height:1.5;">{heart['desc']}</p>
        </div>
        """, unsafe_allow_html=True)

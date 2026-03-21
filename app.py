import streamlit as st
import pandas as pd

# ==========================================
# 1. 系統與頁面基本設定
# ==========================================
st.set_page_config(
    page_title="馬立雲部落觀光導覽 | Maibul",
    page_icon="🍃",
    layout="wide", # 改用寬螢幕佈局，更適合觀光圖片展示
    initial_sidebar_state="expanded"
)

# ==========================================
# 2. 側邊欄導覽系統 (SPA 架構)
# ==========================================
st.sidebar.image("https://images.unsplash.com/photo-1588614959060-4d144f28b207?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80", caption="舞鶴台地茶園風光")
st.sidebar.title("馬立雲部落導覽")
st.sidebar.markdown("探索花蓮瑞穗的撒奇萊雅族秘境")

# 觀光模式的核心選單
page = st.sidebar.radio(
    "開始您的旅程：",
    ["🏠 認識馬立雲", "🗺️ 景點探索", "🔥 文化與體驗", "🛍️ 部落市集", "🚗 交通與地圖"]
)

st.sidebar.markdown("---")
st.sidebar.info("💡 **貼心提醒**\n部落導覽與特殊體驗活動，請提早至少一週向部落協會預約喔！")

# ==========================================
# 3. 各頁面內容設計
# ==========================================

if page == "🏠 認識馬立雲":
    st.title("歡迎來到馬立雲部落 (Maibul)")
    st.subheader("浴火重生的撒奇萊雅族 (Sakizaya) 最大聚落")
    
    # 使用大圖展示 (此處使用 Unsplash 示意圖，您可以替換成部落真實圖片)
    st.image("https://images.unsplash.com/photo-1501785888041-af3ef285b470?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80", use_column_width=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### 📖 部落簡介")
        st.write("""
        馬立雲部落位於花蓮縣瑞穗鄉的舞鶴台地上，是台灣原住民族**「撒奇萊雅族」**最大的聚落。
        在1878年的「加禮宛戰役」後，撒奇萊雅族人為了躲避追擊，隱姓埋名藏身於阿美族中長達百餘年，直到 2007 年才正式正名。
        來到馬立雲，您不僅能欣賞到美麗的茶園風光，更能深刻感受到這個民族堅韌的生命力。
        """)
    with col2:
        st.markdown("### ✨ 觀光亮點")
        st.write("✔️ **歷史尋根**：聆聽撒奇萊雅族的火神祭與歷史故事。\n")
        st.write("✔️ **茶香四溢**：品嚐享譽國際的舞鶴「蜜香紅茶」。\n")
        st.write("✔️ **巨石奇觀**：探訪充滿神話色彩的「掃叭石柱」。\n")
        st.write("✔️ **在地風味**：享用部落專屬的刺蔥與野菜無菜單料理。")

elif page == "🗺️ 景點探索":
    st.title("🗺️ 周邊景點探索")
    st.markdown("馬立雲部落周邊擁有多樣的自然與人文景觀，建議您可以安排半日或一日遊。")
    
    # 使用 Tabs 來分類景點
    tab1, tab2, tab3 = st.tabs(["⛰️ 自然地景", "🏺 歷史人文", "☕ 舞鶴休閒農業區"])
    
    with tab1:
        st.subheader("掃叭石柱 (Satokoay)")
        st.image("https://images.unsplash.com/photo-1469474968028-56623f02e42e?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80", caption="自然地景示意")
        st.write("矗立在舞鶴台地上的兩根巨大石柱，是台灣著名的史前巨石文化遺跡，也是花東縱谷重要的地標。在阿美族與撒奇萊雅族的神話中，都有關於這兩根石柱的迷人傳說。")
        
    with tab2:
        st.subheader("北回歸線標誌公園")
        st.write("距離部落不遠處的北回歸線標誌，是熱帶與亞熱帶的分界線。每年夏至中午，還能體驗「立竿不見影」的天文奇觀，是遊客必拍的打卡熱點。")
        
    with tab3:
        st.subheader("舞鶴茶園與咖啡莊園")
        st.write("馬立雲部落所在的舞鶴台地，氣候與土壤非常適合茶樹生長。這裡最著名的就是被小綠葉蟬叮咬後，散發獨特天然果蜜香的「蜜香紅茶」，以及在地栽種的「舞鶴咖啡」。漫步在茶園中，身心都能得到極大的放鬆。")

elif page == "🔥 文化與體驗":
    st.title("🔥 深度文化與導覽體驗")
    st.markdown("透過親手參與，深入了解馬立雲的靈魂。")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("### 👘 撒奇萊雅文化導覽")
        st.write("**活動時間：** 約 1.5 小時")
        st.write("**特色：** 認識撒奇萊雅族代表性的「凝血暗紅」與「土地金黃」服飾意義。導覽員將帶您走進部落，訴說加禮宛戰役的歷史，以及每年秋季舉辦的「火神祭 (Palamal)」背後感人的追思故事。")
        st.button("預約文化導覽")
        
    with col2:
        st.success("### 🍃 蜜香紅茶採茶與揉茶體驗")
        st.write("**活動時間：** 約 2.5 小時")
        st.write("**特色：** 戴上斗笠，背起茶簍，跟著部落茶農走進茶園尋找小綠葉蟬。從採茶、萎凋到親手揉捻，最後品嚐自己製作的茶湯，是一場完美的食農教育體驗。")
        st.button("預約採茶體驗")

elif page == "🛍️ 部落市集":
    st.title("🛍️ 馬立雲農創市集")
    st.markdown("把部落的美好風味帶回家。")
    
    # 簡單的商品網格展示
    st.markdown("---")
    c1, c2, c3 = st.columns(3)
    
    with c1:
        st.markdown("<h1 style='text-align: center;'>🍵</h1>", unsafe_allow_html=True)
        st.subheader("頂級蜜香紅茶")
        st.write("無毒農業的驕傲，天然蜜香回甘不澀。適合冷泡或熱飲。")
        st.markdown("**NT$ 450 / 盒**")
        
    with c2:
        st.markdown("<h1 style='text-align: center;'>☕</h1>", unsafe_allow_html=True)
        st.subheader("舞鶴在地咖啡豆")
        st.write("水洗淺中焙，帶有花東縱谷獨特的微酸果香與堅果尾韻。")
        st.markdown("**NT$ 550 / 磅**")
        
    with c3:
        st.markdown("<h1 style='text-align: center;'>🧵</h1>", unsafe_allow_html=True)
        st.subheader("撒奇萊雅編織小物")
        st.write("部落婦女手工製作，融入傳統暗紅與金黃圖騰的零錢包或提袋。")
        st.markdown("**NT$ 250 起**")

elif page == "🚗 交通與地圖":
    st.title("🚗 交通指南與地圖")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("### 📍 位置資訊")
        st.write("**地址：** 花蓮縣瑞穗鄉舞鶴村 (馬立雲部落)")
        st.write("**聯絡電話：** 03-887-XXXX (部落發展協會)")
        
        st.markdown("### 🚂 大眾運輸")
        st.write("搭乘台鐵至**「瑞穗火車站」**，出站後轉乘計程車或租賃機車，沿台9線南下約 15 分鐘即可抵達舞鶴台地。")
        
        st.markdown("### 🚙 自行開車")
        st.write("沿台9線（花東縱谷公路）行駛至約 277K 處，見到舞鶴台地標誌即可沿指標進入部落。")

    with col2:
        # 使用 Streamlit 原生 st.map 標示大略位置 (瑞穗舞鶴周邊座標)
        st.markdown("### 🗺️ 區域地圖")
        map_data = pd.DataFrame({
            'lat': [23.4735], 
            'lon': [121.3458],
            'name': ['馬立雲部落']
        })
        st.map(map_data, zoom=12)

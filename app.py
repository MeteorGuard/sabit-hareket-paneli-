import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Sayfa ayarları
st.set_page_config(page_title="Sabit Yönlü Hareket Paneli", layout="wide")

# Başlık
st.markdown("<h1 style='color:#00ffff;'>🚀 Sabit Yönlü Hareket Paneli – Fizik </h1>", unsafe_allow_html=True)
st.write("Bu panelde sabit yönlü hareketin grafiklerini hız ve zaman aralığına göre inceleyebilirsin.")

# 🔹 Kullanıcıdan hız ve zaman aralığı al
hiz = st.slider("Hız (m/s)", min_value=1, max_value=30, value=5)
zaman_son = st.slider("Zaman Aralığı (saniye)", min_value=5, max_value=60, value=10)

# 🔹 Zaman ve Hareket Verisi
t = np.linspace(0, zaman_son, 100)
x = hiz * t
v = np.full_like(t, hiz)
a = np.zeros_like(t)

# 🔹 Grafik Fonksiyonu
def grafik_ciz(x, y, baslik, y_label, renk):
    fig, ax = plt.subplots()
    ax.plot(x, y, color=renk, linewidth=2)
    ax.set_title(baslik)
    ax.set_xlabel("Zaman (s)")
    ax.set_ylabel(y_label)
    ax.grid(True)
    st.pyplot(fig)

# 🔹 Konum-Zaman Grafiği
st.subheader("📍 Konum-Zaman Grafiği")
grafik_ciz(t, x, "Konum-Zaman", "Konum (m)", "deepskyblue")
st.markdown("""
**Grafik Açıklaması:**  
Konum zamanla doğrusal olarak artar. Bu, cismin sabit hızla ilerlediğini gösterir.  
Grafiğin eğimi, cismin hızını temsil eder. Eğimi ne kadar dikse, hız o kadar büyüktür.
""")

# 🔹 Hız-Zaman Grafiği
st.subheader("🏃‍♂️ Hız-Zaman Grafiği")
grafik_ciz(t, v, "Hız-Zaman", "Hız (m/s)", "limegreen")
st.markdown("""
**Grafik Açıklaması:**  
Hız sabit olduğu için grafik yatay bir çizgidir.  
Bu, cismin hareket boyunca hızını değiştirmediğini gösterir.  
Yatay çizginin yüksekliği, cismin hızını gösterir.
""")

# 🔹 İvme-Zaman Grafiği
st.subheader("⚡ İvme-Zaman Grafiği")
grafik_ciz(t, a, "İvme-Zaman", "İvme (m/s²)", "crimson")
st.markdown("""
**Grafik Açıklaması:**  
İvme sıfırdır çünkü hız değişmiyor.  
Grafik x ekseni boyunca düz bir çizgidir.  
Bu, sabit yönlü hareketin temel özelliğidir: ivme yoktur.
""")

# 🔹 Ek Bilgi Modülü
st.markdown("### 📚 Fiziksel Formüller")
st.code("""
Konum = hız × zaman
Hız = sabit (v = const)
İvme = 0 (çünkü hız değişmiyor)
""")

st.markdown("Notlar")
st.write("- Sabit yönlü hareket, doğrusal ve sabit hızlı bir harekettir.")
st.write("- Grafiklerin şekli, hareketin özelliklerini doğrudan yansıtır.")
st.write("- Bu tür hareketlerde enerji dönüşümü veya kuvvet etkisi gözlenmez.")

from speedtest import Speedtest

st = Speedtest()

print("İndirme Hızı", st.download()/1000000, "Mbps")
print("Yükleme Hızı", st.upload()/1000000, "Mbps")
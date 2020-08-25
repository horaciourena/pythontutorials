from speedtest import Speedtest
st = Speedtest()
print("Tu velocidad de Descarga es:", st.download()/1000000)
print("Tu velocidad de Subida es: ", st.upload()/1000000)
# st.get_servers([])
print("Ping: ", st.results.ping)
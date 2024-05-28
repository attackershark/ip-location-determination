import geocoder
import folium
import requests

def get_location(ip):
    response = requests.get(f'https://ipapi.co/{ip}/json/').json()

    if "city" in response and "region" in response and "country_name" in response:
        location_data = {
            "Ip Adres": ip,
            "Şehir": response.get("city"),
            "Bölge": response.get("region"),
            "Ülke": response.get("country_name")
        }
        return location_data
    else:
        return "Konum verisi bulunamadı."

if __name__ == "__main__":
    user = input("IP adres girin: ")
    location = get_location(user)
    print(location)

    g = geocoder.ip(user)
    latlng = g.latlng

    if latlng is not None:
        user_map = folium.Map(location=latlng, zoom_start=12)
        folium.Marker(location=latlng, popup=f"IP Adres: {user}").add_to(user_map)
        user_map.save("C:/Users/user/Desktop/chatbot/deneme/ip konum/my_map.html")
        print("Harita oluşturuldu: my_map.html")
    else:
        print("Konum bilgisi bulunamadı.")

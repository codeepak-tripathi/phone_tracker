# phone tracker
import geocoder as geocoder
import phonenumbers
from number import number
import folium
from phonenumbers import geocoder



def parse():
    ch_number = phonenumbers.parse(number, "CH")
    print(phonenumbers.geocoder.description_for_number(ch_number, "en"))
    print("hello")
    from phonenumbers import carrier
    service_provider = phonenumbers.parse(number, "RO")
    print(carrier.name_for_number(service_provider, "en"))
    from phonenumbers import carrier
    service_provider = phonenumbers.parse(number)
    print(carrier.name_for_number(service_provider, "en"))

    from opencage.geocoder import OpenCageGeocode
    key="e79d72fef2cf483d8acc2660da0c31dc"
    geocoder = OpenCageGeocode(key)
    yourLocation=phonenumbers.geocoder.description_for_number(ch_number, "en")
    query = str(yourLocation)
    results = geocoder.geocode(query)
    # print(results)

    lat = results[0]['geometry']['lat']

    long = results[0]['geometry']['lng']

    print(lat, long)

    myMap = folium.Map(location=[lat, long], zoom_start=0)

    folium.Marker([lat, long], popup=yourLocation).add_to(myMap)

    # html save
    myMap.save("myLoc.html")

    # import module
    from geopy.geocoders import Nominatim

    # initialize Nominatim API
    geolocator = Nominatim(user_agent="geoapiExercises")

    # Latitude & Longitude input
    Latitude = str(lat)
    Longitude = str(long)

    location = geolocator.reverse(Latitude + "," + Longitude)

    address = location.raw['address']

    # traverse the data
    city = address.get('city', '')
    state = address.get('state', '')
    country = address.get('country', '')
    code = address.get('country_code')
    zipcode = address.get('postcode')
    print('City : ', city)
    print('State : ', state)
    print('Country : ', country)
    print('Zip Code : ', zipcode)


if __name__ == '__main__':

    print_hi()

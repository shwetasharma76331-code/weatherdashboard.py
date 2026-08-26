import streamlit as st
import requests
from datetime import datetime




st.set_page_config(
    page_title="Live Weather Dashboard",
    page_icon="🌤️",
    layout="centered"
)


st.markdown("""
<style>

.main {
    background-color: #f5f9ff;
}

.title {
    text-align: center;
    color: #1e3a8a;
    font-size: 42px;
    font-weight: bold;
}

.subtitle {
    text-align: center;
    color: #64748b;
    font-size: 18px;
}

.weather-card {
    background: linear-gradient(135deg, #2563eb, #38bdf8);
    padding: 30px;
    border-radius: 20px;
    color: white;
    text-align: center;
    margin-top: 25px;
}

.temperature {
    font-size: 60px;
    font-weight: bold;
}

.description {
    font-size: 22px;
    text-transform: capitalize;
}

.info-card {
    background-color: white;
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.08);
}

</style>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="title">🌤️ Live Weather Dashboard</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Check real-time weather information</div>',
    unsafe_allow_html=True
)

st.write("")


API_KEY = "YOUR_API_KEY"

city = st.text_input(
    "📍 Enter City Name",
    placeholder="Example: Delhi"
)


def get_weather(city):

    url = (
        "https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}"
        f"&appid={API_KEY}"
        "&units=metric"
    )

    response = requests.get(url)

    if response.status_code == 200:
        return response.json()

    return None


if st.button("🔍 Get Weather", use_container_width=True):

    if city.strip() == "":
        st.warning("Please enter a city name.")

    else:

        with st.spinner("Fetching live weather..."):

            data = get_weather(city)

        if data:

        
            city_name = data["name"]
            country = data["sys"]["country"]

            temperature = data["main"]["temp"]
            feels_like = data["main"]["feels_like"]

            humidity = data["main"]["humidity"]
            pressure = data["main"]["pressure"]

            wind_speed = data["wind"]["speed"]

            description = data["weather"][0]["description"]

            icon = data["weather"][0]["icon"]

            weather_icon_url = (
                f"https://openweathermap.org/img/wn/"
                f"{icon}@2x.png"
            )


            st.markdown(
                f"""
                <div class="weather-card">

                    <h1>{city_name}, {country}</h1>

                    <img src="{weather_icon_url}" width="100">

                    <div class="temperature">
                        {round(temperature)}°C
                    </div>

                    <div class="description">
                        {description}
                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )

            st.write("")


            col1, col2, col3, col4 = st.columns(4)

            with col1:
                st.markdown(
                    f"""
                    <div class="info-card">
                        <h3>💧</h3>
                        <p>Humidity</p>
                        <h3>{humidity}%</h3>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            with col2:
                st.markdown(
                    f"""
                    <div class="info-card">
                        <h3>🌡️</h3>
                        <p>Feels Like</p>
                        <h3>{round(feels_like)}°C</h3>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            with col3:
                st.markdown(
                    f"""
                    <div class="info-card">
                        <h3>💨</h3>
                        <p>Wind Speed</p>
                        <h3>{wind_speed} m/s</h3>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            with col4:
                st.markdown(
                    f"""
                    <div class="info-card">
                        <h3>📊</h3>
                        <p>Pressure</p>
                        <h3>{pressure} hPa</h3>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            st.write("")

            current_time = datetime.now().strftime(
                "%d %B %Y, %I:%M %p"
            )
                f"Last updated: {current_time}"
import requests
from datetime import datetime

st.set_page_config(
    page_title="Live Weather Dashboard",
    page_icon="🌤️",
    layout="centered"
)

st.markdown("""
<style>

.main {
    background-color: #f5f9ff;
}

.title {
    text-align: center;
    color: #1e3a8a;
    font-size: 42px;
    font-weight: bold;
}

.subtitle {
    text-align: center;
    color: #64748b;
    font-size: 18px;
}

.weather-card {
    background: linear-gradient(135deg, #2563eb, #38bdf8);
    padding: 30px;
    border-radius: 20px;
    color: white;
    text-align: center;
    margin-top: 25px;
}

.temperature {
    font-size: 60px;
    font-weight: bold;
}

.description {
    font-size: 22px;
    text-transform: capitalize;
}

.info-card {
    background-color: white;
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.08);
}

</style>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="title">🌤️ Live Weather Dashboard</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Check real-time weather information</div>',
    unsafe_allow_html=True
)

st.write("")


API_KEY = "YOUR_API_KEY"


city = st.text_input(
    "📍 Enter City Name",
    placeholder="Example: Delhi"
)




def get_weather(city):

    url = (
        "https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}"
        f"&appid={API_KEY}"
        "&units=metric"
    )

    response = requests.get(url)

    if response.status_code == 200:
        return response.json()

    return Note

if st.button("🔍 Get Weather", use_container_width=True):

    if city.strip() == "":
        st.warning("Please enter a city name.")

    else:

        with st.spinner("Fetching live weather..."):

            data = get_weather(city)

        if data:

            
            city_name = data["name"]
            country = data["sys"]["country"]

            temperature = data["main"]["temp"]
            feels_like = data["main"]["feels_like"]

            humidity = data["main"]["humidity"]
            pressure = data["main"]["pressure"]

            wind_speed = data["wind"]["speed"]

            description = data["weather"][0]["description"]

            icon = data["weather"][0]["icon"]

            weather_icon_url = (
                f"https://openweathermap.org/img/wn/"
                f"{icon}@2x.png"
            )


            st.markdown(
                f"""
                <div class="weather-card">

                    <h1>{city_name}, {country}</h1>

                    <img src="{weather_icon_url}" width="100">

                    <div class="temperature">
                        {round(temperature)}°C
                    </div>

                    <div class="description">
                        {description}
                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )

            st.write("")


            col1, col2, col3, col4 = st.columns(4)

            with col1:
                st.markdown(
                    f"""
                    <div class="info-card">
                        <h3>💧</h3>
                        <p>Humidity</p>
                        <h3>{humidity}%</h3>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            with col2:
                st.markdown(
                    f"""
                    <div class="info-card">
                        <h3>🌡️</h3>
                        <p>Feels Like</p>
                        <h3>{round(feels_like)}°C</h3>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            with col3:
                st.markdown(
                    f"""
                    <div class="info-card">
                        <h3>💨</h3>
                        <p>Wind Speed</p>
                        <h3>{wind_speed} m/s</h3>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            with col4:
                st.markdown(
                    f"""
                    <div class="info-card">
                        <h3>📊</h3>
                        <p>Pressure</p>
                        <h3>{pressure} hPa</h3>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            st.write("")

            current_time = datetime.now().strftime(
                "%d %B %Y, %I:%M %p"
            )

            st.caption(
                f"Last updated: {current_time}"
            )

        else:

            st.error(
                "❌ City not found. Please check the city name."
            )


        else:

            st.error(
                "❌ City not found. Please check the city name."
            )

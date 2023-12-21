import requests
import streamlit as st


st.header("Breweries: Choose a State")

state_names = [
    "Alaska",
    "Alabama",
    "Arkansas",
    "Arizona",
    "California",
    "Colorado",
    "Connecticut",
    "District ",
    "of Columbia",
    "Delaware",
    "Florida",
    "Georgia",
    "Guam",
    "Hawaii",
    "Iowa",
    "Idaho",
    "Illinois",
    "Indiana",
    "Kansas",
    "Kentucky",
    "Louisiana",
    "Massachusetts",
    "Maryland",
    "Maine",
    "Michigan",
    "Minnesota",
    "Missouri",
    "Mississippi",
    "Montana",
    "North Carolina",
    "North Dakota",
    "Nebraska",
    "New Hampshire",
    "New Jersey",
    "New Mexico",
    "Nevada",
    "New York",
    "Ohio",
    "Oklahoma",
    "Oregon",
    "Pennsylvania",
    "Puerto Rico",
    "Rhode Island",
    "South Carolina",
    "South Dakota",
    "Tennessee",
    "Texas",
    "Utah",
    "Virginia",
    "Virgin Islands",
    "Vermont",
    "Washington",
    "Wisconsin",
    "West Virginia",
    "Wyoming",
]


def mapify(brewery_data):
    coordinates = {"longitude": [], "latitude": []}

    for brewery in brewery_data:
        lon = brewery["longitude"]
        lat = brewery["latitude"]
        if lon != None and lat != None:
            coordinates["longitude"].append(float(lon))
            coordinates["latitude"].append(float(lat))
    st.map(coordinates)


state_choice = st.selectbox("Choose a state...", options=state_names, index=None)


if state_choice in state_names:
    breweries = requests.get(
        "https://api.openbrewerydb.org/v1/breweries?by_state="
        + state_choice
        + "&per_page=200"
    ).json()

    if st.button("Show density map of breweries", type="primary"):
        mapify(breweries)

    st.write("---")

    col1, col2 = st.columns(2)

    brew_names = [brew["name"] for brew in breweries]
    counter = 0

    for name in brew_names:
        half = len(brew_names) // 2
        counter += 1

        if counter <= half:
            with col1:
                st.button(name, key=counter)

        else:
            with col2:
                st.button(name, key=counter)

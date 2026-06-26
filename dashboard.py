import streamlit as st
import json
import pandas as pd
import pydeck as pdk

from datetime import datetime
from geopy.geocoders import Nominatim
from ml.predict import predict_flood_risk
from agents.coordinator_agent import CoordinatorAgent

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Project Sentinel",
    page_icon="🚨",
    layout="wide"
)

# =====================================================
# LOCATION
# =====================================================

location_name = st.text_input(
    "📍 Disaster Location",
    value="Enter name of city, town, or village",
    placeholder="Enter location (city, town, village)"
)

# =====================================================
# HEADER
# =====================================================

st.title("🚨 Project Sentinel")
st.caption("AI Powered Disaster Intelligence & Emergency Response System")

col1, col2 = st.columns([2, 1])

with col1:
    st.caption(f"📍 Location: {location_name}")

with col2:
    st.caption(f"🕒 {datetime.now().strftime('%d-%m-%Y %I:%M:%S %p')}")
# =====================================================
# GET COORDINATES
# =====================================================

latitude = 15.2695
longitude = 76.3909

try:
    geolocator = Nominatim(user_agent="project_sentinel")

    loc = geolocator.geocode(location_name)

    if loc:
        latitude = loc.latitude
        longitude = loc.longitude

except:
    pass

# =====================================================
# SIDEBAR
# =====================================================

with st.sidebar:

    st.header("🚨 Emergency Dashboard")

    st.success("System Online")

    st.divider()

    st.header("🤖 AI Agent Network")

    st.success("Coordinator Agent")
    st.success("Risk Assessment Agent")
    st.success("Medical Agent")
    st.success("Resource Agent")
    st.success("Evacuation Agent")
    st.success("Communication Agent")

    st.metric("Total Agents", "6")
    st.divider()

    st.header("☎ Emergency Contacts")

    st.info("""
🚓 Police : 100

🚒 Fire : 101

🚑 Ambulance : 108

🆘 Disaster Helpline : 1070
""")

    st.divider()

    st.header("ℹ About")

    st.write("""
Project Sentinel uses multiple AI agents to:

• Assess disaster risks

• Plan evacuations

• Allocate resources

• Generate alerts

• Support emergency teams
""")

# =====================================================
# MAP
# =====================================================

st.subheader("🌍 Disaster Location Map")

map_df = pd.DataFrame(
    {
        "lat": [latitude],
        "lon": [longitude],
        "location": [location_name]
    }
)

layer = pdk.Layer(
    "ScatterplotLayer",
    data=map_df,
    get_position="[lon, lat]",
    get_fill_color="[255,0,0,180]",
    get_radius=1000,
    pickable=True
)

view_state = pdk.ViewState(
    latitude=latitude,
    longitude=longitude,
    zoom=11
)

st.pydeck_chart(
    pdk.Deck(
        initial_view_state=view_state,
        layers=[layer],
        tooltip={
            "html": """
            <b>🚨 Disaster Reported</b><br/>
            Location: {location}
            """
        }
    )
)


# =====================================================
# FLOOD PREDICTION
# =====================================================

st.subheader("🌧️ AI Flood Risk Prediction")

col1, col2, col3 = st.columns(3)

with col1:
    rainfall = st.number_input(
        "Rainfall (mm)",
        min_value=0,
        max_value=500,
        value=200
    )

with col2:
    river_level = st.number_input(
        "River Level (m)",
        min_value=0.0,
        max_value=20.0,
        value=7.0
    )

with col3:
    density = st.selectbox(
        "Population Density",
        ["Low", "Medium", "High"]
    )

density_map = {
    "Low": 1,
    "Medium": 2,
    "High": 3
}

if st.button("🌊 Predict Flood Risk"):

    prediction, probability = predict_flood_risk(
        rainfall,
        river_level,
        density_map[density]
    )

    st.metric(
        "Flood Probability",
        f"{probability}%"
    )

    if prediction == 1:
        st.error("🔴 Flood Risk Detected")
    else:
        st.success("🟢 Low Flood Risk")

st.subheader("📈 Historical Disaster Analytics")

chart_df = pd.DataFrame({
    "Month": [
        "Jan", "Feb", "Mar",
        "Apr", "May", "Jun"
    ],
    "Risk Score": [
        20, 35, 50,
        65, 80, 90
    ]
})

st.line_chart(
    chart_df.set_index("Month")
)

# =====================================================
# REPORT INPUT
# =====================================================

report = st.text_area(
    "📝 Enter Disaster Report",
    height=200,
    placeholder="""
Severe flooding reported near Hospet.

Population affected: 50,000

Heavy rainfall expected for next 72 hours.

Several roads inaccessible.

Power outages reported.
"""
)

# =====================================================
# ANALYZE BUTTON
# =====================================================

if st.button("🚀 Analyze Disaster"):

    coordinator = CoordinatorAgent()

    result = coordinator.coordinate(report, location_name)

    severity = result["risk_assessment"]["severity"]
    risk_score = result["risk_assessment"]["risk_score"]

    # ================================================
    # ALERT BANNER
    # ================================================

    # if severity.upper() == "CRITICAL":
    #     st.error("🔴 CRITICAL DISASTER DETECTED")

    # elif severity.upper() == "HIGH":
    #     st.warning("🟠 HIGH RISK DISASTER")

    # else:
    #     st.success("🟢 LOW RISK DISASTER")

    # # ================================================
    # # RISK METER
    # # ================================================

    # st.subheader("📊 Risk Level")

    # st.progress(min(risk_score, 100) / 100)

    # st.write(f"Risk Score: {risk_score}/100")

    # st.divider()

    # ================================================
    # METRICS
    # ================================================

    # col1, col2, col3 = st.columns(3)

    # with col1:
    #     st.metric("Severity", severity)
    #     st.metric("Risk Score", risk_score)

    # with col2:
    #     st.metric(
    #         "Ambulances",
    #         result["medical_response"]["ambulances"]
    #     )

    #     st.metric(
    #         "Doctors",
    #         result["medical_response"]["doctors"]
    #     )

    # with col3:
    #     st.metric(
    #         "Food Kits",
    #         result["resource_allocation"]["food_kits"]
    #     )

    #     st.metric(
    #         "Shelters",
    #         result["resource_allocation"]["shelters"]
    #     )

    # ================================================
    # TABS
    # ================================================

    tab1, tab2, tab3, tab4 = st.tabs(
        [
            "🧠 Intelligence",
            "🚑 Evacuation",
            "📢 Alerts",
            "📄 Full Report"
        ]
    )

    # ================================================
    # TAB 1
    # ================================================

    with tab1:

        st.subheader("⚠ Major Threats")

        for threat in result["risk_assessment"]["major_threats"]:
            st.warning(threat)

        st.subheader("📦 Resource Allocation")

        st.success(
            f"Food Kits: {result['resource_allocation']['food_kits']}"
        )

        st.info(
            f"Water Supply: {result['resource_allocation']['water_supply_liters']} Liters"
        )

        st.success(
            f"Shelters: {result['resource_allocation']['shelters']}"
        )


    # ================================================
    # TAB 2
    # ================================================

    with tab2:

        evacuation = result.get("evacuation_plan")

        if evacuation:

            st.subheader("🚑 Evacuation Plan")

            st.error(
                f"Priority: {evacuation['evacuation_priority']}"
            )

            st.write(
                f"People To Evacuate: {evacuation['people_to_evacuate']}"
            )

            st.subheader("🏠 Nearby Safe Locations")

            safe_locations = result.get("safe_location_map", [])

            if safe_locations:

                map_df = pd.DataFrame({
                    "lat": [p["latitude"] for p in safe_locations],
                    "lon": [p["longitude"] for p in safe_locations],
                    "name": [p["name"] for p in safe_locations]
                })

                layer = pdk.Layer(
                    "ScatterplotLayer",
                    data=map_df,
                    get_position="[lon, lat]",
                    get_fill_color="[0,255,0,180]",
                    get_radius=800,
                    pickable=True,
                )

                view_state = pdk.ViewState(
                    latitude=map_df["lat"].mean(),
                    longitude=map_df["lon"].mean(),
                    zoom=11,
                )

                st.pydeck_chart(
                    pdk.Deck(
                        initial_view_state=view_state,
                        layers=[layer],
                        tooltip={"text": "{name}"},
                    )
                )

                st.markdown("### 📍 Safe Shelter Details")

                for place in safe_locations:

                    st.success(place["name"])
                    st.write(f"Latitude : {place['latitude']}")
                    st.write(f"Longitude : {place['longitude']}")

                    st.link_button(
                        "📍 Open in Google Maps",
                        place["maps_url"]
                    )

                    st.divider()

            else:
                st.warning("No safe locations found.")

        else:
            st.warning("No evacuation plan available.")
    # ================================================
    # TAB 3
    # ================================================

    with tab3:

        alerts = result.get("communication")

        if alerts:

            st.subheader("🚨 Emergency Alert Center")

            st.error("🔴 Public Safety Alert")
            st.write(alerts["public_alert"])

            st.markdown("---")

            st.warning("📱 Emergency SMS")
            st.code(alerts["emergency_sms"])

            st.markdown("---")

            st.info("🏛 Government Situation Report")
            st.write(alerts["government_briefing"])

            st.markdown("---")

            st.subheader("✅ Immediate Safety Instructions")

            instructions = [
                "Move immediately to the nearest safe shelter.",
                "Avoid flooded roads and bridges.",
                "Switch off electricity and gas before leaving home.",
                "Carry drinking water, medicines, and important documents.",
                "Keep your mobile phone fully charged.",
                "Follow instructions from local authorities only.",
                "Do not spread unverified information on social media.",
                "Call Emergency 1070 or 108 only if immediate assistance is required."
            ]

            for step in instructions:
                st.success(step)

            st.markdown("---")

            st.subheader("📞 Emergency Contacts")

            c1, c2, c3, c4 = st.columns(4)

            with c1:
                st.metric("Police", "100")

            with c2:
                st.metric("Fire", "101")

            with c3:
                st.metric("Ambulance", "108")

            with c4:
                st.metric("Disaster", "1070")

            st.markdown("---")

            st.subheader("📢 Share Emergency Alert")

            alert_text = f"""
🚨 EMERGENCY ALERT

Location : {location_name}

Severity : {severity}

Risk Score : {risk_score}/100

Please evacuate immediately to the nearest safe shelter.

Emergency Numbers:
Police - 100
Fire - 101
Ambulance - 108
Disaster Helpline - 1070
"""

            st.download_button(
                "📥 Download Emergency Alert",
                alert_text,
                "Emergency_Alert.txt",
                "text/plain"
            )

        else:
            st.warning("No alerts available.")
    # ================================================
    # TAB 4
    # ================================================

    with tab4:

        st.subheader("📄 Disaster Intelligence Report")

        if severity.upper() == "CRITICAL":
            st.error("🔴 CRITICAL DISASTER DETECTED")

        elif severity.upper() == "HIGH":
            st.warning("🟠 HIGH RISK DISASTER")

        else:
            st.success("🟢 LOW RISK DISASTER")

        st.subheader("📊 Risk Level")

        st.progress(min(risk_score, 100) / 100)

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Severity", severity)

        with col2:
            st.metric("Risk Score", risk_score)

        st.divider()

        st.markdown(f"""
### Risk Assessment

**Severity:** {result['risk_assessment']['severity']}

**Risk Score:** {result['risk_assessment']['risk_score']}

### Medical Response

- Ambulances: {result['medical_response']['ambulances']}
- Doctors: {result['medical_response']['doctors']}
- Medical Kits: {result['medical_response']['medical_kits']}

### Resource Allocation

- Food Kits: {result['resource_allocation']['food_kits']}
- Water Supply: {result['resource_allocation']['water_supply_liters']} Liters
- Shelters: {result['resource_allocation']['shelters']}
""")

        report_text = f"""
PROJECT SENTINEL DISASTER REPORT

Location: {location_name}

Severity: {result['risk_assessment']['severity']}
Risk Score: {result['risk_assessment']['risk_score']}

Major Threats:
{chr(10).join(result['risk_assessment']['major_threats'])}

Medical Response:
Ambulances: {result['medical_response']['ambulances']}
Doctors: {result['medical_response']['doctors']}
Medical Kits: {result['medical_response']['medical_kits']}

Resource Allocation:
Food Kits: {result['resource_allocation']['food_kits']}
Water Supply: {result['resource_allocation']['water_supply_liters']}
Shelters: {result['resource_allocation']['shelters']}
"""

        st.download_button(
            label="📥 Download Disaster Report",
            data=report_text,
            file_name="Project_Sentinel_Report.txt",
            mime="text/plain"
        )
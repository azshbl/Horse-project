import streamlit as st
st.set_page_config(
    page_title="Horse Stable System",
    page_icon="🐎",
    layout="wide"
)

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #1b130d, #2b1d12, #0f0f0f);
    color: #f5e6c8;
}

.main-title {
    font-size: 45px;
    font-weight: bold;
    color: #d4af37;
    text-align: center;
    margin-bottom: 5px;
}

.sub-title {
    font-size: 18px;
    color: #f5e6c8;
    text-align: center;
    margin-bottom: 30px;
}

.card {
    background-color: rgba(255, 255, 255, 0.08);
    padding: 20px;
    border-radius: 18px;
    border: 1px solid #d4af37;
    margin-bottom: 15px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.4);
}

.card-title {
    color: #d4af37;
    font-size: 22px;
    font-weight: bold;
}

.sidebar .sidebar-content {
    background-color: #1b130d;
}

div.stButton > button {
    background-color: #d4af37;
    color: black;
    border-radius: 10px;
    border: none;
    font-weight: bold;
}

div.stButton > button:hover {
    background-color: #b89020;
    color: white;
}

[data-testid="stMetricValue"] {
    color: #d4af37;
}

h1, h2, h3 {
    color: #d4af37;
}
</style>
""", unsafe_allow_html=True)

st.set_page_config(page_title="Horse Stable System", layout="centered")

horses = {
    1: {"owner_name": "Turki", "horse_name": "Wadah", "age": 6, "gender": "male", "breed": "arabian", "status": "stable", "horse_level": 100, "health_score": 100},
    2: {"owner_name": "Turki", "horse_name": "Shamekh", "age": 5, "gender": "male", "breed": "arabian", "status": "stable", "horse_level": 97, "health_score": 95},
    3: {"owner_name": "Turki", "horse_name": "Alskb", "age": 7, "gender": "male", "breed": "frezian", "status": "stable", "horse_level": 94, "health_score": 92},
    4: {"owner_name": "Turki", "horse_name": "Abiah.t", "age": 7, "gender": "female", "breed": "arabian", "status": "stable", "horse_level": 96, "health_score": 98},
    5: {"owner_name": "Turki", "horse_name": "Seham", "age": 5, "gender": "female", "breed": "arabian", "status": "stable", "horse_level": 91, "health_score": 93},
    6: {"owner_name": "Turki", "horse_name": "Rahaf", "age": 6, "gender": "female", "breed": "arabian", "status": "stable", "horse_level": 72, "health_score": 96},
    7: {"owner_name": "Turki", "horse_name": "Kehelan", "age": 4, "gender": "male", "breed": "arabian", "status": "stable", "horse_level": 72, "health_score": 89},
    8: {"owner_name": "Turki", "horse_name": "shujaa", "age": 8, "gender": "male", "breed": "arabian", "status": "stable", "horse_level": 99, "health_score": 99},
    9: {"owner_name": "Turki", "horse_name": "Borkan", "age": 5, "gender": "male", "breed": "arabian", "status": "stable", "horse_level": 93, "health_score": 94},
    10: {"owner_name": "Turki", "horse_name": "Raad", "age": 4, "gender": "male", "breed": "arabian", "status": "stable", "horse_level": 92, "health_score": 90},
    11: {"owner_name": "Turki", "horse_name": "Barq", "age": 7, "gender": "male", "breed": "arabian", "status": "stable", "horse_level": 75, "health_score": 99},
    12: {"owner_name": "Turki", "horse_name": "Asael", "age": 6, "gender": "female", "breed": "arabian", "status": "stable", "horse_level": 77, "health_score": 95},
    13: {"owner_name": "Nawaf", "horse_name": "Mazyon", "age": 5, "gender": "male", "breed": "arabian", "status": "boarding", "horse_level": 88, "health_score": 84},
    14: {"owner_name": "Abdulaziz", "horse_name": "alshqh", "age": 4, "gender": "male", "breed": "arabian", "status": "boarding", "horse_level": 85, "health_score": 87},
    15: {"owner_name": "Nawaf.z", "horse_name": "gzar", "age": 6, "gender": "male", "breed": "frezian", "status": "boarding", "horse_level": 89, "health_score": 91},
    16: {"owner_name": "Abdullah", "horse_name": "nomas", "age": 5, "gender": "male", "breed": "arabian", "status": "boarding", "horse_level": 100, "health_score": 100},
    17: {"owner_name": "Khulod", "horse_name": "Najm", "age": 7, "gender": "male", "breed": "arabian", "status": "boarding", "horse_level": 100, "health_score": 100},
    18: {"owner_name": "Abdulaziz", "horse_name": "abiah", "age": 4, "gender": "female", "breed": "arabian", "status": "boarding", "horse_level": 74, "health_score": 90},
    19: {"owner_name": "Nawaf", "horse_name": "Anood", "age": 5, "gender": "female", "breed": "arabian", "status": "boarding", "horse_level": 70, "health_score": 85},
    20: {"owner_name": "Nawaf.z", "horse_name": "Shadad", "age": 6, "gender": "male", "breed": "frezian", "status": "boarding", "horse_level": 65, "health_score": 89}
}

trainers = {
    1: {"trainer_name": "Turki", "age": 24, "training_type": "Racing, For fun", "sessions_completed": 70, "performance_score": 99},
    2: {"trainer_name": "Abdulaziz", "age": 24, "training_type": "Jumping", "sessions_completed": 56, "performance_score": 95},
    3: {"trainer_name": "Nawaf.z", "age": 24, "training_type": "For fun", "sessions_completed": 20, "performance_score": 89},
    4: {"trainer_name": "Nawaf", "age": 24, "training_type": "Racing", "sessions_completed": 50, "performance_score": 85},
    5: {"trainer_name": "Khalid", "age": 22, "training_type": "Racing", "sessions_completed": 30, "performance_score": 80},
    6: {"trainer_name": "Saud", "age": 20, "training_type": "Racing", "sessions_completed": 10, "performance_score": 79},
    7: {"trainer_name": "Abdullah", "age": 24, "training_type": "Jumping", "sessions_completed": 22, "performance_score": 75},
    8: {"trainer_name": "Mohammed", "age": 26, "training_type": "For fun", "sessions_completed": 40, "performance_score": 70}
}

if "trainees" not in st.session_state:
    st.session_state.trainees = {
        1: {"trainee_name": "Ahmed", "age": 20, "training_type": "Jumping", "level": "Beginner", "completed_classes": 5, "package": 10, "assigned_trainer": "Abdullah", "assigned_horse": "Rahaf", "license": False},
        2: {"trainee_name": "Mohammed", "age": 23, "training_type": "Racing", "level": "Intermediate", "completed_classes": 18, "package": 20, "assigned_trainer": "Nawaf", "assigned_horse": "Mazyon", "license": False},
        3: {"trainee_name": "Khalid", "age": 25, "training_type": "For fun", "level": "Advanced", "completed_classes": 35, "package": 40, "assigned_trainer": "Turki", "assigned_horse": "Wadah", "license": False},
        4: {"trainee_name": "Saad", "age": 21, "training_type": "Jumping", "level": "Advanced", "completed_classes": 40, "package": 40, "assigned_trainer": "Abdulaziz", "assigned_horse": "Shamekh", "license": True}
    }


def trainer_level(score):
    if score >= 90:
        return "Advanced"
    elif score >= 80:
        return "Intermediate"
    else:
        return "Beginner"


def assign_trainer(training_type, level):
    for trainer in trainers.values():
        score = trainer["performance_score"]

        if level == "Beginner" and score < 80:
            if training_type.lower() in trainer["training_type"].lower():
                return trainer["trainer_name"]

        elif level == "Intermediate" and 80 <= score <= 89:
            if training_type.lower() in trainer["training_type"].lower():
                return trainer["trainer_name"]

        elif level == "Advanced" and score >= 90:
            if training_type.lower() in trainer["training_type"].lower():
                return trainer["trainer_name"]

    return "No Trainer Available"


def assign_horse(level):
    for horse in horses.values():
        horse_level = horse["horse_level"]

        if level == "Beginner" and 60 <= horse_level <= 79:
            return horse["horse_name"]

        elif level == "Intermediate" and 80 <= horse_level <= 89:
            return horse["horse_name"]

        elif level == "Advanced" and horse_level >= 90:
            return horse["horse_name"]

    return "No Horse Available"


st.markdown('<div class="main-title">🐎 Horse Stable Management System</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">A luxury management system for horses, trainers, owners, and trainees</div>', unsafe_allow_html=True)


main_choice = st.sidebar.selectbox(
    "Role Selection",
    ["Admin", "Horse Owner", "Trainee"]
)

if main_choice == "Admin":
    st.header("Admin Menu")

    admin_choice = st.selectbox(
        "Choose Option",
        ["Show Horses", "Search Horse", "Horse Statistics", "Show Trainers", "Best Trainer", "Show Trainees"]
    )

    
    if admin_choice == "Show Horses":

        st.subheader("🐴 Stable Horses")

        for horse_id, horse in horses.items():

            st.markdown(f"""
            <div style="
            background:#2c1d12;
            padding:20px;
            border-radius:20px;
            border:2px solid gold;
            margin-bottom:15px;
            ">

            <h2 style="color:gold;">🐎 {horse["horse_name"]}</h2>

            <p><b>Horse ID:</b> {horse_id}</p>
            <p><b>Owner:</b> {horse["owner_name"]}</p>
            <p><b>Breed:</b> {horse["breed"].title()}</p>
            <p><b>Age:</b> {horse["age"]}</p>
            <p><b>Gender:</b> {horse["gender"].title()}</p>
            <p><b>Status:</b> {horse["status"].title()}</p>
            <p><b>Health Score:</b> {horse["health_score"]}/100</p>
            <p><b>Horse Level:</b> {horse["horse_level"]}/100</p>

            </div>
            """, unsafe_allow_html=True)


    elif admin_choice == "Search Horse":
        horse_name = st.text_input("Enter horse name:")

        if st.button("Search"):
            found = False

            for horse_id, horse in horses.items():
                if horse["horse_name"].lower() == horse_name.lower():
                    st.success("Horse Found!")
                    st.write("ID:", horse_id)
                    st.write("Name:", horse["horse_name"])
                    st.write("Owner:", horse["owner_name"])
                    st.write("Health Score:", horse["health_score"])
                    st.write("Horse Level:", horse["horse_level"])
                    found = True
                    break

            if found == False:
                st.error("Horse not found.")

    elif admin_choice == "Horse Statistics":
        total_horses = len(horses)
        stable_count = 0
        boarding_count = 0
        arabian_count = 0
        frezian_count = 0

        for horse in horses.values():
            if horse["status"] == "stable":
                stable_count += 1
            elif horse["status"] == "boarding":
                boarding_count += 1

            if horse["breed"] == "arabian":
                arabian_count += 1
            elif horse["breed"] == "frezian":
                frezian_count += 1

        
        col1, col2, col3, col4 = st.columns(4)

        col1.metric("🐎 Total Horses", total_horses)
        col2.metric("🏠 Stable Horses", stable_count)
        col3.metric("📋 Boarding Horses", boarding_count)
        col4.metric("🌟 Arabian Horses", arabian_count)



        col1.metric("Total Horses", total_horses)
        col2.metric("Stable Horses", stable_count)
        col3.metric("Boarding Horses", boarding_count)
        col4.metric("Arabian Horses", arabian_count)

    elif admin_choice == "Show Trainers":
        for trainer_id, trainer in trainers.items():
            st.write("Trainer ID:", trainer_id)
            st.write("Trainer Name:", trainer["trainer_name"])
            st.write("Age:", trainer["age"])
            st.write("Training Type:", trainer["training_type"])
            st.write("Sessions Completed:", trainer["sessions_completed"])
            st.write("Performance Score:", trainer["performance_score"])
            st.write("Level:", trainer_level(trainer["performance_score"]))
            st.write("---")

    elif admin_choice == "Best Trainer":
        best = max(trainers.values(), key=lambda trainer: trainer["performance_score"])

        st.success("Best Trainer")
        st.write("Trainer Name:", best["trainer_name"])
        st.write("Performance Score:", best["performance_score"])
        st.write("Sessions Completed:", best["sessions_completed"])
        st.write("Level:", trainer_level(best["performance_score"]))

    elif admin_choice == "Show Trainees":
        for trainee_id, trainee in st.session_state.trainees.items():
            st.write("Trainee ID:", trainee_id)
            st.write("Name:", trainee["trainee_name"])
            st.write("Age:", trainee["age"])
            st.write("Training Type:", trainee["training_type"])
            st.write("Level:", trainee["level"])
            st.write("Completed Classes:", trainee["completed_classes"])
            st.write("Package:", trainee["package"])
            st.write("Assigned Trainer:", trainee["assigned_trainer"])
            st.write("Assigned Horse:", trainee["assigned_horse"])
            st.write("License:", trainee["license"])
            st.write("---")



elif main_choice == "Horse Owner":

    st.header("🐎 Horse Owner Menu")

    owner_choice = st.selectbox(
        "Choose Option",
        ["Boarding", "View My Horses"]
    )

    # ================= BOARDING =================

    if owner_choice == "Boarding":

        owner_name = st.text_input("Owner Name")

        horse_name = st.text_input("Horse Name")

        horse_age = st.number_input(
            "Horse Age",
            min_value=1,
            max_value=40,
            value=5
        )

        horse_gender = st.selectbox(
            "Horse Gender",
            ["Male", "Female"]
        )

        duration = st.selectbox(
            "Boarding Duration",
            [
                "1 Month - 1500 SAR",
                "3 Months - 4300 SAR",
                "5 Months - 7300 SAR",
                "7 Months - 10300 SAR",
                "9 Months - 13300 SAR",
                "11 Months - 16300 SAR",
                "1 Year - 17500 SAR"
            ]
        )

        if st.button("Submit Boarding Request"):

            st.success("Boarding Request Submitted Successfully")

            st.markdown(f"""
            <div style="
            background:#2c1d12;
            padding:20px;
            border-radius:20px;
            border:2px solid gold;
            margin-top:10px;
            ">

            <h2 style="color:gold;">
            📋 Boarding Request
            </h2>

            <p><b>Owner:</b> {owner_name}</p>
            <p><b>Horse:</b> {horse_name}</p>
            <p><b>Age:</b> {horse_age}</p>
            <p><b>Gender:</b> {horse_gender}</p>
            <p><b>Duration:</b> {duration}</p>

            </div>
            """, unsafe_allow_html=True)

    # ================= VIEW MY HORSES =================

    elif owner_choice == "View My Horses":

        owner_name = st.text_input("Enter Owner Name")

        if st.button("View My Horses"):

            found = False

            for horse_id, horse in horses.items():

                if horse["owner_name"].lower() == owner_name.lower():

                    st.markdown(f"""
                    <div style="
                    background:#2c1d12;
                    padding:20px;
                    border-radius:20px;
                    border:2px solid gold;
                    margin-bottom:15px;
                    ">

                    <h2 style="color:gold;">
                    🐎 {horse["horse_name"]}
                    </h2>

                    <p><b>Horse ID:</b> {horse_id}</p>

                    <p><b>Owner:</b> {horse["owner_name"]}</p>

                    <p><b>Breed:</b> {horse["breed"].title()}</p>

                    <p><b>Age:</b> {horse["age"]}</p>

                    <p><b>Gender:</b> {horse["gender"].title()}</p>

                    <p><b>Status:</b> {horse["status"].title()}</p>

                    <p><b>Health Score:</b> {horse["health_score"]}/100</p>

                    <p><b>Horse Level:</b> {horse["horse_level"]}/100</p>

                    </div>
                    """, unsafe_allow_html=True)

                    found = True

            if found == False:
                st.error("No horses found for this owner.")




elif main_choice == "Trainee":
    st.header("Trainee Menu")

    trainee_choice = st.selectbox(
        "Choose Option",
        ["Register Trainee", "My Information", "Progress Report", "Complete Class"]
    )

    if trainee_choice == "Register Trainee":
        name = st.text_input("Enter your name:")
        age = st.number_input("Enter your age:", min_value=5, max_value=100)
        training_type = st.selectbox("Choose training type:", ["Jumping", "Racing", "For fun"])
        package = st.selectbox("Choose package:", [10, 20, 40])
        level = st.selectbox("Initial Assessment:", ["Beginner", "Intermediate", "Advanced"])

        if st.button("Register"):
            trainee_id = max(st.session_state.trainees.keys()) + 1
            trainer_name = assign_trainer(training_type, level)
            horse_name = assign_horse(level)

            st.session_state.trainees[trainee_id] = {
                "trainee_name": name,
                "age": age,
                "training_type": training_type,
                "level": level,
                "completed_classes": 0,
                "package": package,
                "assigned_trainer": trainer_name,
                "assigned_horse": horse_name,
                "license": False
            }

            st.success("Registration Successful.")
            st.write("Assigned Trainer:", trainer_name)
            st.write("Assigned Horse:", horse_name)

    elif trainee_choice == "My Information":
        name = st.text_input("Enter your name:")

        if st.button("Show Information"):
            found = False

            for trainee in st.session_state.trainees.values():
                if trainee["trainee_name"].lower() == name.lower():
                    st.write("Name:", trainee["trainee_name"])
                    st.write("Age:", trainee["age"])
                    st.write("Training Type:", trainee["training_type"])
                    st.write("Level:", trainee["level"])
                    st.write("Package:", trainee["package"])
                    st.write("Completed Classes:", trainee["completed_classes"])
                    st.write("Assigned Trainer:", trainee["assigned_trainer"])
                    st.write("Assigned Horse:", trainee["assigned_horse"])

                    if trainee["license"]:
                        st.success("License Status: Licensed")
                    else:
                        st.warning("License Status: Not Licensed")

                    found = True
                    break

            if found == False:
                st.error("Trainee not found.")

    elif trainee_choice == "Progress Report":
        name = st.text_input("Enter your name:")

        if st.button("Show Progress"):
            found = False

            for trainee in st.session_state.trainees.values():
                if trainee["trainee_name"].lower() == name.lower():
                    progress = (trainee["completed_classes"] / trainee["package"]) * 100
                    remaining = trainee["package"] - trainee["completed_classes"]

                    if remaining < 0:
                        remaining = 0

                    st.write("Completed Classes:", trainee["completed_classes"])
                    st.write("Remaining Classes:", remaining)
                    st.write("Progress:", str(round(progress)) + "%")
                    st.progress(min(progress / 100, 1.0))

                    found = True
                    break

            if found == False:
                st.error("Trainee not found.")

    elif trainee_choice == "Complete Class":
        name = st.text_input("Enter your name:")

        if st.button("Complete One Class"):
            found = False

            for trainee in st.session_state.trainees.values():
                if trainee["trainee_name"].lower() == name.lower():
                    trainee["completed_classes"] += 1
                    st.success("Class Completed Successfully.")

                    if trainee["completed_classes"] >= 40:
                        trainee["license"] = True
                        st.balloons()
                        st.success("Congratulations! You have earned your riding license.")

                    found = True
                    break

            if found == False:
                st.error("Trainee not found.")

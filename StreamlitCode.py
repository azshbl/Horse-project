import streamlit as st

st.set_page_config(
    page_title="Horse Stable System",
    page_icon="🐎",
    layout="centered",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@600;800&family=Inter:wght@400;500;600;700&display=swap');

* { font-family: 'Inter', sans-serif; }

.stApp {
    background: radial-gradient(circle at 20% 0%, #1a2e2a 0%, #0a1410 45%, #060908 100%);
    color: #eae3d3;
}

/* animated glow backdrop behind the title */
.hero-wrap {
    position: relative;
    text-align: center;
    padding: 38px 10px 28px 10px;
    margin-bottom: 10px;
    overflow: hidden;
    border-radius: 24px;
    background: linear-gradient(135deg, rgba(212,175,55,0.08), rgba(20,80,60,0.15));
    border: 1px solid rgba(212,175,55,0.25);
}

.hero-glow {
    position: absolute;
    top: -60px; left: 50%;
    width: 420px; height: 220px;
    transform: translateX(-50%);
    background: radial-gradient(ellipse, rgba(212,175,55,0.35), transparent 70%);
    filter: blur(10px);
    animation: pulse-glow 4s ease-in-out infinite;
    pointer-events: none;
}

@keyframes pulse-glow {
    0%, 100% { opacity: 0.55; }
    50% { opacity: 1; }
}

.main-title {
    position: relative;
    font-family: 'Cinzel', serif;
    font-size: 44px;
    font-weight: 800;
    background: linear-gradient(90deg, #f5e6c8, #d4af37, #8fd9b6, #d4af37, #f5e6c8);
    background-size: 300% auto;
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;
    animation: shimmer 6s linear infinite;
    letter-spacing: 1px;
    margin-bottom: 6px;
}

@keyframes shimmer {
    0% { background-position: 0% center; }
    100% { background-position: 300% center; }
}

.sub-title {
    position: relative;
    font-size: 15px;
    color: #9fcdb8;
    text-align: center;
    letter-spacing: 3px;
    text-transform: uppercase;
    font-weight: 600;
}

/* ---- glass cards ---- */
.card {
    position: relative;
    background: rgba(255,255,255,0.045);
    backdrop-filter: blur(6px);
    padding: 22px 24px;
    border-radius: 20px;
    border: 1px solid rgba(212,175,55,0.35);
    margin-bottom: 16px;
    box-shadow: 0 8px 24px rgba(0,0,0,0.45);
    transition: transform 0.18s ease, box-shadow 0.18s ease, border-color 0.18s ease;
    overflow: hidden;
}

.card::before {
    content: "";
    position: absolute;
    top: 0; left: 0; right: 0; height: 3px;
    background: linear-gradient(90deg, #d4af37, #5ec99a, #d4af37);
}

.card:hover {
    transform: translateY(-3px);
    border-color: rgba(94,201,154,0.6);
    box-shadow: 0 12px 30px rgba(94,201,154,0.18);
}

.card-title {
    font-family: 'Cinzel', serif;
    color: #f0d68a;
    font-size: 21px;
    font-weight: 700;
    margin-bottom: 10px;
    display: flex;
    align-items: center;
    gap: 8px;
}

.card-row {
    display: flex;
    justify-content: space-between;
    padding: 6px 2px;
    border-bottom: 1px dashed rgba(234,227,211,0.1);
    font-size: 14.5px;
}

.card-row:last-child { border-bottom: none; }

.card-label { color: #8fae9d; font-weight: 600; }
.card-value { color: #eae3d3; font-weight: 500; }

.badge {
    display: inline-block;
    padding: 3px 13px;
    border-radius: 20px;
    font-size: 11.5px;
    font-weight: 700;
    letter-spacing: 0.5px;
}
.badge-green { background: #2e8b57; color: white; }
.badge-blue  { background: #2a6f97; color: white; }
.badge-gold  { background: #d4af37; color: #1a1208; }
.badge-grey  { background: #444f4a; color: #ddd; }

hr.divider {
    border: none;
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(212,175,55,0.5), transparent);
    margin: 22px 0;
}

/* ---- nav pill buttons (sections) ---- */
.nav-tag {
    text-align: center;
    margin-bottom: 14px;
}
.nav-tag span {
    background: linear-gradient(135deg, rgba(94,201,154,0.18), rgba(212,175,55,0.12));
    border: 1px solid rgba(94,201,154,0.4);
    color: #cdebd9;
    padding: 5px 18px;
    border-radius: 30px;
    font-size: 13px;
    font-weight: 600;
    letter-spacing: 0.5px;
}

div.stButton > button {
    width: 100%;
    background: linear-gradient(135deg, #163a2f, #0e251d);
    color: #ecd9a0;
    border: 1px solid rgba(212,175,55,0.4);
    border-radius: 12px;
    font-weight: 600;
    padding: 10px 14px;
    transition: all 0.18s ease;
    box-shadow: 0 2px 10px rgba(0,0,0,0.3);
}

div.stButton > button:hover {
    background: linear-gradient(135deg, #d4af37, #b89020);
    color: #14201a;
    border-color: #f0d68a;
    box-shadow: 0 0 16px rgba(212,175,55,0.55);
    transform: translateY(-1px);
}

div.stButton > button:active {
    transform: translateY(0px) scale(0.98);
}

/* primary CTA buttons (submit/register/etc.) get a richer gradient via type=primary */
div.stButton > button[kind="primary"] {
    background: linear-gradient(135deg, #d4af37, #8fd9b6);
    color: #0a1410;
    border: none;
    font-weight: 800;
}
div.stButton > button[kind="primary"]:hover {
    box-shadow: 0 0 20px rgba(94,201,154,0.6);
}

[data-testid="stMetricValue"] { color: #d4af37; font-weight: 800; }
[data-testid="stMetric"] {
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(212,175,55,0.3);
    border-radius: 16px;
    padding: 12px;
}

h1, h2, h3 { color: #f0d68a; font-family: 'Cinzel', serif; }

.stSelectbox label, .stTextInput label, .stNumberInput label {
    color: #cdebd9 !important;
    font-weight: 600;
}

.stProgress > div > div > div {
    background-image: linear-gradient(to right, #d4af37, #5ec99a);
}

section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0e1a16, #060908);
    border-right: 1px solid rgba(212,175,55,0.2);
}
</style>
""", unsafe_allow_html=True)


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

owners = {
    1: {"owner_name": "Turki", "phone": "05012345671", "city": "Riyadh", "owner_type": "Stable Owner"},
    2: {"owner_name": "Nawaf", "phone": "05012345681", "city": "Riyadh", "owner_type": "Boarding Client"},
    3: {"owner_name": "Abdulaziz", "phone": "05012345691", "city": "Riyadh", "owner_type": "Boarding Client"},
    4: {"owner_name": "Nawaf.z", "phone": "05012345701", "city": "Riyadh", "owner_type": "Boarding Client"},
    5: {"owner_name": "Abdullah", "phone": "05012345711", "city": "Riyadh", "owner_type": "Boarding Client"},
    6: {"owner_name": "Khulod", "phone": "05012345721", "city": "Riyadh", "owner_type": "Boarding Client"},
    7: {"owner_name": "Abulaziz", "phone": "05012345731", "city": "Riyadh", "owner_type": "Boarding Client"}
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


def level_badge(level):
    colors = {"Advanced": "badge-green", "Intermediate": "badge-blue", "Beginner": "badge-grey"}
    cls = colors.get(level, "badge-grey")
    return f'<span class="badge {cls}">{level}</span>'


def status_badge(status):
    cls = "badge-gold" if status == "stable" else "badge-blue"
    return f'<span class="badge {cls}">{status.title()}</span>'


def license_badge(licensed):
    return '<span class="badge badge-green">Licensed</span>' if licensed else '<span class="badge badge-grey">Not Licensed</span>'


def render_card(title, icon, rows):
    rows_html = "".join(
        f'<div class="card-row"><span class="card-label">{label}</span>'
        f'<span class="card-value">{value}</span></div>'
        for label, value in rows
    )
    st.markdown(f"""
    <div class="card">
        <div class="card-title">{icon} {title}</div>
        {rows_html}
    </div>
    """, unsafe_allow_html=True)


def nav_tag(label):
    st.markdown(f'<div class="nav-tag"><span>📍 {label}</span></div>', unsafe_allow_html=True)


# ============== HERO HEADER ==============

st.markdown("""
<div class="hero-wrap">
    <div class="hero-glow"></div>
    <div class="main-title">🐎 Horse Stable Management System</div>
    <div class="sub-title">Elegance · Performance · Legacy</div>
</div>
""", unsafe_allow_html=True)


main_choice = st.sidebar.selectbox(
    "Role Selection",
    ["Admin", "Horse Owner", "Trainee"]
)

if main_choice == "Admin":

    st.header("Admin Menu")

    if "admin_choice" not in st.session_state:
        st.session_state.admin_choice = "Show Horses"

    st.subheader("Choose Option")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("🐴 Show Horses", use_container_width=True):
            st.session_state.admin_choice = "Show Horses"

        if st.button("📊 Horse Statistics", use_container_width=True):
            st.session_state.admin_choice = "Horse Statistics"

        if st.button("🏆 Best Trainer", use_container_width=True):
            st.session_state.admin_choice = "Best Trainer"

        if st.button("👤 Show Owners", use_container_width=True):
            st.session_state.admin_choice = "Show Owners"

    with col2:
        if st.button("🔍 Search Horse", use_container_width=True):
            st.session_state.admin_choice = "Search Horse"

        if st.button("👨‍🏫 Show Trainers", use_container_width=True):
            st.session_state.admin_choice = "Show Trainers"

        if st.button("🎓 Show Trainees", use_container_width=True):
            st.session_state.admin_choice = "Show Trainees"

    admin_choice = st.session_state.admin_choice

    st.markdown('<hr class="divider">', unsafe_allow_html=True)
    nav_tag(admin_choice)

    if admin_choice == "Show Horses":

        st.subheader("🐴 Stable Horses")

        for horse_id, horse in horses.items():
            render_card(
                horse["horse_name"], "🐎",
                [
                    ("Horse ID", horse_id),
                    ("Owner", horse["owner_name"]),
                    ("Breed", horse["breed"].title()),
                    ("Age", horse["age"]),
                    ("Gender", horse["gender"].title()),
                    ("Status", status_badge(horse["status"])),
                    ("Health Score", f'{horse["health_score"]}/100'),
                    ("Horse Level", f'{horse["horse_level"]}/100'),
                ]
            )

    elif admin_choice == "Search Horse":
        horse_name = st.text_input("Enter horse name:")

        if st.button("Search", type="primary"):
            found = False

            for horse_id, horse in horses.items():
                if horse["horse_name"].lower() == horse_name.lower():
                    st.success("Horse Found!")
                    render_card(
                        horse["horse_name"], "🐎",
                        [
                            ("ID", horse_id),
                            ("Owner", horse["owner_name"]),
                            ("Health Score", horse["health_score"]),
                            ("Horse Level", horse["horse_level"]),
                        ]
                    )
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

        col1, col2, col3, col4, col5 = st.columns(5)

        col1.metric("🐎 Total Horses", total_horses)
        col2.metric("🏠 Stable Horses", stable_count)
        col3.metric("📋 Boarding Horses", boarding_count)
        col4.metric("🌟 Arabian Horses", arabian_count)
        col5.metric("🌟 Frezian Horses", frezian_count)

    elif admin_choice == "Show Trainers":
        st.subheader("👨‍🏫 Trainers List")

        for trainer_id, trainer in trainers.items():
            lvl = trainer_level(trainer["performance_score"])
            render_card(
                trainer["trainer_name"], "👨‍🏫",
                [
                    ("Trainer ID", trainer_id),
                    ("Age", trainer["age"]),
                    ("Training Type", trainer["training_type"]),
                    ("Sessions Completed", trainer["sessions_completed"]),
                    ("Performance Score", f'{trainer["performance_score"]}/100'),
                    ("Level", level_badge(lvl)),
                ]
            )

    elif admin_choice == "Best Trainer":
        best = max(trainers.values(), key=lambda trainer: trainer["performance_score"])
        lvl = trainer_level(best["performance_score"])

        st.subheader("🏆 Best Trainer")
        render_card(
            best["trainer_name"], "🏆",
            [
                ("Performance Score", f'{best["performance_score"]}/100'),
                ("Sessions Completed", best["sessions_completed"]),
                ("Level", level_badge(lvl)),
            ]
        )

    elif admin_choice == "Show Trainees":
        st.subheader("🎓 Trainees List")

        for trainee_id, trainee in st.session_state.trainees.items():
            render_card(
                trainee["trainee_name"], "🎓",
                [
                    ("Trainee ID", trainee_id),
                    ("Age", trainee["age"]),
                    ("Training Type", trainee["training_type"]),
                    ("Level", level_badge(trainee["level"])),
                    ("Completed Classes", trainee["completed_classes"]),
                    ("Package", trainee["package"]),
                    ("Assigned Trainer", trainee["assigned_trainer"]),
                    ("Assigned Horse", trainee["assigned_horse"]),
                    ("License", license_badge(trainee["license"])),
                ]
            )

    elif admin_choice == "Show Owners":

        st.subheader("👤 Owners List")

        for owner_id, owner in owners.items():
            render_card(
                owner["owner_name"], "👤",
                [
                    ("Owner ID", owner_id),
                    ("Phone", owner["phone"]),
                    ("City", owner["city"]),
                    ("Owner Type", owner["owner_type"]),
                ]
            )


elif main_choice == "Horse Owner":

    st.header("🐎 Horse Owner Menu")

    if "owner_choice" not in st.session_state:
        st.session_state.owner_choice = "Boarding"

    st.subheader("Choose Option")

    ocol1, ocol2 = st.columns(2)

    with ocol1:
        if st.button("📋 Boarding", use_container_width=True):
            st.session_state.owner_choice = "Boarding"

    with ocol2:
        if st.button("🐴 View My Horses", use_container_width=True):
            st.session_state.owner_choice = "View My Horses"

    owner_choice = st.session_state.owner_choice

    st.markdown('<hr class="divider">', unsafe_allow_html=True)
    nav_tag(owner_choice)

    # ================= BOARDING =================

    if owner_choice == "Boarding":

        owner_name = st.text_input("Owner Name")
        phone = st.text_input("Phone Number")
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

        if st.button("Submit Boarding Request", type="primary"):

          

            if owner_name == "" or phone == "":
                st.error("Please enter owner name and phone number.")

            else:
                 st.success("Boarding Request Submitted Successfully")
            render_card(
                "Boarding Request", "📋",
                [
                    ("Owner", owner_name),
                    ("Phone", phone),
                    ("Horse", horse_name),
                    ("Age", horse_age),
                    ("Gender", horse_gender),
                    ("Duration", duration),
                ]
            )

    # ================= VIEW MY HORSES =================

    elif owner_choice == "View My Horses":

        owner_name = st.text_input("Enter Owner Name")

        if st.button("View My Horses", type="primary"):

            found = False

            for horse_id, horse in horses.items():

                if horse["owner_name"].lower() == owner_name.lower():
                    render_card(
                        horse["horse_name"], "🐎",
                        [
                            ("Horse ID", horse_id),
                            ("Owner", horse["owner_name"]),
                            ("Breed", horse["breed"].title()),
                            ("Age", horse["age"]),
                            ("Gender", horse["gender"].title()),
                            ("Status", status_badge(horse["status"])),
                            ("Health Score", f'{horse["health_score"]}/100'),
                            ("Horse Level", f'{horse["horse_level"]}/100'),
                        ]
                    )
                    found = True

            if found == False:
                st.error("No horses found for this owner.")


elif main_choice == "Trainee":
    st.header("Trainee Menu")

    if "trainee_choice" not in st.session_state:
        st.session_state.trainee_choice = "Register Trainee"

    st.subheader("Choose Option")

    tcol1, tcol2 = st.columns(2)

    with tcol1:
        if st.button("📝 Register Trainee", use_container_width=True):
            st.session_state.trainee_choice = "Register Trainee"

        if st.button("📈 Progress Report", use_container_width=True):
            st.session_state.trainee_choice = "Progress Report"

    with tcol2:
        if st.button("ℹ️ My Information", use_container_width=True):
            st.session_state.trainee_choice = "My Information"

        if st.button("✅ Complete Class", use_container_width=True):
            st.session_state.trainee_choice = "Complete Class"

    trainee_choice = st.session_state.trainee_choice

    st.markdown('<hr class="divider">', unsafe_allow_html=True)
    nav_tag(trainee_choice)

    if trainee_choice == "Register Trainee":
        name = st.text_input("Enter your name:")
        age = st.number_input("Enter your age:", min_value=5, max_value=100)
        training_type = st.selectbox("Choose training type:", ["Jumping", "Racing", "For fun"])
        package = st.selectbox("Choose package:", [10, 20, 40])
        level = st.selectbox("Initial Assessment:", ["Beginner", "Intermediate", "Advanced"])

        if st.button("Register", type="primary"):
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
            render_card(
                name, "🎓",
                [
                    ("Assigned Trainer", trainer_name),
                    ("Assigned Horse", horse_name),
                ]
            )

    elif trainee_choice == "My Information":
        name = st.text_input("Enter your name:")

        if st.button("Show Information", type="primary"):
            found = False

            for trainee in st.session_state.trainees.values():
                if trainee["trainee_name"].lower() == name.lower():
                    render_card(
                        trainee["trainee_name"], "🎓",
                        [
                            ("Age", trainee["age"]),
                            ("Training Type", trainee["training_type"]),
                            ("Level", level_badge(trainee["level"])),
                            ("Package", trainee["package"]),
                            ("Completed Classes", trainee["completed_classes"]),
                            ("Assigned Trainer", trainee["assigned_trainer"]),
                            ("Assigned Horse", trainee["assigned_horse"]),
                            ("License Status", license_badge(trainee["license"])),
                        ]
                    )
                    found = True
                    break

            if found == False:
                st.error("Trainee not found.")

    elif trainee_choice == "Progress Report":
        name = st.text_input("Enter your name:")

        if st.button("Show Progress", type="primary"):
            found = False

            for trainee in st.session_state.trainees.values():
                if trainee["trainee_name"].lower() == name.lower():
                    progress = (trainee["completed_classes"] / trainee["package"]) * 100
                    remaining = trainee["package"] - trainee["completed_classes"]

                    if remaining < 0:
                        remaining = 0

                    render_card(
                        trainee["trainee_name"], "📈",
                        [
                            ("Completed Classes", trainee["completed_classes"]),
                            ("Remaining Classes", remaining),
                            ("Progress", f"{round(progress)}%"),
                        ]
                    )
                    st.progress(min(progress / 100, 1.0))

                    found = True
                    break

            if found == False:
                st.error("Trainee not found.")

    elif trainee_choice == "Complete Class":
        name = st.text_input("Enter your name:")

        if st.button("Complete One Class", type="primary"):
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

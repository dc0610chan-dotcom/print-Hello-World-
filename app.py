import streamlit as st

# --- PAGE NAVIGATION ---
st.set_page_config(page_title="Hackathon Website", layout="wide")
pages = ["Home", "Career Quiz", "Writing on the Wall", "Creators"]
page = st.sidebar.radio("Navigate", pages)

# --- HOME PAGE ---
if page == "Home":
    st.title("Welcome to DJM's Hackathon Website!")
    st.markdown("""
    High schoolers are pressured into university or nothing thinking before they even know who they are. This leads to anxiety, debt, and misguided life choices.
Open Door helps them discover a direction that fits the life they actually want, not just the path everyone expects.
    """)
 ####bottom of home page  
    st.markdown("**External Resources:**")
    st.markdown("""
    - [Support Helpline](#)
    - [Inspiring Films/Art](#)
    - [Social Media Communities](#)
    """)

# --- CAREER QUIZ PAGE ---
elif page == "Career Quiz":
    st.title("Career Quiz")
    st.markdown("Answer the questions to get suggestions that match your interests!")
# question 1 - 20 not including personality
# --- Initialize scores for all NAICS industries ---
if "scores" not in st.session_state:
    st.session_state.scores = {
        "Agriculture, Forestry, Fishing and Hunting": 0,
        "Mining, Quarrying, and Oil and Gas Extraction": 0,
        "Utilities": 0,
        "Construction": 0,
        "Manufacturing": 0, 
        "Wholesale Trade": 0,
        "Retail Trade" 
        "Transportation and Warehousing": 0,
        "Information and Cultural Industries": 0,
        "Finance and Insurance": 0,
        "Real Estate and Rental and Leasing": 0,
        "Professional, Scientific and Technical Services": 0,
        "Management of Companies and Enterprises": 0,
        "Administrative and Support, Waste Management and Remediation Services": 0,
        "Educational Services": 0,
        "Health Care and Social Assistance": 0,
        "Arts, Entertainment and Recreation": 0,
        "Accommodation and food services": 0,
        "Public AdministratFon": 0
        "Other Services (excluding Public Administration)": 0,    }
i 0    
#urban dictionary type shit

scores = st.session_state.scores
agri = "Agriculture, Forestry, Fishing and Hunting"
mining = "Mining, Quarrying, and Oil and Gas Extraction"
uti = "Utilities"
const = "Construction"
manuf = "Manufacturing"
wholesale = "Wholesale Trade"
retail = "Retail Trade"
transport = "Transportation and Warehousing"
infoind = "Information and Cultural Industries"
finance = "Finance and Insurance"
real_estate = "Real Estate and Rental and Leasing"
professional = "Professional, Scientific and Technical Services"
management = "Management of Companies and Enterprises"
admin = "Administrative and Support, Waste Management and Remediation Services"
education = "Educational Services"
health = "Health Care and Social Assistance"
arts = "Arts, Entertainment and Recreation"
food = "Accommodation and Food Services"
public = "Public Administration"ng Public Administration)
other = "Other Services (excluding Public Administration)"


#Question 1
q1 = st.radio(
    "If you had a free day right now, what would you do first?",
    ("Call or spend time with someone you love", "Clean / organize your space",
    "Take a nap / relax", "Watch your favorite show or media", "Explore your town / go outside" )
            )
    
#Question 2
q2 = st.radio(
    "What are your 3 favorite hobbies?",
    ("Creating art, music, or writing", "Playing or watching sports", "Volunteering / helping others",
     "Gaming, coding, or digital projects", "Building, fixing, or crafting", "Exploring nature / outdoor activities" )
            )

#Question 3
q3 = st.radio( 
    "What kind of hobby really excites you", 
    ("Making something with your hands (crafts, building, cooking)", "Expressing yourself creatively (music, writing, art)",
    "Playing or watching sports / staying active", "Solving puzzles or learning new concepts", "Spending time with friends / social activities",
    "Being outdoors / exploring nature")
            ) 
#Question 4
q4 = st.radio(
    " How do you usually spend your evenings?",
    ("Watching shows or movies", "Reading or learning something new", "Hanging out with friends", "Doing hands-on projects (crafts, cooking, building)",
    "Planning / organizing your week", "Relaxing in nature / exercising")
            )

    #Question 5
q5 = st.radio(
    "Which of these sounds like your ideal weekend?", 
    ("Attending a concert, art exhibit, or performance", "Hosting or attending a dinner / party", "Working on a personal project or hobby",
    "Going on a short trip or exploring your town", "Volunteering or helping a local cause", "Staying in and relaxing")
            )
    
#Question 6
q6 = st.radio(
    "What’s your ideal work setting?", 
    ("A busy office with clear tasks and schedules", "A creative studio or workshop", "Outdoors or in nature", "Flexible coworking spaces / cafes / changing environments", 
     "A calm, quiet room with minimal interruptions", "High-energy, social, hands-on environment")
            )
    
#Question 7 
q7 = st.radio(
    "What is your approach to tasks?", 
    ("Follow a clear step-by-step plan", "Work independently and creatively", "Collaborate and brainstorm with others", "Jump in and figure things out as you go", 
    "Focus on precision and details", "Focus on people’s needs and feelings")
            )
    
    #Question 8
q8 = st.radio(
        "What is your preferred pace of work?",
        ("Fast, dynamic, and changing constantly", "Steady but challenging", "Slow, deliberate, and structured", "Flexible, adaptable depending on the day", "Energetic and social", 
         "Calm and focused")
                )
    
    #Question 9
q9 = st.radio(
        "What is your preferred level of supervision?", 
        ("Completely independently", "Mostly independently, occasional check-ins", "In a team with shared responsibility", "With clear instructions and supervision", 
         "Rotating between teamwork and solo work", "Being guided by a mentor or leader")
                )
    
    #Question 10
q10 = st.radio(
        "When do you do your best work?", 
        ("Early in the morning, when everything is calm", "Late at night, when I'm inspired", "In short bursts with lots of variety", "When I’m actively moving or hands-on", 
         "When collaborating with others", "When I can experiment and try new ideas")
                    )
    
    #Question 11
q11 = st.radio(
        "How do you usually recharge after a busy day?", 
        ("Spending time with close friends or family", "Being alone reading, gaming, or watching media", "Going for a walk or doing something active", "Trying a new hobby or exploring something new", 
         "Volunteering or helping someone", "Organizing or planning your space")
                    )
    
    #Question 12
q12 = st.radio(
        "In a social gathering, which describes you best?", 
        ("I thrive in large groups and enjoy meeting new people", "I prefer small groups of close friends", "I like being around people but also need breaks alone",
         "I mostly observe rather than actively participate", "I avoid social gatherings whenever possible", "I adapt easily to any size or type of group")
                )
    
    #Queston 13
q13 = st.radio(
         "How do you handle energy demands during a busy week?", 
         ("I’m energized by activity and social interaction", "I manage energy with planned breaks", "I focus best when calm and consistent", "I like alternating high-energy bursts with downtime", 
          "I prefer low-energy, predictable routines", "I adapt my energy to whatever the day demands")
                )
    
    #Question 14
q14 = st.radio(
         "When exploring new experiences, which sounds most like you?", 
         ("I dive in headfirst and love variety", "I prefer to try a few new things at a time", "I stick to what I know", "I plan new experiences carefully before doing them", 
          "I like spontaneous adventures but also enjoy downtime", "I mostly observe new experiences rather than participate")
                )
    
    #Question 15
q15 = st.radio(
         "When faced with a new challenge, what's your first instinct?", 
         ("Analyze the data and look for patterns", "Brainstorm creative solutions, even unusual ones", "Ask others for input and collaborate", 
          "Tackle it hands-on and learn by doing", "Follow step-by-step instructions carefully", "Take time to observe and reflect before acting")
                )

   #Question 16
q16 = st.radio(
        "What scares you most about trying something new?",
        ("Failing and looking incompetent", "Not knowing where to start", "That it might be boring or repetitive", "It will be physically demanding", 
        "Feeling socially awkward or judged", "Making a mistake that affects others")
                )
    
    #Question 17
q17 = st.radio(
         "What excites you most about trying something new?", 
         ("Solving a problem or overcoming a challenge", "Learning something new and expanding skills", "Being creative and trying something original", 
          "Meeting or working with new people", "Getting hands-on experience", "Exploring the unknown or unexpected") 
                 )
    
    #Question 18
q18 = st.radio(
         "Which of these motivates you most in your career?", 
         ("Making a positive difference in other people’s lives", "Achieving financial success", "Gaining recognition or fame", 
          "Creating stability for yourself and loved ones", "Exploring new ideas and creative possibilities", "Building a family or close personal relationships alongside work")
                    )

    #Question 19
q19 = st.radio(
         "Which of these outcomes would make you feel most fulfilled?", 
         ("Helping or mentoring others", "Earning wealth or material success", "Becoming well-known or influential", "Feeling secure and stable in your life", 
          "Making something new, original, or impactful", "Building strong relationships or a family")
                )

    #Question 20
q20 = st.radio(
         "Which of these matters most to you in your work/life balance?", 
         ("Helping others and contributing to society", "Financial reward and material comfort", "Fame, recognition, or prestige", "Security and stability", 
          "Freedom to explore new opportunities", "Family, friends, and personal relationships")
                )

    
    
    
    ###don't touch it likes randomly breaking####
  if not st.session_state.q1_answered:
    if st.button("Submit Question 1"):
        if q1 == "Call or spend time with someone you love":
            st.session_state.scores["Health care and social assistance"] += 1
                        st.session_state.scores[":
        d services"] += 1
        elif q1 == "Clean / organiz            st.session_state.scores[y":
            st.session_state.d suppoarts services"] += 1
            st.session_state.scores[professional        elif q1 == "Learn a new hobbinfoind] += 1nt and recreation"] += 1
            st.session_state.scores[uroal, scientific and technical services"] += 1
            st.session_state.scores[          
t           st.session_state.scores[adminscores["Information and cultural industries"] += 1
        else:  # Take a nap / relax
util += 1ist.session_state.q1_answeredpublic        st.experimental_rerun()
utilities        elif page == "Writing on the Wall":
    st.t
    if not st.session_state.q1_answered:
        if st.button("Submit Question 2")
            if q2 == "Creating art, music, or writing":
                st.session_st2te.scores["Inform] ltural"] += 1
                st.session_state.scores["Art] +=, Entertainment and Recreation"] += 1
            elif q2 == "Playing or watching sports":
                st.session_state.scores[infoindecreation"] += 1
                st.session_state.scores[arts= 1
            elif q2 == "Volunteering / helping others":
            elif q2 == "Gaming, coding, arts]            elifst.session_state.scores[health] += 1
                 q2 == "Building, fixingfood            else: #Exploring nature / outdoor activitie
                st.session_state.scores[health] += 1
                st.session_state.scores[education] += 1
                st.session_state.scores[public] += 1s 
        

                st.session_state.scores[infoind] += 1
                st.session_state.scores[professional] += 1

                st.session_state.scores[manu] += 1
                st.session_state.scores[const] += 1
                st.session_state.scores[uti] += 1

  st.sess      ion_state.scores["Profestrans                st.session_state.scores[agri] += 1
                st.session_state.scores[arts] += 1

    if not st.session_state.q3_answered:
        if st.button("Submit Question 3")
            if q3 == "Making something with your hands (crafts, building, cooking)":
                st.session_state.scores[manu] += 1
                st.session_state.scores[arts] += 1
                st.session_state.scores[const] += 1
            elif q3 == "Expressing yourself creatively (music, writing, art)":
                st.session_state.scores[arts] += 1
                st.session_state.scores[infoind] += 1
            elif q3 == "Playing or watching sports / staying active":
                st.session_state.scores[food] += 1
                st.session_state.scores[arts] += 1
                st.session_state.scores[health] += 1
            elif q3 == "Solving puzzles or learning new concepts":
                st.session_state.scores[professional] += 1
                st.session_state.scores[infoind] += 1
                st.session_state.scores[education] += 1
            elif q3 == "Spending time with friends / social activities":
                st.session_state.scores[health] += 1
                st.session_state.scores[food] += 1
            else: #Being outdoors / exploring nature
                st.session_state.scores[trans] += 1
                st.session_state.scores[agri] += 1
                st.session_state.scores[arts] += 1

    if not st.session_state.q4_answered:
        if st.button("Submit Question 4")
            if q4 == "Watching shows or movies":
                st.session_state.scores[arts] += 1
                st.session_state.scores[infoind] += 1
            elif q4 == "Expressing yourself creatively (music, writing, art)":
                st.session_state.scores[education] += 1
                st.session_state.scores[infoind] += 1
                st.session_state.scores[professional] += 1
            elif q4 == "Hanging out with friends":
                st.session_state.scores[health] += 1
                st.session_state.scores[food] += 1
            elif q4 == "Doing hands-on projects (crafts, cooking, building)":
                st.session_state.scores[manu] += 1
                st.session_state.scores[arts] += 1
                st.session_state.scores[const] += 1
            elif q4 == "Planning / organizing your week":
                st.session_state.scores[admin] += 1
                st.session_state.scores[public] += 1
                st.session_state.scores[management] += 1
            else: #Relaxing in nature / exercising
                st.session_state.scores[trans] += 1
                st.session_state.scores[agri] += 1
                st.session_state.scores[food] += 1


    if not st.session_state.q5_answered:
        if st.button("Submit Question 5"food            if q5 == "Attending a concerhealthexhibi                st.session_state.scores[infoind] += 1
            elif q5 == "Hosting or attenprofessional dinne
                st.session_state.scores[manu] += 1r / party":
                st.session_state.scores[artsation] += 1
                st.session_state.scores[infoind] += 1
                st.session_state.scores[agriessional] += 1
            elif q5 == "Working on a perartsl project or hobby":
                st.session_state.scores[transh] += 1
                st.session_state.scores[food] += 1
            elif q5 == "Going on a shortpublic or exploring your town":
                st.session_state.scores[health+= 1
                st.session_state.scores[education
                st.session_state.scores[const] += 1
            elif q5 == "Volunteering or uting a local cause":
                st.session_state.scores[publicn] += 1
                st.session_state.scores[otheric] += 1
                st.session_state.scores[management] += 1

    if not st.session_state.q6_answered:
        if st.button("Submit Question 6")
            if q6 == "Attending a concert, art exhibit, or performance":
                st.session_state.scores[arts] += 1
                st.session_state.scores[infoind] += 1
            elif q6 == "Hosting or attending a dinner / party":
                st.session_state.scores[food] += 1
                st.session_state.scores[health] += 1
            elif q6 == "Working on a personal project or hobby":
                st.session_state.scores[professional] += 1
                st.session_state.scores[manu] += 1
                st.session_state.scores[arts] += 1
            elif q6 == "Going on a short trip or exploring your town":
                st.session_state.scores[agri] += 1
                st.session_state.scores[arts] += 1
                st.session_state.scores[trans] += 1
            elif q6 == "Volunteering or helping a local cause":
                st.session_state.scores[public] += 1
                st.session_state.scores[health] += 1
                st.session_state.scores[education] += 1
            else: #High-energy, social, hands-on environment
                st.session_state.scores[uti] += 1
                st.session_state.scores[public] += 1
                st.session_state.scores[other] += 1            else: #Staying in and relaxing
                st.session_state.scores[trans] += 1
                st.session_state.scores[agri] += 1
                st.session_state.scores[food] += 1



































    st.title("Writing on the Wall")
    st.markdown("Leave anonymous messages for other students. Messages are moderated for language.")

    # Input new message
    new_message = st.text_area("Write your message here:")
    if st.button("Post Message"):
        if any(bad_word in new_message.lower() for bad_word in ["bitch", "fuck", "shit", "dick", "ass", "cunt", "pussy",]):  # simple moderation
            st.error("Message contains inappropriate language.")
        else:
            st.success("Message posted!")
            # For now, we'll just show it on the page (in memory)
            if "messages" not in st.session_state:
                st.session_state.messages = []
            st.session_state.messages.append(new_message)

    # Display messages
    if "messages" in st.session_state:
        st.markdown("**Previous Messages:**")
        for msg in st.session_state.messages:
            st.markdown(f"- {msg}")

# --- CREATORS PAGE ---
elif page == "Creators":
    st.title("Meet the Team")
    st.markdown("""
    - **Mikaela** – Stuff (Year 1 Computer Science Student)
    - **Davin** – Leader and more stuff (Year 1 Computer Science Student)
    - **Joshua** – Other stuff (Year 1 Computer Science Student)
    
    This team built this website to give students a reflective, interactive space to explore life choices.
    """)
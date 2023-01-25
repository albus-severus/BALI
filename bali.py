import streamlit as st
import pandas as pd



st.write("""
# Bali Itinerary From India
""")

st.sidebar.text("Few Images")
from PIL import Image
img = Image.open("bg.JPG")
st.sidebar.image(img)



st.markdown("""
<p align="right": style="font-size:35px;color:blue;font-family: Papyrus;"><i><u>by Saurabh Kumar</u></i>""", unsafe_allow_html=True)
st.markdown("""
<body style='text-align: center; color: blue;'>
<ul>
<li> <p align="justify": style="color:black;">Bali is a small island and a province of Indonesia. The provincial capital, Denpasar, is the most populous city.Bali is Indonesia's main tourist destination.It is one of the bigger south east asian nations and is naturally closer to the equator.

</li><li><p align="justify">Being just 8 degrees south of the equator, Bali has a fairly even climate all year round. Average year-round temperature stands at around 30 °C (86 °F) with a humidity level of about 85%. 

</li><li><p align="justify">  We visited Bali in the 2nd week of december 2022, It was told that this is the monsoon season and the weather would be unpredictible, End of summer means heat would be at its peak.However the actual scenario was different. In our 8-9 days stay we only faced rain twice both of 15-20 mins duration.

</li><li> <p align="justify">Advantages of going to bali in a non-peak season is that the crowd is less, Hotels are cheaper. Bali is a place which is dedicated for tourists only, People are very friendly, helpful, soulful and religious. We enjoyed a lot and it was truly a worthy "first foreign trip" for us. 

</li><li> <p align="justify">Lets move ahead and discuss Bali Itenerary, Budget, Hotels, Transportation, Food, Activities, etc. Check Out the Tabs Below. . . I have tried to jam as much information as i could remember and hopefully it could be of some help to the readers. Have a Great Trip ....

</li></body>""", unsafe_allow_html=True)

from PIL import Image
img4 = Image.open("bali.jpg")
st.sidebar.image(img4)

from PIL import Image
img5 = Image.open("bali2.jpg")
st.image(img5)



tab1,tab2,tab3,tab4,tab5,tab6,tab7 = st.tabs(["Prerequisites & tips","Day 1 & 2","Day 3 & 4","Day 5 & 6","Day 7, 8 & 9","Expenditure","Random Tips"])


with tab1: 
    st.markdown("""<p align="justify": style="font-size:15px;color:blue;font-family:Comic-Sans;">
    <li>Take printouts of tickets, Xerox of passport, Vaccination Certificates, Prebooked Hotel stays (1-2 days),and 35$ cash/person for visa (if possible).
    <li>For Health Declaration Download PeduliLindungi app on your mobile phone. as Airport wifi at Denpasar airport may be weak. """, unsafe_allow_html=True)
    from PIL import Image
    img6 = Image.open("pedungi.jpg")
    st.image(img6)
    st.markdown("""<p align="justify": style="font-size:15px;color:blue;font-family:Comic-Sans;">
    <li> Also download utility apps like Gojek, Grab, Klook etc (like ola, uber, swiggy) etc and integrate Niyo card in it to avail cashless taxi, food, activity bookings.  
    <li> Download Offline Google maps (300-400 mb) of entire region of Bali, Nusa & Gili islands. It helps a lot.
    <li> For transcations the best card i found was that of Neo Global debit card. I had opened a bank account with  Neo global app and deposited Rs 5000 via UPI. On depositing Rs 5000 they 
    will automatically send the physical debit card withing 6-7 days. It worked on all the POS machines not only in bali but also on airports of Thailand & Malaysia with zero forex charges. ATM Transaction costed
    Rs. 118 (with tax) per withdrawl. With the help of Neo App , i could also track the total expenditure incurred.
    <li> For driving or renting vehicles in Bali, Its better to carry an International Driving Permit. Apply it with your state RTO . 
    Takes around 1 week and Costs around Rs. 1000. Go to below website & Go to your DL Issuing State & Follow the lead""", unsafe_allow_html=True)
    from PIL import Image
    img7 = Image.open("idp.jpg")
    st.image(img7)
    

#day1-9
with tab2:
#  st.subheader("Day 1 & 2 ")
#  st.markdown("""<p align="justify": style="font-size:15px;color:red;font-family: Papyrus;"><i><u>Day One & TWO With Suggestions</u></i>""", unsafe_allow_html=True)
 
 col1, col2 = st.columns(2)
 col1.subheader("Day1")
 col1.markdown("""<span style="word-wrap:break-word;">Arriving at Denpasar Airport. <br> <li> Proceed to hotel by Cab. <br> <li> Buy sim card, Explore Local beach like Kuta Beach or Jimbaran Beach in the evening. <li> Dinner at Jimbaran Beach or Any local Resturants nearby. </span>""", unsafe_allow_html=True)
 
 col2.subheader("Day2")
 col2.markdown("""<span style="word-wrap:break-word;">After Breakfast - Local Sight Seeing Uluwatu Temple, Garuda Vishnu Park, Tanha Lot <br> <li> Ulluwatu Temple in First Half . (Towards South Bali). <br>
 <li> Garuda Vishnu Park after Lunch . <br> <li> Tanha Lot Temple in the evening - (Sunset is awesome here !) </span>""", unsafe_allow_html=True)
 
 st.markdown("""<p align="justify": style="font-size:15px;color:blue;font-family:Comic-Sans;">Suggestion#1 Buy Local sim card (many shops available) with around 20-25 GB internet Preferably "Telcomsel" as it has good service in both set of islands i.e Nusa & Gilli. (Also carry a sim removal pin)
 <br><br>Suggestion#2 For Vegetarians , Booking hotel in market area of Kuta is better as Indian resturants are available. May search for INDIAN FOOD PUNJABI GRILL,QUEENS OF INDIA etc on google & Accordingly book hotels nearby. For Non Vegetarians, Staying anywhere wont be an issue as non veg food is available everywhere.
 <br><br>Suggestion#3 For hotels we had stayed in Hotel Jimbaran Beach Bay Resort near jimbaran beach as we had planned for dinner on Jimbaran Beach. During return we stayed in Hotel Grand IXORA. There are thousands of options and one can book any hotel from Agoda, Booking.com etc based on budget, location (Near Kuta beach or Jimbaran Beach), Food etc.
 <br><br>Suggestion#4 For Taxi we relied on GOJEK and GRAB . Make sure to Add your Neo Global Debit card in these apps beforehand to save Forex Charges and Cash.
 <br><br>Suggestion#5 If using Neo Global Card then it charges Rs 118 per ATM transaction. So its better to take out the maximum amount allowed in the machine for each tyransaction. Some ATMs allow Maximum 1000000 IDR while some allow Maximum of 2500000 IDR (Google those ATMs) . Also try to swipe the card wherever available in restuarants, shops etc.
 </p>""", unsafe_allow_html=True)
 from PIL import Image
 imga = Image.open("uluwatu.jpg")
 st.image(imga)
 st.markdown("""<p align="center">Uluwatu Temple""", unsafe_allow_html=True)
 from PIL import Image
 imgb = Image.open("garuda.jpg")
 st.image(imgb)
 st.markdown("""<p align="center">Garuda Visnu Kencana statue""", unsafe_allow_html=True)
 from PIL import Image
 imgc = Image.open("tanha.jpg")
 st.image(imgc)
 st.markdown("""<p align="center">Tanha Lot Temple""", unsafe_allow_html=True)
 



with tab3:
#  st.subheader(" Day 2 & 3")
#  st.markdown("""<p align="justify": style="font-size:15px;color:red;font-family: Papyrus;"><i><u>Day One & TWO With Suggestions</u></i>""", unsafe_allow_html=True)
 
 col3, col4 = st.columns(2)
 col3.subheader("Day3")
 col3.markdown("""<span style="word-wrap:break-word;"><b><u> NUSA Penida </b></u> <br>Early Checkout & Leave for SANUR HARBOUR. 
 <br> <li> 30-40 Mins journey (by speedboat) to Nusa Penida Island  
 <br> <li> East & west trip - Diamond Beach , ATUH Beach, Tree house (Skipped), Kelingking beach, Angel Billabong , Broken Beach .
  <br> <li> Drop at Hotel in Nusa, Dinner at local Resturants or Hotel nearby. </span>""", unsafe_allow_html=True)
 
 col4.subheader("Day4")
 col4.markdown("""<span style="word-wrap:break-word;">Early Checkout & Reach Banjar NYUH Harbour and book locally for a ferry to GILLI Trawangan Islands. (MUST VISIT). 400000 IDR Per person . <br>
 <li>Book hotel and cycle  locally - Hotels around 2000 INR & Cycle 400 INR per day . <br>
  <li>Enjoy beach, Cycle ride and Vibe the entire day . <br>
  <li>Book snorkeling, Scooba etc for the next day with any local shops (Many options available) - We paid 1.2 Million IDR (6500 INR) for two people private snorkeling with GO PRO Camera.  </span>""", unsafe_allow_html=True)
 
 st.markdown("""<p align="justify": style="font-size:15px;color:blue;font-family:Comic-Sans;"><br> Suggestion#1-(day3)--Bargain with Local travel agents AT SANUR HARBOUR for best fare to go to NUSA PENIDA Island . We paid 200000 IDR per person. (1100 INR) Leaving time - 9 am Local
 <br><br>Suggestion#2-(day3)--Upon arrival at Nusa Penida - Various taxi drivers will surround you for Sight seeing packages.  Ask for both east & west trip and Bargain with confidence . We paid 650000 IDR (3500 INR) for full day taxi. 
 <br><br>Suggestion#3-(day3)--Book hotel in market area  for better food availability , the driver will help in this if not booked previously.  We lived in SANTEN BEACH BUNGLOWS, which was on the beach but little secluded. Hotels near Banjar NYUH Harbor area will be better in case transfer needed to gilli islands the next morning. 
 </body>""", unsafe_allow_html=True)
 from PIL import Image
 imgg = Image.open("speedboat.jpg")
 st.image(imgg)
 st.markdown("""<p align="center">Speed Boat""", unsafe_allow_html=True)
 from PIL import Image
 imgd = Image.open("diamond.jpg")
 st.image(imgd)
 st.markdown("""<p align="center">Diamond Beach""", unsafe_allow_html=True)
 from PIL import Image
 imge = Image.open("kellingking.jpg")
 st.image(imge)
 st.markdown("""<p align="center">Kellingking Beach""", unsafe_allow_html=True)
 from PIL import Image
 imgf = Image.open("broken_beach.jpg")
 st.image(imgf)
 st.markdown("""<p align="center">Broken Beach""", unsafe_allow_html=True)
#  st.image("one.jpg",width =500 )

with tab4:
 col5, col6 = st.columns(2)
 col5.subheader("Day5")
 col5.markdown("""<span style="word-wrap:break-word;">Leave as early in the morning as possible for snorkeling.
 <li>3 snorkeling points - Underwater statue, Turtle point - Lunch at Gilli Air  & Then 1 or 2 other points as per request . 
 <li>Return in afternoon to Hotel. 
 <li>Enjoy beach, Cycle ride and Vibe the rest of the  day again. Gili T is a party island with beautiful view & live music.    <li>
 Also book the ticket for ferry ride to UBUD the next day . </span>""", unsafe_allow_html=True)
 
 col6.subheader("Day6")
 col6.markdown("""<span style="word-wrap:break-word;">After breakfast leave for harbour & reach Padang bai Harbour (Ubud) 
 <li> Prebook the cab to Ubud. <li> Book hotel in ubud near "ubud central" or " "ubud palace". <li> Places to explore near Ubud - Monkey forest , Ubud Palace etc. We explored the city and local market & resturants by local scooty. <li>Book any local cab service for the next two days .
 </span>""", unsafe_allow_html=True)
 
 
 
 from PIL import Image
 imgh = Image.open("gili.jpeg")
 st.image(imgh)
 st.markdown("""<p align="center">Gili Islands""", unsafe_allow_html=True)
 from PIL import Image
 imgi = Image.open("statue.jpg")
 st.image(imgi)
 st.markdown("""<p align="center">Snorkeling Point - Underwater Statue""", unsafe_allow_html=True)
 from PIL import Image
 imgj = Image.open("turtle.jpg")
 st.image(imgj)
 st.markdown("""<p align="center">Snorkeling- Turtle Point""", unsafe_allow_html=True)
#   st.image("dbz.jpg",width =500 )



with tab5:
 col7, col8, col9 = st.columns(3)
 col7.subheader("Day7")
 col7.markdown("""<span style="word-wrap:break-word;">Leave as early in the morning as possible. 
 <li>From taxi Bali Swings - we went to alas haroom. Reach early to avoid crowd. 
 <li>After that Tegalalang rice field
 <li>After that Nearby waterfalls ( There are many ) eg. Kanto lampo waterfall, Tegenungan waterfall  <li>
 Tirta Empul Temple <li> Return to UBUD in the evening </span>""", unsafe_allow_html=True)
 
 col8.subheader("Day8")
 col8.markdown("""<span style="word-wrap:break-word;">Leave Hotel at around 4-5 am for Lempuyang Temple TO AVOID RUSH. <li> Lempuyang Temple <li> Tukad Cepung waterfall, Tirta Ganga & Many sight seeing places, Waterfalls in between. <li>
 Drop at Hotel in Kuta or Ubud as per plan <li> We had booked our last night stay back in Kuta and had requested the taxi driver to drop us in Kuta instead of Ubud . 
 <li> 2 days ubud taxi fare - 1.4 Million IDR <li> Evening spent at Kuta beach </span>""", unsafe_allow_html=True)
 

 col9.subheader("Day9")
 col9.markdown("""<span style="word-wrap:break-word;">Breakfast , Shopping at nearby market , Checkout & leave for Airport. 
 We had flight at 3 pm </span>""", unsafe_allow_html=True)
 
 
 from PIL import Image
 imgk = Image.open("swing.jpg")
 st.image(imgk)
 st.markdown("""<p align="center">Bali Swings""", unsafe_allow_html=True)
 from PIL import Image
 imgl = Image.open("kanto.jpg")
 st.image(imgl)
 st.markdown("""<p align="center">Kanto lampo waterfall""", unsafe_allow_html=True)
 from PIL import Image
 imgm = Image.open("tirtaempul.jpg")
 st.image(imgm)
 st.markdown("""<p align="center">Tirta Empul Temple""", unsafe_allow_html=True)
 from PIL import Image
 imgn = Image.open("tukad.jpg")
 st.image(imgn)
 st.markdown("""<p align="center">Tukad Cepung waterfall""", unsafe_allow_html=True)
 imgo = Image.open("tirtaganga.jpg")
 st.image(imgo)
 st.markdown("""<p align="center">Tirta Ganga""", unsafe_allow_html=True)


 


with tab6:

 from PIL import Image
 img3 = Image.open("expenditure.jpg")
 st.image(img3)


with tab7:
    st.markdown("""<p align="justify": style="font-size:15px;color:blue;font-family:Comic-Sans;">
    <br><br> #side_tips_for_middle_class: In international Airports , its a scam that they dont allow water after security area but you can take the empty bottle by saying that i need it . In security area and Flight they charge around 150-200 rs for water of 600ml . So better to carry empty bottle and fill from the freely available water filter in the boarding area.
    <br><br> Never, Never Exchange money at the airport or in general shady money exchange shops who claim zero charges. Better use your trusted cards (Preferably Good Forex cards) and take out cash when required from ATMs.
    <br><br> We skipped few places like Mount Batur trek, Monkey forest in Ubud. Tree House in Nusa and Garuda Park in Denpasar/Kuta. 
    <br><br> Nasi Goreng is "almost" the national food in bali which is basically Fried rice with egg, chicken etc . Mie goreng is fried noodles with egg, chicken etc. Maggi is not available and lookout for beef in their noodles or even chips. Never try pizza .In general a lack of spices and even salt may be noticed in Indonesian food. Because no food is better than indian food. (Seriously !!!, Carry few packets of maggi masala , haha)
    <br><br> Indian restuarnts were available in Kuta as well as in Ubud . However they were understandably costly as compared to India. 
    <br><br> Carry general medicines, and mosquito repellent - Odomos (However we didnt need but many suggest the same. )
    <br><br>  """, unsafe_allow_html=True)

<h1 align="center">MartianFiction</h1>

---

## 👥 Team Members:
- Jorge Jacuinde Mayés / JuipoMinutes
- Ashley Dafne Aguilar Salinas/ [AshleyDafneAguilar](https://github.com/AshleyDafneAguilar)
- Sofía García De La Rosa / SofiaDeLaRosa

---

### MartianFiction/MartianFiction is licensed under the MIT License see [LICENSE](https://github.com/MartianFiction/MartianFiction/blob/main/LICENSE) for details.

---

##  📚 Introduction
Isaac Asimov is still considered one of the biggest science fiction writers of all time, that is why MartianFiction got curious about how much his representation of space travels could be true, that is why, using the information both from Asimov’s Tale “The Martian Way” and possible missing information based on reality, MartianFiction has done this project to represent and visualize the first travel that is described on the story given it’s starting parameters.

---

## 🔍 Objectives
- Using the numerical data from Asimov’s story, corroborate whether it’s possible to be in orbit from Mars to Saturn using an n-body model.
- If applicable, improve some numerical data from Asimov’s story to have a better model of the journey from Mars to Saturn.
- Create a model that simulates the movement of Mars and Saturn without significant external changes.

---

## ⚙️ Toolset
- Python 3.11
- Pyplot from the Matplotlib module
- NumPy  1.19.2
  
---

## 📝 Methodology
- **Observation**: Get the physical measures of the space trip from Mars to Saturn narrated in The Martian Way and the physical movements of both Mars and Saturn
- **Physical Theory** / **Law**: Use Newton’s Laws of Motion and Law of Universal Gravitation. 
- **Numerical Method**: In this step we will calculate the missing numerical data based on the physical theory of this phenomenon. The frame of reference to be used has not yet been determined.
- **Implementation**: Create a n-body model. The classes and functions that will be used to implement the model are not known with certainty, however information such as: mass, speed and position will be considered.
- **Validation**: Run the n-body model giving other physical measures.

---

## 💡 Usage
- To change the initial conditions modify the n-body.py file.
- To gather data run the n-body.py file and store it's contents on a file, example command: `python n-body.py > data_1.txt`
- Be aware the estimated time of script running is about 4 hours.
- With visualize.py create the images to represent the travel.

---

## 📊 Results
- After several tries and hours the results where stored on the "data.txt" file.
Here the results video:
[https://youtu.be/DclfLVQKfbM](https://youtu.be/DclfLVQKfbM)

---

## 🌟 Conclusions
Our model ended up on the next Conclusions:
Due to the initial vague indications Asimov left on "The Martian Way" the rocket's movement vector was flawed and could not move directly to Saturn, still, the rocket, did had a really good velocity and acceleration to actually be possible to achieve said journey.
The 6 month time that Asimov theorized with his calculations was actually too much and, even if the angle would have been correct, the rocket surpassed all Saturn's coordinates on aproximately the 90th day.

---

## 📖 Reference

- Asimov, I. (2019). Cuentos completos II ( Colección Cuentos completos 2 ).

---

Copyright
All licenses in this repository are copyrighted by their respective authors. Everything else is released under The MIT License. See LICENSE for details.

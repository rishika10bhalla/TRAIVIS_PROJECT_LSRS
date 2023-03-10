# TRAIVIS_PROJECT_LSRS
Welcome to our machine learning model for recommending learning styles for students.
The proposed system automatically depends on an Al classification algorithm to identify students' learning styles using a data-driven approach. We have built our model in light of the Felder and Silverman Learning Style Model (FSLSM) as it is a widely used model that has proven to be suitable for use in traditional educational systems. TRAIVIS's team has decided to use FSLSM as a guide because it focuses on the teaching approaches and students' psychological analysis. The collected data from students' behaviour on TRAVIS's platform and feedback system will feed the trained Al model for analysis. Then, TRAITS-LSRS will display student learning styles in four different parameters based on student behaviour patterns.
This project aims to help students identify their preferred learning style to optimize their learning outcomes. The model was built using various machine learning techniques such as data preprocessing, feature engineering, model selection, and hyperparameter tuning.
We have used KNN algorithm for implementing our project.

Active/Reflective: This parameter defines active and reflective students who prefer physical or theoretical classes. Active students mostly prefer to work in groups and complete more assignments. Whilst reflective students prefer to work alone and do fewer assignments. These learning behaviours will be collected, such as forum discussions, chats, and assignments.
Sensitive/ Intuitive: This parameter defines sensitive and Intuitive students. Students with sensitive learning styles
are more attentive and cautious, with fewer trials and better performance on exams and assignments than students with intuition perception. Intuitive students show boredom in detail, carelessness, many attempts and low performance in in exams and assignments. The students' behaviour patterns, such as time spent on tests and assignments, will be the input for the model.
Visual/Verbal: This parameter identifies verbal and visual learners according to their interaction with learning materials and participation in group activities. Based on the characteristics of verbal and visual learners, behavioural patterns such as text, origin points, and hyperlinks will be the input for the model.
Sequential/global: Students are characterised according to their understanding. Sequential students learn in small incremental steps and therefore have linear learning progress. They tend to follow gradual logical paths to find solutions. Conversely, global students use a holistic thinking process and learn quickly. They tend to absorb the teaching material almost randomly without seeing the connections, but suddenly they get the complete picture after learning enough materials related to a subject. So, they can solve complex problems, find connections between different areas, and organise things in new ways, but find it difficult to explain how they did it. The behavioural patterns include asking questions, watching videos in sequence or random, etc.
Feedback System is another feature that will help measure students' understanding of the educational materials. The Feedback system will be the best tool to take genuine feedback from the users working with the image classification technique and using the live feed from the user's web camera. Students' facial expressions will be captured throughout the session and will predict the level of focusing and comprehension on the course using Al technology.

Our model takes into account various factors such as student demographics, academic performance, extracurricular activities, and personal preferences to recommend a learning style that suits them the best.
The factors we have taken into consideration specifically are:
ABC - area before content
D - definitions
C - detailed content
A - activity questions
AAC - area after content( summaries, revision exercises)
V - content pages with visual illustrations
ABC T - time on area before content
D T - time spent on definitions
C T - time spent on detailed content
A T - time spent on activity questions
AAC T - time spent on area after content(summaries, revision exercises)
LS - learning style to be predicted

We used a publicly available dataset to train(knn.js) and test our model(test0.js). We also conducted a cross-validation study to ensure the robustness of our model.

This model is intended to be used as a guidance tool and not a definitive assessment of a student's learning style. We encourage students to explore various learning styles and find what works best for them.

We hope that our model will be useful to students, educators, and researchers in the field of education. If you have any questions or suggestions for improvement, please feel free to reach out to us.

Thank you for using our machine learning model for recommending learning styles!






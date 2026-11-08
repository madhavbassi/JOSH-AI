documents = [
"""
PROFESSIONAL SNAPSHOT

Name: Madhav Bassi

Current positioning: AI / ML student and aspiring AI/ML or software developer.

Resume headline used: AI Engineer Intern.

Education: B.Tech in Computer Science / Computer Science and Engineering, specialization in Artificial Intelligence and Machine Learning, SGT University, Haryana/Gurugram, India.

Expected graduation: 2028 (resume lists August 2024 – August 2028).

CGPA: 7.5 (as stated in the resume; latest known figure).

Current academic stage: Third year / fifth semester as of October 2026.

Primary job market: Delhi NCR, including Delhi and Gurugram.

Primary opportunity sought: First AI/ML internship or AI-engineering-related internship. Also open to relevant software/technology internship opportunities.

Professional experience level: Student / early-career. No confirmed full-time professional experience and no confirmed AI/ML industry internship as of the preparation date.

Portfolio direction: Building practical, usable AI applications rather than only academic demonstrations.



Short introduction:

"Madhav Bassi is a Computer Science student specializing in Artificial Intelligence and Machine Learning at SGT University. He is building practical applications using Python, machine-learning fundamentals, APIs, and LLM integrations. His current portfolio includes a content-based movie recommendation system and an AI-powered resume analyzer. He is looking for an opportunity to learn from an engineering team and contribute to real products."



Longer introduction:

"I am pursuing a B.Tech in Computer Science with a specialization in AI and ML at SGT University. I work primarily with Python and have hands-on experience with data preprocessing, exploratory data analysis, machine-learning fundamentals, and building application interfaces around APIs. I have built a movie recommendation system using TF-IDF and cosine similarity, with FastAPI and Streamlit, and an AI resume analyzer that uses an LLM API and structured validation to compare resumes with job descriptions. I am currently developing a personal professional AI assistant that can answer recruiter questions using my professional information. I am looking for an AI/ML or software internship where I can strengthen my engineering skills while contributing to practical work."



2\. CONTACT AND PROFESSIONAL LINKS





Email: workwithmadhavbassi\@gmail.com

Phone: +91 8375929291

Location on resume: New Delhi, India

GitHub profile: https\://github.com/madhavbassi

LinkedIn: https\://linkedin.com/in/madhav-bassi-*7ba622205*/



Known repositories:

1\. Movie recommender: https\://github.com/madhavbassi/-Movie-Recommender

2\. Resume analyzer / resume parser: https\://github.com/madhavbassi/resume-parser



Note: Verify that repository visibility, README instructions, and deployment links are current before sharing them with recruiters.



3\. EDUCATION



SGT University, Haryana / Gurugram, India

Bachelor of Technology (B.Tech), Computer Science / Computer Science and Engineering, specialization in Artificial Intelligence and Machine Learning.

Period: August 2024 – August 2028 (expected).

CGPA: 7.5.



School education recorded in an earlier resume version:

\- Class XII, CBSE — St. Mark’s Senior Secondary Public School.

\- Class X, CBSE — MBS International School.

These school details were present in an older resume version and were omitted from the October 2026 resume. Confirm before using in a formal application.



4\. TECHNICAL SKILLS



Programming and data:

\- Python.

\- NumPy.

\- Pandas.

\- JSON.



Machine learning and data science:

\- Scikit-learn.

\- Machine-learning fundamentals.

\- Exploratory Data Analysis (EDA).

\- Data cleaning and preprocessing.

\- TF-IDF vectorization.

\- Cosine similarity.

\- Basic model training / working with training workflows.



Visualization:

\- Matplotlib.

\- Seaborn.



Application development and APIs:

\- FastAPI.

\- Streamlit.

\- REST/API integration and working with APIs.

\- Groq API / LLM API integration.

\- Pydantic for structured data validation.



Developer tools:

\- Git.

\- GitHub.

\- Jupyter Notebook.

\- Visual Studio Code.



LLM application concepts:

\- LLM API integration.

\- Prompt engineering.

\- Structured extraction / schema-guided output using Pydantic.

\- Resume and job-description analysis.



Skill-depth guidance:

\- Python, data handling, ML fundamentals, and application building are areas Madhav has used in projects.

\- The resume lists the technologies above, but it does not establish expert-level proficiency in every item.

\- SQL is a learning / desired skill mentioned in career-planning conversations; it is not listed in the October 2026 resume. Do not present it as a strong demonstrated skill without confirmation.

\- OOP, web scraping, and deeper backend engineering have appeared in learning plans or desired skill lists; do not claim professional mastery.

\- Do not claim deep learning, model research, production-scale ML, advanced MLOps, cloud architecture, or fine-tuning experience unless Madhav supplies concrete evidence.

\- Madhav prefers honest representation and does not want skills or experience exaggerated.



5\. PROJECTS



PROJECT A — NETFLIX MOVIE RECOMMENDATION SYSTEM

Also referred to as: Movie Recommender / CineMatch.

Status: Built portfolio project.

Repository: https\://github.com/madhavbassi/-Movie-Recommender



Problem:

A user wants movie suggestions based on a movie they already like. The application uses movie metadata to identify similar titles and present recommendations.



What it does:

\- Uses a content-based recommendation approach.

\- Processes a dataset containing more than 45,000 movie records.

\- Cleans and prepares movie metadata using Pandas and NumPy.

\- Uses TF-IDF vectorization to represent text metadata numerically.

\- Uses cosine similarity to compare movie representations and identify similar movies.

\- Exposes recommendation functionality through a FastAPI backend.

\- Uses a Streamlit frontend to provide an interactive user interface.

\- Integrates the TMDB API to retrieve movie posters / visual movie information.

\- Uses Pickle to store and load precomputed objects / artifacts.



Technology stack:

Python, Pandas, NumPy, scikit-learn, TF-IDF, cosine similarity, FastAPI, Streamlit, TMDB API, Pickle.



Known project artifacts / implementation context:

\- project.ipynb

\- movies_metadata.csv

\- df.pkl

\- indices.pkl

\- tfidf.pkl

\- tfidf_matrix.pkl



Deployment / engineering context:

\- The project has been deployed with a FastAPI backend and Streamlit frontend.

\- The hosted FastAPI backend on Render may sleep when inactive, so its first request can be delayed.

\- Python 3.12 was used because of a SciPy compatibility issue encountered with Python 3.13 in the project environment.



How to explain it to a recruiter:

"I built a content-based movie recommendation system using a dataset of more than 45,000 movies. I cleaned and prepared the metadata with Pandas and NumPy, converted text features into TF-IDF vectors, and used cosine similarity to find movies with similar metadata. I exposed the recommendation logic through FastAPI and built a Streamlit interface. I also integrated TMDB to fetch movie posters and make the results more usable."



Likely technical follow-up topics:

\- Why content-based filtering was selected.

\- Difference between content-based and collaborative filtering.

\- What information was used as movie metadata.

\- How text preprocessing was performed.

\- What TF-IDF means and why it is useful.

\- What cosine similarity measures.

\- How the recommendation result is selected and returned.

\- Why FastAPI was used for the backend.

\- How Streamlit communicates with the backend.

\- How TMDB API integration works.

\- What was serialized with Pickle and why.

\- How the application handles missing or invalid movie titles.

\- How the dataset was cleaned and what limitations remain.



Important honesty note:

The project is a content-based recommender using metadata similarity. Do not call it a deep-learning recommendation engine or claim it was trained on user behaviour unless Madhav confirms that implementation.



PROJECT B — AI RESUME ANALYZER

Also referred to as: ResumeAI / Resume Parser.

Status: Built portfolio project; deployed on Streamlit Community Cloud according to the October 2026 resume.

Repository: https\://github.com/madhavbassi/resume-parser



Problem:

A candidate or recruiter wants to compare a resume against a job description and understand how well the candidate's stated skills align with the role.



What it does:

\- Accepts resume documents and job descriptions.

\- Supports PDF and DOCX resume parsing in the implementation context.

\- Uses a Groq LLM API call with the model openai/gpt-oss-*120b* to extract / structure relevant information.

\- Uses Pydantic schemas to validate structured data.

\- Identifies matching skills and missing skills.

\- Produces a candidate match score / matching analysis.

\- Presents the workflow through a Streamlit web application.

\- Deployed on Streamlit Community Cloud according to the resume.



Technology stack:

Python, Streamlit, Groq API, openai/gpt-oss-*120b*, Pydantic, Pandas, pypdf, python-docx, Git, GitHub.



Core concepts:

Resume parsing, job-description analysis, candidate-job matching, skill matching, rule-based scoring, structured extraction, data validation, LLM API integration.



How to explain it to a recruiter:

"I built an AI-powered resume analyzer that takes a resume and a job description, extracts structured information using a Groq-hosted LLM, validates the output with Pydantic, and compares the candidate's skills with the requirements. It identifies matching and missing skills and provides a match score through a Streamlit interface."



Likely technical follow-up topics:

\- Why an LLM is used for extracting resume information.

\- Why Pydantic validation is useful when working with LLM output.

\- How PDF and DOCX text extraction works.

\- How the job description is represented / parsed.

\- How matching and missing skills are identified.

\- Which parts of scoring are rule-based versus LLM-generated.

\- What can go wrong with unstructured or inconsistent resumes.

\- How to handle hallucinated or malformed LLM output.

\- How API keys are stored securely using environment variables.

\- What deployment issues were encountered.



Important honesty note:

Do not claim the analyzer makes objective hiring decisions, predicts job performance, or is validated against a real hiring dataset. Describe it as a resume/job-description matching tool. The resume mentions rule-based scoring and data validation; explain the actual scoring formula only if Madhav confirms the precise implementation.



PROJECT C — PERSONAL PROFESSIONAL AI ASSISTANT

Working names: Hire Me AI; A.U.R.A. (Personal Intelligence System).

Status: In development as of 31 October 2026. Do not present as a completed production deployment.

Purpose:

Instead of sending only a static resume, Madhav can share a link to a conversational assistant that answers recruiter questions about his education, skills, projects, experience, and professional background.



Planned user experience:

\- Recruiters can ask free-form questions about Madhav's professional profile.

\- Quick prompts include "Why hire Madhav?", "Technical capabilities", and "Projects & builds".

\- A resume download action is planned / included in the frontend design.

\- The assistant should distinguish proven experience from learning areas and should answer from a grounded knowledge base.

\- The interface is intended to be distinctive but professional, with an Iron Man / A.I. assistant-inspired visual direction. The frontend uses the name A.U.R.A.



Technical implementation context:

\- Python backend using FastAPI.

\- Groq API integration.

\- Model used in the current implementation context: openai/gpt-oss-*120b*.

\- Pydantic.

\- python-dotenv and environment variables for API configuration.

\- PDF extraction with pypdf; python-docx is also part of the toolset.

\- Frontend HTML/CSS/JavaScript work exists in a file named aura_frontend.html.

\- The backend work includes a chat endpoint / chat flow and system prompt handling.

\- Madhav is currently learning the code and wants to understand and build it himself rather than blindly copy and paste.



RAG status:

Madhav has asked about making the assistant RAG-based and the benefits / code changes involved. Treat RAG implementation as a planned or actively explored enhancement unless a working retrieval pipeline is explicitly confirmed. Do not say that the current assistant already has embeddings, a vector database, chunking, retrieval, or a complete RAG pipeline unless those components are implemented and verified.



Potential RAG knowledge sources:

\- This professional profile document.

\- Current resume.

\- Project READMEs and source code.

\- Verified project architecture notes.

\- Confirmed interview answers and technical explanations.

\- Updated employment / education records supplied by Madhav.



How to explain the product:

"I am building a personal professional AI assistant that lets recruiters explore my profile through a conversation instead of relying only on a static resume. The goal is to provide grounded answers about my projects, skills, and background, with a knowledge base that keeps the answers consistent and accurate."



6\. EXPERIENCE AND LEADERSHIP



VIDEO EDITOR (PAID INTERN) — UNIVERSITY INSTAGRAM

Academic period stated on resume: Second year.

Employer / exact formal department name: Resume describes this as "University Instagram"; exact employer entity and dates are not specified in the latest resume.

Responsibilities stated:

\- Directed on-campus shoots.

\- Edited video content for the university's official social media presence.

\- Contributed to the creation of university social-media content.



How to explain:

"Alongside my technical work, I worked as a paid video editor for the university's Instagram presence. I directed on-campus shoots and edited video content for the university's official social channels."



Do not invent:

\- Exact start/end dates.

\- Campaign performance metrics.

\- Number of videos or shoots.

\- Team size or budget.

\- Formal job title beyond the resume wording.

\- Any connection to a different employer unless Madhav confirms it.



CREATIVE HEAD — GOOGLE DEVELOPER STUDENT CLUB (GDSC)

Academic period stated on resume: First year.

Responsibilities stated:

\- Led video creation.

\- Worked on promotional campaigns.

\- Contributed to Instagram marketing to drive club engagement.



How to explain:

"I was the Creative Head at the Google Developer Student Club during my first year. I led video creation and contributed to promotional campaigns and Instagram marketing to support club engagement."



Do not invent:

\- Number of members managed.

\- Growth percentages, reach, impressions, or event attendance.

\- Formal employment status; this is a student leadership role.



Experience summary:

Madhav has creative/media execution and student-club leadership experience, alongside technical portfolio projects. The latest resume does not list a formal AI/ML internship or professional AI engineering role. His technical work is primarily represented through self-built projects.



7\. CERTIFICATION



Foundation2AI Data Analytics Course Completion Certificate — Samatrix.

The resume lists this as a course completion certificate.

Do not infer a degree, professional accreditation, or advanced certification from it.



8\. CAREER INTERESTS AND GOALS



Current near-term goals:

\- Secure a first AI/ML internship or AI-engineering-related internship.

\- Also consider software engineering / developer internships that provide relevant engineering experience.

\- Target Delhi NCR, especially Delhi and Gurugram.

\- Improve the ability to explain technical concepts clearly in interviews.

\- Build a portfolio that demonstrates practical product-building ability.

\- Develop stronger foundations in Python, DSA, machine learning, backend development, and LLM applications.



Longer-term interests:

\- AI engineering and applied AI.

\- Building useful AI products.

\- Startup environments and early-stage product teams.

\- Founder’s Office / startup operations exposure as a possible adjacent career path.

\- Long-term ambition to build a startup and potentially move toward AI leadership / CAIO-level responsibility.



These are interests and aspirations, not current job titles or achieved outcomes.



9\. JOB SEARCH AND PROFESSIONAL DEVELOPMENT CONTEXT



\- Primary target roles: AI/ML Intern, AI Engineer Intern, Machine Learning Intern, Python Developer Intern, Software Developer Intern, and related applied-AI roles.

\- Location preference: Delhi NCR (Delhi and Gurugram).

\- Madhav is early-career and wants realistic opportunities aligned with his actual experience.

\- He has explored startup roles and referral-based applications.

\- He prefers not to exaggerate experience or claim technologies he cannot explain.

\- Interview preparation should focus on explaining project decisions, fundamentals, code flow, debugging, and trade-offs—not memorized buzzwords.

\- A prior job-search workflow looked at company career boards including Atlys, Forma.ai, Enterpret, Trackmind, Cresta, Meraki Labs, Karya, Drivetrain, CertifyOS, Notion, Outmarket AI, Novita AI, Mico, Samaya AI, and Instawork. A recorded run fetched 442 listings but filtered all of them out due to title and location criteria. This is historical job-search tooling context, not evidence of applications, interviews, or offers from those companies.



FOUNDER'S OFFICE / INCUBE MEDIA CONTEXT:

Madhav previously explored a Founder’s Office opportunity with InCube Media through a process involving Rishabh Biswas. The described role covered hiring, sales, and operations. The process included a 12-slide performance-marketing sales deck assignment based on website research, submitted on 29 September 2026. The discussed arrangement was initially remote for three months with a possible later Delhi hybrid setup. This is an application / selection-process context only. Do not list it as employment, an internship, or completed work experience unless Madhav later confirms an offer and actual start.



10\. WORKING STYLE AND PROFESSIONAL COMMUNICATION



\- Prefers practical, direct feedback and realistic assessments.

\- Values building products that solve a real problem rather than creating projects only to fill a resume.

\- Wants to understand code and engineering decisions, not simply copy-paste generated code.

\- Benefits from explanations in simple English, with concepts introduced before code.

\- For technical guidance, prefers a clear sequence, folder structure, explanation of each file, and terminal commands when needed.

\- For resume and LinkedIn writing, prefers authentic, recruiter-facing language that sounds human and not excessively polished or generic.

\- Wants claims to be evidence-based and proportionate to actual skill level.

\- Interested in both technical development and product thinking.



11\. RECRUITER / COLLEAGUE FAQ — GROUNDED ANSWERS



Q: Tell me about yourself.

A: "I am Madhav Bassi, a B.Tech Computer Science student specializing in AI and Machine Learning at SGT University. I work mainly with Python and have built projects involving machine learning, APIs, and LLM integrations. My main projects are a content-based movie recommendation system and an AI resume analyzer. I am currently building a personal professional AI assistant and looking for an opportunity to contribute to a real engineering team while continuing to learn."



Q: What kind of role are you looking fo&#x72;*?*

A: "I am primarily looking for an AI/ML or AI-engineering internship. I am also open to relevant Python or software-development internships where I can work on real applications and strengthen my engineering fundamentals."



Q: Where are you looking for opportunitie&#x73;*?*

A: "My primary location preference is Delhi NCR, including Delhi and Gurugram."



Q: What is your educational backgroun&#x64;*?*

A: "I am pursuing a B.Tech in Computer Science with a specialization in Artificial Intelligence and Machine Learning at SGT University. My expected graduation year is 2028."



Q: What is your CGP&#x41;*?*

A: "My latest stated CGPA is 7.5."



Q: What are your strongest technical area&#x73;*?*

A: "Python, data handling with Pandas and NumPy, machine-learning fundamentals, data preprocessing and EDA, and building applications using APIs. I have applied these in my movie recommendation and resume analyzer projects."



Q: Which programming language do you mainly us&#x65;*?*

A: "Python is my primary programming language."



Q: Have you worked with machine learnin&#x67;*?*

A: "I have applied machine-learning concepts in a content-based movie recommendation project, including TF-IDF vectorization and cosine similarity using scikit-learn. I am continuing to strengthen my fundamentals."



Q: Explain your movie recommendation project.

A: "It processes metadata for more than 45,000 movies, represents text features using TF-IDF, and compares movies using cosine similarity. I built a FastAPI backend and Streamlit frontend and integrated TMDB for posters."



Q: What is TF-ID&#x46;*?*

A: The assistant can explain the general concept: Term Frequency–Inverse Document Frequency weights terms based on their frequency in a document and how uncommon they are across the collection. For Madhav's project, it converts text metadata into numerical vectors. Madhav should be asked for implementation-specific details if a question goes beyond this general explanation.



Q: What is cosine similarit&#x79;*?*

A: The assistant can explain the general concept: cosine similarity compares the angle between two vectors and is commonly used to measure similarity between text representations. In the movie recommender, it is used to compare TF-IDF vectors. Do not invent the exact similarity threshold or ranking implementation.



Q: Why did you use content-based filterin&#x67;*?*

A: "The project recommends movies using the similarity of their metadata. This allows recommendations to be made from item information rather than requiring a large dataset of user ratings or behaviour." This is a conceptual explanation; do not claim that all possible alternatives were experimentally benchmarked.



Q: What is the difference between content-based and collaborative filterin&#x67;*?*

A: Content-based filtering uses item features and a user's/item's stated or inferred preferences; collaborative filtering uses patterns in user-item interactions, such as ratings or clicks. In Madhav's project, the implemented approach is content-based.



Q: Why FastAP&#x49;*?*

A: "I used FastAPI to expose the recommendation functionality through backend API endpoints, separating the recommendation logic from the user interface."



Q: Why Streamli&#x74;*?*

A: "I used Streamlit to create an interactive Python-based frontend for users to try the recommendation system."



Q: What does TMDB do in your projec&#x74;*?*

A: "The TMDB API is integrated to retrieve movie posters and related visual information for the recommendations."



Q: Explain your AI Resume Analyzer.

A: "It extracts information from resumes and job descriptions using a Groq-hosted LLM, validates structured output with Pydantic, and compares skills to identify matches and gaps. It presents the analysis in a Streamlit application."



Q: Why use an LLM in the resume analyze&#x72;*?*

A: "Resumes and job descriptions are written in varied natural-language formats. An LLM can help extract relevant information into a consistent structure, which the application can then validate and use for matching."



Q: Why Pydanti&#x63;*?*

A: "Pydantic lets the application define expected data structures and validate the data returned by the model. This helps catch missing or incorrectly typed fields before using the output."



Q: Does the resume analyzer make hiring decision&#x73;*?*

A: "No. It is a resume and job-description matching tool that highlights skill overlap and gaps. It should support review, not replace human hiring judgment."



Q: Have you worked with LLM&#x73;*?*

A: "I have integrated an LLM through the Groq API in my resume analyzer and am using Groq in my personal professional assistant project. My experience is with building applications around LLM APIs, structured outputs, and prompts—not training foundation models."



Q: Have you built a RAG syste&#x6D;*?*

A: "I am exploring and developing a RAG-based knowledge layer for my personal professional assistant. The current RAG implementation should only be described as complete once document ingestion, chunking, embeddings, retrieval, and grounded generation are implemented and tested."



Q: Have you completed an AI/ML internshi&#x70;*?*

A: "My current resume does not list an AI/ML industry internship. My technical experience so far is represented mainly through my projects. I do have creative experience as a paid video editor for the university's Instagram presence and student leadership experience as GDSC Creative Head."



Q: What work experience do you hav&#x65;*?*

A: "My resume lists a paid video editor role for the university's Instagram presence, where I directed on-campus shoots and edited official social content. It also lists my role as Creative Head at GDSC, where I led video creation and contributed to promotional campaigns and Instagram marketing."



Q: Have you led a tea&#x6D;*?*

A: "I served as Creative Head at GDSC and led video creation and promotional work." The size of the team and exact management responsibilities are not documented; do not invent them.



Q: What certification do you hav&#x65;*?*

A: "I have a Foundation2AI Data Analytics course completion certificate from Samatrix."



Q: What are you currently buildin&#x67;*?*

A: "I am building a personal professional AI assistant, currently referred to as Hire Me AI / A.U.R.A. The idea is to let recruiters ask questions about my professional background through a conversational interface. I am working on the backend and exploring a RAG-based knowledge base so answers can be grounded in verified profile information."



Q: Why did you build a personal AI assistan&#x74;*?*

A: "A resume is static and limited in how much context it can communicate. I wanted to build something that lets a recruiter ask follow-up questions about my projects, skills, and background in a more interactive way."



Q: What are your strength&#x73;*?*

A: Grounded evidence supports describing Madhav as hands-on, interested in practical product-building, willing to learn, and able to combine technical project work with creative execution. Avoid unsupported claims such as "exceptional leadership", "expert problem solver", or quantified productivity.



Q: What is an area you are improvin&#x67;*?*

A: "I am working on strengthening my fundamentals and becoming better at explaining the technical decisions behind my projects, not just getting an application to run."



Q: Why should we hire yo&#x75;*?*

A: "I can bring a foundation in Python and applied machine-learning concepts, along with hands-on experience building projects that combine data processing, APIs, and user-facing applications. I am early in my career, so I am looking for a team where I can learn quickly, take ownership of well-defined tasks, and contribute with a practical, product-focused mindset."



Q: What are your salary expectation&#x73;*?*

A: Not documented. The assistant should ask Madhav or say he is open to discussing compensation based on the role, responsibilities, and internship structure. Do not invent a number.



Q: What is your notice period or availabilit&#x79;*?*

A: Not documented. Ask Madhav.



Q: Are you open to relocation or hybrid wor&#x6B;*?*

A: Not definitively documented. Delhi NCR is the stated target market. Ask Madhav about relocation, commute, remote, or hybrid preferences before answering.



Q: What is your LinkedI&#x6E;*?*

A: https\://linkedin.com/in/madhav-bassi-*7ba622205*/



Q: Can I see your GitHu&#x62;*?*

A: https\://github.com/madhavbassi



Q: Can you share your resum&#x65;*?*

A: The resume is available as a separate file / download in the A.U.R.A. application if that file is configured. Do not claim that a download is available unless the deployed application actually serves the current resume file.





12\. QUESTIONS THE AGENT SHOULD HANDLE



The assistant should be prepared to answer these professional questions using the facts above and verified project documentation:



PERSONAL INTRODUCTION AND FIT

\- Who is Madhav Bass&#x69;*?*

\- Give me a 30-second / 60-second introduction.

\- What is he studying and when will he graduat&#x65;*?*

\- What kind of internship is he seekin&#x67;*?*

\- Why is he interested in AI/M&#x4C;*?*

\- Why should we shortlist hi&#x6D;*?*

\- What value could he bring to a small startup tea&#x6D;*?*

\- What is his current experience leve&#x6C;*?*



EDUCATION

\- Which university and degre&#x65;*?*

\- What is his specializatio&#x6E;*?*

\- What is his CGP&#x41;*?*

\- What are his expected graduation date&#x73;*?*

\- Which school did he atten&#x64;*?*

\- What coursework has he complete&#x64;*?* (Only answer when Madhav supplies course details.)



SKILLS

\- Which programming languages does he us&#x65;*?*

\- Which Python libraries has he use&#x64;*?*

\- What ML algorithms / methods has he applie&#x64;*?*

\- Has he used Pandas, NumPy, scikit-lear&#x6E;*?*

\- Has he used FastAPI or Streamli&#x74;*?*

\- Has he worked with API&#x73;*?*

\- Has he used Git/GitHu&#x62;*?*

\- What is his level in SQL, OOP, DSA, deep learning, cloud, Docker, databases, and deploymen&#x74;*?* (These require updated self-assessment; do not guess.)

\- Which skills are demonstrated in projects versus currently being learne&#x64;*?*



PROJECT DEEP DIVES

\- What problem does each project solv&#x65;*?*

\- What is the architectur&#x65;*?*

\- What was Madhav personally responsible fo&#x72;*?*

\- What dataset was use&#x64;*?*

\- What preprocessing was don&#x65;*?*

\- Why were specific libraries chose&#x6E;*?*

\- How is the model / algorithm use&#x64;*?*

\- How is the frontend connected to the backen&#x64;*?*

\- How is the application deploye&#x64;*?*

\- What challenges were encountere&#x64;*?*

\- What would he improve nex&#x74;*?*

\- What are the limitation&#x73;*?*

\- Is the project publicly accessible no&#x77;*?*

\- What is the GitHub repositor&#x79;*?*



EXPERIENCE AND LEADERSHIP

\- What did he do as a paid video edito&#x72;*?*

\- What did he do as GDSC Creative Hea&#x64;*?*

\- Did he manage people, shoots, campaigns, or social conten&#x74;*?*

\- What did he learn from creative work that transfers to engineerin&#x67;*?*

\- Has he worked in a professional AI/ML rol&#x65;*?* (Current answer: no such role is listed in the latest resume.)

\- Has he completed an internship at a technology compan&#x79;*?* (Do not infer one.)



WORK STYLE AND CULTURE

\- How does he learn a new technolog&#x79;*?*

\- Does he prefer independent work or teamwor&#x6B;*?* (Ask Madhav for a clear answer.)

\- How does he approach debuggin&#x67;*?*

\- How does he respond to feedbac&#x6B;*?*

\- What kind of environment helps him lear&#x6E;*?*

\- Does he prefer startups or larger companie&#x73;*?* (He has expressed interest in startup environments, but ask for current preference.)

\- What is his communication styl&#x65;*?*

\- What are his strengths and development area&#x73;*?*



PRACTICAL HIRING DETAILS

\- Availability / joining date.

\- Internship duration.

\- Remote, hybrid, or onsite preference.

\- Salary / stipend expectations.

\- Notice period.

\- Relocation willingness.

\- Work authorization.

\- Current semester timetable / exam constraints.

These are not documented and must be confirmed directly with Madhav.



14\. PROFILE GAPS — INFORMATION TO ADD LATER



To make this knowledge base stronger and improve recruiter answers, add verified details when available:



1\. Latest resume file and date.

2\. Current CGPA and semester confirmation.

3\. Exact dates, formal employer name, and duration for the paid video editor role.

4\. Any measurable outcomes from video editing, campus shoots, GDSC campaigns, or events.

5\. Exact responsibilities and team size as GDSC Creative Head.

6\. A clear skill-level assessment for Python, OOP, DSA, SQL, scikit-learn, FastAPI, Streamlit, Git, and LLM application development.

7\. Courses / subjects completed in the B.Tech curriculum.

8\. Project architecture diagrams, README files, demo links, and exact implementation details.

9\. Specific technical challenges and how Madhav solved them in each project.

10\. Current deployment URLs and whether each project is online.

11\. Exact status and architecture of the RAG implementation in A.U.R.A.

12\. Internship availability, joining date, duration, stipend expectations, and work-mode preferences.

13\. Preferred job titles and any roles he does not want.

14\. Any new internship, freelance, open-source, or team project experience.

15\. Updated portfolio / personal website link, if available.





15\. RESUME TRANSCRIPTION — OCTOBER 2026 VERSION



The following is a text transcription of the resume file titled "Resume.pdf", available in the user's Library and created on 25 October 2026. Formatting has been normalized for readability; wording and claims are retained as closely as possible.



MADHAV BASSI

Phone: +91 8375929291

Location: New Delhi, India

GitHub: https\://github.com/madhavbassi

Email: workwithmadhavbassi\@gmail.com

LinkedIn: https\://linkedin.com/in/madhav-bassi-*7ba622205*/



Headline:

AI ENGINEER INTERN



PROJECTS



Netflix Movie Recommendation System using Machine Learning!

Tech Stack: Python | Pandas & NumPy | Scikit-learn | FastAPI | Streamlit | TMDB API | Pickle



\- Processed and cleaned a dataset of 45,000+ movies using Pandas and NumPy to prepare movie metadata for recommendation.

\- Implemented a content-based recommendation algorithm using TF-IDF vectorization and cosine similarity to recommend movies based on metadata similarity.

\- Built a FastAPI backend and Streamlit frontend, integrating the TMDB API to retrieve movie posters and display recommendations through an interactive interface.



AI Resume Analyzer | Python, Groq API, Pydantic, Streamlit



Core Concepts: Resume Parsing, Job Description Analysis, Candidate Job Matching, Rule Based Scoring, Data Validation.

Tech Stack: Python | Streamlit | Groq API (LLM) | Pydantic | Pandas | Git | GitHub.



\- Parsed resumes and job descriptions using Groq’s openai/gpt-oss-*120b* model with Pydantic schema validation.

\- Implemented skill matching to identify matching skills, missing skills, and candidate match scores.

\- Built a Streamlit web application and deployed it on Streamlit Community Cloud.



SKILLS



Libraries:

NumPy | Pandas | Matplotlib | Seaborn | Scikit-learn



Tools:

Git | GitHub | Jupyter Notebook | VS Code | Pydantic | Groq API | JSON



Other skills:

\- Exploratory Data Analysis (EDA)

\- Data preprocessing / cleaning

\- Training Model

\- Working with API

\- AI/LLM: LLM API Integration, Prompt Engineering



CERTIFICATION



Foundation2AI Data Analytics Course Completion Certificate — Samatrix.



EDUCATION



Bachelor of Technology in Computer Science (AIML), SGT University.

August 2024 – August 2028 (expected).

CGPA: 7.5.



CREATIVE EXPERIENCE



Video Editor (Paid Intern) | University Instagram (*2nd* Year)

Directed on-campus shoots and edited video content for the university's official social media presence.



Creative Head | Google Developer Student Club (GDSC) (*1st* Year)

Led video creation, promotional campaigns, and Instagram marketing to drive club engagement.



"""
]
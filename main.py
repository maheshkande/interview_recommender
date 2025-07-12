import pandas as pd

# Sample internship database
data = {
    "Domain": ["Data Science", "Web Development", "AI/ML", "Cybersecurity", "Cloud Computing", "DevOps"],
    "Min_CGPA": [6.0, 5.0, 6.5, 5.5, 6.0, 6.0],
    "Skills": [
        ["Python", "Pandas", "Excel"],
        ["HTML", "CSS", "JavaScript"],
        ["Python", "ML", "Deep Learning"],
        ["Networking", "Linux", "Security"],
        ["Cloud", "AWS", "Docker"],
        ["Git", "CI/CD", "Docker"]
    ],
    "Top_Companies": [
        ["TCS", "Mu Sigma", "Accenture"],
        ["Wipro", "Zoho", "Turing"],
        ["Google", "Fractal", "Hugging Face"],
        ["CyberPeace", "TCS", "Accenture"],
        ["AWS", "Microsoft", "Infosys"],
        ["RedHat", "IBM", "Freshworks"]
    ],
    "Recommended_Courses": [
        ["Excel + Pandas (Kaggle)", "IBM DS Cert"],
        ["Frontend on freeCodeCamp", "Responsive Web Cert"],
        ["Coursera ML by Andrew Ng", "Fast.ai"],
        ["Cisco Cyber Essentials", "Google Cybersecurity"],
        ["AWS Cloud Practitioner", "Great Learning Cloud"],
        ["DevOps by IBM", "Docker Basics"]
    ]
}

df = pd.DataFrame(data)

# Get user input
print("🎯 Internship Recommender\n")
cgpa = float(input("Enter your CGPA: "))
skills = input("Enter your skills (comma-separated): ").lower().split(',')

# Clean skills
skills = [s.strip().capitalize() for s in skills]

# Recommend domains
print("\n🧠 Recommended Domains Based on Your Profile:\n")

found = False
for index, row in df.iterrows():
    if cgpa >= row['Min_CGPA'] and any(skill in row['Skills'] for skill in skills):
        found = True
        print(f"📌 Domain: {row['Domain']}")
        print(f"   ✅ Companies: {', '.join(row['Top_Companies'])}")
        print(f"   📚 Courses: {', '.join(row['Recommended_Courses'])}")
        print("-" * 50)

if not found:
    print("❌ Sorry bro, no strong matches found. Try adding more core skills or improving CGPA.")

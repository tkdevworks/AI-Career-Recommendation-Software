import anvil.email
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from google import genai

client = genai.Client(api_key="AIzaSyCTxFmsbjK7xroWDWVsoeJveJ0jbBNWEhM")
@anvil.server.callable
def ask_gemini(prompt):
  response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt
  )
  return response.text


@anvil.server.callable
def career_advice(interests, hobbies, subjects, aims, skills):
  system_prompt = """You are a career guidance assistant. The user will provide: interests, hobbies, subjects, aims, and skills. They are a secondary school student living in Victoria following the VCE curriculum.

Your response must follow this exact structure and formatting:

1. Career Match Score
   - Display the single best-fit career first, followed by a match percentage (e.g., "Software Engineer – 88% match").
   - Highlight the career name subtly using capitalization or spacing to make it stand out.
   - Optionally add a relevant emoji to reinforce the career visually (e.g., 🎯, 💻, 🛡️).

2. Career Description
   - Provide a concise, clear description of what the job actually does. Keep sentences professional and easy to read.
   - Include a subtle emoji if it helps illustrate the work (e.g., 💡 for innovation, 🖥️ for tech).

3. Advantages, Disadvantages & Typical Pay
   - Include one key advantage and one key disadvantage of the career.
   - Include typical pay ranges in Australia (starting and average salary).
   - Format as short, clear bullet points or line breaks for readability.

4. Why this career?
   - Explain why this career fits the user based on their interests, hobbies, subjects, aims, and skills.
   - Use concise sentences, professional language, and, if suitable, a small emoji to convey alignment (e.g., ✅).

5. Skills Highlight
   - List 3–5 core skills as plain text separated by commas. 
   - Do not use brackets or asterisks. Emphasise skill importance subtly with commas.

6. Alternative Options
   - List 2–3 other suitable careers. Each should include a short description of what the role entails.
   - Optionally use a small relevant emoji for each alternative.

7. VCE Subjects
   - List the VCE subjects the user should prioritise for this career.
   - Use line breaks for each subject to improve visual clarity.

8. Extra Learning & Certifications
   - Recommend relevant online courses, certifications, competitions, or extracurriculars.
   - Use concise phrasing and, if appropriate, a subtle emoji (📚, 🏆).

9. College/University Pathway
   - Suggest the most relevant degree or training course in Victoria. Please reference the Exact University.
   - Include one short sentence explaining why it is suitable.
   - Use line breaks and, optionally, a university or graduation emoji 🎓.

10. Future Trends
    - Provide a brief insight into the career’s industry growth or emerging technology trends.
    - Keep it concise and forward-looking, optionally using an innovation or growth emoji 🌱.

Formatting Rules:
- Do not use asterisks, brackets, or markdown symbols.
- Headings must remain clear and prominent exactly as above.
- Keep paragraphs short, visually separated, and readable.
- Skills should be plain text separated by commas.
- Use emojis sparingly to enhance readability and modern style.
- Output should resemble a sleek, premium career profile card that feels modern, professional, and engaging.
"""

  user_input = f"""
Interests: {interests}
Hobbies: {hobbies}
Subjects: {subjects}
Aims: {aims}
Skills: {skills}
"""

  response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=[system_prompt, user_input]
  )
  return response.text


@anvil.server.callable
def followup(interests, hobbies, subjects, aims, skills, advice, followup):
  system_prompt = """You are a career recommendation engine. You have already provided the user with a primary career suggestion, based on their skills, hobbies, interests, subjects and aims.
You must now respond to their follow-up question while keeping in mind the context of their profile and the career advice you have already given.
Your answers should remain professional, clear, and directly relevant to their career development."""

  user_input = f"""
Interests: {interests}
Hobbies: {hobbies}
Subjects: {subjects}
Aims: {aims}
Skills: {skills}
Career Advice: {advice}
Follow-up question: {followup}
"""

  response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=[system_prompt, user_input]
  )
  return response.text


@anvil.server.callable
def createRoad(interests, hobbies, subjects, aims, skills, advice):
  system_prompt = """You are a career roadmap generator. You will get user data and the career recommendation they have been provided.  
Always output exactly 4 steps for them to achieve what is described, relevant to their user data and recommendation. 
All recommendations must be realistic and actionable within the next few years of the student's life. For example, if the student is Year 10–12, focus on VCE subjects, short-term learning, certifications, and first-year university pathways. Do not assume long-term career progression beyond first year of college/university.
Make it thorough. Each step must follow this format:

Step: Title
§ Bullet point 1
§ Bullet point 2
§ Bullet point 3
§ Bullet point 4
§ Bullet point 5

(Repeat for 4 steps)

Rules:
- Each step starts with the title on its own line.
- Before each title, put the step number e.g. (Step 1: then the title)
- Each bullet point starts with § and a space.
- Separate steps with a blank line.
- Provide practical actions."""

  user_input = f"""
Interests: {interests}
Hobbies: {hobbies}
Subjects: {subjects}
Aims: {aims}
Skills: {skills}
Recommendation: {advice}
"""

  response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=[system_prompt, user_input]
  )
  return response.text

  # more functions pertaining to task manager
@anvil.server.callable
def deleteCartItem(row_id,userId):
  row = app_tables.cart.get_by_id(row_id)
  if row and row['userId'] == userId:
    row.delete()

@anvil.server.callable
def getCartItems(userId):
  return list(app_tables.cart.search(userId=userId))

@anvil.server.callable
def clearCart(userId):
  for row in app_tables.cart.search(userId=userId):
    row.delete()


# roadmap functions to delete and save

@anvil.server.callable
def delete_user_roadmap(userId):

  rows = app_tables.road.search(userId=userId)
  for row in rows:
    row.delete()

@anvil.server.callable
def save_roadmap(userId, roadmap_steps):

  delete_user_roadmap(userId)


  for step in roadmap_steps:
    app_tables.road.add_row(
      userId=userId,
      title=step['title'],
      dotpoints=step['dotpoints']
    )
    
@anvil.server.callable
def get_user_roadmap(userId):

  rows = app_tables.road.search(userId=userId)
  return [{"title": row['title'], "dotpoints": row['dotpoints']} for row in rows]


# creating the user, and ensuring user is authenticated
@anvil.server.callable
def createUser(username, password):
  if app_tables.users.get(username=username):
    return "exists"
  else:
    app_tables.users.add_row(username=username, password=password)
    return "created"

@anvil.server.callable
def authenticateUser(username, password):
  if app_tables.users.get(username=username, password=password):
    return "exists"   

  # adding a task
@anvil.server.callable
def addToCart(mealSize, addOns, price, userId, timeTake, taskName, datePick):
  app_tables.cart.add_row(
    mealSize=mealSize,
    addOns=', '.join(addOns) if addOns else 'None',
    price=round(price, 2),
    userId=userId,
    timeTake=timeTake,
    taskName=taskName,
    datePick=datePick
  )


  # saving user context
@anvil.server.callable
def addData(interests, hobbies, subjects, aims, skills, userId, advice):
  app_tables.data.add_row(
    interests = interests,
    hobbies = hobbies,
    subjects = subjects,
    aims = aims,
    skills = skills,
    userId = userId,
    advice = advice
  )

@anvil.server.callable
def deleteData(userId):
  table = app_tables.data  

  rows = table.search(userId=userId)

  for row in rows:
    row.delete()

# saving tasks analytics
@anvil.server.callable
def incrementTasksAdded(userId):
  row = app_tables.task.get(userId=userId)
  if row:
    row['taskTotal'] += 1
  else:
    app_tables.task.add_row(userId=userId, taskTotal=1)

@anvil.server.callable
def getTasksAdded(userId):
  row = app_tables.task.get(userId=userId)
  return row['taskTotal'] if row else 0

@anvil.server.callable
def getOpenTasks(userId):
  return len(app_tables.cart.search(userId=userId))

@anvil.server.callable
def getData(userId):
  return list(app_tables.data.search(userId=userId))


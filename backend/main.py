import os
from fastapi import FastAPI
from pydantic import BaseModel
from crewai import Agent, Task, Crew, Process
from crewai.llm import LLM
from dotenv import load_dotenv

# Load .env
load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
if not openai_api_key:
    raise ValueError("❌ OPENAI_API_KEY not found in .env file")

# FastAPI app
app = FastAPI()

# Request schema
class InterviewRequest(BaseModel):
    role: str  # e.g. "Software Engineer", "Data Scientist"

# LLM
llm = LLM(
    model="gpt-3.5-turbo",
    api_key=openai_api_key,
    temperature=0.8
)

# Agents
hr_agent = Agent(
    role="HR Agent",
    goal="Generate realistic interview questions",
    backstory="An HR manager who interviews candidates for various job roles.",
    allow_delegation=False,
    verbose=True,
    llm=llm,
)

candidate_agent = Agent(
    role="Candidate Agent",
    goal="Give structured, professional answers to interview questions",
    backstory="A well-prepared candidate aiming to impress the interviewer.",
    allow_delegation=False,
    verbose=True,
    llm=llm,
)

feedback_agent = Agent(
    role="Feedback Agent",
    goal="Analyze the answers and suggest improvements",
    backstory="A career coach who provides constructive feedback.",
    allow_delegation=False,
    verbose=True,
    llm=llm,
)


@app.post("/interview")
def run_interview(req: InterviewRequest):
    # Tasks
    hr_task = Task(
        description=f"Generate 3 interview questions for the role: {req.role}",
        expected_output="Three professional interview questions.",
        agent=hr_agent,
    )

    candidate_task = Task(
        description="Answer the HR Agent's questions with professional and clear responses.",
        expected_output="Answers to each interview question.",
        agent=candidate_agent,
        context=[hr_task]
    )

    feedback_task = Task(
        description="Provide feedback and improvement tips for the Candidate Agent's answers.",
        expected_output="Constructive feedback for each answer.",
        agent=feedback_agent,
        context=[candidate_task]
    )

    # Crew
    crew = Crew(
        agents=[hr_agent, candidate_agent, feedback_agent],
        tasks=[hr_task, candidate_task, feedback_task],
        process=Process.sequential,
        verbose=True,
    )

    result = crew.kickoff(inputs={})

    return {
        "questions": hr_task.output.raw,
        "answers": candidate_task.output.raw,
        "feedback": feedback_task.output.raw,
        "final_summary": result.raw
    }

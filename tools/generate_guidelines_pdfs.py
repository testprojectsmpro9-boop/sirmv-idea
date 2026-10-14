"""
One-off script to generate guideline PDFs into static/media/guidelines/.
Run from project root (directory containing manage.py):
  python tools/generate_guidelines_pdfs.py
"""
from pathlib import Path

from fpdf import FPDF
from fpdf.enums import XPos, YPos

ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "static" / "media" / "guidelines"


def write_pdf(filename: str, title: str, lines: list[str]) -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=14)
    pdf.add_page()
    pdf.set_font("Helvetica", "B", 13)
    pdf.multi_cell(0, 7, title, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(2)
    pdf.set_font("Helvetica", "", 10)
    for i, line in enumerate(lines, start=1):
        pdf.multi_cell(0, 5.5, f"{i}. {line}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.output(OUT_DIR / filename)


STUDENT_LINES = [
    "Students from Classes 1 to 10 are eligible to participate in the competition.",
    "An optional participation category is available for Classes 11 and 12 Science stream students.",
    "School dropout children between the age group of 6 to 18 years may also participate through the respective category.",
    "You are encouraged to be innovative, creative, and focused on problem-solving.",
    "Identify real-life problems from your home, school, village, city, or society and propose innovative solutions.",
    "Ideas submitted must be original and should not be copied from others or the internet.",
    "You can submit ideas related to: Technology; Environment; Education; Agriculture; Health & Safety; Social & Community Development.",
    "Solutions should be practical, affordable, useful, innovative, and easy to understand.",
    "Take part in your school's internal innovation competition, screening, or idea presentation session on the date communicated to you.",
    "Work with your teacher coordinator or innovation mentor when your school appoints one to guide you.",
    "Prepare for idea exhibitions, presentations, or evaluation rounds your school may organise before final selection.",
    "Prototype or working model submission is optional during the initial stage.",
    "You may include drawings, sketches, charts, diagrams, or photographs to explain your ideas.",
    "Ideas can be submitted in English, Kannada, or any Indian language.",
    "Ensure your entry includes proper student details and a clear explanation of the idea, as required by your school or the submission form.",
    "Submit your entry before the announced deadline.",
    "The decision of the jury or evaluation committee will be final and binding.",
    "If selected, you may receive mentorship support, prototype development guidance, certificates and awards, exhibition opportunities, and innovation recognition.",
    "Ideas can be submitted through email, WhatsApp, postal channels, or the online submission form on the website, as directed by your school.",
    "Participate honestly and support your peers in learning together.",
]

SCHOOL_LINES = [
    "Schools having students from Classes 1 to 10 are eligible to participate in the competition.",
    "An optional participation category is available for Classes 11 and 12 Science stream students.",
    "School dropout children between the age group of 6 to 18 years may also participate through the respective category.",
    "Schools are encouraged to promote innovation, creativity, and problem-solving among students.",
    "Students should identify real-life problems from home, school, village, city, or society and propose innovative solutions.",
    "Ideas submitted by students must be original and should not be copied from others or the internet.",
    "Students can submit ideas related to: Technology; Environment; Education; Agriculture; Health & Safety; Social & Community Development.",
    "Solutions should be practical, affordable, useful, innovative, and easy to understand.",
    "Schools may organize an internal innovation competition, screening, or idea presentation session on a suitable date.",
    "Schools are encouraged to appoint a teacher coordinator or innovation mentor to guide students during participation.",
    "Schools can conduct idea exhibitions, presentations, or evaluation rounds before final selection.",
    "Each school can shortlist and submit a maximum of 2 best ideas to the next level of evaluation.",
    "Prototype or working model submission is optional during the initial stage.",
    "Students may include drawings, sketches, charts, diagrams, or photographs to explain their ideas.",
    "Ideas can be submitted in English, Kannada, or any Indian language.",
    "Schools should ensure that all submitted entries contain proper student details and clear explanations of the idea.",
    "Selected ideas must be submitted before the announced deadline.",
    "The decision of the jury/evaluation committee will be final and binding.",
    "Selected students and schools may receive: Mentorship Support; Prototype Development Guidance; Certificates & Awards; Exhibition Opportunities; Innovation Recognition.",
    "Ideas can be submitted through: Email Submission; WhatsApp Submission; Postal Submission; Online Submission Form available on the website.",
    "Schools are encouraged to motivate maximum student participation and support grassroots innovation initiatives.",
]

GROUP_LINES = [
    "Each group may include up to 2 students working together on one original idea or innovation.",
    "All members must meet the eligibility criteria for their class level and participation category (including optional senior science and dropout categories where applicable).",
    "The idea must be developed jointly by the team; copying from others, seniors, or the internet is not permitted.",
    "Submit one entry per idea and include every member's name, class, and school details as required by your school or the submission form.",
    "Ideas may relate to Technology, Environment, Education, Agriculture, Health & Safety, or Social & Community Development.",
    "Solutions should be practical, affordable, useful, innovative, and easy to understand.",
    "Follow your school's internal competition schedule and the instructions of your teacher coordinator or innovation mentor.",
    "Prototype or working model submission is optional during the initial stage.",
    "You may include drawings, sketches, charts, diagrams, or photographs to explain your shared idea.",
    "Submissions may be in English, Kannada, or any Indian language.",
    "Your school may shortlist group entries alongside individual entries according to the announced limits (for example, a maximum number of ideas advancing from each school).",
    "If selected, the team may receive mentorship, prototype development support, certificates, exhibition opportunities, and innovation recognition, as applicable.",
    "The jury treats the entry as one submission; the evaluation committee's decision will be final and binding.",
    "Submit through email, WhatsApp, postal channels, or the online submission form on the website, as directed by your school.",
    "Work fairly as a team, acknowledge each member's contribution, and support a positive learning environment for all participants.",
]


def main() -> None:
    write_pdf(
        "student-guidelines.pdf",
        "Rules & Guidelines for Students - Visvesvaraya Idea Bank",
        STUDENT_LINES,
    )
    write_pdf(
        "school-guidelines.pdf",
        "Rules & Guidelines for Schools - Visvesvaraya Idea Bank",
        SCHOOL_LINES,
    )
    write_pdf(
        "group-guidelines.pdf",
        "Rules & Guidelines for Group Participants - Visvesvaraya Idea Bank",
        GROUP_LINES,
    )
    print("Wrote PDFs to", OUT_DIR)


if __name__ == "__main__":
    main()

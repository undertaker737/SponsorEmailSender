import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import time

# Your Gmail / Workspace account
EMAIL = "<email>"
PASSWORD = ""# go to 2 factor auth and at the bottom there should be something that says app password use that

# List of sponsors (company name + email)
sponsors = [
    {"name": "[Sponsor Email]", "email": "[Sponsor email]"},
]



# Email subject
SUBJECT = "Daydream Hackathon Sponsorship Opportunity"

# Example info for sending
SENDER_NAME = "<your name>"
SENDER_GRADE = "Grade"
CITY = "<city>"
PHONE = "<phone>"
WEBSITE = "<website>"
LOCATION = "<Location>"

# HTML template using cid for images
# You can change this. In fact I think you should.
def load_template(company, name, grade, city):
    return f"""
<html>
<head>
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono&display=swap" rel="stylesheet">
<style>
body {{
    background-color: #C2EDFB;
    font-family: 'JetBrains Mono', monospace;
    color: #1a1a1a;
}}
header, footer {{
    background-color: #ffffff;
    text-align: center;
    padding: 10px 0;
}}
.container {{
    padding: 30px 20px;
    max-width: 700px;
    margin: 0 auto;
    background-color: #ffffff;
    border-radius: 12px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}}
h1 {{ font-family: 'Orbitron', sans-serif; color: #1E90FF; }}
h2 {{ color: #2E8B57; }}
h3 {{ color: #FF6347; }}
p {{ font-size: 16px; line-height: 1.6; text-align: justify; }}
a {{ color: #1E90FF; text-decoration: none; }}
</style>
</head>
<body>

<header>
    <h1>Daydream Hackathon</h1>
    <img src="cid:header_img" alt="Header" style="max-width:100%; height:auto;">
</header>

<div class="container">
    <h2>Sponsorship Opportunity</h2>
    <h3>Daydream Hackathon ({city})</h3>

    <p>Dear <strong>{company}</strong> Team,</p>

    <p>I hope this email finds you well. My name is <strong>{name}</strong>, a <strong>{grade}</strong> student and member of Hack Club. We're organizing Daydream Hackathon this year and would love to explore a sponsorship partnership with your company.</p>

    <p>On September 27th, we're hosting a 24-hour hackathon for over 100 teenagers at <strong>{LOCATION}</strong>. We are seeking sponsors who believe in empowering the next generation of innovators.</p>

    <p>Daydream is a beginner-friendly game jam, where students collaborate to build games over 24 hours. This event is part of a larger global initiative.</p>

    <p>By sponsoring Daydream Hackathon, your company would gain valuable exposure to tech-savvy teenagers and their families, while supporting STEM education in <strong>{city}</strong>. Any kind of help is appreciated—whether it’s resources, mentorship, or simply spreading the word.</p>

    <p>You can learn more about our event at <a href="{WEBSITE}">{WEBSITE}</a> or reach me directly at <strong>{PHONE}</strong>.</p>

    <p>Thank you for considering supporting our young innovators, and we look forward to your favorable reply.</p>

    <p>Warm regards,<br>
    <strong>{name}</strong><br>
    On behalf of the Daydream Hackathon team</p>
</div>

<footer>
    <img src="cid:footer_img" alt="Footer" style="max-width:100%; height:auto;">
</footer>

</body>
</html>
"""

def send_email(to_email, company, name=SENDER_NAME, grade=SENDER_GRADE, city=CITY):
    msg = MIMEMultipart('related')
    msg['From'] = EMAIL
    msg['To'] = to_email
    msg['Subject'] = SUBJECT

    msg_alternative = MIMEMultipart('alternative')
    msg.attach(msg_alternative)

    html_content = load_template(company, name, grade, city)
    msg_alternative.attach(MIMEText(html_content, 'html'))

    # Attach images inline
    for img_path, cid in [("Header.png", "header_img"), ("Footer.png", "footer_img")]:
        with open(img_path, 'rb') as f:
            img = MIMEImage(f.read())
            img.add_header('Content-ID', f'<{cid}>')
            img.add_header('Content-Disposition', 'inline', filename=img_path)
            msg.attach(img)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(EMAIL, PASSWORD)
        server.sendmail(EMAIL, to_email, msg.as_string())

    print(f"✅ Sent email to {company} ({to_email})")

# Send emails one by one with delay
for sponsor in sponsors:
    send_email(sponsor["email"], sponsor["name"])
    time.sleep(30)

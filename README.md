# Email Sender

This project is a simple Python script to send emails using your Gmail account. It supports sending emails with attachments and custom headers/footers (images).

## Features
- Send emails via Gmail
- Attach images (e.g., header and footer)
- Simple configuration

## Requirements
- Python 3.7 or higher
- Gmail account with 2-Step Verification enabled
- Gmail App Password (see below)

## Dependencies
Install the required Python packages using pip:

```bash
pip install smtplib email pillow
```

If you use additional packages in `main.py`, add them to the list above.

## Setting Up Gmail App Password
Google requires an App Password to allow third-party apps to send emails if you have 2-Step Verification enabled. Follow these steps:

1. Go to your [Google Account Security page](https://myaccount.google.com/security).
2. Ensure 2-Step Verification is enabled.
3. Under "Signing in to Google," select **App Passwords**.
4. Sign in again if prompted.
5. Select **Mail** as the app and **Windows Computer** (or any name) as the device.
6. Click **Generate**.
7. Copy the 16-character app password. Use this in your script instead of your regular Gmail password.

**Never share your app password.**

## Usage

1. Replace the default `Header.png` and `Footer.png` images in the project directory with your own header and footer images. This will customize the look of your emails.
	- If you are a Daydream event organizer, you can find high-quality graphics at [Daydream Graphics Repository](https://github.com/advaitconty/daydream/tree/master/Graphics).
2. Edit `main.py` to add your email, app password, recipient, and message details.
3. Run the script:

```bash
python main.py
```

## Notes
- This script is for educational purposes. Do not use it to send spam.
- Keep your app password secure and do not commit it to version control.

## License
MIT License

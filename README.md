# CS50's Capstone Project "MyJobBoard"

![Job Board Photo](jobs.jpg)

## Introduction
This project uses django, JavaScript, HTML, and Boostrap to create a job board where users can post job ads, submit applications, and job posters can view resumes and cover letters.'

## Video Demo
https://www.youtube.com/watch?v=krjuYg493GM&ab_channel=Shallonp

## Distinctiveness and Complexity

### Distinctiveness
This project stands out from others in the course due to its specific purpose of facilitating employers to post and oversee job applications, while also enabling job seekers to submit applications in the form of a resume and cover letter PDFs for employers' review. This distinctive functionality caters to both employers and job seekers, providing a comprehensive platform for the job application process.

My project diverges from previous web apps created in the course by offering enhanced capabilities for job posters and job seekers. Unlike previous apps that restricted user submissions to predefined fields, this project allows job posters to utilize text fields with features resembling a word processor, akin to Microsoft Word, enabling them to create highly informative postings. Additionally, job seekers have the ability to submit PDF documents to the backend, which can be reviewed by job posters. This unique approach provides greater flexibility and functionality for both parties involved in the job application process.

### Complexity
The project meets the complexity requirements by incorporating Bootstrap to ensure that elements on the page dynamically render, making them viewable on both desktop and mobile devices. Three Django models are utilized to store information regarding job postings submitted, as well as applications sent to job postings. Additionally, a user model is implemented to manage registered users on the site. JavaScript is employed to dynamically render information regarding submissions to applications, and to add Bootstrap classes to navbar links upon clicking, providing visual cues to help users identify the active page.

Further complexity has been integrated to empower users to create sophisticated job postings through Django forms enhanced with Bootstrap classes. The utilization of CKEditor enables job posters to craft postings according to their preferences, leveraging RichTextFields for styling flexibility. By incorporating Bootstrap classes, the postings become visually appealing and responsive. Moreover, error handling is seamlessly managed through Django forms, directing users to incorrect fields with precision, thereby enhancing the overall user experience. 

## Features

1. **Post a Job**: Authenticated users who have registered can create a job posting by using the nav bar to "Post a Job" where they can include further relevant details including, job title, location, logo url, etc. But can eloborate further by using rich text fields to create bullet points, bold text, formatting, etc.
2. **Job Management**: A posted job can be managed by the creator by going to "Manage Job Postings" finding their desired post and viewing a modal where they can:
    1. **View Listing** like a job seeker.
    2. **Edit Listing**: Make changes to the job details.
    3. **View Applicants**: See who has applied including their name, email, resume, and cover letter as PDF's.
    4. **Close Application**: Close the application removing it from visibility of other users. Closed applications will be displayed as light gray and say they are closed for the creator to show that they have closed the application and wont appear at all for other users.
3. **View and Apply**: Anyone can view a job posting on the homepage by clicking on the "view" button where they will be provided details including a summary, location, pay if provided, etc... At the bottom of the page they can apply where they can upload their resume and cover letter as a pdf to submit their application for the position.
4. **Boostrap**: Boostrap is used to make the application look visually appealing, keep elements aligned, allow for modals for form submissions as to not redirect users to another page, and have a beautiful nav bar.

## How to Run

1. Clone this repository: https://github.com/shallondev/myjobboard.git
2. Ensure python3 is installed.
3. Execute `pip3 install -r requirements.txt`
4. Execute `cd myjobboard`
5. Execute `python3 manage.py runserver`
6. Read terminal to locate address to access application through your web browser.

## Files Included
- **media**: Folder where PDF's of resumes and cover letters are stored.
- **db.sqlite3** Database holding job postings, users, and job applications.
- **templates/jobportal**: Contains HTML files providing the structure of various URL's that can be accessed.
- **static/jobportal**: Contains all JavaScript files which hold front-end logic of the application, CSS styling, a logo image, and folders for ckeditor stuff.
- **admin.py**: Registes models that can be accessed by server admins.
- **forms.py**: Creates Form classes that are associated with job applications and postings.
- **models.py**: Contains all the models used in this application.
- **urls.py**: Contains all urls that can be accessed in this application.
- **views.py**: Contains logic behind that rendering requests recieved to the backend. Responsible for rendering different html files for different URL's.
- **myjobboard/** A folder that holds the files created when you create a django project, some changes were made to urls.py and settings.py to fit the needs of this project.

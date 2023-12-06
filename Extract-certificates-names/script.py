from bs4 import BeautifulSoup

# Dummy HTML content. Replace this with your actual HTML content.
html_content = "example.html"

# Parse the HTML content with BeautifulSoup
# soup = BeautifulSoup(html_content, 'html.parser')
with open(html_content, 'r', encoding='utf-8') as file:
    soup = BeautifulSoup(file, 'html.parser')

# Assuming the course name and date are in span tags with the following classes.
courses = soup.find_all('span', class_='lls-card-headline')
dates = soup.find_all('span', class_='lls-card-completion-state--completed')
datesInTxt = [span.get_text(strip=True) for span in dates]

# Create a list to hold the course details strings
course_details = []

# Extract the course names and dates and store them in the list
for course, date in zip(courses, dates):
    course_name = course.get_text(strip=True)
    completion_date = date.get_text(strip=True).replace('Completed ', '')
    course_details.append(f"{course_name} ({completion_date})")

# Join the course details strings with a " - " and write to a text file
output_string = " - ".join(course_details)

output_file_path = r'C:\Users\Alvar\Documents\PROJECTS DISK C\Scripts\Extract-certificates-names\courses_output.txt'

with open(output_file_path, 'w') as file:
    file.write(output_string)

# Output to let the user know the file has been saved
print("The course details have been saved to courses_output.txt.")

# Monte Carlo Pi Estimation

This project is a Django-based web application that visualizes the Monte Carlo method to estimate the value of π (pi). The application uses JavaScript to generate random points, calculate the approximation of π, and display the results graphically.

## Features

- Interactive slider to change the number of points used in the Monte Carlo simulation.
- Real-time visualization of points and the unit circle.
- Display of the calculated value of π.

## Prerequisites

- Python 3.8 or higher
- Django 3.2 or higher
- Node.js (for JavaScript and Tailwind CSS integration)
- Git (for version control)

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/sbstnzcr/django-pi.git
   cd monte-carlo-pi-estimation
   ```

2. **Create and Activate a Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**

   Create a `.env` file in the root of the project and add your secret key and any other environment variables:

   ```env
   SECRET_KEY=your-django-secret-key
   ```

5. **Run Database Migrations**

   ```bash
   python manage.py migrate
   ```

6. **Start the Development Server**

   ```bash
   python manage.py runserver
   ```

7. **Open the Application in Your Browser**

   Visit `http://127.0.0.1:8000` to see the application in action.

## Usage

- Use the slider to change the number of points used in the Monte Carlo simulation.
- The canvas will update in real-time to show the points and the estimated value of π.
# Django-Ecommerce

Modern ecommerce website built with Django 3.2.20, Python 3.12, featuring product management and shopping cart functionality

![image](https://user-images.githubusercontent.com/29988949/65267147-499fc580-dac9-11e9-90e8-eccbc93c7c3a.png)

`Product Slide`

![image](https://user-images.githubusercontent.com/29988949/65999313-ff67fe00-e451-11e9-9ed9-fc7bce704f17.png)

`Shop Page`
![image](https://user-images.githubusercontent.com/29988949/66098968-923f9000-e559-11e9-8691-cd5c2b181ca1.png)

`Product Detail Page`
![image](https://user-images.githubusercontent.com/29988949/66291084-bff84200-e895-11e9-8d53-3aa23b29dbae.png)

`Cart Page`
![image](https://user-images.githubusercontent.com/29988949/66291144-f0d87700-e895-11e9-8545-b8f93f799063.png)

`BillingAddress Page`
![image](https://user-images.githubusercontent.com/29988949/66291542-013d2180-e897-11e9-8ea9-40afcb90cee2.png)

`Order Success Page`
![image](https://user-images.githubusercontent.com/29988949/66291657-3e091880-e897-11e9-830b-6cf44e72a995.png)




# Installation

## 🐳 Docker Setup (Recommended)

The fastest way to get started is using Docker. Skip to the [Docker Setup section](#docker-setup-recommended) below if you have Docker installed.

### Installation Options Comparison

| Method | Pros | Cons | Best For |
|--------|------|------|----------|
| 🐳 **Docker** | ✅ Quick setup<br>✅ No dependency issues<br>✅ Consistent environment | ❌ Requires Docker<br>❌ Larger disk usage | Production, Quick demos |
| 🔧 **Manual** | ✅ Full control<br>✅ Development friendly<br>✅ Smaller footprint | ❌ More setup steps<br>❌ Potential dependency conflicts | Development, Learning |

## Manual Installation

### Prerequisites

Before starting, ensure you have the following installed on your VM:
- Python 3.12 or higher
- Git
- pip (Python package manager)

## Quick Setup Commands for VM

If you're setting up this project on a fresh VM, run these commands in order:

### 1. Update System and Install Dependencies

```bash
# Update package list
sudo apt update

# Install Python 3.12, pip, git, and build tools
sudo apt install -y python3.12 python3.12-venv python3-pip git build-essential python3-dev libffi-dev

# Verify installations
python3.12 --version
git --version
```

### 2. Clone the Repository

```bash
# Clone the project
git clone https://github.com/itsBaivab/django-e-commerces.git

# Navigate to project directory
cd Django-Ecommerce
```

### 3. Set Up Virtual Environment

```bash
# Create virtual environment
python3.12 -m venv venv

# Activate virtual environment (Linux/Mac)
source venv/bin/activate

# For Windows (if using Windows VM)
# venv\Scripts\activate
```

### 4. Install Python Dependencies

```bash
# Upgrade pip, setuptools, and wheel first
pip install --upgrade pip setuptools wheel

# Install project dependencies
pip install -r requirements.txt
```

### 5. Set Up Database

```bash
# Create database migrations
python manage.py makemigrations

# Apply migrations to create database tables
python manage.py migrate
```

### 6. Create Admin User (Optional)

```bash
# Create superuser for admin access
python manage.py createsuperuser
# Follow prompts to set username, email, and password
# Recommended: Username: admin, Password: admin123 (for development only)
```

### 7. Run the Development Server

```bash
# Start the Django development server
python manage.py runserver 0.0.0.0:8000
```

The application will be available at `http://your-vm-ip:8000`

## Docker Setup (Recommended)

The easiest way to run this project is using Docker with the pre-built image from Docker Hub.

### Prerequisites for Docker
- Docker installed on your VM/machine
- Internet connection to pull the image

#### Install Docker (if not already installed)

**For Ubuntu/Debian:**
```bash
# Update package index
sudo apt update

# Install Docker
sudo apt install -y docker.io

# Start and enable Docker
sudo systemctl start docker
sudo systemctl enable docker

# Add your user to docker group (optional, to run without sudo)
sudo usermod -aG docker $USER

# Log out and back in, or run:
newgrp docker

# Verify installation
docker --version
```

**For CentOS/RHEL:**
```bash
# Install Docker
sudo yum install -y docker

# Start and enable Docker
sudo systemctl start docker
sudo systemctl enable docker

# Verify installation
docker --version
```

### Quick Docker Setup

**Option 1: Using Pre-built Image from Docker Hub**

```bash
# Pull the latest image from Docker Hub
docker pull e-commerces-django-app:latest

# Run the container
docker run -d \
  --name django-ecommerce \
  -p 8000:8000 \
  e-commerces-django-app:latest

# Check if container is running
docker ps
```

**Option 2: Build from Source**

```bash
# Clone the repository (if not already done)
git clone https://github.com/itsBaivab/django-e-commerces.git
cd Django-Ecommerce

# Build the Docker image
docker build -t django-ecommerce-local .

# Run the container
docker run -d \
  --name django-ecommerce \
  -p 8000:8000 \
  django-ecommerce-local

# Check if container is running
docker ps
```

### Docker Setup with Environment Variables

For production use with custom settings:

```bash
# Run with environment variables
docker run -d \
  --name django-ecommerce \
  -p 8000:8000 \
  -e DEBUG=False \
  -e SECRET_KEY='your-production-secret-key' \
  e-commerces-django-app:latest
```

### Docker Management Commands

```bash
# Stop the container
docker stop django-ecommerce

# Start the container
docker start django-ecommerce

# View container logs
docker logs django-ecommerce

# Access container shell (for debugging)
docker exec -it django-ecommerce /bin/bash

# Remove container (when no longer needed)
docker rm django-ecommerce

# Remove image (to free up space)
docker rmi e-commerces-django-app:latest
```

### Custom Docker Port

If port 8000 is already in use:

```bash
# Run on a different port (e.g., 8080)
docker run -d \
  --name django-ecommerce \
  -p 8080:8000 \
  e-commerces-django-app:latest

# Access at http://your-vm-ip:8080
```

### Docker Compose (Optional)

Create a `docker-compose.yml` file for easier management:

```yaml
version: '3.8'

services:
  web:
    image: e-commerces-django-app:latest
    container_name: django-ecommerce
    ports:
      - "8000:8000"
    environment:
      - DEBUG=False
      - SECRET_KEY=your-secret-key-here
    restart: unless-stopped

  # Optional: Add PostgreSQL database
  # db:
  #   image: postgres:13
  #   container_name: postgres-db
  #   environment:
  #     POSTGRES_DB: ecommerce_db
  #     POSTGRES_USER: postgres
  #     POSTGRES_PASSWORD: your-db-password
  #   volumes:
  #     - postgres_data:/var/lib/postgresql/data

# volumes:
#   postgres_data:
```

Then run with:

```bash
# Start services
docker-compose up -d

# Stop services
docker-compose down

# View logs
docker-compose logs
```

The application will be available at `http://your-vm-ip:8000`

### Building and Pushing Docker Image (For Developers)

If you want to build and push your own version of the image:

```bash
# Build the image with a tag
docker build -t your-dockerhub-username/django-ecommerce:latest .

# Test the image locally
docker run -d --name test-container -p 8000:8000 your-dockerhub-username/django-ecommerce:latest

# Push to Docker Hub (requires docker login)
docker push your-dockerhub-username/django-ecommerce:latest

# Clean up test container
docker stop test-container
docker rm test-container
```

## Manual Installation (Alternative Method)

If you prefer step-by-step installation:

```bash
# Clone repository
git clone https://github.com/zinmyoswe/Django-Ecommerce.git
cd Django-Ecommerce

# Create and activate virtual environment
python3.12 -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

# Install dependencies
pip install --upgrade pip setuptools wheel

pip install -r requirements.txt

# Set up database
python manage.py makemigrations
python manage.py migrate

# Create admin user
python manage.py createsuperuser

# Run development server
python manage.py runserver 0.0.0.0:8000
```

## Project Dependencies

The project uses these main dependencies (automatically installed with requirements.txt):

- **Django 3.2.20** - Web framework
- **django-allauth 0.54.0** - Authentication and registration
- **django-crispy-forms 2.0** - Form styling
- **django-countries 7.5.1** - Country field support
- **Pillow 10.0.0** - Image processing
- **psycopg2-binary 2.9.9** - PostgreSQL adapter

## Troubleshooting

### Common Issues and Solutions:

#### 1. Permission Denied Error
```bash
sudo chown -R $USER:$USER /path/to/project
```

#### 2. Port Already in Use
```bash
# Use a different port
python manage.py runserver 0.0.0.0:8001

# Or kill process using port 8000
sudo lsof -t -i tcp:8000 | xargs kill -9
```

#### 3. Dependencies Installation Failed
```bash
# Install system dependencies first
sudo apt install -y build-essential python3-dev libffi-dev

# Then retry pip install
pip install -r requirements.txt
```

#### 4. Database Issues
```bash
# Reset database (WARNING: This will delete all data)
rm db.sqlite3
python manage.py makemigrations
python manage.py migrate
```

## Environment Variables

For production deployment, set these environment variables:

```bash
export DEBUG=False
export SECRET_KEY='your-secret-key-here'
```

## Testing

Run the test suite:

```bash
# Run all tests
python manage.py test

# Run specific app tests
python manage.py test core

# Run with pytest (if installed)
pytest
```

## Admin Access

After creating a superuser, access the admin panel at:
- URL: `http://your-vm-ip:8000/admin/`
- Default credentials (if following setup): 
  - Username: `admin`
  - Password: `admin123` (or whatever you set during `createsuperuser`)

## Demo

Live demo available at: http://djangoecommerce.pythonanywhere.com

## Features

- **Product Management**: Categories, product listings, product details
- **Shopping Cart**: Add/remove items, quantity management  
- **User Authentication**: Registration, login, logout with django-allauth
- **Order Management**: Order tracking and history
- **Admin Panel**: Django admin for managing products, orders, users
- **Responsive Design**: Mobile-friendly interface
- **Image Management**: Product image upload and display

## Tech Stack

- **Backend**: Django 3.2.20, Python 3.12
- **Database**: SQLite (development), PostgreSQL (production ready)
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap
- **Authentication**: Django Allauth
- **Image Processing**: Pillow

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Commit changes: `git commit -am 'Add some feature'`
4. Push to branch: `git push origin feature-name`
5. Create a Pull Request

## License

This project is open source and available under the [MIT License](LICENSE).

## Credits

- **HTML Template**: [Fashe by Colorlib](https://colorlib.com/etc/fashe/index.html)
- **Original Project**: Based on Django-Ecommerce by zinmyoswe

## Support

If you encounter any issues during setup, please:
1. Check the troubleshooting section above
2. Ensure all prerequisites are installed
3. Verify Python and Django versions
4. Create an issue on the repository with detailed error messages



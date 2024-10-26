# Use an official Python image as a base
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy requirements.txt
COPY requirements.txt .

# Upgrade pip and install dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Install Jupyter Notebook
RUN pip install notebook

# Copy the rest of your project files into the container
COPY . .

# Expose the port Jupyter uses
EXPOSE 8888

# Set the CMD to start Jupyter Notebook
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--allow-root", "--no-browser", "--notebook-dir=/app"]


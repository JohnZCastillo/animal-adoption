FROM python:3.12-slim

WORKDIR /usr/src/app

# Copy requirements first for better layer caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Create non-root user for security
RUN useradd --create-home appuser && chown -R appuser:appuser /usr/src/app
USER appuser

# Expose Flask default port
EXPOSE 5000

# Use proper Flask CLI command for production-like setup
ENV FLASK_APP=src
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000

ENTRYPOINT ["flask"]

CMD ["run"]

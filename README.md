# MediLink - AI-Powered ADR Detection

MediLink is an advanced platform that uses artificial intelligence to detect Adverse Drug Reactions (ADRs) by analyzing data from multiple sources including social media, wearable devices, and electronic health records.

## 🚀 Features

- **🤖 AI-Powered Drug Prediction**: Predicts drugs based on reported side effects using machine learning (75% accuracy)
- **💬 Interactive Chat Interface**: Modern chat interface with real-time AI interaction
- **⚡ Real-time ADR Detection**: Identifies potential adverse drug reactions before they become critical
- **📊 Comprehensive Drug Database**: Access to 2931+ medications with detailed information
- **🔗 Multi-Source Data Integration**: Combines data from social media, wearables, and EHRs
- **📈 Confidence Scoring**: Provides accurate confidence percentages for AI predictions
- **🎯 56+ Drug Classes**: Extensive coverage of pharmaceutical categories
- **🎨 Professional UI**: Clean, medical-themed interface with green color scheme

## 🚀 Quick Start

### 1. Start the AI Server
```bash
cd python
# Activate conda environment (recommended)
conda activate medilink

# Or use pip in virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

# Start the AI server
python ai_server.py
```

### 2. Start the Spring Boot Application
```bash
# In the project root directory
./mvnw spring-boot:run
```

### 3. Access the Application
- **Web Application**: `http://localhost:8080`
- **AI Chat Interface**: `http://localhost:8080/chat.html`
- **AI API**: `http://localhost:8051`

## 🌐 Application URLs

- **Home Page**: http://localhost:8080/
- **AI Chat**: http://localhost:8080/chat.html  
- **Profile**: http://localhost:8080/profile.html
- **Research**: http://localhost:8080/research.html

## Chat Interface Integration

The chat interface (`chat.html`) now includes:
- Real-time AI predictions
- Fallback endpoints (Spring Boot → Flask)
- Enhanced UX with loading indicators
- Confidence scores and alternative suggestions
- Medical disclaimers and safety warnings

## Project Architecture

```
project-root/
├── src/main/                      # Spring Boot application
│   ├── java/dev/culturiz/hacka_boot/
│   │   ├── model/                 # Data models
│   │   ├── run/                   # Drug-related components
│   │   ├── service/               # Services including OpenAI
│   │   └── HackaBootApplication.java
│   └── resources/
│       ├── static/                # Frontend files
│       │   ├── chat.html
│       │   ├── index.html
│       │   ├── styles.css
│       │   └── script.js
│       ├── data/                  # Data files
│       │   └── drugs.json
│       └── application.properties
├── python/                        # Python ML components
│   ├── app.py                     # Flask API for ML model
│   ├── train_model.py             # Model training script
│   └── models/                    # Directory for saved models
│       └── drug_prediction_model.pkl
└── pom.xml                        # Maven dependencies
```

## Setup Instructions

### Prerequisites

- Java 21
- Maven
- Python 3.8+
- MySQL (optional, H2 is configured by default)

### Backend Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd medilink
   ```

2. Build the Spring Boot application:
   ```bash
   mvn clean install
   ```

3. Run the Spring Boot application:
   ```bash
   mvn spring-boot:run
   ```

### Python ML Service Setup

1. Navigate to the Python directory:
   ```bash
   cd python
   ```

2. Install required packages:
   ```bash
   pip install flask flask-cors scikit-learn pandas numpy pickle-mixin
   ```

3. Update the model path in `app.py`:
   ```python
   # Change this line
   with open("models/drug_prediction_model.pkl", 'rb') as file:
   ```

4. Run the Flask application:
   ```bash
   python app.py
   ```

## API Endpoints

### Drug API

- `GET /api/drugs` - Get all drugs
- `GET /api/drugs/{id}` - Get a drug by ID
- `GET /api/drugs/condition/{condition}` - Find drugs by medical condition
- `GET /api/drugs/name/{name}` - Find drugs by name
- `POST /api/drugs` - Create a new drug
- `PUT /api/drugs/{id}` - Update a drug
- `DELETE /api/drugs/{id}` - Delete a drug

### ML API

- `POST /predict` - Predict drug based on side effects
    - Request body: `{"side_effects": "headache and nausea"}`
    - Response: `{"predicted_drug": "Ibuprofen"}`

## Configuration

The `application.properties` file contains configuration settings including database and OpenAI API settings. Make sure to set your own OpenAI API key:

```properties
spring.ai.openai.api-key=your-api-key-here
```

## Contributors

- Divi Jaiwanth
- SP Bharath
- Meet Tak
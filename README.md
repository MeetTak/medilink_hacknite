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

## 💬 Chat Interface

The modern chat interface includes:
- **🎯 Real-time AI predictions** with 75% accuracy
- **📊 Confidence scoring** with actual percentages  
- **🔄 Fallback system** (Spring Boot → Flask AI Server)
- **⚡ Enhanced UX** with loading indicators and animations
- **🏥 Medical disclaimers** and safety warnings
- **🎨 Professional design** with green medical theme
- **📱 Responsive layout** for all devices

## 🏗️ Project Architecture

```
medilink/
├── src/main/                           # Spring Boot Backend
│   ├── java/dev/culturiz/hacka_boot/
│   │   ├── run/                        # Drug API & Controllers
│   │   ├── user/                       # User management
│   │   └── HackaBootApplication.java   # Main application
│   └── resources/
│       ├── static/                     # Frontend Assets
│       │   ├── index.html              # Landing page
│       │   ├── chat.html               # AI Chat interface
│       │   ├── profile.html            # User profile
│       │   ├── research.html           # Research page
│       │   ├── styles.css              # Styling
│       │   ├── chat-style.css          # Chat styling
│       │   ├── script.js               # JavaScript
│       │   └── assets/                 # Images & icons
│       ├── data/
│       │   └── drugs.json              # Drug database (2931 drugs)
│       └── application.properties      # Configuration
├── python/                             # AI/ML Components
│   ├── ai_server.py                    # Flask AI API server
│   ├── final_model.py                  # Model training
│   ├── final.csv                       # Training dataset
│   ├── lookup_table.csv                # Drug lookup
│   ├── main.py                         # Utilities
│   └── requirements.txt                # Python dependencies
├── hacka_boot_data/                    # Research Datasets
│   ├── drugs_side_effects_drugs_com.csv
│   ├── medicine_dataset.csv
│   └── [other medical datasets]
└── pom.xml                             # Maven configuration
```

## ⚙️ Setup Instructions

### Prerequisites

- **Java 21** or higher
- **Maven 3.6+**
- **Python 3.8+**
- **Conda** (recommended) or **pip**

### 🔧 Backend Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/MeetTak/medilink_hacknite.git
   cd hacka_boot
   ```

2. **Build the Spring Boot application:**
   ```bash
   ./mvnw clean install
   ```

3. **Run the Spring Boot application:**
   ```bash
   ./mvnw spring-boot:run
   ```

### 🤖 Python AI Service Setup

1. **Navigate to Python directory:**
   ```bash
   cd python
   ```

2. **Set up environment (Conda recommended):**
   ```bash
   # Option 1: Conda (recommended)
   conda create -n medilink python=3.11
   conda activate medilink
   
   # Option 2: Virtual environment
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Start the AI server:**
   ```bash
   python ai_server.py
   ```

## 📡 API Endpoints

### Spring Boot Drug API (Port 8080)

- `GET /api/drugs` - Get all drugs (2931+ medications)
- `GET /api/drugs/{id}` - Get drug by ID  
- `GET /api/drugs/condition/{condition}` - Find drugs by medical condition
- `GET /api/drugs/name/{name}` - Find drugs by name
- `POST /api/drugs` - Create new drug
- `PUT /api/drugs/{id}` - Update drug
- `DELETE /api/drugs/{id}` - Delete drug

### AI Prediction API (Port 8051)

- `POST /predict` - AI drug prediction based on symptoms
    - **Request**: `{"side_effects": "headache and nausea"}`
    - **Response**: `{"predicted_drug": "ibuprofen", "confidence": 0.85}`

### Web Pages (Port 8080)

- `/` - Landing page with overview
- `/chat.html` - AI chat interface  
- `/profile.html` - User profile management
- `/research.html` - Research documentation

## 🔧 Configuration

### Database
- **Default**: H2 in-memory database
- **Production**: Configure MySQL in `application.properties`

### AI Model
- **Algorithm**: MultinomialNB with TF-IDF vectorization
- **Accuracy**: 75% on medical datasets
- **Classes**: 56+ drug categories
- **Training Data**: Comprehensive medical symptom-drug mappings

## 🧪 AI Model Details

- **Model Type**: Multinomial Naive Bayes
- **Feature Extraction**: TF-IDF Vectorization
- **Training Dataset**: Medical symptom-drug correlations
- **Accuracy**: 75% on test data
- **Drug Classes**: 56 pharmaceutical categories
- **Confidence Scoring**: Probabilistic predictions with percentages

## 🎨 UI Features

- **Design**: Professional medical theme with green color scheme
- **Typography**: Inter font family for modern appearance  
- **Icons**: FontAwesome integration
- **Responsive**: Mobile-first design approach
- **Animations**: Smooth transitions and loading states
- **Accessibility**: WCAG compliant color contrasts

## 👥 Contributors

- **Divi Jaiwanth** - Full Stack Development & AI Integration
- **SP Bharath** - Backend Development & API Design  
- **Meet Tak** - Frontend Development & UI/UX Design

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📞 Support

For support and questions:
- Create an issue on GitHub
- Contact the development team
- Check the documentation in `/research.html`

---

**MediLink** - Transforming healthcare through AI-powered adverse drug reaction detection. 🏥✨
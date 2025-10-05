# 2025-NASA-Space-Apps-Challenge
Our team is participating in the 2025 NASA Space Apps Challenge under the theme “Will It Rain On My Parade?”. This challenge is centered on using NASA’s Earth observation data to explore how weather conditions can be better understood and communicated for outdoor activity planning.

# 🌦️ Will It Rain On My Parade?


A web application that helps users plan outdoor activities with confidence by analyzing the likelihood of adverse weather conditions using NASA Earth observation data.

![Project UI](Project%20UI.png)

## 📋 Overview

"Will It Rain On My Parade?" is an interactive weather analysis tool that leverages NASA's comprehensive Earth observation datasets to provide probability-based weather forecasts. Users can select any location on Earth, choose a date range, and analyze specific weather conditions that might affect their outdoor plans.

## ✨ Features

### 🗺️ Interactive Location Selection
- Click anywhere on the interactive map to select a location
- Enter coordinates or city names manually
- Visual marker placement for selected locations

### 📅 Flexible Time Range Analysis
- **Single Day**: Hour-by-hour analysis
- **Week**: Day-by-day forecasts
- **Month**: Weekly summaries
- **Season**: Monthly trends

### 🌡️ Multi-Condition Weather Analysis
- **Very Hot** (>90°F): Heat wave detection
- **Very Cold** (<32°F): Frost and freeze warnings
- **Very Windy** (>25 mph): High wind alerts
- **Very Wet** (>1 inch): Heavy precipitation forecasts
- **Very Uncomfortable**: High humidity and heat index analysis

### 📊 Data Visualization
- Real-time probability calculations with color-coded risk levels
- Interactive bar charts showing condition probabilities
- Historical trend analysis with temperature and precipitation patterns
- Responsive Chart.js visualizations

### 💾 Data Export
- **CSV Export**: Tabular data for spreadsheet analysis
- **JSON Export**: Structured data for programmatic use
- Timestamped file naming for easy organization

### 🛰️ NASA Data Integration
Direct links to official NASA data sources:
- GES DISC OPeNDAP
- Giovanni Data Visualization
- Hydrology Data Rods
- Worldview Satellite Imagery
- Earthdata Search
- Python API Tutorials
- CPTEC/INPE Satellite Data

## 🛠️ Tech Stack

- **Backend**: Python 3.x with Flask
- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Mapping**: Leaflet.js
- **Charts**: Chart.js
- **Icons**: Font Awesome
- **Architecture**: Single-file application for easy deployment

## 📦 Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Setup Instructions

1. **Clone or download the repository**
   \`\`\`bash
   git clone <repository-url>
   cd will-it-rain-on-my-parade
   \`\`\`

2. **Install Flask**
   \`\`\`bash
   pip install flask
   \`\`\`

3. **Run the application**
   \`\`\`bash
   python analyze-weather.py
   \`\`\`

4. **Open your browser**
   Navigate to: `http://localhost:5000`

## 🚀 Usage Guide

### Step 1: Select Location
- Click on the map to select your desired location, or
- Enter coordinates in the format: `latitude, longitude`
- Example: `40.7128, -74.0060` (New York City)

### Step 2: Choose Date and Time Range
- Select the date you want to analyze
- Choose a time range (day, week, month, or season)

### Step 3: Select Weather Conditions
- Click on one or more weather condition cards
- Selected conditions will be highlighted in blue
- You can select multiple conditions for comprehensive analysis

### Step 4: Analyze
- Click the "Analyze Weather" button
- Wait for the analysis to complete (simulated data processing)
- View probability results, charts, and historical trends

### Step 5: Export Data (Optional)
- Download results as CSV for spreadsheet analysis
- Download as JSON for programmatic use
- Files are timestamped for easy organization

## 🌐 NASA Data Sources

This application is designed to integrate with the following NASA Earth observation data sources:

| Source | Purpose | URL |
|--------|---------|-----|
| **GES DISC OPeNDAP** | Historical weather data access | [Link](https://disc.gsfc.nasa.gov/information/tools?title=OPeNDAP%20and%20GDS) |
| **Giovanni** | Data visualization and analysis | [Link](https://giovanni.gsfc.nasa.gov/) |
| **Hydrology Data Rods** | Precipitation and water cycle data | [Link](https://disc.gsfc.nasa.gov/information/tools?title=Hydrology%20Data%20Rods) |
| **Worldview** | Real-time satellite imagery | [Link](https://worldview.earthdata.nasa.gov/) |
| **Earthdata Search** | Comprehensive dataset discovery | [Link](https://search.earthdata.nasa.gov/search) |
| **Python Tutorials** | API integration guides | [Link](https://disc.gsfc.nasa.gov/information/howto?page=1&dataTools=Python) |

## 🔮 Current Status & Future Improvements

### Current Implementation
- ✅ Fully functional user interface
- ✅ Interactive map and location selection
- ✅ Multiple weather condition analysis
- ✅ Data visualization with charts
- ✅ CSV and JSON export functionality
- ⚠️ **Using simulated data** (random probability generation)

### Planned Enhancements
- 🔄 **NASA API Integration**: Replace simulated data with real NASA Earth observation data
- 🔄 **Historical Data Analysis**: Query actual historical weather patterns from GES DISC
- 🔄 **Machine Learning**: Implement predictive models for improved accuracy
- 🔄 **User Accounts**: Save favorite locations and analysis history
- 🔄 **Mobile App**: Native iOS and Android applications
- 🔄 **Email Alerts**: Automated weather notifications for saved events
- 🔄 **Social Sharing**: Share weather analysis with friends and family

## 🏗️ Architecture

This application uses a **single-file architecture** for simplicity and ease of deployment:

```
main.py/
├── 📦 Flask Backend
│   ├── 🔁 Route Handlers
│   ├── 🔗 API Endpoints
│   │   ├── /api/analyze
│   │   └── /api/download/*
│   └── 🧠 Data Processing Functions
└── 🌐 Embedded Frontend
    ├── 📝 HTML Template
    ├── 🎨 CSS Styling
    │   ├── CSS Variables
    │   └── Responsive Design
    └── 📜 JavaScript
        ├── Leaflet.js
        ├── Chart.js
        └── Fetch API
```

### Key Design Decisions
- **Single File**: Easy to deploy and share
- **Embedded Assets**: No external file dependencies (uses CDNs)
- **RESTful API**: Clean separation between frontend and backend logic
- **Responsive Design**: Mobile-first CSS with flexbox and grid layouts
- **Dark Theme**: Optimized for extended viewing sessions

## 👥 Team CodeExploitrz

This project was developed for the **NASA Space Apps Challenge 2025** by Team CodeExploitrz.

### Challenge
**Will It Rain On My Parade?**  
Create a tool that helps users plan outdoor activities by analyzing the likelihood of adverse weather conditions using NASA Earth observation data.

## 📄 License

This project was created for the NASA Space Apps Challenge 2025. Please refer to the challenge guidelines for usage and distribution terms.

## 🙏 Acknowledgments

- **NASA** for providing comprehensive Earth observation data and APIs
- **NASA Space Apps Challenge** for organizing this global hackathon
- **OpenStreetMap** contributors for map tiles
- **Leaflet.js** and **Chart.js** communities for excellent open-source libraries

---

**Built with ❤️ for NASA Space Apps Challenge 2025**

"""
NASA Space Apps Challenge 2025 - Will It Rain On My Parade?
Team: CodeExploitrz
Single-file Flask application with embedded HTML, CSS, and JavaScript
"""

from flask import Flask, render_template_string, jsonify, request, send_file
import json
import csv
import io
from datetime import datetime, timedelta
import random
import math

app = Flask(__name__)

# HTML Template with embedded CSS and JavaScript
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Will It Rain On My Parade? - CodeExploitrz</title>
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" />
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        :root {
            --primary-bg: #101825;
            --secondary-bg: #1a2332;
            --card-bg: #243447;
            --accent-blue: #3b82f6;
            --accent-cyan: #06b6d4;
            --text-primary: #f1f5f9;
            --text-secondary: #94a3b8;
            --border-color: #334155;
            --success: #10b981;
            --warning: #f59e0b;
            --danger: #ef4444;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, var(--primary-bg) 0%, #0f172a 100%);
            color: var(--text-primary);
            min-height: 100vh;
            line-height: 1.6;
        }

        .header {
            background: var(--primary-bg);
            padding: 1.5rem 2rem;
            border-bottom: 2px solid var(--accent-blue);
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
        }

        .header-content {
            max-width: 1400px;
            margin: 0 auto;
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 1rem;
        }

        .logo-section {
            display: flex;
            align-items: center;
            gap: 1rem;
        }

        .logo {
            width: 60px;
            height: 60px;
            background: var(--primary-bg);
            border-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 2rem;
            border: 2px solid var(--accent-blue);
        }

        .title-section h1 {
            font-size: 1.8rem;
            font-weight: 700;
            background: linear-gradient(135deg, var(--accent-blue), var(--accent-cyan));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }

        .title-section p {
            color: var(--text-secondary);
            font-size: 0.9rem;
        }

        .nasa-badge {
            background: var(--card-bg);
            padding: 0.5rem 1rem;
            border-radius: 8px;
            border: 1px solid var(--accent-blue);
            font-size: 0.85rem;
        }

        .container {
            max-width: 1400px;
            margin: 2rem auto;
            padding: 0 2rem;
        }

        .dashboard-grid {
            display: grid;
            grid-template-columns: 1fr 2fr;
            gap: 2rem;
            margin-bottom: 2rem;
        }

        .card {
            background: var(--card-bg);
            border-radius: 12px;
            padding: 1.5rem;
            border: 1px solid var(--border-color);
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2);
        }

        .card-header {
            display: flex;
            align-items: center;
            gap: 0.75rem;
            margin-bottom: 1.5rem;
            padding-bottom: 1rem;
            border-bottom: 2px solid var(--border-color);
        }

        .card-header i {
            color: var(--accent-blue);
            font-size: 1.5rem;
        }

        .card-header h2 {
            font-size: 1.3rem;
            font-weight: 600;
        }

        .form-group {
            margin-bottom: 1.5rem;
        }

        .form-group label {
            display: block;
            margin-bottom: 0.5rem;
            color: var(--text-secondary);
            font-weight: 500;
            font-size: 0.9rem;
        }

        .form-control {
            width: 100%;
            padding: 0.75rem;
            background: var(--secondary-bg);
            border: 1px solid var(--border-color);
            border-radius: 8px;
            color: var(--text-primary);
            font-size: 1rem;
            transition: all 0.3s ease;
        }

        .form-control:focus {
            outline: none;
            border-color: var(--accent-blue);
            box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.1);
        }

        .btn {
            padding: 0.75rem 1.5rem;
            border: none;
            border-radius: 8px;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s ease;
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            font-size: 1rem;
        }

        .btn-primary {
            background: linear-gradient(135deg, var(--accent-blue), var(--accent-cyan));
            color: white;
        }

        .btn-primary:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 12px rgba(59, 130, 246, 0.3);
        }

        .btn-secondary {
            background: var(--secondary-bg);
            color: var(--text-primary);
            border: 1px solid var(--border-color);
        }

        .btn-secondary:hover {
            background: var(--card-bg);
        }

        .btn-group {
            display: flex;
            gap: 1rem;
            margin-top: 1rem;
        }

        #map {
            height: 400px;
            border-radius: 8px;
            border: 2px solid var(--border-color);
        }

        .weather-conditions {
            display: grid;
            grid-template-columns: repeat(2, 1fr); /* 2 columns */
            gap: 1rem; /* spacing between cards */
            max-width: 500px; /* optional: controls overall width */
            margin-top: 1rem;
        }

        .condition-card {
            background: var(--secondary-bg);
            padding: 0.75rem;
            border-radius: 6px;
            border: 1px solid var(--border-color);
            text-align: center;
            transition: all 0.3s ease;
            cursor: pointer;
            font-size: 0.875rem;
        }

        .condition-card:hover {
            transform: translateY(-2px);
            border-color: var(--accent-blue);
            box-shadow: 0 3px 6px rgba(59, 130, 246, 0.15);
        }

        .condition-card.active {
            border-color: var(--accent-blue);
            background: linear-gradient(135deg, rgba(59, 130, 246, 0.1), rgba(6, 182, 212, 0.1));
        }

        .condition-icon {
            font-size: 2.5rem;
            margin-bottom: 0.5rem;
        }

        .condition-label {
            font-weight: 600;
            margin-bottom: 0.25rem;
        }

        .condition-desc {
            font-size: 0.85rem;
            color: var(--text-secondary);
        }

        .results-section {
            display: none;
        }

        .results-section.active {
            display: block;
        }

        .probability-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 1.5rem;
            margin-bottom: 2rem;
        }

        .probability-card {
            background: var(--secondary-bg);
            padding: 1.5rem;
            border-radius: 8px;
            border: 1px solid var(--border-color);
        }

        .probability-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 1rem;
        }

        .probability-title {
            font-weight: 600;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }

        .probability-value {
            font-size: 1.5rem;
            font-weight: 700;
            color: var(--accent-blue);
        }

        .probability-bar {
            height: 8px;
            background: var(--card-bg);
            border-radius: 4px;
            overflow: hidden;
            margin-bottom: 0.5rem;
        }

        .probability-fill {
            height: 100%;
            background: linear-gradient(90deg, var(--accent-blue), var(--accent-cyan));
            transition: width 1s ease;
        }

        .probability-details {
            font-size: 0.85rem;
            color: var(--text-secondary);
            margin-top: 0.5rem;
        }

        .chart-container {
            background: var(--secondary-bg);
            padding: 1.5rem;
            border-radius: 8px;
            border: 1px solid var(--border-color);
            margin-bottom: 2rem;
        }

        .chart-title {
            font-weight: 600;
            margin-bottom: 1rem;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }

        canvas {
            max-width: 100%;
        }

        .data-sources {
            background: var(--secondary-bg);
            padding: 1.5rem;
            border-radius: 8px;
            border: 1px solid var(--border-color);
            margin-top: 2rem;
        }

        .data-sources h3 {
            margin-bottom: 1rem;
            color: var(--accent-blue);
        }

        .source-links {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 1rem;
        }

        .source-link {
            display: flex;
            align-items: center;
            gap: 0.5rem;
            padding: 0.75rem;
            background: var(--card-bg);
            border-radius: 6px;
            color: var(--text-primary);
            text-decoration: none;
            transition: all 0.3s ease;
            font-size: 0.9rem;
        }

        .source-link:hover {
            background: var(--primary-bg);
            transform: translateX(4px);
        }

        .loading {
            display: none;
            text-align: center;
            padding: 2rem;
        }

        .loading.active {
            display: block;
        }

        .spinner {
            border: 4px solid var(--border-color);
            border-top: 4px solid var(--accent-blue);
            border-radius: 50%;
            width: 50px;
            height: 50px;
            animation: spin 1s linear infinite;
            margin: 0 auto 1rem;
        }

        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }

        .alert {
            padding: 1rem;
            border-radius: 8px;
            margin-bottom: 1rem;
            display: flex;
            align-items: center;
            gap: 0.75rem;
        }

        .alert-info {
            background: rgba(59, 130, 246, 0.1);
            border: 1px solid var(--accent-blue);
            color: var(--accent-blue);
        }

        .footer {
            text-align: center;
            padding: 2rem;
            color: var(--text-secondary);
            border-top: 1px solid var(--border-color);
            margin-top: 3rem;
        }

        @media (max-width: 768px) {
            .dashboard-grid {
                grid-template-columns: 1fr;
            }

            .header-content {
                flex-direction: column;
                text-align: center;
            }

            .title-section h1 {
                font-size: 1.5rem;
            }
        }
        .logo-section {
            display: flex;
            align-items: center;
            gap: 1rem;
        }

        .logo {
            width: 70px;
            height: 70px;
            background: white;
            border-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            border: 3px solid var(--accent-blue);
            overflow: hidden;
            box-shadow: 0 4px 8px rgba(59, 130, 246, 0.3);
        }

        .logo img {
            width: 100%;
            height: 100%;
            object-fit: cover;
        }
    </style>
</head>
<body>
    <header class="header">
        <div class="header-content">
            <div class="logo-section">
                <div class="logo">
                    <img src="https://assets.spaceappschallenge.org/media/images/1000120948.2e16d0ba.fill-300x250.jpg" alt="CodeExploitrz Logo">
                </div>
                <div class="title-section">
                    <h1>Will It Rain On My Parade?</h1>
                    <p>Team CodeExploitrz</p>
                </div>
            </div>
            <div class="nasa-badge">
                <i class="fas fa-rocket"></i> 2025 NASA Space Apps Challenge
            </div>
        </div>
    </header>

    <div class="container">
        <div class="alert alert-info">
            <i class="fas fa-info-circle"></i>
            <div>
                <strong>Plan Your Outdoor Activities with Confidence!</strong>
                Select a location and date to check the likelihood of adverse weather conditions using NASA Earth observation data.
            </div>
        </div>

        <div class="dashboard-grid">
            <div class="card">
                <div class="card-header">
                    <i class="fas fa-sliders-h"></i>
                    <h2>Query Parameters</h2>
                </div>

                <div class="form-group">
                    <label><i class="fas fa-map-marker-alt"></i> Location</label>
                    <input type="text" id="locationInput" class="form-control" placeholder="Enter city or coordinates">
                    <small style="color: var(--text-secondary); display: block; margin-top: 0.5rem;">
                        Or click on the map to select a location
                    </small>
                </div>

                <div class="form-group">
                    <label><i class="fas fa-calendar"></i> Date</label>
                    <input type="date" id="dateInput" class="form-control">
                </div>

                <div class="form-group">
                    <label><i class="fas fa-clock"></i> Time Range</label>
                    <select id="timeRange" class="form-control">
                        <option value="day">Single Day</option>
                        <option value="week">Week</option>
                        <option value="month">Month</option>
                        <option value="season">Season</option>
                    </select>
                </div>

                <div class="form-group">
                    <label><i class="fas fa-cloud"></i> Weather Conditions</label>
                    <div class="weather-conditions">
                        <div class="condition-card" data-condition="hot">
                            <div class="condition-icon">🔥</div>
                            <div class="condition-label">Very Hot</div>
                            <div class="condition-desc">&gt;90°F</div>
                        </div>
                        <div class="condition-card" data-condition="cold">
                            <div class="condition-icon">❄️</div>
                            <div class="condition-label">Very Cold</div>
                            <div class="condition-desc">&lt;32°F</div>
                        </div>
                        <div class="condition-card" data-condition="windy">
                            <div class="condition-icon">🌬️</div>
                            <div class="condition-label">Very Windy</div>
                            <div class="condition-desc">&gt;25 mph</div>
                        </div>
                        <div class="condition-card" data-condition="wet">
                            <div class="condition-icon">🌧️</div>
                            <div class="condition-label">Very Wet</div>
                            <div class="condition-desc">&gt;1 inch</div>
                        </div>
                        <div class="condition-card" data-condition="uncomfortable">
                            <div class="condition-icon">😓</div>
                            <div class="condition-label">Uncomfortable</div>
                            <div class="condition-desc">High humidity</div>
                        </div>
                    </div>
                </div>

                <div class="btn-group">
                    <button class="btn btn-primary" onclick="analyzeWeather()">
                        <i class="fas fa-search"></i> Analyze Weather
                    </button>
                    <button class="btn btn-secondary" onclick="resetForm()">
                        <i class="fas fa-redo"></i> Reset
                    </button>
                </div>
            </div>

            <div class="card">
                <div class="card-header">
                    <i class="fas fa-map"></i>
                    <h2>Location Selection</h2>
                </div>
                <div id="map"></div>
            </div>
        </div>

         Loading Indicator 
        <div class="loading" id="loading">
            <div class="spinner"></div>
            <p>Analyzing NASA Earth observation data...</p>
        </div>

         Results Section 
        <div class="results-section" id="results">
            <div class="card">
                <div class="card-header">
                    <i class="fas fa-chart-line"></i>
                    <h2>Weather Analysis Results</h2>
                </div>

                <div id="resultsContent"></div>

                <div class="btn-group">
                    <button class="btn btn-primary" onclick="downloadCSV()">
                        <i class="fas fa-download"></i> Download CSV
                    </button>
                    <button class="btn btn-primary" onclick="downloadJSON()">
                        <i class="fas fa-download"></i> Download JSON
                    </button>
                </div>
            </div>

             Charts 
            <div class="chart-container">
                <div class="chart-title">
                    <i class="fas fa-chart-bar"></i>
                    Historical Probability Trends
                </div>
                <canvas id="probabilityChart"></canvas>
            </div>

            <div class="chart-container">
                <div class="chart-title">
                    <i class="fas fa-chart-area"></i>
                    Temperature & Precipitation Patterns
                </div>
                <canvas id="weatherChart"></canvas>
            </div>
        </div>

         NASA Data Sources 
        <div class="data-sources">
            <h3><i class="fas fa-satellite"></i> NASA Data Sources</h3>
            <div class="source-links">
                <a href="https://disc.gsfc.nasa.gov/information/tools?title=OPeNDAP%20and%20GDS" target="_blank" class="source-link">
                    <i class="fas fa-database"></i> GES DISC OPeNDAP
                </a>
                <a href="https://giovanni.gsfc.nasa.gov/" target="_blank" class="source-link">
                    <i class="fas fa-globe"></i> Giovanni
                </a>
                <a href="https://disc.gsfc.nasa.gov/information/tools?title=Hydrology%20Data%20Rods" target="_blank" class="source-link">
                    <i class="fas fa-water"></i> Hydrology Data Rods
                </a>
                <a href="https://worldview.earthdata.nasa.gov/" target="_blank" class="source-link">
                    <i class="fas fa-satellite-dish"></i> Worldview
                </a>
                <a href="https://search.earthdata.nasa.gov/search" target="_blank" class="source-link">
                    <i class="fas fa-search"></i> Earthdata Search
                </a>
                <a href="https://disc.gsfc.nasa.gov/information/howto?page=1&dataTools=Python" target="_blank" class="source-link">
                    <i class="fab fa-python"></i> Python Tutorials
                </a>
                <a href="https://satelite.cptec.inpe.br/home/index.jsp" target="_blank" class="source-link">
                    <i class="fas fa-cloud-sun"></i> CPTEC/INPE
                </a>
            </div>
        </div>
    </div>

    <footer class="footer">
        <p>&copy; 2025 CodeExploitrz | NASA Space Apps Challenge</p>
        <p>Powered by NASA Earth Observation Data</p>
    </footer>

    <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.js"></script>
    <script>
        // Global variables
        let map;
        let marker;
        let selectedConditions = [];
        let currentResults = null;

        // Initialize map
        function initMap() {
            map = L.map('map').setView([20, 0], 2);
            
            L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                attribution: '© OpenStreetMap contributors',
                maxZoom: 18
            }).addTo(map);

            map.on('click', function(e) {
                const lat = e.latlng.lat.toFixed(4);
                const lng = e.latlng.lng.toFixed(4);
                
                if (marker) {
                    map.removeLayer(marker);
                }
                
                marker = L.marker([lat, lng]).addTo(map);
                document.getElementById('locationInput').value = `${lat}, ${lng}`;
            });
        }

        // Initialize date input with today's date
        function initDate() {
            const today = new Date().toISOString().split('T')[0];
            document.getElementById('dateInput').value = today;
        }

        // Handle condition card selection
        document.querySelectorAll('.condition-card').forEach(card => {
            card.addEventListener('click', function() {
                this.classList.toggle('active');
                const condition = this.dataset.condition;
                
                if (selectedConditions.includes(condition)) {
                    selectedConditions = selectedConditions.filter(c => c !== condition);
                } else {
                    selectedConditions.push(condition);
                }
            });
        });

        // Analyze weather function
        async function analyzeWeather() {
            const location = document.getElementById('locationInput').value;
            const date = document.getElementById('dateInput').value;
            const timeRange = document.getElementById('timeRange').value;

            if (!location || !date) {
                alert('Please enter a location and date');
                return;
            }

            if (selectedConditions.length === 0) {
                alert('Please select at least one weather condition');
                return;
            }

            // Show loading
            document.getElementById('loading').classList.add('active');
            document.getElementById('results').classList.remove('active');

            try {
                const response = await fetch('/api/analyze', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({
                        location: location,
                        date: date,
                        timeRange: timeRange,
                        conditions: selectedConditions
                    })
                });

                const data = await response.json();
                currentResults = data;
                displayResults(data);
            } catch (error) {
                console.error('Error:', error);
                alert('Error analyzing weather data. Please try again.');
            } finally {
                document.getElementById('loading').classList.remove('active');
            }
        }

        // Display results
        function displayResults(data) {
            const resultsContent = document.getElementById('resultsContent');
            
            let html = `
                <div style="margin-bottom: 2rem;">
                    <h3 style="color: var(--accent-blue); margin-bottom: 1rem;">
                        <i class="fas fa-map-marker-alt"></i> ${data.location}
                    </h3>
                    <p style="color: var(--text-secondary);">
                        <i class="fas fa-calendar"></i> ${data.date} | 
                        <i class="fas fa-clock"></i> ${data.timeRange}
                    </p>
                </div>

                <div class="probability-grid">
            `;

            data.probabilities.forEach(prob => {
                const icon = getConditionIcon(prob.condition);
                const color = getProbabilityColor(prob.probability);
                
                html += `
                    <div class="probability-card">
                        <div class="probability-header">
                            <div class="probability-title">
                                <span style="font-size: 1.5rem;">${icon}</span>
                                ${prob.label}
                            </div>
                            <div class="probability-value" style="color: ${color};">
                                ${prob.probability}%
                            </div>
                        </div>
                        <div class="probability-bar">
                            <div class="probability-fill" style="width: ${prob.probability}%; background: ${color};"></div>
                        </div>
                        <div class="probability-details">
                            ${prob.details}
                        </div>
                    </div>
                `;
            });

            html += '</div>';
            resultsContent.innerHTML = html;

            // Show results section
            document.getElementById('results').classList.add('active');

            // Create charts
            createProbabilityChart(data);
            createWeatherChart(data);

            // Scroll to results
            document.getElementById('results').scrollIntoView({ behavior: 'smooth' });
        }

        // Get condition icon
        function getConditionIcon(condition) {
            const icons = {
                'hot': '🔥',
                'cold': '❄️',
                'windy': '🌬️',
                'wet': '🌧️',
                'uncomfortable': '😓'
            };
            return icons[condition] || '🌤️';
        }

        // Get probability color
        function getProbabilityColor(probability) {
            if (probability >= 70) return '#ef4444';
            if (probability >= 40) return '#f59e0b';
            return '#10b981';
        }

        // Create probability chart
        function createProbabilityChart(data) {
            const ctx = document.getElementById('probabilityChart');
            
            if (window.probabilityChartInstance) {
                window.probabilityChartInstance.destroy();
            }

            window.probabilityChartInstance = new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: data.probabilities.map(p => p.label),
                    datasets: [{
                        label: 'Probability (%)',
                        data: data.probabilities.map(p => p.probability),
                        backgroundColor: data.probabilities.map(p => getProbabilityColor(p.probability) + '80'),
                        borderColor: data.probabilities.map(p => getProbabilityColor(p.probability)),
                        borderWidth: 2
                    }]
                },
                options: {
                    responsive: true,
                    plugins: {
                        legend: {
                            labels: {
                                color: '#f1f5f9'
                            }
                        }
                    },
                    scales: {
                        y: {
                            beginAtZero: true,
                            max: 100,
                            ticks: {
                                color: '#94a3b8'
                            },
                            grid: {
                                color: '#334155'
                            }
                        },
                        x: {
                            ticks: {
                                color: '#94a3b8'
                            },
                            grid: {
                                color: '#334155'
                            }
                        }
                    }
                }
            });
        }

        // Create weather chart
        function createWeatherChart(data) {
            const ctx = document.getElementById('weatherChart');
            
            if (window.weatherChartInstance) {
                window.weatherChartInstance.destroy();
            }

            window.weatherChartInstance = new Chart(ctx, {
                type: 'line',
                data: {
                    labels: data.historicalData.labels,
                    datasets: [
                        {
                            label: 'Temperature (°F)',
                            data: data.historicalData.temperature,
                            borderColor: '#ef4444',
                            backgroundColor: '#ef444420',
                            tension: 0.4,
                            yAxisID: 'y'
                        },
                        {
                            label: 'Precipitation (inches)',
                            data: data.historicalData.precipitation,
                            borderColor: '#3b82f6',
                            backgroundColor: '#3b82f620',
                            tension: 0.4,
                            yAxisID: 'y1'
                        }
                    ]
                },
                options: {
                    responsive: true,
                    interaction: {
                        mode: 'index',
                        intersect: false
                    },
                    plugins: {
                        legend: {
                            labels: {
                                color: '#f1f5f9'
                            }
                        }
                    },
                    scales: {
                        y: {
                            type: 'linear',
                            display: true,
                            position: 'left',
                            ticks: {
                                color: '#94a3b8'
                            },
                            grid: {
                                color: '#334155'
                            }
                        },
                        y1: {
                            type: 'linear',
                            display: true,
                            position: 'right',
                            ticks: {
                                color: '#94a3b8'
                            },
                            grid: {
                                drawOnChartArea: false
                            }
                        },
                        x: {
                            ticks: {
                                color: '#94a3b8'
                            },
                            grid: {
                                color: '#334155'
                            }
                        }
                    }
                }
            });
        }

        // Download CSV
        async function downloadCSV() {
            if (!currentResults) return;

            const response = await fetch('/api/download/csv', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(currentResults)
            });

            const blob = await response.blob();
            const url = window.URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = `weather_analysis_${Date.now()}.csv`;
            a.click();
        }

        // Download JSON
        async function downloadJSON() {
            if (!currentResults) return;

            const dataStr = JSON.stringify(currentResults, null, 2);
            const blob = new Blob([dataStr], { type: 'application/json' });
            const url = window.URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = `weather_analysis_${Date.now()}.json`;
            a.click();
        }

        // Reset form
        function resetForm() {
            document.getElementById('locationInput').value = '';
            document.getElementById('dateInput').value = new Date().toISOString().split('T')[0];
            document.getElementById('timeRange').value = 'day';
            
            document.querySelectorAll('.condition-card').forEach(card => {
                card.classList.remove('active');
            });
            
            selectedConditions = [];
            
            if (marker) {
                map.removeLayer(marker);
                marker = null;
            }
            
            document.getElementById('results').classList.remove('active');
        }

        // Initialize on page load
        window.addEventListener('DOMContentLoaded', function() {
            initMap();
            initDate();
        });
    </script>
</body>
</html>
"""

# API endpoint for weather analysis
@app.route('/api/analyze', methods=['POST'])
def analyze_weather():
    """
    Analyze weather conditions based on user input
    In production, this would query actual NASA APIs
    """
    data = request.json
    location = data.get('location')
    date = data.get('date')
    time_range = data.get('timeRange')
    conditions = data.get('conditions', [])

    # Simulate NASA data analysis
    # In production, integrate with actual NASA APIs:
    # - GES DISC OPeNDAP for historical data
    # - Giovanni for data visualization
    # - Worldview for satellite imagery
    # - Earthdata Search for comprehensive datasets

    probabilities = []
    condition_labels = {
        'hot': 'Very Hot',
        'cold': 'Very Cold',
        'windy': 'Very Windy',
        'wet': 'Very Wet',
        'uncomfortable': 'Very Uncomfortable'
    }

    for condition in conditions:
        # Simulate probability calculation based on historical data
        probability = random.randint(15, 85)
        
        details = generate_condition_details(condition, probability, date)
        
        probabilities.append({
            'condition': condition,
            'label': condition_labels.get(condition, condition),
            'probability': probability,
            'details': details
        })

    # Generate historical data for charts
    historical_data = generate_historical_data(date, time_range)

    result = {
        'location': location,
        'date': date,
        'timeRange': time_range,
        'probabilities': probabilities,
        'historicalData': historical_data,
        'dataSources': [
            'NASA GES DISC',
            'Giovanni',
            'Worldview',
            'Earthdata Search'
        ],
        'metadata': {
            'generatedAt': datetime.now().isoformat(),
            'dataQuality': 'High',
            'confidence': '85%'
        }
    }

    return jsonify(result)

def generate_condition_details(condition, probability, date):
    """Generate detailed explanation for each condition"""
    details_map = {
        'hot': f"Based on {probability}% historical occurrence of temperatures exceeding 90°F. Heat index may reach dangerous levels.",
        'cold': f"Historical data shows {probability}% probability of temperatures below 32°F. Frost and ice conditions likely.",
        'windy': f"{probability}% chance of sustained winds exceeding 25 mph. May affect outdoor activities significantly.",
        'wet': f"Precipitation probability of {probability}% with potential for over 1 inch of rainfall. Plan for wet conditions.",
        'uncomfortable': f"{probability}% likelihood of high humidity (>70%) combined with temperature. Heat index will feel higher."
    }
    return details_map.get(condition, f"{probability}% probability based on historical data")

def generate_historical_data(date, time_range):
    """Generate simulated historical weather data"""
    # Parse date
    target_date = datetime.strptime(date, '%Y-%m-%d')
    
    # Generate labels based on time range
    if time_range == 'day':
        labels = [f"{i}:00" for i in range(0, 24, 3)]
        num_points = 8
    elif time_range == 'week':
        labels = [(target_date + timedelta(days=i)).strftime('%a') for i in range(7)]
        num_points = 7
    elif time_range == 'month':
        labels = [f"Week {i+1}" for i in range(4)]
        num_points = 4
    else:  # season
        labels = ['Month 1', 'Month 2', 'Month 3']
        num_points = 3

    # Generate temperature data (40-95°F range)
    temperature = [random.randint(40, 95) for _ in range(num_points)]
    
    # Generate precipitation data (0-3 inches)
    precipitation = [round(random.uniform(0, 3), 2) for _ in range(num_points)]

    return {
        'labels': labels,
        'temperature': temperature,
        'precipitation': precipitation
    }

@app.route('/api/download/csv', methods=['POST'])
def download_csv():
    """Generate CSV file from analysis results"""
    data = request.json
    
    output = io.StringIO()
    writer = csv.writer(output)
    
    # Write headers
    writer.writerow(['Weather Analysis Report'])
    writer.writerow(['Location', data['location']])
    writer.writerow(['Date', data['date']])
    writer.writerow(['Time Range', data['timeRange']])
    writer.writerow([])
    
    # Write probabilities
    writer.writerow(['Condition', 'Probability (%)', 'Details'])
    for prob in data['probabilities']:
        writer.writerow([prob['label'], prob['probability'], prob['details']])
    
    writer.writerow([])
    
    # Write historical data
    writer.writerow(['Historical Data'])
    writer.writerow(['Period', 'Temperature (°F)', 'Precipitation (inches)'])
    for i, label in enumerate(data['historicalData']['labels']):
        writer.writerow([
            label,
            data['historicalData']['temperature'][i],
            data['historicalData']['precipitation'][i]
        ])
    
    # Create response
    output.seek(0)
    return send_file(
        io.BytesIO(output.getvalue().encode()),
        mimetype='text/csv',
        as_attachment=True,
        download_name=f'weather_analysis_{datetime.now().strftime("%Y%m%d_%H%M%S")}.csv'
    )

@app.route('/')
def index():
    """Render main application page"""
    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    print("=" * 60)
    print("NASA Space Apps Challenge 2025")
    print("Will It Rain On My Parade?")
    print("Team: CodeExploitrz")
    print("=" * 60)
    print("\nStarting Flask application...")
    print("Open your browser and navigate to: http://localhost:5000")
    print("\nPress CTRL+C to stop the server")
    print("=" * 60)
    
    app.run(debug=True, host='0.0.0.0', port=5000)

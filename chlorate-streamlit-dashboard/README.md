# Chlorate Streamlit Dashboard

## Overview
The Chlorate Streamlit Dashboard is a web application designed to model and visualize the concentrations of sodium hypochlorite and chlorate in water. It allows users to input various parameters and see the effects on chemical concentrations over time.

## Project Structure
```
chlorate-streamlit-dashboard
├── src
│   ├── streamlit_app.py          # Main entry point for the Streamlit application
│   ├── model.py                  # Contains the original model code for calculations
│   ├── calculations.py           # Helper functions for calculations
│   ├── components
│   │   ├── charts.py             # Functions to create visualizations
│   │   └── inputs.py             # Functions to create input components
│   └── data
│       └── sample_inputs.json     # Sample input data in JSON format
├── requirements.txt               # Lists project dependencies
├── .streamlit
│   └── config.toml               # Configuration settings for the Streamlit app
├── tests
│   └── test_calculations.py      # Unit tests for calculations
└── README.md                     # Documentation for the project
```

## Installation
To set up the project, follow these steps:

1. Clone the repository:
   ```
   git clone <repository-url>
   cd chlorate-streamlit-dashboard
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage
To run the Streamlit application, execute the following command in your terminal:
```
streamlit run src/streamlit_app.py
```

Once the application is running, you can adjust the input parameters using the interactive sliders and view the resulting charts for hypochlorite and chlorate concentrations.

## Features
- Interactive input sliders for:
  - Initial sodium hypochlorite strength (%w/w)
  - Initial chlorate concentration (g/L)
  - Chlorine dose (mg/L)
  - Pump capacity (L/hr)
  - Water flow rate (MLD)
  - Storage temperature (°C)
- Real-time calculations of:
  - Remaining hypochlorite concentration
  - Chlorate concentration in the chemical product and water stream
- Visualizations of concentration changes over time

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
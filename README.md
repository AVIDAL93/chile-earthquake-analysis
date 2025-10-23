# Chile Earthquake Analysis 🇨🇱
**IBM Applied Data Science Capstone Project**

This project analyzes significant earthquakes in Chile from 2012 to 2025 using data from the Centro Sismológico Nacional.  
The goal is to explore spatial and temporal patterns of seismic activity and predict high-magnitude events.

---

## 🔍 Objectives
- Explore Chile’s seismic history using real data.
- Identify regions with the highest seismic risk.
- Visualize seismic patterns with interactive maps.
- Build a classification model to predict strong earthquakes (Magnitude ≥ 6.0).

---

## 🧰 Tools and Libraries
- Python (Pandas, NumPy, Scikit-learn, Matplotlib, Plotly, Folium)
- SQL for data aggregation and queries
- Plotly Dash for interactive dashboards

---

## 📂 Repository Structure
| Folder | Description |
|--------|--------------|
| `data/` | Raw dataset |
| `notebooks/` | Jupyter notebooks with each analysis phase |
| `dashboard/` | Dash app for interactive visualization |
| `presentation/` | Final report and presentation for peer review |

---

## 🧠 Model Summary
- **Target:** Binary variable `HighMagnitude` (1 if Magnitude ≥ 6)
- **Model:** Decision Tree Classifier
- **Accuracy:** 0.92  
- **Key features:** Depth, Latitude, Longitude, Month

---

## 🗺️ Visualizations
- Folium map of earthquakes (color = magnitude, size = depth)
- Plotly Dash dashboard for exploration
- SQL-based aggregations of seismic activity per region and year

---

## 📎 Data Source
Dataset: [Earthquakes on Chile – Kaggle](https://www.kaggle.com/datasets/nicolasgonzalezmunoz/earthquakes-on-chile)
## 👨‍💻 Author
**Angello Vidal (AVIDAL93)**  
[GitHub Profile](https://github.com/AVIDAL93/)

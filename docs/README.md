# LekunutuAI 

**LekunutuAI** is a sophisticated fraud detection system designed to enhance security in real-time transactions and web activities. Utilizing cutting-edge machine learning techniques, LekunutuAI analyzes user behavior and transaction patterns to identify and mitigate potential fraud risks effectively.

## Project Overview

LekunutuAI integrates various technologies and techniques to offer comprehensive fraud detection and prevention. The system includes real-time monitoring, behavioral analytics, and custom alerts to safeguard against fraudulent activities and ensure secure transactions.

## Current Features

- **Real-Time Transaction Monitoring**: Continuously analyzes transaction data to detect and flag suspicious activities as they occur, preventing fraudulent transactions before they are completed.
- **Behavioral Analytics**: Evaluates user behavior to identify anomalies and potential security threats, adjusting risk scores based on deviations from normal patterns.
- **Custom Alerts**: Generates alerts based on risk scores and behavioral analytics, providing immediate feedback and actions, such as notifying users or security teams about high-risk activities.
- **User Feedback Integration**: Incorporates user feedback to refine and improve the model's accuracy and adapt to evolving threats.
- **Fraud Detection Models**: Employs advanced machine learning models, including ensemble methods and XGBoost, to assess transaction and link risks. Models are designed to balance precision and recall, focusing on precision-based metrics.

## Current State

The transaction fraud detection model is currently being trained and awaits deployment and integration with the browser extension. Progress includes:
- **Model Training:** The model is in the training phase with a focus on achieving high accuracy and robustness.
- **Pending Integration:** Integration with the browser extension is the next step.

## Usage

### 1. Run the Backend Server
Start the FastAPI backend server to enable the fraud detection system:
```bash
uvicorn backend.main:app --reload

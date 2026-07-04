package com.ajith.fake_review_backend.dto;

public class PredictionResponse {

    private String prediction;
    private double confidence;

    public PredictionResponse() {
    }

    public PredictionResponse(String prediction, double confidence) {
        this.prediction = prediction;
        this.confidence = confidence;
    }

    public String getPrediction() {
        return prediction;
    }

    public void setPrediction(String prediction) {
        this.prediction = prediction;
    }

    public double getConfidence() {
        return confidence;
    }

    public void setConfidence(double confidence) {
        this.confidence = confidence;
    }
}
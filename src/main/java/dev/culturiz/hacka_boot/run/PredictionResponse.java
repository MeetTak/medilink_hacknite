package dev.culturiz.hacka_boot.run;

public class PredictionResponse {
    private String predictedDrug;
    private String confidence;
    private String[] topPredictions;

    public PredictionResponse() {
    }

    public PredictionResponse(String predictedDrug, String confidence, String[] topPredictions) {
        this.predictedDrug = predictedDrug;
        this.confidence = confidence;
        this.topPredictions = topPredictions;
    }

    public String getPredictedDrug() {
        return predictedDrug;
    }

    public void setPredictedDrug(String predictedDrug) {
        this.predictedDrug = predictedDrug;
    }

    public String getConfidence() {
        return confidence;
    }

    public void setConfidence(String confidence) {
        this.confidence = confidence;
    }

    public String[] getTopPredictions() {
        return topPredictions;
    }

    public void setTopPredictions(String[] topPredictions) {
        this.topPredictions = topPredictions;
    }
}

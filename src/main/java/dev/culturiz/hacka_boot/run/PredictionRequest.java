package dev.culturiz.hacka_boot.run;

public class PredictionRequest {
    private String sideEffects;

    public PredictionRequest() {
    }

    public PredictionRequest(String sideEffects) {
        this.sideEffects = sideEffects;
    }

    public String getSideEffects() {
        return sideEffects;
    }

    public void setSideEffects(String sideEffects) {
        this.sideEffects = sideEffects;
    }
}

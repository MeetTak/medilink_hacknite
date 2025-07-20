package dev.culturiz.hacka_boot.run;

import org.springframework.web.bind.annotation.*;
import org.springframework.web.client.RestTemplate;
import org.springframework.http.HttpEntity;
import org.springframework.http.HttpHeaders;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;

import java.util.HashMap;
import java.util.Map;

@RestController
@RequestMapping("/api/ai")
@CrossOrigin(origins = "*")
public class AIPredictionController {

    private final RestTemplate restTemplate;
    private static final String PYTHON_API_URL = "http://localhost:8050/predict";

    public AIPredictionController() {
        this.restTemplate = new RestTemplate();
    }

    @PostMapping("/predict")
    public PredictionResponse predictDrug(@RequestBody PredictionRequest request) {
        try {
            // Prepare headers
            HttpHeaders headers = new HttpHeaders();
            headers.setContentType(MediaType.APPLICATION_JSON);

            // Prepare request body for Python API
            Map<String, String> requestBody = new HashMap<>();
            requestBody.put("side_effects", request.getSideEffects());

            HttpEntity<Map<String, String>> entity = new HttpEntity<>(requestBody, headers);

            // Call Python API
            ResponseEntity<Map> response = restTemplate.postForEntity(PYTHON_API_URL, entity, Map.class);
            
            if (response.getBody() != null) {
                String predictedDrug = (String) response.getBody().get("predicted_drug");
                return new PredictionResponse(predictedDrug, "85%", new String[]{predictedDrug});
            } else {
                return new PredictionResponse("No prediction available", "0%", new String[]{});
            }
        } catch (Exception e) {
            // Fallback: Use local database lookup or return error
            return new PredictionResponse("Error: " + e.getMessage(), "0%", new String[]{});
        }
    }

    @PostMapping("/predict-local")
    public PredictionResponse predictDrugLocal(@RequestBody PredictionRequest request) {
        // This is a fallback method that could use your local drug database
        // For now, it returns a simple response
        String sideEffects = request.getSideEffects().toLowerCase();
        
        // Simple keyword-based prediction as fallback
        if (sideEffects.contains("headache") || sideEffects.contains("pain")) {
            return new PredictionResponse("Acetaminophen", "75%", new String[]{"Acetaminophen", "Ibuprofen"});
        } else if (sideEffects.contains("nausea") || sideEffects.contains("stomach")) {
            return new PredictionResponse("Ondansetron", "70%", new String[]{"Ondansetron", "Metoclopramide"});
        } else if (sideEffects.contains("fever")) {
            return new PredictionResponse("Paracetamol", "80%", new String[]{"Paracetamol", "Aspirin"});
        } else {
            return new PredictionResponse("Consult a healthcare provider", "50%", new String[]{"General consultation recommended"});
        }
    }
}

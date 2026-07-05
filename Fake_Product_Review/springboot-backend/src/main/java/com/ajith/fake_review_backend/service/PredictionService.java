package com.ajith.fake_review_backend.service;

import com.ajith.fake_review_backend.dto.PredictionResponse;
import com.ajith.fake_review_backend.dto.ReviewRequest;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpEntity;
import org.springframework.http.HttpHeaders;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

@Service
public class PredictionService {

    @Autowired
    private RestTemplate restTemplate;

    private final String FLASK_API = "https://fake-product-review-detection-1-b77c.onrender.com/predict";

    public PredictionResponse predictReview(ReviewRequest request) {

        HttpHeaders headers = new HttpHeaders();
        headers.setContentType(MediaType.APPLICATION_JSON);

        HttpEntity<ReviewRequest> entity = new HttpEntity<>(request, headers);

        ResponseEntity<PredictionResponse> response =
                restTemplate.postForEntity(
                        FLASK_API,
                        entity,
                        PredictionResponse.class
                );

        return response.getBody();
    }
}

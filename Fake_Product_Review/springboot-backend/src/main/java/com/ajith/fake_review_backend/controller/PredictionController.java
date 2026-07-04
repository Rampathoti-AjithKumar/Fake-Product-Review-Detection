package com.ajith.fake_review_backend.controller;

import com.ajith.fake_review_backend.dto.PredictionResponse;
import com.ajith.fake_review_backend.dto.ReviewRequest;
import com.ajith.fake_review_backend.service.PredictionService;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api")
@CrossOrigin("*")
public class PredictionController {

    @Autowired
    private PredictionService predictionService;

    @PostMapping("/predict")
    public PredictionResponse predict(@RequestBody ReviewRequest request) {
        return predictionService.predictReview(request);
    }
}
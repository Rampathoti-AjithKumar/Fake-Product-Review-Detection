package com.ajith.fake_review_backend.dto;

public class ReviewRequest {

    private String review;

    public ReviewRequest() {
    }

    public ReviewRequest(String review) {
        this.review = review;
    }

    public String getReview() {
        return review;
    }

    public void setReview(String review) {
        this.review = review;
    }
}
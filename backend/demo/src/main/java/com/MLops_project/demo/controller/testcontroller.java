package com.MLops_project.demo.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.reactive.function.client.WebClient;
import reactor.core.publisher.Mono;
import org.springframework.http.HttpHeaders;
import org.springframework.stereotype.Controller;


@Controller
public class testcontroller {

    @GetMapping("/")
    public String home(){
        return "index";
    }

    @Autowired
    private WebClient.Builder webClientBuilder;
    @CrossOrigin(origins = "http://localhost:8080")
    @PostMapping("/predict")
    public Mono<ResponseEntity<String>> predict(@RequestBody String data) {
        String pythonServiceUrl = "http://localhost:5000/predict";

        return webClientBuilder.build()
                .post()
                .uri(pythonServiceUrl)
                .bodyValue(data) 
                .header(HttpHeaders.CONTENT_TYPE, "application/json")
                .retrieve()
                .toEntity(String.class) 
                .onErrorResume(e -> Mono.just(ResponseEntity.internalServerError()
                        .body("Error communicating with Python service: " + e.getMessage())));
    }
}



package dev.culturiz.hacka_boot.controller;

import dev.culturiz.hacka_boot.model.Answer;
import dev.culturiz.hacka_boot.model.Question;
import dev.culturiz.hacka_boot.service.OpenAIService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/api/openai")
public class OpenAIController {

    @Autowired
    private OpenAIService openAIService;

    @PostMapping
    public Answer getAnswer(@RequestBody Question question) {
        return openAIService.getResult(question);
    }

}
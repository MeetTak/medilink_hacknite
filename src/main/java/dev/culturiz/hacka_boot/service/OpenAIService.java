package dev.culturiz.hacka_boot.service;

import dev.culturiz.hacka_boot.model.Answer;
import dev.culturiz.hacka_boot.model.Question;
import org.springframework.ai.chat.ChatClient;
import org.springframework.ai.chat.ChatResponse;
import org.springframework.ai.chat.prompt.Prompt;
import org.springframework.ai.chat.prompt.PromptTemplate;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class OpenAIService {

    @Autowired
    private ChatClient chatClient;

    public Answer getResult(Question question) {
        PromptTemplate promptTemplate = new PromptTemplate("{{question}}");
        promptTemplate.add("question", question.question());
        Prompt prompt = promptTemplate.create();

        ChatResponse response = chatClient.call(prompt);
        if (response != null && !response.getResults().isEmpty()) {
            return new Answer(response.getResults().get(0).getOutput().getContent());
        }

        return new Answer("No response received!!");
    }
}
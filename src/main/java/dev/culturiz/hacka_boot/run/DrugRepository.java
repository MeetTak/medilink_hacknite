package dev.culturiz.hacka_boot.run;

import java.util.List;
import java.util.Optional;

public interface DrugRepository {

    List<Drug> findAll();

    Optional<Drug> findById(Integer id);

    void create(Drug Drug);

    void update(Drug Drug, Integer id);

    void delete(Integer id);

    int count();

    void saveAll(List<Drug> Drugs);

    List<Drug> findByLocation(String location);
}

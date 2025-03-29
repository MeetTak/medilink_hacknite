package dev.culturiz.hacka_boot.run;

import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/drugs")
public class DrugController {

    private final JdbcDrugRepository drugRepository;

    public DrugController(JdbcDrugRepository drugRepository) {
        this.drugRepository = drugRepository;
    }

    @GetMapping
    public List<Drug> getAllDrugs() {
        return drugRepository.findAll();
    }

    @GetMapping("/{id}")
    public Drug getDrugById(@PathVariable Integer id) {
        return drugRepository.findById(id)
                .orElseThrow(DrugNotFoundException::new);
    }

    @PostMapping
    @ResponseStatus(HttpStatus.CREATED)
    public void createDrug(@RequestBody Drug drug) {
        drugRepository.create(drug);
    }

    @PutMapping("/{id}")
    public void updateDrug(@RequestBody Drug drug, @PathVariable Integer id) {
        drugRepository.update(drug, id);
    }

    @DeleteMapping("/{id}")
    public void deleteDrug(@PathVariable Integer id) {
        drugRepository.delete(id);
    }

    @GetMapping("/condition/{condition}")
    public List<Drug> getDrugsByMedicalCondition(@PathVariable String condition) {
        // This actually searches by medical condition despite the method name
        return drugRepository.findByLocation(condition);
    }

    @GetMapping("/name/{name}")
    public List<Drug> getDrugsByName(@PathVariable String name) {
        return drugRepository.findByDrugName(name);
    }

    @GetMapping("/count")
    public int getDrugCount() {
        return drugRepository.count();
    }
}
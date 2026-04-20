from student_grades import StudentsGrades
from sorting import random_numbers

def main():
    results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])

    print(f"Počet studentů, kteří psali test: {results.count()}")

    for i in range(results.count()):
        points = results.get_by_index(i)
        mark = results.get_grade(i)
        print(f"Student {i}: {points} points – {mark}")

    full_score = results.find(100)
    print(f"Studenti s plným počtem bodů: {full_score}")

    sorted_scores = results.get_sorted()
    print(f"Seřazené výsledky: {sorted_scores}")
    print(f"Původní seznam: {results.scores}")
    
    random_data = random_numbers(30, 0, 100)
    random_results = StudentsGrades(random_data)
    print(f"Náhodný počet studentů: {random_results.count()}")
    print(f"Seřazené výsledky: {random_results.get_sorted()}")

if __name__ == "__main__":
    main()

class StudentsGrades:

    def __init__(self, scores):
        self.scores = scores
        self._sorted_scores = None

    def get_by_index(self, index):
        return self.scores[index]

    def count(self):
        return len(self.scores)


    def get_grade(self, index):
        points = self.get_by_index(index)
        if points > 90:
            znamka = "A"
        elif points < 90 and points > 79:
            znamka = "B"
        elif points < 80 and points > 69:
            znamka = "C"
        elif points < 70 and points > 59:
            znamka = "D"
        elif points < 60 and points > 49:
            znamka = "E"
        elif points < 50:
            znamka = "f"

        return znamka

    def find(self, target_points):  #100
        finds = []
        for i in range(self.count()):
            if self.scores[i] == target_points:
                finds.append(i)
        return finds

    def get_sorted(self):
        rada_numbers = self.scores.copy()
        max_index = len(rada_numbers)

        for i in range(max_index):

            for current_index in range(max_index - 1 - i):
                if rada_numbers[current_index] > rada_numbers[current_index + 1]:
                    rada_numbers[current_index], rada_numbers[current_index + 1] = rada_numbers[current_index + 1], \
                    rada_numbers[current_index]
        return rada_numbers




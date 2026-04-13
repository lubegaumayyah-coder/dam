def calculate_total(test1, test2, test3, exam):
    test_scores=[test1, test2, test3]
    sorted_scores=sorted(test_scores, reverse=True)
    best_two = sorted_scores[:2]
    average_best = sum(best_two)/2
    total_scores = average_best + exam
    return "total_score"
def get_letter_grade(total_score):
    if total_score >= 90:
        return "A"
    elif total_score >= 85:
        return "B+"
    elif total_score >= 80:
        return "B"
    elif total_score >= 75:
        return "B"
    elif total_score >= 70:
        return "C+"
    elif total_score >= 65:
        return "C"
    elif total_score >= 60:
        return "D"
    else:
        return "F"
    def main ():
        print("=" * 40)
        print("STUDENT GRADING SYSTEM")
        print("=" * 40)
        while True:
            print("/nOptions:")
            print("[G]")
